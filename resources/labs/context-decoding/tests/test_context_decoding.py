import sys
from pathlib import Path

LESSON_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(LESSON_DIR))
sys.modules.pop("workbench", None)

from workbench import (
    ContextItem,
    choose_model_strategy,
    decode_next_token,
    estimate_tokens,
    select_context,
    softmax,
)


def test_estimate_tokens_counts_terms_and_handles_blank_text():
    assert estimate_tokens("AAPL revenue improved") == 3
    assert estimate_tokens("   ") == 0


def test_select_context_keeps_high_priority_items_within_budget():
    items = [
        ContextItem("low", "extra market color", 1),
        ContextItem("high", "AAPL revenue improved", 10),
        ContextItem("mid", "margin pressure noted", 5),
    ]

    selection = select_context(items, max_tokens=5)

    assert [item.source_id for item in selection.kept] == ["high", "mid"]
    assert [item.source_id for item in selection.dropped] == ["low"]
    assert selection.token_count == 5


def test_softmax_returns_probabilities_that_sum_to_one():
    probs = softmax([1.0, 2.0, 3.0])

    assert round(sum(probs), 6) == 1.0
    assert probs[-1] > probs[0]


def test_decode_next_token_supports_greedy_and_temperature_modes():
    logits = {"up": 1.0, "flat": 0.2, "down": -1.0}

    assert decode_next_token(logits, mode="greedy") == "up"
    assert decode_next_token(logits, mode="temperature", temperature=0.7) == "up"


def test_choose_model_strategy_explains_tradeoff():
    decision = choose_model_strategy("calculate percentage change", 100, 500)

    assert decision["strategy"] == "deterministic"
    assert "reason" in decision
    assert decision["needs_larger_context"] is False
