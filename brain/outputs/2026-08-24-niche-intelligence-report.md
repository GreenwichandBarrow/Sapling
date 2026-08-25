---
schema_version: 1.2.0
date: 2026-08-24
type: output
output_type: niche-intelligence-report
status: draft
skill_origin: niche-intelligence
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: ["[[entities/greenwich-and-barrow]]"]
projects: []
trace: "[[traces/agents/2026-08-24-niche-intelligence]]"
tags:
  - date/2026-08-24
  - output
  - output/niche-intelligence-report
  - status/draft
  - person/kay-schneider
  - company/greenwich-and-barrow
  - topic/niche-intelligence
  - topic/search-fund
---

# Monday Niche Intelligence Report - 2026-08-24

```json
{
  "run_date": "2026-08-24",
  "run_mode": "monday",
  "runtime": "Codex/systemd",
  "niches_evaluated": 3,
  "niches_identified": 2,
  "one_pagers_written": 2,
  "scorecards_written": 2,
  "tracker_updated": true,
  "edge_niches_considered": 3,
  "top_niche": "Commercial/Industrial Air Purification Installed-Base Service and Compliance Maintenance",
  "source_coverage": {
    "recent_track": "complete with last30days unavailable; web search substituted",
    "historical_track": "partial; OneNote, ChatGPT export, and older direct Granola unavailable/incomplete"
  }
}
```

## Executive Summary

The headless Monday run completed under Codex/systemd. Two new niches were identified, one-pagers and industry scorecards were uploaded, and both rows were appended to the Industry Research Tracker `WEEKLY REVIEW` tab.

The strongest new candidate is **Commercial/Industrial Air Purification Installed-Base Service and Compliance Maintenance** at **2.44 / 3.00**. The score is supported by a real broker signal, sufficient target-density proxies, mid-single-digit industrial filtration growth, repeat installed-base service potential, and a large enough TAM. The primary diligence issue is whether target revenue is genuinely service/contract/consumables driven rather than equipment resale or install-heavy HVAC work.

**Art-Dealer Cultural-Goods Compliance and Back-Office Operations** scored **1.96 / 3.00**. It has strong G&B right-to-win and a real regulatory tailwind, but should stay in HOLD until target density, recurring-retainer economics, and standalone acquisition candidates are proven.

## Data Sources This Week

| Track | Coverage | Diagnostics |
|---|---|---|
| RECENT | Gmail newsletters, Gmail deal flow/investor threads, recent Granola notes, recent vault calls/outputs, passive inbox scan, supplemental web research | `last30days` CLI was unavailable in the headless environment; web search substituted, so full social coverage is incomplete. Gmail was read-only with `--gmail-no-send`. |
| HISTORICAL | Local `brain/calls/*.md`, historical Gmail read-only searches, prior niche-intelligence outputs/traces | Partial. OneNote SEARCH FUND notebook, requested ChatGPT export, and older direct Granola coverage were unavailable/incomplete and are logged as evidence gaps. |
| SYNTHESIS | Cross-source matrix, named company registry, contact map, lead lifecycle tracker, picks-and-shovels expansion, convergence report | Attio was not checked because no safe CLI/MCP path was exposed; no secret files were inspected. |

## New Niches Identified

### Commercial/Industrial Air Purification Installed-Base Service and Compliance Maintenance - Score: 2.44 / 3.00

**Thesis:** Technical air-purification and filtration systems create a repeat installed-base service wedge: preventive maintenance, filter/parts replacement, emergency repair, validation/testing support, retrofits, and safety/compliance documentation. The market is fragmented enough to support a long sprint, but the acquisition target must be scoped away from product-only distribution, generic HVAC, and install-heavy work.

**Detailed Scorecard:**

| Category | Score | Weight | Notes |
|---|---:|---:|---|
| Growth & Catalyst | 2.75 | 25% | Industrial air filtration market sources cite roughly 4.9%-6.1% CAGR, with workplace safety, emissions control, aging equipment, and facility-health standards as demand drivers. |
| Size & Fragmentation | 3.00 | 10% | Target proxies include 43,753 broad NAICS 81131 entities, 6,000+ U.S. air-filter suppliers, and an estimated 100-300 independent service-oriented targets after exclusions. |
| Industry Economics | 2.33 | 10% | One broker target showed about 31% normalized EBITDA; service-heavy models can clear 15%, but equipment resale and installation mix can dilute margins. |
| Mission Criticality | 2.33 | 15% | Failure creates downtime, safety, OSHA/EHS, air-quality, and process-risk exposure for labs, municipalities, manufacturers, training sites, and process facilities. |
| Exogenous Risks | 2.00 | 10% | Risks include technical labor, vendor dependence, standards exposure, and medium-rising PE activity in filtration manufacturing/distribution. |
| Porter's Forces | 2.00 | 15% | Fragmented service field, but manufacturers, distributors, HVAC firms, and sponsor-backed filtration platforms can compress the opportunity. |
| Value Creation | 2.50 | 10% | Professionalize PM contracts, dispatch, compliance documentation, route density, parts/consumables attach, and vendor partnerships. |
| Impact | 2.50 | 5% | Positive workplace safety, air quality, and contaminant-control externalities. |

**Initial Screen:** Pass on margins, recurring/reoccurring revenue, industry growth, and Growth TAM, with caveats around service mix.

**WEEKLY REVIEW Columns:** QSBS: likely eligible if acquired as a domestic C-corp service business; confirm tax counsel and watch equipment/manufacturing mix. Target Pool: 100-300 likely independently owned U.S. targets after exclusions. Quick notes: Score 2.44/3.00. TEST. Strong installed-base service thesis with market growth and target density; main diligence is contracted/repeat service mix versus install/equipment resale, plus PE heat.

**Deliverables:** One-pager: https://docs.google.com/presentation/d/1QeTkNjrJHqsIFhNAvz7SIPVnRlZXYaUn/edit. Scorecard: https://docs.google.com/spreadsheets/d/1XYW7BYW08hriupby_K7rwQ5N9eJUqq1y/edit. Folder: https://drive.google.com/drive/folders/1cs20XcJiEy4NJexAdlyYwR0JoFbvw20E.

**Evidence Gaps:** Confirm recurring/contracted service percentage, service aftermarket versus equipment resale/install economics, technician certifications, PE-backed share in the service-only segment, customer retention, and customer concentration.

### Art-Dealer Cultural-Goods Compliance and Back-Office Operations - Score: 1.96 / 3.00

**Thesis:** Cultural-goods import rules, AML/KYC scrutiny, provenance/title risk, consignment accounting, and cross-border art movement create back-office complexity for art dealers and galleries. G&B has unusually strong credibility in the customer environment, but the narrow acquisition market may be too small or too embedded inside law, CPA, advisory, or software firms.

**Detailed Scorecard:**

| Category | Score | Weight | Notes |
|---|---:|---:|---|
| Growth & Catalyst | 2.00 | 25% | Compliance burden is rising, but the art-dealer end market itself appears flat/contracting and no clean outsourced-service CAGR was found. |
| Size & Fragmentation | 2.00 | 10% | Customer universe is large, but standalone service-provider target pool is estimated at only 10-40 U.S.-reachable candidates after exclusions. |
| Industry Economics | 2.00 | 10% | Productized compliance/accounting/provenance services can work; bespoke senior-expert services may compress margin and scalability. |
| Mission Criticality | 2.33 | 15% | Documentation failures create import/export, provenance, sanctions, tax/accounting, insurance, lending, and reputational risk. |
| Exogenous Risks | 1.60 | 10% | AI document workflows, legal/CPA bundling, art-market cyclicality, and regulatory uncertainty create material risk. |
| Porter's Forces | 1.67 | 15% | Specialist providers compete with law firms, CPA firms, advisory boutiques, software tools, logistics advisors, insurers, and in-house staff. |
| Value Creation | 2.00 | 10% | Opportunity exists to productize retainers, templates, records, workflows, and dealer operations, but target availability is uncertain. |
| Impact | 2.00 | 5% | Supports lawful cultural-goods trade, provenance clarity, and better stewardship. |

**Initial Screen:** Pass/caveated on margins, recurring revenue, and Growth TAM; fail/caveated on industry growth because the demand tailwind is compliance burden rather than broad art-market expansion.

**WEEKLY REVIEW Columns:** QSBS: likely eligible only if a clean standalone domestic service company is acquired; law/CPA practices, partnership structures, and embedded departments may not fit. Target Pool: 10-40 U.S.-reachable candidates, 40-120 global, with heavy exclusions. Quick notes: Score 1.96/3.00. HOLD. Strong art/luxury right-to-win and regulatory tailwind, but prove 20+ standalone targets and recurring-retainer economics before outreach.

**Deliverables:** One-pager: https://docs.google.com/presentation/d/1yjbQG2zS5uq1pmjY33tUzHCFxIz0cNh4/edit. Scorecard: https://docs.google.com/spreadsheets/d/1mXrWs_GamCdbxRYq3Fx6_ICAvha9aiWt/edit. Folder: https://drive.google.com/drive/folders/1pnJthlCdJREb5tyrWRRhqnuO6KJOKkjf.

**Evidence Gaps:** Prove 20+ standalone acquisition candidates, distinguish productized service companies from law/CPA/advisory departments, quantify recurring-retainer share, find customer willingness-to-pay evidence, and validate whether U.S.-reachable TAM clears the investor floor.

## Duplicate-Screened Candidate Not Advanced

**Beauty claims substantiation and regulatory documentation for active-led cosmetic/wellness products** was not advanced as a new one-pager because it overlaps active tracker rows: Fragrance & Cosmetic Product Testing Labs, MoCRA-Compliant Beauty 3PL, Luxury Package Testing & Validation Labs, High-End Beauty & Fragrance Packaging, Value-Added Fragrance Distribution, and the older Compliance & Packaging SaaS lane. The signal is real, but it belongs as a refinement to existing beauty-infrastructure rows rather than a duplicate new niche.

## Tracker Update

Both scored niches were appended to `WEEKLY REVIEW` with status `New`:

| Rank | Niche | Score | Tracker Status |
|---:|---|---:|---|
| 41 | Commercial/Industrial Air Purification Installed-Base Service and Compliance Maintenance | 2.44 | New |
| 42 | Art-Dealer Cultural-Goods Compliance and Back-Office Operations | 1.96 | New |

Verification re-read found both rows exactly once in `WEEKLY REVIEW!A40:K46`.

## Open Loops / Infra

- `last30days` CLI was unavailable in the headless environment; web search substituted, so full social coverage is incomplete.
- OneNote SEARCH FUND notebook was unavailable because no OneNote MCP tool was exposed in this session.
- Requested ChatGPT export was not found/read in the headless environment.
- Older direct Granola coverage was incomplete; local `brain/calls/` served as the historical-call corpus.
- Attio was not checked because no safe CLI/MCP path was available; no secret files were inspected.

## Run Links

- Chatroom trace: [[traces/agents/2026-08-24-niche-intelligence]]
- Air purification folder: https://drive.google.com/drive/folders/1cs20XcJiEy4NJexAdlyYwR0JoFbvw20E
- Art-dealer compliance folder: https://drive.google.com/drive/folders/1pnJthlCdJREb5tyrWRRhqnuO6KJOKkjf
