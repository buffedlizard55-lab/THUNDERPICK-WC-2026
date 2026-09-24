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
    if ids != list(range(1, 61)):
        fail(f"research ledger must contain IDs 1..60 in order (three passes), found {ids}")
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

    # Third-pass data shape checks (rulebook + pre-event calendar).
    rules = data.get("tournament", {}).get("rules", {})
    for key in ("core_roster", "stand_in", "server", "veto_bo3", "veto_bo5", "withdrawal", "seeding", "source"):
        if key not in rules:
            fail(f"tournament.rules missing '{key}'")
    if "12,500" not in rules["server"]:
        fail("tournament.rules.server must state the $12,500 overtime money from the rulebook")
    calendar = data.get("tournament", {}).get("pre_event_calendar", {})
    for key in ("starseries_fall_2026", "blast_open_porto_2026", "esl_pro_league_s24", "cs2_update", "major_vrs_cutoff"):
        if key not in calendar:
            fail(f"tournament.pre_event_calendar missing '{key}'")
    rows = [(c["date"], c["team"], c["change"]) for c in data.get("roster_changes_timeline", [])]
    if len(rows) != len(set(rows)):
        fail("roster timeline contains duplicate rows")
    if [r[0] for r in rows] != sorted(r[0] for r in rows):
        fail("roster timeline must be sorted by date")

    # The second- and third-pass entries must be mirrored on the Verified List page.
    master = (ROOT / "master-list.html").read_text(encoding="utf-8")
    for probe in ("Entries 21–40", "DragonClaw", "MR12", "Entries 41–60", "StarSeries",
                  "12,500", "Schengen", "Pro League", "60-entry ledger"):
        if probe not in master:
            fail(f"master-list.html is missing pass-2/3 content ({probe!r})")
    section = master.split('id="entries-41-60"', 1)
    if len(section) != 2:
        fail("master-list.html lacks the entries-41-60 section")
    body = section[1].split('id="irregularities"', 1)[0]
    shown = [int(n) for n in re.findall(r'<td class="num">(\d+)</td>', body)]
    if shown != list(range(41, 61)):
        fail(f"entries 41-60 table must list IDs 41..60 in order, found {shown}")

    # Retired claims must not reappear anywhere (corrected in pass 3).
    for page in ROOT.glob("*.html"):
        html = page.read_text(encoding="utf-8")
        if re.search(r"\$10,000</b> OT|\$10,000 OT money at Majors", html):
            fail(f"{page.name} still carries the retired '$10,000 OT at Majors' claim")
        if "entire Cologne Major campaign (5th–8th) as BetBoom's fifth, deputizing for visa-hit d1Ledez" in html:
            fail(f"{page.name} still carries the retired BetBoom/Cologne claim")

    # Catch broken local links without attempting remote network checks.
    local_link_errors = []
    for page in ROOT.glob("*.html"):
        html = page.read_text(encoding="utf-8")
        for href in re.findall(r'href="([^"]+)"', html):
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target, _, frag = href.partition("#")
            if target and not (page.parent / target).exists():
                local_link_errors.append(f"{page.name}: {href}")
            elif frag and target.endswith(".html"):
                if f'id="{frag}"' not in (page.parent / target).read_text(encoding="utf-8"):
                    local_link_errors.append(f"{page.name}: {href} (missing anchor)")
    if local_link_errors:
        fail("broken local links: " + ", ".join(local_link_errors))

    print("OK: 8 teams, 40 players, 8 coaches, bench/reserve fields, 60 verified ledger entries, "
          "ranking/schedule/rules/calendar blocks, entries 41-60 mirrored, retired claims absent, local links + anchors")


if __name__ == "__main__":
    main()
