import contextlib
import importlib.util
import io
import unittest
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location("qualified_reference", Path(__file__).resolve().parents[1] / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class SftDemonstrationTests(unittest.TestCase):
    def test_utf8_instruction_bytes_preserved_under_fixture_policy(self):
        tokens = module.tokenize_instruction_pair("مرحبا", "你好")
        a = len("مرحبا".encode("utf-8"))
        self.assertEqual(tokens[1:1+a], list("مرحبا".encode("utf-8")))
        self.assertEqual(tokens[a+3:], list("你好".encode("utf-8")))

    def test_response_mask_excludes_prompt_and_control(self):
        tokens = module.tokenize_instruction_pair("A", "xy")
        np.testing.assert_array_equal(module.create_loss_mask(tokens), [0, 0, 0, 0, 1, 1])

    def test_shifted_mask_scores_first_response_target(self):
        tokens = module.tokenize_instruction_pair("A", "xy")
        targets, shifted_mask = np.array(tokens[1:]), module.create_loss_mask(tokens)[1:]
        supervised = targets[shifted_mask.astype(bool)]
        np.testing.assert_array_equal(supervised, list(b"xy"))

    def test_masked_loss_ignores_prompt_logits(self):
        logits = np.zeros((1, 3, 4))
        targets, mask = np.array([[1, 2, 3]]), np.array([[0, 1, 1]])
        initial = module.masked_cross_entropy_loss(logits, targets, mask)
        logits[0, 0] = [100, -100, 50, 10]
        self.assertAlmostEqual(module.masked_cross_entropy_loss(logits, targets, mask), initial)

    def test_uniform_response_loss(self):
        logits = np.full((1, 2, 8), 9999.0)
        loss = module.masked_cross_entropy_loss(logits, np.array([[1, 2]]), np.ones((1, 2)))
        self.assertAlmostEqual(loss, np.log(8))

    def test_zero_mask_returns_placeholder_not_learning_evidence(self):
        self.assertEqual(module.masked_cross_entropy_loss(np.zeros((1, 1, 4)), np.array([[1]]), np.zeros((1, 1))), 0)
        self.assertEqual(module.REFERENCE_STATUS, "random_update_not_sft")

    def test_random_update_routine_labels_its_limitation(self):
        np.random.seed(7)
        model = module.MiniGPT(vocab_size=256, embed_dim=8, num_heads=1, num_layers=1, max_seq_len=16, ff_dim=16)
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            module.sft_train(model, [{"instruction": "A", "response": "xy"}], num_epochs=1, seq_len=16)
        self.assertIn("RANDOM-UPDATE DEMONSTRATION, NOT SFT", out.getvalue())
        self.assertIn("Excluded from adaptation", out.getvalue())


if __name__ == "__main__":
    unittest.main()
