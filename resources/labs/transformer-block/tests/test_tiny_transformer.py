import math
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.modules.pop("workbench", None)

from workbench import (
    TransformerResult,
    add_vectors,
    dot_product,
    feed_forward,
    layer_norm,
    lookup_embeddings,
    project_sequence,
    project_vector,
    self_attention,
    softmax,
    transformer_block,
    weighted_sum,
)


def sample_embedding_table():
    return {
        10: [1.0, 0.0],
        20: [0.5, 0.5],
        30: [0.0, 1.0],
    }


def identity_matrix():
    return [[1.0, 0.0], [0.0, 1.0]]


def sample_projection_matrices():
    return {
        "query": identity_matrix(),
        "key": identity_matrix(),
        "value": identity_matrix(),
    }


def test_add_vectors_adds_matching_positions():
    assert add_vectors([1.0, 2.0], [3.0, 4.0]) == [4.0, 6.0]


def test_add_vectors_rejects_mismatched_dimensions():
    try:
        add_vectors([1.0, 2.0], [1.0])
    except ValueError as error:
        assert "same length" in str(error)
    else:
        raise AssertionError("add_vectors should reject mismatched dimensions")


def test_layer_norm_centers_values_stably():
    normalized = layer_norm([1.0, 2.0, 3.0])

    assert len(normalized) == 3
    assert math.isclose(sum(normalized), 0.0, abs_tol=1e-6)
    assert normalized[0] < normalized[1] < normalized[2]


def test_layer_norm_handles_all_equal_values():
    assert layer_norm([5.0, 5.0, 5.0]) == [0.0, 0.0, 0.0]


def test_lookup_embeddings_preserves_token_order_and_copies_vectors():
    embeddings = lookup_embeddings([30, 10, 20], sample_embedding_table())

    assert embeddings == [[0.0, 1.0], [1.0, 0.0], [0.5, 0.5]]
    embeddings[0][0] = 99.0
    assert sample_embedding_table()[30] == [0.0, 1.0]


def test_lookup_embeddings_reports_missing_token_id():
    try:
        lookup_embeddings([10, 99], sample_embedding_table())
    except KeyError as error:
        assert "99" in str(error)
    else:
        raise AssertionError("lookup_embeddings should reject missing token IDs")


def test_project_vector_uses_matrix_rows_as_output_dimensions():
    matrix = [
        [1.0, 0.0],
        [0.5, 0.5],
        [0.0, 1.0],
    ]

    assert project_vector([2.0, 4.0], matrix) == [2.0, 3.0, 4.0]


def test_project_vector_rejects_wrong_matrix_width():
    try:
        project_vector([1.0, 2.0], [[1.0, 0.0], [1.0]])
    except ValueError as error:
        assert "same length" in str(error)
    else:
        raise AssertionError("project_vector should reject rows with the wrong width")


def test_project_sequence_preserves_sequence_order():
    assert project_sequence([[1.0, 0.0], [0.0, 1.0]], identity_matrix()) == [
        [1.0, 0.0],
        [0.0, 1.0],
    ]


def test_dot_product_multiplies_matching_positions():
    assert dot_product([1.0, 2.0, 3.0], [4.0, 0.5, -1.0]) == 2.0


def test_dot_product_rejects_mismatched_dimensions():
    try:
        dot_product([1.0, 2.0], [1.0])
    except ValueError as error:
        assert "same length" in str(error)
    else:
        raise AssertionError("dot_product should reject vectors with different lengths")


def test_softmax_returns_positive_weights_that_sum_to_one():
    weights = softmax([1.0, 2.0, 3.0])

    assert len(weights) == 3
    assert all(weight > 0 for weight in weights)
    assert math.isclose(sum(weights), 1.0, rel_tol=1e-9)
    assert weights[2] > weights[1] > weights[0]


def test_softmax_handles_large_logits_stably():
    weights = softmax([1000.0, 1001.0, 1002.0])

    assert math.isclose(sum(weights), 1.0, rel_tol=1e-9)
    assert weights[2] > weights[0]


def test_weighted_sum_blends_value_vectors():
    assert weighted_sum([0.25, 0.75], [[2.0, 0.0], [0.0, 4.0]]) == [0.5, 3.0]


def test_weighted_sum_rejects_mismatched_weight_count():
    try:
        weighted_sum([1.0], [[1.0, 0.0], [0.0, 1.0]])
    except ValueError as error:
        assert "weights" in str(error)
    else:
        raise AssertionError("weighted_sum should reject weights that do not align to values")


def test_self_attention_returns_contextual_vector_per_token():
    vectors = [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]]

    outputs, weights = self_attention(vectors, sample_projection_matrices())

    assert len(outputs) == 3
    assert len(weights) == 3
    assert all(len(output) == 2 for output in outputs)
    assert all(math.isclose(sum(row), 1.0, rel_tol=1e-9) for row in weights)
    assert weights[0][0] > weights[0][2]
    assert weights[2][2] > weights[2][0]


def test_feed_forward_projects_then_adds_bias():
    weights = [[1.0, 0.0], [0.5, 0.5]]
    bias = [0.25, -0.25]

    assert feed_forward([2.0, 4.0], weights, bias) == [2.25, 2.75]


def test_transformer_block_returns_outputs_and_trace():
    result = transformer_block(
        token_ids=[10, 20, 30],
        embedding_table=sample_embedding_table(),
        projection_matrices=sample_projection_matrices(),
        feed_forward_weights=identity_matrix(),
        feed_forward_bias=[0.0, 0.0],
    )

    assert isinstance(result, TransformerResult)
    assert len(result.outputs) == 3
    assert all(len(output) == 2 for output in result.outputs)
    assert result.trace["token_ids"] == [10, 20, 30]
    assert result.trace["embedding_shape"] == (3, 2)
    assert result.trace["attention_shape"] == (3, 2)
    assert result.trace["output_shape"] == (3, 2)
    assert "attention_weights" in result.trace
    assert "normalized_vectors" in result.trace


def test_transformer_block_handles_empty_token_sequence_with_trace():
    result = transformer_block(
        token_ids=[],
        embedding_table=sample_embedding_table(),
        projection_matrices=sample_projection_matrices(),
        feed_forward_weights=identity_matrix(),
        feed_forward_bias=[0.0, 0.0],
    )

    assert result.outputs == []
    assert result.trace["token_ids"] == []
    assert result.trace["output_shape"] == (0, 0)
