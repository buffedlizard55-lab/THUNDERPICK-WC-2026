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
    if ids != list(range(1, 41)):
        fail(f"research ledger must contain IDs 1..40 in order (two passes), found {ids}")
    if any(entry.get("status") != "verified" for entry in entries):
        fail("every research-ledger entry must have status=verified after review")
    if any(not entry.get("sources") for entry in entries):
        fail("every research-ledger entry must have at least one review URL")

    # Second-pass data shape checks.
    rankings = data.get("rankings_snapshot", {})
    if "hltv_live_valve_ranking_2026_09_23" not in rankings:
        fail("rankings snapshot must include the Sept 23 live Valve ranking block")
    if len(rankings["hltv_live_valve_ranking_2026_09_23"]["twc_teams"]) != 8:
        fail("the live Valve ranking block must cover all eight teams")
    schedule = data.get("tournament", {}).get("finals_week_schedule", {})
    for key in ("arrival_day", "media_day", "group_stage", "playoffs", "departure_day"):
        if key not in schedule:
            fail(f"finals_week_schedule missing '{key}'")
    timeline_dates = sorted(c["date"] for c in data.get("roster_changes_timeline", []))
    if len(timeline_dates) != len(set(timeline_dates)) and len(set(timeline_dates)) < 30:
        fail("roster timeline lost entries during the second pass")

    # The 20 second-pass entries must be mirrored on the Verified List page.
    master = (ROOT / "master-list.html").read_text(encoding="utf-8")
    for probe in ("21", "40", "Entries 21–40", "DragonClaw", "MR12"):
        if probe not in master:
            fail(f"master-list.html is missing second-pass content ({probe!r})")

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

    print("OK: 8 teams, 40 players, 8 coaches, bench/reserve fields, 40 verified ledger entries, "
          "second-pass ranking/schedule blocks, and local links")


if __name__ == "__main__":
    main()
