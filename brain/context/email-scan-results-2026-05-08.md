---
date: 2026-05-08
type: context
title: "Email Scan Results — 2026-05-08"
tags:
  - date/2026-05-08
  - context
  - topic/email-scan
  - topic/morning-briefing
  - topic/deal-flow
schema_version: 1.1.0
---

## Summary

- Inbox scanned (newer_than:2d, 50-thread cap): 19 threads visible.
- Outbound scanned (kay.s@greenwichandbarrow.com newer_than:2d): 10 threads (mostly 5/7 reply traffic — no fresh outbound today).
- CIM auto-trigger fires: 0
- NDA auto-trigger fires (PDF attached): 0 (E&K BLASTs link to external NDA URLs, do not attach PDF)
- Active Deal Fast-Path fires: 0
- Bookkeeper P&L auto-fires: 0
- Broker BLAST per-listing rows: 5 (Quiet Light ×3, Everingham & Kerr ×2)
- Auto-acknowledgment Gmail drafts created: 0
- Granola new transcripts: 0 (`cache-v6.json` last flushed 5/7 08:36 — unchanged since yesterday's scan; `.enc` flushed 5/8 07:16 but encrypted per known open loop)

## 1. Actionable Items Created

| timestamp | source | item | inbox_file | urgency |
|---|---|---|---|---|
| 2026-05-08 06:35 | James Emden (Helmsley Spear) | Calendar acceptance — June 1 lunch confirmed (12:30-1:30 ET). Auto-confirm; no action. | none | low |
| 2026-05-07 19:03 | NPMA Events | Pest-management association event newsletter — niche signal only, no action. | none | low |

**No new actionable items today.** All 5/6 items (Eric Mendelsohn email change, Jackson Niketas AI coaching, Megan Benson dinner, Payal Keshvani dinner, Andrew Lowis Axial intro update) were captured in yesterday's scan and are tracked in `session-decisions-2026-05-07.md`.

**Carry-forward (per session-decisions-2026-05-07 OPEN):**
- Allison Allen PWIPM Council reply — 3rd day carried; women-network-priority + pest mgmt Active-Outreach lens. No fresh inbound from Allison.
- Taft (Payal) vs KeyBank (Megan) Thu 5/14 dinner — Megan invite from 5/6 10:37 still open. No fresh inbound from either today.

No `brain/inbox/` files written this run.

## 2. Deal Flow Classified

| classification | count | notes |
|---|---|---|
| DIRECT (personalized to Kay) | 9 | James Emden (calendar accept + RE: Meeting), Barrie Green ×2 (internal team-auto), Harrison Wells ×2 (server work), Eric Mendelsohn (5/6, scanned yesterday), Jackson Niketas (5/6), Megan Benson (5/6), GJ King (5/6) |
| BLAST (broker / deal-flow) | 6 | Quiet Light ×3 (Fashion Blog 5/7 14:00, Pet Ramp 5/7 10:00, Prepper Food 5/6 14:00); Everingham & Kerr ×3 (Structural Engineering 5/7 18:23, SaaS Healthcare 5/7 12:30, Family Medical 5/6 17:32 — already in yesterday's section 7) |
| NEWSLETTER | 11 | Mike Allen / Axios ×2, Helen Guo SMB Deal Hunter ×2 (newsletter aggregator per `feedback_marketplace_vs_broker_distinction` — does not represent listings), NPMA Events, Sara Teare 1Password promo, Wispr Flow promo, Mitchell Baldridge, Beacon AI Friday reminder, NAEPC May 12 conference reminder |
| OPS / SYSTEM | 7 | 1Password invoice, Dodo Digital Stripe receipt, DMARC reports ×2, Anthropic console login, Ria Bautista StartVirtual quality audit (5/6), Kay-self Yahoo hotel forward (5/6) |

## 3. Draft Status

Gmail draft list returned 9 drafts (unchanged from yesterday's scan).

| draft_id | thread_subject | state | age | action |
|---|---|---|---|---|
| `r-7216983259268091776` | "Tomorrow's call — could we push to 10:30 ET?" (Andrew Lowis Axial reschedule) | **Already SENT 2026-05-06** per session-decisions-2026-05-06; ghost draft persists | 3d | Suppress — do NOT flag stale (per `<gmail_scanning>` cross-check rule) |
| `r989550462937595579` | (legacy thread `19caf...`) | Stale | >60d | Already known-stale (carried forward) |
| `r-5013177138505427051` thru `r8922907573534439329` (7 entries) | All on `19c81...` thread family | Stale | >60d | Known-stale legacy from pre-2026 testing |

**No new unsent drafts > 48 hours.** No fresh draft creation needed.

## 4. Introductions Detected

None this scan window.

## 5. Niche Signals

| signal | source | direction |
|---|---|---|
| NPMA pest-management association event newsletter | NPMA Events | POSITIVE — Pest is Active-Outreach niche; reinforces association-channel presence |
| Helen Guo aggregator includes "30-year interior plant management company" | Helen Guo SMB Deal Hunter (5/7 13:09) | NEUTRAL — interior plant mgmt is B2B services-adjacent; aggregator only, not represented |
| Full-service Structural Engineering Firm — NJ | Everingham & Kerr (5/7 18:23) | NEUTRAL — engineering-services category in tristate, but $200K rev / $100K cash flow is well below G&B $2M EBITDA floor |
| Cloud-Based SaaS Healthcare / Regulatory Compliance Software | Everingham & Kerr (5/7 12:30) | NEGATIVE — SaaS not B2B services, $700K revenue, virtual/remote; out of buy-box across multiple gates |
| Online consumer product / content sites (fashion blog, pet ramp, prepper food) | Quiet Light ×3 | NEGATIVE — e-commerce / online businesses, out of B2B services buy-box |

## 6. In-Person Meetings Today

**None.** Today's calendar:
- 10:30-11:30 ET — Steam, Sauna & Salt Bath (S10 Recovery, 109 Leroy St NYC) — personal/wellness
- 13:00-14:00 ET — AI Friday: Measuring the Real ROI of AI in Software Engineering — virtual webinar (StreamYard, Anacapa Beacon recurring series)

No external in-person business meetings → no Granola in-person reminder needed.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---|
| David @ Quiet Light (david@quietlight.com) | Leading Fashion Blog \| 2.4M Visitors Per Year \| Huge Pinterest Traffic \| <10 Hours Per Week | undisclosed (online business) | undisclosed | undisclosed | undisclosed | E-commerce / content site (online media) | single-listing-blast | 19e039967236fca4 | 1 |
| Joel Reichert @ Quiet Light (joel.reichert@quietlight.com) | 15-Year-Old US-Made Pet Ramp Brand \| Virtually No Marketing \| Low Owner Workload | USA (manufacturing) | undisclosed | undisclosed | undisclosed | E-commerce / consumer product | single-listing-blast | 19e02bd589b6b755 | 1 |
| Brad @ Quiet Light (brad@quietlight.com) | 12-Year-Old Prepper Food Business \| $629 AOV \| USA Supply Chain \| Low Multiple | USA | undisclosed (subject only references AOV) | undisclosed | undisclosed | E-commerce / consumer goods | single-listing-blast | 19dfe72cdb08fc0c | 1 |
| Everingham & Kerr (admin1@everkerr.com) | Full-service Structural Engineering, Inspection & Consulting Firm | New Jersey | $200K | $100K (normalized cash flow) | ~50% | Engineering services / B2B services | single-listing-blast | 19e0489d0691b5ff | 1 |
| Everingham & Kerr (admin1@everkerr.com) | Cloud-Based SaaS Healthcare / Regulatory Compliance Software Company | Virtual / Remote | $700K (mostly recurring) | undisclosed | undisclosed | Healthcare regtech SaaS | single-listing-blast | 19e034732ed5648c | 1 |

**Out-of-buy-box note:** All 5 listings fall outside G&B buy-box.
- E&K Structural Engineering: $100K cash flow is 20× below the $2M EBITDA practical floor (per `feedback_deal_screen_300k_salary_15pct_margin`); cannot support Kay's $300K salary even before debt service.
- E&K SaaS Healthcare: SaaS product business, not B2B services; virtual/remote (not tristate); $700K revenue below $5M revenue floor.
- Quiet Light ×3: All e-commerce / content / online product businesses — wrong category (B2B services niche only) and below revenue/EBITDA floors.

None advancing to target-discovery. Logged for broker-channel volume tracking.

**Note on E&K Family Medical Practice 5/6 17:32 (`19dff3511a04ba4c`):** Already extracted in yesterday's section 7 — not re-listed here to avoid cross-artifact confusion (intra-run dedup key still respected).

## 8. Auto-Drafts Created

None.

**Reasoning:** All 5 broker BLASTs in section 7 either (a) link to NDA via external URL rather than attaching a PDF (E&K pattern — `<auto_ack_drafts>` requires PDF attachment whose filename contains NDA/CA/non-disclosure/confidentiality), or (b) are pure marketing teasers with no NDA/CIM attachment (Quiet Light pattern). No CIM PDFs ≥5 pages with structured financials landed inbound. No NDA wrapper trigger fired by design.

Listings are all out-of-buy-box, so even on manual review no acknowledgment is owed.
