---
date: 2026-05-13
deals_found: 0
sources_scanned: 20
sources_blocked_verified: 3
sources_blocked_single_attempt: 8
email_deals: 0
---
# Deal Aggregator Scan — 2026-05-13

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. `brain/context/email-scan-results-2026-05-13.md` artifact missing at scan time — email-intelligence run not yet completed or failed. See Near Misses for gap note.

## Near Misses (not Slacked)

- **Email-scan-results artifact missing for 2026-05-13** — email-driven channels (Everingham & Kerr, Flippa email, Quiet Light email, Viking Mergers, IAG M&A Advisors, SMB Deal Hunter) could not be processed this run. Surface to email-intelligence pipeline-manager check; afternoon top-up will re-attempt.
- **Business Exits — CA Property Tax Consultants** ($6.7M rev / $4.68M EBITDA / 70% margin / CA): revenue below $10M services floor; CA soft-flag. Watch list for Property Tax Appeal Services niche (currently New - Pending Review).
- **Business Exits — GovCon IT Firm (Judiciary & VA Contracts)** ($19.7M rev / $3.45M EBITDA / 17% margin): clears Services buy-box gate but no active-niche corpus match. Buy-box-new-niche signal — not luxury/HVA thesis.
- **Business Exits — B2B Experiential Marketing Vendor** ($14.3M rev / $3.3M EBITDA / 23% margin): clears buy-box gate; no luxury/HVA niche match.
- **Business Exits — CA Staffing Firm** ($7.8M rev / $3.2M EBITDA / 41% margin / CA): below floor; CA soft-flag.
- **Business Exits — Government Contract ERP Service** ($14M rev / $2.57M EBITDA / 18% margin): clears buy-box gate; no luxury/HVA niche match.
- **Business Exits — Landscape Architecture** ($5.5M rev / $1.8M EBITDA / 33%): below floor; design-services subdomain straddles construction exclude.
- **Synergy — LED Display Solutions (FL)** ($11.2M rev / $4.63M EBITDA / 41% margin): clears buy-box; no luxury/HVA niche match.
- **Synergy — Telecom Caller Trust SaaS** ($2.71M ARR / $1.61M EBITDA / 59% / 120% NRR): ARR $290K below $3M SaaS floor but otherwise strong; telecom not luxury/HVA thesis. Worth corpus-tuning calibration on vertical-SaaS niche definition.
- **Synergy — Admissions Consulting Practice** ($2M rev / $1.3M EBITDA / 65% margin): below $10M services floor.
- **Synergy Real Estate — Midwest STR Property Mgmt** ($3.23M rev / $371K EBITDA / 11% margin): below floor; STR adjacent to Estate Management thesis but not high-value-asset focus.
- **Synergy Real Estate — Boutique Property Mgmt (VT)** ($1.56M rev / $299K EBITDA / 19% margin): below floor; loosely Estate Mgmt-adjacent but not HVA-focused.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | California Property Tax Consultants | California | $6.68M | $4.68M | 70% | Tax consulting | NEAR-MISS | Revenue $6.7M below $10M services floor; CA soft-flag |
| Business Exits | GovCon IT Firm – Judiciary & VA Contracts | undisclosed | $19.7M | $3.45M | 17% | Government IT services | NEAR-MISS | Buy-box gate cleared; no active-niche match (luxury thesis miss) |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.3M | $3.3M | 23% | Marketing services | NEAR-MISS | Buy-box cleared; no luxury/HVA niche match |
| Business Exits | California Staffing Firm with Recurring Revenue | California | $7.82M | $3.2M | 41% | Staffing | NEAR-MISS | Revenue below floor; CA soft-flag |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14M | $2.57M | 18% | ERP services | NEAR-MISS | Buy-box cleared; no luxury/HVA niche match |
| Business Exits | Landscape Architecture Business (SBA Eligible) | undisclosed | $5.5M | $1.8M | 33% | Landscape architecture | NEAR-MISS | Revenue below floor; may straddle construction exclude |
| Synergy Business Brokers | Growing LED Display Solutions (FL) | Florida | $11.2M | $4.63M | 41% | LED tech distribution | NEAR-MISS | Buy-box cleared; no active-niche match |
| Synergy Business Brokers | Telecom Caller Trust SaaS | United States | $2.71M ARR | $1.61M | 59% | Vertical SaaS (telecom) | NEAR-MISS | ARR below $3M SaaS floor; telecom not luxury/HVA thesis |
| Synergy Business Brokers | Admissions Consulting Practice (Remote) | United States | $2M | $1.3M | 65% | Consulting | NEAR-MISS | Revenue below $10M services floor |
| Synergy Real Estate | Short-Term Rental Property Mgmt (Midwest) | Midwest | $3.23M | $371K | 11% | Property management/STR | NEAR-MISS | Revenue below floor; STR not HVA-focused |
| Synergy Real Estate | Boutique Property Mgmt w/ Real Estate (VT) | Vermont | $1.56M | $299K | 19% | Property management | NEAR-MISS | Below floor; loosely Estate Mgmt-adjacent |
| Business Exits | Design & Build Studio for Themed Props/Interactive | undisclosed | $10M | $3.06M | 31% | Custom fabrication/design | FLAG | Design/build straddles construction hard-exclude; clarification needed |
| Website Closers | Loss Prevention Training Platform | undisclosed | undisclosed | $793K | undisclosed | B2B SaaS/training | FLAG | Revenue undisclosed; EBITDA below SaaS floor; ARR/GRR undisclosed |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2.4M | undisclosed | M&A brokerage | FLAG | Revenue undisclosed; brokerage model adjacent to lending exclude |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest US | $21.3M | $13.0M | 61% | Healthcare/wellness multi-location | HARD-REJECT | Physician/medical practice — services hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | 25% | Construction | HARD-REJECT | Construction hard-exclude + non-US |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | 74% | Hospitality/event venue | HARD-REJECT | Hospitality hard-exclude |
| Business Exits | Metal Building Supplier with US Manufacturing | US | $33.7M | $3.97M | 12% | Manufacturing/construction | HARD-REJECT | Capital-intensive manufacturing + construction hard-excludes |
| Business Exits | Texas Non-Emergency Medical Transport | Texas | $7.74M | $2.87M | 37% | Medical transport | HARD-REJECT | Revenue below floor + labor-heavy field service |
| Business Exits | Northeast Commercial Contractor (Healthcare/Financial) | Northeast | $21.96M | $2.78M | 13% | Commercial construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Atlanta Residential Plumbing & Septic | Georgia | $11.7M | $2.4M | 21% | Plumbing | HARD-REJECT | Labor-heavy field service + residential consumer |
| Business Exits | Texas HVAC – Residential New Construction | Texas | $22M | $2.28M | 10% | HVAC residential | HARD-REJECT | Construction + residential consumer hard-excludes |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | 22% | Telecom field services | HARD-REJECT | Labor-heavy field services + revenue below floor |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.3M | 21% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Specialized Military/Aerospace Parts Distributor | undisclosed | $8.23M | $1.9M | 23% | Aerospace distribution | HARD-REJECT | Revenue below floor + aerospace |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.9M | $1.54M | 31% | Manufacturing | HARD-REJECT | Capital-intensive manufacturing + revenue below floor |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | 36% | Construction/electrical | HARD-REJECT | Construction + below floor |
| Business Exits | Arizona Addiction Treatment Center | Arizona | $4.45M | $1.1M | 25% | Healthcare/treatment | HARD-REJECT | Physician practice + below floor |
| Business Exits | Safe Pet Travel Products Distribution | undisclosed | $1.67M | $1.03M | 62% | Pet products distribution | HARD-REJECT | Consumer DTC + below floor |
| Business Exits | Nevada Commercial Fireproofing Contractor | Nevada | $3.06M | $932K | 30% | Construction/fireproofing | HARD-REJECT | Construction hard-exclude + below floor |
| Business Exits | Government Contracted Military Promotional Products | USA Remote | $8.18M | $788K | 10% | Promotional products | HARD-REJECT | Retail product + revenue/EBITDA below floor |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2.28M CAD | $764K CAD | 33% | Staffing/recruitment | HARD-REJECT | Non-US + revenue below floor |
| Business Exits | Florida Med Spa & Regenerative Medicine Clinic | Florida | $1.07M | $683K | 64% | Med spa | HARD-REJECT | Physician practice + below floor |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.14M | $714K | 17% | Restaurant franchise | HARD-REJECT | Franchise + restaurant hard-excludes |
| Business Exits | Colorado Regenerative & Functional Medicine Practice | Colorado | $895K | $494K | 55% | Medicine practice | HARD-REJECT | Physician practice + below floor |
| Business Exits | Bay Area Residential Roofing Company | California | $2.5M | $470K | 19% | Construction/roofing | HARD-REJECT | Construction + residential + below floor |
| Business Exits | Texas Home Health Staffing Firm | Texas | $2.49M | $337K | 14% | Home health staffing | HARD-REJECT | Labor-heavy + below floor |
| Empire Flippers | Pet Care eCommerce #94115 | undisclosed | $19.4M ann | $4.1M ann | 21% | Pet care eCommerce | HARD-REJECT | Consumer eCommerce/DTC hard-exclude |
| Empire Flippers | Health & Fitness eCommerce #94170 | undisclosed | $17.6M ann | $4.6M ann | 26% | eCommerce | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Culinary/Pet eCommerce #92985 | undisclosed | $24.5M ann | $2.6M ann | 11% | eCommerce | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Beauty/Health eCommerce #94312 | undisclosed | $6.3M ann | $1.5M ann | 24% | Amazon FBA beauty | HARD-REJECT | Consumer DTC + revenue below floor |
| Synergy Business Brokers | Seafood Processing & Distribution (Portugal) | Portugal | $165M | $5.9M | 4% | Food processing | HARD-REJECT | Non-US + capital-intensive manufacturing + margin below floor |
| Synergy Business Brokers | Oil & Gas Equipment Rental & Trucking (TX) | Texas | $15.3M | $6.56M | 43% | Oil & gas services | HARD-REJECT | Capital-intensive + construction-adjacent |
| Synergy Business Brokers | Commercial Plumbing Company (NJ) | New Jersey | $13.6M | $4.03M | 30% | Plumbing/construction | HARD-REJECT | Construction/labor-heavy hard-exclude |
| Synergy Business Brokers | Women's Health OB/GYN Practice (FL) | Florida | $6.58M | $3.38M | 51% | Physician practice | HARD-REJECT | Physician practice hard-exclude |
| Synergy Business Brokers | Precision Machine Shop (AZ) | Arizona | $7.5M | $2.3M | 31% | Manufacturing | HARD-REJECT | Capital-intensive manufacturing + below floor |
| Synergy Business Brokers | Ethanol Producer (India) | India | $10.5M | $3M | 29% | Manufacturing/energy | HARD-REJECT | Non-US + capital-intensive |
| Synergy Business Brokers | Industrial Minerals Producer (Peru) | Peru | $7M | $4.5M | 64% | Mining/distribution | HARD-REJECT | Non-US + capital-intensive |
| Synergy Business Brokers | NYC High-End Renovation Design/Build | New York | $8.5M | $2.34M | 28% | Construction/renovation | HARD-REJECT | Construction hard-exclude |
| Synergy Business Brokers | Garment Manufacturing (Bangladesh) | Bangladesh | $12.5M | $1.95M | 16% | Manufacturing | HARD-REJECT | Non-US + capital-intensive manufacturing |
| Synergy Business Brokers | Railroad Construction Business (MO) | Missouri | $7.83M | $1.5M | 19% | Construction | HARD-REJECT | Construction hard-exclude |
| Synergy Business Brokers | B2B Health/Beauty Ingredient Mfr (Dubai) | Dubai | $3.09M | $2.25M | 73% | Distribution/manufacturing | HARD-REJECT | Non-US + below floor |
| Synergy Business Brokers | Copper Alloy Wire Manufacturer (India) | India | $20M | $2M | 10% | Manufacturing | HARD-REJECT | Non-US + capital-intensive |
| Synergy Business Brokers | Travel & Tourism Leader (Saudi Arabia) | Saudi Arabia | $7.94M | $2.95M | 37% | Travel/tourism | HARD-REJECT | Hospitality + non-US |
| Synergy Business Brokers | Tech-Enabled Behavioral Health Firm (DC) | Washington, DC | $5M | $1M | 20% | Behavioral health/tech | HARD-REJECT | Physician/medical practice + below floor |
| Synergy Business Brokers | Pediatric Practice (NY) | New York | $5.83M | $1.65M | 28% | Physician practice | HARD-REJECT | Physician practice |
| Synergy Business Brokers | Utility Support Construction (NY) | New York | $12M | $2M | 17% | Construction | HARD-REJECT | Construction hard-exclude |
| Synergy Business Brokers | Midwest Trucking & Transport Brokerage | Midwest | $9M | $1.65M | 18% | Trucking | HARD-REJECT | Labor-heavy + below floor |
| Website Closers | Authenticated Collectibles eCommerce | undisclosed | undisclosed | $259K | undisclosed | Collectibles eCommerce | HARD-REJECT | Consumer DTC + below floor |
| Website Closers | Lead Generation & Performance Marketing Agency | undisclosed | undisclosed | $847K | undisclosed | Marketing agency | HARD-REJECT | Lead-gen analog + below floor |
| Website Closers | SaaS Comment Card & Customer Feedback Platform | undisclosed | undisclosed | $211K | undisclosed | Horizontal SaaS | HARD-REJECT | Horizontal SaaS hard-exclude + below SaaS floor |
| Website Closers | Luxury RV & Coach Marketplace | undisclosed | undisclosed | $594K | undisclosed | B2B Marketplace (RV) | HARD-REJECT | Below floor + consumer/prosumer leaning |
| Website Closers | Cayman Architectural Design Firm (67yr) | Cayman Islands | undisclosed | $387K | undisclosed | Architecture | HARD-REJECT | Non-US + below floor |
| Website Closers | Towels & Socks eCommerce Brand | undisclosed | undisclosed | $526K | undisclosed | Consumer eCommerce | HARD-REJECT | Consumer DTC hard-exclude |
| Website Closers | Procurement Services & Distribution | undisclosed | undisclosed | $200K | undisclosed | Procurement | HARD-REJECT | EBITDA far below floor |
| Website Closers | Collectible Merchandise Brand | undisclosed | undisclosed | $724K | undisclosed | Consumer eCommerce | HARD-REJECT | Consumer DTC + below floor |
| Website Closers | Proprietary Home Products eCommerce | undisclosed | undisclosed | $5.8M | undisclosed | Consumer eCommerce | HARD-REJECT | Consumer DTC hard-exclude |
| Website Closers | Guided Fitness Journals eCommerce | undisclosed | undisclosed | $304K | undisclosed | Publishing/eCommerce | HARD-REJECT | Consumer DTC + below floor |
| Sica Fletcher | Safe Harbour Insurance Management — sold to ALKEME | Massachusetts | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to ALKEME (consolidator) — closed deal |
| Sica Fletcher | O'Neill Associates — sold to ALKEME | Florida | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to consolidator |
| Sica Fletcher | Surety Bonds LLC — sold to Hilb Group | Georgia | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to consolidator |
| Sica Fletcher | Quantum Resource Group — sold to ALKEME | Maryland | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to consolidator |
| Sica Fletcher | Centennial State Insurance — sold to ALKEME | Colorado | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to consolidator |
| Sica Fletcher | C&A Insurance Agency — sold to World Insurance | New York | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to consolidator |
| Sica Fletcher | Bellwether Insurance Group — sold to ALKEME | Florida | undisclosed | undisclosed | undisclosed | Insurance brokerage | HARD-REJECT | Already sold to consolidator |
| GP Bullhound | Sdui — Bain Capital fundraise | Europe | undisclosed | undisclosed | undisclosed | EdTech SaaS | HARD-REJECT | Fundraise (not sale) + non-US + PE-backed |
| GP Bullhound | Peak — acquired by UiPath | UK/US | undisclosed | undisclosed | undisclosed | AI/SaaS | HARD-REJECT | Already acquired (closed deal) |
| GP Bullhound | Flo Health — General Atlantic investment | US | undisclosed | undisclosed | undisclosed | Consumer health tech | HARD-REJECT | Consumer/B2C + PE-invested |
| GP Bullhound | Runna — acquired by Strava | UK/US | undisclosed | undisclosed | undisclosed | Consumer fitness app | HARD-REJECT | Closed deal + B2C |
| GP Bullhound | Instaleap — sale to Instacart | Global | undisclosed | undisclosed | undisclosed | Grocery SaaS | HARD-REJECT | Closed deal |
| GP Bullhound | AB Tasty / VWO — Everstone Capital merger | Europe | undisclosed | undisclosed | undisclosed | Horizontal SaaS (CRO) | HARD-REJECT | PE-backed + horizontal SaaS + non-US |
| Synergy Real Estate | Event Rental Company Full-Service (FL) | Florida | $1.63M | $486K | 30% | Event rental | HARD-REJECT | Hospitality-adjacent + below floor |
| Synergy Real Estate | Groundwater Treatment Equipment Rental (FL) | Florida | $3.5M | $1.3M | 37% | Equipment rental/water | HARD-REJECT | Below floor + capital-intensive equipment |
| Synergy Real Estate | Musical Instrument Rental & Repair (NJ) | New Jersey | $2.35M | $284K | 12% | Music equipment rental | HARD-REJECT | Below floor + consumer-leaning |
| Synergy Real Estate | Real Estate Investment Co Semi-Absentee (PA) | Pennsylvania | $2.37M | $395K | 17% | Real estate investment | HARD-REJECT | Below floor + asset-holding |
| Synergy Real Estate | Property Management Firm (NY) | New York | $600K | $300K | 50% | Property management | HARD-REJECT | Far below floor |
| Synergy Real Estate | Real Estate Property Mgmt Office (NY) | New York | $888K | undisclosed | undisclosed | Property management | HARD-REJECT | Below floor |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| DealForce | General | login-gated | 200 | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 4 | 0 | — |
| Everingham & Kerr | General (Email-only) | blocked (single-attempt) | skipped-email-only | 0 | 0 | — |
| Flippa | General (Email-only) | blocked (verified) | 200 | 0 | 0 | — |
| IAG M&A Advisors | General (Email-only) | blocked (single-attempt) | skipped-email-only | 0 | 0 | — |
| Quiet Light | General (Email-only) | blocked (verified) | 403 | 0 | 0 | — |
| Rejigg | General | blocked (single-attempt) | 200 | 0 | 0 | — |
| SMB Deal Hunter | General (Email-only) | blocked (single-attempt) | skipped-email-only | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Viking Mergers | General (Email-only) | blocked (single-attempt) | skipped-email-only | 0 | 0 | — |
| Website Closers | General | active | 200 | 12 | 0 | — |
| GP Bullhound | Niche-Specific (SaaS) | active | 200 | 6 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | blocked (single-attempt) | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 7 | 0 | — |
| Synergy Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 | 0 | — |

Notes:
- All 6 email-only sources marked blocked (single-attempt) because `brain/context/email-scan-results-2026-05-13.md` artifact was not present at scan time. Email-intelligence morning run did not produce the artifact; afternoon top-up will re-attempt.
- BizBuySell, Quiet Light (web), Flippa (web) are persistent verified blocks (Cloudflare / JS shell).
- DealForce login-gated — listings page is membership-paid; deal flow surfaces via email alerts (covered under email-only path).
- PCO Bookkeepers single-attempt: homepage returned no transactions in single fetch; M&A subpage not deep-crawled. Acceptable degradation.
- Rejigg single-attempt: homepage shows no active public listings; primary flow is email-only.
- Corpus path per niche logged: all 7 active-thesis niches with DealsX foreign-key matched used "DEALSX keywords" path (Specialty Pest, Estate Management, Specialty Commercial Equipment, Specialty Insurance Brokerage, Vertical SaaS for Luxury, Specialty Storage, High-End Commercial Cleaning). Private art advisory firms used "WR row enrichment" path (Niche Hypothesis + Quick notes — no DealsX equivalent). High-End Commercial Cleaning niche is pre-launch (7/20/2026) — corpus loaded but no thesis-match volume expected.

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: see `brain/trackers/weekly/{latest}-deal-aggregator-digest.md` for trailing window
- Target: 1-3/day — BELOW TARGET

Note: 0-match days have been frequent this cycle. Friday digest will surface source-productivity trend + proposed additions/retirements.
