---
date: 2026-05-15
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 1
sources_blocked_single_attempt: 8
email_deals: 0
buy_box_source: live
---
# Deal Aggregator Scan — 2026-05-15

## Deals Surfaced (sent to Slack individually)

None today.

## Email Inbound Deals

None today. `brain/context/email-scan-results-2026-05-15.md` was not present at scan time — email-intelligence artifact gap (see Near Misses).

## Near Misses (not Slacked)

- **email-scan-results-2026-05-15.md missing** — email-intelligence artifact for today not on disk; all 8 email-channel sources (DealForce, Everingham & Kerr, Flippa email, IAG M&A, Quiet Light email, Rejigg, SMB Deal Hunter, Viking Mergers) went unread this run. Logged as `blocked (single-attempt)` in scorecard. Email channels typically carry the highest hit rate — gap likely deflates today's PASS count.
- **GovCon IT firm** ($19.7M rev, Virginia-focused, Business Exits) — Services BB rev range PASS; no active-niche corpus match (govcon IT services not in luxury-services thesis). Tracked for thesis drift.
- **B2B Experiential Marketing Vendor** ($14.3M rev, Business Exits) — Services BB rev range PASS, EBITDA undisclosed, no niche corpus match. Marketing services not on thesis list.
- **Government Contract ERP Service** ($14M rev, Business Exits) — Services BB rev PASS, but vertical SaaS for govt is not the luxury-vertical SaaS niche corpus. NEAR-MISS.
- **Oil/Gas Equipment Rental & Trucking** (Texas, $15.29M rev, $6.56M cash flow / 43% margin, Synergy) — clears Services BB financial gate; energy-services not in active niche corpus.
- **LED Display Solutions** (Florida, $11.19M rev, $4.63M EBITDA / 41% margin, Synergy) — clears Services BB financial gate; tech-distribution not in active niche corpus.
- **SaaS Provider, Business Management Software** ($40M ask, Website Closers) — generic horizontal business-mgmt SaaS, not vertical-luxury-asset SaaS corpus → SaaS BB likely fails on horizontal hard-exclude. ARR/EBITDA undisclosed.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm – 120+ Million in Judiciary & VA-Focused Contracts | Virginia | $19.7M | undisclosed | undisclosed | IT services / govcon | NEAR-MISS | Clears Services BB rev gate; no active-niche corpus match (govcon IT not on luxury-services thesis) |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.3M | undisclosed | undisclosed | Marketing services | NEAR-MISS | Clears rev gate; no active-niche corpus match |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14M | undisclosed | undisclosed | SaaS / govcon | NEAR-MISS | Govt vertical, not luxury-asset SaaS corpus |
| Synergy Business Brokers | Oil and Gas Specialty: Equipment Rental and Trucking | Midland County, TX | $15.29M | $6.56M (NCF) | 43% | Oil/gas services | NEAR-MISS | Clears Services BB; no active-niche corpus match |
| Synergy Business Brokers | Growing LED Display Solutions Company | Florida | $11.19M | $4.63M (NCF) | 41% | Tech / distribution | NEAR-MISS | Clears Services BB; no active-niche corpus match |
| Website Closers | SaaS Provider of Business Management Software | undisclosed | undisclosed | undisclosed | undisclosed | Horizontal SaaS | NEAR-MISS | Generic business-mgmt SaaS, likely horizontal hard-exclude; ARR undisclosed |
| Sica Fletcher | Safe Harbour Insurance Management → ALKEME (announcement) | Massachusetts | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal for Specialty Insurance niche, not sell-side |
| Sica Fletcher | O'Neill Associates Consulting → ALKEME (announcement) | Florida | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Surety Bonds LLC → Hilb Group (announcement) | Georgia | undisclosed | undisclosed | undisclosed | Surety bonds | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Quantum Resource Group → ALKEME (announcement) | Maryland | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Centennial State Insurance Group → ALKEME (announcement) | Colorado | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal |
| GP Bullhound | Sdui growth investment by Bain Capital (announcement) | undisclosed | undisclosed | undisclosed | undisclosed | EdTech SaaS | FLAG | Growth round, not sell-side |
| GP Bullhound | Peak → UiPath (announcement) | undisclosed | undisclosed | undisclosed | undisclosed | Horizontal AI SaaS | FLAG | Closed acquisition; horizontal SaaS |
| GP Bullhound | Flo Health investment by General Atlantic (announcement) | undisclosed | undisclosed | undisclosed | undisclosed | Consumer health SaaS | FLAG | Growth round, B2C |
| GP Bullhound | Runna → Strava (announcement) | undisclosed | undisclosed | undisclosed | undisclosed | Consumer fitness SaaS | FLAG | Closed B2C acquisition |
| GP Bullhound | Instaleap → Instacart (announcement) | undisclosed | undisclosed | undisclosed | undisclosed | Retail/commerce SaaS | FLAG | Closed acquisition; not luxury vertical |
| GP Bullhound | AB Tasty ↔ VWO merger (announcement) | undisclosed | undisclosed | undisclosed | undisclosed | Horizontal SaaS | FLAG | Horizontal A/B-testing SaaS |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest | $21.3M | undisclosed | undisclosed | Healthcare / provider-owned | HARD-REJECT | Industry hard-exclude (physician/provider-owned healthcare) |
| Business Exits | Ireland Construction Business | Ireland | €25M | undisclosed | undisclosed | Construction | HARD-REJECT | Industry hard-exclude (construction) + non-US |
| Business Exits | California Property Tax Consultants | California | $6.7M | undisclosed | undisclosed | Tax/consulting services | HARD-REJECT | Below $10M Services BB rev floor (disclosed-and-failed); CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.2M | undisclosed | undisclosed | Hospitality / events | HARD-REJECT | Industry hard-exclude (hospitality / restaurants) + below rev floor |
| Business Exits | Metal Building Supplier with US Manufacturing | US | $33.7M | undisclosed | undisclosed | Construction / manufacturing | HARD-REJECT | Industry hard-exclude (construction + cap-intensive mfg) |
| Business Exits | Texas Non-Emergency Medical Transport | Texas | $7.7M | undisclosed | undisclosed | Healthcare-adjacent transport | HARD-REJECT | Below $10M rev floor + healthcare-provider adjacency |
| Business Exits | California Staffing Firm | California | $7.8M | undisclosed | undisclosed | Staffing services | HARD-REJECT | Below $10M rev floor; CA soft-flag |
| Business Exits | Northeast Commercial Contractor (Healthcare/Financial) | Northeast | $22M | undisclosed | undisclosed | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Business Exits | Atlanta Residential Plumbing & Septic | Georgia | $11.7M | undisclosed | undisclosed | Construction / labor-heavy field service | HARD-REJECT | Industry hard-exclude (labor-heavy field service) |
| Business Exits | Themed Props & Structures Studio | undisclosed | $10M | undisclosed | undisclosed | Construction / manufacturing | HARD-REJECT | Industry hard-exclude (construction + mfg) |
| Business Exits | Texas HVAC Residential New Construction | Texas | $22M | undisclosed | undisclosed | Construction labor-heavy | HARD-REJECT | Industry hard-exclude (construction) |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.9M | undisclosed | undisclosed | Telecom field service | HARD-REJECT | Below $10M rev floor (disclosed-and-failed) |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | undisclosed | undisclosed | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8.2M | undisclosed | undisclosed | Wholesale / distribution | HARD-REJECT | Below $10M rev floor |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.9M | undisclosed | undisclosed | Manufacturing / retail | HARD-REJECT | Below floor + cap-intensive mfg + consumer retail |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.3M | undisclosed | undisclosed | Construction | HARD-REJECT | Below floor + construction |
| Business Exits | Arizona Addiction Treatment Center | Arizona | $4.4M | undisclosed | undisclosed | Healthcare provider | HARD-REJECT | Below floor + healthcare provider |
| Business Exits | Safe Pet Travel Products Distribution | undisclosed | $1.7M | undisclosed | undisclosed | Consumer DTC | HARD-REJECT | Below floor + consumer retail/DTC |
| Business Exits | Nevada Commercial Fireproofing Contractor | Nevada | $3.1M | undisclosed | undisclosed | Construction | HARD-REJECT | Below floor + construction |
| Business Exits | Government Contracted Military Promotional Products | USA (remote) | $8.2M | undisclosed | undisclosed | Consumer retail | HARD-REJECT | Below floor + consumer retail |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2.3M CAD | undisclosed | undisclosed | Staffing services | HARD-REJECT | Below floor + non-US |
| Business Exits | Florida Med Spa and Regenerative Medicine | Florida | $1.1M | undisclosed | undisclosed | Healthcare provider | HARD-REJECT | Below floor + healthcare provider |
| Business Exits | Landscape Architecture Business (SBA Eligible) | undisclosed | $5.5M | undisclosed | undisclosed | Construction | HARD-REJECT | Below floor + construction |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.1M | undisclosed | undisclosed | Restaurant + franchise | HARD-REJECT | Industry hard-exclude (franchise + restaurant) |
| Business Exits | Colorado Regenerative & Functional Medicine | Colorado | $895K | undisclosed | undisclosed | Healthcare provider | HARD-REJECT | Below floor + healthcare provider |
| Business Exits | Bay Area Residential Roofing | California | $2.5M | undisclosed | undisclosed | Construction | HARD-REJECT | Below floor + construction; CA soft-flag |
| Business Exits | Texas Home Health Staffing Firm | Texas | $2.5M | undisclosed | undisclosed | Healthcare staffing | HARD-REJECT | Below floor + healthcare provider adjacency |
| Synergy BB Real Estate | Event Rental Company: Full-Service | Florida (South) | $1.63M | $486K (SDE) | 30% | Event services | HARD-REJECT | Below $10M Services BB rev floor + below EBITDA floor |
| Synergy BB Real Estate | Short-Term Rental Property Management Co (80+ Locations) | Midwest | $3.23M | $371K (SDE) | 11% | Vacation-rental property mgmt | HARD-REJECT | Below rev floor + below EBITDA floor; STR mgmt not Estate Mgmt corpus |
| Website Closers | eCommerce Brand ($4M ask) | undisclosed | undisclosed | undisclosed | undisclosed | eCommerce / DTC | HARD-REJECT | Industry hard-exclude (consumer retail/DTC) |
| Website Closers | eCommerce Retailer ($85M ask, multi-brand Amazon) | undisclosed | undisclosed | undisclosed | undisclosed | eCommerce / DTC | HARD-REJECT | Industry hard-exclude (consumer retail/DTC) + above rev ceiling |
| Empire Flippers | Beauty/Health/Fitness Amazon FBA | undisclosed | $6.31M annualized | $1.53M annualized | 24% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Finance affiliate/digital | undisclosed | $1.26M annualized | $625K annualized | 50% | Affiliate / digital product | HARD-REJECT | Below floor + consumer/DTC |
| Empire Flippers | Religion/Spirituality Amazon KDP | undisclosed | $477K annualized | $369K annualized | 77% | Amazon KDP digital | HARD-REJECT | Below floor + consumer/DTC |
| Empire Flippers | Sports/Hobbies eCommerce | undisclosed | $1.77M annualized | $181K annualized | 10% | eCommerce | HARD-REJECT | Below floor + consumer/DTC |
| Empire Flippers | Home Amazon FBA | undisclosed | $861K annualized | $144K annualized | 17% | Amazon FBA | HARD-REJECT | Below floor + consumer/DTC |
| Empire Flippers | Tech/News/Education digital subscription | undisclosed | $298K annualized | $119K annualized | 40% | Digital subscription | HARD-REJECT | Below floor + consumer DTC |
| Empire Flippers | Health/Fitness/Home/Medical Amazon FBA ($23M ask) | undisclosed | $17.59M annualized | $4.60M annualized | 26% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Culinary/Pet/F&B Amazon FBA ($18.65M ask) | undisclosed | $24.46M annualized | $2.57M annualized | 11% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Pet Care eCommerce ($17M ask) | undisclosed | $19.40M annualized | $4.11M annualized | 21% | eCommerce / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Crypto digital/newsletter ($16M ask) | undisclosed | $8.30M annualized | $5.20M annualized | 63% | Crypto digital media | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Lifestyle/Travel eCommerce ($8.8M ask) | undisclosed | $14.35M annualized | $2.17M annualized | 15% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Home Amazon FBA ($7.17M ask) | undisclosed | $8.10M annualized | $1.91M annualized | 24% | Amazon FBA | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Business/Digital Media service+digital ($5.32M ask) | undisclosed | $3.75M annualized | $1.78M annualized | 47% | Service + digital product | HARD-REJECT | Consumer DTC adjacency; service-digital hybrid not luxury-vertical |
| Empire Flippers | Supplements/Health/Beauty Amazon FBA ($5.32M ask) | undisclosed | $3.32M annualized | $1.39M annualized | 42% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Home/Romance Amazon FBA ($4.77M ask) | undisclosed | $5.84M annualized | $1.47M annualized | 25% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Hobbies/Gaming Amazon FBA ($4.63M ask) | undisclosed | $4.40M annualized | $1.32M annualized | 30% | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Synergy Business Brokers | Seafood Processing and Distribution | Portugal | $165M | $5.9M | 4% | Distribution / mfg | HARD-REJECT | Above $50M rev ceiling + below 10% margin floor + non-US + cap-intensive mfg |
| Synergy Business Brokers | Commercial Construction Tech (+176% YoY) | Florida | $9.06M | $3.28M | 36% | Construction tech | HARD-REJECT | Below $10M rev floor + construction |
| Synergy Business Brokers | Commercial Plumbing Company | New Jersey | $13.58M | $4.03M | 30% | Construction / labor-heavy | HARD-REJECT | Industry hard-exclude (construction labor-heavy field service) |
| Synergy Business Brokers | Women's Health OB/GYN Multi-Physician | Central Florida | $6.58M | $3.38M | 51% | Healthcare physician-owned | HARD-REJECT | Industry hard-exclude (provider-owned healthcare) + below floor |
| Synergy Business Brokers | Precision Machine Shop (50yr Legacy) | Arizona | $7.5M | $2.3M | 31% | Manufacturing | HARD-REJECT | Industry hard-exclude (cap-intensive mfg) + below floor |
| Synergy Business Brokers | Telecom Caller Trust Platform (59% EBITDA) | United States | $2.71M | $1.61M | 59% | SaaS / telecom | HARD-REJECT | Below SaaS BB ARR floor ($3M) |
| Synergy Business Brokers | Ethanol Producer with Real Estate | India | $10.5M | $3M | 29% | Manufacturing | HARD-REJECT | Manufacturing + non-US |
| Synergy Business Brokers | Industrial Minerals Producer | Peru | $7M | $4.5M | 64% | Manufacturing / distribution | HARD-REJECT | Below floor + manufacturing + non-US |
| Synergy Business Brokers | Renovation Design and Build (NYC) | New York City | $8.5M | $2.34M | 28% | Construction (NYC) | HARD-REJECT | NYC construction explicitly excluded + below floor |
| Synergy Business Brokers | Garment Manufacturing Facility | Bangladesh | $12.5M | $1.95M | 16% | Manufacturing / distribution | HARD-REJECT | Manufacturing + non-US |
| Synergy Business Brokers | Railroad Construction with $11.5M Contracts | Missouri | $7.83M | $1.50M | 19% | Construction | HARD-REJECT | Below floor + construction |
| Synergy Business Brokers | B2B Health/Beauty Ingredient Manufacturer | Dubai | $3.09M | $2.25M | 73% | Manufacturing | HARD-REJECT | Below floor + manufacturing + non-US |
| Synergy Business Brokers | Specialty Copper Alloy Wires Manufacturer | India | $20M | $2M | 10% | Manufacturing | HARD-REJECT | Manufacturing + non-US |
| Synergy Business Brokers | Travel and Tourism Leader | Saudi Arabia | $7.94M | $2.95M | 37% | Hospitality / travel | HARD-REJECT | Hospitality + non-US + below floor |
| Synergy Business Brokers | Admissions Consulting Practice (Global) | United States (remote) | $2M | $1.3M | 65% | Services | HARD-REJECT | Below floor (disclosed-and-failed) |
| Synergy Business Brokers | 40-Year Pediatric Practice | New York | $5.83M | $1.65M | 28% | Healthcare physician-owned | HARD-REJECT | Industry hard-exclude (physician-owned) + below floor |
| Synergy Business Brokers | Utility Support Construction | Nassau County, NY | $12M | $2M | 17% | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Synergy Business Brokers | Midwestern Trucking and Transportation Brokerage | Midwest | $9M | $1.65M | 18% | Transportation services | HARD-REJECT | Below floor (disclosed-and-failed) |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 30 | 0 | — |
| DealForce | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 16 | 0 | — |
| Everingham & Kerr | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| Flippa | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| IAG M&A Advisors | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| Quiet Light | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| Rejigg | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| SMB Deal Hunter | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Viking Mergers | General (email) | blocked (single-attempt) | — | 0 | 0 | — |
| Website Closers | General | active | 200 | 3 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | 200 | 6 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 5 | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |

**Notes on blocked status:**
- BizBuySell: WebFetch returned 403 on two separate paths (`/businesses-for-sale/` and `/north-east-businesses-for-sale/`); agent-browser fallback unavailable on this VPS (`agent-browser: command not found`). Status `blocked (verified)` per stop hook (two attempts). `BROWSER_AUTOMATION_UNAVAILABLE` infra gap surfaced for installation.
- 8 email-channel sources marked `blocked (single-attempt)` because today's `email-scan-results-2026-05-15.md` is missing on disk. Email-intelligence run did not produce the artifact; deal-aggregator could not parse email channels this cycle. Backfill on next email-intelligence run will recover any deals.
- Last Match Date column shows `—` for every source: fingerprint store `brain/context/deal-aggregator-fingerprints.jsonl` is empty (0 records). No prior matches recorded.

**Niche corpus path used (per Step 0c):**
- Premium Pest Management → DealsX keywords (Specialty Pest & Environmental Management Services row)
- Private art advisory firms → WR row enrichment (DealsX Niche blank; Niche Hypothesis + Quick notes corpus)
- Estate Management Companies → DealsX keywords
- Specialty Coffee Equipment Service → DealsX keywords (Specialty Commercial Equipment Services row)
- High-End Commercial Cleaning → DealsX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords (Specialty Insurance Brokerage row)
- Storage & Related Services for High Value Assets → DealsX keywords (Specialty Storage & Handling for High-Value Collections row)

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: 0 (fingerprint store empty)
- Target: 1-3/day — BELOW TARGET

Drivers: (1) email channels unparsed today due to missing email-scan-results artifact — typically the highest-yield surface; (2) BizBuySell blocked, agent-browser dependency unmet on VPS; (3) public marketplace inventory today skews construction / healthcare / consumer-DTC / non-US / sub-floor — eight near-misses cleared the financial gate but missed active-niche corpora.
