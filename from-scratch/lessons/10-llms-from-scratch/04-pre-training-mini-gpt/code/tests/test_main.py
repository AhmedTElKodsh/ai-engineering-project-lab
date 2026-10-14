import contextlib
import importlib.util
import io
import unittest
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location("qualified_reference", Path(__file__).resolve().parents[1] / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PartialReferenceTests(unittest.TestCase):
    def setUp(self):
        np.random.seed(4)
        self.model = module.MiniGPT(vocab_size=16, embed_dim=8, num_heads=2, num_layers=1, max_seq_len=8, ff_dim=16)

    def test_forward_shape_and_finite_logits(self):
        logits = self.model.forward(np.array([[1, 2, 3]]))
        self.assertEqual(logits.shape, (1, 3, 16))
        self.assertTrue(np.isfinite(logits).all())

    def test_future_tokens_do_not_change_earlier_logits(self):
        first = self.model.forward(np.array([[1, 2, 3]]))
        changed = self.model.forward(np.array([[1, 7, 8]]))
        np.testing.assert_allclose(first[:, :1], changed[:, :1], atol=1e-12)

    def test_uniform_cross_entropy_and_large_logits_are_stable(self):
        logits = np.full((1, 2, 16), 10000.0)
        self.assertAlmostEqual(module.cross_entropy_loss(logits, np.array([[1, 2]])), np.log(16))

    def test_feedforward_gradient_matches_finite_difference_at_smooth_point(self):
        ffn = module.FeedForward(2, 3)
        ffn.W1[:] = 0.2
        ffn.b1[:] = 1.0
        x, upstream = np.array([[[0.3, 0.4]]]), np.array([[[0.5, -0.2]]])
        gradient = module.ffn_backward(upstream, x, ffn)[1]
        original = ffn.W1[0, 0]
        eps = 1e-6
        ffn.W1[0, 0] = original + eps
        plus = np.sum(ffn.forward(x) * upstream)
        ffn.W1[0, 0] = original - eps
        minus = np.sum(ffn.forward(x) * upstream)
        self.assertAlmostEqual(gradient[0, 0], (plus - minus) / (2 * eps), places=8)

    def test_layernorm_gradient_matches_finite_difference(self):
        ln = module.LayerNorm(3)
        x, upstream = np.array([[[0.2, -0.3, 0.8]]]), np.array([[[0.5, 0.3, -0.2]]])
        dx = module.layernorm_backward(upstream, x, ln)[0]
        eps = 1e-6
        plus, minus = x.copy(), x.copy()
        plus[0, 0, 0] += eps
        minus[0, 0, 0] -= eps
        reference = np.sum((ln.forward(plus) - ln.forward(minus)) * upstream) / (2 * eps)
        self.assertAlmostEqual(dx[0, 0, 0], reference, places=8)

    def test_generation_is_bounded(self):
        self.assertEqual(len(module.generate(self.model, [1], max_new_tokens=3)), 4)

    def test_update_routine_is_explicitly_qualified(self):
        self.assertEqual(module.REFERENCE_STATUS, "partial_backward")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            module.train_mini_gpt("small byte fixture repeated " * 3, embed_dim=8, num_heads=1, num_layers=1, seq_len=4, num_steps=1)
        self.assertIn("PARTIAL-BACKWARD", out.getvalue())
        self.assertIn("Excluded from full-training", out.getvalue())


if __name__ == "__main__":
    unittest.main()
