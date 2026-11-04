from pathlib import Path
import tempfile
import unittest

from scripts.safety_gate import (
    evaluate_safety_log,
    load_safety_log,
    render_safety_report,
)


class SafetyGateTests(unittest.TestCase):
    def setUp(self):
        self.valid_payload = {
            "revision": "R1-A5",
            "inspector": "QC Engineer",
            "date": "2026-09-02",
            "mechanical_checks": {
                "no_added_material_in_eye_corridor": True,
                "exterior_seams_and_knots": True,
                "unmodified_faceguard_structure": True,
                "no_hazardous_fasteners": True,
                "flip_up_cycles_20_without_catching": True,
                "secure_strap_attachment": True,
            },
            "visibility_checks": {
                "phone_text_legible_each_eye": True,
                "finger_count_at_1m_3m_and_periphery": True,
                "floor_objects_visible_1m_2m": True,
                "extreme_gaze_no_intrusion": True,
                "normal_removal_without_snag": True,
            },
            "seated_wear_tests": {
                "one_minute_seated_symptom_free": True,
                "ten_minute_seated_symptom_free": True,
                "reported_symptoms": [],
            },
        }

    def test_complete_passing_safety_log(self):
        res = evaluate_safety_log(self.valid_payload)
        self.assertTrue(res["safety_gate_passed"])
        self.assertEqual(len(res["failures"]), 0)
        report = render_safety_report(res)
        self.assertIn("Safety Gate Evaluation: PASS", report)
        self.assertIn("CLEARED FOR TESTING", report)

    def test_mechanical_failure_blocks_gate(self):
        payload = dict(self.valid_payload)
        payload["mechanical_checks"] = dict(self.valid_payload["mechanical_checks"])
        payload["mechanical_checks"]["flip_up_cycles_20_without_catching"] = False

        res = evaluate_safety_log(payload)
        self.assertFalse(res["safety_gate_passed"])
        self.assertTrue(any("flip_up_cycles" in f for f in res["failures"]))
        report = render_safety_report(res)
        self.assertIn("REJECTED - DO NOT TEST", report)

    def test_visibility_failure_blocks_gate(self):
        payload = dict(self.valid_payload)
        payload["visibility_checks"] = dict(self.valid_payload["visibility_checks"])
        payload["visibility_checks"]["extreme_gaze_no_intrusion"] = False

        res = evaluate_safety_log(payload)
        self.assertFalse(res["safety_gate_passed"])
        self.assertTrue(any("extreme_gaze" in f for f in res["failures"]))

    def test_symptom_blocks_gate(self):
        payload = dict(self.valid_payload)
        payload["seated_wear_tests"] = {
            "one_minute_seated_symptom_free": True,
            "ten_minute_seated_symptom_free": False,
            "reported_symptoms": ["mild eye strain", "headache"],
        }

        res = evaluate_safety_log(payload)
        self.assertFalse(res["safety_gate_passed"])
        self.assertTrue(any("Reported wearer symptoms detected" in f for f in res["failures"]))

    def test_load_and_evaluate_reference_file(self):
        ref_path = Path(__file__).resolve().parents[1] / "data" / "reference-safety-log-r1.json"
        self.assertTrue(ref_path.exists())
        data = load_safety_log(ref_path)
        res = evaluate_safety_log(data)
        self.assertTrue(res["safety_gate_passed"])


if __name__ == "__main__":
    unittest.main()
