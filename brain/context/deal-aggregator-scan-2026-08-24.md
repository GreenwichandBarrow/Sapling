---
date: 2026-08-24
deals_found: 0
sources_scanned: 19
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 1
email_scan_status: live
---
# Deal Aggregator Scan — 2026-08-24

## Deals Surfaced (sent to Slack individually)
None today

## Email Inbound Deals
None today

## DealsX Proprietary Outreach Replies
None today

## Broker Opportunistic Review
1. **High-Growth AI Services Firm** — Axial | undisclosed | $2M EBITDA | AI services / GovCon | Key signals: not disclosed | Why it matters: financially plausible broker-platform lead with no hard-exclude, but no active thesis corpus match. | https://www.axial.net

## Near Misses (not Slacked)
- **Medical Animation and Visualization and Digital Media Company** — Everingham & Kerr | too sparse to evaluate; no financials disclosed and no active thesis match.
- **Commercial and Industrial Air Purification Systems Company** — Everingham & Kerr | ambiguous product/service split, no financials disclosed, preserve for review.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens (e.g. broker-buy-box reruns, dual-filter retroactive replays) a 5-minute query instead of a 90-minute artifact-mining exercise. Aggregate counts in Source Scorecard tell you HOW MANY listings each source produced; this section tells you WHICH listings and WHY they were tagged the way they were.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Axial | High-Growth AI Services Firm | undisclosed | undisclosed | $2M | undisclosed | AI services / GovCon | not disclosed | BROKER-OPPORTUNISTIC | Financially plausible broker-platform lead with no hard-exclude, but no active thesis corpus match. |
| Everingham and Kerr, Inc. | Medical Animation and Visualization and Digital Media Company | undisclosed | undisclosed | undisclosed | undisclosed | digital media | not disclosed | FLAG | Too sparse to evaluate; no financials disclosed and no active thesis match. |
| Everingham and Kerr, Inc. | Commercial and Industrial Air Purification Systems Company | undisclosed | undisclosed | undisclosed | undisclosed | air purification / industrial | not disclosed | FLAG | Ambiguous product/service split; no financials disclosed. |
| Business Exits | DOT Pre-Qualified Civil and Site Work Contractor | Southeast and Gulf Coast | $7,873,849 | $1,692,242 | 21.5% | civil and site work contractor | not disclosed | HARD-REJECT | Construction/labor-heavy field services are hard-excluded. |
| Flavia Milano, IAG Service | Midwest Outdoor Living and Specialty Contractor (38125) | Midwest | $35.4M | $3.8M | 10.7% | outdoor living / specialty contracting | not disclosed | HARD-REJECT | Construction/labor-heavy field services are hard-excluded. |
| BizBuySell | Own a Medical Franchise producing over $260K EBITDA built by a Pro Sports Surgeon | undisclosed | $740,796 | $263,634 | undisclosed | hyperbaric oxygen therapy / medical franchise | not disclosed | HARD-REJECT | Franchise listing or franchise-adjacent, excluded. |
| Transworld Business Advisors | Comprehensive Skin Care and Weight Loss Clinic | Bergen County, New Jersey | undisclosed | $1,004,578 SDE | undisclosed | medical / skin care | not disclosed | HARD-REJECT | Provider-owned healthcare is hard-excluded. |
| New Deal via Axial | Direct-to-Consumer Home Protection Brand | undisclosed | $13.2M LTM net sales | undisclosed | 80% gross margin | home protection brand | not disclosed | HARD-REJECT | Consumer retail / DTC hard-excluded. |
| New Deal via Axial | Premier Mid-Atlantic Commercial HVAC Company | mid-Atlantic | undisclosed | undisclosed | undisclosed | HVAC | not disclosed | HARD-REJECT | Construction/labor-heavy field services are hard-excluded. |
| Everingham and Kerr, Inc. | NJ-based Commercial and Residential Landscaping and Construction Company | New Jersey | undisclosed | undisclosed | undisclosed | landscaping / construction | not disclosed | HARD-REJECT | Construction/labor-heavy field services are hard-excluded. |

## Source Scorecard

Every source scanned this run MUST appear as a row — no exceptions. Missing rows = scan agent skipped a source and the run fails its stop hook.

Dashboard source categories are intentionally limited to three audience-facing buckets:
- `Marketplace` — searchable listing sites or buyer platforms the skill scrubs directly.
- `Newsletter` — recurring broker/platform blasts, saved-search alerts, or membership digests parsed from email.
- `Direct email` — any intermediary, broker, advisor, or contact email addressed to Kay with a particular deal reference.

Manual deal-source work is separate from reviewed sources. Only marketplace-style sources that require login, setup, registration, or manual search should appear in the manual queue; direct relationship/email sources should not be shown as manual marketplace work.

Dashboard deal status is binary for Kay: `Matches` = PASS rows; `Filtered out` = every non-PASS row, including broker-opportunistic, near-miss, flag, and hard-reject. Keep internal lanes in artifacts if useful for calibration, but do not expose a separate borderline/learning metric on the dashboard.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | Marketplace | active | 200 | 1 | 0 | — |
| DealForce | Marketplace | active email alerts | — | 0 | 0 | — |
| Empire Flippers | Marketplace | active | — | 0 | 0 | — |
| Rejigg | Marketplace | active | — | 0 | 0 | — |
| Baton Market | Marketplace | active email alerts | — | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Marketplace | active | — | 0 | 0 | — |
| Axial | Marketplace | pending G&B registration | — | 3 | 0 | — |
| BizBuySell | Newsletter | active email/newsletter | — | 1 | 0 | — |
| Everingham & Kerr | Newsletter | active email-only | — | 3 | 0 | 2026-06-17 |
| Viking Mergers (email-only) | Newsletter | active email-only | — | 0 | 0 | — |
| Viking Mergers (newsletter) | Newsletter | active newsletter | — | 0 | 0 | — |
| Calder Capital | Newsletter | active email-only | — | 0 | 0 | — |
| PCO Bookkeepers | Newsletter | active | — | 0 | 0 | — |
| BizQuest Search Agent | Newsletter | observed active email | — | 0 | 0 | — |
| Transworld Business Advisors | Newsletter | observed active email | — | 1 | 0 | — |
| IAG M&A Advisors | Direct email | active | — | 1 | 0 | — |
| GP Bullhound | Direct email | active | — | 0 | 0 | — |
| Sica Fletcher | Direct email | active | — | 0 | 0 | — |
| DealsX replies | Direct email | active | — | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 1
- 7-day rolling average: 0.0
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality
