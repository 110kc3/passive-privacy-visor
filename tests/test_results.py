from pathlib import Path
import tempfile
import unittest

from scripts.evaluate_results import (
    REQUIRED_MATRIX_IDS,
    evaluate_results,
    load_results_csv,
    parse_bool,
    render_report,
)


class EvaluateResultsTests(unittest.TestCase):
    def test_parse_bool(self):
        self.assertTrue(parse_bool("true"))
        self.assertTrue(parse_bool("True"))
        self.assertTrue(parse_bool("1"))
        self.assertTrue(parse_bool("pass"))
        self.assertFalse(parse_bool("false"))
        self.assertFalse(parse_bool("0"))
        self.assertFalse(parse_bool(""))

    def test_complete_passing_matrix(self):
        rows = []
        for tid in REQUIRED_MATRIX_IDS:
            rows.append({
                "test_id": tid,
                "baseline_or_visor": "baseline",
                "visibility_pass": "true",
                "comfort_pass": "true",
                "landmark_disruption_0_to_3": "0",
            })
            rows.append({
                "test_id": tid,
                "baseline_or_visor": "visor",
                "visibility_pass": "true",
                "comfort_pass": "true",
                "landmark_disruption_0_to_3": "2",
            })

        summary = evaluate_results(rows, min_score_target=2.0)
        self.assertTrue(summary["gate_passed"])
        self.assertEqual(summary["average_disruption_score"], 2.0)
        self.assertEqual(len(summary["missing_matrix_ids"]), 0)
        self.assertEqual(len(summary["unpaired_test_ids"]), 0)
        self.assertEqual(len(summary["safety_failures"]), 0)

        report = render_report(summary)
        self.assertIn("Acceptance Gate Evaluation: PASS", report)

    def test_missing_matrix_ids_and_unpaired(self):
        rows = [
            {
                "test_id": "D1",
                "baseline_or_visor": "visor",
                "visibility_pass": "true",
                "comfort_pass": "true",
                "landmark_disruption_0_to_3": "3",
            }
        ]
        summary = evaluate_results(rows, min_score_target=2.0)
        self.assertFalse(summary["gate_passed"])
        self.assertIn("D2", summary["missing_matrix_ids"])
        self.assertIn("D1", summary["unpaired_test_ids"])

    def test_safety_check_failure(self):
        rows = []
        for tid in REQUIRED_MATRIX_IDS:
            rows.append({
                "test_id": tid,
                "baseline_or_visor": "baseline",
                "visibility_pass": "true",
                "comfort_pass": "true",
            })
            rows.append({
                "test_id": tid,
                "baseline_or_visor": "visor",
                "visibility_pass": "false" if tid == "D1" else "true",
                "comfort_pass": "true",
                "landmark_disruption_0_to_3": "3",
            })

        summary = evaluate_results(rows, min_score_target=2.0)
        self.assertFalse(summary["gate_passed"])
        self.assertEqual(len(summary["safety_failures"]), 1)
        self.assertEqual(summary["safety_failures"][0]["test_id"], "D1")

    def test_load_results_csv(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            csv_path = Path(tmpdir) / "test.csv"
            csv_path.write_text(
                "test_id,baseline_or_visor,visibility_pass,comfort_pass,landmark_disruption_0_to_3\n"
                "D1,visor,true,true,2\n",
                encoding="utf-8",
            )
            rows = load_results_csv(csv_path)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["test_id"], "D1")


if __name__ == "__main__":
    unittest.main()
