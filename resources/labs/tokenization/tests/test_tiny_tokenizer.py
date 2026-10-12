import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
sys.modules.pop("workbench", None)

from workbench import (
    TinyTokenizer,
    bytes_to_text,
    count_adjacent_pairs,
    decode,
    encode,
    estimate_token_budget,
    merge_pair,
    text_to_bytes,
    train_bpe,
)


def test_text_to_bytes_uses_utf8_integer_values():
    assert text_to_bytes("AAPL") == [65, 65, 80, 76]
    assert text_to_bytes("cafe") == [99, 97, 102, 101]
    assert text_to_bytes("cafe!")[-1] == 33


def test_bytes_to_text_reconstructs_unicode_text():
    original = "NVDA beats estimates!"
    assert bytes_to_text(text_to_bytes(original)) == original


def test_count_adjacent_pairs_counts_every_neighbor():
    tokens = [65, 65, 80, 76, 65, 65]

    counts = count_adjacent_pairs(tokens)

    assert counts[(65, 65)] == 2
    assert counts[(65, 80)] == 1
    assert counts[(80, 76)] == 1
    assert counts[(76, 65)] == 1


def test_merge_pair_replaces_non_overlapping_pairs_left_to_right():
    tokens = [65, 65, 65, 80, 65, 65]

    merged = merge_pair(tokens, (65, 65), 256)

    assert merged == [256, 65, 80, 256]


def test_train_bpe_records_merges_and_vocabulary_entries():
    tokenizer = train_bpe("AAPL AAPL MSFT", target_vocab_size=260)

    assert isinstance(tokenizer, TinyTokenizer)
    assert tokenizer.merges
    assert len(tokenizer.vocabulary) >= 260
    assert all(token_id in tokenizer.vocabulary for token_id in range(256))


def test_encode_applies_learned_merges_in_order():
    tokenizer = TinyTokenizer(
        merges=[(65, 65), (256, 80)],
        vocabulary={
            **{i: (i,) for i in range(256)},
            256: (65, 65),
            257: (65, 65, 80),
        },
    )

    assert encode("AAP", tokenizer) == [257]
    assert encode("AAPL", tokenizer) == [257, 76]


def test_decode_reconstructs_text_from_base_and_merged_tokens():
    tokenizer = TinyTokenizer(
        merges=[(65, 65), (256, 80)],
        vocabulary={
            **{i: (i,) for i in range(256)},
            256: (65, 65),
            257: (65, 65, 80),
        },
    )

    assert decode([257, 76], tokenizer) == "AAPL"


def test_training_round_trip_preserves_market_text():
    corpus = "AAPL rises after earnings. MSFT falls after guidance."
    tokenizer = train_bpe(corpus, target_vocab_size=265)

    text = "AAPL falls after guidance."

    assert decode(encode(text, tokenizer), tokenizer) == text


def test_estimate_token_budget_counts_each_original_text():
    tokenizer = train_bpe("AAPL AAPL MSFT MSFT earnings guidance", target_vocab_size=262)
    texts = [
        "AAPL earnings",
        "MSFT guidance",
        "AAPL earnings guidance",
    ]

    budget = estimate_token_budget(texts, tokenizer)

    assert set(budget) == set(texts)
    assert budget["AAPL earnings"] > 0
    assert budget["AAPL earnings guidance"] >= budget["AAPL earnings"]
