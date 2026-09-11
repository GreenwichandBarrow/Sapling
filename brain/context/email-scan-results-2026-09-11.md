---
schema_version: 1.1.0
date: 2026-09-11
type: email-scan-results
skill_origin: email-intelligence
tags: [date/2026-09-11, output/email-scan-results, status/draft, source/gmail]
---

# Email Scan Results - 2026-09-11

## 1. Actionable Items Created

- Created `[[inbox/2026-09-11-august-management-report-budget-trigger]]` from Anthony James Balleras Bacagan / StartVirtual, Gmail message `1a08c3acb3f9a424`, for reporting period 2026-08. PDFs filed to Drive folder `AUGUST 2026` under BOOKKEEPING / MONTHLY REPORTING.
- `budget-manager monthly` invoked in-session for 2026-08 and completed successfully. Output: `[[outputs/2026-09-11-budget-report-aug-2026]]`. Four variance flags; dashboard stop hooks passed; Slack HTTP 200.
- No CIM, Active Deal fast-path, intro, or auto-acknowledgment trigger detected in the compact source artifact.

## 2. Deal Flow Classified

- 60 inbound messages scanned; 7 outbound messages scanned; 1 Gmail draft checked.
- DIRECT: 22 — personalized correspondence, individual deal alerts, internal/calendar responses, service messages, or lead notifications.
- BLAST: 9 — generic broker/platform listing or opportunity mail.
- NEWSLETTER: 29 — newsletters, marketplace digests, editorial mail, receipts, and automated updates.
- Deal-newsletter/listing extraction was run for broker/platform messages below; newsletter classification does not suppress listing extraction.

## 3. Draft Status

- 1 unsent Gmail draft found: created 2026-08-20, approximately 22 days old; recipient and subject metadata were blank in the bounded draft artifact. No matching SENT or DELETED record was found in the 2026-09-10 session log.
- No drafts were sent or auto-created during this run.

## 4. Introductions Detected

None.

## 5. Niche Signals

- Passive deal-flow observations: HVAC/plumbing contractor, pest-control brand, metrology solutions, subscription video editing, career services, CPR/first-aid content site, travel ecommerce, umbrella ecommerce, fintech SaaS, restaurant portfolio, laundromat, pilates studios, and pool service.
- These are observations from inbound deal/newsletter content, not validated thesis or fit conclusions.

## 6. In-Person Meetings Today

None. Calendar contains external virtual meeting `Mike I Kay` at 11:30 ET; no in-person external meeting was identified.

Granola notes updated 2026-09-10 (`not_pbW9xciAW0SYxt`, `not_ZbsSsTm9M5xpuE`) were already represented by existing call notes, so no duplicate files were written.

## 7. Broker BLAST Listings (per-deal extraction)

| source | headline | geo | revenue | ebitda | margin | industry | flag_reason | gmail_msg_id | listing_ordinal |
|---|---|---|---|---|---|---|---|---|---:|
| Helen Guo, SMB Deal Hunter | Pool service company with manager | undisclosed | undisclosed | undisclosed | undisclosed | pool service | deal-newsletter-known-sender | 1a08cf764ec7aa15 | 1 |
| Helen Guo, SMB Deal Hunter | Pawn shop with growing demand | undisclosed | undisclosed | undisclosed | undisclosed | pawn / retail | deal-newsletter-known-sender | 1a08cf764ec7aa15 | 2 |
| Helen Guo, SMB Deal Hunter | New off-market business listing | undisclosed | undisclosed | undisclosed | undisclosed | undisclosed | deal-newsletter-known-sender | 1a08812b3ff479ab | 1 |
| Helen Guo, SMB Deal Hunter | Laundromat portfolio with real estate | undisclosed | undisclosed | undisclosed | undisclosed | laundromat | deal-newsletter-known-sender | 1a08306d1bdaabfc | 1 |
| Transworld Business Advisors | Recent business listing | MA | undisclosed | undisclosed | undisclosed | restaurant portfolio | single-listing-blast | 1a06c0e7e40d2157 | 1 |
| BizBuySell Marketplace | SBA-eligible listing | undisclosed | undisclosed | undisclosed | undisclosed | franchise / SMB | deal-newsletter-known-sender | 1a08b7550208265b | 1 |
| BizBuySell Marketplace | Hot franchise listing | undisclosed | undisclosed | undisclosed | undisclosed | franchise | deal-newsletter-known-sender | 1a082047766a5661 | 1 |
| Quiet Light, Ryan Condie | 2-Year-Old FinTech SaaS | undisclosed | undisclosed | $33K SDE | undisclosed | fintech SaaS | single-listing-blast | 1a06cc1f6924bc30 | 1 |
| Quiet Light, Jon Hainstock | Subscription video-editing service | undisclosed | undisclosed | undisclosed | 4.8/5 rating | video editing / subscription service | single-listing-blast | 1a0815c263569620 | 1 |
| Quiet Light, Chris Wozniak | UV-protection umbrella brand | undisclosed | undisclosed | undisclosed | undisclosed | ecommerce / consumer brand | single-listing-blast | 1a08236a262aae39 | 1 |
| Quiet Light, Chris Wozniak | DTC pest-control brand | 45+ states | $10.7M TTM | undisclosed | undisclosed | pest control ecommerce | single-listing-blast | 1a08682be0f5b1b5 | 1 |
| Quiet Light, Brad Wayland | Career services business | undisclosed | undisclosed | undisclosed | 33%+ net | career services | single-listing-blast | 1a0875cf723c21ba | 1 |
| Quiet Light, Brad Wayland | Free CPR and first-aid training site | undisclosed | undisclosed | undisclosed | undisclosed | content / training | single-listing-blast | 1a08ba75e1e29372 | 1 |
| Quiet Light, Ethan Alexander | Shark Tank Shopify travel brand | undisclosed | undisclosed | undisclosed | ~50% repeat customer rate | ecommerce / travel | single-listing-blast | 1a08c8380fa1306a | 1 |
| Calder Capital, Max Friar | Integrated metrology solutions provider | undisclosed | $2.29M | undisclosed | undisclosed | metrology / engineering | single-listing-blast | 1a08729e03bcfb82 | 1 |
| Calder Capital, Max Friar | HVAC and plumbing contractor | undisclosed | undisclosed | undisclosed | undisclosed | HVAC / plumbing | single-listing-blast | 1a08c530f98fd199 | 1 |

## 8. Auto-Drafts Created

None.

## Actionable Items / System Status

- Bookkeeper chain completed: `BOOKKEEPER-PL-CHAIN: invoked budget-manager monthly for period 2026-08`.
- Budget report output landed at `[[outputs/2026-09-11-budget-report-aug-2026]]`; downstream briefing should surface its variance flags and runway metrics, not the trigger event.
- No Granola API failure. Existing call-note files made ingestion idempotent.
