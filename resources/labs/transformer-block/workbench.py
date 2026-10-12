"""Tiny transformer block workbench for Module 2 Phase 4.

Expected time to finish: 5-7 hours.

Learners should complete the TODOs using plain Python only.
"""

from __future__ import annotations

from dataclasses import dataclass

Vector = list[float]
Matrix = list[Vector]


@dataclass(frozen=True)
class TransformerResult:
    """Final block outputs plus inspectable trace metadata."""

    outputs: Matrix
    trace: dict[str, object]


def add_vectors(left: Vector, right: Vector) -> Vector:
    """Add two equal-length vectors."""
    # TODO: Validate that both vectors have the same length, then add
    # matching positions.
    return []


def layer_norm(vector: Vector, epsilon: float = 1e-6) -> Vector:
    """Return a centered, scaled version of one vector."""
    # TODO: Center values by their mean, divide by the standard deviation,
    # and keep all-equal vectors numerically stable.
    return []


def lookup_embeddings(token_ids: list[int], embedding_table: dict[int, Vector]) -> Matrix:
    """Map token IDs to vectors while preserving token order."""
    # TODO: Return one copied embedding vector for each token ID. Raise a
    # helpful KeyError when a token ID is missing.
    return []


def project_vector(vector: Vector, matrix: Matrix) -> Vector:
    """Project one vector through a small plain-Python matrix."""
    # TODO: Treat each row in matrix as one output dimension and compute dot
    # products against the input vector.
    return []


def project_sequence(vectors: Matrix, matrix: Matrix) -> Matrix:
    """Project every vector in a sequence with the same matrix."""
    # TODO: Call project_vector for each vector and preserve sequence order.
    return []


def dot_product(left: Vector, right: Vector) -> float:
    """Return the dot product of two equal-length vectors."""
    # TODO: Reuse the same dimension discipline as add_vectors.
    return 0.0


def softmax(scores: list[float]) -> list[float]:
    """Convert scores into positive weights that sum to 1."""
    # TODO: Use a stable softmax by subtracting the largest score first.
    return []


def weighted_sum(weights: list[float], values: Matrix) -> Vector:
    """Blend value vectors using attention weights."""
    # TODO: Validate that weights and values align, then return the weighted
    # sum across all value vectors.
    return []


def self_attention(
    vectors: Matrix, projection_matrices: dict[str, Matrix]
) -> tuple[Matrix, list[list[float]]]:
    """Run tiny scaled dot-product self-attention over a sequence."""
    # TODO: Build queries, keys, and values, then return one contextual vector
    # and one attention-weight row per input token.
    return [], []


def feed_forward(vector: Vector, weights: Matrix, bias: Vector) -> Vector:
    """Apply a small deterministic feed-forward step."""
    # TODO: Project the vector and add bias. Keep dimensions explicit.
    return []


def transformer_block(
    token_ids: list[int],
    embedding_table: dict[int, Vector],
    projection_matrices: dict[str, Matrix],
    feed_forward_weights: Matrix,
    feed_forward_bias: Vector,
) -> TransformerResult:
    """Run a tiny transformer-style block and return outputs plus trace."""
    # TODO: Lookup embeddings, run self-attention, add residuals, normalize,
    # feed forward, and return trace metadata for debugging.
    return TransformerResult(outputs=[], trace={})


if __name__ == "__main__":
    sample_embeddings = {
        1: [1.0, 0.0],
        2: [0.5, 0.5],
        3: [0.0, 1.0],
    }
    identity = [[1.0, 0.0], [0.0, 1.0]]
    projections = {"query": identity, "key": identity, "value": identity}
    result = transformer_block(
        token_ids=[1, 2, 3],
        embedding_table=sample_embeddings,
        projection_matrices=projections,
        feed_forward_weights=identity,
        feed_forward_bias=[0.0, 0.0],
    )
    print(result)
