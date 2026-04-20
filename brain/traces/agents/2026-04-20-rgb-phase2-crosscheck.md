---
schema_version: 1.0.0
date: 2026-04-20
task: River-guide-builder Phase 2 cross-check across 8 active niches (warm-intro-finder 5-source scan)
agents: [rgb2-insurance, rgb2-pest, rgb2-estate-mgmt, rgb2-coffee, rgb2-art-storage, rgb2-commercial-cleaning, rgb2-vertical-saas, rgb2-private-art-advisory]
status: active
linked_trace: brain/traces/agents/2026-04-20-river-guide-sprint.md
---

# Agent Chatroom: RGB Phase 2 cross-check (8 niches)

**Task:** For each niche's River Guides tab, run warm-intro-finder's 5-source scan on every row and populate `Known Contact` / `Source` / `Evidence` columns.

**5 sources:**
1. LinkedIn CSV at `archives/linkedin/connections.csv` (~901 rows)
2. Attio People (search by name + company via `mcp__attio__*`)
3. Vault entities at `brain/entities/*.md`
4. Gmail history (`gog gmail search`)
5. Investor network

**Output columns (populate on River Guides tab of each niche's sheet):**
- `Known Contact`: WARM / INVESTOR INTRO / SHARED BACKGROUND / COLD
- `Source`: which of the 5 sources hit (LinkedIn / Attio / Vault / Gmail / Investor)
- `Evidence`: short snippet (e.g., "LinkedIn 1st degree, connected 2019" / "vault: 2025-09-17 call" / "investor Margot intro")

**No Apollo dependency.** Phase 2 is fully independent of the Apollo enrichment that's running elsewhere.

**Sheet ID registry:**
| Niche | Agent | Sheet ID |
|---|---|---|
| Specialty Insurance | rgb2-insurance | `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ` |
| Premium Pest | rgb2-pest | `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I` |
| Estate Management | rgb2-estate-mgmt | `1Kv4Vpl9FWdcZ3rKLLHW6G75Ytf2lql4-myrOWEZw1eY` |
| Specialty Coffee Equipment Service | rgb2-coffee | `1UNGi0_Bcdhk3nqT_aF4tHRAC3b6BhtellxQOMjlrHt0` |
| Art Storage | rgb2-art-storage | `1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g` |
| High-End Commercial Cleaning | rgb2-commercial-cleaning | `12CDAcAD9Pi96LBK7Mdwm3lVWKT3hBVKGZKJ0bRhXDw4` |
| Vertical SaaS Luxury HV-Asset Services | rgb2-vertical-saas | **TBD** — must locate sheet via Drive search / tracker |
| Private Art Advisory | rgb2-private-art-advisory | **TBD** — must locate sheet via Drive search / tracker |

## Coordination Log

## [15:35] orchestrator
Spawning 8 agents in background. 6 have direct sheet IDs; 2 (vertical-saas, private-art-advisory) must locate their sheet first from Drive or the Industry Research Tracker WEEKLY REVIEW tab.

Entering polling loop. Timeout: 30 minutes.

## [15:36] rgb2-estate-mgmt
Starting. Sheet ID `1Kv4Vpl9FWdcZ3rKLLHW6G75Ytf2lql4-myrOWEZw1eY`, opening River Guides tab.
→ WORKING

## [15:37] rgb2-coffee
Starting Phase 2 cross-check on Specialty Coffee Equipment Service sheet. Reading River Guides tab structure.
## [15:37] rgb2-art-storage
Starting Phase 2 cross-check on Art Storage sheet. Reading River Guides tab and Do Not Call tab.
→ WORKING

## [15:37] rgb2-insurance
Starting. Sheet `15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ`. 35 named rows. Running 5-source cross-check now.
→ WORKING

## [15:38] rgb2-pest
Starting. Sheet `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`. 26 rows on River Guides tab. Running 5-source scan.
→ WORKING

## [15:37] rgb2-vertical-saas
Starting. No direct sheet ID — searching Drive + Tracker for Vertical SaaS Luxury HV-Asset Services target sheet.
→ WORKING

## [15:38] rgb2-commercial-cleaning
Starting Phase 2 cross-check on High-End Commercial Cleaning sheet. 37 rows across 13 categories (ISSA/BSCAI, Healthcare EVS, Data Center, Biotech/Pharma, Luxury Hospitality, Museums, Trade Press, Conferences, Consultants, M&A, Adjacent Operators).
→ WORKING

## [15:38] rgb2-vertical-saas
Located sheet via Drive search: `1x8DAZGOQX1GJfLV617HX1MV-Il-sIzopMBzOl3N7w1s` — "Vertical SaaS for Luxury & HV-Asset Services - Target List". Modified 2026-04-20 17:52 UTC. Opening River Guides tab.
→ WORKING
