---
schema_version: 1.1.0
date: 2026-06-15
type: output
output_type: deal-aggregator-scan
status: draft
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 3
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 5
email_scan_status: live
buy_box_source: live
tags:
  - date/2026-06-15
  - output
  - output/deal-aggregator-scan
  - source/deal-aggregator
  - topic/deal-aggregator
  - topic/morning-briefing
---

# Deal Aggregator Scan - 2026-06-15

Morning headless run (Mon). Buy-box docs read live from Drive. Active niches loaded from WEEKLY REVIEW + DEALSX.

Corpus paths used this run:
- Premium Pest Management -> DealsX keywords
- Private art advisory firms -> WR row enrichment (Niche Hypothesis + Quick notes)
- Estate Management Companies -> DealsX keywords
- Specialty Coffee Equipment Service -> DealsX keywords
- High-End Commercial Cleaning -> DealsX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries -> DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) -> DealsX keywords
- Storage & Related Services for High Value Assets -> DealsX keywords

BROWSER_AUTOMATION_UNAVAILABLE: BizBuySell, Quiet Light, and Viking Mergers required browser fallback for deeper listing inspection; Flippa exposed a JS shell with no card data in raw HTML, so only shell-level scanning was possible this run.

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. Email-intelligence found no actionable CIMs, broker teasers, or DealsX replies in the 2026-06-15 inbox artifact.

## DealsX Proprietary Outreach Replies

None today.

## Broker Opportunistic Review

Financially plausible broker/platform listings that do not match an active thesis corpus. Artifact-only by default; use this lane for CIO review and corpus/source tuning.
1. **California Property Tax Consultants** - Business Exits | $6.68M | $4.68M | Key signals: Recurring tax-compliance service | No active-niche corpus match; preserve for CIO review | https://businessexits.com/listing/ca_property_tax_consultants/
2. **Healthcare Professional Development Agency** - Website Closers | undisclosed | undisclosed | Key signals: 300+ clients; no ownership reliance | No active-niche corpus match; preserve for CIO review | https://www.websiteclosers.com/businesses/sba-pre-qualified-healthcare-professional-development-agency-300-clients-strong-yoy-growth-15-years-15-coaches-33-net-margin-no-ownership-reliance/119047/
3. **Lead Generation Marketplace for Local Service Pros** - Website Closers | $9.6M gross income | $2.37M cash flow | Key signals: 200,000 active lead buyers; SaaS model | No active-niche corpus match; preserve for CIO review | https://www.websiteclosers.com/businesses/lead-generation-marketplace-for-local-service-pros-cpl-saas-models-200-000-active-lead-buyers-10-premium-domains-massive-yoy-growth/118958/
4. **Mission-Critical SaaS for Financial Trading Firms** - Website Closers | undisclosed | undisclosed | Key signals: High-margin recurring SaaS; blue-chip clients | No active-niche corpus match; preserve for CIO review | https://www.websiteclosers.com/businesses/software-platform-for-saas-infrastructure-tech-stack-for-saas-prop-trading-firms-50-enterprise-clients-180k-aov-1-million-active-traders/118819/
5. **AI News Intelligence & Data Platform** - Website Closers | undisclosed | undisclosed | Key signals: Real-time API news data; recurring subscription | No active-niche corpus match; preserve for CIO review | https://www.websiteclosers.com/businesses/ai-news-intelligence-data-platform-real-time-api-news-data-fintech-trading-platforms-ai-model-training-massive-yoy-growth-97-recurring-revenue/118930/

## Near Misses (not Slacked)

- **GovCon IT Firm - 120+ Million in Judiciary & VA-Focused Contracts** (Business Exits) - Outside active niche corpus
- **Full Service Digital Marketing Agency** (Website Closers) - Agency economics are plausible but outside active niche corpus
- **AI-Driven Ed-Tech Platform** (Website Closers) - Strong recurring revenue but not an active niche
- **Sales Coaching & Lead Generation Training Platform** (Website Closers) - Interesting recurring education product, but not active niche
- **Award Winning, SBA Pre-Qualified Marketing & PR Agency** (Website Closers) - Outside active niche corpus
- **67-Year Cayman Islands Architectural Design Firm** (Website Closers) - Foreign service firm outside active niche corpus
- **Procurement Services & Distribution Company** (Website Closers) - B2B but outside active niche corpus
- **Growing LED Display Solutions Company** (Synergy Business Brokers) - Outside active niche corpus
- **Short-Term Rental Property Management Company: 80+ Prime Locations** (Synergy Business Brokers Real Estate) - Adjacency to property management, but not the estate-management thesis

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. This is the per-listing forensic log that makes future re-screens a 5-minute query instead of a 90-minute artifact-mining exercise.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Business Exits | California Property Tax Consultants | California | $6.68M | $4.68M | ~70% | Property tax consulting | Recurring tax-compliance service | BROKER-OPPORTUNISTIC | No active-niche corpus match; preserve for CIO review |
| Website Closers | Healthcare Professional Development Agency | undisclosed | undisclosed | undisclosed | 33% | Healthcare professional development / training | 300+ clients; no ownership reliance | BROKER-OPPORTUNISTIC | No active-niche corpus match; preserve for CIO review |
| Website Closers | Lead Generation Marketplace for Local Service Pros | undisclosed | $9.6M gross income | $2.37M cash flow | undisclosed | Lead generation marketplace / local services SaaS | 200,000 active lead buyers; SaaS model | BROKER-OPPORTUNISTIC | No active-niche corpus match; preserve for CIO review |
| Website Closers | Mission-Critical SaaS for Financial Trading Firms | undisclosed | undisclosed | undisclosed | undisclosed | Vertical SaaS / trading infrastructure | High-margin recurring SaaS; blue-chip clients | BROKER-OPPORTUNISTIC | No active-niche corpus match; preserve for CIO review |
| Website Closers | AI News Intelligence & Data Platform | undisclosed | undisclosed | undisclosed | 97% | AI / data platform | Real-time API news data; recurring subscription | BROKER-OPPORTUNISTIC | No active-niche corpus match; preserve for CIO review |
| Business Exits | GovCon IT Firm - 120+ Million in Judiciary & VA-Focused Contracts | undisclosed | $19.7M | $3.45M | ~17.5% | GovCon IT / service+SaaS | not disclosed | NEAR-MISS | Outside active niche corpus |
| Website Closers | Full Service Digital Marketing Agency | undisclosed | undisclosed | undisclosed | undisclosed | Digital marketing services | not disclosed | NEAR-MISS | Agency economics are plausible but outside active niche corpus |
| Website Closers | AI-Driven Ed-Tech Platform | undisclosed | undisclosed | undisclosed | 83% | Ed-tech / training platform | recurring / retention / service-criticality | NEAR-MISS | Strong recurring revenue but not an active niche |
| Website Closers | Sales Coaching & Lead Generation Training Platform | undisclosed | undisclosed | undisclosed | undisclosed | Training / coaching platform | recurring / retention / service-criticality | NEAR-MISS | Interesting recurring education product, but not active niche |
| Website Closers | Award Winning, SBA Pre-Qualified Marketing & PR Agency | undisclosed | undisclosed | undisclosed | undisclosed | Marketing / PR services | not disclosed | NEAR-MISS | Outside active niche corpus |
| Website Closers | 67-Year Cayman Islands Architectural Design Firm | undisclosed | undisclosed | undisclosed | undisclosed | Architectural design services | not disclosed | NEAR-MISS | Foreign service firm outside active niche corpus |
| Website Closers | Procurement Services & Distribution Company | undisclosed | undisclosed | undisclosed | 36% | Commercial procurement / distribution | not disclosed | NEAR-MISS | B2B but outside active niche corpus |
| Synergy Business Brokers | Growing LED Display Solutions Company | Florida | undisclosed | undisclosed | undisclosed | LED display solutions | not disclosed | NEAR-MISS | Outside active niche corpus |
| Synergy Business Brokers Real Estate | Short-Term Rental Property Management Company: 80+ Prime Locations | Midwest | undisclosed | undisclosed | undisclosed | Property management / vacation rental ops | not disclosed | NEAR-MISS | Adjacency to property management, but not the estate-management thesis |
| SMB Deal Hunter (Helen Guo) | Deal review beta launch / example analysis of a real deal | undisclosed | undisclosed | undisclosed | undisclosed | acquisition-search tooling / deal analysis | not disclosed | FLAG | Newsletter/product announcement, not a specific deal |
| Business Exits | Midwest-Based Multi-Location Wellness Practice with Exceptional Margins | Midwest | $21.31M | $12.97M | ~61% | Healthcare / multi-location wellness | not disclosed | HARD-REJECT | Healthcare provider-owned hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25.0M | €6.15M | ~25% | Construction | not disclosed | HARD-REJECT | Construction hard-exclude; non-US |
| Business Exits | Metal Building Supplier with US Manufacturing | US | $33.69M TTM | $3.97M | ~12% | Manufacturing / construction supply | not disclosed | HARD-REJECT | Capital-intensive manufacturing hard-exclude |
| Website Closers | DTC eCommerce Jewelry Brand | undisclosed | undisclosed | undisclosed | undisclosed | DTC eCommerce | not disclosed | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Website Closers | DTC Personal Wellness eCommerce Brand | undisclosed | undisclosed | undisclosed | undisclosed | DTC eCommerce | not disclosed | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Website Closers | Subscription eCommerce Brand - Women's Intimates | undisclosed | undisclosed | undisclosed | undisclosed | Subscription eCommerce | not disclosed | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Website Closers | 25-Year eCommerce Brand - Fine Jewelry | undisclosed | undisclosed | undisclosed | undisclosed | eCommerce / fine jewelry | not disclosed | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Website Closers | Towels & Socks eCommerce Brand | undisclosed | undisclosed | undisclosed | undisclosed | eCommerce / home goods | not disclosed | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Website Closers | eCommerce Brand - Guided Fitness Journals | undisclosed | undisclosed | undisclosed | undisclosed | eCommerce / consumer products | not disclosed | HARD-REJECT | Consumer retail / DTC hard-exclude |
| Synergy Business Brokers | Commercial Construction Technology | Florida | undisclosed | undisclosed | undisclosed | Construction technology | not disclosed | HARD-REJECT | Construction hard-exclude |
| Synergy Business Brokers | Oil and Gas Specialty: Equipment Rental and Trucking Solutions | Texas | undisclosed | undisclosed | undisclosed | Equipment rental / trucking | not disclosed | HARD-REJECT | Field-service / labor-heavy operations |
| Synergy Business Brokers | Seafood Processing And Distribution Company | Europe | undisclosed | undisclosed | undisclosed | Food processing / distribution | not disclosed | HARD-REJECT | Food processing and distribution not in active thesis corpus |
| Synergy Business Brokers | Commercial Plumbing Company, Strong Client Base | New Jersey | undisclosed | undisclosed | undisclosed | Commercial plumbing | not disclosed | HARD-REJECT | Labor-heavy field services hard-exclude |
| Synergy Business Brokers Real Estate | Event Rental Company: Full-Service | Florida | undisclosed | undisclosed | undisclosed | Event rental / hospitality | not disclosed | HARD-REJECT | Hospitality / event rental is not a fit |
| Empire Flippers | Listing #92963 | undisclosed | $228,544 | $32,124 | 14% | Food & beverages / hospitality | not disclosed | HARD-REJECT | Hospitality / food category outside active theses |
| Empire Flippers | Listing #94486 | undisclosed | $48,339 | $24,635 | 51% | Supplements / eCommerce | not disclosed | HARD-REJECT | Consumer retail / eCommerce hard-exclude |
| Empire Flippers | Listing #94515 | undisclosed | $90,429 | $22,905 | 25% | Home / lifestyle eCommerce | not disclosed | HARD-REJECT | Consumer retail / eCommerce hard-exclude |
| Empire Flippers | Listing #94558 | undisclosed | $35,589 | $4,283 | 12% | Hobbies / health & fitness eCommerce | not disclosed | HARD-REJECT | Consumer retail / eCommerce hard-exclude |
| Empire Flippers | Listing #93279 | undisclosed | $10,209 | $3,321 | 33% | Hobbies / equipment / dropshipping | not disclosed | HARD-REJECT | Consumer retail / dropshipping hard-exclude |

## Source Scorecard

Every source scanned this run MUST appear as a row. Missing rows mean the scan skipped a source.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 5 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| DealForce | General | active | 200 | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 5 | 0 | — |
| Everingham & Kerr | General | active | 200 | 0 | 0 | — |
| Flippa | General | active | 200 | 0 | 0 | — |
| IAG M&A Advisors | General | active | 200 | 0 | 0 | — |
| Quiet Light | General | blocked (verified) | 403 | 0 | 0 | — |
| Rejigg | General | active | 200 | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active | 200 | 1 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 5 | 0 | — |
| Viking Mergers | General | blocked (verified) | 403 | 0 | 0 | — |
| Website Closers | General | active | 200 | 18 | 0 | 2026-06-05 |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Management) | active | 200 | 2 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 5
- 7-day rolling average: 0.0/day
- Target: 1-3/day - CRITICAL
- Email leg: live
- Funnel bottleneck: source quality

