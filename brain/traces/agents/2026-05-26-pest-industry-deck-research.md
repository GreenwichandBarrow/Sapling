---
schema_version: 1.0.0
date: 2026-05-26
task: Gather source material for pest management industry section of CIM deck (investor-facing)
agents: [insurance-deck-loader, pest-corpus-loader, conference-call-loader, web-fetcher]
status: active
linked_trace: brain/traces/2026-05-26-pest-cim-industry-deck-outline.md
---

# Agent Chatroom: Pest Industry CIM Deck Research

## Task Context

Kay is building the industry section of a CIM deck for a pest management acquisition. Audience = investors. Modeled on the existing "Specialty Insurance Brokerage Analysis 1.7.26" deck in Drive.

Need to gather:
1. Insurance reference deck structure (template to mirror)
2. Pest one-pager + scorecard + Pest Gemini Industry Research 5.26.26
3. Bill Hoffman NJPMA conference Granola note + today's Oswaldo Ponce call (75¢/$1.50 quote)
4. Capstone pest sector update + Potomac Company pest-deal references

First deliverable: proposed slide outline mirroring insurance deck's structure with pest content mapped. Then iterate slide-by-slide.

## Coordination Log

## [now] orchestrator
Spawning 4 agents in parallel. Each focused on one source bucket. Independent reads — no expected cross-dependencies, but post discoveries that should change another agent's approach.

## [23:19] insurance-deck-loader
Found deck — `Specialty Insurance Brokerage Analysis 1.7.26.pptx` (ID `1RHTLlwPuY_HQo3VGkMkMPL00sFstaMRY`, 4.6 MB). Downloading + parsing slide XML now.
→ WAITING for parse

## [23:20] pest-corpus-loader
Starting. Vault has 5 candidate files (10-co June experiment plan, holdco architecture discussion, 20 women-owned West Village, 10-co experiment trace, 2 entity stubs). No file matches "one-pager" or "scorecard" by name in vault. Searching Drive in parallel.
→ READY

## [23:19] web-fetcher
Starting. Fetching Capstone Partners pest sector article first (primary source), then Potomac Company site for pest/services transaction list + team.
→ READY

## [23:25] web-fetcher
DONE. Both sources extracted.

**Capstone (Jan 30 2025, Izzy Jack):** Global pest $24.4B 2024 → $49.7B 2034 @ 6.5% CAGR (Future Market Insights). 2024 M&A: 97 deals, +27.6% YoY, 50.5% strategic / 49.5% financial, add-ons +29.4% YoY. Rollins 32 deals/$106M Q1-Q3, Rentokil 23 deals/$255.1M Q1-Q3. Rentokil/Terminix Dec 2021: 3.7x EV/Rev, 19.9x EV/EBITDA ($7.6B). 16 named transactions extracted. PE platforms: Certus (Imperial), Rockit (Halle), PestCo (TSCP), Barefoot (Incline), Action (Shore), Senske (GCTR). Aptive→Citation Capital Aug 2024 — Aptive $450.5M rev 2023 (+9% YoY), #5 N.Am residential. 5 pull-quotes ready — Kenneth Wasik anchor: "one of the strongest sectors in the Consumer industry and one of the most prolific M&A sectors due to annuity revenues, leverage, and ease of integration." NO sub-segment quantitative breakdown, NO EBITDA margin data — gaps for other sources to fill.

**Potomac:** Sell-side pest specialist boutique. Claim: "Since 2003, advised on hundreds of transactions in pest control — totaling more than $10 billion." 21 of 24 deals 2022-2025 are pest (87.5%). Notable 2024-2025 closes: Saela→Rollins, ProActive→Greenix, Spidexx→Greenix, Hargrove→Rollins, Beaver UK→Orkin, Eitan Amichai (Israel)→Rentokil, multiple Barefoot/PestCo/Anticimex platform adds, Bug House→Rollins. Sole named pest advisor: **Paul Giannamore, Managing Director** — author of all 14 pest-specific commentary posts dating to 2018 (notably "I'm Calling a Top" Nov 2018, "Beginning of the End? Multiples Contract" Jan 2020 post-ServiceMaster). No team page on site. Useful Potomac-as-Cap-IQ-proxy for full deal list + Giannamore as a name to drop in deck.

Full digest returned to orchestrator.
→ DONE

## [23:21] conference-call-loader
Starting. NJPMA/Hoffman note FOUND: `brain/library/internal/pest-management/2026-04-29-hoffman-exterminating-presentation.md` (NJPMA Business Management Workshop, Topgolf Edison NJ, 2026-04-29 Hour 1; Granola id `1909eae1-cb25-4f37-a2e0-15bf780df706`). Oswaldo Ponce call from today: post-call-analyzer queue STUCK (queue file `not_Gn4BVFoV13pDKF.json` queued 13:00 ET, no vault note). Pulling transcript directly from Granola API.
→ READY

## [23:20] insurance-deck-loader
Deck parsed — 16 slides total. Structure: cover → TOC → Exec Summary → Investment Highlights (slides 5-8: Tailwinds, Why Specialty Brokerages Capture It, Why Fits Search Fund, Value Creation Drivers) → Industry Overview (slides 10-16: Global Market sizing, US Market Structure, Consolidation Trend, Competitive Landscape, Client Segments, Regulatory, Risks). All slides watermarked "WIP" + footer "Strictly Confidential". Note: only Investment Highlights + Industry Overview sections built so far — Company / Operations / KPIs / Historical Financials / Growth / Risks / Appendix listed in TOC but NOT in deck (deal-side sections still empty).
Full outline in agent response.
→ READY

## [23:24] conference-call-loader
DONE. Both extracts gathered.

**NJPMA/Hoffman:** Full notes at `brain/library/internal/pest-management/2026-04-29-hoffman-exterminating-presentation.md`. Date 2026-04-29, Topgolf Edison NJ. Hoffman = President Hoffman Exterminating Co (NJ), Hour 1 speaker. Key content: community-aspect framing, 20-year consolidation table (Terminix sub-$1B 2005 → Rentokil $3.4B / Rollins $3.3B / Anticimex $625M 2025), NJ-specific Annie CMEX #1 + Ned's $140M (gutter-cleaning crossover), 4 consolidation drivers, "everyone has been approached to sell" + "when they are ready, it IS worth something," P×4 succession framework, $1-3M EBITDA tier still at 4-5x while $3M+ at 6-8x. Note: source file shows "Annie Seix" / "Annie CMEX" — those are transcription artifacts of **Anticimex** (Swedish-headquartered pest co), should be corrected when used in deck.

**Oswaldo Ponce 5/26 noon ET call:** Granola note `not_Gn4BVFoV13pDKF` STILL stuck in post-call-analyzer queue (vault note not written, headless wrapper crashed per session-decisions 5/26 open loop #4). Pulled transcript directly via `granola-api get-note`. Pest-specific quote NOT the "75¢ → $1.50" Kay paraphrased — actual mechanic is account ARR multiple arbitrage, more nuanced and more useful for the deck. Verbatim block in main output. Saved transcript at `/tmp/ponce_transcript.txt` (1011 segments, 33.6K chars).

Returning to orchestrator.
→ READY

## [23:22] pest-corpus-loader
Located all 4 artifacts. Folder = `1RavIVgtU6ZBuM51c7zZYnBFm9aNl7M2x` (likely INDUSTRY RESEARCH/Pest):
1. **Pest Gemini Industry Research 5.26.26** — Doc `1MMtjEvk2HUcRUZVuNBKQvkKA_aFNHVHkca00ybkEhTs` (exported, 30KB markdown, Northeast/NYC+LI luxury thesis, Bill Hoffman playbook reference)
2. **Premium Pest Management 4.20.26.pptx** — `1zGHXMAB7NkrSo33undB-1KbYO6mhhF3A`, 1 slide = THE ONE-PAGER (2.73/3.0 = 91% scorecard total)
3. **Premium Pest Management Scorecard 4.4.26.xlsx** — `1glvHJzMM5-lg4KzVDjOmphq5PD6Lot7z`, two sheets (Initial Screen PASS, Industry Scorecard 2.73)
4. **Premium Pest Management - Industry Insights** (Google Slides) — `1dOuzxIiMit2IOBf5Ut8PgMAab4_1jGPWE2bXXmfQWYo`, 12 slides = NJPMA Hoffman + Falcey conference log + multiples context

ALSO FOUND: **Pest Management Analysis 5.18.26v2.pptx** (`1Rgnqoo6WwqsjrL3mUZxZgt_c9u-w716G`) — INCOMPLETE shell deck. Slides 1, 2, 3 = pest-specific (TOC, "Scrap Paper" brainstorm). Slides 4-17 = INSURANCE template content NOT yet swapped to pest. This is the deck Kay is building. @insurance-deck-loader: this is your template-already-applied-to-pest-but-WIP file. Worth knowing.

Vault: `outputs/2026-05-08-discussion-pest-control-holdco-architecture.md` is the master thesis (Wertheimer/19yr/Operating Holdco anchored on pest roll-up + Pest AI Co + FO LLC). Also `outputs/2026-05-15-pest-20-women-owned-west-village.md`, `outputs/2026-05-26-pest-10-co-june-experiment-plan.md`.

Returning digest to orchestrator now.
→ DONE

## [now] orchestrator
All 4 agents complete. Material findings collected:
- Insurance deck template: 16 slides, industry-thesis half of CIM
- WIP pest CIM exists: `Pest Management Analysis 5.18.26v2.pptx` (1Rgnqoo6WwqsjrL3mUZxZgt_c9u-w716G), slides 1-3 pest, slides 4-17 still insurance — swap-target identified
- Pest one-pager + scorecard (2.73/3.0) + Gemini Research (today) + Hoffman NJPMA + Ponce ARR-arb mechanic + Capstone 97-deal data + Potomac/Giannamore sell-side benchmark + named PE platforms

Synthesizing to slide outline for Kay's approval.
→ CLOSE
