import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from projects.grounded_support_assistant.app import (
    REFUSAL,
    Citation,
    GroundedAnswer,
    SupportQuestion,
    answer_question,
    load_sections,
)

CASES = json.loads((Path(__file__).with_name("eval") / "cases.json").read_text(encoding="utf-8"))
PARAMS = [
    pytest.param(
        case,
        id=case["id"],
        marks=pytest.mark.xfail(reason=case["known_failure"], strict=True, raises=AssertionError),
    )
    if "known_failure" in case
    else pytest.param(case, id=case["id"])
    for case in CASES
]


@pytest.mark.parametrize("case", PARAMS)
def test_fixed_evaluation(case: dict[str, object]) -> None:
    result = answer_question(SupportQuestion(text=str(case["question"])))

    assert result.abstained is case["abstained"]
    sections = [citation.section for citation in result.citations]
    assert sections == ([] if case["section"] is None else [case["section"]])
    if result.abstained:
        assert result.answer == "I cannot answer this from the support handbook."
    else:
        for fact in case["answer_contains"]:
            assert str(fact).casefold() in result.answer.casefold()


def test_question_contract_rejects_blank_input() -> None:
    with pytest.raises(ValidationError):
        SupportQuestion(text="  ")


def test_answer_contract_rejects_unknown_fields() -> None:
    with pytest.raises(ValidationError):
        GroundedAnswer(
            question="Known?",
            answer="Known.",
            citations=[],
            abstained=False,
            confidence=1.0,
        )


@pytest.mark.parametrize(
    "fields",
    [
        {"answer": "", "citations": [], "abstained": False},
        {"answer": "Text.", "citations": [], "abstained": False},
        {"answer": "Unapproved claim.", "citations": [], "abstained": True},
        {"answer": REFUSAL, "citations": [{"source": "a", "section": "b"}], "abstained": True},
    ],
)
def test_result_rejects_contradictory_states(fields: dict) -> None:
    with pytest.raises(ValidationError):
        GroundedAnswer(question="Question?", **fields)


def test_citation_rejects_blank_source() -> None:
    with pytest.raises(ValidationError):
        Citation(source="  ", section="Known")


def test_empty_handbook_section_is_rejected(tmp_path: Path) -> None:
    corpus = tmp_path / "handbook.md"
    corpus.write_text("## Empty\n", encoding="utf-8")
    with pytest.raises(ValueError, match="nonblank"):
        load_sections(corpus)


@pytest.mark.parametrize("question", ["كيف أغير كلمة المرور؟", "...", "the and what"])
def test_no_english_query_terms_abstain(question: str) -> None:
    result = answer_question(SupportQuestion(text=question))
    assert result.abstained and result.answer == REFUSAL and not result.citations


CHALLENGES = json.loads((Path(__file__).with_name("eval") / "challenges.json").read_text())


@pytest.mark.parametrize(
    "case",
    [
        pytest.param(
            case,
            id=case["id"],
            marks=pytest.mark.xfail(reason=case["reason"], strict=True, raises=AssertionError),
        )
        for case in CHALLENGES
    ],
)
def test_review_challenges_remain_visible(case: dict) -> None:
    result = answer_question(SupportQuestion(text=case["question"]))
    assert result.abstained is case["abstained"]
    for fact in case.get("required_facts", []):
        assert fact.casefold() in result.answer.casefold()
