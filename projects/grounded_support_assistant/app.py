"""Transparent retrieval baseline for the Grounded Support Assistant."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, model_validator

CORPUS_PATH = Path(__file__).with_name("data") / "handbook.md"
REFUSAL = "I cannot answer this from the support handbook."
WORD = re.compile(r"[a-z0-9]+")
STOPWORDS = {
    "a",
    "an",
    "and",
    "are",
    "be",
    "can",
    "do",
    "does",
    "for",
    "from",
    "how",
    "i",
    "in",
    "is",
    "it",
    "my",
    "of",
    "on",
    "the",
    "to",
    "what",
    "when",
    "where",
    "which",
    "who",
}


class SupportQuestion(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    text: str = Field(min_length=3, max_length=500)


class Citation(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    source: str = Field(min_length=1)
    section: str = Field(min_length=1)


class GroundedAnswer(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    question: str = Field(min_length=1)
    answer: str = Field(min_length=1)
    citations: list[Citation]
    abstained: bool

    @model_validator(mode="after")
    def check_result_invariants(self) -> GroundedAnswer:
        if self.abstained and (self.citations or self.answer != REFUSAL):
            raise ValueError("Abstention requires the standard refusal and no citations")
        if not self.abstained and not self.citations:
            raise ValueError("A retrieved answer requires at least one source citation")
        return self


@dataclass(frozen=True)
class Section:
    source: str
    title: str
    body: str


def load_sections(path: Path = CORPUS_PATH) -> list[Section]:
    sections: list[Section] = []
    title: str | None = None
    body: list[str] = []

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if raw_line.startswith("## "):
            if title:
                sections.append(Section(path.name, title, " ".join(body)))
            title, body = raw_line[3:].strip(), []
        elif title and raw_line.strip():
            body.append(raw_line.strip())

    if title:
        sections.append(Section(path.name, title, " ".join(body)))
    if any(not section.title or not section.body for section in sections):
        raise ValueError("Handbook sections require nonblank headings and content")
    if not sections:
        raise ValueError(f"No level-two sections found in {path}")
    return sections


def tokens(text: str) -> set[str]:
    return {token for token in WORD.findall(text.lower()) if token not in STOPWORDS}


def answer_question(question: SupportQuestion, path: Path = CORPUS_PATH) -> GroundedAnswer:
    query_tokens = tokens(question.text)

    sections = load_sections(path)
    # Relevance is not supportedness; measured challenge failures remain visible in evaluation.
    scores = [
        (len(query_tokens & tokens(f"{section.title} {section.body}")), section)
        for section in sections
    ]
    score, best = max(scores, key=lambda item: item[0])

    if score < 2:
        return GroundedAnswer(
            question=question.text,
            answer=REFUSAL,
            citations=[],
            abstained=True,
        )

    return GroundedAnswer(
        question=question.text,
        answer=best.body,
        citations=[Citation(source=best.source, section=best.title)],
        abstained=False,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Query the local support handbook.")
    parser.add_argument("question")
    args = parser.parse_args()
    result = answer_question(SupportQuestion(text=args.question))
    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
