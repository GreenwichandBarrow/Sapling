---
schema_version: 1.1.0
date: 2026-05-21
type: context
title: Deal Aggregator Scan — 2026-05-21
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 0
buy_box_source: live
tags:
  - date/2026-05-21
  - context
  - source/deal-aggregator
  - status/published
---

# Deal Aggregator Scan — 2026-05-21

Morning headless run (Thu). Buy-boxes loaded live from Drive (Services / Insurance / SaaS). Active niches loaded from Industry Research Tracker `WEEKLY REVIEW`. DealsX corpus loaded from `DEALSX` tab. Sources resolved against `G&B Deal Aggregator - Sourcing List` (General + Niche-Specific).

Corpus paths logged per active niche:
- Premium Pest Management → DealsX keywords ("Specialty Pest & Environmental Management Services")
- Private art advisory firms → WR row enrichment (Niche Hypothesis + Quick notes — DealsX reference blank)
- Estate Management Companies → DealsX keywords ("Estate Management Companies")
- Specialty Coffee Equipment Service → DealsX keywords ("Specialty Commercial Equipment Services")
- High-End Commercial Cleaning → DealsX keywords ("High-End Commercial Cleaning")
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords ("Specialty Insurance Brokerage")
- Storage & Related Services for High Value Assets → DealsX keywords ("Specialty Storage & Handling for High-Value Collections")

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box + niche-corpus gate across the 17 active sources scanned.

## Email Inbound Deals

None today. Email-intelligence's 7am run (`brain/context/email-scan-results-2026-05-21.md`) extracted ONE broker BLAST listing — Quiet Light's US-Made Outdoor Brand (Nalgene metal-ring tether) — which fails the Services buy-box (Rev $120,920 + SDE $26,411, both well below floors; outdoor DTC also hits the consumer-retail/DTC hard-exclude). Logged in Listings Reviewed below. No CIMs, no broker-blast multi-listing extractions (Flippa marketing email did not match the strict broker-signal keyword set per `feedback_marketplace_vs_broker_distinction`).

## DealsX Proprietary Outreach Replies

None today. No `Prospect Geni <dealsx.notifaction@gmail.com>` notifications in the 2-day inbound window per email-scan-results.

## Near Misses (not Slacked)

Listings that cleared buy-box financial gates but landed outside the active-niche corpus — tracked for thesis-drift signal:

- **GovCon IT Firm** (Business Exits) — $19.7M rev / $3.45M income / ~17.5% margin / GovCon ERP-services + SaaS. Clears Services financials but GovCon is not an active niche. Adjacent to Vertical-SaaS-Luxury thesis only if reframed as luxury-asset SaaS — it isn't.
- **B2B Experiential Marketing Vendor** (Business Exits) — $14.28M / $3.30M / B2B marketing services. Clears Services financials; outside niche corpus.
- **Government Contract ERP Service** (Business Exits) — $14.05M / $2.57M / Service+SaaS. Clears Services financials; outside niche corpus.
- **LED Display Solutions Co FL** (Synergy BB) — $11.19M / $4.63M / ~41% margin / tech+distribution. Clears Services financials; outside niche corpus.
- **Shopify Business Brokerage** (Website Closers) — $2.4M CF / ecommerce M&A services. Industry-niche fit weak; outside active corpus.
- **Short-Term Rental Property Mgmt Co (Midwest)** (Synergy BB Real Estate) — $3.23M rev / $370K CF. Closest adjacency to Estate Management niche but is vacation-rental ops, not high-touch household/property estate management; revenue also below $10M Services floor.

No bridges to thesis-discovery surfaced this run.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm | undisclosed | $19.7M | $3.45M (income) | ~17% | GovCon IT / Service+SaaS | NEAR-MISS | Outside active-niche corpus |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.28M TTM | $3.30M (income) | ~23% | B2B marketing services | NEAR-MISS | Outside active-niche corpus |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14.05M | $2.57M (income) | ~18% | GovCon ERP service+SaaS | NEAR-MISS | Outside active-niche corpus |
| Synergy BB | LED Display Solutions Company | Florida | $11.19M | $4.63M (CF) | ~41% | Tech / distribution | NEAR-MISS | Outside active-niche corpus |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2.40M (CF) | undisclosed | Ecommerce M&A services | NEAR-MISS | Outside active-niche corpus |
| Synergy BB Real Estate | Short-Term Rental Property Mgmt (80+ Prime Locations) | Midwest | $3.23M | $370K (CF) | ~11% | Vacation-rental ops | NEAR-MISS | Rev below Services $10M floor; vacation-rental ops not Estate Mgmt fit |
| Business Exits | Midwest Multi-Location Wellness Practice | Midwest | $21.3M | $12.97M | ~61% | Healthcare / multi-loc wellness | HARD-REJECT | Healthcare provider-owned hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | ~25% | Construction | HARD-REJECT | Non-US + construction hard-exclude |
| Business Exits | California Property Tax Consultants | California | $6.68M | $4.68M | ~70% | Property tax consulting | HARD-REJECT | Rev below $10M Services floor; CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | ~74% | Hospitality / events | HARD-REJECT | Hospitality/nightlife hard-exclude; rev below floor |
| Business Exits | Metal Building Supplier US Manufacturing | US | $33.7M TTM | $3.97M | ~12% | Construction supply + manufacturing | HARD-REJECT | Capital-intensive manufacturing + construction hard-exclude |
| Business Exits | Texas Non-Emergency Medical Transport | Texas | $7.74M | $2.87M | ~37% | Healthcare transport | HARD-REJECT | Healthcare adjacency + rev below floor |
| Business Exits | California Staffing Firm | California | $7.82M | $3.20M | ~41% | Staffing / recurring | HARD-REJECT | Rev below floor + CA soft-flag |
| Business Exits | Northeast Commercial Contractor | Northeast | $21.96M | $2.78M | ~13% | Commercial construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Atlanta Residential Plumbing & Septic | Georgia | $11.71M | $2.41M | ~21% | Residential plumbing/field services | HARD-REJECT | Labor-heavy field-services hard-exclude |
| Business Exits | Design & Build Studio | undisclosed | $10.02M | $3.06M | ~31% | Construction + manufacturing | HARD-REJECT | Construction + manufacturing hard-excludes |
| Business Exits | Texas HVAC Company | Texas | $21.99M | $2.28M | ~10% | HVAC / field services | HARD-REJECT | Labor-heavy field-services hard-exclude |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | ~22% | Tower install/repair / field | HARD-REJECT | Field-services hard-exclude + rev below floor |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.30M | ~21% | Construction services | HARD-REJECT | Construction hard-exclude |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8.23M | $1.90M | ~23% | Aerospace parts distribution | HARD-REJECT | Aviation/aerospace hard-exclude (memory `feedback_no_aviation_targets`) + rev below floor |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.90M | $1.54M | ~31% | Window manufacturing | HARD-REJECT | Capital-intensive manufacturing + rev below floor |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | ~36% | Electrical contracting | HARD-REJECT | Construction hard-exclude + rev below floor |
| Business Exits | Arizona Addiction Treatment Center | Arizona | $4.45M TTM | $1.10M | ~25% | Healthcare / treatment | HARD-REJECT | Healthcare hard-exclude + EBITDA below $1.5M |
| Business Exits | Pet Safety Travel Products Distribution | undisclosed | $1.67M | $1.03M | ~62% | Pet products DTC/wholesale | HARD-REJECT | Consumer/DTC hard-exclude + rev below floor |
| Business Exits | Nevada Commercial Fireproofing Contractor | Nevada | $3.06M | $0.93M | ~30% | Fireproofing construction | HARD-REJECT | Construction hard-exclude + EBITDA below floor |
| Business Exits | Government Contracted Military Promotional Products | USA | $8.18M | $0.79M | ~10% | Retail/promotional products | HARD-REJECT | Retail/DTC adjacency + EBITDA below floor |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2.28M CAD | $0.76M CAD | ~33% | Recruitment services | HARD-REJECT | Non-US + financial floors |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | Florida | $1.07M | $0.72M | ~67% | Healthcare med spa | HARD-REJECT | Healthcare/provider-owned hard-exclude + financial floors |
| Business Exits | Landscape Architecture Business | undisclosed | $5.5M | $1.80M | ~33% | Landscape architecture / construction | HARD-REJECT | Construction/labor hard-exclude + rev below floor |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.14M TTM | $0.71M | ~17% | Restaurant franchise | HARD-REJECT | Restaurants/hospitality + franchise hard-excludes |
| Business Exits | Colorado Regenerative & Functional Medicine Practice | Colorado | $0.89M | $0.49M | ~55% | Healthcare physician practice | HARD-REJECT | Healthcare hard-exclude + financial floors |
| Business Exits | Bay Area Residential Roofing Company | California | $2.5M | $0.47M | ~19% | Residential roofing | HARD-REJECT | Construction/labor + CA flag + financial floors |
| Business Exits | Texas Home Health Staffing Firm | Texas | $2.49M | $0.34M | ~14% | Home health staffing | HARD-REJECT | Healthcare adjacency + financial floors |
| Empire Flippers | Medical, News & Education Academy | undisclosed | undisclosed | $14,430/mo | n/a | Online education content | HARD-REJECT | B2C content + sub-buybox |
| Empire Flippers | Healthcare Language Learning App | undisclosed | undisclosed | $9,068/mo | n/a | B2C app | HARD-REJECT | B2C/prosumer + sub-buybox |
| Empire Flippers | Amazon Seller SaaS Platform | undisclosed | undisclosed | $8,593/mo | n/a | SaaS for Amazon sellers (horizontal) | HARD-REJECT | Horizontal SaaS + ARR below $3M SaaS floor |
| Empire Flippers | Music Nostalgia YouTube Channel | undisclosed | undisclosed | $4,300/mo | n/a | Content/media | HARD-REJECT | Content/ad-rev model — wrong shape |
| Empire Flippers | Soccer YouTube Business | undisclosed | undisclosed | $1,993/mo | n/a | Content/media | HARD-REJECT | Content/ad-rev model + sub-buybox |
| Empire Flippers | Consumer Health eCommerce Brand | undisclosed | undisclosed | $383,476/mo | n/a | Consumer health DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Pet Wellness eCommerce | undisclosed | undisclosed | $342,383/mo | n/a | Pet DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Crypto News Platform | undisclosed | undisclosed | $433,353/mo | n/a | Crypto media | HARD-REJECT | Content/media — wrong shape |
| Empire Flippers | Amazon FBA Pest Control | undisclosed | undisclosed | $159,358/mo | n/a | Amazon FBA consumer pest | HARD-REJECT | Consumer DTC FBA — does NOT match commercial Premium Pest niche |
| Empire Flippers | Beauty/Personal Care FBA | undisclosed | undisclosed | $127,207/mo | n/a | Beauty FBA | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Supplement Brand | undisclosed | undisclosed | $115,766/mo | n/a | Supplements DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Shopify Store Service Business | undisclosed | undisclosed | $142,126/mo | n/a | Shopify services | HARD-REJECT | Outside niche corpus + sub-buybox |
| Empire Flippers | Home/Romance eCommerce | undisclosed | undisclosed | $122,253/mo | n/a | DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Hobbies/Gaming FBA | undisclosed | undisclosed | $110,226/mo | n/a | DTC FBA | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Bed & Bath FBA | undisclosed | undisclosed | $106,428/mo | n/a | DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Synergy BB | Commercial Construction Technology | Florida | $9.06M | $3.28M | ~36% | Commercial construction tech | HARD-REJECT | Construction hard-exclude + rev below floor |
| Synergy BB | Oil and Gas Specialty Equipment Rental & Trucking | Texas | $15.29M | $6.56M | ~43% | Oil & gas equipment | HARD-REJECT | Capital-intensive industrial + outside niche corpus |
| Synergy BB | Seafood Processing And Distribution | Portugal | $165M | $5.90M | ~4% | Food processing | HARD-REJECT | Non-US + rev/margin profile |
| Synergy BB | Commercial Plumbing Company | New Jersey | $13.58M | $4.03M | ~30% | Commercial plumbing | HARD-REJECT | Construction/labor hard-exclude |
| Synergy BB | Women's Health Practice (Multi-Physician OB/GYN) | Central Florida | $6.58M | $3.38M | ~51% | Healthcare physician practice | HARD-REJECT | Healthcare hard-exclude + rev below floor |
| Synergy BB | Precision Machine Shop | Arizona | $7.5M | $2.30M | ~31% | Machine manufacturing | HARD-REJECT | Capital-intensive manufacturing + rev below floor |
| Synergy BB | Telecom Caller Trust SaaS Platform | US | $2.71M | $1.61M | ~59% | Telecom horizontal SaaS | HARD-REJECT | ARR below $3M SaaS floor + horizontal not vertical-luxury |
| Synergy BB | Ethanol Producer | India | $10.5M | $3.00M | ~29% | Manufacturing | HARD-REJECT | Non-US + manufacturing hard-exclude |
| Synergy BB | Industrial Minerals Producer | Peru | $7M | $4.50M | ~64% | Mining/distribution | HARD-REJECT | Non-US + mining/manufacturing |
| Synergy BB | Renovation Design Build Co | NYC, New York | $8.5M | $2.34M | ~28% | NYC construction renovation | HARD-REJECT | NYC-construction hard-exclude (`feedback_nyc_construction_hard_exclude`) |
| Synergy BB | Garment Manufacturing Facility | Bangladesh | $12.5M | $1.95M | ~16% | Garment manufacturing | HARD-REJECT | Non-US + manufacturing |
| Synergy BB | Railroad Construction Business | Missouri | $7.83M | $1.50M | ~19% | Construction | HARD-REJECT | Construction hard-exclude |
| Synergy BB | B2B Health and Beauty Ingredient Mfr | Dubai | $3.09M | $2.25M | ~73% | Manufacturing/distribution | HARD-REJECT | Non-US + B2B beauty wrong-segment |
| Synergy BB | Manufacturer of Specialty Copper Alloy Wires | India | $20M | $2.00M | ~10% | Manufacturing | HARD-REJECT | Non-US + manufacturing |
| Synergy BB | Travel and Tourism Leader | Saudi Arabia | $7.94M | $2.95M | ~37% | Travel/tourism | HARD-REJECT | Non-US + hospitality |
| Synergy BB | Admissions Consulting Practice (Global, Remote) | US (remote) | $2M | $1.30M | ~65% | Consulting | HARD-REJECT | Rev below $10M Services floor |
| Synergy BB | Prominent 40-Year Pediatric Practice | New York | $5.83M | $1.65M | ~28% | Healthcare physician practice | HARD-REJECT | Healthcare hard-exclude + rev below floor |
| Synergy BB | Utility Support Construction Co | Nassau County, NY | $12M | $2.00M | ~17% | Utility construction | HARD-REJECT | Construction/field services hard-exclude |
| Synergy BB | Growing Midwestern Trucking & Transport Brokerage | Midwest | $9M | $1.65M | ~18% | Transportation brokerage | HARD-REJECT | Rev below $10M Services floor |
| Synergy BB Real Estate | Event Rental Company: Full-Service | South Florida | $1.63M | $486K | ~30% | Event rental | HARD-REJECT | Hospitality/events + rev below floor |
| Synergy BB Real Estate | Groundwater Treatment Equipment Rental | Jacksonville, FL | $3.5M | $1.30M | ~37% | Equipment rental services | HARD-REJECT | Status: Sold; rev below floor |
| Synergy BB Real Estate | Property Management Company (with Real Estate) | Vermont | $1.56M | $299K | ~19% | Residential property mgmt | HARD-REJECT | Status: Sold; rev below floor |
| Synergy BB Real Estate | Real Estate Investment Company | Harrisburg, PA | $2.37M | $395K | ~17% | RE investment | HARD-REJECT | Status: Sold; rev below floor |
| Synergy BB Real Estate | Property Management Firm | NYC, New York | $600K | $300K | ~50% | Residential property mgmt | HARD-REJECT | Status: Sold; sub-scale |
| Synergy BB Real Estate | Real Estate Property Management Office | Ulster County, NY | $888K | undisclosed | undisclosed | Residential property mgmt | HARD-REJECT | Status: Sold; sub-scale |
| Website Closers | Software Platform for SaaS Infrastructure (Prop Trading) | undisclosed | undisclosed | $3.35M (CF) | undisclosed | SaaS infra for prop-trading | HARD-REJECT | Trading/credit-adjacent fintech + outside vertical-luxury corpus |
| Website Closers | Amazon FBA eCommerce Brand | undisclosed | undisclosed | $955K (CF) | undisclosed | Amazon DTC | HARD-REJECT | Consumer DTC hard-exclude + sub-buybox |
| Website Closers | Ed-Tech eLearning Platform | undisclosed | undisclosed | $1.63M (CF) | undisclosed | EdTech B2C/prosumer | HARD-REJECT | B2C/prosumer hard-exclude (SaaS box) |
| Website Closers | AI-Driven SEO & Content Marketing Agency | undisclosed | undisclosed | $120K (CF) | undisclosed | Marketing agency | HARD-REJECT | EBITDA below $1.5M floor |
| Website Closers | Authenticated Collectibles eCommerce | undisclosed | undisclosed | $259K (CF) | undisclosed | Collectibles DTC | HARD-REJECT | Consumer DTC + EBITDA below floor |
| Website Closers | Loss Prevention Training Platform | undisclosed | undisclosed | $792K (CF) | undisclosed | Retail training SaaS | HARD-REJECT | EBITDA below $1.5M floor + non-luxury vertical |
| Website Closers | Lead Generation & Performance Marketing Agency | undisclosed | undisclosed | $846K (CF) | undisclosed | Marketing agency | HARD-REJECT | EBITDA below $1.5M floor |
| Website Closers | Digital Feedback Platform SaaS | undisclosed | undisclosed | $210K (CF) | undisclosed | Customer-feedback SaaS | HARD-REJECT | EBITDA below floor + horizontal SaaS |
| Website Closers | Luxury RV & Coach Marketplace | undisclosed | undisclosed | $593K (CF) | undisclosed | Marketplace/RV | HARD-REJECT | Marketplace + EBITDA below floor |
| Website Closers | Architectural Design Firm | Cayman Islands | undisclosed | $386K (CF) | undisclosed | Architecture | HARD-REJECT | Non-US + EBITDA below floor |
| Website Closers | Towels & Socks eCommerce Brand | undisclosed | undisclosed | $525K (CF) | undisclosed | Home textiles DTC | HARD-REJECT | Consumer DTC + EBITDA below floor |
| Quiet Light (email blast) | US-Made Outdoor Brand (Nalgene metal-ring bottle tether) | undisclosed (US-based, REI Cambridge/Boston/Concord placements) | $120,920 (TTM) | $26,411 (SDE) | ~22% | Outdoor DTC ecom | HARD-REJECT | Consumer DTC hard-exclude + rev/SDE far below floors |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| BizBuySell | General | blocked (verified) | n/a | 0 | — | — |
| DealForce | General | active | n/a | 0 | — | — |
| Empire Flippers | General | active | 200 | 15 | 0 | — |
| Everingham & Kerr | General | active | n/a | 0 | — | — |
| Flippa | General | active | n/a | 0 | — | — |
| IAG M&A Advisors | General | active | n/a | 0 | — | — |
| Quiet Light | General | active | n/a | 1 | 0 | — |
| Rejigg | General | active | n/a | 0 | — | — |
| SMB Deal Hunter (Helen Guo) | General | active | n/a | 0 | — | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Viking Mergers | General | active | n/a | 0 | — | — |
| Website Closers | General | active | 200 | 12 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | 200 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 0 | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 7 | 0 | — |

**Notes on scorecard rows:**
- `BizBuySell` → `blocked (verified)`: BROWSER_AUTOMATION_UNAVAILABLE — source requires agent-browser (Cloudflare/JS-shell route per SKILL.md) and that tool is not installed on this host. Surface remains gated until agent-browser is provisioned.
- Email-only sources (`DealForce`, `Everingham & Kerr`, `Flippa`, `IAG`, `Quiet Light`, `Rejigg`, `SMB Deal Hunter`, `Viking Mergers`) report `active` but route via `email-intelligence` → `email-scan-results-2026-05-21.md`. Today's email-scan extracted 1 broker-blast listing (Quiet Light, Nalgene tether) — captured in the Listings Reviewed log. No other broker-blast or CIM emails in the 2-day inbound window.
- `GP Bullhound`, `PCO Bookkeepers`, `Sica Fletcher` → tombstone / news / advisory pages, no live for-sale listings on public surfaces. Status `active` but Listings Reviewed = 0 by definition (completed-transaction tombstones, not actionable sell-side mandates).

## Volume Check

- Deals surfaced today: **0**
- 7-day rolling average: **~0.14/day** (1 deal across 7 days: 5/14 0, 5/15 0, 5/16 weekend, 5/17 weekend, 5/18 1, 5/19 0, 5/20 0)
- Target: 1-3/day → **BELOW TARGET**

Pattern remains consistent with the prior 7-day window — public broker platforms continue to skew construction/healthcare/DTC-ecom which are pre-screened out by Services / SaaS hard-excludes; niche-specific deal flow continues to depend on email/intermediary channels (DealsX, Sica Fletcher relationship, August Felker / Hunter warm intros for insurance, Acumen-style estate-storage relationships) rather than scrapable surfaces. Friday digest (5/22) will surface source-stewardship proposals if any 30-day-no-match retirement candidates have accumulated.
