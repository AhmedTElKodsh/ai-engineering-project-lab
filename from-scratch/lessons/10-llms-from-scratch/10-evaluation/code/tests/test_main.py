import contextlib
import importlib.util
import io
import unittest
from pathlib import Path
import numpy as np

spec = importlib.util.spec_from_file_location("qualified_reference", Path(__file__).resolve().parents[1] / "main.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvaluationTests(unittest.TestCase):
    def test_exact_match_declares_case_and_whitespace_policy(self):
        self.assertEqual(module.exact_match(" Paris ", "paris"), 1.0)
        self.assertEqual(module.exact_match("Paris France", "paris"), 0.0)

    def test_token_overlap_empty_and_partial_cases(self):
        self.assertEqual(module.token_f1("", "answer"), 0.0)
        self.assertAlmostEqual(module.token_f1("one two", "two three"), 0.5)

    def test_uniform_log_probability_perplexity(self):
        self.assertAlmostEqual(module.perplexity([np.log(0.25)] * 3), 4.0)

    def test_unequal_target_counts_use_total_nll_over_total_targets(self):
        self.assertEqual(module.mean_target_nll([(2.0, 1), (12.0, 3)]), 3.5)
        self.assertNotEqual(module.mean_target_nll([(2.0, 1), (12.0, 3)]), (2.0+4.0)/2)

    def test_rebatching_preserves_aggregate(self):
        self.assertEqual(module.mean_target_nll([(2.0, 1), (12.0, 3)]), module.mean_target_nll([(14.0, 4)]))

    def test_invalid_or_zero_target_evaluation_rejected(self):
        for totals in ([], [(0.0, 0)], [(2, 0)], [(2, -1)], [(2, True)], [(float("nan"), 2)]):
            with self.assertRaises(ValueError):
                module.mean_target_nll(totals)

    def test_elo_update_is_zero_sum_for_equal_ratings(self):
        tracker = module.ELOTracker()
        tracker.record_match("a", "b", "a")
        self.assertAlmostEqual(sum(tracker.ratings.values()), 3000)
        self.assertGreater(tracker.ratings["a"], tracker.ratings["b"])

    def test_simulated_presentations_are_labelled(self):
        self.assertEqual(module.REFERENCE_STATUS, "simulated_metrics")
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            module.run_perplexity_demo()
        self.assertIn("SIMULATED Perplexity", out.getvalue())
        self.assertIn("not model measurements", out.getvalue())


if __name__ == "__main__":
    unittest.main()
