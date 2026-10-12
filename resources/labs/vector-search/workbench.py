"""Tiny embedding and retrieval workbench for Module 2 Phase 2.

Expected time to finish: 4-6 hours.

Learners should complete the TODOs using plain Python only.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MarketNote:
    """A source document that FinAgent may retrieve."""

    note_id: str
    ticker: str
    text: str


@dataclass(frozen=True)
class SearchResult:
    """A scored retrieval result."""

    note: MarketNote
    score: float


@dataclass(frozen=True)
class TinyVectorIndex:
    """A deterministic vector index for market notes."""

    vocabulary: list[str]
    notes: list[MarketNote]
    vectors: list[list[float]]


def normalize_terms(text: str) -> list[str]:
    """Lowercase text and return simple alphanumeric terms."""
    # Hint reference: hints.md#normalize_terms
    # TODO: Return lowercase terms such as "AAPL revenue!" -> ["aapl", "revenue"].
    # Hint: decide what counts as a term before counting or scoring anything.
    # Example shape: "AAPL revenue!" -> ["aapl", "revenue"].
    return []


def build_vocabulary(texts: list[str]) -> list[str]:
    """Build a sorted vocabulary from all texts."""
    # Hint reference: hints.md#build_vocabulary
    # TODO: Collect unique normalized terms and return them in sorted order.
    # Hint: use uniqueness for the set of dimensions, then sort for determinism.
    # Example shape: ["MSFT cloud", "MSFT margins"] -> ["cloud", "margins", "msft"].
    return []


def vectorize(text: str, vocabulary: list[str]) -> list[float]:
    """Convert text into a term-frequency vector using the given vocabulary."""
    # Hint reference: hints.md#vectorize
    # TODO: Count each vocabulary term in the normalized text.
    # Hint: the output length should always match len(vocabulary).
    # Example shape: text "aapl aapl", vocabulary ["aapl", "msft"] -> [2.0, 0.0].
    return []


def dot_product(left: list[float], right: list[float]) -> float:
    """Return the dot product of two equal-length vectors."""
    # Hint reference: hints.md#dot_product
    # TODO: Multiply matching positions and sum the products.
    # Hint: matching positions represent the same vocabulary term.
    # Example shape: [1, 2] and [3, 4] -> 11.0.
    return 0.0


def magnitude(vector: list[float]) -> float:
    """Return the Euclidean length of a vector."""
    # Hint reference: hints.md#magnitude
    # TODO: Return sqrt(sum(value squared)).
    # Hint: this is the vector length used to normalize similarity.
    # Example shape: [3, 4] -> 5.0.
    return 0.0


def cosine_similarity(left: list[float], right: list[float]) -> float:
    """Return cosine similarity, or 0.0 when either vector is empty/zero."""
    # Hint reference: hints.md#cosine_similarity
    # TODO: Use dot product divided by both vector magnitudes.
    # Hint: avoid division when either vector has no length.
    # Example shape: identical non-zero vectors -> 1.0.
    return 0.0


def build_index(notes: list[MarketNote]) -> TinyVectorIndex:
    """Build a tiny vector index from market notes."""
    # Hint reference: hints.md#build_index
    # TODO: Build vocabulary from note text and vectorize each note.
    # Hint: index.vectors should line up with index.notes by position.
    # Example shape: two notes in -> two vectors out in the same order.
    return TinyVectorIndex(vocabulary=[], notes=notes, vectors=[])


def search(query: str, index: TinyVectorIndex, top_k: int = 3) -> list[SearchResult]:
    """Return the top matching notes for a query."""
    # Hint reference: hints.md#search
    # TODO: Vectorize query, score every indexed note, sort by score descending,
    # preserve original note order for ties, and return top_k positive results.
    # Hint: keep enough pairing information during sorting to recover the note.
    # Example shape: query "cloud" -> results whose note text shares "cloud" first.
    return []


def build_grounded_context(results: list[SearchResult]) -> str:
    """Format retrieval results as source-grounded context."""
    # Hint reference: hints.md#build_grounded_context
    # TODO: Return one line per result with note ID, ticker, score, and text.
    # Hint: this output is for humans and prompts, so include citation-like IDs.
    # Example shape: one SearchResult -> one grounded context line.
    return ""


if __name__ == "__main__":
    notes = [
        MarketNote("note-1", "AAPL", "AAPL reports stronger iPhone revenue."),
        MarketNote("note-2", "MSFT", "MSFT expands cloud margins."),
        MarketNote("note-3", "TSLA", "TSLA lowers delivery guidance."),
    ]
    index = build_index(notes)
    print(build_grounded_context(search("Apple revenue", index)))
