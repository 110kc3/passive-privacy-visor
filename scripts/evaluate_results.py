#!/usr/bin/env python3
"""Evaluate passive privacy visor test results against the acceptance gate.

Validates test matrix completeness (paired baseline and visor recordings),
safety criteria (visibility and comfort passes), and landmark disruption scores.
"""

from __future__ import annotations

import argparse
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path
from typing import Any

REQUIRED_MATRIX_IDS = ("D1", "D2", "I1", "I2", "F1", "F2", "W1", "M1")


def parse_bool(value: str) -> bool:
    """Parse common truthy boolean representations."""
    return value.strip().lower() in ("true", "1", "yes", "pass", "t", "y")


def load_results_csv(path: Path) -> list[dict[str, str]]:
    """Read a test-results CSV file and return list of rows as dicts."""
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        return [row for row in reader if any(v.strip() for v in row.values())]


def evaluate_results(
    rows: list[dict[str, str]],
    min_score_target: float = 2.0,
) -> dict[str, Any]:
    """Evaluate rows against the prototype acceptance criteria.

    Criteria (from docs/test-plan.md and docs/implementation-plan.md):
    - All matrix test IDs must have paired baseline and visor records.
    - Visibility and comfort checks must pass for all visor trials.
    - Average landmark disruption on visor trials must meet or exceed min_score_target.
    """
    by_test_id: dict[str, dict[str, dict[str, str]]] = {}
    for row in rows:
        tid = row.get("test_id", "").strip()
        kind = row.get("baseline_or_visor", "").strip().lower()
        if not tid or not kind:
            continue
        by_test_id.setdefault(tid, {})[kind] = row

    missing_matrix: list[str] = []
    unpaired: list[str] = []

    for req_id in REQUIRED_MATRIX_IDS:
        if req_id not in by_test_id:
            missing_matrix.append(req_id)
        else:
            kinds = by_test_id[req_id]
            if "baseline" not in kinds or "visor" not in kinds:
                unpaired.append(req_id)

    safety_failures: list[dict[str, str]] = []
    visor_disruption_scores: list[int] = []

    for row in rows:
        kind = row.get("baseline_or_visor", "").strip().lower()
        if kind == "visor":
            tid = row.get("test_id", "unknown")
            vis_pass = parse_bool(row.get("visibility_pass", "false"))
            comf_pass = parse_bool(row.get("comfort_pass", "false"))
            if not vis_pass or not comf_pass:
                safety_failures.append({
                    "test_id": tid,
                    "visibility_pass": str(vis_pass),
                    "comfort_pass": str(comf_pass),
                })
            score_str = row.get("landmark_disruption_0_to_3", "").strip()
            if score_str:
                try:
                    score = int(score_str)
                    if not (0 <= score <= 3):
                        raise ValueError(f"Score out of range 0..3: {score}")
                    visor_disruption_scores.append(score)
                except ValueError as err:
                    raise ValueError(f"Invalid disruption score in test {tid}: {err}") from err

    avg_score = (
        sum(visor_disruption_scores) / len(visor_disruption_scores)
        if visor_disruption_scores
        else 0.0
    )

    passed = (
        len(missing_matrix) == 0
        and len(unpaired) == 0
        and len(safety_failures) == 0
        and avg_score >= min_score_target
    )

    return {
        "total_rows": len(rows),
        "visor_trials_count": len(visor_disruption_scores),
        "missing_matrix_ids": missing_matrix,
        "unpaired_test_ids": unpaired,
        "safety_failures": safety_failures,
        "average_disruption_score": round(avg_score, 2),
        "target_score": min_score_target,
        "gate_passed": passed,
    }


def render_report(eval_summary: dict[str, Any]) -> str:
    """Format evaluation summary as a human-readable text report."""
    status = "PASS" if eval_summary["gate_passed"] else "FAIL"
    lines = [
        f"Acceptance Gate Evaluation: {status}",
        f"  Total records: {eval_summary['total_rows']}",
        f"  Visor trials: {eval_summary['visor_trials_count']}",
        f"  Average disruption score: {eval_summary['average_disruption_score']} (target >= {eval_summary['target_score']})",
    ]
    if eval_summary["missing_matrix_ids"]:
        lines.append(f"  Missing required matrix IDs: {', '.join(eval_summary['missing_matrix_ids'])}")
    if eval_summary["unpaired_test_ids"]:
        lines.append(f"  Unpaired test IDs: {', '.join(eval_summary['unpaired_test_ids'])}")
    if eval_summary["safety_failures"]:
        lines.append(f"  Safety check failures: {len(eval_summary['safety_failures'])} visor trials failed visibility or comfort")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("results_csv", type=Path, help="Path to test-results.csv")
    parser.add_argument("--target-avg", type=float, default=2.0, help="Minimum average landmark disruption (default 2.0)")
    args = parser.parse_args()

    rows = load_results_csv(args.results_csv)
    summary = evaluate_results(rows, min_score_target=args.target_avg)
    print(render_report(summary))
    if not summary["gate_passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
