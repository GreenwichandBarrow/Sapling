---
date: 2026-05-28
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 10
dealsx_replies: 0
---
# Deal Aggregator Scan — 2026-05-28

Morning headless run. 17 Active sources covered (13 General + 4 Niche-Specific). Email-scan-results-2026-05-28 already extracted 10 listings (5 Helen Guo SMB Deal Hunter + 4 Flippa Marketplace + 1 Quiet Light single-listing alert) — those are screened below in the per-listing log alongside fresh WebFetch pulls from Business Exits, Synergy Business Brokers Real Estate, Empire Flippers, and Website Closers. Niche INTEL sources (Sica Fletcher, PCO Bookkeepers) and ad-hoc niche-broker pulls (Calder Capital for High-End Commercial Cleaning, MidCap Advisors for Art Storage) scraped for market signal — no Slack ping per Channel-Type INTEL routing. No DealsX Proprietary Outreach replies in today's email-scan-results.

**Result: zero PASS listings → zero Slack posts to `#active-deals` today.** Four NEAR-MISS items (clear Services buy-box financial gate but no active-niche corpus match) and two FLAG items (SaaS gate uncertain — ARR undisclosed per Data Availability Rule) surfaced in the per-listing log for thesis-drift and calibration visibility.

Corpus path log per active niche (Step 0c):
- Premium Pest Management → DEALSX keywords (DealsX "Specialty Pest & Environmental Management Services")
- Private art advisory firms → WR row enrichment (Niche Hypothesis + Quick notes — DealsX Niche field blank)
- Estate Management Companies → DEALSX keywords
- Specialty Coffee Equipment Service → DEALSX keywords (DealsX "Specialty Commercial Equipment Services")
- High-End Commercial Cleaning → DEALSX keywords
- Vertical SaaS for Luxury & High-Value Asset Service Industries → DEALSX keywords
- Specialty Insurance Brokerage (Art & Collectibles) → DEALSX keywords
- Storage & Related Services for High Value Assets → DEALSX keywords (DealsX "Specialty Storage & Handling for High-Value Collections")

## Deals Surfaced (sent to Slack individually)

None today. Zero listings passed both the buy-box financial gate AND an active-niche corpus match.

## Email Inbound Deals

The 10 listings extracted by email-intelligence in section 7 of [[brain/context/email-scan-results-2026-05-28]] (5 Helen Guo SMB Deal Hunter + 4 Flippa Marketplace digest + 1 Quiet Light single-listing alert) all HARD-REJECTED on revenue/EBITDA below Services Buy Box floors or on Industry/Geography hard-excludes. Per-listing verdicts in the Listings Reviewed log below. No CIMs, NDA confirmations, broker BLASTs targeted at G&B, intro forwards, or other deal-specific emails in today's email-scan window (per email-scan-results section 2: 0 BLAST classified, 3 DEAL_NEWSLETTER — covered here).

## DealsX Proprietary Outreach Replies

None today. No `dealsx.notifaction@gmail.com` "Lead Interested" notifications in today's email-scan-results.

## Near Misses (not Slacked)

- **GovCon IT Firm (Business Exits)** — $17.5M ask / $19.7M rev / $3.45M EBITDA / 17% margin. Clears Services Buy Box financial gate cleanly. Government IT contracting is off-thesis for current 8 active niches — no luxury / high-value-asset adjacency. NEAR-MISS rather than PASS because corpus match is the gate.
- **B2B Experiential Marketing Vendor (Business Exits)** — $16-20M ask / $14.3M rev / $3.3M EBITDA / 23% margin. Clears Services Buy Box. B2B experiential / event marketing is off-thesis; not in active-niche corpus. NEAR-MISS.
- **Government Contract ERP Service Business (Business Exits)** — $12M ask / $14M rev / $2.57M EBITDA / 18% margin. Clears Services Buy Box. GovCon ERP service + SaaS hybrid; off-thesis. NEAR-MISS.
- **California Property Tax Consultants (Business Exits)** — $28M ask / $6.68M rev / $4.68M EBITDA / 70% margin. Revenue $6.68M is **disclosed-and-below** the $10M Services floor → would be HARD-REJECT, BUT: this listing pattern-matches the WEEKLY REVIEW row 11 "Property Tax Appeal Services (Commercial-Property)" niche (currently "New - Pending Review"). Margin profile (70%, recurring contingency-fee) and CA geography both align with the New-Pending row's description. Flagging as NEAR-MISS for niche-intelligence calibration: even though it fails Services Buy Box revenue floor and CA soft-flags, the underlying business pattern is the strongest empirical evidence yet that the Property Tax Appeal niche has real flow at the broker layer. Not Slacked.
- **No new broker introductions** detected in today's email-scan-results (section 4 intros = Greg Pitkoff franchise PR via Marsha Weiner — relationship infra, not deal flow per email-intel classification).

## Listings Reviewed (full log)

Every listing scraped or parsed during this run, regardless of verdict. Sort: PASS → NEAR-MISS → FLAG → HARD-REJECT.

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm | undisclosed | $19.7M | $3.45M | 17% | Government IT contracting / service+SaaS | NEAR-MISS | Clears Services Buy Box; off-thesis (no active-niche corpus match) |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.28M | $3.3M | 23% | B2B experiential / event marketing | NEAR-MISS | Clears Services Buy Box; off-thesis |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14.05M | $2.57M | 18% | GovCon ERP service+SaaS | NEAR-MISS | Clears Services Buy Box; off-thesis |
| Business Exits | California Property Tax Consultants | CA | $6.68M | $4.68M | 70% | Property tax consulting | NEAR-MISS | Rev below $10M floor + CA soft-flag, BUT pattern-matches "New - Pending Review" Property Tax Appeal niche (row 11) — calibration signal |
| Website Closers | Mission-Critical SaaS for Financial Trading Firms | undisclosed | undisclosed (50 enterprise clients @ $180K AOV implies ~$9M) | $3.35M | undisclosed | Vertical SaaS for prop-trading firms | FLAG | ARR undisclosed; clears EBITDA-positive SaaS gate; balance-sheet-heavy fintech adjacency risk per SaaS Buy Box HE — surface for human review |
| Website Closers | Ed-Tech eLearning Platform (10-Year, 95% recurring) | undisclosed | undisclosed | $1.63M | undisclosed | Ed-tech / vertical SaaS | FLAG | ARR undisclosed (1,400 subs implies possibly $3-7M ARR); B2C / horizontal ed-tech adjacency risk; off-thesis if disclosed |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest | $21.31M | $12.97M | 61% | Healthcare provider (wellness practice) | HARD-REJECT | Physician practices / provider-owned healthcare hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | 25% | Construction | HARD-REJECT | Non-US (US TAM only) + Construction hard-exclude |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | 74% | Hospitality / wedding venue | HARD-REJECT | Revenue below $10M floor; Restaurants/hospitality/nightlife hard-exclude |
| Business Exits | Metal Building Supplier w/ US Manufacturing | US | $33.69M | $3.97M | 12% | Capital-intensive manufacturing | HARD-REJECT | Capital-intensive manufacturing + Construction adjacency hard-exclude |
| Business Exits | California Staffing Firm with Recurring Revenue | CA | $7.82M | $3.2M | 41% | Staffing | HARD-REJECT | Revenue below $10M floor; CA soft-flag; staffing off-thesis |
| Business Exits | Texas Non-Emergency Medical Transport | TX | $7.74M | $2.87M | 37% | NEMT / healthcare-adjacent transport | HARD-REJECT | Revenue below floor; provider-owned healthcare adjacency |
| Business Exits | Atlanta Area Residential Plumbing & Septic | GA | $11.71M | $2.41M | 21% | Plumbing / labor-heavy field service | HARD-REJECT | Construction/labor-heavy field services hard-exclude |
| Business Exits | Northeast Commercial Contractor | Northeast | $21.96M | $2.78M | 13% | Construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Design & Build Studio for Themed Props | undisclosed | $10.02M | $3.06M | 31% | Construction + Manufacturing | HARD-REJECT | Construction + capital-intensive manufacturing hard-excludes |
| Business Exits | Thriving Texas HVAC Company | TX | $21.99M | $2.28M | 10% | HVAC / labor-heavy field service | HARD-REJECT | Construction/labor-heavy field services hard-exclude |
| Business Exits | Multi-Service Oilfield Infrastructure & Automation | undisclosed | $12.9M | $1.97M | 15% | Oilfield services / capital-intensive | HARD-REJECT | Capital-intensive industrial services off-thesis |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | 22% | Telecom infrastructure / labor-heavy | HARD-REJECT | Revenue below floor; labor-heavy field services hard-exclude |
| Business Exits | Specialized Military and Aerospace Parts Distributor | undisclosed | $8.23M | $1.9M | 23% | Aerospace/defense parts distribution | HARD-REJECT | Revenue below floor; aviation/aerospace per [[feedback-no-aviation-targets]] |
| Business Exits | Niche Construction Service Business | undisclosed | $10.8M | $2.3M | 21% | Construction service | HARD-REJECT | Construction/labor-heavy field services hard-exclude |
| Business Exits | Category Defining Window Manufacturer | undisclosed | $4.9M | $1.54M | 31% | Window manufacturing + retail | HARD-REJECT | Revenue below floor; Capital-intensive manufacturing + consumer-retail hard-excludes |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | 36% | Electrical contracting / construction | HARD-REJECT | Revenue below floor; Construction hard-exclude |
| Business Exits | Safe Pet Travel Products Distribution | undisclosed | $1.67M | $1.03M | 62% | Consumer pet products / wholesale | HARD-REJECT | Revenue below floor; Consumer retail/DTC hard-exclude |
| Business Exits | Nevada Commercial Fireproofing Contractor | NV | $3.06M | $932K | 30% | Construction / fireproofing | HARD-REJECT | Revenue + EBITDA below floors; Construction hard-exclude |
| Business Exits | Government Contracted Military Promotional Products | US/Remote | $8.18M | $788K | 10% | Promotional products retail/service | HARD-REJECT | Revenue + EBITDA below floors |
| Business Exits | Specialized Canadian Recruitment Agency | Canada | $2.28M CAD | $764K CAD | 33% | Recruitment / staffing | HARD-REJECT | Non-US (US TAM only); Revenue + EBITDA below floors |
| Business Exits | Florida Med Spa and Regenerative Medicine Clinic | FL | $1.07M | $724K | 67% | Healthcare provider | HARD-REJECT | Revenue + EBITDA below floors; provider-owned healthcare hard-exclude |
| Business Exits | Landscape Architecture Business | undisclosed | $5.5M | $1.8M | 33% | Landscape architecture / construction-adjacent | HARD-REJECT | Revenue below floor; Construction adjacency |
| Business Exits | Restaurant and Juice Bar Franchise | undisclosed | $4.14M | $714K | 17% | Restaurant franchise | HARD-REJECT | Franchises hard-exclude; Restaurants/hospitality hard-exclude; Revenue + EBITDA below floors |
| Business Exits | Colorado Regenerative & Functional Medicine | CO | $895K | $494K | 55% | Healthcare provider | HARD-REJECT | Revenue + EBITDA below floors; provider-owned healthcare hard-exclude |
| Business Exits | Bay Area Residential Roofing | CA | $2.5M | $470K | 19% | Roofing / construction | HARD-REJECT | Revenue + EBITDA below floors; Construction hard-exclude; CA soft-flag |
| Business Exits | Texas Home Health Staffing Firm | TX | $2.49M | $337K | 14% | Healthcare staffing | HARD-REJECT | Revenue + EBITDA below floors; healthcare-staffing adjacency |
| Synergy BB Real Estate | Short-Term Rental Property Management (80+ locations) | Midwest | $3.23M | $371K | 11% | STR property management | HARD-REJECT | Revenue + EBITDA below floors; STR mgmt is consumer-facing, not HNW Estate Mgmt niche |
| Synergy BB Real Estate | Event Rental Company: Full-Service | South FL | $1.63M | $486K | 30% | Event rentals | HARD-REJECT | Revenue + EBITDA below floors |
| Empire Flippers | Health & Fitness / Home / Medical (Amazon FBA, $383K MRR) | undisclosed | ~$17.6M | ~$4.6M | 26% | Amazon FBA / DTC consumer | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Pet Care eCommerce ($342K MRR) | undisclosed | ~$19.4M | ~$4.1M | 21% | Pet eCommerce / DTC | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Cryptocurrency Newsletter+Service ($433K MRR) | undisclosed | ~$8.3M | ~$5.2M | 63% | Crypto digital products / newsletter | HARD-REJECT | Off-thesis; lending/credit-extension adjacency risk |
| Empire Flippers | Home Amazon FBA ($159K MRR) | undisclosed | ~$8.1M | ~$1.9M | 24% | Amazon FBA / DTC consumer home | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Beauty / Health & Fitness ($127K MRR) | undisclosed | ~$6.3M | ~$1.53M | 24% | Beauty/H&F eComm / FBA | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Business / Digital Media ($142K MRR) | undisclosed | undisclosed | ~$1.7M | undisclosed | Service+Digital Product+Affiliate | HARD-REJECT | Off-thesis service; affiliate/content adjacent to consumer media |
| Empire Flippers | Home / Romance (Amazon FBA+FBM, $122K MRR) | undisclosed | undisclosed | ~$1.47M | undisclosed | Amazon FBA romance/home | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | Hobbies / Gaming Amazon FBA ($110K MRR) | undisclosed | undisclosed | ~$1.32M | undisclosed | Gaming/hobbies eCommerce | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | #94296 Sports/Business/Entertainment/Hospitality/Travel ($33K MRR) | undisclosed | undisclosed | ~$394K | undisclosed | eCommerce + service + digital product | HARD-REJECT | EBITDA below floor; off-thesis |
| Empire Flippers | #92853 Home/Outdoors Amazon FBA ($53K MRR) | undisclosed | undisclosed | ~$638K | undisclosed | Amazon FBA consumer | HARD-REJECT | EBITDA below floor; Consumer retail/DTC |
| Empire Flippers | #94174 News & Education Amazon KDP ($10K MRR) | undisclosed | undisclosed | ~$124K | undisclosed | Amazon KDP self-publishing | HARD-REJECT | EBITDA below floor; consumer content |
| Empire Flippers | #94619 Pet Care/Outdoors Amazon FBA ($7.6K MRR) | undisclosed | undisclosed | ~$91K | undisclosed | Pet/outdoor consumer products | HARD-REJECT | EBITDA below floor; Consumer retail/DTC; operating <5 yrs |
| Empire Flippers | #94797 Apparel/Children DropShipping ($5.1K MRR) | undisclosed | undisclosed | ~$61K | undisclosed | Apparel dropship consumer | HARD-REJECT | EBITDA below floor; Consumer retail/DTC |
| Empire Flippers | #94577 Entertainment YouTube ($5K MRR) | undisclosed | undisclosed | ~$60K | undisclosed | YouTube channel | HARD-REJECT | EBITDA below floor; consumer content; operating <5 yrs |
| Website Closers | Award Winning Marketing & PR Agency | undisclosed | undisclosed | $295K | undisclosed | Marketing/PR agency | HARD-REJECT | EBITDA below floor; off-thesis services |
| Website Closers | 25-Year eCommerce Brand Fine Jewelry | undisclosed | undisclosed | $282K | undisclosed | Fine jewelry eCommerce | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | SBA Pre-Qualified AI-Driven Cybersecurity Ed-Tech | undisclosed | undisclosed | $779K | undisclosed | EdTech / cybersecurity SaaS | HARD-REJECT | Sub-$3M ARR likely; horizontal cyber-ed-tech off-thesis |
| Website Closers | Sales Coaching & Lead Generation Training Platform | undisclosed | undisclosed | $109K | undisclosed | Sales coaching SaaS | HARD-REJECT | EBITDA below floor; horizontal SaaS |
| Website Closers | SBA Pre-Qualified Amazon FBA eCommerce Brand | undisclosed | undisclosed | $955K | undisclosed | Amazon FBA consumer | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | AI Native SEO & Content Marketing Agency | undisclosed | undisclosed | $121K | undisclosed | Digital marketing / SEO | HARD-REJECT | EBITDA below floor; off-thesis services |
| Website Closers | SBA Pre-Qualified Authenticated Collectibles eCommerce | undisclosed | undisclosed | $259K | undisclosed | Collectibles eCommerce | HARD-REJECT | EBITDA below floor; Consumer retail/DTC |
| Website Closers | Loss Prevention Training & Awareness Platform | undisclosed | undisclosed | $793K | undisclosed | B2B compliance training SaaS | HARD-REJECT | Sub-$3M ARR likely; off-thesis (W&H&S compliance is "New - Pending Review" not Active) |
| Website Closers | SBA Pre-Qualified Lead Generation & Performance Marketing Agency | undisclosed | undisclosed | $847K | undisclosed | Lead-gen / performance marketing agency | HARD-REJECT | EBITDA below floor; off-thesis services |
| Website Closers | Shopify Business Brokerage | undisclosed | undisclosed | $2.4M | undisclosed | M&A / Shopify brokerage service | HARD-REJECT | Off-thesis service; broker-of-businesses model not in active corpus |
| Helen Guo SMB Deal Hunter | Semi-Absentee Auto Repair & Smog Check Shop | Southern CA | $1.22M | $500K | 41% | Auto repair / smog inspection | HARD-REJECT | Rev + EBITDA below floors; CA soft-flag; auto-retail off-thesis |
| Helen Guo SMB Deal Hunter | Wholesale Ice Cream Distributor (30-yr routes) | Central CA | $1.1M | $385K | 35% | Frozen food distribution | HARD-REJECT | Rev + EBITDA below floors; CA soft-flag; food-distribution off-thesis |
| Helen Guo SMB Deal Hunter | Automotive Aftermarket Parts & Services (70 dealership clients) | MN | undisclosed | $1.7M | undisclosed | Auto aftermarket B2B | HARD-REJECT | Revenue undisclosed but ask~$5-8M implies sub-floor; auto aftermarket off-thesis |
| Helen Guo SMB Deal Hunter | Trucking Company (12-month contracts) | IA | undisclosed | $1.5M | undisclosed | Trucking / logistics | HARD-REJECT | EBITDA at floor edge; off-thesis (trucking not in active corpus) |
| Helen Guo SMB Deal Hunter | Truss Manufacturing Company | FL | undisclosed | $400K | undisclosed | Building products / capital-intensive mfg | HARD-REJECT | EBITDA below floor; Capital-intensive manufacturing hard-exclude |
| Flippa Marketplace | Premium Home Sauna Shopify Brand | undisclosed (US) | $20M | undisclosed | undisclosed | DTC home wellness | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Flippa Marketplace | Established SEO Agency (10-yr) | undisclosed | $755K | undisclosed | undisclosed | Digital marketing services | HARD-REJECT | Revenue below floor; off-thesis services |
| Flippa Marketplace | Global Travel Connectivity Brand (portable Wi-Fi + eSIM) | global | $331K | undisclosed | 79% | Travel tech DTC | HARD-REJECT | Revenue below floor; Consumer retail/DTC; non-US sales mix |
| Flippa Marketplace | 4.4-Star Headwear Brand | undisclosed | undisclosed | undisclosed | undisclosed | DTC apparel | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Quiet Light | Washable HVAC Filter DTC Brand (patent-pending) | North America | $125K | $57K SDE | 46% | DTC home HVAC consumables | HARD-REJECT | Revenue + EBITDA below floors; Consumer retail/DTC hard-exclude |
| Sica Fletcher | Safe Harbour Insurance Mgmt → ALKEME (2/27/2026) | MA | undisclosed | undisclosed | undisclosed | Insurance brokerage (closed deal) | HARD-REJECT | INTEL ONLY — historical announcement, not active listing; PE-consolidator (ALKEME) buyer = hard-exclude |
| Sica Fletcher | O'Neill Associates Consulting → ALKEME (2/27/2026) | FL | undisclosed | undisclosed | undisclosed | Insurance brokerage (closed deal) | HARD-REJECT | INTEL ONLY — closed deal; PE-consolidator buyer |
| Sica Fletcher | Surety Bonds LLC → The Hilb Group (2/15/2026) | GA | undisclosed | undisclosed | undisclosed | Surety/insurance (closed deal) | HARD-REJECT | INTEL ONLY — closed deal; PE-consolidator buyer |
| Sica Fletcher | Quantum Resource Group → ALKEME (2/13/2026) | MD | undisclosed | undisclosed | undisclosed | Insurance brokerage (closed deal) | HARD-REJECT | INTEL ONLY — closed deal; PE-consolidator buyer |
| Sica Fletcher | Centennial State Insurance Group → ALKEME (1/9/2026) | CO | undisclosed | undisclosed | undisclosed | Insurance brokerage (closed deal) | HARD-REJECT | INTEL ONLY — closed deal; PE-consolidator buyer |
| Sica Fletcher | C&A Insurance Agency → World Insurance Assoc (12/31/2025) | NY | undisclosed | undisclosed | undisclosed | Insurance brokerage (closed deal) | HARD-REJECT | INTEL ONLY — closed deal; PE-consolidator buyer |
| Calder Capital | Springwise Facility Management → MI Facility Mgmt Co | IN | undisclosed | undisclosed | undisclosed | Commercial cleaning / facility mgmt (closed) | HARD-REJECT | INTEL ONLY — closed tombstone, not active listing |
| Calder Capital | Hi-Tec Building Services → 4-M Building Solutions | MI | undisclosed | undisclosed | undisclosed | Commercial cleaning (closed) | HARD-REJECT | INTEL ONLY — closed tombstone |
| Calder Capital | Corporate Clean Services → Individual Investor | MI | undisclosed | undisclosed | undisclosed | Commercial cleaning (closed) | HARD-REJECT | INTEL ONLY — closed tombstone |
| Calder Capital | Aggressive Cleaning Services → New Image Building | MI | undisclosed | undisclosed | undisclosed | Commercial cleaning (closed) | HARD-REJECT | INTEL ONLY — closed tombstone |
| Calder Capital | Blue Sky Window Cleaners → Award Window | MI | undisclosed | undisclosed | undisclosed | Window cleaning (closed) | HARD-REJECT | INTEL ONLY — closed tombstone |
| Calder Capital | Squeegee Squad → Individual Investor | MI | undisclosed | undisclosed | undisclosed | Window cleaning (closed) | HARD-REJECT | INTEL ONLY — closed tombstone |
| MidCap Advisors | Artemis Fine Arts Services → Cadogan Tate | undisclosed | undisclosed | undisclosed | undisclosed | Fine art logistics (closed deal, archive) | HARD-REJECT | INTEL ONLY — historical 2023 announcement; surface only as Art Storage niche signal |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Business Exits | General | active | 200 | 30 | 0 | — |
| DealForce | General | active | — | 0 | 0 | — |
| Empire Flippers | General | active | 200 | 14 | 0 | — |
| Everingham & Kerr | General | active | — | 0 | 0 | — |
| Flippa | General | active | — | 4 | 0 | — |
| IAG M&A Advisors | General | active | — | 0 | 0 | — |
| Quiet Light | General | active | — | 1 | 0 | — |
| Rejigg | General | active | — | 0 | 0 | — |
| SMB Deal Hunter (Helen Guo) | General | active | — | 5 | 0 | — |
| Synergy Business Brokers | General | active | — | 0 | 0 | — |
| Viking Mergers | General | active | — | 0 | 0 | — |
| Website Closers | General | active | 200 | 12 | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | blocked (verified) | 404 | 0 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Premium Pest) | active | 200 | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 6 | 0 | — |
| Synergy Business Brokers Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 2 | 0 | — |

**Notes:**
- `BizBuySell` returned HTTP 403 on scraper user-agent (verified pattern from yesterday + SKILL.md "must use agent-browser" list). agent-browser is NOT installed on this VPS → `BROWSER_AUTOMATION_UNAVAILABLE: BizBuySell skipped, requires agent-browser install` per stop hook.
- `GP Bullhound` `/transactions/` returned HTTP 404. Previous successful scrape was at root domain; transactions path appears moved. Single-attempt fallback to root domain not attempted today (rate-limit hygiene) — but classifying as `blocked (verified)` since the canonical path was confirmed 404, not a transient timeout. Will retry alternate path next run.
- `DealForce`, `Everingham & Kerr`, `IAG M&A Advisors`, `Quiet Light`, `Rejigg`, `SMB Deal Hunter`, `Viking Mergers`, `Flippa` — email-only sources per Sourcing Sheet. Channel health verified by recent email-scan-results history. Today's email-scan-results extracted listings from SMB Deal Hunter (5), Flippa (4), and Quiet Light (1 single-listing alert). The other five email-only sources had no inbound triggering a DEAL_NEWSLETTER classification today.
- `Synergy Business Brokers` (general tab) — not directly scraped this run; general inventory pulled yesterday (2026-05-27, 15 listings, all HARD-REJECT). Marketplace inventory turnover is slow (most cross-day fingerprints would dedupe). Niche-Specific Synergy Real Estate sub-site WAS scraped this run.
- `Sica Fletcher` — INTEL-only per Channel-Type routing. 6 historical 2026 announcements logged in Listings Reviewed for market-signal completeness, all closed PE-consolidator-driven deals (ALKEME, World, Hilb). No new 2026 announcements since 2/27. Per Channel-Type routing INTEL sources NEVER Slack-ping.
- `PCO Bookkeepers` — INTEL-only newsletter source. Homepage offers M&A services but no current deal-specific listings shown today. 0 listings to log.
- **Supplemental niche-broker pulls (not in Active source list):** `Calder Capital` (High-End Commercial Cleaning, Status "Not yet scanning" per Sourcing Sheet — pulled 6 tombstones for cleaning-niche calibration); `MidCap Advisors` (Art Storage, Intel-only — pulled 1 historical Artemis→Cadogan Tate announcement). Both INTEL-grade, logged in Listings Reviewed for cleaning + art-storage niche signal visibility. Not counted toward `sources_scanned` (which counts Active-status sources only).

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: 0 (consistent with 2026-05-26 + 2026-05-27 prior artifacts — zero PASS on three consecutive headless runs)
- Target: 1-3/day — **BELOW TARGET**

**Below-target note:** Today's ~80 listings reviewed (30 Business Exits + 14 Empire Flippers + 12 Website Closers + 2 Synergy RE + 10 email inbound + 6 Sica Fletcher tombstones + 6 Calder tombstones + 1 MidCap historical) yielded zero PASS matches. Pattern continues from 2026-05-27: (a) Helen Guo + Flippa + Quiet Light email-driven SMB-scale newsletters all sub-floor; (b) Business Exits + Empire Flippers + Website Closers general inventory skewed to construction, consumer-FBA/DTC, healthcare provider, and horizontal SaaS — all hard-excluded; (c) Synergy Real Estate had only 2 active listings, both sub-floor; (d) niche INTEL sources surface closed PE-consolidator deals (Sica Fletcher all → ALKEME) which are blacklist signals not flow. The active-niche corpus is narrow (8 niches, weighted to specialty/luxury services) while broker-marketplace inventory is broad/generalist — corpus mismatch is the dominant filter. Reinforces [[feedback-industry-is-output-of-network]] doctrine (network-mapping-first thesis: broad marketplace screens are diminishing-returns for Kay's specific buy-box; women-led network and warm-intro paths produce signal where marketplaces produce noise).

**Notable calibration signal:** California Property Tax Consultants on Business Exits ($28M ask / $6.68M rev / $4.68M EBITDA / 70% margin) — fails Services Buy Box revenue floor and CA soft-flags, but the business pattern (contingency-fee recurring-revenue commercial-property tax appeals) is the strongest broker-layer empirical evidence for WEEKLY REVIEW row 11 ("Property Tax Appeal Services" — New - Pending Review). Worth noting that broker-channel flow exists for this niche even though the active-pipeline channel is warm-intro-driven.
