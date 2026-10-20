"""Context window and decoding workbench for Module 2 Phase 4.

Learners should complete the TODOs using plain Python only.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ContextItem:
    source_id: str
    text: str
    priority: int


@dataclass(frozen=True)
class ContextSelection:
    kept: list[ContextItem]
    dropped: list[ContextItem]
    token_count: int


def estimate_tokens(text: str) -> int:
    """Estimate tokens by counting whitespace-separated terms."""

    # TODO: Return 0 for blank text and otherwise count terms.
    # Hint: this is a cheap estimate, so blank and whitespace-only text matter.
    # Example shape: "AAPL rises" -> 2; "   " -> 0.
    return 0


def select_context(items: list[ContextItem], max_tokens: int) -> ContextSelection:
    """Keep highest-priority context items within a token budget."""

    # TODO: Sort by priority descending, preserve source IDs, and split kept/dropped.
    # Hint: keep a running token total; once an item cannot fit, it belongs in dropped.
    # Ties should stay predictable so debugging traces are stable.
    # Example shape: max_tokens too small -> low-priority or oversized items in dropped.
    return ContextSelection([], [], 0)


def softmax(logits: list[float], temperature: float = 1.0) -> list[float]:
    """Convert logits into probabilities."""

    # TODO: Reject temperature <= 0 and use stable softmax.
    # Hint: temperature changes sharpness before exponentiation; stability still matters.
    # Example shape: equal logits -> equal probabilities.
    return []


def decode_next_token(
    logits: dict[str, float], mode: str = "greedy", temperature: float = 1.0
) -> str:
    """Choose the next token deterministically."""

    # TODO: Greedy returns highest logit. Temperature mode returns highest softmax probability.
    # Hint: both modes still return one token string, not the probability table.
    # Example shape: {"up": 2.0, "down": 1.0} in greedy mode -> "up".
    return ""


def choose_model_strategy(
    requirement: str, context_tokens: int, budget_tokens: int
) -> dict[str, object]:
    """Return a model/system strategy decision for a narrow requirement."""

    # TODO: Prefer deterministic code for calculations, RAG for evidence gaps,
    # and larger context only when the token budget is exceeded.
    # Hint: choose based on the requirement text first, then token budget pressure.
    # The returned dict should explain the decision enough for a reviewer.
    # Example shape: calculation request -> deterministic strategy with a reason.
    return {}
