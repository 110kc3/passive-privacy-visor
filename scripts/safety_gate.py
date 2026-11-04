#!/usr/bin/env python3
"""Evaluate passive privacy visor safety gates and mechanical checklists.

Validates mechanical inspection, wearer visibility checks, and seated wear
duration tests prior to camera recording sessions per docs/safety.md.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_MECHANICAL_CHECKS = (
    "no_added_material_in_eye_corridor",
    "exterior_seams_and_knots",
    "unmodified_faceguard_structure",
    "no_hazardous_fasteners",
    "flip_up_cycles_20_without_catching",
    "secure_strap_attachment",
)

REQUIRED_VISIBILITY_CHECKS = (
    "phone_text_legible_each_eye",
    "finger_count_at_1m_3m_and_periphery",
    "floor_objects_visible_1m_2m",
    "extreme_gaze_no_intrusion",
    "normal_removal_without_snag",
)

REQUIRED_SEATED_CHECKS = (
    "one_minute_seated_symptom_free",
    "ten_minute_seated_symptom_free",
)


def load_safety_log(path: Path) -> dict[str, Any]:
    """Read safety inspection record from a JSON file."""
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def evaluate_safety_log(data: dict[str, Any]) -> dict[str, Any]:
    """Evaluate safety inspection data against safety gate rules.

    Checks:
    - Revision, inspector, and date are present.
    - All required mechanical checks are true.
    - All required visibility checks are true.
    - All seated duration tests are true and reported symptoms list is empty.
    """
    failures: list[str] = []

    revision = str(data.get("revision", "")).strip()
    if not revision:
        failures.append("Missing or empty 'revision'")

    inspector = str(data.get("inspector", "")).strip()
    if not inspector:
        failures.append("Missing or empty 'inspector'")

    date_str = str(data.get("date", "")).strip()
    if not date_str:
        failures.append("Missing or empty 'date'")

    # Mechanical checks
    mech = data.get("mechanical_checks", {})
    if not isinstance(mech, dict):
        failures.append("'mechanical_checks' must be a dictionary")
        mech = {}
    for check in REQUIRED_MECHANICAL_CHECKS:
        if not bool(mech.get(check)):
            failures.append(f"Mechanical check failed: '{check}'")

    # Visibility checks
    vis = data.get("visibility_checks", {})
    if not isinstance(vis, dict):
        failures.append("'visibility_checks' must be a dictionary")
        vis = {}
    for check in REQUIRED_VISIBILITY_CHECKS:
        if not bool(vis.get(check)):
            failures.append(f"Visibility check failed: '{check}'")

    # Seated checks & symptoms
    seated = data.get("seated_wear_tests", {})
    if not isinstance(seated, dict):
        failures.append("'seated_wear_tests' must be a dictionary")
        seated = {}
    for check in REQUIRED_SEATED_CHECKS:
        if not bool(seated.get(check)):
            failures.append(f"Seated duration check failed: '{check}'")

    symptoms = seated.get("reported_symptoms", [])
    if symptoms:
        failures.append(f"Reported wearer symptoms detected: {symptoms}")

    passed = len(failures) == 0

    return {
        "revision": revision,
        "inspector": inspector,
        "date": date_str,
        "safety_gate_passed": passed,
        "failures": failures,
    }


def render_safety_report(summary: dict[str, Any]) -> str:
    """Render human-readable text report for safety gate evaluation."""
    status = "PASS" if summary["safety_gate_passed"] else "FAIL"
    lines = [
        f"=== Safety Gate Evaluation: {status} ===",
        f"Revision:  {summary.get('revision', 'N/A')}",
        f"Inspector: {summary.get('inspector', 'N/A')}",
        f"Date:      {summary.get('date', 'N/A')}",
        f"Result:    {'CLEARED FOR TESTING' if summary['safety_gate_passed'] else 'REJECTED - DO NOT TEST'}",
    ]
    if summary["failures"]:
        lines.append("Failures:")
        for f in summary["failures"]:
            lines.append(f"  - {f}")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Evaluate passive privacy visor safety gates.")
    parser.add_argument("log_file", type=Path, help="Path to safety inspection JSON log")
    parser.add_argument("--json", action="store_true", help="Print output as JSON")

    args = parser.parse_args()

    data = load_safety_log(args.log_file)
    summary = evaluate_safety_log(data)

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        print(render_safety_report(summary))

    if not summary["safety_gate_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
