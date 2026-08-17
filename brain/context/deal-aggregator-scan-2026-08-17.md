---
schema_version: 1.1.0
date: 2026-08-17
type: context
title: Deal Aggregator Scan — 2026-08-17
deals_found: 0
sources_scanned: 16
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 2
email_scan_status: live
buy_box_source: live
sourcing_sheet_source: live
dealsx_source: stale
tags: [date/2026-08-17, context, source/deal-aggregator, status/published]
---

# Deal Aggregator Scan — 2026-08-17

Morning headless run. Buy-boxes loaded live from Drive. Active niches loaded from `WEEKLY REVIEW`. DealsX corpus loaded from `DEALSX`. New-niche watchlist loaded for review-only signals. Paused SaaS and paywalled Deal Hunter sources were excluded from the active review set.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today.

## DealsX Proprietary Outreach Replies

None today.

## Broker Opportunistic Review

1. [[entities/axial|Axial]] — GPO business with 86% margin and $5M TTM | undisclosed | $5M TTM | undisclosed | group purchasing / distribution | Key signals: financially plausible | Very high-margin B2B distribution-like profile; no active thesis match but financially plausible. | [[brain/context/email-scan-results-2026-08-17.md]]
2. [[entities/buyyourbiz|BuyYourBiz]] — Specialize in ATM Management Services | multi-state Mid-South corridor | $6.8M | $945,720 | ATM and Bitcoin ATM services | Key signals: financially plausible | Recurring service model with disclosed revenue/EBITDA and no hard-exclude. | [[brain/context/email-scan-results-2026-08-17.md]]

## Near Misses (not Slacked)

None today.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens a fast query instead of artifact-mining.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| [[entities/axial|Axial]] | GPO business with 86% margin and $5M TTM | undisclosed | $5M TTM | undisclosed | 86% margin | group purchasing / distribution | financially plausible | BROKER-OPPORTUNISTIC | Very high-margin B2B distribution-like profile; no active thesis match but financially plausible. |
| [[entities/buyyourbiz|BuyYourBiz]] | Specialize in ATM Management Services | multi-state Mid-South corridor | $6.8M | $945,720 | 34.6% | ATM and Bitcoin ATM services | financially plausible | BROKER-OPPORTUNISTIC | Recurring service model with disclosed revenue/EBITDA and no hard-exclude. |
| [[entities/axial|Axial]] | High-performance 3PL distribution business | national reach | undisclosed | undisclosed | undisclosed | logistics / 3PL | not disclosed | FLAG | Distribution/logistics with no disclosed financials; preserve for review only. |
| [[entities/axial|Axial]] | Medical animation and digital media provider | undisclosed | undisclosed | undisclosed | undisclosed | media services | not disclosed | FLAG | Digital media / services listing with no disclosed financials and no active-thesis match. |
| [[entities/axial|Axial]] | Self-storage platform company | undisclosed | undisclosed | undisclosed | undisclosed | self-storage | not disclosed | FLAG | Platform-like listing with no disclosed financials; real-estate-adjacent and too sparse to clear. |
| [[entities/everingham-kerr|Everingham & Kerr]] | Industrial and safety equipment distribution company | undisclosed | undisclosed | undisclosed | undisclosed | industrial distribution | not disclosed | FLAG | Industrial distribution with no disclosed financials; preserve for review only. |
| [[entities/axial|Axial]] | Regional landscape and construction services provider | regional | undisclosed | undisclosed | undisclosed | landscaping and construction | not disclosed | HARD-REJECT | Construction / labor-heavy services hard-exclude. |
| [[entities/bizbuysell|BizBuySell]] | Premium pre-owned car dealership | Florida | $4,000,000 | undisclosed | undisclosed | auto dealership | not disclosed | HARD-REJECT | Retail auto dealership hard-exclude. |
| [[entities/bizbuysell|BizBuySell]] | Profitable hospitality opportunity | North Carolina | $2,900,000 | undisclosed | undisclosed | hospitality | not disclosed | HARD-REJECT | Hospitality hard-exclude. |
| [[entities/bizbuysell|BizBuySell]] | Profitable wine and liquor store in growing Orange County market | New York | $240,000 | undisclosed | undisclosed | retail liquor store | not disclosed | HARD-REJECT | Consumer retail hard-exclude. |
| [[entities/bizbuysell|BizBuySell]] | Stone and concrete restoration service | Texas | $1,000,000 | undisclosed | undisclosed | restoration services | not disclosed | HARD-REJECT | Construction / labor-heavy field services hard-exclude. |
| [[entities/bizbuysell|BizBuySell]] | Thriving electrical contractor, semi-absentee | New York | $3,300,000 | undisclosed | undisclosed | electrical contracting | not disclosed | HARD-REJECT | Construction / labor-heavy field services hard-exclude. |
| [[entities/everingham-kerr|Everingham & Kerr]] | Commercial HVAC contractor | Eastern PA | undisclosed | undisclosed | undisclosed | HVAC contracting | not disclosed | HARD-REJECT | Labor-heavy field services hard-exclude. |

## Source Scorecard

Every source scanned this run appears below. Active roster sources are preserved even when no new listings surfaced.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| [[entities/bizbuysell|BizBuySell]] | Newsletter | active email newsletter | n/a | 5 | 0 | — |
| Business Exits | Marketplace | active | n/a | 0 | 0 | — |
| [[entities/dealforce|DealForce]] | Marketplace | active email alerts | n/a | 0 | 0 | — |
| [[entities/empire-flippers|Empire Flippers]] | Marketplace | active | n/a | 0 | 0 | — |
| [[entities/everingham-kerr|Everingham & Kerr]] | Newsletter | active email-only | n/a | 2 | 0 | — |
| [[entities/iag-m-and-a-advisors|IAG M&A Advisors]] | Direct email | active email alerts | n/a | 0 | 0 | — |
| [[entities/rejigg|Rejigg]] | Marketplace | active email alerts | n/a | 0 | 0 | — |
| [[entities/viking-mergers|Viking Mergers]] | Newsletter | active email-only | n/a | 0 | 0 | — |
| [[entities/viking-mergers|Viking Mergers]] | Newsletter | active newsletter | n/a | 0 | 0 | — |
| [[entities/baton-market|Baton Market]] | Marketplace | active email alerts | n/a | 0 | 0 | — |
| [[entities/calder-capital|Calder Capital]] | Newsletter | active email-only | n/a | 0 | 0 | — |
| GP Bullhound | Direct email | active | n/a | 0 | 0 | — |
| [[entities/pco-bookkeepers|PCO Bookkeepers]] | Newsletter | active | n/a | 0 | 0 | — |
| [[entities/sica-fletcher|Sica Fletcher]] | Direct email | active | n/a | 0 | 0 | — |
| [[entities/synergy-business-brokers|Synergy Business Brokers Real Estate]] | Marketplace | active | n/a | 0 | 0 | — |
| [[entities/buyyourbiz|BuyYourBiz]] | Newsletter | active inbox-observed | n/a | 1 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 2
- 7-day rolling average: below target
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: screening strictness
