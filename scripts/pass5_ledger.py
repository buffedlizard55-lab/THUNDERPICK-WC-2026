#!/usr/bin/env python3
"""Pass 5 (Sept 24, 2026): append verified entries 81-100 to the research ledger.

Every entry below was verified line-by-line against the linked source on
Sept 24, 2026 (see the pass-5 section of master-list.html for the audit trail).
Run from the repo root:  python3 scripts/pass5_ledger.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "data" / "research-ledger.json"

ENTRIES = [
    {
        "id": 81,
        "claim": "FISSURE Playground 3 (Sept 8-13, Suzhou, $1,000,000, 16 teams) - the last completed event with Finals teams before TWC - ended with Legacy champions, BetBoom 3rd-4th, FURIA 5th-6th, and both 9z and PARIVISION eliminated at 9th-12th; Falcons, Aurora and Virtus.pro did not attend.",
        "detail": "Legacy swept G2 3-0 in the final (Ancient 13-9, Mirage 13-10, Dust2 13-4). FURIA lost their quarter-final 0-2 to G2 (Ancient 14-16 in OT after leading 11-7; Dust2 3-13) and had also lost to Legacy in the group stage. BetBoom topped their group 3-0 and lost the semi-final 1-2 to G2. 9z fell 1-2 to G2 in an elimination match (Dust2 13-11 won; Ancient 8-13; Inferno 10-13). PARIVISION lost 0-2 to magic (Ancient 11-13; Inferno 14-16 in OT after leading 12-6) and, per HLTV, 'continue their slide down the rankings'.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/events/8266/fissure-playground-3",
            "https://www.hltv.org/news/45509/legacy-sweep-g2-to-lift-fissure-playground-3-trophy",
            "https://www.hltv.org/news/45502/g2-smash-furia-on-dust2-to-secure-fpg-semi-finals",
            "https://www.hltv.org/news/45508/g2-move-past-betboom-en-route-to-fpg-3-final",
            "https://www.hltv.org/news/45491/9z-and-tyloo-bow-out-of-fpg-3",
            "https://www.hltv.org/news/45492/magic-dump-parivision-out-of-fpg-3",
        ],
    },
    {
        "id": 82,
        "claim": "BetBoom swept their FISSURE Playground 3 group (2-0 over BIG, 2-0 over Astralis - the organization's first-ever win over the Astralis tag - and 2-0 over MIBR) into the semi-finals, and S1ren called the event 'a ramp-up' for a roughly 20-day European trip (EPL S24 in Katowice, then TWC in Malta).",
        "detail": "S1ren (Sept 10): 'We're using this tournament as a ramp-up, because literally in about twenty days we're heading off on a big trip through Europe.' He cautioned that group-stage form does not predict playoffs - BetBoom went 3-0 in groups in Guangzhou earlier in the season and 'just got smashed' in the playoffs there.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45496/s1ren-the-experience-weve-built-up-should-help-us-in-the-playoffs",
            "https://www.hltv.org/news/45508/g2-move-past-betboom-en-route-to-fpg-3-final",
        ],
    },
    {
        "id": 83,
        "claim": "FalleN (Sept 12, after FURIA's FPG3 quarter-final exit): 'I know it's coming to an end, and I want to make the most of it' - the 35-year-old's end-of-2026 retirement looms over FURIA's season, and he described the travel grind of going 'from Paris to Porto and then China'.",
        "detail": "FURIA also lost to Legacy in Suzhou ('They have been playing very good Counter-Strike'). On the 0-2 defeat by G2: 'I guess we had to win the first map to actually have a chance in the series.' His retirement was originally announced on the IEM Rio stage in April 2026.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45506/fallen-i-know-its-coming-to-an-end-and-i-want-to-make-the-most-of-it",
            "https://www.hltv.org/news/44399/fallen-announces-he-will-retire-at-the-end-of-2026",
        ],
    },
    {
        "id": 84,
        "claim": "YEKINDAR (Sept 16, StarSeries media day) described FURIA's 2026 as title-free despite grand-final appearances at IEM Krakow and the IEM Cologne Major, said the team held a no-conflict meeting after the G2 loss, and framed the FalleN retirement pressure as 'everyone's individual responsibility to be the best version of themselves'.",
        "detail": "FURIA's two 2026 grand finals verified in the article: IEM Krakow and the IEM Cologne Major (0-3 vs Falcons). YEKINDAR on the team talk: 'Guys, we know FalleN is going to be retiring; we know we're playing bad right now. How can we fix it? That's basically the mojo.' He also admitted the back-to-back event schedule 'definitely hits you'.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45529/yekindar-on-pressure-of-fallen-retiring-its-everyones-individual-responsibility-to-be-the-best-version-of-themselves",
        ],
    },
    {
        "id": 85,
        "claim": "FURIA AWPer molodoy (HLTV #6 player of 2025) is playing through an eye condition that requires surgery: he posted photos of a swollen eye before EWC (reported Aug 9-11), and per the Sept 20 StarLadder broadcast he has pressure behind his eyes causing migraines, with tablets having little effect and surgery planned once he returns to Kazakhstan.",
        "detail": "HLTV's StarSeries EVP piece (Sept 23): 'There is more pressure on KSCERATO to deliver with molodoy's eye issues.' Watch item for TWC: any absence would reshape FURIA's ceiling, and the 3-of-5 core-roster rule (entry 41) limits replacements. Sources are an HLTV article, a specialist news post and an X post citing the broadcast - flagged accordingly.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45564/the-evps-and-all-stars-of-starladder-starseries-fall-2026",
            "https://x.com/NartOutHere/status/2101691201891999864",
            "https://hawk.live/posts/molodoy-suffers-injury-ahead-esports-world-cup-2026",
        ],
    },
    {
        "id": 86,
        "claim": "KSCERATO claimed the top EVP of StarSeries Fall 2026 (1.26 rating, 89.9 ADR) despite FURIA not reaching the final - his fourth consecutive event above a 1.20 rating, including a 1.23 rating against top-10 teams while his highest-rated teammate managed 0.97.",
        "detail": "HLTV credits him with seven standout maps, 'only two fewer than ZywOo', with big map wins against MOUZ and MIBR.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45564/the-evps-and-all-stars-of-starladder-starseries-fall-2026",
        ],
    },
    {
        "id": 87,
        "claim": "ZywOo earned an uncontested StarSeries Fall MVP - his fifth of 2026 (1.50 rating, +6.13% round swing) - as Vitality beat Aurora 3-1 in the final for their first title since May, resetting the benchmark the TWC field is measured against.",
        "detail": "ZywOo: 'I wanted at least one MVP for the second part of the season... So now it feels good to have this MVP.' ropz added an EVP (1.28 rating in map wins).",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45564/the-evps-and-all-stars-of-starladder-starseries-fall-2026",
            "https://www.hltv.org/news/45559/zywoo-claims-uncontested-starseries-fall-mvp",
            "https://www.hltv.org/news/45558/vitality-beat-aurora-at-starseries-fall-for-first-title-since-may",
        ],
    },
    {
        "id": 88,
        "claim": "Aurora's Jimpphat was the second-best player of StarSeries Fall: a series-high 1.36 rating in the upper-final win over Vitality, a 1.41 rating in map wins en route to the final, and his first EVP since IEM Rio at the end of 2024 - 'Recently I've just had such a crazy amount of confidence.'",
        "detail": "Aurora's run: 2-0 over NAVI, 2-0 over NRG, 2-1 over Vitality in the upper final, then a 1-3 grand-final loss to Vitality. HLTV credits coach ash with 'making good on his promise to make him a star anchor once more'.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45554/jimpphat-recently-ive-just-had-such-a-crazy-amount-of-confidence",
            "https://www.hltv.org/news/45564/the-evps-and-all-stars-of-starladder-starseries-fall-2026",
        ],
    },
    {
        "id": 89,
        "claim": "The FISSURE Playground 3 EVPs went to Legacy's n1ssim (1.20 rating; in the MVP race before the final), G2's NertZ (1.22 playoff rating; first EVP since IEM Rio 2024) and MIBR's nqz (1.21) - and HLTV notes n1ssim had benched himself in the summer, returning only after Legacy failed to replace him.",
        "detail": "latto took the MVP (entry 90). n1ssim's award is Legacy's second individual honor from the event and a marker of their top-heavy-but-deep form.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45563/the-evps-and-all-stars-of-fissure-playground-3",
        ],
    },
    {
        "id": 90,
        "claim": "latto (Legacy) is a three-time MVP in China - CAC 2025, CAC 2026 and FISSURE Playground 3, all three of Legacy's Chinese titles - and rated the FPG3 grand final (1.67 rating; a 2.25-rated Dust2) as the best performance of his career: 'It's China magic, I think.'",
        "detail": "With two MVP medals and two EVP awards in 2026 he is targeting a first HLTV Top 20 appearance after finishing in the 2025 Top 30; he credits mental work with BobZ, adrrr and arT and his partnership with dumau, together since 2021.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45511/latto-after-third-mvp-in-china-its-china-magic-i-think",
            "https://www.hltv.org/news/45563/the-evps-and-all-stars-of-fissure-playground-3",
            "https://www.hltv.org/news/45509/legacy-sweep-g2-to-lift-fissure-playground-3-trophy",
        ],
    },
    {
        "id": 91,
        "claim": "Aurora's former head coach Fabre (benched June 29, 2026) was appointed Eternal Fire head coach on September 11, reuniting with jottAAA and soulfly at the rebuilt, now-international Eternal Fire (ranked #47 HLTV / #67 VRS at the time).",
        "detail": "Fabre coached the Turkish core from 2022 to 2025 - overseeing Eternal Fire's PGL Major Copenhagen quarter-final and, after the roster's April 2025 move to Aurora, their IEM Cologne Major semi-final run - before being benched in Aurora's July international rebuild.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45503/fabre-returns-to-eternal-fire",
        ],
    },
    {
        "id": 92,
        "claim": "BC.Game benched electroNic and signed Australian asap (from THUNDER dOWNUNDER) on September 22 - a move that switches the s1mple-Magisk-Senzu-mzinho project (coached by TaZ) from the Europe VRS, where they sat 36th (outside the top-18 Singapore invite zone), to the Asia VRS, where their 1,191 points would currently rank 4th (five Asian invites).",
        "detail": "asap reached his first Major (IEM Cologne Major 2026) with THUNDER dOWNUNDER, posting a 1.24 rating in Stage 1 including a 2.04-rated BO1 win over MIBR. Relevant to TWC as ex-Falcons IGL Magisk's team and as an Asia Major-race marker (both ex-MongolZ players Senzu and mzinho stay).",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45566/official-bcgame-add-asap",
            "https://www.hltv.org/news/45565/bcgame-bench-electronic-sources-indicate-asap-as-replacement",
        ],
    },
    {
        "id": 93,
        "claim": "PGL Masters Bucharest's 16-team field was completed on September 13: Nemiga (Europe qualifier; swept B8 3-0 in the final), DENDELE (South America, beating Imperial and Fluxo twice), Liquid (North America) and TYLOO (Asia) joined the twelve VRS invites - including all five attending TWC teams (FURIA, Legacy, Aurora, 9z, BetBoom) plus Spirit, MOUZ, Vitality, FUT, G2, NAVI and The MongolZ.",
        "detail": "Bucharest (Oct 24-31, $1,250,000) starts six days after the TWC grand final; its results feed the Oct 5 and Nov 2 VRS snapshots used for Singapore Major invites and Bucharest seeding.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45513/liquid-tyloo-dendele-and-nemiga-qualify-for-pgl-masters-bucharest",
            "https://www.hltv.org/news/45146/falcons-the-only-top-team-to-skip-pgl-masters-bucharest-as-invites-are-announced",
        ],
    },
    {
        "id": 94,
        "claim": "Perfect World confirmed on September 15 that the second Major of 2027 will be hosted in Shanghai, slated for November 22 - December 12, 2027 over four stages with an expected $1.25 million prize pool; the first 2027 Major will be hosted by FiReSPORTS in Buenos Aires, and HLTV previously reported BLAST and ESL won the 2028 Major bids.",
        "detail": "Perfect World's second Major after Shanghai 2024 (won by Spirit over FaZe). Calendar context: the PGL Major Singapore 2026 (Nov 25 - Dec 13) remains the immediate horizon for TWC's VRS points.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45512/perfect-world-confirms-shanghai-as-host-city-of-second-2027-major",
        ],
    },
    {
        "id": 95,
        "claim": "Esports World Cup 2027 (July 20 - August 1, 2027) keeps CS2's expanded 32-team, $2 million format; its slot distribution is 20 Global VRS invites, 2 North American, 2 South American, 2 Asian and 2 wildcard invites plus 4 spots from the Riyadh open qualifier (July 16-18). EWC 2028 is tentatively scheduled for July 14-30, 2028.",
        "detail": "Calendar context: TWC 2026's VRS weight ($1,000,000) feeds invitation standings that reach as far as EWC 2027.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45521/esports-world-cup-2027-and-2028-dates-revealed",
            "https://esportsworldcup.com/en/news/counter-strike-2-returns-to-ewc-2027",
        ],
    },
    {
        "id": 96,
        "claim": "In the Americas VRS race for Singapore Major invites, BESTIA won Circuit X Curitiba Season 3 (Sept 17-20; +204 points, with drop named tournament MVP by Dust2 Brasil) to move joint-10th with Fluxo - just 14 Valve points outside the qualification zone - while paiN slide continued.",
        "detail": "BESTIA's first LAN with drop and kauez. paiN, the region's long-time #1, replaced piriajr with Tatu on September 14 (HLTV) amid the pressure. Context for the South American TWC teams (9z, Legacy) and the Major seeding picture.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45562/bestia-and-fluxo-breathing-down-pains-neck-in-americas-vrs-after-circuit-x-curitiba",
            "https://www.hltv.org/news/45517/official-tatu-replaces-piriajr-on-pain",
        ],
    },
    {
        "id": 97,
        "claim": "Complexity ceased operations, announced September 23: founder and CEO Jason Lake departed after 23 years and ownership of the brand reverted to GameSquare; the organization had exited Counter-Strike in August 2025 citing a 'challenging' esports economy.",
        "detail": "One of CS's most storied brands: first roster in 2004, 10 official Majors attended (best: 3rd-4th at DreamHack Winter 2013), titles at ESWC 2005, CPL Summer 2006 and ESL Challenger Jonkoping 2024. Lake: 'this is coL 1 signing out of Complexity, after 23 years.'",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45568/complexity-ceases-operations-and-jason-lake-departs-after-23-years",
        ],
    },
    {
        "id": 98,
        "claim": "Brazilian organization ODDIK suspended esports operations indefinitely with immediate effect (September 23), ending their Counter-Strike division; the org entered CS in June 2022, peaked at #28 in the HLTV rankings after PGL Astana 2025, benched diozera and nardes and released the remaining members as free agents.",
        "detail": "The second organization-level contraction of the week (after Complexity, Sept 23) and part of the South American scene backdrop behind 9z and Legacy.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45569/oddik-pause-esports-operations",
        ],
    },
    {
        "id": 99,
        "claim": "Virtus.pro had cratered below 100th on the VRS before their academy rebuild, then broke into the top 30 by winning the Thunderpick Global Qualifier - a run that began with a loss to K27 and continued with wins over BESTIA, K27, FOKUS, HEROIC (2-1) and HOTU (2-0 sweep in the decider); TWC will be VP's first big international LAN since IEM Chengdu 2025, with only b1st and tO0RO remaining from that roster.",
        "detail": "HLTV: the run gives VP 'a slim chance to qualify for the Singapore Major'. The rebuild was built around four former academy members plus mir.",
        "status": "verified",
        "sources": [
            "https://www.hltv.org/news/45514/virtuspro-enter-top-30-of-vrs-with-thunderpick-world-championship-qualification",
            "https://www.hltv.org/news/45525/falcons-and-furia-headline-thunderpick-world-championship-team-list",
        ],
    },
    {
        "id": 100,
        "claim": "Map-pool profiles from HLTV team stats (all maps played June 24 - September 24, 2026): FURIA Nuke 75.0% / Inferno 66.7% / Anubis 0.0%; Falcons Dust2 75.0% and Inferno 75.0% / Ancient 20.0% / Anubis 0.0% / zero Cache maps; Legacy Inferno 100.0% / Nuke 75.0% / zero Anubis maps; Aurora Nuke 100.0% / Ancient 0.0%; 9z Cache 66.7% / Ancient 25.0% / zero Anubis maps; BetBoom Dust2 100.0% / Mirage 75.0% / zero Inferno maps; PARIVISION Ancient 71.4% / Cache 0.0% / Inferno 20.0% / zero Nuke maps; Virtus.pro Ancient 87.5% / Dust2 72.2% / zero Inferno maps (VP's sample includes non-tier-1 opposition).",
        "detail": "Veto-relevant inputs for the betting guide. 'Zero maps' means exactly that in the 3-month window (online + LAN) - not a confirmed perma-ban, which is not published. Sample sizes per map are small (roughly 5-18 maps); rates are context, not probabilities.",
        "status": "verified",
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
    },
]


def main() -> None:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    entries = ledger["entries"]
    assert [e["id"] for e in entries] == list(range(1, 81)), "expected ledger 1..80 before pass 5"
    assert len(ENTRIES) == 20, "pass 5 must add exactly 20 entries"
    assert [e["id"] for e in ENTRIES] == list(range(81, 101))
    entries.extend(ENTRIES)

    ledger["reviewed_as_of"] = "2026-09-24 (pass 5: entries 81-100)"
    ledger["method"] = (
        "Each claim is checked line-by-line against the linked public source text or structured "
        "record before it is added; every entry carries at least one review URL. Five passes of 20 "
        "entries: passes 1-2 on Sept 23, passes 3-4 on Sept 24 (entries 1-80), pass 5 on Sept 24 "
        "(entries 81-100: FISSURE Playground 3 results and interviews, molodoy's eye condition, "
        "StarSeries MVP/EVPs, the PGL Masters Bucharest qualifier field, the 2027 Major/EWC "
        "calendar, the Americas VRS race, org closures, Virtus.pro's VRS trajectory, and 3-month "
        "map-pool win rates for all eight teams). Source conflicts and moving rankings stay visible; "
        "see the Irregularities section of master-list.html."
    )
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"OK: ledger now has {len(entries)} entries (IDs 1..{entries[-1]['id']})")


if __name__ == "__main__":
    main()
