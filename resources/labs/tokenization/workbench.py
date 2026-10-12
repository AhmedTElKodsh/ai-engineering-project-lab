"""Tiny byte-pair tokenizer workbench for Module 2 Phase 1.

Expected time to finish: 4-6 hours.

Learners should complete the TODOs using plain Python only.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class TinyTokenizer:
    """A minimal tokenizer state produced by training."""

    merges: list[tuple[int, int]]
    vocabulary: dict[int, tuple[int, ...]]


def text_to_bytes(text: str) -> list[int]:
    """Convert text to UTF-8 byte values."""
    # Hint reference: hints.md#text_to_bytes
    # TODO: Return a list of integer byte values for the input text.
    # Hint: Python strings must become bytes before they can become byte IDs.
    # Check that non-ASCII text can round-trip through bytes_to_text later.
    # Example shape: "A" -> [65].
    return []


def bytes_to_text(byte_values: list[int]) -> str:
    """Convert UTF-8 byte values back into text."""
    # Hint reference: hints.md#bytes_to_text
    # TODO: Reconstruct the original string from integer byte values.
    # Hint: reverse text_to_bytes without assuming one byte equals one character.
    # Example shape: [65] -> "A".
    return ""


def count_adjacent_pairs(tokens: list[int]) -> dict[tuple[int, int], int]:
    """Count how often each adjacent token pair appears."""
    # Hint reference: hints.md#count_adjacent_pairs
    # TODO: Count pairs such as [65, 65, 66] -> {(65, 65): 1, (65, 66): 1}.
    # Hint: adjacent means positions (0, 1), then (1, 2), not every combination.
    # Example shape: [1, 2, 1] -> {(1, 2): 1, (2, 1): 1}.
    return {}


def merge_pair(tokens: list[int], pair: tuple[int, int], new_token_id: int) -> list[int]:
    """Replace every non-overlapping occurrence of pair with new_token_id."""
    # Hint reference: hints.md#merge_pair
    # TODO: Walk left to right and merge non-overlapping pair occurrences.
    # Hint: after you merge a pair, skip both original tokens before continuing.
    # A copied output list is easier to reason about than editing while scanning.
    # Example shape: [1, 2, 1, 2], pair=(1, 2), new=99 -> [99, 99].
    return tokens


def train_bpe(corpus: str, target_vocab_size: int) -> TinyTokenizer:
    """Train a tiny BPE tokenizer on the provided corpus."""
    # Hint reference: hints.md#train_bpe
    # TODO: Start with byte vocabulary, learn the most frequent pair merges,
    # and return TinyTokenizer with merge history and token byte sequences.
    # Hint: each new merge creates one new token ID and one vocabulary entry.
    # Stop when there are no repeated pairs worth merging or the target is met.
    # Example shape: "aa" with room for one merge -> tokenizer.merges has one pair.
    return TinyTokenizer(merges=[], vocabulary={})


def encode(text: str, tokenizer: TinyTokenizer) -> list[int]:
    """Encode text by applying learned merges in training order."""
    # Hint reference: hints.md#encode
    # TODO: Convert text to bytes, then apply each learned merge.
    # Hint: training order matters because later merges may depend on earlier ones.
    # Example shape: learned merge for "AA" should make "AA" shorter than raw bytes.
    return []


def decode(token_ids: list[int], tokenizer: TinyTokenizer) -> str:
    """Decode token IDs back into text."""
    # Hint reference: hints.md#decode
    # TODO: Expand token IDs into byte values using the vocabulary, then decode.
    # Hint: every token ID should map back to one or more original byte values.
    # Example shape: encoded token IDs from encode("A", tokenizer) -> "A".
    return ""


def estimate_token_budget(texts: list[str], tokenizer: TinyTokenizer) -> dict[str, int]:
    """Return token counts for each text snippet.

    FinAgent will later use this kind of boundary check before sending market
    notes or summaries into an LLM context window.
    """
    # Hint reference: hints.md#estimate_token_budget
    # TODO: Map each original text snippet to the length of its encoded tokens.
    # Hint: the dictionary key is the original text; the value is its encoded length.
    # Example shape: ["AAPL", "MSFT"] -> {"AAPL": count, "MSFT": count}.
    return {}


if __name__ == "__main__":
    sample = "AAPL rises after earnings. AAPL guidance improves."
    trained = train_bpe(sample, target_vocab_size=270)
    print(encode("AAPL rises.", trained))
