---
schema_version: 1.0.0
date: 2026-05-19
type: output
output_type: niche-intelligence-report
status: complete
run_mode: tuesday
people:
  - "[[entities/august-felker]]"
  - "[[entities/hunter-hartwell]]"
  - "[[entities/jeremy-black]]"
  - "[[entities/jeff-stevens]]"
  - "[[entities/carlos-nieto]]"
  - "[[entities/camilla-rojas]]"
tags:
  - output
  - date/2026-05-19
  - output/niche-intelligence-report
  - topic/niche-intelligence
  - source/niche-intelligence
  - person/august-felker
  - person/hunter-hartwell
  - person/jeremy-black
  - person/jeff-stevens
  - status/complete
related:
  - "[[traces/agents/2026-05-19-niche-intelligence]]"
  - "[[trackers/niches/niche-intel-2026-05-19]]"
  - "[[outputs/2026-05-12-niche-intelligence-report]]"
---

# Niche Intelligence Report — Tuesday 2026-05-19

Headless launchd Tuesday run. Pipeline executed: GATHER (parallel) → SYNTHESIZE → IDENTIFY → ONE-PAGER (refresh) → SCORE (re-score) → UPDATE (tracker).

Chatroom trace: [[traces/agents/2026-05-19-niche-intelligence]]

## TL;DR

**Zero NEW niches added to WEEKLY REVIEW this week. Pipeline depth, not breadth, is the right move.**

Both gathering agents converged on the same recommendation: G&B walks into Wednesday's analyst call with **7 unprocessed candidates from last week** (rows 9-15 — Trade Credit/Customs/Cargo, Property Tax Appeal, OSHA Workplace H&S Training, Aviation Insurance, HNW Personal Lines Concierge, Funeral Home Software, Surplus Lines Compliance) **plus 8 active sprints**. The synthesizer evaluated 17 niche/signal candidates against the cross-source matrix and the identifier ran them against the 4-gate INITIAL SCREEN. Zero net-new candidates cleared the KILLED/TABLED/ACTIVE filter with 2+ source confirmation. The convergent signal this cycle reinforces existing rows rather than expanding the search frontier.

**Two depth actions executed instead:**

1. **WEEKLY REVIEW row 13 (HNW Personal Lines Concierge Insurance Brokerage) re-scored 2.53 → 2.65** (+0.12) on new historical evidence: August Felker 11/19 endorsement of the "two-women-retiring HNW personal-lines-only" target archetype as the platonic version of the niche, plus Hunter Hartwell 1/12 carve-out workaround for the 12-14x multiple wall. Scorecard xlsx + one-pager pptx both refreshed and re-uploaded to Drive.

2. **WEEKLY REVIEW row 4 (Specialty Coffee Equipment Service) one-pager refreshed** with the unanswered Jeff Stevens 4/22 diagnostic ("do mid-sized regional chains in/outsource servicing?") and Carlos Nieto 5/13 peer-searcher convergence. Score unchanged at 2.55; the diagnostic now lives in the body so the analyst call can decide pipeline expansion beyond pure-play artisan cafés.

**Headline message for the analyst call:** the cleanest research-history target archetype on file (Aug Felker's "two-women-retiring HNW personal-lines" brokerage) maps directly to a row that has been sitting in "New - Pending Review" for a week. The depth move is to advance row 13 to **Active - Outreach** with a single-question warm-rekindle to Aug Felker (asking for the named target). Row 9 (Trade Credit / Customs / Cargo) and row 4 (Specialty Coffee Equipment) carry the next-most-actionable depth.

## What Each Sub-Agent Did

| Sub-agent | Status | Output |
|---|---|---|
| `niche-intel-recent` | complete | 7/7 sources scanned (newsletters, deal flow, investor inbox, vault calls, vault outputs, inbox signals, web). Granola MCP unavailable (PKCE OAuth headless-incompatible — same as 5/12); fell back to `brain/calls/` for 14-day window. `last30days.py` not on VPS; substituted 2 WebSearch queries. 9 raw signals surfaced — top signal: PE-backed specialty/P&C insurance brokerage M&A wave at $500K-$10M revenue band reinforcing **five** pipeline rows. |
| `niche-intel-historical` | partial | 4 sub-agents executed sequentially (Agent tool unavailable in env). 22 historical call notes (Aug 2025 - Apr 2026), 120+ Gmail thread metadata + 1 deep-read (Jeremy Black 2/3 specialty insurance email), ChatGPT export pre-processed into memory files (`project_thesis_evolution.md`, `project_deal_history.md`, `project_network_contacts.md`). OneNote MCP unavailable. 0 net-new proposable niches; recommendation: depth, not breadth. |
| `niche-intel-synthesizer` | complete | 5 outputs delivered: Cross-Source Signal Matrix (17 niches), Named Company Registry (15 companies, 3 NEW_TARGETs for Attio cross-ref, 6 VAULT_HISTORY insurance targets), Contact Map (16 contacts ranked HOT/WARM/COOL/COLD), Lead Lifecycle Tracker (15 proposals with status), Convergence Report (top 5 signals). |
| `niche-intel-identifier` | complete | Proposed **0 new niches.** Single discretionary candidate (Commercial Plumbing federal/tribal credentialed, Helen Guo AZ $725K EBITDA) **skipped** on 4-gate failure: project-based not recurring; sub-$500M acquirable-independent TAM; 8(a)/HUBZone/SDVOSB credentials do not survive ownership change for non-qualifying acquirers; single sub-buy-box company does not validate the segment. |
| `niche-intel-scorer` | complete | Row 13 re-scored 2.53 → 2.65 (+0.12). Three rating bumps applied: EBITDA margins +/- → + (Aug Felker 25-35%); Porter's level-of-competition +/- → + (carve-out reduces sub-segment bidding); Value Creation business complexity +/- → + (carve-out isolates clean book). Conservative landing at low end of identifier's projected 2.65-2.70 band. New xlsx + new pptx uploaded; old files trashed. |
| `niche-intel-onepager` | complete | Row 4 refreshed with Jeff Stevens 4/22 unanswered diagnostic + Carlos Nieto 5/13 peer-searcher convergence + source citations. Score unchanged at 2.55. New pptx uploaded; old file trashed. |
| `niche-intel-tracker` | complete | WEEKLY REVIEW row 13 (sheet row 16) — `E16` score `2.53` → `2.65`; `H16` notes appended with re-score rationale. Range `E16:H16` written via `--values-json` (no positional delimiter risk). Verified by re-read. |

## Depth Actions Executed

### Row 13 — HNW Personal Lines Concierge Insurance Brokerage — 2.53 → 2.65

**What changed:** Three sub-criterion ratings stepped up on new evidence from the HISTORICAL agent's call mining.

| Category | Sub-criterion | Prior | New | Reason |
|---|---|---|---|---|
| Industry Economics | EBITDA margins | +/- (2) | + (3) | Aug Felker 11/19 quote — "really valuable" HNW personal-lines brokerages run 25-35% EBITDA at scale, clearing the 30%+ band for specialty insurance brokerage |
| Porter's Five Forces | Level of competition | +/- (2) | + (3) | Hunter Hartwell 1/12 carve-out workaround reduces sub-segment bidding intensity vs. whole-brokerage 12-14x multiple wall |
| Value Creation | Business complexity | +/- (2) | + (3) | Carve-out path isolates a clean book — lower integration complexity than whole-brokerage acquisition |

**Categories ceiling-locked (no change possible):** Growth, Penetration & Catalyst (3.0 already); Mission Criticality (3.0 already — the Aug Felker endorsement reinforces but cannot lift a maxed category).

**Recommended action for Wednesday:**
1. Advance row 13 to **Active - Outreach** — it now ties for the strongest non-Active score in WEEKLY REVIEW.
2. Re-engage Aug Felker with a single-question warm-rekindle email (4+ months stale): "Aug — any update on the two women near retirement you mentioned in November? Wondering if it's still alive or if we should move on." This is the named-target reveal G&B never collected.
3. Channel decision: the warm-network channel for Aug Felker as river guide, not DealsX cold email — the entire RTW is the warm relationship.

**Files:**
- Scorecard xlsx (new): file `136sFfqfxEpfZaLvuPHYPDNbqCTMXrqJ5` in folder `1ZryW7c3b7s6mB7SLF1MEMWdOpW-91lJL`
- One-pager pptx (new): file `1xRKrVV8t4RlJCjTwOUBHfPoeDcoIxdip` in same folder
- Old xlsx + pptx trashed.

### Row 4 — Specialty Coffee Equipment Service — refresh only (2.55 unchanged)

**What changed:** One-pager body refreshed; score unchanged.

Added under Macro Trends & Growth Drivers: *"Outstanding diagnostic (Jeff Stevens 4/22): unclear whether mid-sized regional chains (10-50 locations such as Joe Coffee, Blue Bottle scale) outsource equipment servicing or keep it in-house. Resolving this gates pipeline expansion beyond pure-play artisan cafes."*

Added under Key Success Factors: Carlos Nieto 5/13 peer-searcher convergence note (niche on radar of credentialed searchers but not over-fished).

Added source citations: `brain/calls/2026-04-22-jeff-stevens-call.md` and `brain/calls/2026-05-13-carlos-nieto-dca.md`.

**Note flagged for downstream:** the in-pptx "Assessment: 2.50 / 3.0" string in cell [1][0] was NOT touched because the brief said score stays. The WEEKLY REVIEW shows row 4 at 2.55. The scorer/tracker may want to reconcile that in-doc string in a separate pass.

**Recommended action for Wednesday:** sequence the Jeff Stevens diagnostic resolution before any pipeline expansion past pure-play artisan cafés. Direct ask to Jeff in the next G&B-Jeff cadence touchpoint.

**Files:**
- One-pager pptx (new): file `1leHHK9dBu0CIu8gkoZN1m_7v9HIDz4sr` in folder `13_ZNe6kY-1EUYWPYzWmiGK6i5Jdxfdts`
- Old pptx trashed.

## Why No NEW Niches This Week

The synthesizer evaluated 17 distinct niche/signal candidates. The identifier ran the 4-gate INITIAL SCREEN against each. **Zero cleared the KILLED/TABLED/ACTIVE filter with 2+ source confirmation.**

Documented diagnostic trail (preserves visibility for repeated zero-finding patterns):

| Source Channel | What it produced | Why it didn't yield a new niche |
|---|---|---|
| RECENT — newsletters (auto/subscriptions & education + auto/industry research) | 65 messages scanned, ~12 relevant | All signal mapped to specialty insurance brokerage M&A — already 5 rows in pipeline. No net-new vertical surfaced. |
| RECENT — Gmail deal flow (auto/deal flow + auto/investors) | 69 messages scanned, ~8 relevant | Broker teasers all in already-tracked or already-killed verticals; STREAM Capital industrials channel reinforces existing thesis. |
| RECENT — Granola/vault calls (14d) | 8 calls scanned (Granola MCP unavailable) | Carlos Nieto 5/13 + Krupa Shah 5/14 reinforced existing AI-as-disruption-risk doctrine; no new vertical. |
| RECENT — vault outputs | 6 outputs scanned | All within already-tracked niche universe. |
| RECENT — passive signals (brain/inbox since 5/13) | 4 inbox files | All pre-existing niche signals; nothing new. |
| RECENT — web/social (last30days unavailable, 2 WebSearch queries) | HVAC, commercial roofing, commercial plumbing surfaced | All flagged as searcher-overlap-saturated or thesis-fit-fail; specifically Commercial Plumbing federal/tribal credentialed evaluated and SKIPPED on 4-gate failure (above). |
| HISTORICAL — hist-calls (22 notes Aug 2025-Apr 2026) | Reinforcement of existing rows (rows 4, 7, 9, 13); MGA-build path DEAD; pure art advisory LIVE-but-constrained | All convergence mapped to existing rows. |
| HISTORICAL — hist-email (5 query buckets, ~120 threads, 1 deep-read) | Jeremy Black 2/3 sourced row 9's carriers (Trade Risk Group, Trade Acceptance, Texel); 6 VAULT_HISTORY insurance targets surfaced | Supports prioritization of existing row 9, not new niche. |
| HISTORICAL — hist-onenote | UNAVAILABLE — OneNote MCP not registered in env | Coverage gap. Would have scanned INDUSTRY MEMOS, INDUSTRY CONFERENCE LISTS, COMPANY MEMOS. |
| HISTORICAL — hist-chatgpt | Pre-processed in memory files 2026-03-16 | No re-mining of raw 18,600-message JSON; downstream memory files used instead. |

**Zero-finding reason (canonical, for sidecar):** *"7 pending candidates from prior week unprocessed; convergent signal is depth not breadth — five insurance-brokerage rows sit inside one PE-consolidation wave demanding advance-or-table decisions; no net-new niche cleared KILLED/TABLED filter with 2+ source confirmation."*

## Documented Rejections (synthesizer-surfaced, NOT advancing)

Candidates surfaced in HISTORICAL or RECENT gathering posts but rejected by the Identifier. Captured so they don't re-propose next Tuesday.

| Niche / Signal | Reason for rejection |
|---|---|
| Commercial Plumbing — federal/tribal credentialed | Project-based not recurring; sub-$500M acquirable-independent TAM; 8(a)/HUBZone/SDVOSB credentials do not transfer; sub-buy-box single data point. |
| HVAC Service & Repair (consolidation play) | Searcher-overlap saturated; PE roll-up window closed; killed parent variants already on KILLED list. |
| Commercial Roofing | Project-based revenue; weather/labor exposure; no G&B RTW. |
| B2B Trade-Magazine Publishing | AI-disruption risk + declining ad revenue; not mission-critical. |
| MGA Build Path | DEAD — Mark Gardella + Tobias Marshberry independently convergent on "build, don't buy" verdict 3/31. Documented in Lead Lifecycle Tracker. |
| Pure Art Advisory Standalone (key-person risk) | LIVE-but-constrained — Margot Romano 4/4 + Jeff Stevens 4/22 both flagged key-person risk. Already in WEEKLY REVIEW row 2 active; flag is for cadence, not new add. |
| Insurance Back-Office Shared Services (Camilla 2/4 + Jeremy 2/2) | Inhabits the SIU-sub-niche space that 5/12 report deferred to a future cycle. Camilla + Jeremy convergent but the BPO basic-claims sub-segment is already KILLED. |

## Companies Surfaced for Attio Cross-Reference (Synthesizer Registry)

Synthesizer flagged these as NEW_TARGET (need Attio cross-ref before any outreach):
- **Trade Risk Group** — trade credit insurance specialist
- **Trade Acceptance Group** — trade credit specialty broker
- **Texel Group** (formerly Meridian) — trade credit/cargo
- **Euler Hermes / Allianz Trade** — carrier (not target — reference only)
- **Atradius** — carrier (not target — reference only)
- **Coface** — carrier (not target — reference only)

Synthesizer flagged these as VAULT_HISTORY (mentioned in prior calls/outputs — verify cadence, do NOT cold-email):
- **PRMS** — Celia Santana CEO, HNW personal lines (from `project_deal_history.md`, ~5 months stale)
- **J.W. Allen** — HNW personal lines
- **Genser** — HNW personal lines
- **Grober Imbey** — HNW personal lines
- **Hamptons Risk** — HNW personal lines
- **DRO** — HNW personal lines

Action: confirm Attio status before next outreach cadence to any of these.

## Contacts Surfaced (Synthesizer Map)

| Contact | Warmth | Niche | Ask |
|---|---|---|---|
| August Felker | WARM (4mo stale) | HNW Personal Lines Concierge (row 13) | Named target from Nov reveal — single-question rekindle |
| Hunter Hartwell | WARM | Specialty Insurance (rows 7, 12, 13) | Carve-out path framing for HNW |
| Jeremy Black | WARM | Trade Credit / Customs / Cargo (row 9) | Cadence check; he sourced the bundle |
| Jeff Stevens | WARM | Specialty Coffee Equipment (row 4); Specialty Insurance Art (row 7) | Mid-sized chain in/outsource diagnostic |
| Carlos Nieto | COOL (recent meeting) | Specialty Coffee Equipment (row 4) | Peer-searcher coordination |
| Camilla Rojas | WARM | Insurance Back-Office (deferred) | SIU sub-niche framing for future cycle |
| Sarah Rowell | COOL (WSN mentor) | OSHA Workplace H&S Training (row 11) | Distribution channel intro |
| Krupa Shah | COOL (recent meeting) | AI-as-risk doctrine | Reinforce rather than add |
| Margot Romano | WARM | Art Advisory (row 2) | Key-person risk diagnostic |

## Recommended Wednesday Analyst Call Sequencing

1. **Row 13 (HNW Personal Lines Concierge)** — advance to Active - Outreach. G&B-Email warm-network channel. Aug Felker single-question rekindle. (Highest-conviction depth move this cycle.)
2. **Row 9 (Trade Credit / Customs / Cargo)** — set channel. Jeremy Black sourced the carriers; target-discovery has a head start.
3. **Row 4 (Specialty Coffee Equipment)** — sequence Jeff Stevens diagnostic before any pipeline expansion.
4. **Rows 11, 12, 14, 15** (remaining pending) — explicit advance / table / kill calls. Don't let them slip another cycle.

## Sidecar Contract

JSON sidecar at `brain/trackers/niches/niche-intel-2026-05-19.json` carries the machine-parseable summary for the wrapper validator:
- `niches_evaluated`: 17 (synthesizer signal matrix count — floor satisfied)
- `niches_identified`: 0 (zero_finding_reason populated — full diagnostic trail above)
- `one_pagers_written`: 2 (row 13 update + row 4 refresh)
- `scorecards_written`: 1 (row 13 re-score)
- `tracker_updated`: true (WEEKLY REVIEW row 13 score + notes write verified by re-read)
- `runtime_seconds`: ~3600 (wrapper start to sidecar write)
