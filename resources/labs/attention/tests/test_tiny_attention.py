import math
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.modules.pop("workbench", None)

from workbench import (
    AttentionResult,
    AttentionSource,
    attention,
    dot_product,
    explain_attention,
    most_attended_source,
    scale_scores,
    softmax,
    weighted_sum,
)


def sample_sources():
    return [
        AttentionSource("note-1", "AAPL", "AAPL revenue improved."),
        AttentionSource("note-2", "MSFT", "MSFT cloud margins expanded."),
        AttentionSource("note-3", "TSLA", "TSLA deliveries fell."),
    ]


def test_dot_product_multiplies_matching_positions():
    assert dot_product([1.0, 2.0, 3.0], [4.0, 0.5, 2.0]) == 11.0


def test_dot_product_rejects_mismatched_dimensions():
    try:
        dot_product([1.0, 2.0], [1.0])
    except ValueError as error:
        assert "same length" in str(error)
    else:
        raise AssertionError("dot_product should reject mismatched dimensions")


def test_scale_scores_divides_by_square_root_dimension():
    scaled = scale_scores([2.0, 4.0], dimension=4)

    assert scaled == [1.0, 2.0]


def test_softmax_returns_weights_that_sum_to_one():
    weights = softmax([1.0, 2.0, 3.0])

    assert len(weights) == 3
    assert math.isclose(sum(weights), 1.0, rel_tol=1e-9)
    assert weights[2] > weights[1] > weights[0]


def test_softmax_handles_empty_scores():
    assert softmax([]) == []


def test_weighted_sum_blends_value_vectors():
    output = weighted_sum(
        weights=[0.25, 0.75],
        values=[
            [4.0, 0.0],
            [0.0, 8.0],
        ],
    )

    assert output == [1.0, 6.0]


def test_attention_scores_query_against_keys_and_blends_values():
    sources = sample_sources()
    query = [1.0, 0.0]
    keys = [[1.0, 0.0], [0.2, 0.8], [0.0, 1.0]]
    values = [[10.0, 1.0], [2.0, 8.0], [1.0, 9.0]]

    result = attention(query, keys, values, sources)

    assert isinstance(result, AttentionResult)
    assert result.sources == sources
    assert len(result.weights) == 3
    assert math.isclose(sum(result.weights), 1.0, rel_tol=1e-9)
    assert result.weights[0] > result.weights[1] > result.weights[2]
    assert len(result.output) == 2


def test_attention_rejects_unaligned_inputs():
    try:
        attention(
            query=[1.0, 0.0],
            keys=[[1.0, 0.0]],
            values=[[1.0, 0.0], [0.0, 1.0]],
            sources=sample_sources()[:1],
        )
    except ValueError as error:
        assert "same number" in str(error)
    else:
        raise AssertionError("attention should reject unaligned keys, values, and sources")


def test_most_attended_source_returns_highest_weight_source():
    result = AttentionResult(
        output=[1.0, 2.0],
        weights=[0.2, 0.7, 0.1],
        sources=sample_sources(),
    )

    assert most_attended_source(result).source_id == "note-2"


def test_most_attended_source_returns_none_for_empty_result():
    assert most_attended_source(AttentionResult(output=[], weights=[], sources=[])) is None


def test_explain_attention_names_source_ticker_and_weight():
    result = AttentionResult(
        output=[1.0, 2.0],
        weights=[0.8123, 0.1, 0.0877],
        sources=sample_sources(),
    )

    explanation = explain_attention(result)

    assert "note-1" in explanation
    assert "AAPL" in explanation
    assert "0.81" in explanation
