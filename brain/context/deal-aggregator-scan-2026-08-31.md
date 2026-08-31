---
schema_version: 1.1.0
date: 2026-08-31
type: context
title: "Deal Aggregator Scan — 2026-08-31 (morning run)"
deals_found: 0
sources_scanned: 15
sources_blocked_verified: 0
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
broker_opportunistic: 2
email_scan_status: live
buy_box_source: live
tags: [date/2026-08-31, context, topic/deal-aggregator, topic/morning-scan, status/done]
---
# Deal Aggregator Scan — 2026-08-31

Today's morning run read the three buy-box docs live, rebuilt the active-niche corpus from the WEEKLY REVIEW rows with blank DealsX mappings, and loaded the 2026-08-24 niche-intel watchlist (Commercial/Industrial Air Purification Installed-Base Service and Compliance Maintenance; Art-Dealer Cultural-Goods Compliance and Back-Office Operations). No PASS matches cleared both the active thesis corpus and the buy-box gate. Two broker-opportunistic items were preserved for CIO review; all other parsed listings were logged for rejection calibration or source hygiene.

Active niche corpus path log:
- Specialty Insurance Brokerage (Art & Collectibles) -> WR row enrichment (DealsX Niche blank)
- HNW Personal Lines Concierge Insurance Brokerage -> WR row enrichment (DealsX Niche blank)
- Estate Management Companies -> WR row enrichment (DealsX Niche blank)
- Fine-Art Logistics Services -> WR row enrichment (DealsX Niche blank)
- Storage & Related Services for High-Value Assets -> WR row enrichment (DealsX Niche blank)

## Deals Surfaced (sent to Slack individually)
None today.

## Email Inbound Deals
None today. The email artifact was live, but no direct CIM / teaser / intro inbound surfaced that warranted a standalone email-deal entry.

## DealsX Proprietary Outreach Replies
None today. No `Lead Interested` notifications appeared in the email artifact.

## Broker Opportunistic Review
1. [[entities/axial|Axial]] — High-Growth AI Services Firm - GovCon & Commercial Contracts | undisclosed | $2,000,000 EBITDA | AI services / GovCon | Key signals: commercial contracts | Why it matters: financially plausible B2B services deal with no active thesis match | [[brain/context/email-scan-results-2026-08-31]]
2. [[entities/transworld-business-advisors|Transworld Business Advisors]] — 100 Year Old Flooring Distributor with over $1M/yr Cash Flow! | $6,500,000 asking price | $1,221,578 SDE | flooring / distribution | Key signals: not disclosed | Why it matters: plausible broker blast with no hard-exclude, but no active thesis match | [[brain/context/email-scan-results-2026-08-31]]

## Near Misses (not Slacked)
- [[entities/bizquest|BizQuest]] — High-Volume B2B Print, Promotional & Marketing Center - Manhattan — sparse disclosure; not enough financial detail to promote
- [[entities/quietlight|Quiet Light]] — Scalable AI-Powered SEO Automation Platform — paused SaaS source; active economics are incomplete for this run

## Listings Reviewed (full log)

Every listing scraped or parsed during this run lands here as one row, regardless of verdict. Every reviewable listing from the email artifact is logged here. SMB Deal Hunter / Helen Guo rows were excluded entirely per Kay's paywall decision on 2026-07-17.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Key Signals | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|-------------|---------|---------------|
| Axial | High-Growth AI Services Firm - GovCon & Commercial Contracts | undisclosed | undisclosed | $2,000,000 EBITDA | undisclosed | AI services / GovCon | commercial contracts | BROKER-OPPORTUNISTIC | financially plausible B2B services deal with no active thesis match |
| Transworld Business Advisors | 100 Year Old Flooring Distributor with over $1M/yr Cash Flow! | Camden County, New Jersey | $6,500,000 asking price | $1,221,578 SDE | undisclosed | flooring / distribution | not disclosed | BROKER-OPPORTUNISTIC | plausible broker blast with no hard-exclude, but no active thesis match |
| BizQuest | High-Volume B2B Print, Promotional & Marketing Center - Manhattan | New York County, NY | $500,000 asking price | undisclosed | undisclosed | print / marketing | not disclosed | NEAR-MISS | sparse disclosure; not enough financial detail to promote |
| Quiet Light | Scalable AI-Powered SEO Automation Platform | undisclosed | undisclosed | undisclosed | 68% net margins | SaaS / SEO automation | not disclosed | FLAG | paused SaaS source; active economics are incomplete for this run |
| BizBuySell | MD Hyperbaric opportunity's still available | Maryland | undisclosed | undisclosed | undisclosed | hyperbaric / health services | not disclosed | HARD-REJECT | provider-owned healthcare / hyperbaric clinic |
| BizQuest | Cake & Cookie Manufacturer/ Distributor | Montauk, NY | $5,349,995 asking price | undisclosed | undisclosed | food manufacturing / distribution | not disclosed | HARD-REJECT | food manufacturing / distribution |
| BizQuest | Established Profitable Queens Laundromat Favorable Lease Terms - No SBA | Queens, NY | $575,000 asking price | undisclosed | undisclosed | laundromat | not disclosed | HARD-REJECT | consumer retail / laundromat |
| BizQuest | Fence Construction Business - Turnkey and Profitable/SBA Pre-Approved | Westchester County, NY | $1,350,000 asking price | undisclosed | undisclosed | fence construction | not disclosed | HARD-REJECT | construction / labor-heavy field services |
| BizQuest | Multispecialty Medical Clinic doing $8.3 Million plus Annually in NY | Kings County, NY | $3,250,000 asking price | undisclosed | undisclosed | medical clinic | not disclosed | HARD-REJECT | provider-owned healthcare |
| BizQuest | Recycled Plastics Manufacturing & Product Development Opportunity | Lockport, NY | $125,000 asking price | undisclosed | undisclosed | manufacturing / plastics | not disclosed | HARD-REJECT | manufacturing |
| Calder Capital | Electronics distributor and manufacturer for sale | undisclosed | undisclosed | undisclosed | undisclosed | distribution / manufacturing | not disclosed | HARD-REJECT | manufacturing / distribution |
| Flippa | Award Winning Brand Design Agency | undisclosed | $160K annual revenue | undisclosed | 95% profit margin | brand design agency | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Decal Amazon FBA | undisclosed | $189K annual revenue | undisclosed | 64% profit margin | Amazon FBA / decals | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Established Honey Production Business | undisclosed | $110K annual revenue | undisclosed | 85% profit margin | ecommerce / honey production | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Established Smart Bottle Shopify Brand | undisclosed | $2.8M annual revenue | undisclosed | 74% profit margin | ecommerce / consumer brand | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Home & Garden Amazon FBM | undisclosed | $499K annual revenue | undisclosed | undisclosed | Amazon FBM / home goods | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Home & Kitchen Amazon FBA | undisclosed | $58K annual revenue | undisclosed | undisclosed | Amazon FBA / home goods | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Keepsakes Shopify Store | undisclosed | $2.1M annual revenue | undisclosed | undisclosed | ecommerce / Shopify | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Flippa | Multi-category Audiobook Publishing Business | undisclosed | $46K annual revenue | undisclosed | 99% profit margin | media / audiobook publishing | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Quiet Light | 6-Year-Old Track-and-Field Accessories Shopify Business | undisclosed | undisclosed | undisclosed | 36% YoY SDE growth | ecommerce / Shopify | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Quiet Light | Shopify Patent Home Decor Brand | undisclosed | undisclosed | undisclosed | 1.54x multiple | ecommerce / home decor | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Quiet Light | Unique Golf Accessory Brand | undisclosed | $72K inventory included | undisclosed | 75%+ margins | ecommerce / golf accessory | not disclosed | HARD-REJECT | consumer ecommerce / digital asset outside active theses |
| Transworld Business Advisors | Kitchen Bath Cabinetry 45+ Years | New Jersey | $1,800,000 asking price | $1,699,823 SDE | undisclosed | construction / cabinetry | not disclosed | HARD-REJECT | construction / labor-heavy cabinetry |

## Source Scorecard

Every source scanned this run appears below. Dashboard categories are limited to Marketplace, Newsletter, and Direct email.

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | Newsletter | Active - email newsletter | — | 1 | 0 | — |
| Business Exits | Marketplace | Active - scanning | 200 | 0 | 0 | — |
| DealForce | Marketplace | Active - email alerts | 200 | 0 | 0 | — |
| Empire Flippers | Marketplace | Active - scanning | 200 | 0 | 0 | — |
| Everingham & Kerr | Newsletter | Active - email-only | — | 0 | 1 | 2026-06-17 |
| IAG M&A Advisors | Direct email | Active - email alerts | — | 0 | 0 | — |
| Rejigg | Marketplace | Active - email alerts | 200 | 0 | 0 | — |
| Viking Mergers | Newsletter | Active - email-only | — | 0 | 0 | — |
| Viking Mergers | Newsletter | Active - newsletter | — | 0 | 0 | — |
| Baton Market | Marketplace | Active - email alerts | 200 | 0 | 0 | — |
| Calder Capital | Newsletter | Active - email-only | — | 1 | 0 | — |
| GP Bullhound | Direct email | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Newsletter | active | 200 | 0 | 0 | — |
| Sica Fletcher | Direct email | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Marketplace | active | 200 | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- Broker-opportunistic review items: 2
- 7-day rolling average: 0.0
- Target: 1-3/day — BELOW TARGET
- Email leg: live
- Funnel bottleneck: source quality

## Notes
- 2026-08-24 niche-intel watchlist loaded; no watchlist match cleared the active thesis corpus.
- No source blocker, no browser fallback, and no email-artifact recovery were needed today.
