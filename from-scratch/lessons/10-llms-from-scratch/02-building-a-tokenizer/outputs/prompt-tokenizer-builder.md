---
name: prompt-tokenizer-builder
description: Review an educational stdlib byte-BPE tokenizer contract
version: 1.1.0
phase: 10
lesson: 2
tags: [tokenizer, bpe, byte-level, special-tokens, multilingual]
---

# Educational Tokenizer Contract

1. Declare identity, NFC, or NFKC normalization. Default identity preserves valid Unicode exactly; normalized round-trip uses the declared normalized text.
2. Verify exhaustive chunks: joining them preserves Arabic, CJK, combining marks, emoji, underscores, whitespace, and CRLF.
3. Keep all 256 ordinary byte IDs. Use deterministic numeric-pair tie breaks; controls do not enter merges.
4. Literal registered control spellings remain ordinary text unless the caller explicitly names them in allowed_special. Retrieved/user text must not acquire that permission.
5. Reject unknown/negative/non-integer IDs. State replacement decoding for invalid generated UTF-8.
6. Run stdlib tests and record the actual command/revision. The historical ProductionTokenizer name does not claim production compatibility.
7. Add persistence tests separately if persistence is implemented; this reference does not save/load a model or reproduce a production vocabulary/template.

Compiled comparisons require a separately governed workspace and are deferred here: **stays stdlib-first for educational clarity**. Do not install regex or tiktoken to repair missing characters. Use a tiny permitted corpus. Compression, explanation, independent construction, and retention remain distinct evidence.
