---
schema_version: 1.1.0
date: 2026-07-30
type: context
title: Deal Aggregator Scan — 2026-07-30
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 2
email_scan_status: live
buy_box_source: live
tags:
  - date/2026-07-30
  - context
  - source/deal-aggregator
  - status/published
---

# Deal Aggregator Scan — 2026-07-30

Morning headless run. Buy-boxes were loaded live from Drive, active niches were loaded from `WEEKLY REVIEW`, DealsX corpus was loaded from `DEALSX`, and the latest niche-intelligence watchlist was loaded for corpus-only calibration. Corpus paths used for active theses:
- Premium Pest Management → WR row enrichment (Niche Hypothesis + Quick notes)
- Estate Management Companies → DealsX keywords ("Estate Management Companies")
- High-End Commercial Cleaning → DealsX keywords ("High-End Commercial Cleaning")

New-niche watchlist loaded for review-only signals: Broker-Dealer Compliance and Outsourced Insurance SIU and Fraud Investigation Services.
Paused / paywalled exclusions were honored: SMB Deal Hunter / Helen Guo rows were ignored, and paused SaaS sources were not treated as active deal flow.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. Eighteen email-inbound listings were reviewed from active sources ([[entities/bizbuysell|BizBuySell]], [[entities/axial|Axial]], and [[entities/transworld-business-advisors|Transworld Business Advisors]]), but none were surfaced as email-deal items for Slack. Paused SaaS / paywalled Deal Hunter rows were excluded per standing rules.

## DealsX Proprietary Outreach Replies

None today.

## Broker Opportunistic Review

Artifact-only review items from broker/platform channels that cleared the disclosed financial plausibility gate but did not match an active thesis corpus:

1. [[entities/axial|Axial]] — Rapid Growth $3.3mn EBITDA New Jersey Based Warehousing Provider | NJ | undisclosed | $3.3M | undisclosed | warehousing | Key signals: strong EBITDA, B2B logistics durability, NJ footprint | Preserve for CIO review as broker-opportunistic despite no active thesis match | brain/context/email-scan-results-2026-07-30.md
2. [[entities/transworld-business-advisors|Transworld Business Advisors]] — Thriving Food Distributor with Strong Profits and Large Territory | New York | asking $7M | undisclosed | undisclosed | distribution | Key signals: strong profits, large territory, recurring B2B buyer base implied | Preserve for CIO review as broker-opportunistic despite no active thesis match | brain/context/email-scan-results-2026-07-30.md

## Near Misses

- [[entities/bizbuysell|BizBuySell]] — Established Carpet Cleaning & Restoration Co. | Oregon | cleaning / restoration | Cleaning-adjacent and commercially plausible, but financials and contract depth were not disclosed enough to clear the gate.
- [[entities/bizbuysell|BizBuySell]] — B2B Technical Furniture Dealer for Trading Floors & Control Rooms | New York | industrial / dealer | Interesting B2B industrial profile, but financials were not disclosed and the active-thesis corpus did not match cleanly.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| [[entities/bizbuysell|BizBuySell]] | Established Carpet Cleaning & Restoration Co. | Oregon | undisclosed | undisclosed | undisclosed | cleaning / restoration | not disclosed | NEAR-MISS | Cleaning-adjacent and commercially plausible, but not enough disclosed detail to clear the gate |
| [[entities/bizbuysell|BizBuySell]] | B2B Technical Furniture Dealer for Trading Floors & Control Rooms | New York | undisclosed | undisclosed | undisclosed | industrial / dealer | not disclosed | NEAR-MISS | No disclosed financials and no active-thesis match |
| [[entities/bizbuysell|BizBuySell]] | Fun, Very profitable sports biz, +47% profit/ 3 yrs | Florida | undisclosed | undisclosed | 47% | sports / services | not disclosed | FLAG | Sparse information and no active-thesis match |
| [[entities/axial|Axial]] | Multi-Market Ground Transportation Services Platform | undisclosed | undisclosed | undisclosed | undisclosed | transportation | not disclosed | FLAG | Platform-style listing with no disclosed financials |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Absentee Run Recording Studio Established 20-Year in Brooklyn | New York | asking $325K | SDE $134,988 | undisclosed | media / studio | not disclosed | FLAG | Not enough disclosed detail to promote beyond review |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Behavioral Health AI Software Platform - Strategic Acquisition | New York | asking $1.25M | undisclosed | undisclosed | software / healthcare | not disclosed | FLAG | Strategic software acquisition, but not a vertical-SaaS buy-box match |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Multilingual Translation & Language Services Business | Pennsylvania | asking $50K | SDE $2,418 | undisclosed | services | not disclosed | HARD-REJECT | Disclosed profit is far below the Services floor and the deal is too small |
| [[entities/bizbuysell|BizBuySell]] | 2nd Generation Roofing Repair & New Installation Business | New York | undisclosed | undisclosed | undisclosed | roofing | not disclosed | HARD-REJECT | Construction / labor-heavy field services hard-exclude |
| [[entities/bizbuysell|BizBuySell]] | Profitable Chiropractic Rehab Center with Massive Patient Base | Connecticut | undisclosed | undisclosed | undisclosed | healthcare | not disclosed | HARD-REJECT | Physician / provider-owned healthcare hard-exclude |
| [[entities/bizbuysell|BizBuySell]] | Waterfront Beach Club & Event Venue - 36+ Years Established | New York | $13.6M asking | undisclosed | undisclosed | hospitality / venue | not disclosed | HARD-REJECT | Hospitality / events hard-exclude |
| [[entities/bizbuysell|BizBuySell]] | Pirtek USA | near you | $211K-$610K capital required | undisclosed | undisclosed | franchise | not disclosed | HARD-REJECT | Franchise hard-exclude |
| [[entities/bizbuysell|BizBuySell]] | Code Ninjas, LLC. | near you | $177K-$385.5K capital required | undisclosed | undisclosed | franchise | not disclosed | HARD-REJECT | Franchise hard-exclude |
| [[entities/bizbuysell|BizBuySell]] | Complete Weddings + Events | near you | $35.8K-$71.9K capital required | undisclosed | undisclosed | franchise | not disclosed | HARD-REJECT | Franchise and events / hospitality adjacency hard-exclude |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Established Kitchen and Bath Cabinet Manufacturer | Connecticut | $1.5M asking | undisclosed | undisclosed | manufacturing | not disclosed | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Beloved Pet Store Turn Key Opportunity for New Passionate Owner | New York | $49K asking | $0 SDE | undisclosed | retail | not disclosed | HARD-REJECT | Consumer retail hard-exclude |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Healthy Dining Near SUNY New Paltz - Seller Financing Offered | New York | $195K asking | $79,046 SDE | undisclosed | restaurant | not disclosed | HARD-REJECT | Restaurant / hospitality hard-exclude |
| [[entities/transworld-business-advisors|Transworld Business Advisors]] | Thriving Food Distributor with Strong Profits and Large Territory | New York | asking $7M | undisclosed | undisclosed | distribution | Key signals: strong profits, territory density, repeat B2B demand implied | BROKER-OPPORTUNISTIC | No active-thesis match; preserve because it appears financially plausible |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| [[entities/bizbuysell|BizBuySell]] | General | active email newsletter | n/a | 9 | 0 | — |
| Business Exits | General | active | n/a | 0 | 0 | — |
| DealForce | General | active | n/a | 0 | 0 | — |
| Empire Flippers | General | active | n/a | 0 | 0 | — |
| [[entities/everingham-kerr|Everingham & Kerr]] | General | active email-only | n/a | 0 | 1 | 2026-06-17 |
| IAG M&A Advisors | General | active email alerts | n/a | 0 | 0 | — |
| [[entities/rejigg|Rejigg]] | General | active email alerts | n/a | 0 | 0 | — |
| Viking Mergers | General | active email-only | n/a | 0 | 0 | — |
| Viking Mergers | General | active newsletter | n/a | 0 | 0 | — |
| [[entities/baton-market|Baton Market]] | General | active email alerts | n/a | 0 | 0 | — |
| Calder Capital | General | active email-only | n/a | 0 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | n/a | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | n/a | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | n/a | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Mgmt) | active | n/a | 0 | 0 | — |

## Volume Check

- Deals surfaced today: 0
- Broker-opportunistic review items: 2
- 7-day rolling average: below target
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: screening strictness
