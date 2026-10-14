"""Coverage, deterministic merging, and explicit control-token contracts."""
import contextlib
import importlib.util
import io
import unittest
import unicodedata
from pathlib import Path

spec = importlib.util.spec_from_file_location("byte_bpe_reference", Path(__file__).resolve().parents[1] / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TokenizerTests(unittest.TestCase):
    def tokenizer(self, normalization=None):
        tok = module.ProductionTokenizer(normalization)
        with contextlib.redirect_stdout(io.StringIO()):
            tok.train("مرحبا بالعالم café 中文 🙂 Python Python\r\n", 15)
        return tok

    def test_pretokenization_preserves_every_unicode_character(self):
        for text in ("مرحبا", "你好", "café", "e\u0301 _x １２\t\n", "\x00\x01", "🙂👩‍💻"):
            with self.subTest(text=text):
                self.assertEqual("".join(module.pre_tokenize(text)), text)

    def test_arabic_and_chinese_round_trip(self):
        tok = self.tokenizer()
        for text in ("مرحبا بالعالم", "你好世界", "café"):
            self.assertEqual(tok.decode(tok.encode(text)), text)

    def test_mixed_unicode_crlf_and_empty_round_trip(self):
        tok = self.tokenizer()
        for text in ("عربي 中文 English 🙂\r\n\t _42", "", "e\u0301"):
            self.assertEqual(tok.decode(tok.encode(text)), text)

    def test_byte_baseline_covers_utf8_without_training(self):
        tok = module.ProductionTokenizer()
        text = "عربي你好"
        self.assertEqual(tok.encode(text), list(text.encode("utf-8")))
        self.assertEqual(len(tok.vocab), 256)

    def test_literal_control_spelling_is_ordinary_by_default(self):
        tok = self.tokenizer()
        control = tok.add_special_token("<|end|>")
        ids = tok.encode("quoted <|end|> حرف")
        self.assertNotIn(control, ids)
        self.assertEqual(tok.decode(ids), "quoted <|end|> حرف")

    def test_control_requires_explicit_allowance(self):
        tok = self.tokenizer()
        control = tok.add_special_token("<|end|>")
        self.assertEqual(tok.encode("<|end|>", allowed_special={"<|end|>"}), [control])

    def test_unallowed_controls_still_encode_normally(self):
        tok = self.tokenizer()
        a, b = tok.add_special_token("<|a|>"), tok.add_special_token("<|b|>")
        ids = tok.encode("<|a|><|b|>", allowed_special={"<|a|>"})
        self.assertIn(a, ids)
        self.assertNotIn(b, ids)
        self.assertEqual(tok.decode(ids), "<|a|><|b|>")

    def test_unknown_allowance_or_string_collection_rejected(self):
        tok = self.tokenizer()
        for allowed in ({"<|unknown|>"}, "<|unknown|>"):
            with self.assertRaises(ValueError):
                tok.encode("text", allowed_special=allowed)

    def test_invalid_ids_rejected_instead_of_dropped(self):
        tok = self.tokenizer()
        for invalid in (-1, 999999, True, 1.0, "1"):
            with self.assertRaises(ValueError):
                tok.decode([invalid])

    def test_duplicate_control_registration_is_stable(self):
        tok = self.tokenizer()
        control = tok.add_special_token("<|end|>")
        size = tok.vocab_size()
        self.assertEqual(tok.add_special_token("<|end|>"), control)
        self.assertEqual(tok.vocab_size(), size)

    def test_normalization_is_explicit(self):
        text = "Ｆ café ﬁ e\u0301"
        identity = self.tokenizer()
        nfkc = self.tokenizer("NFKC")
        self.assertEqual(identity.decode(identity.encode(text)), text)
        self.assertEqual(nfkc.decode(nfkc.encode(text)), unicodedata.normalize("NFKC", text))

    def test_invalid_normalization_or_control_rejected(self):
        with self.assertRaises(ValueError):
            module.ProductionTokenizer("invalid")
        tok = module.ProductionTokenizer("NFKC")
        for spelling in ("", "Ｆ"):
            with self.assertRaises(ValueError):
                tok.add_special_token(spelling)

    def test_merges_are_deterministic_and_lexical_ties_are_explicit(self):
        first, second = module.ProductionTokenizer(), module.ProductionTokenizer()
        with contextlib.redirect_stdout(io.StringIO()):
            first.train("aa\nbb", 1)
            second.train("aa\nbb", 1)
        self.assertEqual(first.merges, second.merges)
        self.assertEqual(list(first.merges)[0], (97, 97))

    def test_merge_is_non_overlapping(self):
        self.assertEqual(module.apply_merge([1, 1, 1], (1, 1), 256), [256, 1])

    def test_generated_invalid_utf8_uses_declared_replacement(self):
        tok = module.ProductionTokenizer()
        self.assertEqual(tok.decode([255]), "\ufffd")

    def test_training_policy_and_empty_corpus(self):
        tok = module.ProductionTokenizer()
        with contextlib.redirect_stdout(io.StringIO()):
            tok.train("", 10)
        self.assertEqual(tok.vocab_size(), 256)
        for n in (-1, True, 1.5):
            with self.assertRaises(ValueError):
                tok.train("", n)
        tok.add_special_token("<|end|>")
        with self.assertRaises(ValueError):
            tok.train("data", 1)


if __name__ == "__main__":
    unittest.main()
