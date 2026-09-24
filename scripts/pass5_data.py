#!/usr/bin/env python3
"""Pass 5 (Sept 24, 2026): update data/twc2026.json with the 20 new verified findings.

Companion to scripts/pass5_ledger.py (entries 81-100). Run from repo root:
    python3 scripts/pass5_data.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "twc2026.json"


def insert_sorted(timeline: list, row: dict) -> list:
    out, placed = [], False
    for r in timeline:
        if not placed and row["date"] <= r["date"]:
            out.append(row)
            placed = True
        out.append(r)
    if not placed:
        out.append(row)
    return out


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8"))
    teams = {t["id"]: t for t in data["teams"]}

    # ---- meta -------------------------------------------------------------
    data["meta"]["verification_passes"] = (
        "Five passes of 20 new ledger entries each: first build and entries 1-20 on Sept 23, 2026 "
        "(pass 2, entries 21-40, same day); pass 3 (entries 41-60) and pass 4 (entries 61-80) on "
        "Sept 24, 2026; pass 5 (entries 81-100) on Sept 24, 2026. Pass 4 added the Global Qualifier "
        "deep-dive, field absences, The MongolZ crisis, PGL Masters Bucharest and the odds status. "
        "Pass 5 added FISSURE Playground 3 results and interviews, molodoy's eye condition, "
        "StarSeries MVP/EVPs, the completed Bucharest qualifier field, the 2027 Major/EWC calendar, "
        "the Americas VRS race, the Complexity/ODDIK org closures, Virtus.pro's VRS trajectory and "
        "3-month map-pool win rates for all eight teams. Ledger: data/research-ledger.json (100 entries)."
    )

    # ---- rankings snapshot: live-Valve re-check note -----------------------
    live = data["rankings_snapshot"]["hltv_live_valve_ranking_2026_09_23"]
    live["note"] += " Re-checked from the same page on Sept 24, 2026 (pass 5): identical except Virtus.pro, whose live badge read #44 - live ranks move continuously; the site pins all figures to their read date."

    # ---- new top-level block: map-pool win rates (entry 100) ---------------
    assert "map_pool_win_rates" not in data
    data["map_pool_win_rates"] = {
        "window": "June 24 - September 24, 2026 (HLTV team stats, online + LAN)",
        "note": "Percentages are map win rates over the window; 'no maps' means zero maps played in the window (a veto relevance signal), not a confirmed perma-ban. Sample sizes are small (roughly 5-18 maps per team per map); treat as context, not probability. Virtus.pro's sample includes non-tier-1 opposition.",
        "teams": {
            "FURIA":      {"Nuke": 75.0, "Inferno": 66.7, "Mirage": 55.6, "Ancient": 50.0, "Cache": 44.4, "Dust2": 44.4, "Anubis": 0.0},
            "Falcons":    {"Dust2": 75.0, "Inferno": 75.0, "Nuke": 66.7, "Mirage": 50.0, "Ancient": 20.0, "Anubis": 0.0, "Cache": None},
            "Legacy":     {"Inferno": 100.0, "Nuke": 75.0, "Mirage": 71.4, "Ancient": 66.7, "Dust2": 55.6, "Cache": 50.0, "Anubis": None},
            "Aurora":     {"Nuke": 100.0, "Anubis": 62.5, "Mirage": 60.0, "Inferno": 57.1, "Cache": 50.0, "Dust2": 50.0, "Ancient": 0.0},
            "9z":         {"Cache": 66.7, "Dust2": 62.5, "Mirage": 60.0, "Nuke": 50.0, "Inferno": 33.3, "Ancient": 25.0, "Anubis": None},
            "BetBoom":    {"Dust2": 100.0, "Mirage": 75.0, "Ancient": 60.0, "Cache": 50.0, "Anubis": 50.0, "Nuke": 33.3, "Inferno": None},
            "PARIVISION": {"Ancient": 71.4, "Dust2": 60.0, "Mirage": 50.0, "Anubis": 50.0, "Inferno": 20.0, "Cache": 0.0, "Nuke": None},
            "Virtus.pro": {"Ancient": 87.5, "Dust2": 72.2, "Mirage": 61.5, "Cache": 55.6, "Nuke": 44.4, "Anubis": 37.5, "Inferno": None},
        },
        "source": "https://www.hltv.org/stats/teams/maps/8297/furia?startDate=2026-06-24&endDate=2026-09-24",
        "sources": [
            "https://www.hltv.org/stats/teams/maps/8297/furia?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/11283/falcons?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/12468/legacy?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/11861/aurora?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/9996/9z?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/12394/betboom?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/12467/parivision?startDate=2026-06-24&endDate=2026-09-24",
            "https://www.hltv.org/stats/teams/maps/5378/virtuspro?startDate=2026-06-24&endDate=2026-09-24",
        ],
    }

    # ---- team season updates ----------------------------------------------
    furia = teams["furia"]["season_2026"]
    furia.append(
        "FISSURE Playground 3 (Sept 8-13): quarter-final exit, 5th-6th (0-2 vs G2; 14-16 OT Ancient "
        "after leading 11-7); FalleN: 'I know it's coming to an end, and I want to make the most of it'"
    )
    furia.append(
        "Grand finals in 2026: IEM Krakow and the IEM Cologne Major - both lost; YEKINDAR (Sept 16) calls "
        "the season 'labored': 'we're just failing as a team' (no internal conflict)"
    )
    furia.append(
        "molodoy is playing through an eye condition that requires surgery (pressure behind the eyes "
        "causing migraines; surgery planned in Kazakhstan - Sept 20 StarLadder broadcast); KSCERATO was "
        "StarSeries Fall's top EVP (1.26, 89.9 ADR; 4th straight event above 1.20)"
    )

    aurora = teams["aurora"]["season_2026"]
    aurora.append(
        "Jimpphat: StarSeries Fall EVP (first since IEM Rio 2024; series-high 1.36 in the upper-final win "
        "over Vitality, 1.41 rating in map wins pre-final): 'Recently I've just had such a crazy amount of confidence'"
    )
    for b in teams["aurora"]["bench_or_reserve"]:
        if b["nick"] == "Fabre":
            b["status"] = "benched June 29, 2026; appointed Eternal Fire head coach Sept 11, 2026"

    legacy = teams["legacy"]["season_2026"]
    legacy.append(
        "n1ssim earned an FPG3 EVP (1.20 rating; in the MVP race before the final) - the player who had "
        "benched himself in the summer and returned only after Legacy failed to replace him; latto (2 MVPs "
        "+ 2 EVPs in 2026) targets a first HLTV Top 20 after finishing Top 30 for 2025"
    )

    t9z = teams["9z"]["season_2026"]
    t9z.append(
        "FISSURE Playground 3: 9th-12th (1-2 vs G2 in the elimination match: won Dust2 13-11, lost Ancient "
        "8-13 and Inferno 10-13)"
    )

    betboom = teams["betboom"]["season_2026"]
    betboom.append(
        "FISSURE Playground 3: 3rd-4th (topped the group 3-0 incl. the org's first win over the Astralis "
        "tag; lost the semi 1-2 to G2). S1ren called it 'a ramp-up' for the ~20-day Europe trip (EPL S24 - TWC - Bucharest)"
    )

    parivision = teams["parivision"]["season_2026"]
    parivision.append(
        "FISSURE Playground 3: 9th-12th (0-2 vs magic; Inferno lost 14-16 in OT after leading 12-6) - "
        "HLTV: 'continuing their slide down the rankings'"
    )

    vp = teams["virtuspro"]["season_2026"]
    vp.append(
        "TWC will be VP's first big international LAN since IEM Chengdu 2025 (only b1st and tO0RO remain "
        "from that roster); the GQ title lifted them into the VRS top 30 (Sept 16 HLTV) from below #100 "
        "pre-rebuild, giving them 'a slim chance to qualify for the Singapore Major'"
    )

    # ---- pre-event calendar: FPG3 block + Bucharest qualifier update -------
    cal = data["tournament"]["pre_event_calendar"]
    assert "fissure_playground_3" not in cal
    cal["fissure_playground_3"] = {
        "dates": "Sept 8-13, 2026 (Suzhou, China; $1,000,000; 16 teams)",
        "twc_teams": "Legacy champions (3-0 vs G2; latto MVP), BetBoom 3rd-4th, FURIA 5th-6th (0-2 vs G2), 9z and PARIVISION 9th-12th; Falcons, Aurora and Virtus.pro did not attend",
        "why_it_matters": "Last completed Tier-1 event with Finals teams before TWC; FURIA's OT loss to G2 (11-7 lead lost) extended the 'labored season' narrative, Legacy banked their third straight Chinese title, and BetBoom swept a group containing Astralis and MIBR. EVPs: n1ssim, NertZ, nqz.",
        "source": "https://www.hltv.org/events/8266/fissure-playground-3",
    }
    pgl = cal["pgl_masters_bucharest"]
    pgl["why_it_matters"] += (
        " The 16-team field was completed on Sept 13: Nemiga, DENDELE, Liquid and TYLOO won the qualifiers "
        "(entry 93), joining the five TWC teams (FURIA, Legacy, Aurora, 9z, BetBoom) plus Spirit, MOUZ, "
        "Vitality, FUT, G2, NAVI and The MongolZ."
    )
    pgl["sources"].append("https://www.hltv.org/news/45513/liquid-tyloo-dendele-and-nemiga-qualify-for-pgl-masters-bucharest")

    # ---- new block: 2027 horizon (entries 94-95) ---------------------------
    assert "horizon_2027" not in data
    data["horizon_2027"] = {
        "majors": {
            "first_major_2027": "Buenos Aires (FiReSPORTS)",
            "second_major_2027": "Shanghai (Perfect World), Nov 22 - Dec 12, 2027, four stages, expected $1.25M (confirmed Sept 15, 2026)",
            "majors_2028": "BLAST and ESL won the 2028 Major bids (HLTV)",
        },
        "esports_world_cup_2027": {
            "dates": "July 20 - August 1, 2027",
            "format": "32 teams, $2M; slots: 20 Global VRS + 2 NA + 2 SA + 2 Asia + 2 wildcard + 4 Riyadh open qualifier (July 16-18)",
            "ewc_2028": "tentatively July 14-30, 2028",
        },
        "note": "TWC 2026's VRS weight feeds invitation standings that reach as far as EWC 2027.",
        "sources": [
            "https://www.hltv.org/news/45512/perfect-world-confirms-shanghai-as-host-city-of-second-2027-major",
            "https://www.hltv.org/news/45521/esports-world-cup-2027-and-2028-dates-revealed",
        ],
    }

    # ---- timeline insertions (must stay sorted) ----------------------------
    tl = data["roster_changes_timeline"]
    assert len(tl) == 40
    tl = insert_sorted(tl, {
        "date": "2026-09-11",
        "team": "Aurora",
        "change": "Ex-coach Fabre (benched June 29) appointed Eternal Fire head coach - reunites with jottAAA and soulfly at the rebuilt international EF (#67 VRS)",
        "source": "https://www.hltv.org/news/45503/fabre-returns-to-eternal-fire",
    })
    tl = insert_sorted(tl, {
        "date": "2026-09-13",
        "team": "Legacy / BetBoom / FURIA / 9z / PARIVISION",
        "change": "FISSURE Playground 3 (Suzhou, Sept 8-13): Legacy champions (3-0 vs G2, latto MVP 1.67 in the final); BetBoom 3rd-4th; FURIA 5th-6th (0-2 vs G2); 9z and PARIVISION 9th-12th",
        "source": "https://www.hltv.org/events/8266/fissure-playground-3",
    })
    tl = insert_sorted(tl, {
        "date": "2026-09-20",
        "team": "FURIA",
        "change": "molodoy's eye condition: needs surgery (pressure behind the eyes causing migraines; tablets ineffective; surgery planned in Kazakhstan) - KSCERATO's StarSeries top-EVP load 'There is more pressure on KSCERATO to deliver'",
        "source": "https://www.hltv.org/news/45564/the-evps-and-all-stars-of-starladder-starseries-fall-2026",
    })
    tl = insert_sorted(tl, {
        "date": "2026-09-22",
        "team": "Ecosystem",
        "change": "BC.Game bench electroNic, sign asap (ex-THUNDER dOWNUNDER) and switch from the Europe VRS (36th) to the Asia VRS (1,191 pts would rank 4th; 5 Asian invites) - s1mple, Magisk, Senzu, mzinho project coached by TaZ",
        "source": "https://www.hltv.org/news/45566/official-bcgame-add-asap",
    })
    tl = insert_sorted(tl, {
        "date": "2026-09-23",
        "team": "Ecosystem",
        "change": "Complexity cease operations (Jason Lake departs after 23 years; brand reverts to GameSquare) and ODDIK pause operations indefinitely - two org-level contractions in one day around the TWC scene",
        "source": "https://www.hltv.org/news/45568/complexity-ceases-operations-and-jason-lake-departs-after-23-years",
    })
    data["roster_changes_timeline"] = tl

    # ---- irregularity #20 ---------------------------------------------------
    assert len(data["irregularities"]) == 19
    data["irregularities"].append({
        "issue": "molodoy's eye condition: material claim with partly social/broadcast sourcing",
        "detail": "The surgery detail (pressure behind the eyes causing migraines, tablets ineffective, operation planned in Kazakhstan) comes from the Sept 20 StarLadder broadcast relayed by caster NarT on X plus a hawk.live report; HLTV's StarSeries EVP piece (Sept 23) confirms only that 'molodoy's eye issues' exist. The injury itself dates to pre-EWC reports (Aug 9-11). It is material to FURIA's Finals outlook, but no club or player statement has been issued.",
        "resolution": "The claim is published with all three sources linked (ledger entry 85) and flagged here; it should be re-checked against FURIA's official channels before being used in pricing decisions.",
    })

    # ---- limitations refresh -------------------------------------------------
    data["limitations"] = [
        "Match/outright odds for TWC 2026 were still not published at the fifth-pass re-check (Sept 24, 2026): esportbet's TWC hub still showed odds 'available closer to kickoff'. The betting analysis is a framework plus verified form data, not live prices.",
        "The group draw and day-by-day match schedule are still unpublished as of the Sept 24 pass-5 re-check (the event page shows TBD brackets). The seed order shown is inferred from the Sept 7 VRS.",
        "ESL Pro League S24 round-one pairings were not yet published as of Sept 24 (the event page shows a placeholder grid); EPL results (Oct 3-11) for the seven attending TWC teams are the most important missing signal.",
        "molodoy's surgery timing is open: if it happens before mid-October it materially changes FURIA's Finals outlook (source is partly social/broadcast, flagged in irregularity terms in the ledger).",
        "HLTV player statistics for the Finals will only exist after the event; linked for post-event review.",
        "Head-to-head data covers all four 2026 FURIA-Falcons meetings plus the 2025 BLAST Rivals final; full H2H scraping (all 28 pairings, all maps) is future work.",
        "Map-pool win rates (pass 5) are 3-month samples including online play and, for Virtus.pro, non-tier-1 opposition; they are context inputs, not probabilities, and unplayed maps are not confirmed perma-bans.",
        "Some primary sources are X/Twitter posts or Google Drive files (the rulebook) which may require login or change without notice.",
        "Rankings move weekly (HLTV) and per snapshot (Valve). Every rank figure on the site is labeled with its system and date. The Oct 5 VRS snapshot will change the numbers but not the seeding (which uses September).",
        "Any post-Sept 24 roster news, EPL S24 results, the group draw and opening odds remain uncaptured and must be added in a follow-up pass before Oct 14.",
    ]

    DATA.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: twc2026.json updated (timeline rows: {len(data['roster_changes_timeline'])}, "
          f"irregularities: {len(data['irregularities'])}, new blocks: map_pool_win_rates, horizon_2027, fissure_playground_3)")


if __name__ == "__main__":
    main()
