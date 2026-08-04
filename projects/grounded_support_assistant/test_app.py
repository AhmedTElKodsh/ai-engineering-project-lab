import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from projects.grounded_support_assistant.app import GroundedAnswer, SupportQuestion, answer_question

CASES = json.loads((Path(__file__).with_name("eval") / "cases.json").read_text(encoding="utf-8"))
PARAMS = [
    pytest.param(
        case,
        id=case["id"],
        marks=pytest.mark.xfail(reason=case["known_failure"], strict=True),
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
