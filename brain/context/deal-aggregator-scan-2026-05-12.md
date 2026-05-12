---
date: 2026-05-12
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 1
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live (Services + Insurance + SaaS docs re-read from Drive this run)
---
# Deal Aggregator Scan — 2026-05-12

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box gate AND matched an active niche corpus.

## Email Inbound Deals

None today. `email-scan-results-2026-05-12.md` had not been written at scan time (06:03 ET). Email-intelligence fires at 07:00 ET; the 14:00 ET afternoon top-up run will read today's email-scan artifact and surface any email-channel inbound (CIMs, broker blasts, intro forwards).

## Near Misses (not Slacked)

- **Business Exits — GovCon IT Firm (120+ Million in Judiciary & VA-Focused Contracts)** — $19.7M rev / $3.4M EBITDA / 17.5% margin. Clears Services BB financial gate. Industry (government-contract IT) does not match any active niche corpus.
- **Business Exits — B2B Experiential Marketing Vendor** — $14.3M rev / $3.3M EBITDA / 23.1% margin. Clears Services BB financial gate. Industry (experiential marketing) does not match any active niche corpus.
- **Business Exits — Government Contract ERP Service Business** — $14.0M rev / $2.6M EBITDA / 18.3% margin. Clears Services BB financial gate. Industry (government-contract ERP service) does not match any active niche corpus.
- **Synergy Business Brokers — Growing LED Display Solutions Company (FL)** — $11.2M rev / $4.6M cash flow / 41% margin / Florida. Clears Services BB financial gate. Industry (LED display tech / distribution) does not match any active niche corpus.
- **Email channel gap (timing)** — `email-scan-results-2026-05-12.md` not yet written at 06:03 ET. 8 email-only sources (Quiet Light, Flippa, Everingham & Kerr, Viking Mergers, Rejigg, DealForce, IAG M&A Advisors, SMB Deal Hunter) report 0 listings reviewed this run. Afternoon top-up (`--afternoon`, 14:00 ET) reads today's email-scan artifact and covers these channels.
- **BROWSER_AUTOMATION_UNAVAILABLE** — agent-browser is not installed on this host. BizBuySell skipped (known scraper 403, requires agent-browser). Surface for infra: `npm i -g agent-browser && agent-browser install`.

## Listings Reviewed (full log)

Niche corpus check per row: each listing was matched against the keyword corpus for every Active niche (Premium Pest Mgmt, Private Art Advisory, Estate Mgmt, Specialty Coffee Equipment Service, High-End Commercial Cleaning, Vertical SaaS for Luxury, Specialty Insurance Brokerage, Specialty Storage for HV Assets). Where the WEEKLY REVIEW row had a DealsX Niche reference, the DEALSX `Quick notes` + `Keywords` corpus was primary plus WR `Quick notes` supplementary. For Private Art Advisory (DealsX Niche blank), corpus was built from the WR row itself (Niche Hypothesis + Quick notes).

Sort order: PASS → NEAR-MISS → FLAG → HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm – 120+ Million in Judiciary & VA-Focused Contracts | undisclosed | $19,700,595 | $3,446,340 | 17.5% | Service / Software-SaaS | NEAR-MISS | clears Services BB; govcon IT not in any active niche corpus |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14,277,492 (TTM) | $3,297,944 (TTM) | 23.1% | Marketing & Consulting / Service | NEAR-MISS | clears Services BB; experiential marketing not in any active niche corpus |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14,046,972 | $2,572,171 | 18.3% | Service / Software-SaaS | NEAR-MISS | clears Services BB; govcon ERP not in any active niche corpus |
| Synergy Business Brokers | Growing LED Display Solutions Company | FL | $11,193,625 | $4,634,729 | 41.4% | Technology / Distribution | NEAR-MISS | clears Services BB; LED display tech not in any active niche corpus |
| Website Closers | Category Leading National Push-to-Talk Communications Platform | undisclosed | undisclosed | $12,527,324 (cash flow) | undisclosed | Wireless Communications / B2B | FLAG | revenue undisclosed; cash flow well above floor but no active-niche match — human review |
| Website Closers | Loss Prevention Training & Awareness Platform | undisclosed | undisclosed | $792,507 (cash flow) | undisclosed | Training Services | FLAG | revenue undisclosed; cash flow alone below floor but rev not disclosed — human review per Data Availability |
| Website Closers | SBA Pre-Qualified Lead Generation & Performance Marketing Agency | undisclosed | undisclosed | $846,746 (cash flow) | undisclosed | Marketing / Lead Generation | FLAG | revenue undisclosed; lead-gen is excluded by Insurance BB but routes Services; no niche match |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2,400,690 (cash flow) | undisclosed | M&A Brokerage / eCommerce | FLAG | revenue undisclosed; M&A intermediary not in active corpus |
| Website Closers | SBA Pre-Qualified SaaS — Digital Comment Card Customer Feedback Platform | undisclosed | undisclosed | $210,944 (cash flow) | undisclosed | SaaS (customer feedback) | FLAG | ARR undisclosed; asking $1.055M implies sub-$3M ARR but not auto-rejected per Data Availability — human review |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest | $21,313,476 (2025) | $12,974,692 (2025) | 60.9% | Healthcare | HARD-REJECT | Services BB hard-exclude: physician/provider-owned healthcare |
| Business Exits | Ireland Construction Business | Ireland | €25,000,000 | €6,150,000 | 24.6% | Construction | HARD-REJECT | Services BB hard-exclude: construction; geo non-US |
| Business Exits | California Property Tax Consultants | CA | $6,679,566 (2025) | $4,676,542 (2025) | 70.0% | Marketing & Consulting / Service | HARD-REJECT | revenue $6.7M below Services BB $10M floor (disclosed-and-failed); CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3,175,872 | $2,347,000 | 73.9% | Hospitality / Venue | HARD-REJECT | Services BB hard-exclude: restaurants/hospitality/nightlife; revenue below floor |
| Business Exits | Metal Building Supplier with US Manufacturing | US | $33,694,403 (TTM) | $3,973,506 (TTM) | 11.8% | Construction / Manufacturing | HARD-REJECT | Services BB hard-exclude: capital-intensive manufacturing / construction-adjacent |
| Business Exits | Texas Based Non-Emergency Medical Transport | TX | $7,743,083 | $2,874,318 | 37.1% | Service / Healthcare | HARD-REJECT | revenue below floor; provider-owned healthcare-adjacent |
| Business Exits | California Staffing Firm with Recurring Revenue | CA | $7,824,773 (2025) | $3,196,529 (2025) | 40.9% | Service | HARD-REJECT | revenue below Services BB $10M floor; CA soft-flag |
| Business Exits | Northeast Commercial Contractor Serving Healthcare and Financial Clients | Northeast | $21,959,113 (2024) | $2,784,735 (2024) | 12.7% | Construction | HARD-REJECT | Services BB hard-exclude: construction |
| Business Exits | Growing Atlanta Area Residential Plumbing & Septic Company | Atlanta GA | $11,706,308 (2025) | $2,406,695 (2025) | 20.6% | Service (plumbing) | HARD-REJECT | Services BB hard-exclude: construction / labor-heavy field services |
| Business Exits | Government Contract ERP — see NEAR-MISS row above | — | — | — | — | — | — | (duplicate row removed; see NEAR-MISS) |
| Business Exits | Design & Build Studio for Themed Props, Structures, & Interactive Experiences | undisclosed | $10,022,434 (2024) | $3,057,730 (2024) | 30.5% | Construction / Manufacturing | HARD-REJECT | Services BB hard-exclude: construction + capital-intensive manufacturing |
| Business Exits | Thriving Texas HVAC Company Specializing in Residential New Construction | TX | $21,986,180 | $2,284,289 | 10.4% | Construction-adjacent Service | HARD-REJECT | Services BB hard-exclude: construction / labor-heavy field services |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8,927,055 | $1,946,908 | 21.8% | Construction / Service | HARD-REJECT | revenue below $10M floor; construction-adjacent labor-heavy field services |
| Business Exits | Niche Construction Service Business | undisclosed | $10,800,000 | $2,300,000 (2025 accrual) | 21.3% | Construction | HARD-REJECT | Services BB hard-exclude: construction |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8,231,459 (2025) | $1,903,206 (2025) | 23.1% | Wholesale / Distribution | HARD-REJECT | revenue $8.2M below Services BB $10M floor |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4,895,568 | $1,539,977 | 31.5% | Manufacturing / Retail | HARD-REJECT | revenue below $10M floor; capital-intensive manufacturing hard-exclude |
| Business Exits | Southeast Electrical Contractor | Southeast | $5,280,585 (2025) | $1,910,497 (2025) | 36.2% | Construction / Service | HARD-REJECT | Services BB hard-exclude: construction; revenue below floor |
| Business Exits | Arizona Addiction Treatment Center | AZ | $4,446,766 (TTM) | $1,095,624 (TTM) | 24.6% | Healthcare | HARD-REJECT | Services BB hard-exclude: provider-owned healthcare; revenue below floor |
| Business Exits | Safe Pet Travel Products Distribution Company | undisclosed | $1,666,584 (2024) | $1,032,490 (2024) | 62.0% | Wholesale / Distribution | HARD-REJECT | Services BB hard-exclude: consumer retail / DTC; revenue below floor |
| Business Exits | Nevada Commercial Fireproofing Contractor | NV | $3,057,340 (2025) | $931,994 (2025) | 30.5% | Construction / Service | HARD-REJECT | Services BB hard-exclude: construction; revenue below floor |
| Business Exits | Government Contracted Military Promotional Products Business | undisclosed | $8,179,278 | $787,952 | 9.6% | Retail / Service | HARD-REJECT | revenue below floor; margin 9.6% below 10% margin floor; retail hard-exclude |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2,283,323 CAD | $763,741 CAD | 33.4% | Service | HARD-REJECT | revenue below $10M floor; geo non-US |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | FL | $1,074,754 (2025) | $683,310 (2025) | 63.6% | Healthcare | HARD-REJECT | Services BB hard-exclude: provider-owned healthcare; revenue below floor |
| Business Exits | Landscape Architecture Business – SBA Eligible | undisclosed | $5,500,000 | $1,800,000 | 32.7% | Construction | HARD-REJECT | Services BB hard-exclude: construction; revenue below floor |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4,144,975 (TTM) | $714,160 (TTM) | 17.2% | Restaurant / Food | HARD-REJECT | Services BB hard-excludes: restaurants/hospitality AND franchises |
| Business Exits | Colorado Based Regenerative & Functional Medicine Practice | CO | $894,910 (2025) | $494,099 (2025) | 55.2% | Healthcare | HARD-REJECT | Services BB hard-exclude: physician/provider practice; revenue below floor |
| Business Exits | Bay Area Residential Roofing Company | Bay Area CA | $2,500,254 (2025) | $469,568 (2025) | 18.8% | Construction / Service | HARD-REJECT | Services BB hard-exclude: construction; revenue below floor; CA soft-flag |
| Business Exits | Texas Home Health Staffing Firm | TX | $2,494,220 (2024-25 avg) | $337,193 (2024-25 avg) | 13.5% | Service / Healthcare | HARD-REJECT | revenue below floor; provider-owned healthcare-adjacent |
| Empire Flippers | Health & Fitness (94170) — Amazon FBA / eCommerce | undisclosed | $4,601,712 (annualized) | $383,476/mo net profit | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | Services BB hard-exclude: consumer retail / DTC |
| Empire Flippers | Beauty, Health & Fitness (94312) — eCommerce / FBA | undisclosed | $1,526,484 (annualized) | $127,207/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | Services BB hard-exclude: consumer retail / DTC |
| Empire Flippers | Finance (93687) — Affiliate / Digital Product / Lead Gen | undisclosed | $624,768 (annualized) | $52,064/mo | undisclosed | Digital Product / Affiliate | HARD-REJECT | revenue far below floor; consumer-adjacent content/affiliate |
| Empire Flippers | Medical, News & Education (94286) — eCommerce / Digital Product | undisclosed | $389,904 (annualized) | $32,492/mo | undisclosed | Digital Product / eCommerce | HARD-REJECT | revenue below floor; consumer-content hard-exclude |
| Empire Flippers | Food & Beverages, Religion (88534) — Amazon FBM/FBA | undisclosed | $310,884 (annualized) | $25,907/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | Services BB hard-exclude: consumer retail / DTC |
| Empire Flippers | Home, Lifestyle, Pet Care (86393) — Amazon FBA | undisclosed | $196,044 (annualized) | $16,337/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Home (92502) — Amazon FBA / eCommerce | undisclosed | $144,264 (annualized) | $12,022/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Technology, News & Education (94173) — Digital Product / Info Product / Subscription | undisclosed | $134,052 (annualized) | $11,171/mo | undisclosed | Content / Digital Product | HARD-REJECT | revenue below SaaS ARR floor; not vertical-SaaS |
| Empire Flippers | Business (93813) — Newsletter | undisclosed | $107,760 (annualized) | $8,980/mo | undisclosed | Newsletter / Content | HARD-REJECT | revenue below floor; not vertical SaaS |
| Empire Flippers | SEO, Business, Digital Media (93918) — Agency / Service | undisclosed | $183,204 (annualized) | $15,267/mo | undisclosed | Marketing Agency | HARD-REJECT | revenue below Services BB floor |
| Empire Flippers | Bed & Bath, Home (94001) — Amazon FBA / eCommerce | undisclosed | $42,072 (annualized) | $3,506/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Culinary, Pet Care, Food (92985) — Amazon FBA / eCommerce | undisclosed | $2,572,968 (annualized) | $214,417/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Pet Care (94115) — eCommerce | undisclosed | $4,108,596 (annualized) | $342,383/mo | undisclosed | eCommerce | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Cryptocurrency (90682) — Digital Product / Newsletter | undisclosed | $5,200,236 (annualized) | $433,353/mo | undisclosed | Digital / Crypto Content | HARD-REJECT | crypto/consumer-adjacent; not in active niches; SaaS hard-exclude (lending/credit-adjacent) |
| Empire Flippers | Kitchenware (89990) — Amazon FBA | undisclosed | $2,817,240 (annualized) | $234,770/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Lifestyle, Travel (93931) — eCommerce / FBA | undisclosed | $2,170,668 (annualized) | $180,889/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Home (88177) — Amazon FBA | undisclosed | $1,912,296 (annualized) | $159,358/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Kitchenware (89855) — Amazon FBA | undisclosed | $1,844,712 (annualized) | $153,726/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Business, Digital Media (84831) — Service / Digital Product / Affiliate | undisclosed | $1,775,196 (annualized) | $147,933/mo | undisclosed | Digital Service / Affiliate | HARD-REJECT | revenue below Services BB floor |
| Empire Flippers | Supplements, Health & Fitness (88296) — eCommerce / Subscription / FBA | undisclosed | $1,389,192 (annualized) | $115,766/mo | undisclosed | eCommerce / Subscription | HARD-REJECT | consumer retail / DTC hard-exclude |
| Empire Flippers | Home, Romance (83512) — Amazon FBA / FBM / eCommerce | undisclosed | $1,467,036 (annualized) | $122,253/mo | undisclosed | eCommerce / Amazon FBA | HARD-REJECT | consumer retail / DTC hard-exclude |
| Synergy Business Brokers | Seafood Processing And Distribution Company | Portugal | $165,000,000 | $5,900,000 | 3.6% | Distribution / Manufacturing | HARD-REJECT | geo non-US; manufacturing hard-exclude; margin 3.6% below 10% floor; revenue above $50M ceiling |
| Synergy Business Brokers | Oil and Gas Specialty: Equipment Rental and Trucking Solutions | Midland TX | $15,293,339 | $6,563,296 | 42.9% | Construction / Services | HARD-REJECT | Services BB hard-exclude: labor-heavy field services / construction-adjacent |
| Synergy Business Brokers | Commercial Plumbing Company, Strong Client Base | NJ | $13,575,714 | $4,034,348 | 29.7% | Construction / Services | HARD-REJECT | Services BB hard-exclude: construction |
| Synergy Business Brokers | Women's Health Practice – Multi-Physician OB/GYN and Urogynecology Clinic | Central FL | $6,578,488 | $3,376,803 | 51.3% | Healthcare | HARD-REJECT | Services BB hard-exclude: physician practices |
| Synergy Business Brokers | Precision Machine Shop, 50 Year Legacy | AZ | $7,500,000 | $2,300,000 | 30.7% | Manufacturing | HARD-REJECT | Services BB hard-exclude: capital-intensive manufacturing; revenue below floor |
| Synergy Business Brokers | Telecom Caller Trust Platform, 59% EBITDA Margin, 120% NRR | US | $2,710,000 (ARR-equivalent) | $1,610,000 | 59% | Technology / SaaS | HARD-REJECT | SaaS BB hard-exclude: ARR below $3M floor (disclosed-and-failed) |
| Synergy Business Brokers | Ethanol Producer For Sale With Real Estate | India | $10,500,000 | $3,000,000 | 28.6% | Manufacturing | HARD-REJECT | geo non-US; manufacturing hard-exclude |
| Synergy Business Brokers | Industrial Minerals Producer and Distributor | Peru | $7,000,000 | $4,500,000 | 64.3% | Distribution / Manufacturing | HARD-REJECT | geo non-US; manufacturing hard-exclude; revenue below floor |
| Synergy Business Brokers | Renovation Design And Build Company – Over 100% growth | NYC | $8,500,000 | $2,344,000 | 27.6% | Construction | HARD-REJECT | Services BB hard-exclude: NYC construction explicitly excluded |
| Synergy Business Brokers | Garment Manufacturing Facility, Premier Export-Oriented | Bangladesh | $12,500,000 | $1,950,000 | 15.6% | Distribution / Manufacturing | HARD-REJECT | geo non-US; manufacturing hard-exclude |
| Synergy Business Brokers | Railroad Construction Business with $11.5M in Contracts | MO | $7,833,546 | $1,498,641 | 19.1% | Construction / Transportation | HARD-REJECT | Services BB hard-exclude: construction; revenue below floor |
| Synergy Business Brokers | B2B Health and Beauty: Proprietary Ingredient Manufacturer and Distributor | Dubai | $3,087,523 | $2,245,335 | 72.7% | Distribution / Manufacturing | HARD-REJECT | geo non-US; manufacturing hard-exclude; revenue below floor |
| Synergy Business Brokers | Manufacturer of Specialty Copper Alloy Wires | India | $20,000,000 | $2,000,000 | 10.0% | Distribution / Manufacturing | HARD-REJECT | geo non-US; manufacturing hard-exclude |
| Synergy Business Brokers | Travel and Tourism Leader with Diversified Client Base | Saudi Arabia | $7,944,461 | $2,950,000 | 37.1% | Services / Tourism | HARD-REJECT | geo non-US; hospitality/tourism hard-exclude; revenue below floor |
| Synergy Business Brokers | Tech-Enabled Behavioral Health Firm with Recurring Revenue | Washington DC | $5,000,000 | $1,000,000 | 20.0% | Technology / Healthcare | HARD-REJECT | Services BB hard-exclude: provider-owned healthcare; revenue below floor |
| Synergy Business Brokers | Admissions Consulting Practice, Global, Fully Remote | US | $2,000,000 | $1,300,000 | 65.0% | Services | HARD-REJECT | revenue $2M below Services BB $10M floor |
| Synergy Business Brokers | Prominent 40-Year Pediatric Practice, Real Estate Available | NY | $5,830,000 | $1,650,000 | 28.3% | Healthcare | HARD-REJECT | Services BB hard-exclude: physician practices; revenue below floor |
| Synergy Business Brokers | Utility Support Construction Company | Nassau County NY | $12,000,000 | $2,000,000 | 16.7% | Construction | HARD-REJECT | Services BB hard-exclude: construction |
| Synergy Business Brokers | Growing Midwestern Trucking and Transportation Brokerage | Midwest | $9,000,000 | $1,650,000 | 18.3% | Transportation | HARD-REJECT | revenue $9M below Services BB $10M floor |
| Website Closers | Luxury RV & Coach Marketplace | undisclosed | undisclosed | $593,947 (cash flow) | undisclosed | Online Marketplace / RV | HARD-REJECT | consumer-marketplace / DTC hard-exclude (Services BB) |
| Website Closers | 67-Year Cayman Islands Architectural Design Firm | Cayman Islands | undisclosed | $386,774 (cash flow) | undisclosed | Architecture / Design | HARD-REJECT | geo non-US; cash flow below floor; construction-adjacent |
| Website Closers | Towels & Socks eCommerce Brand | undisclosed | undisclosed | $525,759 (cash flow) | undisclosed | eCommerce / Apparel | HARD-REJECT | consumer retail / DTC hard-exclude |
| Website Closers | Procurement Services & Distribution Company | undisclosed | undisclosed | $200,000 (cash flow) | undisclosed | B2B Distribution / Services | HARD-REJECT | cash flow $200K well below floor (asking $600K implies sub-$1M revenue) |
| Website Closers | Collectible Merchandise Brand | undisclosed | undisclosed | $723,549 (cash flow) | undisclosed | eCommerce / Collectibles | HARD-REJECT | consumer retail / DTC hard-exclude |
| Website Closers | Proprietary Home Products eCommerce Brand | undisclosed | undisclosed | $5,809,257 (cash flow) | undisclosed | eCommerce / Home Goods | HARD-REJECT | consumer retail / DTC hard-exclude |
| Website Closers | eCommerce Brand — Guided Fitness Journals | undisclosed | undisclosed | $304,018 (cash flow) | undisclosed | eCommerce / Fitness | HARD-REJECT | consumer retail / DTC hard-exclude |
| Website Closers | SBA Pre-Qualified B2B & DTC eCommerce Business — Multi-Label Women's Apparel | undisclosed | undisclosed | $890,141 (cash flow) | undisclosed | eCommerce / Apparel | HARD-REJECT | consumer retail / DTC hard-exclude |
| Synergy Business Brokers Real Estate | Event Rental Company: Full-Service | South FL | $1,633,413 | $486,182 (cash flow) | 29.8% | Services / Hospitality | HARD-REJECT | revenue $1.6M well below Services BB $10M floor; hospitality-adjacent |
| Synergy Business Brokers Real Estate | Short-Term Rental Property Management Company: 80+ Prime Locations | Midwest | $3,233,807 | $370,885 (cash flow) | 11.5% | Property Management (STR) | HARD-REJECT | revenue $3.2M below floor; STR property mgmt is different segment from Estate Management thesis (which targets UHNW estate operations) |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| Empire Flippers | General | active | 200 | 21 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Website Closers | General | active | 200 | 13 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | — | — |
| DealForce | General | active | N/A (email channel) | 0 | 0 | — |
| IAG M&A Advisors | General | active | N/A (email channel) | 0 | 0 | — |
| Rejigg | General | active | N/A (email channel) | 0 | 0 | — |
| Everingham & Kerr | General | active | N/A (email channel) | 0 | 0 | — |
| Flippa | General | active | N/A (email channel) | 0 | 0 | — |
| Quiet Light | General | active | N/A (email channel) | 0 | 0 | — |
| Viking Mergers | General | active | N/A (email channel) | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active | N/A (email channel) | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 0 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |
| GP Bullhound | Niche-Specific (SaaS) | active | 200 | 0 | 0 | — |

**Notes on Source Scorecard rows:**
- **BizBuySell** marked `blocked (verified)`: known scraper 403 (Cloudflare/UA-based); agent-browser is the only successful fallback path; `npm i -g agent-browser` is not installed on this host. Per skill stop hook, surfaced explicitly rather than silently dropped.
- **Email channel sources (8)**: `email-scan-results-2026-05-12.md` not yet written at scan time (06:03 ET; email-intelligence fires at 07:00 ET). All 8 email-only sources will be covered by the 14:00 ET afternoon top-up run, which reads today's email-scan artifact.
- **Sica Fletcher**: announcements page returned 10 post-close PE-consolidator tombstones (ALKEME / Hilb / World Insurance / Keyes), classified as intel only — these are closed deals, not for-sale listings, and do not enter the Listings Reviewed log.
- **PCO Bookkeepers**: blog and homepage scanned; no for-sale listings or transaction announcements in the visible content this run.
- **GP Bullhound**: homepage scanned (transactions page returned 404). Featured deals (Sdui, Peak, AB Tasty, Instaleap, Runna, Flo Health) are post-close advisory tombstones, intel only — not for-sale listings.

## Volume Check

- Deals surfaced today: **0**
- 7-day rolling average: **0** (fingerprint store empty — 0 entries; no prior PASS matches in window)
- Target: 1–3/day — **BELOW TARGET**

**Volume diagnostic:** Email channel (8 sources) reports 0 today purely because `email-scan-results-2026-05-12.md` hadn't landed at scan time — the afternoon top-up will fill that gap. Web-scrapable sources (5 active) reviewed 86 listings combined; 0 cleared the niche-corpus match. NEAR-MISS items show that listings are clearing financial gates but landing outside the active thesis corpus (govcon IT, marketing services, LED display tech). FLAG items concentrated at Website Closers reflect chronic revenue-undisclosed pattern on that platform — listings publish cash-flow only, leaving revenue gate ambiguous.

**Corpus path log (per Step 0c):**
- Premium Pest Management → DealsX keywords ("Specialty Pest & Environmental Management Services") + WR Quick notes
- Private art advisory firms → WR row enrichment (Niche Hypothesis + Quick notes) — DealsX reference blank
- Estate Management Companies → DealsX keywords + WR Quick notes
- Specialty Coffee Equipment Service → DealsX keywords ("Specialty Commercial Equipment Services") + WR Quick notes
- High-End Commercial Cleaning → DealsX keywords + WR Quick notes
- Vertical SaaS for Luxury → DealsX keywords + WR Quick notes
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords + WR Quick notes
- Storage & Related Services for High Value Assets → DealsX keywords ("Specialty Storage & Handling for High-Value Collections") + WR Quick notes
