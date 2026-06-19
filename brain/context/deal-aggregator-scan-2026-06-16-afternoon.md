---
schema_version: 1.1.0
date: 2026-06-16
type: output
output_type: deal-aggregator-scan
status: draft
deals_found: 0
sources_scanned: 4
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 1
dealsx_replies: 0
broker_opportunistic: 0
email_scan_status: live
buy_box_source: live
tags: [date/2026-06-16, output, output/deal-aggregator-scan, source/deal-aggregator, topic/deal-aggregator, topic/afternoon-top-up]
---

# Deal Aggregator Scan - 2026-06-16 Afternoon

Afternoon top-up run. Buy-box docs were re-read live from Drive. Active niches were re-read from WEEKLY REVIEW + DEALSX.

Corpus paths used this run:
- Premium Pest Management -> DealsX keywords
- Estate Management Companies -> DealsX keywords
- High-End Commercial Cleaning -> DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) -> DealsX keywords
- Storage & Related Services for High Value Collections -> DealsX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries -> DealsX keywords

Browser fallback unavailable: agent-browser is not installed, so JS-gated deeper inspection stayed shell-only.

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
| Everingham & Kerr email blast | Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die | Mid Atlantic Region | over $20M | over $4.2M | ~21% | metal manufacturing / precision machining / stamping / tool & die | not disclosed | HARD-REJECT | capital-intensive manufacturing is an industry hard-exclude under the Services Buy Box |

## Source Scorecard

Every source scanned this run appears as a row.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Rejigg | General | active | 200 | 0 | 0 | — |
| Flippa | General | active | 200 | 0 | 0 | — |
| Everingham & Kerr | General | active | 200 | 0 | 0 | — |
| Email channel | Channel 2 | active | n/a | 1 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 0
- 7-day rolling average: 0.0/day
- Target: 1-3/day - BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality
