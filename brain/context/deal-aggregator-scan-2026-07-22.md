---
date: 2026-07-22
deals_found: 0
sources_scanned: 18
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 0
email_scan_status: live
---

# Deal Aggregator Scan — 2026-07-22

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
None today.

## DealsX Proprietary Outreach Replies
Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs — no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.
None today.

## Broker Opportunistic Review
None today.

## Near Misses (not Slacked)
- BizBuySell — Established, Profitable Pet Waste Removal Business — recurring local service but no financials
- BizBuySell — Western Slope CO CPA Practice for Sale — recurring client base implied, but too small / no financial detail
- BizQuest Search Agent — Technology Integration & Low-Voltage Infrastructure Company — possible low-voltage / security adjacency but insufficient disclosed detail
- Transworld Business Advisors — Profitable Virtual CORP Events, Gifting, Scalable, GWTH RDY — plausible B2B services but sub-scale and no active thesis match
- Transworld Business Advisors — Absentee Run Recording Studio Established 20-Year in Brooklyn — local service asset, but no recurring contract evidence and no active thesis match
- Axial — Janitorial Commercial Services — commercial cleaning is adjacent to active thesis, but the listing is too generic to confirm the high-end wedge

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens (e.g. broker-buy-box reruns, dual-filter retroactive replays) a 5-minute query instead of a 90-minute artifact-mining exercise. Aggregate counts in Source Scorecard tell you HOW MANY listings each source produced; this section tells you WHICH listings and WHY each was tagged the way it was.

Required when ≥ 1 listing was reviewed. If zero listings were reviewed (every source blocked), emit the table header only, with no data rows. Sort: PASS first, then NEAR-MISS, then FLAG, then HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Axial | Janitorial Commercial Services | undisclosed | undisclosed | undisclosed | undisclosed | commercial cleaning | service criticality | NEAR-MISS | commercial cleaning is adjacent to active thesis, but the listing is too generic to confirm the high-end wedge |
| BizBuySell | Established, Profitable Pet Waste Removal Business | CA | undisclosed | $200,000 asking price | undisclosed | pet services | recurring/reoccurring revenue | NEAR-MISS | recurring local service but no financials |
| BizBuySell | Western Slope CO CPA Practice for Sale | CO | undisclosed | $875,000 asking price | undisclosed | professional services / accounting | cohort/customer durability | NEAR-MISS | recurring client base implied, but too small / no financial detail |
| Transworld Business Advisors | Absentee Run Recording Studio Established 20-Year in Brooklyn | Kings County, NY | $325,000 | $134,988 | undisclosed | media / studio | not disclosed | NEAR-MISS | local service asset, but no recurring contract evidence and no active thesis match |
| Transworld Business Advisors | Profitable Virtual CORP Events, Gifting, Scalable, GWTH RDY | United States | $1,300,000 | $458,863 | undisclosed | events / gifting | not disclosed | NEAR-MISS | plausible B2B services but sub-scale and no active thesis match |
| BizQuest Search Agent | Scalable Personal Property Resale And Downsizing Services Operation | Syracuse, NY | undisclosed | undisclosed | undisclosed | resale / downsizing services | not disclosed | FLAG | estate-management adjacency is too thin without contract / revenue detail |
| BizQuest Search Agent | Technology Integration & Low-Voltage Infrastructure Company | New York | undisclosed | undisclosed | undisclosed | infrastructure services | not disclosed | FLAG | possible low-voltage / security adjacency but insufficient disclosed detail |
| BizBuySell | Established Apex Pizzeria for Sale | NC | undisclosed | $249,999 asking price | undisclosed | food service / pizza | not disclosed | HARD-REJECT | restaurant hard-exclude |
| BizBuySell | Professional Commercial Kitchen Ready to Operate | GA | undisclosed | Not Disclosed | undisclosed | food service / kitchen | not disclosed | HARD-REJECT | restaurant / hospitality exposure hard-exclude |
| BizBuySell | Top-Performing Deli Delicious Franchise - 13+ Years of Proven Success | CA | undisclosed | $415,000 asking price | undisclosed | franchise / restaurant | not disclosed | HARD-REJECT | franchise + restaurant hard-exclude |
| BizBuySell | Well-Established Electrical Contracting Business | MN | undisclosed | $550,000 asking price | undisclosed | electrical contracting | not disclosed | HARD-REJECT | construction / labor-heavy field services hard-exclude |
| BizBuySell | West Phoenix Primary Care | AZ | undisclosed | $550,000 asking price | undisclosed | healthcare / primary care | not disclosed | HARD-REJECT | physician practice hard-exclude |
| BizQuest Search Agent | Profitable Watercolor Stationery Brand Serving the Wedding Market | Tuckahoe, NY | undisclosed | undisclosed | undisclosed | ecommerce / stationery | not disclosed | HARD-REJECT | consumer retail / ecommerce brand |
| Business Exits | Swimwear Amazon Ecommerce Company - SBA Eligible | West (Remote Possible) | $3,256,592 | $661,185 profit (proxy) | undisclosed | ecommerce / apparel | not disclosed | HARD-REJECT | consumer retail / DTC hard-exclude |
| Everingham & Kerr | New Acquisition Opportunity - Provider of Metal Manufacturing; Precision Machining, Stamping & Tool & Die | undisclosed | undisclosed | undisclosed | undisclosed | manufacturing / metalworking | cohort/customer durability | HARD-REJECT | capital-intensive manufacturing hard-exclude |
| Transworld Business Advisors | Behavioral Health AI Software Platform - Strategic Acquisition | New York | pre-revenue | $0 | undisclosed | software / health tech | not disclosed | HARD-REJECT | pre-revenue software / not a vertical SaaS fit |
| Transworld Business Advisors | Beloved Pet Store Turn Key Opportunity for New Passionate Owner | Dutchess County, NY | $49,000 | $0 | undisclosed | retail / pet | not disclosed | HARD-REJECT | consumer retail hard-exclude |
| Transworld Business Advisors | Experienced Bakers! 60-Yr Legacy | Queens, NY | $1,500,000 | $487,719 | undisclosed | bakery / cafe | not disclosed | HARD-REJECT | bakery / cafe falls inside restaurant/hospitality hard-exclude |
| Transworld Business Advisors | Healthy Dining Near SUNY New Paltz - Seller Financing Offered | New Paltz, Ulster County, NY | $195,000 | $79,046 | undisclosed | restaurant / dining | not disclosed | HARD-REJECT | restaurant hard-exclude |

Verdict definitions:
- `PASS` — clears buy-box gate AND matches an active niche corpus. Slack-posted (subject to fingerprint dedup).
- `BROKER-OPPORTUNISTIC` — clears disclosed financial/structural gate from a broker/platform/opportunistic channel, has no hard-exclude, but no active-niche corpus match; OR sits in the `$750K-$3M` EBITDA review band with strong recurring/reoccurring revenue, cohort/customer durability, or service-criticality signal. Artifact-only, not Slack-posted by default.
- `NEAR-MISS` — partially promising, sparse, or useful for thesis/corpus tuning, but not enough for pass or broker-opportunistic review.
- `HARD-REJECT` — fails buy-box on a disclosed-and-failed criterion, hits an industry hard-exclude, or geography hard-excluded.
- `FLAG` — undisclosed-field heavy or ambiguous; logged for human review without auto-rejection.

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
| BizBuySell | Newsletter | active email newsletter | 403 | 7 | 0 | — |
| Business Exits | Marketplace | active | 200 | 1 | 0 | — |
| DealForce | Marketplace | active email alerts | 200 | 0 | 0 | — |
| Empire Flippers | Marketplace | active | 200 | 0 | 0 | — |
| Everingham & Kerr | Newsletter | active email-only | 200 | 1 | 1 | 2026-06-17 |
| IAG M&A Advisors | Direct email | active email alerts | 200 | 0 | 0 | — |
| Rejigg | Marketplace | active email alerts | 200 | 0 | 0 | — |
| Viking Mergers | Newsletter | active email-only | 403 | 0 | 0 | — |
| Viking Mergers | Newsletter | active newsletter | 403 | 0 | 0 | — |
| Baton Market | Marketplace | active email alerts | 200 | 0 | 0 | — |
| Calder Capital | Newsletter | active email-only | 406 | 0 | 0 | — |
| GP Bullhound | Direct email | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Newsletter | active | 200 | 0 | 0 | — |
| Sica Fletcher | Direct email | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Marketplace | active | 200 | 0 | 0 | — |
| Axial | Marketplace | pending G&B registration | 403 | 1 | 0 | — |
| BizQuest Search Agent | Newsletter | active email/newsletter (new source) | 403 | 3 | 0 | — |
| Transworld Business Advisors | Newsletter | active email/newsletter (new source) | 403 | 6 | 1 | 2026-07-15 |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 0
- 7-day rolling average: 0.0
- Target: 1–3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality
