---
schema_version: 1.1.0
date: 2026-09-02
deals_found: 0
sources_scanned: 20
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 1
email_scan_status: live
tags: [date/2026-09-02, output/deal-aggregator-scan, topic/deal-aggregator, status/done]
---

# Deal Aggregator Scan — 2026-09-02

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
None today.

## DealsX Proprietary Outreach Replies
None today.

## Broker Opportunistic Review
1. [[entities/axial|Axial]] deal blast — Marketplace | unknown revenue | $2M EBITDA | AI services / GovCon / commercial contracts | Key signals: recurring contracts, commercial services | Why it matters: financially plausible broker blast with no hard-exclude, but no active thesis corpus match | email-scan-results 2026-09-02

## Near Misses (not Slacked)
- [[entities/bizquest|BizQuest Search Agent]] high-volume B2B print / promotional / marketing center — sparse financial disclosure and ambiguous fit; keep for manual review.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens faster.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| [[entities/axial|Axial]] | $2M EBITDA High-Growth AI Services Firm - GovCon & Commercial Contracts | undisclosed | undisclosed | $2M | undisclosed | AI services / GovCon / commercial contracts | recurring contracts | BROKER-OPPORTUNISTIC | Financially plausible broker blast with no hard-exclude, but no active thesis corpus match. |
| [[entities/bizquest|BizQuest Search Agent]] | High-Volume B2B Print, Promotional & Marketing Center - Manhattan | NY | undisclosed | undisclosed | undisclosed | print / promotional / marketing center | not disclosed | FLAG | Sparse financial disclosure and ambiguous fit. |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Absentee Pair of Edible Arrangements Stores - Nassau County | NY | approx $1.18M | $173,167 SDE | undisclosed | franchise / food retail | not disclosed | HARD-REJECT | Franchise and retail exclusion. |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Four Decade Plus Cabinetry Business with Property | NJ | $3.0M | $894,597 SDE | undisclosed | cabinetry / construction | not disclosed | HARD-REJECT | Construction / labor-heavy field services exclusion. |
| [[entities/quiet-light|Quiet Light]] | 20-Year-Old Amazon Men's Accessories Brand | undisclosed | $942,119 | $12,703 earnings | undisclosed | Amazon FBA / ecommerce | not disclosed | HARD-REJECT | Paused SaaS/digital source plus consumer ecommerce / FBA exclusion. |
| [[entities/quiet-light|Quiet Light]] | 80-Year-Old Feather Brand | NJ | $311,035 | $175,970 earnings | undisclosed | ecommerce / consumer goods | not disclosed | HARD-REJECT | Paused SaaS/digital source plus consumer goods / ecommerce exclusion. |
| [[entities/quiet-light|Quiet Light]] | Business Education Platform | undisclosed | $45,161,452 | $10,843,118 earnings | undisclosed | membership / coaching / ecommerce education | not disclosed | HARD-REJECT | Paused SaaS/digital source and outside active buy-box coverage. |
| [[entities/quiet-light|Quiet Light]] | Patented DTC Cooling Brand | undisclosed | $3,863,852 | $1,038,055 earnings | undisclosed | DTC / Amazon FBA | not disclosed | HARD-REJECT | Paused SaaS/digital source plus DTC / consumer ecommerce exclusion. |
| [[entities/flippa|Flippa]] | AI-powered Messaging SaaS | undisclosed | $736,000 | undisclosed | undisclosed | SaaS / messaging | not disclosed | HARD-REJECT | Paused SaaS source and ARR/revenue below the active SaaS floor. |

## Source Scorecard

Every source scanned this run appears below. Rows include active roster sources plus observed email sources that produced listings.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| [[entities/bizbuysell|BizBuySell]] | Newsletter | active | — | 0 | 0 | — |
| [[entities/business-exits|Business Exits]] | Marketplace | active | 200 | 0 | 0 | — |
| [[entities/dealforce|DealForce]] | Marketplace | active | 200 | 0 | 0 | — |
| [[entities/empire-flippers|Empire Flippers]] | Marketplace | active | 200 | 0 | 0 | — |
| [[entities/everingham-and-kerr|Everingham & Kerr]] | Newsletter | active | — | 0 | 0 | — |
| [[entities/iag-m-and-a-advisors|IAG M&A Advisors]] | Direct email | active | 200 | 0 | 0 | — |
| [[entities/rejigg|Rejigg]] | Marketplace | active | 200 | 0 | 0 | — |
| [[entities/viking-mergers|Viking Mergers]] | Newsletter | active | — | 0 | 0 | — |
| [[entities/viking-mergers|Viking Mergers]] | Newsletter | active | — | 0 | 0 | — |
| [[entities/baton-market|Baton Market]] | Marketplace | active | 200 | 0 | 0 | — |
| [[entities/calder-capital|Calder Capital]] | Newsletter | active | — | 0 | 0 | — |
| [[entities/gp-bullhound|GP Bullhound]] | Direct email | active | 200 | 0 | 0 | — |
| [[entities/pco-bookkeepers|PCO Bookkeepers]] | Newsletter | active | 200 | 0 | 0 | — |
| [[entities/sica-fletcher|Sica Fletcher]] | Direct email | active | 200 | 0 | 0 | — |
| [[entities/synergy-business-brokers|Synergy Business Brokers Real Estate]] | Marketplace | active | 200 | 0 | 0 | — |
| [[entities/axial|Axial]] | Marketplace | active | — | 1 | 0 | — |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Newsletter | active | — | 2 | 0 | — |
| [[entities/bizquest|BizQuest Search Agent]] | Newsletter | active | — | 1 | 0 | — |
| [[entities/quiet-light|Quiet Light]] | Marketplace | dormant | — | 4 | 0 | — |
| [[entities/flippa|Flippa]] | Marketplace | dormant | — | 1 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 1
- 7-day rolling average: 0.00
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: source coverage
