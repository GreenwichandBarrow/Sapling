---
date: 2026-06-13
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 3
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 3
email_scan_status: missing
tags: [date/2026-06-13, output, topic/deal-aggregator, status/draft]
email_scan_note: email-scan-results-2026-06-13.md missing after bounded retry
browser_fallback: unavailable
---
# Deal Aggregator Scan — 2026-06-13

## Deals Surfaced
None today.

## Email Inbound Deals
None today.

## DealsX Proprietary Outreach Replies
Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs - no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.
None today.

## Broker Opportunistic Review
Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **Lead Generation Marketplace for Local Service Pros | CPL & SaaS Models | 200,000 Active Lead Buyers | 10+ Premium Domains | Massive YOY Growth** - Website Closers | undisclosed | undisclosed | Lead generation marketplace / local services SaaS | Key signals: recurring platform model implied by SaaS/CPL framing | Preserving for CIO review despite no active thesis match.
2. **SBA Pre-Qualified Web Design & Website Management Agency | 2-Year Contracts | 19-Year Firm | 350 Active Clients | Monthly Recurring Revenue** - Website Closers | undisclosed | undisclosed | Web design / website management agency | Key signals: monthly recurring revenue, 2-year contracts | Preserving for CIO review despite no active thesis match.
3. **SBA Pre-Qualified Media, Publishing & Digital Marketing Agency | 16-Year Award Winning Agency | 85% Recurring Revenue | Fully Remote** - Website Closers | undisclosed | undisclosed | Media / publishing / digital marketing agency | Key signals: 85% recurring revenue | Preserving for CIO review despite no active thesis match.

## Near Misses
- email leg unavailable - `brain/context/email-scan-results-2026-06-13.md` was still missing after the bounded retry loop.
- California Property Tax Consultants - California soft exclude and financials were undisclosed, so it stays a review item rather than a pass.
- Listing #92963 - food delivery application; no active thesis match and financials were undisclosed.

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens a 5-minute query instead of a 90-minute artifact-mining exercise.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Website Closers | Lead Generation Marketplace for Local Service Pros | undisclosed | undisclosed | undisclosed | undisclosed | Lead generation marketplace / local services SaaS | recurring revenue / platform model implied | BROKER-OPPORTUNISTIC | No active thesis match; preserve for CIO review due SaaS-model framing and buyer activity. |
| Website Closers | SBA Pre-Qualified Web Design & Website Management Agency | undisclosed | undisclosed | undisclosed | undisclosed | Web design / website management agency | recurring revenue / long contracts | BROKER-OPPORTUNISTIC | No active thesis match; preserve for CIO review due monthly recurring revenue and 2-year contracts. |
| Website Closers | SBA Pre-Qualified Media, Publishing & Digital Marketing Agency | undisclosed | undisclosed | undisclosed | undisclosed | Media / publishing / digital marketing agency | recurring revenue | BROKER-OPPORTUNISTIC | No active thesis match; preserve for CIO review due 85% recurring revenue. |
| Business Exits | California Property Tax Consultants | California | undisclosed | undisclosed | undisclosed | Property tax consulting | service criticality / recurring appeals process | FLAG | California soft exclude and financials undisclosed. |
| Empire Flippers | Listing #92963 | undisclosed | undisclosed | undisclosed | undisclosed | Application / food delivery niche | not disclosed | NEAR-MISS | Consumer app; no active thesis match and no financials disclosed. |
| Business Exits | Midwest-Based Multi-Location Wellness Practice with Exceptional Margins | undisclosed | undisclosed | undisclosed | undisclosed | Healthcare / wellness provider | not disclosed | HARD-REJECT | Provider-owned healthcare / medical practice hard-exclude. |
| Business Exits | Ireland Construction Business | Ireland | undisclosed | undisclosed | undisclosed | Construction services | not disclosed | HARD-REJECT | Construction / labor-heavy field services hard-exclude. |
| Empire Flippers | Listing #94486 | undisclosed | undisclosed | undisclosed | undisclosed | Health and wellness eCommerce / dietary supplements | not disclosed | HARD-REJECT | DTC retail / supplements eCommerce hard no. |
| Empire Flippers | Listing #94515 | undisclosed | undisclosed | undisclosed | undisclosed | Amazon FBA / Shopify home goods and wellness | not disclosed | HARD-REJECT | DTC retail / Amazon FBA and Shopify consumer goods hard no. |

## Source Scorecard

Every source scanned this run appears as a row.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 3 | 0 | — |
| DealForce | General | active | 200 | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 3 | 0 | — |
| Everingham & Kerr | General | active | 200 | 0 | 0 | — |
| Flippa | General | active | 200 | 0 | 0 | — |
| IAG M&A Advisors | General | active | 200 | 0 | 0 | — |
| Quiet Light | General | blocked (verified) | 403 | 0 | 0 | — |
| Rejigg | General | active | 200 | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active | 200 | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 0 | 0 | — |
| Viking Mergers | General | blocked (verified) | 403 | 0 | 0 | — |
| Website Closers | General | active | 200 | 3 | 2 | 2026-06-05 |
| GP Bullhound | Niche | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Niche | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche | active | 200 | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 3
- 7-day rolling average: 0.0
- Target: 1-3/day - CRITICAL
- Email leg: missing
- Funnel bottleneck: email leg
