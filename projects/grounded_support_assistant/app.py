"""Transparent retrieval baseline for the Grounded Support Assistant."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field

CORPUS_PATH = Path(__file__).with_name("data") / "handbook.md"
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
    model_config = ConfigDict(extra="forbid")

    source: str
    section: str


class GroundedAnswer(BaseModel):
    model_config = ConfigDict(extra="forbid")

    question: str
    answer: str
    citations: list[Citation]
    abstained: bool


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
    if not sections:
        raise ValueError(f"No level-two sections found in {path}")
    return sections


def tokens(text: str) -> set[str]:
    return {token for token in WORD.findall(text.lower()) if token not in STOPWORDS}


def answer_question(question: SupportQuestion, path: Path = CORPUS_PATH) -> GroundedAnswer:
    query_tokens = tokens(question.text)
    if not query_tokens:
        raise ValueError("Question must contain a searchable term")

    sections = load_sections(path)
    # ponytail: exact-token overlap is the baseline ceiling; replace it after measured failures.
    scores = [
        (len(query_tokens & tokens(f"{section.title} {section.body}")), section)
        for section in sections
    ]
    score, best = max(scores, key=lambda item: item[0])

    if score < 2:
        return GroundedAnswer(
            question=question.text,
            answer="I cannot answer this from the support handbook.",
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
