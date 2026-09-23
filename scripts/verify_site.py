#!/usr/bin/env python3
"""Zero-dependency integrity checks for the static TWC 2026 site.

This validates local structure and the dated research ledger. It deliberately does
not claim that a remote source is permanently available: the source URLs remain
visible for human review and should be re-checked at every data refresh.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    data = json.loads((ROOT / "data/twc2026.json").read_text(encoding="utf-8"))
    ledger = json.loads((ROOT / "data/research-ledger.json").read_text(encoding="utf-8"))

    teams = data.get("teams", [])
    if len(teams) != 8:
        fail(f"expected 8 Finals teams, found {len(teams)}")
    if any(len(team.get("roster", [])) != 5 for team in teams):
        fail("every Finals team must have exactly five main-roster players")
    if any("coach" not in team for team in teams):
        fail("every Finals team must have a coach record")
    if any("bench_or_reserve" not in team for team in teams):
        fail("every Finals team must expose bench_or_reserve status")

    entries = ledger.get("entries", [])
    ids = [entry.get("id") for entry in entries]
    if ids != list(range(1, 21)):
        fail(f"research ledger must contain IDs 1..20 in order, found {ids}")
    if any(entry.get("status") != "verified" for entry in entries):
        fail("every research-ledger entry must have status=verified after review")
    if any(not entry.get("sources") for entry in entries):
        fail("every research-ledger entry must have at least one review URL")

    # Catch broken local links without attempting remote network checks.
    local_link_errors = []
    for page in ROOT.glob("*.html"):
        html = page.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = href.split("#", 1)[0]
            if target and not (page.parent / target).exists():
                local_link_errors.append(f"{page.name}: {href}")
    if local_link_errors:
        fail("broken local links: " + ", ".join(local_link_errors))

    print("OK: 8 teams, 40 players, 8 coaches, bench/reserve fields, 20 verified ledger entries, and local links")


if __name__ == "__main__":
    main()
