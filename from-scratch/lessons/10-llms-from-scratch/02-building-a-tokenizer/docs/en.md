# Building a Tokenizer from Scratch

> Preserve every Unicode character, then compress UTF-8 bytes without confusing quoted text with controls.

**Type:** Build
**Languages:** Python
**Prerequisites:** Phase 10, Lesson 01 (Tokenizers: BPE, WordPiece, SentencePiece)
**Time:** ~90 minutes

## Learning Objectives

- Trace a Unicode string through UTF-8 bytes, pre-tokenization, merges, and decoding.
- Build a deterministic byte-BPE tokenizer with standard-library tools.
- Preserve Arabic, CJK, accents, emoji, whitespace, and literal control spellings.
- Separate ordinary text encoding from explicit structural-token insertion.
- Verify normalization, merge ties, invalid IDs, and round-trip boundaries.

## The Problem

An ASCII-only word pattern can silently omit Arabic or Chinese characters. A
256-byte vocabulary cannot recover characters that pre-tokenization discarded.
Likewise, recognizing a control spelling in every input lets quoted ordinary text
acquire structure the caller did not authorize.

This educational implementation fixes both boundaries. It is not compatible with
GPT-2 or any production tokenizer's exact vocabulary/pattern. The historical
ProductionTokenizer class name remains for compatibility; its scope is a small
stdlib byte-BPE reference. Persistence, large-corpus performance, and production
chat-template compatibility need separate implementation and tests.

## The Concept

~~~mermaid
flowchart LR
    A[Unicode text] --> B[Declared normalization]
    B --> C[Exhaustive Unicode chunks]
    C --> D[UTF-8 bytes]
    D --> E[Ordered BPE merges]
    E --> F[Ordinary IDs]
    G[Explicit allowed controls] --> F
~~~

The vocabulary begins with all byte values 0–255. Byte sequences merge within
pre-tokenized chunks. Choose the most frequent adjacent pair; break frequency
ties by the numeric pair. Apply learned merges in their recorded order. This is
an original educational implementation of the merge mechanism described in
[the primary subword paper](https://arxiv.org/abs/1508.07909).

Normalization is a contract. The default is identity, so valid Unicode text
round-trips exactly. Optional NFC/NFKC changes the expected round trip to the
declared normalized text. Arbitrary sampled bytes can be invalid UTF-8; decoding
uses replacement characters. Unknown, negative, non-integer, and boolean IDs are
rejected rather than silently dropped.

## Build It

### Unicode coverage

Python's standard-library re uses Unicode word-character semantics. Use an
exhaustive pattern, including underscores/word characters and whitespace, and
test that joining its matches restores the whole input:

~~~python
import re

PRETOKEN_PATTERN = re.compile(
    r"'(?:[sdmt]|ll|ve|re)| ?[^\W\d_]+| ?\d+| ?[^\s\w]+|\w+|\s+"
)

def pre_tokenize(text):
    return [match.group() for match in PRETOKEN_PATTERN.finditer(text)]
~~~

This pattern is deliberately simpler than production patterns. Combining marks
can form their own chunks but must never disappear. See [Python's official
Unicode regex rules](https://docs.python.org/3/library/re.html).

### Byte vocabulary and deterministic merges

Inspect [the reference implementation](../code/main.py). Every ordinary chunk is
UTF-8 encoded before merges. Training uses a fresh tokenizer before controls are
registered; a negative/non-integer merge count fails. Empty training data retains
the byte baseline. Both training and ordinary encoding exclude reserved control
IDs. Registering a spelling twice returns the same control ID.

### Ordinary text versus controls

The ordinary encode method treats a registered spelling as ordinary bytes by
default. The allowed_special argument recognizes only named registered spellings.
Unknown allowance entries fail; a string is not an allowance collection. A caller
can also deliberately insert a registered ID in a governed sequence builder.
Ordinary retrieved/user text must not receive that permission.

~~~python
tokenizer = ProductionTokenizer()
eos_id = tokenizer.add_special_token("<|end|>")
ordinary = tokenizer.encode("quoted <|end|>")
assert eos_id not in ordinary
assert tokenizer.decode(ordinary) == "quoted <|end|>"
structural = tokenizer.encode("<|end|>", allowed_special={"<|end|>"})
assert structural == [eos_id]
~~~

### Verify the boundary

The tests include Arabic, CJK, composed/decomposed accents, emoji, CRLF,
underscores, empty text, byte fallback, deterministic ties, controls, and invalid
IDs. Declared normalization is tested separately from identity round-trip.

~~~console
python -X utf8 main.py
python -X utf8 -m unittest discover tests -v
~~~

Run from this lesson's code directory with the actual selected interpreter.

## Use It

Use Python's built-in UTF-8 conversion as the independent byte-baseline comparison:

~~~python
text = "مرحبا 你好 café"
baseline_ids = list(text.encode("utf-8"))
assert bytes(baseline_ids).decode("utf-8") == text
~~~

Compare BPE compression on the same text and report vocabulary size and
normalization. A compiled production-tokenizer comparison requires its actual
vocabulary/template and a separately governed workspace. It is deferred here:
**stays stdlib-first for educational clarity**. No regex or tiktoken installation
is needed for the canonical demo.

## Ship It

Use the [tokenizer contract prompt](../outputs/prompt-tokenizer-builder.md) to
review byte coverage, normalization, controls, IDs, and deterministic merges.
It is a checklist, not evidence that a tokenizer is production ready.

## Exercises

- Explain why a full byte vocabulary cannot rescue a lossy pre-tokenizer.
- Add an original Unicode fixture and a regression test.
- Predict an ordinary versus explicitly allowed control encoding.
- Compare identity and NFKC on a small fixture; report the changed contract.
- Design persistence tests as later depth without assuming this reference saves a model.
