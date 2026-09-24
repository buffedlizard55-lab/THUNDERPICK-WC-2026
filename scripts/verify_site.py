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
    if ids != list(range(1, 101)):
        fail(f"research ledger must contain IDs 1..100 in order (five passes), found {ids}")
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
    # Fourth-pass data shape checks (Global Qualifier block, Bucharest, irregularities).
    gq = data.get("tournament", {}).get("global_qualifier", {})
    for key in ("slots", "format", "placings", "prize", "sources"):
        if key not in gq:
            fail(f"tournament.global_qualifier missing '{key}'")
    if "1st" not in gq.get("placings", {}):
        fail("global_qualifier.placings must include the winner (1st)")
    cal4 = data.get("tournament", {}).get("pre_event_calendar", {})
    if "pgl_masters_bucharest" not in cal4:
        fail("tournament.pre_event_calendar missing 'pgl_masters_bucharest'")
    if len(data.get("irregularities", [])) < 20:
        fail("expected at least 20 flagged irregularities after the fifth pass")
    # Fifth-pass data shape checks (map-pool block, 2027 horizon, FPG3 calendar).
    maps = data.get("map_pool_win_rates", {})
    for key in ("window", "note", "teams", "sources"):
        if key not in maps:
            fail(f"map_pool_win_rates missing '{key}'")
    if len(maps.get("teams", {})) != 8:
        fail("map_pool_win_rates must cover all eight teams")
    if any(len(v) != 7 for v in maps.get("teams", {}).values()):
        fail("map_pool_win_rates must list all seven Active Duty maps per team")
    horizon = data.get("horizon_2027", {})
    for key in ("majors", "esports_world_cup_2027", "sources"):
        if key not in horizon:
            fail(f"horizon_2027 missing '{key}'")
    cal5 = data.get("tournament", {}).get("pre_event_calendar", {})
    if "fissure_playground_3" not in cal5:
        fail("tournament.pre_event_calendar missing 'fissure_playground_3'")
    if len(data.get("roster_changes_timeline", [])) < 45:
        fail("roster timeline must keep all pass 1-5 rows (expected >= 45)")
    rows = [(c["date"], c["team"], c["change"]) for c in data.get("roster_changes_timeline", [])]
    if len(rows) != len(set(rows)):
        fail("roster timeline contains duplicate rows")
    if [r[0] for r in rows] != sorted(r[0] for r in rows):
        fail("roster timeline must be sorted by date")

    # The second- and third-pass entries must be mirrored on the Verified List page.
    master = (ROOT / "master-list.html").read_text(encoding="utf-8")
    for probe in ("Entries 21–40", "DragonClaw", "MR12", "Entries 41–60", "StarSeries",
                  "12,500", "Schengen", "Pro League", "Entries 61–80", "Global Qualifier",
                  "MongolZ", "Bucharest", "device",
                  "Entries 81–100", "molodoy", "Map-pool profiles", "BC.Game",
                  "Shanghai", "100-entry ledger", "Complexity"):
        if probe not in master:
            fail(f"master-list.html is missing pass 2-4 content ({probe!r})")
    section = master.split('id="entries-41-60"', 1)
    if len(section) != 2:
        fail("master-list.html lacks the entries-41-60 section")
    body = section[1].split('id="entries-61-80"', 1)[0]
    shown = [int(n) for n in re.findall(r'<td class="num">(\d+)</td>', body)]
    if shown != list(range(41, 61)):
        fail(f"entries 41-60 table must list IDs 41..60 in order, found {shown}")
    section4 = master.split('id="entries-61-80"', 1)
    if len(section4) != 2:
        fail("master-list.html lacks the entries-61-80 section")
    body4 = section4[1].split('id="entries-81-100"', 1)[0]
    shown4 = [int(n) for n in re.findall(r'<td class="num">(\d+)</td>', body4)]
    if shown4 != list(range(61, 81)):
        fail(f"entries 61-80 table must list IDs 61..80 in order, found {shown4}")
    section5 = master.split('id="entries-81-100"', 1)
    if len(section5) != 2:
        fail("master-list.html lacks the entries-81-100 section")
    body5 = section5[1].split('id="irregularities"', 1)[0]
    shown5 = [int(n) for n in re.findall(r'<td class="num">(\d+)</td>', body5)]
    if shown5 != list(range(81, 101)):
        fail(f"entries 81-100 table must list IDs 81..100 in order, found {shown5}")

    # Fifth-pass content must be mirrored on the subpages.
    page_probes = {
        "stats.html": ('id="map-pool"', "Map-pool profiles"),
        "roster-changes.html": ("INJURY WATCH", "Eternal Fire head coach"),
        "teams.html": ("FISSURE Playground 3 quarter-final exit", "first big international LAN since IEM Chengdu 2025"),
        "players.html": ("KSCERATO", "n1ssim"),
        "betting-guide.html": ("stats.html#map-pool", "molodoy"),
        "cs2-guide.html": ("Shanghai", "Asia VRS region"),
        "index.html": ("fifth pass", "FISSURE Playground 3"),
    }
    for page_name, probes in page_probes.items():
        html = (ROOT / page_name).read_text(encoding="utf-8")
        for probe in probes:
            if probe not in html:
                fail(f"{page_name} is missing pass-5 content ({probe!r})")

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

    print("OK: 8 teams, 40 players, 8 coaches, bench/reserve fields, 100 verified ledger entries, "
          "ranking/schedule/rules/calendar/GQ/map-pool/horizon blocks, entries 41-60, 61-80 and 81-100 mirrored, "
          "pass-5 subpage mirrors, 20 irregularities, retired claims absent, local links + anchors")


if __name__ == "__main__":
    main()
