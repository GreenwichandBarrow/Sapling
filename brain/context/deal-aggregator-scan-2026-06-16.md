---
schema_version: 1.1.0
date: 2026-06-16
type: output
output_type: deal-aggregator-scan
status: draft
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 0
sources_blocked_single_attempt: 3
email_deals: 1
dealsx_replies: 0
broker_opportunistic: 0
email_scan_status: live
buy_box_source: live
tags: [date/2026-06-16, output, output/deal-aggregator-scan, source/deal-aggregator, topic/deal-aggregator, topic/morning-briefing]
---

# Deal Aggregator Scan - 2026-06-16

Morning headless run. Buy-box docs read live from Drive. Active niches loaded from WEEKLY REVIEW + DEALSX.

Corpus paths used this run:
- Premium Pest Management -> DealsX keywords
- Estate Management Companies -> DealsX keywords
- High-End Commercial Cleaning -> DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) -> DealsX keywords
- Storage & Related Services for High Value Assets -> DealsX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries -> DealsX keywords

BROWSER_AUTOMATION_UNAVAILABLE: BizBuySell, Quiet Light, and Viking Mergers required browser fallback for deeper listing inspection; agent-browser is not installed, so only shell-level scanning was possible this run.

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
1. **Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die** - Everingham & Kerr | Blast | over $20M revenue, over $4.2M EBITDA, ~21% margin, Mid Atlantic Region | HARD-REJECT: capital-intensive manufacturing is a Services Buy Box hard-exclude.

## DealsX Proprietary Outreach Replies
Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs - no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.
None today.

## Broker Opportunistic Review
Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
None today.

## Near Misses
None today.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Everingham & Kerr | Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die | Mid Atlantic Region | over $20M | over $4.2M | ~21% | metal manufacturing / precision machining / stamping / tool & die | not disclosed | HARD-REJECT | capital-intensive manufacturing is an industry hard-exclude under the Services Buy Box |

## Source Scorecard

Every source scanned this run appears as a row.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 0 | 0 | — |
| BizBuySell | General | blocked (single-attempt) | 403 | 0 | 0 | — |
| DealForce | General | active | 200 | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 0 | 0 | — |
| Everingham & Kerr | General | active | 200 | 1 | 0 | — |
| Flippa | General | active | 200 | 0 | 0 | — |
| IAG M&A Advisors | General | active | 200 | 0 | 0 | — |
| Quiet Light | General | blocked (single-attempt) | 403 | 0 | 0 | — |
| Rejigg | General | active | 200 | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 0 | 0 | — |
| Viking Mergers | General | blocked (single-attempt) | 403 | 0 | 0 | — |
| Website Closers | General | active | 200 | 0 | 2 | 2026-06-05 |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 0 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | 200 | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 0
- 7-day rolling average: 0.0/day
- Target: 1-3/day - BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality
