#!/usr/bin/env python3
"""Calculate purchase totals from data/bom.json without external packages."""

from __future__ import annotations

import argparse
from decimal import Decimal, ROUND_HALF_UP
import json
from pathlib import Path
from typing import Any


CENT = Decimal("0.01")
DEFAULT_BOM = Path(__file__).resolve().parents[1] / "data" / "bom.json"


def money(value: Decimal) -> Decimal:
    return value.quantize(CENT, rounding=ROUND_HALF_UP)


def load_bom(path: Path = DEFAULT_BOM) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def calculate(data: dict[str, Any], profile: str) -> dict[str, Any]:
    if profile not in data["profiles"]:
        valid = ", ".join(sorted(data["profiles"]))
        raise ValueError(f"unknown profile {profile!r}; choose one of: {valid}")

    selected = [item for item in data["items"] if profile in item["profiles"]]
    groups: dict[str, dict[str, Any]] = {}

    for item in selected:
        group_id = item["shipping_group"]
        if group_id not in data["shipping_groups"]:
            raise ValueError(f"item {item['id']!r} uses missing shipping group {group_id!r}")

        group = groups.setdefault(
            group_id,
            {
                "vendor": data["shipping_groups"][group_id]["vendor"],
                "items_pln": Decimal("0"),
                "shipping_pln": Decimal(data["shipping_groups"][group_id]["shipping_pln"]),
            },
        )
        line_total = Decimal(item["quantity"]) * Decimal(item["unit_price_pln"])
        group["items_pln"] += money(line_total)

    item_total = money(sum((group["items_pln"] for group in groups.values()), Decimal("0")))
    shipping_total = money(
        sum((group["shipping_pln"] for group in groups.values()), Decimal("0"))
    )

    rendered_groups = []
    for group_id, group in groups.items():
        group_total = money(group["items_pln"] + group["shipping_pln"])
        rendered_groups.append(
            {
                "id": group_id,
                "vendor": group["vendor"],
                "items_pln": f"{money(group['items_pln']):.2f}",
                "shipping_pln": f"{money(group['shipping_pln']):.2f}",
                "total_pln": f"{group_total:.2f}",
            }
        )

    return {
        "profile": profile,
        "description": data["profiles"][profile],
        "currency": data["currency"],
        "groups": rendered_groups,
        "items_pln": f"{item_total:.2f}",
        "shipping_pln": f"{shipping_total:.2f}",
        "delivered_total_pln": f"{money(item_total + shipping_total):.2f}",
    }


def render_text(result: dict[str, Any]) -> str:
    rows = [f"{result['profile']}: {result['description']}"]
    for group in result["groups"]:
        rows.append(
            "  {vendor}: items {items_pln} + shipping {shipping_pln} = "
            "{total_pln} PLN".format(**group)
        )
    rows.append(
        f"  delivered total: {result['delivered_total_pln']} {result['currency']}"
    )
    return "\n".join(rows)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bom", type=Path, default=DEFAULT_BOM)
    parser.add_argument(
        "--profile", choices=("core", "complete", "all"), default="core"
    )
    parser.add_argument("--json", action="store_true", dest="as_json")
    args = parser.parse_args()

    data = load_bom(args.bom)
    profiles = list(data["profiles"]) if args.profile == "all" else [args.profile]
    results = [calculate(data, profile) for profile in profiles]

    if args.as_json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print("\n\n".join(render_text(result) for result in results))


if __name__ == "__main__":
    main()
