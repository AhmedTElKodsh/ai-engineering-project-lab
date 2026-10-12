import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.modules.pop("workbench", None)

from workbench import (
    MarketNote,
    SearchResult,
    TinyVectorIndex,
    build_grounded_context,
    build_index,
    build_vocabulary,
    cosine_similarity,
    dot_product,
    magnitude,
    normalize_terms,
    search,
    vectorize,
)


def sample_notes():
    return [
        MarketNote("note-1", "AAPL", "AAPL reports stronger iPhone revenue."),
        MarketNote("note-2", "MSFT", "MSFT expands cloud margins."),
        MarketNote("note-3", "TSLA", "TSLA lowers delivery guidance."),
    ]


def test_normalize_terms_lowercases_and_removes_punctuation():
    assert normalize_terms("AAPL revenue, revenue!") == ["aapl", "revenue", "revenue"]
    assert normalize_terms("Cloud-margin expands.") == ["cloud", "margin", "expands"]


def test_build_vocabulary_returns_sorted_unique_terms():
    vocabulary = build_vocabulary(["AAPL revenue", "MSFT revenue cloud"])

    assert vocabulary == ["aapl", "cloud", "msft", "revenue"]


def test_vectorize_counts_terms_in_vocabulary_order():
    vocabulary = ["aapl", "cloud", "revenue"]

    vector = vectorize("AAPL revenue revenue", vocabulary)

    assert vector == [1.0, 0.0, 2.0]


def test_dot_product_multiplies_matching_positions():
    assert dot_product([1.0, 2.0, 3.0], [4.0, 0.5, 2.0]) == 11.0


def test_magnitude_uses_euclidean_length():
    assert magnitude([3.0, 4.0]) == 5.0
    assert magnitude([0.0, 0.0]) == 0.0


def test_cosine_similarity_handles_related_and_zero_vectors():
    assert cosine_similarity([1.0, 0.0], [1.0, 0.0]) == 1.0
    assert cosine_similarity([1.0, 0.0], [0.0, 1.0]) == 0.0
    assert cosine_similarity([0.0, 0.0], [1.0, 0.0]) == 0.0


def test_build_index_stores_vocabulary_notes_and_vectors():
    notes = sample_notes()

    index = build_index(notes)

    assert isinstance(index, TinyVectorIndex)
    assert index.notes == notes
    assert "aapl" in index.vocabulary
    assert "revenue" in index.vocabulary
    assert len(index.vectors) == len(notes)
    assert all(len(vector) == len(index.vocabulary) for vector in index.vectors)


def test_search_returns_highest_scoring_relevant_note_first():
    index = build_index(sample_notes())

    results = search("AAPL revenue", index, top_k=2)

    assert len(results) == 1
    assert isinstance(results[0], SearchResult)
    assert results[0].note.note_id == "note-1"
    assert results[0].score > 0


def test_search_preserves_document_order_when_scores_tie():
    notes = [
        MarketNote("note-1", "AAPL", "AAPL revenue"),
        MarketNote("note-2", "MSFT", "MSFT revenue"),
    ]
    index = build_index(notes)

    results = search("revenue", index, top_k=2)

    assert [result.note.note_id for result in results] == ["note-1", "note-2"]


def test_search_returns_empty_list_for_no_positive_matches():
    index = build_index(sample_notes())

    assert search("semiconductor inventory", index, top_k=3) == []


def test_build_grounded_context_formats_sources_for_finagent():
    result = SearchResult(
        note=MarketNote("note-1", "AAPL", "AAPL reports stronger iPhone revenue."),
        score=0.75,
    )

    context = build_grounded_context([result])

    assert "[note-1]" in context
    assert "AAPL" in context
    assert "score=0.75" in context
    assert "AAPL reports stronger iPhone revenue." in context
