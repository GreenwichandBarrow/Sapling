---
schema_version: 1.2.0
date: 2026-07-21
type: output
output_type: niche-intelligence-report
status: draft
skill_origin: niche-intelligence
kay_approved: null
kay_approval_date: null
people: ["[[entities/kay-schneider]]"]
companies: ["[[entities/greenwich-and-barrow]]"]
projects: []
tags:
  - date/2026-07-21
  - output
  - output/niche-intelligence-report
  - status/draft
  - person/kay-schneider
  - company/greenwich-and-barrow
  - topic/niche-intelligence
  - topic/search-fund
---

# Tuesday Niche Intelligence Report — 2026-07-21

Run metadata: Codex/systemd headless Tuesday run. Chatroom trace: [[traces/agents/2026-07-21-niche-intelligence]].

## Machine Summary

```json
{
  "run_date": "2026-07-21",
  "run_mode": "tuesday",
  "runner": "Codex/systemd",
  "niches_evaluated": 3,
  "niches_identified": 3,
  "one_pagers_written": 3,
  "scorecards_written": 3,
  "tracker_updated": true,
  "weekly_review_rows_added": [41, 42, 43],
  "top_score": {
    "name": "MoCRA-Compliant Beauty 3PL, Kitting, and Fulfillment for Independent Cosmetics Brands",
    "score": 2.13
  }
}
```

## Executive Summary

The run found three defensible new niche candidates after duplicate/lifecycle control: Yacht Property Management, MoCRA-Compliant Beauty 3PL/Kitting/Fulfillment, and Jeweler's Block Insurance Brokerage. Each received a one-pager, a standalone G&B industry scorecard XLSX, and a new WEEKLY REVIEW row.

The strongest score was MoCRA-Compliant Beauty 3PL at 2.13/3, narrowly ahead of Yacht Property Management at 2.12/3. Jeweler's Block Insurance Brokerage scored 1.93/3 because recurring insurance economics are strong, but the target pool is thin and QSBS/roll-up risk is substantial.

## Source Coverage

| Track | Sources Covered | Key Signals |
|---|---|---|
| RECENT | Web/social, newsletters, Granola calls, Gmail deal flow/investors, vault research, passive signals | Beauty infrastructure, yacht/marine services, specialty insurance, HVA logistics, and active-response signals. |
| HISTORICAL | Vault calls, historical Gmail, killed/tabled tracker context | Lifecycle controls suppressed dead art/fashion/women's-health lanes and prevented duplicates of active rows. |
| SYNTHESIS | RECENT + HISTORICAL chatroom posts, tracker snapshots, learnings | Three narrowed candidates survived duplicate control and independent validation. |

Infrastructure gaps: OneNote MCP was unavailable; the ChatGPT export was not present on the VPS; last30days was partial because Reddit returned 403 and X/YouTube were unavailable; historical Granola pagination was not exhausted; Gmail attachments/CIMs were not opened; Attio cross-reference was skipped because the skill's example conflicted with secret-handling rules.

## New Niches Identified

### Yacht Property Management for Private Yacht Owners in Coastal HNW Markets — 2.12/3

Thesis: Private yacht owners need an outsourced operating layer for planned maintenance, crew, compliance documents, marina/vendor management, budgeting, accounting, seasonal prep, and owner reporting. This is distinct from the existing boat/yacht transport row because the core service is ongoing asset stewardship, not transport coordination.

Scorecard summary: Initial screen passed on margins, recurring/reoccurring revenue, industry growth, and Growth TAM. Growth is supported by yacht-management and U.S. luxury-yacht market growth; the main concern is whether enough firms have platform-scale EBITDA rather than owner-operator captain-service economics.

Deliverables:
- One-pager: https://docs.google.com/presentation/d/1FKtFSjH4ZgaplJZKVcGFBn-9a8m9C4Gx/edit
- Scorecard XLSX: https://docs.google.com/spreadsheets/d/12OeFnnBLYHo3NokwGgYzGR_vLPv5QLl-/edit
- Drive folder: https://drive.google.com/drive/folders/1rlCxKK2lYH2XHz33q17ZzhO9Gf10ukSQ

Tracker row: WEEKLY REVIEW row 41, rank 38, status New.

### MoCRA-Compliant Beauty 3PL, Kitting, and Fulfillment for Independent Cosmetics Brands — 2.13/3

Thesis: Beauty brands increasingly need specialized fulfillment that handles lot/expiration tracking, climate control, hazmat/fragrance handling, kitting, returns, and FDA/MoCRA documentation workflows. This is not a duplicate of beauty testing, package validation, packaging manufacturing, or fragrance distribution; the target is the embedded logistics/fulfillment provider.

Scorecard summary: Initial screen passed. MoCRA creates a real compliance catalyst, and beauty logistics has attractive recurring/reoccurring order-flow behavior, but generic 3PL margin compression and overlap with existing beauty-infrastructure rows are the key diligence risks.

Deliverables:
- One-pager: https://docs.google.com/presentation/d/1msCpE52gq3Tk2kWVG-6oVdhCQSh-pPnO/edit
- Scorecard XLSX: https://docs.google.com/spreadsheets/d/1WFZ1xMHTw9aW7OY2uxszdL-4SgcFpAB4/edit
- Drive folder: https://drive.google.com/drive/folders/1Rcp1HYFJnBo60JZDOwyxI61FJGMdxmO2

Tracker row: WEEKLY REVIEW row 42, rank 39, status New.

### Jeweler's Block Insurance Brokerage for Independent Jewelry Retailers, Wholesalers, and Pawn/Jewelry Trade Businesses — 1.93/3

Thesis: Jeweler's block is a narrow commercial insurance wedge covering jewelry inventory, entrusted customer property, goods in transit, trade shows, theft, and related jewelry-trade risk. It is a better specialty-insurance child wedge than generic brokerage, but it should stay caveated unless proprietary access appears.

Scorecard summary: Initial screen passed with caveats on market-growth evidence and Growth TAM. The economics and mission criticality are strong, but target pool depth, QSBS treatment, carrier/program power, and insurance roll-up saturation pushed the score below the other two candidates.

Deliverables:
- One-pager: https://docs.google.com/presentation/d/18UhRulGaWoq1vs-3f-lEporgQvTdtMt-/edit
- Scorecard XLSX: https://docs.google.com/spreadsheets/d/19WK6m-g9BmN2PiRFdp-XYb2qFUJcx7rG/edit
- Drive folder: https://drive.google.com/drive/folders/1v89CuViXP9UYHAN646RFF-wd6TX4Miac

Tracker row: WEEKLY REVIEW row 43, rank 40, status New.

## Tracker Update

The tracker agent re-fetched live WEEKLY REVIEW before writing, saved `/tmp/niche-weekly-review-pre-tracker-2026-07-21.json` for rollback context, appended three rows, then re-read WEEKLY REVIEW and verified each new niche appears exactly once. `Current Outreach Channel` was left blank. The sheet did not have `Red flags noted`, so red flags were folded into `Quick notes`.

## Open Loops

- Run CRM/Attio duplicate checks before any target-discovery or outreach list write.
- Pull OneNote and ChatGPT exports into the scheduled environment if those sources remain required.
- Open recent CIM attachments in a follow-up pass if Kay wants deal-flow-derived niche signals to be more complete.
- Verify platform-scale target depth for Yacht Property Management and Jeweler's Block before any sprint activation.
