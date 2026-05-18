---
date: 2026-05-18
deals_found: 1
sources_scanned: 17
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 0
dealsx_replies: 1
buy_box_source: live
---
# Deal Aggregator Scan — 2026-05-18

## Deals Surfaced (sent to Slack individually)

None from platform/email scanning. No listing cleared the buy-box gate AND matched an active-niche corpus today. (One DealsX inbound reply surfaced separately — see DealsX Proprietary Outreach Replies below; it counts toward the daily evaluable-deals volume.)

## Email Inbound Deals

None today. `brain/context/email-scan-results-2026-05-18.md` present and parsed: no CIMs, no NDA/teaser/blind-profile emails, no broker BLAST with listing-signal keywords (artifact Sections 2 & 7 both "None"). SMB Deal Hunter / Helen Guo "It's finally out!" confirmed product-launch newsletter, not a per-listing broker blast.

## DealsX Proprietary Outreach Replies

Inbound owner replies to DealsX cold outreach (Channel 6). Contact handoffs — no financials. Surfaced to Slack, count toward daily volume, do NOT trigger target-discovery.

1. **Greg Bruyere** — tristate-stl.com | gregb@tristate-stl.com | linkedin.com/in/greg-bruyere-71275544 — Source: DealsX Proprietary Outreach (Prospect Geni notification 2026-05-17 19:38, arrived after 5/17 scans; first surfaced today). St. Louis MO. Industry/fit unqualified — outreach-manager owns qualification. Slack-posted to #active-deals (http 200), fingerprint added.

## Near Misses (not Slacked)

- **GovCon IT Firm** ($19.7M rev, $3.45M EBITDA / 17%, Virginia, Business Exits) — clears Services BB financial gate; IT/govcon not in any active-niche corpus (luxury/high-value-asset services thesis).
- **B2B Experiential Marketing Vendor** ($14.28M rev, $3.30M EBITDA / 23%, Business Exits) — clears Services BB; marketing services off-thesis.
- **Government Contract ERP Service** ($14.05M rev, $2.57M EBITDA, Business Exits) — clears Services BB rev; govt ERP is not the luxury-vertical SaaS corpus.
- **Oil & Gas Equipment Rental & Trucking** ($15.29M rev, $6.56M NCF / 43%, Midland TX, Synergy) — clears Services rev gate; energy services off active-niche corpus (NCF also above the $5M Services EBITDA band — flagged either way).
- **LED Display Solutions** ($11.19M rev, $4.63M NCF / 41%, Florida, Synergy) — clears Services BB financials; tech distribution off-thesis.
- **Ed-Tech eLearning Platform** (SDE $1.63M, $7.5M ask, Website Closers) — education SaaS, ARR undisclosed (flag-not-reject), not the luxury-asset vertical SaaS corpus.
- **Loss Prevention Training & Awareness Platform** (B2B software, SDE $792K, $3.3M ask, Website Closers) — B2B training software, ARR undisclosed; not a luxury-asset vertical SaaS niche.
- **Shopify Business Brokerage** (SDE $2.4M, $14.5M ask, Website Closers) — B2B brokerage service, eComm-adjacent, no revenue disclosed, no active-niche corpus match.
- **infra: fingerprint helper `check` broken on Linux VPS** — `scripts/deal-aggregator-fingerprint.sh check` runs `date -u -v-30d` (BSD/macOS syntax) whenever the store file exists; fails with `date: invalid option -- 'v'` under `set -e`. Dedup performed manually this run (store has 0 records → all NEW). `hash` and `add` work (portable `date -u +%Y-%m-%d`). Recommend porting the cutoff to GNU `date -u -d "-30 days" +%Y-%m-%d` with an OS guard.
- **infra: agent-browser not installed on this VPS** — `agent-browser: command not found`. JS-shell/Cloudflare/403 fallback unavailable; BizBuySell and GP Bullhound could not be recovered (see Source Scorecard notes).

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm – 120M+ Judiciary & VA Contracts | Virginia | $19.7M | $3.45M | 17% | IT services / govcon | NEAR-MISS | Clears Services BB; no active-niche corpus match |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.28M | $3.30M | 23% | Marketing services | NEAR-MISS | Clears Services BB; off-thesis industry |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14.05M | $2.57M | 18% | SaaS / govcon | NEAR-MISS | Govt vertical, not luxury-asset SaaS corpus |
| Synergy Business Brokers | Oil and Gas Specialty: Equipment Rental & Trucking | Midland County, TX | $15.29M | $6.56M (NCF) | 43% | Oil/gas services | NEAR-MISS | Clears Services rev; off-thesis; NCF above $5M band |
| Synergy Business Brokers | Growing LED Display Solutions Company | Florida | $11.19M | $4.63M (NCF) | 41% | Tech / distribution | NEAR-MISS | Clears Services BB; off-thesis industry |
| Website Closers | Ed-Tech eLearning Platform | undisclosed | undisclosed | $1.63M (SDE) | undisclosed | Education SaaS | NEAR-MISS | ARR undisclosed; not luxury-asset vertical SaaS corpus |
| Website Closers | Loss Prevention Training & Awareness Platform | undisclosed | undisclosed | $792K (SDE) | undisclosed | B2B training software | NEAR-MISS | ARR undisclosed; not luxury-asset SaaS corpus |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2.4M (SDE) | undisclosed | Business brokerage / eComm | NEAR-MISS | No rev disclosed; no active-niche corpus match |
| Sica Fletcher | Safe Harbour Insurance Management → ALKEME | Massachusetts | undisclosed | undisclosed | undisclosed | Insurance management | FLAG | Closed-deal tombstone; Insurance niche intel, not sell-side |
| Sica Fletcher | O'Neill Associates Consulting → ALKEME | Florida | undisclosed | undisclosed | undisclosed | Consulting / insurance | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Surety Bonds LLC → The Hilb Group | Georgia | undisclosed | undisclosed | undisclosed | Surety bonds | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Quantum Resource Group → ALKEME | Maryland | undisclosed | undisclosed | undisclosed | Insurance services | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Centennial State Insurance Group → ALKEME | Colorado | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | C&A Insurance Agency → World Insurance Associates | New York | undisclosed | undisclosed | undisclosed | Insurance agency | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Bellwether Insurance Group → ALKEME | Florida | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Velocity Public Adjusting → Gavnat Public Adjusters | Kentucky/Arizona | undisclosed | undisclosed | undisclosed | Public adjusting | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Filer Insurance → Keyes Coverage / Keystone Agency Partners | Florida | undisclosed | undisclosed | undisclosed | Insurance services | FLAG | Closed-deal tombstone; intel signal |
| Sica Fletcher | Couch Braunsdorf Insurance Group → ALKEME | New Jersey | undisclosed | undisclosed | undisclosed | Insurance brokerage | FLAG | Closed-deal tombstone; intel signal |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest | $21.31M | $12.97M | 61% | Healthcare / provider-owned | HARD-REJECT | Industry hard-exclude (provider-owned healthcare) |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | 25% | Construction | HARD-REJECT | Industry hard-exclude (construction) + non-US |
| Business Exits | California Property Tax Consultants | California | $6.68M | $4.68M | 70% | Tax / consulting services | HARD-REJECT | Below $10M Services rev floor (disclosed-and-failed); CA soft-flag |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | 74% | Hospitality / events | HARD-REJECT | Industry hard-exclude (hospitality) + below rev floor |
| Business Exits | Metal Building Supplier with US Manufacturing | US | $33.69M | $3.97M | 12% | Construction / mfg | HARD-REJECT | Industry hard-exclude (construction + cap-intensive mfg) |
| Business Exits | Texas Non-Emergency Medical Transport | Texas | $7.74M | $2.87M | 37% | Healthcare-adjacent transport | HARD-REJECT | Below $10M rev floor + healthcare adjacency |
| Business Exits | California Staffing Firm with Recurring Revenue | California | $7.82M | $3.20M | 41% | Staffing services | HARD-REJECT | Below $10M rev floor; CA soft-flag |
| Business Exits | Northeast Commercial Contractor (Healthcare/Financial) | Northeast | $21.96M | $2.78M | 13% | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Business Exits | Atlanta Area Residential Plumbing & Septic | Georgia | $11.71M | $2.41M | 21% | Construction / labor-heavy field svc | HARD-REJECT | Industry hard-exclude (labor-heavy field service) |
| Business Exits | Design & Build Studio for Themed Props & Structures | undisclosed | $10.02M | $3.06M | 31% | Construction / mfg | HARD-REJECT | Industry hard-exclude (construction + mfg) |
| Business Exits | Texas HVAC – Residential New Construction | Texas | $21.99M | $2.28M | 10% | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | 22% | Telecom field service | HARD-REJECT | Below $10M rev floor (disclosed-and-failed) |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.30M | 21% | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8.23M | $1.90M | 23% | Wholesale / distribution | HARD-REJECT | Below $10M rev floor |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.9M | $1.54M | 31% | Manufacturing / retail | HARD-REJECT | Below floor + cap-intensive mfg + consumer retail |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | 36% | Construction | HARD-REJECT | Below floor + construction |
| Business Exits | Arizona Addiction Treatment Center | Arizona | $4.45M | $1.10M | 25% | Healthcare provider | HARD-REJECT | Below floor + healthcare provider |
| Business Exits | Safe Pet Travel Products Distribution | undisclosed | $1.67M | $1.03M | 62% | Consumer DTC | HARD-REJECT | Below floor + consumer retail/DTC |
| Business Exits | Nevada Commercial Fireproofing Contractor | Nevada | $3.06M | $932K | 30% | Construction | HARD-REJECT | Below floor + construction |
| Business Exits | Government Contracted Military Promotional Products | USA (remote) | $8.18M | $788K | 10% | Consumer retail | HARD-REJECT | Below floor + consumer retail |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2.28M CAD | $764K CAD | 33% | Staffing services | HARD-REJECT | Below floor + non-US |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | Florida | $1.07M | $724K | 67% | Healthcare provider | HARD-REJECT | Below floor + healthcare provider |
| Business Exits | Landscape Architecture Business (SBA Eligible) | undisclosed | $5.5M | $1.80M | 33% | Construction | HARD-REJECT | Below floor + construction |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.14M | $714K | 17% | Restaurant + franchise | HARD-REJECT | Industry hard-exclude (franchise + restaurant) |
| Business Exits | Colorado Regenerative & Functional Medicine Practice | Colorado | $895K | $494K | 55% | Healthcare provider | HARD-REJECT | Below floor + healthcare provider |
| Business Exits | Bay Area Residential Roofing Company | California | $2.5M | $470K | 19% | Construction | HARD-REJECT | Below floor + construction; CA soft-flag |
| Business Exits | Texas Home Health Staffing Firm | Texas | $2.49M | $337K | 14% | Healthcare staffing | HARD-REJECT | Below floor + healthcare-provider adjacency |
| Synergy Business Brokers | Seafood Processing and Distribution Company | Portugal | $165M | $5.9M (NCF) | 4% | Distribution / mfg | HARD-REJECT | Above $50M rev ceiling + below 10% margin + non-US + cap-mfg |
| Synergy Business Brokers | Commercial Construction Tech (+176% YoY) | Florida | $9.06M | $3.28M (NCF) | 36% | Construction tech | HARD-REJECT | Below $10M rev floor + construction |
| Synergy Business Brokers | Commercial Plumbing Company | New Jersey | $13.58M | $4.03M (NCF) | 30% | Construction / labor-heavy | HARD-REJECT | Industry hard-exclude (construction labor-heavy) |
| Synergy Business Brokers | Women's Health Multi-Physician OB/GYN Clinic | Central Florida | $6.58M | $3.38M (NCF) | 51% | Healthcare provider-owned | HARD-REJECT | Industry hard-exclude (provider-owned) + below floor |
| Synergy Business Brokers | Precision Machine Shop, 50-Year Legacy | Arizona | $7.5M | $2.30M (NCF) | 31% | Manufacturing | HARD-REJECT | Industry hard-exclude (cap-intensive mfg) + below floor |
| Synergy Business Brokers | Telecom Caller Trust Platform (59% EBITDA, 120% NRR) | United States | $2.71M | $1.61M (NCF) | 59% | SaaS / telecom | HARD-REJECT | Below SaaS BB ARR floor ($3M, disclosed-and-failed) |
| Synergy Business Brokers | Ethanol Producer with Real Estate | India | $10.5M | $3.0M (NCF) | 29% | Manufacturing | HARD-REJECT | Manufacturing + non-US |
| Synergy Business Brokers | Industrial Minerals Producer and Distributor | Peru | $7.0M | $4.5M (NCF) | 64% | Manufacturing / distribution | HARD-REJECT | Below floor + manufacturing + non-US |
| Synergy Business Brokers | Renovation Design and Build Company | NYC, New York | $8.5M | $2.34M (NCF) | 28% | Construction (NYC) | HARD-REJECT | NYC construction explicitly excluded + below floor |
| Synergy Business Brokers | Garment Manufacturing Facility | Bangladesh | $12.5M | $1.95M (NCF) | 16% | Manufacturing | HARD-REJECT | Manufacturing + non-US |
| Synergy Business Brokers | Railroad Construction Business ($11.5M Contracts) | Missouri | $7.83M | $1.50M (NCF) | 19% | Construction | HARD-REJECT | Below floor + construction |
| Synergy Business Brokers | B2B Health & Beauty Ingredient Manufacturer | Dubai | $3.09M | $2.25M (NCF) | 73% | Manufacturing | HARD-REJECT | Below floor + manufacturing + non-US |
| Synergy Business Brokers | Specialty Copper Alloy Wires Manufacturer | India | $20M | $2.0M (NCF) | 10% | Manufacturing | HARD-REJECT | Manufacturing + non-US |
| Synergy Business Brokers | Travel and Tourism Leader | Saudi Arabia | $7.94M | $2.95M (NCF) | 37% | Hospitality / travel | HARD-REJECT | Hospitality + non-US + below floor |
| Synergy Business Brokers | Admissions Consulting Practice (Global, Remote) | United States | $2.0M | $1.30M (NCF) | 65% | Services | HARD-REJECT | Below rev floor (disclosed-and-failed) |
| Synergy Business Brokers | Prominent 40-Year Pediatric Practice | New York | $5.83M | $1.65M (NCF) | 28% | Healthcare provider-owned | HARD-REJECT | Industry hard-exclude (physician-owned) + below floor |
| Synergy Business Brokers | Utility Support Construction Company | Nassau County, NY | $12M | $2.0M (NCF) | 17% | Construction | HARD-REJECT | Industry hard-exclude (construction) |
| Synergy Business Brokers | Growing Midwestern Trucking & Transportation Brokerage | Midwest | $9.0M | $1.65M (NCF) | 18% | Transportation services | HARD-REJECT | Below rev floor (disclosed-and-failed) |
| Synergy BB Real Estate | Event Rental Company: Full-Service | South Florida | $1.63M | $486K (NCF) | 30% | Event services | HARD-REJECT | Below $10M rev floor + below EBITDA floor |
| Synergy BB Real Estate | Short-Term Rental Property Mgmt Co (80+ Locations) | Midwest | $3.23M | $371K (NCF) | 11% | Vacation-rental property mgmt | HARD-REJECT | Below rev/EBITDA floor; STR mgmt ≠ HNW Estate Mgmt corpus |
| Synergy BB Real Estate | Groundwater Treatment Equipment Rental (SOLD) | Jacksonville, FL | $3.5M | $1.3M (NCF) | 37% | Equipment rental services | HARD-REJECT | Closed/sold — not available; below rev floor |
| Synergy BB Real Estate | Musical Instrument Rental & Repair Company (SOLD) | Union County, NJ | $2.35M | $284K (NCF) | 12% | Rental/repair services | HARD-REJECT | Closed/sold — not available; below floor |
| Synergy BB Real Estate | Property Management Company w/ Real Estate (SOLD) | Vermont | $1.56M | $299K (NCF) | 19% | Property management | HARD-REJECT | Closed/sold — not available; below floor |
| Synergy BB Real Estate | Real Estate Investment Company, Semi-Absentee (SOLD) | Harrisburg, PA | $2.37M | $395K (NCF) | 17% | Real estate investment | HARD-REJECT | Closed/sold — not available; below floor |
| Synergy BB Real Estate | Property Management Firm (SOLD) | NYC, New York | $600K | $300K (NCF) | 50% | Property management | HARD-REJECT | Closed/sold — not available; below floor |
| Synergy BB Real Estate | Real Estate Property Management Office (SOLD) | Ulster County, NY | $888K | undisclosed | undisclosed | Property management | HARD-REJECT | Closed/sold — not available; below floor |
| Empire Flippers | Religion & Spirituality – Amazon KDP | undisclosed | $369K (annlzd NP) | $369K | undisclosed | Amazon KDP digital | HARD-REJECT | Consumer DTC hard-exclude + below floor |
| Empire Flippers | Medical, News & Education – Digital/Info Product | undisclosed | $178K (annlzd NP) | $178K | undisclosed | Digital product | HARD-REJECT | Consumer DTC hard-exclude + below floor |
| Empire Flippers | Sports, Equipment, Hobbies – eCommerce | undisclosed | $181K (annlzd NP) | $181K | undisclosed | eCommerce | HARD-REJECT | Consumer DTC hard-exclude + below floor |
| Empire Flippers | Home (Pest Control) – Amazon FBA/eCommerce | undisclosed | $144K (annlzd NP) | $144K | undisclosed | Amazon FBA (pest-control product) | HARD-REJECT | Consumer DTC (product, not pest-mgmt service) |
| Empire Flippers | Health & Fitness, Home, Medical – Amazon FBA | undisclosed | $4.60M (annlzd NP) | $4.60M | undisclosed | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Culinary, Pet Care, Food & Beverages – Amazon FBA | undisclosed | $2.57M (annlzd NP) | $2.57M | undisclosed | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Pet Care – eCommerce | undisclosed | $4.11M (annlzd NP) | $4.11M | undisclosed | eCommerce / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Cryptocurrency – Digital/Newsletter/Service | undisclosed | $5.20M (annlzd NP) | $5.20M | undisclosed | Crypto digital media | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Lifestyle, Travel – eCommerce/Amazon FBA | undisclosed | $2.17M (annlzd NP) | $2.17M | undisclosed | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Home (Pest Control) – Amazon FBA | undisclosed | $1.91M (annlzd NP) | $1.91M | undisclosed | Amazon FBA (pest-control product) | HARD-REJECT | Consumer DTC (product, not pest-mgmt service) |
| Empire Flippers | Beauty, Health & Fitness – eCommerce/Amazon FBA | undisclosed | $1.53M (annlzd NP) | $1.53M | undisclosed | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Business, Digital Media – Service/Digital/Affiliate | undisclosed | $1.78M (annlzd NP) | $1.78M | undisclosed | Service + digital product | HARD-REJECT | Consumer DTC adjacency; not luxury-vertical |
| Empire Flippers | Supplements, Health & Fitness, Beauty – Amazon FBA | undisclosed | $1.39M (annlzd NP) | $1.39M | undisclosed | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Empire Flippers | Home, Romance – Amazon FBA/FBM/eCommerce | undisclosed | $1.47M (annlzd NP) | $1.47M | undisclosed | Amazon FBA / DTC | HARD-REJECT | Consumer DTC hard-exclude |
| Website Closers | SBA Pre-Qualified Amazon FBA eCommerce Brand | undisclosed | undisclosed | $955K (SDE) | undisclosed | eCommerce / DTC | HARD-REJECT | Industry hard-exclude (consumer retail/DTC) |
| Website Closers | AI Native SEO & Content Marketing Agency | undisclosed | undisclosed | $121K (SDE) | undisclosed | Marketing agency | HARD-REJECT | Below floor + marketing agency off-thesis |
| Website Closers | SBA Pre-Qualified Authenticated Collectibles eCommerce | undisclosed | undisclosed | $259K (SDE) | undisclosed | eCommerce / collectibles | HARD-REJECT | Industry hard-exclude (consumer retail/DTC) |
| Website Closers | SBA Pre-Qualified Lead Gen & Performance Marketing Agency | undisclosed | undisclosed | $847K (SDE) | undisclosed | Marketing / lead-gen agency | HARD-REJECT | Below floor + lead-gen off-thesis |
| Website Closers | SBA Pre-Qualified SaaS – Customer Feedback Platform | undisclosed | undisclosed | $211K (SDE) | undisclosed | Horizontal SaaS | HARD-REJECT | Horizontal SaaS hard-exclude + ARR likely <$3M |
| Website Closers | SBA Pre-Qualified Luxury RV & Coach Marketplace | undisclosed | undisclosed | $594K (SDE) | undisclosed | B2B marketplace (RV) | HARD-REJECT | Below floor; consumer-RV marketplace off-thesis |
| Website Closers | 67-Year Cayman Islands Architectural Design Firm | Cayman Islands | undisclosed | $387K (SDE) | undisclosed | Architecture / design | HARD-REJECT | Non-US + below floor + design/construction |
| Website Closers | Towels & Socks eCommerce Brand | undisclosed | undisclosed | $526K (SDE) | undisclosed | eCommerce / retail | HARD-REJECT | Industry hard-exclude (consumer retail/DTC) |
| Website Closers | SBA Pre-Qualified Procurement Services & Distribution | undisclosed | undisclosed | $200K (SDE) | undisclosed | Distribution / services | HARD-REJECT | Below rev/EBITDA floor |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 30 | 0 | — |
| DealForce | General (email) | active | — | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 14 | 0 | — |
| Everingham & Kerr | General (email) | active | — | 0 | 0 | — |
| Flippa | General (email) | active | — | 0 | 0 | — |
| IAG M&A Advisors | General (email) | active | — | 0 | 0 | — |
| Quiet Light | General (email) | active | — | 0 | 0 | — |
| Rejigg | General (email) | active | — | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General (email) | active | — | 0 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Viking Mergers | General (email) | active | — | 0 | 0 | — |
| Website Closers | General | active | 200 | 12 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | blocked (verified) | 404 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 10 | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 | 0 | — |

**Notes on blocked status:**
- **BizBuySell** — `blocked (verified)`: WebFetch returned HTTP 403 on two distinct paths (`/businesses-for-sale/` and `/north-east-businesses-for-sale/`). agent-browser fallback unavailable on this VPS (`agent-browser: command not found`). Two attempts → verified. `BROWSER_AUTOMATION_UNAVAILABLE` infra gap surfaced.
- **GP Bullhound** — `blocked (verified)`: WebFetch returned HTTP 404 on three path attempts (`/transactions/`, `/transactions`, `/news/`). Site likely restructured or JS-rendered; agent-browser fallback unavailable. Surfaced for path re-verification + agent-browser install.
- **Email-channel sources** (DealForce, Everingham & Kerr, Flippa, IAG M&A, Quiet Light, Rejigg, SMB Deal Hunter, Viking Mergers) marked `active`: today's `email-scan-results-2026-05-18.md` was present and parsed; email-intelligence reported zero deal-bearing inbound (no CIM/NDA/teaser/blast with listing keywords). Channels scanned via the artifact, 0 listings — not blocked.
- **Last Match Date** `—` for all: fingerprint store had 0 records at scan start (1 record added this run for the DealsX lead, which is not a platform listing).
- **Non-Active tiers not in scorecard** (per stop hook, only Status:Active sources require rows): Acquire.com / Axial / BizScout / Kumo / FE International (pending registration, login-gated); Benchmark International / Searchfunder / Paine Pacific / Woodbridge-Mariner (dormant / no public listings); Agency Checklists, Anticimex, CMM Online, IA Magazine, Inside Self-Storage, MarshBerry, MidCap Advisors, Reagan Consulting (intel-only, no Slack); Cetane, Exit Strategies Group, Software Equity Group, Tyton Partners, Calder Capital, Green Bridge Advisors, Keystone Business Advisors, Union Square Advisors (weak / not-yet-scanning); Private Art Advisory + Specialty Coffee Equipment Service = confirmed structural source GAPs.

**Niche corpus path used (per Step 0c):**
- Premium Pest Management → DealsX keywords (Specialty Pest & Environmental Management Services)
- Private art advisory firms → WR row enrichment (DealsX Niche blank; Niche Hypothesis + Quick notes: "art advisory / art advisor / private advisory / art consulting / collection-strategy retainers")
- Estate Management Companies → DealsX keywords (Estate Management Companies)
- Specialty Coffee Equipment Service → DealsX keywords (Specialty Commercial Equipment Services)
- High-End Commercial Cleaning → DealsX keywords (High-End Commercial Cleaning)
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DealsX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DealsX keywords (Specialty Insurance Brokerage)
- Storage & Related Services for High Value Assets → DealsX keywords (Specialty Storage & Handling for High-Value Collections)

## Volume Check

- Deals surfaced today: 1 (DealsX inbound reply — Greg Bruyere / Tristate; 0 platform/email PASS)
- 7-day rolling average: <1 (fingerprint store was empty pre-run; 5/13–5/15 artifacts recorded 0 platform PASS/day)
- Target: 1-3/day — BELOW TARGET (platform/email yield 0)

Drivers: (1) public marketplace inventory today is the same off-thesis skew as recent runs — construction / healthcare-provider / consumer-DTC / non-US / sub-floor dominate; eight listings cleared a financial gate but matched no active-niche corpus (luxury / high-value-asset services thesis). (2) BizBuySell blocked (verified) and GP Bullhound 404 across three paths — agent-browser dependency still unmet on this VPS, capping general + SaaS-niche coverage. (3) Email channels carried zero deal-bearing inbound this window. (4) Only inbound flow today is the DealsX proprietary reply (St. Louis), which is a contact handoff routed to outreach-manager, not a screened buy-box deal. Infra follow-ups for Kay/launchd-debugger: install agent-browser; port `deal-aggregator-fingerprint.sh` cutoff off BSD `date -v`.
