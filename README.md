# THUNDERPICK WC 2026 — Expert Hub

An expert research hub and static website covering the **Thunderpick World Championship 2026** (Counter-Strike 2, October 14–18, 2026, BLAST Studios Malta, $1,000,000).

**Live site:** https://buffedlizard55-lab.github.io/THUNDERPICK-WC-2026/

## What this project is

A verified, source-linked knowledge base for the tournament, aimed at readers who already understand betting markets and want clean, trustworthy CS2 data:

- **Tournament overview** — dates, format, prize distribution, circuit (regional series + qualifier), map pool, broadcast
- **Teams & full rosters** — the 8 finalists, 40 players + 8 coaches, ranks pinned to exact dates, bench/reserve status
- **Stats & form** — dated VRS/HLTV snapshots and recent form signals, with a hard boundary around unavailable event stats
- **Roster change tracker** — every verified transfer/benching/signing affecting the field, with dates, sources and impact notes
- **Betting guide** — format implications for markets, favorites/dark horses with verified form data, risk register (educational; no odds are invented)
- **CS2 universe guide** — game rules, ecosystem (VRS, Majors, tiers), 2026 meta and map pool
- **Verified master list** — an audit ledger: 80 research entries (four passes of 20, each verified line-by-line before being added), plus 19 flagged irregularities, limitations and the complete source directory

## The no-hallucination rule

Every factual claim on the site links to at least one public source (HLTV, Liquipedia, Valve's official VRS GitHub, official press releases, reputable specialist press) for manual review. Where sources disagree, the conflict is **flagged, not smoothed over** — see the [Irregularities section](master-list.html) of the master list.

Key verification anchors:

| Data | Source of truth | Snapshot date |
|---|---|---|
| Finals field & rosters | Liquipedia TWC 2026 + HLTV event page | Sept 24, 2026 |
| Invite basis | Valve VRS Global (official GitHub) | Aug 3, 2026 |
| Latest Valve ranks | Valve VRS Global (official GitHub) | Sept 7, 2026 |
| HLTV world ranking | HLTV ranking page | Sept 21, 2026 |
| Live Valve ranks (HLTV badges) | HLTV event page | Sept 23, 2026 |
| Finals-week schedule | Official TWC site | Sept 23, 2026 |
| Roster changes | HLTV news / official club announcements | per event date |
| Prize pool & format | Official Thunderpick releases + Liquipedia | Sept 23, 2026 |
| Rules (roster, stand-in, veto, server, forfeits) | TWC 2026 Official Rulebook (Google Drive PDF dated 01.07.2026, marked "[INTERNAL]") | Sept 24, 2026 |
| Seeding basis | Valve VRS Global Sept 7, 2026 (rulebook/official page: "September VRS") | Sept 24, 2026 |
| Pre-event calendar (StarSeries, BLAST Open Porto, EPL S24, patch, Major cutoff) | HLTV, BLAST.tv, Liquipedia, PGL coverage | Sept 24, 2026 |
| 2025 player ranking | HLTV Top 20 of 2025 (final list) | Jan 10, 2026 |
| Regional series results | HLTV event pages / Liquipedia / Hotspawn | per event date |
| Global Qualifier (format, slots, placings) | Official TWC GQ page + HLTV event 9308 | Sept 24, 2026 |
| PGL Masters Bucharest (Oct 24–31) | Liquipedia + TalkEsport + ShaneTheGamer | Sept 24, 2026 |
| EPL S24 field & acceptances | HLTV news + Insider Gaming | Sept 24, 2026 |
| Odds availability | esportbet TWC hub + esportsinsider | Sept 24, 2026 |

## Repository structure

```
├── README.md                  ← this file
├── .nojekyll                  ← tells GitHub Pages to serve files verbatim
├── data/
│   ├── twc2026.json           ← machine-readable master data (teams, rosters, changes, flags)
│   └── research-ledger.json   ← 80 dated research entries (20 per pass) and source links
├── scripts/
│   └── verify_site.py         ← zero-dependency local integrity check
├── assets/
│   └── style.css              ← design system (no JS dependencies)
├── index.html                 ← tournament overview          (GitHub Pages serves
├── teams.html                 ← the 8 teams & rosters          this repo root as
├── players.html               ← all players & coaches          the website)
├── stats.html                 ← pre-event stats & form signals
├── roster-changes.html        ← change tracker / timeline
├── betting-guide.html         ← betting framework (educational)
├── cs2-guide.html             ← Counter-Strike 2 primer
└── master-list.html           ← verification ledger & sources
```

The site is dependency-free HTML/CSS (no build step, no tracking, no external scripts). Pages is configured to serve the **root of `main`** — a `.nojekyll` file keeps assets served verbatim.

## Data status & known limitations

- **Data cutoff: September 24, 2026 (passes 1–2 on Sept 23, passes 3–4 on Sept 24).** Roster moves, the group draw, the schedule and odds released after this date are not yet captured.
- Outright/match odds for TWC 2026 were **still not published** at the fourth-pass check (Sept 24: esportbet hub shows "Odds … are not available"; esportsinsider carried no futures); the betting guide deliberately contains no invented prices — only verified historical results and a framework.
- Group draw and day-by-day schedule: **TBD** (to be added when published). The finals-week structure (arrival Oct 12 → departure Oct 19; match days Oct 14–18) is verified from the official site.
- Some primary sources are X/Twitter posts (e.g., PARIVISION's announcements) or a Google Drive PDF (the rulebook, marked "[INTERNAL]" with stale 2025 text) that may require login or change without notice.
- Seed order is **inferred** from the Sept 7 VRS; the seed-to-group mapping is unpublished.
- **ESL Pro League S24 (Oct 3–11)** involves 7 of 8 TWC teams and ends 3 days before TWC; its results are not captured yet and are the most important remaining pre-event signal.
- Rankings move weekly (HLTV) / per-snapshot (Valve) / continuously (HLTV's live Valve badge); every rank figure on the site is labeled with system + date.
- Second-pass additions: previous editions' full context (2023 FaZe, 2024 The MongolZ in Berlin, 2025 FURIA), all five 2026 regional series results, HLTV's 2025 Top 20 (six Finals players), the complete FURIA–Falcons H2H (Falcons 4–0 in 2026), CS2 MR12 rules, VRS mechanics, and the BetBoom visa/ArtFr0st chain.
- Fourth-pass additions (entries 61–80): the Global Qualifier deep-dive (format, slots, full placings, 100 Thieves with device/rain, the official-page "four teams" contradiction, September-VRS seeding, slot-only reward), field absences (Spirit/Vitality/MOUZ/NAVI/G2 out; only FURIA of the past champions), The MongolZ crisis (tikuak/DarkMeister signed July, benched Sept 15), HObbit's 2017 Kraków Major pedigree and June–July stand-in stint, PGL Masters Bucharest (Oct 24–31: format, Oct 5 VRS seeding, five TWC teams in the field, Falcons skip), the "final VRS opportunity" conflict, EPL S24 field checks (1win = TDK core + fame + BELCHONOKK), dated odds status, broadcast TBA, the per-place 50/50 prize-share table, and two disclosure notes (HLTV/Dexerto are listed event partners; Thunderpick books markets on its own event). **New flags:** irregularities #18 (official GQ page self-contradiction) and #19 (the "final opportunity" claim).
- Third-pass additions (entries 41–60): rulebook rules (3-of-5 core-roster rule, stand-ins, veto order, $12,500 OT, forfeits, withdrawal, integrity), Sept VRS seeding, Schengen logistics, the EPL S24 clash, StarSeries Fall (Aurora 2nd, FURIA 3rd), BLAST Open Porto, YEKINDAR's calling change, the Sept 22 CS2 update, the Nov 2 Major VRS cutoff. **Corrections:** BetBoom at the Cologne Major (S1ren, not d1Ledez, was absent), overtime money (entry 37), Magisk and fame records.

## Next steps (planned for a follow-up session)

1. Refresh after ESL Pro League S24 ends (Oct 11) and before Oct 14: EPL results per TWC team, group draw, schedule, late roster moves/stand-ins (check against the 3-of-5 core rule).
1b. Track The MongolZ (three active players since Sept 15) and PGL Masters Bucharest (Oct 24–31) outcomes — both move the VRS/Major picture around TWC.
2. Capture opening odds (Thunderpick + aggregators) when posted, with timestamps.
3. Add per-map team profiles (map win rates) once sample sizes justify it.
4. Automate weekly VRS/HLTV rank snapshots from Valve's machine-readable GitHub data.
5. Post-event: results, final prize distribution, and a prediction-vs-outcome review.

## Updating the site

Run `python3 scripts/verify_site.py` before publishing. It checks the eight-team/roster shape, the 80-entry ledger (four passes) and its mirror on the Verified List page, the data blocks (live Valve ranks, finals-week schedule, rulebook rules, pre-event calendar, Global Qualifier block), timeline order/duplicates, retired (corrected) claims, reserve fields, and local links including #anchors; it does not replace manual review of remote sources.

Edit the root HTML files (and mirror structural data changes into `data/twc2026.json` and `data/research-ledger.json`), commit to a branch, open a PR, and merge — GitHub Pages serves the repository root from `main` (`.nojekyll` is present).

## Disclaimer

This is an independent, unofficial research project. It is informational only, provides no betting advice, and is not affiliated with Thunderpick, GAM3RS_X, GRID, Valve, or any team. Esports betting carries risk; 18+/21+ depending on jurisdiction.
