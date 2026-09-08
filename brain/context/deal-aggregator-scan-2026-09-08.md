---
schema_version: 1.1.0
date: 2026-09-08
mode: morning
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 21
dealsx_replies: 0
broker_opportunistic: 1
email_scan_status: live
tags: [date/2026-09-08, output/deal-aggregator-scan, status/complete, topic/deal-aggregator]
---
# Deal Aggregator Scan — 2026-09-08

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
1. **High-Growth Distribution Company** — Samuel Curcio / Transworld Business Advisors NY | Blast | Preserved as broker-opportunistic; financially plausible broker listing, no hard-exclude, no active thesis match.
2. **Event planning and entertainment company for sale** — Calder Capital M&A | Blast | Near miss; small relative size, no active thesis match.

## DealsX Proprietary Outreach Replies
None today.

## Broker Opportunistic Review
Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **High-Growth Distribution Company** — Transworld Business Advisors NY | undisclosed | $1,446,050 | distribution | Key signals: not disclosed | Why it matters: no hard-exclude; preserve for CIO review despite thesis mismatch | —

## Near Misses (not Slacked)
- Calder Capital M&A - Event planning and entertainment company for sale - below floor, no active thesis match.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens a 5-minute query instead of a 90-minute artifact-mining exercise. Aggregate counts in Source Scorecard tell you how many listings each source produced; this section tells you which listings and why they were tagged the way they were.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Samuel Curcio / Transworld Business Advisors NY | High-Growth Distribution Company | Suffolk County, New York | undisclosed | $1,446,050 | undisclosed | distribution | not disclosed | BROKER-OPPORTUNISTIC | No hard-exclude; financially plausible broker listing outside active thesis corpus. |
| Calder Capital M&A | Event planning and entertainment company for sale | Mid-Atlantic | $432,721 | cash flow $256,088 | undisclosed | event planning / entertainment | not disclosed | NEAR-MISS | Below current floor and no active thesis match. |
| Samuel Curcio / Transworld Business Advisors NY | Behavioral Health AI Software Platform | New York | undisclosed | $0 | undisclosed | software / AI | not disclosed | FLAG | SaaS economics not disclosed; EBITDA not positive enough for the SaaS buy box. |
| Samuel Curcio / Transworld Business Advisors NY | Turnkey Dog Daycare, Boarding and Grooming | New York County, New York | undisclosed | $0 | undisclosed | pet care | not disclosed | FLAG | Consumer-service / sparse structure and financial detail; not enough to screen confidently. |
| Samuel Curcio / Transworld Business Advisors NY | SBA Pre Qual Multi-Restaurant Portfolio | Massachusetts | $4,000,000 | $459,435 | undisclosed | restaurant portfolio | not disclosed | HARD-REJECT | Restaurants are a hard no. |
| Samuel Curcio / Transworld Business Advisors NY | Commercial Restroom Partitions Business | Suffolk County, New York | $2,300,000 | -$25,256 | undisclosed | construction supply / partitions | not disclosed | HARD-REJECT | Construction supply / labor-heavy and negative EBITDA. |
| Samuel Curcio / Transworld Business Advisors NY | Established Neuropsychology and Therapy Practice | Nassau County, New York | undisclosed | $118,003 | undisclosed | healthcare / therapy | not disclosed | HARD-REJECT | Provider-owned healthcare is a hard no. |
| Samuel Curcio / Transworld Business Advisors NY | High-Volume Sports Bar and Event Venue | Nassau County, New York | undisclosed | $432,427 | undisclosed | hospitality / events | not disclosed | HARD-REJECT | Hospitality / nightlife hard no. |
| Samuel Curcio / Transworld Business Advisors NY | High-End Midtown Med Skincare Spa | New York County, New York | $400,000+ | $0 | undisclosed | med spa | not disclosed | HARD-REJECT | Provider-adjacent healthcare and zero EBITDA. |
| Samuel Curcio / Transworld Business Advisors NY | Art and Frame Business in Prime Midtown Location | New York County, New York | undisclosed | $20,391 | undisclosed | retail / framing | not disclosed | HARD-REJECT | Retail hard no. |
| Samuel Curcio / Transworld Business Advisors NY | B2B Construction Supply Co. in Queens | Queens County, New York | undisclosed | $440,361 | undisclosed | construction supply | not disclosed | HARD-REJECT | Construction supply / labor-heavy and below floor. |
| Samuel Curcio / Transworld Business Advisors NY | Multilingual Translation and Language Services Business | Pennsylvania | undisclosed | $2,418 | undisclosed | services / translation | not disclosed | HARD-REJECT | EBITDA far below current floor. |
| Samuel Curcio / Transworld Business Advisors NY | Kitchen and Bath Cabinet Manufacturer | Northeastern Connecticut | undisclosed | $0 | undisclosed | manufacturing | not disclosed | HARD-REJECT | Capital-intensive manufacturing hard no. |
| Samuel Curcio / Transworld Business Advisors NY | Absentee Run Recording Studio | Brooklyn, New York | undisclosed | $134,988 | undisclosed | recording studio | not disclosed | HARD-REJECT | Entertainment-adjacent and not B2B/B2B2C. |
| Samuel Curcio / Transworld Business Advisors NY | Urban Landscaping Business | New York County, New York | undisclosed | $290,607 | undisclosed | landscaping | not disclosed | HARD-REJECT | Construction / labor-heavy field services hard no. |
| Samuel Curcio / Transworld Business Advisors NY | Semi Passive Multi-territory Services Franchise | Fairfield, Connecticut | undisclosed | $0 | undisclosed | services franchise | not disclosed | HARD-REJECT | Franchise hard no. |
| Samuel Curcio / Transworld Business Advisors NY | Absentee Owner-Heritage Custom Frame Shop | Westchester County, New York | undisclosed | $127,131 | undisclosed | framing / retail | not disclosed | HARD-REJECT | Retail hard no. |
| Samuel Curcio / Transworld Business Advisors NY | New 2,900 SQFT Pilates Studio | New York County, New York | undisclosed | -$205,000 | undisclosed | fitness / studio | not disclosed | HARD-REJECT | Consumer fitness / not B2B, negative EBITDA. |
| Samuel Curcio / Transworld Business Advisors NY | Absentee Turnkey Edible Arrangements Location | Nassau County, New York | $590,000 | $96,243 | undisclosed | franchise / retail | not disclosed | HARD-REJECT | Franchise / retail hard no. |
| Samuel Curcio / Transworld Business Advisors NY | Absentee Pair of Edible Arrangements Stores | Nassau County, New York | $1.18M | $173,167 | undisclosed | franchise / retail | not disclosed | HARD-REJECT | Franchise / retail hard no. |
| Samuel Curcio / Transworld Business Advisors NY | Carpet and Tile Business | Nassau County, New York | undisclosed | $131,815 | undisclosed | flooring / retail | not disclosed | HARD-REJECT | Retail / labor-heavy and not thesis-aligned. |

## Source Scorecard

Every source scanned this run MUST appear as a row. Missing rows mean the scan skipped a source.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | Marketplace | active | 200 | 0 | 0 | — |
| DealForce | Marketplace | active | 200 | 0 | 0 | — |
| Empire Flippers | Marketplace | active | 200 | 0 | 0 | — |
| Rejigg | Marketplace | active | 200 | 0 | 0 | — |
| Baton Market | Marketplace | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Marketplace | active | 200 | 0 | 0 | — |
| BizBuySell | Newsletter | active | 403 | 0 | 0 | — |
| Everingham & Kerr | Newsletter | active | 200 | 0 | 0 | — |
| Viking Mergers | Newsletter | active | 200 | 0 | 0 | — |
| Calder Capital | Newsletter | active | 200 | 1 | 0 | — |
| PCO Bookkeepers | Newsletter | active | 200 | 0 | 0 | — |
| Transworld Business Advisors NY | Newsletter | active | — | 20 | 0 | — |
| IAG M&A Advisors | Direct email | active | 200 | 0 | 0 | — |
| Sica Fletcher | Direct email | active | 200 | 0 | 0 | — |
| GP Bullhound | Direct email | active | 200 | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 1
- 7-day rolling average: 0.0/day
- Target: 1-3/day - BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality
