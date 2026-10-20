"""Scaled dot-product attention workbench for Module 2 Phase 3.

Expected time to finish: 4-6 hours.

Learners should complete the TODOs using plain Python only.
"""

from __future__ import annotations

from dataclasses import dataclass

Vector = list[float]
Matrix = list[Vector]


@dataclass(frozen=True)
class AttentionSource:
    """A named context item that can receive attention."""

    source_id: str
    ticker: str
    text: str


@dataclass(frozen=True)
class AttentionResult:
    """Attention output plus inspectable source weights."""

    output: Vector
    weights: list[float]
    sources: list[AttentionSource]


def dot_product(left: Vector, right: Vector) -> float:
    """Return the dot product of two equal-length vectors."""

    # TODO: Validate matching lengths, multiply matching positions, and sum.
    # Hint: a shape mismatch is a data bug; fail before doing partial math.
    # Example shape: [1, 2] and [3, 4] -> 11.0.
    return 0.0


def scale_scores(scores: list[float], dimension: int) -> list[float]:
    """Scale scores by sqrt(dimension)."""

    # TODO: Divide each score by sqrt(dimension). Reject non-positive dimensions.
    # Hint: the same scale factor applies to every score for this query.
    # Example shape: scores [2.0], dimension 4 -> [1.0].
    return []


def softmax(scores: list[float]) -> list[float]:
    """Convert scores into positive weights that sum to 1."""

    # TODO: Implement stable softmax by subtracting the max score first.
    # Hint: subtracting the max changes numerical stability, not the ranking.
    # Example shape: [1.0, 1.0] -> two equal probabilities.
    return []


def weighted_sum(weights: list[float], values: Matrix) -> Vector:
    """Blend value vectors using attention weights."""

    # TODO: Return the weighted sum across all value vectors.
    # Hint: each output dimension is built from that same dimension in every value.
    # Example shape: weights [1.0], values [[3.0, 4.0]] -> [3.0, 4.0].
    return []


def attention(
    query: Vector,
    keys: Matrix,
    values: Matrix,
    sources: list[AttentionSource],
) -> AttentionResult:
    """Run scaled dot-product attention for one query over many sources."""

    # TODO: Validate aligned inputs, score query against keys, scale, softmax,
    # blend values, and return AttentionResult.
    # Hint: keys, values, and sources are parallel lists; their lengths must agree.
    # Build the result in the same order: score -> scale -> weights -> output.
    # Example shape: one key/value/source -> one weight and one blended output vector.
    return AttentionResult(output=[], weights=[], sources=sources)


def most_attended_source(result: AttentionResult) -> AttentionSource | None:
    """Return the source with the highest attention weight."""

    # TODO: Return None when there are no weights or sources.
    # Hint: the winning weight's index points to the winning source.
    # Example shape: weights [0.2, 0.8] -> second source.
    return None


def explain_attention(result: AttentionResult) -> str:
    """Create a short debugging explanation for FinAgent."""

    # TODO: Include the top source ID, ticker, and weight rounded to two decimals.
    # Hint: call the helper that finds the top source instead of duplicating it.
    # Example shape: top AAPL source at 0.82 -> text names AAPL and 0.82.
    return ""


if __name__ == "__main__":
    sources = [
        AttentionSource("note-1", "AAPL", "AAPL revenue improved."),
        AttentionSource("note-2", "MSFT", "MSFT cloud margins expanded."),
        AttentionSource("note-3", "TSLA", "TSLA deliveries fell."),
    ]
    query = [1.0, 0.0]
    keys = [[1.0, 0.0], [0.2, 0.8], [0.0, 1.0]]
    values = [[10.0, 1.0], [2.0, 8.0], [1.0, 9.0]]
    print(explain_attention(attention(query, keys, values, sources)))
