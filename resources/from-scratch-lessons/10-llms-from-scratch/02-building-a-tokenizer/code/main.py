# Lesson: phases/10-llms-from-scratch/02-building-a-tokenizer/docs/en.md
# Educational byte-BPE reference, implemented with Python standard library.
# Source: https://arxiv.org/abs/1508.07909 (subword merge algorithm).
# All valid Unicode text is covered; normalization is an explicit choice.
# Control spellings remain ordinary text unless explicitly allowed by the caller.
import re
import unicodedata
from collections import Counter

# Unicode-aware and exhaustive; this is not the GPT-2 production regex.
PRETOKEN_PATTERN = re.compile(
    r"'(?:[sdmt]|ll|ve|re)| ?[^\W\d_]+| ?\d+| ?[^\s\w]+|\w+|\s+"
)


def pre_tokenize(text):
    return [match.group() for match in PRETOKEN_PATTERN.finditer(text)]


def apply_merge(byte_seq, pair, new_id):
    merged = []
    i = 0
    while i < len(byte_seq):
        if i + 1 < len(byte_seq) and (byte_seq[i], byte_seq[i + 1]) == pair:
            merged.append(new_id)
            i += 2
        else:
            merged.append(byte_seq[i])
            i += 1
    return merged


class SpecialTokenHandler:
    def __init__(self):
        self.special_tokens = {}

    def add_token(self, token_str, token_id):
        self.special_tokens[token_str] = token_id

    def split_with_specials(self, text, allowed_special=()):
        if isinstance(allowed_special, (str, bytes)):
            raise ValueError("allowed_special must be a collection of registered spellings")
        allowed = set(allowed_special)
        if not allowed <= self.special_tokens.keys():
            raise ValueError("allowed_special contains an unregistered control spelling")
        if not allowed:
            return [(text, False)]
        pattern = re.compile("|".join(re.escape(t) for t in sorted(allowed, key=lambda t: (-len(t), t))))
        parts, last_end = [], 0
        for match in pattern.finditer(text):
            if match.start() > last_end:
                parts.append((text[last_end:match.start()], False))
            parts.append((match.group(), True))
            last_end = match.end()
        if last_end < len(text):
            parts.append((text[last_end:], False))
        return parts


class ProductionTokenizer:
    """Historical class name; educational BPE, not production-model compatible.

    Default normalization is identity. NFC/NFKC change the declared round trip.
    Valid Unicode strings encode to UTF-8; arbitrary sampled bytes decode with
    replacement. Invalid token IDs fail rather than disappearing silently.
    """
    def __init__(self, normalization=None):
        if normalization not in {None, "NFC", "NFKC"}:
            raise ValueError("normalization must be None, NFC, or NFKC")
        self.normalization = normalization
        self.merges = {}
        self.vocab = {i: bytes([i]) for i in range(256)}
        self.special_handler = SpecialTokenHandler()
        self.next_id = 256

    def normalize(self, text):
        return unicodedata.normalize(self.normalization, text) if self.normalization else text

    def train(self, text, num_merges):
        if type(num_merges) is not int or num_merges < 0:
            raise ValueError("num_merges must be a non-negative integer")
        if self.merges or self.special_handler.special_tokens:
            raise ValueError("train a fresh tokenizer before registering controls")
        chunks = [list(chunk.encode("utf-8")) for chunk in pre_tokenize(self.normalize(text))]
        for i in range(num_merges):
            pairs = Counter(pair for seq in chunks for pair in zip(seq, seq[1:]))
            if not pairs:
                break
            best = min(pairs, key=lambda pair: (-pairs[pair], pair))
            new_id = self.next_id
            self.next_id += 1
            self.merges[best] = new_id
            self.vocab[new_id] = self.vocab[best[0]] + self.vocab[best[1]]
            chunks = [apply_merge(seq, best, new_id) for seq in chunks]
            print(f"Merge {i + 1}: {best} -> {new_id} = {self.vocab[new_id]}")

    def add_special_token(self, token_str):
        if not isinstance(token_str, str) or not token_str or self.normalize(token_str) != token_str:
            raise ValueError("a control spelling must be non-empty and unchanged by normalization")
        if token_str in self.special_handler.special_tokens:
            return self.special_handler.special_tokens[token_str]
        token_id = self.next_id
        self.next_id += 1
        self.special_handler.add_token(token_str, token_id)
        self.vocab[token_id] = token_str.encode("utf-8")
        return token_id

    def encode(self, text, *, allowed_special=()):
        all_ids = []
        for part_text, is_special in self.special_handler.split_with_specials(self.normalize(text), allowed_special):
            if is_special:
                all_ids.append(self.special_handler.special_tokens[part_text])
            else:
                for chunk in pre_tokenize(part_text):
                    seq = list(chunk.encode("utf-8"))
                    for pair, new_id in self.merges.items():
                        seq = apply_merge(seq, pair, new_id)
                    all_ids.extend(seq)
        return all_ids

    def get_token_bytes(self, token_id):
        if type(token_id) is not int or token_id not in self.vocab:
            raise ValueError(f"invalid token ID: {token_id!r}")
        return self.vocab[token_id]

    def decode(self, ids):
        return b"".join(self.get_token_bytes(token_id) for token_id in ids).decode("utf-8", errors="replace")

    def vocab_size(self):
        return len(self.vocab)


def demo():
    print("Educational stdlib byte-BPE; identity normalization; explicit controls")
    tokenizer = ProductionTokenizer()
    tokenizer.train("Python teaches. مرحبا بالعالم. café 你好 Python teaches.", 12)
    control = tokenizer.add_special_token("<|end|>")
    for text in ("مرحبا", "你好", "café", "Arabic عربي 中文 🙂 _42\r\n", "", "<|end|>"):
        ids = tokenizer.encode(text)
        restored = tokenizer.decode(ids)
        assert restored == text
        assert control not in ids
        print(f"Input={text!r}; IDs={ids}; round-trip=PASS")
    print(f"Explicit control opt-in: {tokenizer.encode('<|end|>', allowed_special={'<|end|>'})}")
    print("Compiled-tokenizer comparison deferred: stays stdlib-first for educational clarity.")


if __name__ == "__main__":
    demo()
