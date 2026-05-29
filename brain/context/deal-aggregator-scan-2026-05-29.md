---
date: 2026-05-29
deals_found: 0
sources_scanned: 30
sources_blocked_verified: 1
sources_blocked_single_attempt: 2
email_deals: 2
dealsx_replies: 0
---
# Deal Aggregator Scan — 2026-05-29

Morning (full) run. 22 sources fetched directly + 8 email-driven channels checked via email-intelligence artifact. 78 marketplace listings scraped + 21 email-BLAST listings parsed = **99 for-sale listings reviewed**. **0 thesis matches.** Every for-sale listing failed a disclosed financial floor, hit an industry/geography hard-exclude (B2C / restaurant / construction / healthcare-provider / lending / non-US / franchise / DTC eCommerce), or sat off the active luxury/HNW thesis. 4 generic B2B-services listings cleared the financial bands but matched no active niche → logged as Near Misses (not Slacked). No CIMs, no NDAs, no DealsX outreach replies today.

**Infra gap surfaced:** `agent-browser` is NOT installed on this VPS → BizBuySell (403) and Cetane (403) could not be retried and are marked `blocked (single-attempt)`. BizBuySell is the largest LMM platform; recommend installing `agent-browser` (`npm i -g agent-browser && agent-browser install`) to unblock it on future runs. (Per `feedback_test_before_concluding_channel_dead`, not marked verified-dark — only one attempt was possible.)

## Deals Surfaced (sent to Slack individually)
None today. 0 listings cleared the buy-box gate AND matched an active niche corpus. Fingerprint store unchanged (no new Slack posts).

## Email Inbound Deals
2 broker BLASTs processed via email-intelligence (`email-scan-results-2026-05-29.md`, Section 7); decomposed into 21 per-listing rows (logged below). **No CIM, no NDA/CIM attachment, no Active-Deal fast-path** this run.
1. **Everingham & Kerr** — BLAST | 1 listing (Southern NJ residential landscaping, $1M rev / ~$300K cash flow) | sub-box, B2C/labor-heavy → HARD-REJECT
2. **Transworld / Samuel Curcio** — BLAST | 20 listings (Suffolk/NY/CT/MA/PA cluster) | predominantly B2C (restaurants, spas, salons, auto), sub-box SDE, or hard-exclude (legal funding = lending) → all HARD-REJECT

## DealsX Proprietary Outreach Replies
None today. No `Prospect Geni <dealsx.notifaction@gmail.com>` / "Lead Interested" notifications or forwarded `@dealsx.io` owner replies in today's email-scan artifact.

## Near Misses (not Slacked)
Cleared the buy-box financial gate but matched no active-niche corpus — generic out-of-thesis B2B services. Logged for thesis-drift / corpus-tuning calibration only; per skill, random-industry one-offs are not Slacked.
- **GovCon IT Firm** (Business Exits) — $19.7M rev / $3.45M EBITDA / 18% — government-contract IT services, off luxury/HNW thesis.
- **B2B Experiential Marketing Vendor** (Business Exits) — $14.28M / $3.30M / 23% — B2B marketing services, off-thesis.
- **Government Contract ERP Service** (Business Exits) — $14.05M / $2.57M / 18% — GovCon ERP/IT services, off-thesis.
- **LED Display Solutions** (Synergy) — $11.19M / $4.63M cash flow / 41%, FL — tech/distribution; clears bands but install-heavy and off-thesis.

**Intel signals (advisory closed-deal announcements — not for-sale listings, not logged as rows):**
- Insurance brokerage consolidation remains intensely aggregator-crowded (Sica Fletcher ~30 closed deals + MarshBerry + Agency Checklists Jan–May 2026: ALKEME, Risk Strategies, Hilb, Acrisure, World, Higginbotham, Baldwin, Trucordia). Relevant as exit-channel/competitor intel for the Specialty Insurance niche, not deal flow — all PE-backed serial consolidators.
- Pest: Anticimex (EQT-backed) confirms strong strategic-acquirer appetite for owner-operated pest businesses (200+ acquisitions); recent named targets foreign, no US targets disclosed.
- Art-logistics comp: MidCap Advisors — Artemis Fine Arts Services acquired by Cadogan Tate (usable comp for the High-Value Asset Storage / art-logistics thesis).
- Self-storage M&A is all institutional/REIT-scale ($1B+, above buy-box); no specialty/wine/art storage niche deals named.

## Listings Reviewed (full log)

99 for-sale listings parsed this run. Sorted PASS → NEAR-MISS → FLAG → HARD-REJECT. (Advisory closed-deal announcements from Sica Fletcher / GP Bullhound / Software Equity and the intel-only group are market signals, not for-sale listings — captured under Near Misses → Intel signals and counted in the Source Scorecard, not logged as rows here.)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Business Exits | GovCon IT Firm | National | $19.7M | $3.45M | 18% | GovCon IT services | NEAR-MISS | Clears services gate; no active-niche match (off luxury/HNW thesis) |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.28M | $3.30M | 23% | B2B marketing services | NEAR-MISS | Clears gate; off-thesis |
| Business Exits | Government Contract ERP Service | National | $14.05M | $2.57M | 18% | GovCon ERP/IT services | NEAR-MISS | Clears gate; off-thesis |
| Synergy | Growing LED Display Solutions | FL | $11.19M | $4.63M (cash flow) | 41% | LED display tech/distribution | NEAR-MISS | Clears bands; off-thesis, install-heavy flag |
| Website Closers | SaaS for Financial/Prop Trading Firms (50 enterprise clients) | undisclosed | undisclosed | $3.35M SDE | undisclosed | Financial/prop-trading SaaS | FLAG | ARR/revenue undisclosed; fintech-adjacent, not luxury vertical |
| Business Exits | Midwest Multi-Location Wellness Practice | Midwest | $21.3M | $12.97M | 61% | Healthcare (provider) | HARD-REJECT | Provider-owned healthcare exclude; EBITDA over band |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | 25% | Construction | HARD-REJECT | Non-US + construction exclude |
| Business Exits | California Property Tax Consultants | CA | $6.68M | $4.68M | 70% | Consulting | HARD-REJECT | Rev <$10M floor; CA flag; niche not active |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | 74% | Hospitality/events | HARD-REJECT | Hospitality + B2C + rev <$10M |
| Business Exits | Metal Building Supplier | National | $33.7M | $3.97M | 12% | Construction/mfg | HARD-REJECT | Capital-intensive mfg + construction |
| Business Exits | Atlanta Residential Plumbing & Septic | GA | $11.71M | $2.41M | 21% | Home service | HARD-REJECT | Labor-heavy field service |
| Business Exits | Northeast Commercial Contractor | Northeast | $21.96M | $2.78M | 13% | Construction | HARD-REJECT | Construction exclude |
| Business Exits | Design & Build Studio | undisclosed | $10.02M | $3.06M | 31% | Construction/build | HARD-REJECT | Construction exclude |
| Business Exits | Texas HVAC Company | TX | $21.99M | $2.28M | 10% | Home service/HVAC | HARD-REJECT | Labor-heavy field service |
| Business Exits | Oilfield Infrastructure & Automation | undisclosed | $12.90M | $1.97M | 15% | Energy service | HARD-REJECT | Capital/labor-heavy field service; off-thesis |
| Business Exits | Cell Phone Tower Install & Repair | National | $8.93M | $1.95M | 22% | Telecom service | HARD-REJECT | Rev <$10M + labor-heavy field service |
| Business Exits | Military & Aerospace Parts Distributor | National | $8.23M | $1.90M | 23% | Distribution | HARD-REJECT | Rev <$10M floor |
| Business Exits | Niche Construction Service Business | undisclosed | $10.80M | $2.30M | 21% | Construction | HARD-REJECT | Construction exclude |
| Business Exits | Category-Defining Window Manufacturer | National | $4.90M | $1.54M | 31% | Manufacturing | HARD-REJECT | Capital-intensive mfg + rev <$10M |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | 36% | Construction/electrical | HARD-REJECT | Construction + rev <$10M |
| Business Exits | California Staffing Firm | CA | $7.82M | $3.20M | 41% | Staffing | HARD-REJECT | Rev <$10M floor; CA flag |
| Business Exits | Texas Non-Emergency Medical Transport | TX | $7.74M | $2.87M | 37% | Healthcare transport | HARD-REJECT | Rev <$10M; healthcare-adjacent |
| Business Exits | Safe Pet Travel Products | undisclosed | $1.67M | $1.03M | undisclosed | Consumer products | HARD-REJECT | EBITDA <$1.5M floor + DTC |
| Business Exits | Nevada Fireproofing | NV | $3.06M | $0.93M | undisclosed | Construction service | HARD-REJECT | EBITDA <floor + construction |
| Business Exits | Government Promotional Products | undisclosed | $8.18M | $0.79M | undisclosed | Distribution | HARD-REJECT | EBITDA <floor + rev <$10M |
| Business Exits | Canadian Recruitment Firm | Canada | $2.28M CAD | $0.76M CAD | undisclosed | Staffing | HARD-REJECT | Non-US + below floor |
| Business Exits | Florida Med Spa | FL | $1.07M | $0.72M | undisclosed | Med spa | HARD-REJECT | Below floor + B2C/healthcare |
| Business Exits | Texas Landscape Architecture | TX | $5.50M | $1.80M | undisclosed | Landscape | HARD-REJECT | Rev <$10M; labor-heavy |
| Business Exits | Restaurant/Juice Bar Franchise | undisclosed | $4.14M | $0.71M | undisclosed | Restaurant franchise | HARD-REJECT | Franchise + restaurant + below floor |
| Business Exits | Colorado Regenerative Medicine | CO | $0.89M | $0.49M | undisclosed | Healthcare | HARD-REJECT | Below floor + healthcare |
| Business Exits | Bay Area Roofing | CA | $2.50M | $0.47M | undisclosed | Construction/roofing | HARD-REJECT | Below floor + construction + CA |
| Business Exits | Texas Home Health Staffing | TX | $2.49M | $0.34M | undisclosed | Healthcare staffing | HARD-REJECT | Below floor + healthcare |
| Synergy | Commercial Construction Technology +176% YoY | FL | $9.06M | $3.28M (cash flow) | 36% | Construction/tech | HARD-REJECT | Rev <$10M + construction-adjacent |
| Synergy | Oil & Gas Equipment Rental and Trucking | Midland County, TX | $15.29M | $6.56M (cash flow) | 43% | Energy service | HARD-REJECT | EBITDA over band + labor/capital-heavy |
| Synergy | Seafood Processing & Distribution | Portugal | $165M | $5.9M (cash flow) | 3.6% | Food processing | HARD-REJECT | Non-US + margin <10% + mfg |
| Synergy | Commercial Plumbing Company | NJ | $13.58M | $4.03M (cash flow) | 30% | Construction | HARD-REJECT | Labor-heavy field service |
| Synergy | Women's Health OB/GYN & Urogynecology Clinic | Central FL | $6.58M | $3.38M (cash flow) | 51% | Healthcare | HARD-REJECT | Physician practice + rev <$10M |
| Synergy | Precision Machine Shop (50-yr) | AZ | $7.5M | $2.3M (cash flow) | 31% | Manufacturing | HARD-REJECT | Capital-intensive mfg + rev <$10M |
| Synergy | High-End Renovation Design & Build +100% | NYC, NY | $8.5M | $2.34M (cash flow) | 28% | Construction | HARD-REJECT | NYC construction (explicit exclude) |
| Synergy | Nationwide Niche Logistics Business | DuPage County, IL | $12.06M | $1.19M (cash flow) | 9.9% | Transportation | HARD-REJECT | Margin <10% floor + cash flow <$1.5M |
| Synergy | Telecom Caller Trust SaaS Platform | US | $2.71M | $1.61M (cash flow) | 59% | Telecom SaaS | HARD-REJECT | ARR <$3M SaaS floor + horizontal |
| Synergy | Railroad Construction ($11.5M contracts) | MO | $7.83M | $1.50M (cash flow) | 19% | Construction | HARD-REJECT | Construction + rev <$10M |
| Synergy | Admissions Consulting Practice (remote) | US | $2.0M | $1.3M (cash flow) | 65% | Consulting | HARD-REJECT | Rev + EBITDA below floor |
| Synergy | 40-Year Pediatric Practice | NY | $5.83M | $1.65M (cash flow) | 28% | Healthcare | HARD-REJECT | Physician practice + rev <$10M |
| Synergy | Utility Support Construction Company | Nassau County, NY | $12.0M | $2.0M (cash flow) | 16.7% | Construction | HARD-REJECT | Construction exclude |
| Synergy | Ethanol Producer | India | $10.5M | $3.0M | undisclosed | Manufacturing | HARD-REJECT | Non-US + capital-intensive mfg |
| Synergy | Garment Manufacturing | Bangladesh | $12.5M | $1.95M | undisclosed | Manufacturing | HARD-REJECT | Non-US + mfg |
| Synergy | Industrial Minerals | Peru | $7.0M | $4.5M | undisclosed | Mining/minerals | HARD-REJECT | Non-US + capital-intensive |
| Synergy | B2B Health/Beauty | Dubai | $3.09M | $2.25M | undisclosed | Distribution | HARD-REJECT | Non-US |
| Synergy | Copper Alloy Wires | India | $20M | $2.0M | undisclosed | Manufacturing | HARD-REJECT | Non-US + mfg |
| Synergy | Travel/Tourism | Saudi Arabia | $7.94M | $2.95M | undisclosed | Travel | HARD-REJECT | Non-US + travel/B2C |
| Website Closers | Ed-Tech eLearning Platform (95% recurring) | undisclosed | undisclosed | $1.63M SDE | undisclosed | Online education | HARD-REJECT | B2C ed-tech |
| Website Closers | Amazon FBA eCommerce Brand (30 SKUs) | undisclosed | undisclosed | $0.96M SDE | undisclosed | eCommerce | HARD-REJECT | DTC retail |
| Website Closers | Loss Prevention Training & Awareness Platform | undisclosed | undisclosed | $0.79M SDE | undisclosed | B2B training/SaaS | HARD-REJECT | Sub-scale; off-thesis |
| Website Closers | AI-Driven Ed-Tech Platform (83% margins) | undisclosed | undisclosed | $0.78M SDE | undisclosed | Ed-tech | HARD-REJECT | B2C/sub-scale |
| Website Closers | AI News Intelligence & Data Platform | undisclosed | undisclosed | $0.57M SDE | undisclosed | Fintech/SaaS | HARD-REJECT | Sub-scale + fintech-adjacent |
| Website Closers | 13-Yr Women's Apparel eCommerce | undisclosed | undisclosed | $0.37M SDE | undisclosed | eCommerce | HARD-REJECT | Below floor + DTC |
| Website Closers | Marketing & PR Agency | undisclosed | undisclosed | $0.29M SDE | undisclosed | Marketing | HARD-REJECT | Below floor |
| Website Closers | Fine Jewelry eCommerce | undisclosed | undisclosed | $0.28M SDE | undisclosed | eCommerce | HARD-REJECT | Below floor + DTC |
| Website Closers | Authenticated Collectibles eCommerce | undisclosed | undisclosed | $0.26M SDE | undisclosed | eCommerce | HARD-REJECT | Below floor + DTC |
| Website Closers | AI-Native SEO Agency | undisclosed | undisclosed | $0.12M SDE | undisclosed | Marketing/agency | HARD-REJECT | Below floor |
| Website Closers | Sales Coaching/Lead-Gen | undisclosed | undisclosed | $0.11M SDE | undisclosed | Lead-gen | HARD-REJECT | Below floor |
| Empire Flippers | #94170 Health & Fitness / Home / Medical | undisclosed | ~$17.6M/yr | $383K/mo net | ~26% | Amazon FBA + eCommerce | HARD-REJECT | Consumer retail/DTC exclude |
| Empire Flippers | #94115 Pet Care eCommerce | undisclosed | ~$19.4M/yr | $342K/mo net | ~21% | eCommerce | HARD-REJECT | DTC exclude |
| Empire Flippers | #90682 Cryptocurrency Content/Service | undisclosed | ~$8.3M/yr | $433K/mo net | ~63% | Digital product/newsletter | HARD-REJECT | B2C content |
| Empire Flippers | #88177 Home | undisclosed | ~$8.1M/yr | $159K/mo net | ~24% | Amazon FBA | HARD-REJECT | DTC exclude |
| Empire Flippers | #94312 Beauty / Health & Fitness | undisclosed | ~$6.3M/yr | $127K/mo net | ~24% | eCommerce/FBA | HARD-REJECT | DTC exclude |
| Empire Flippers | #84831 Business / Digital Media | undisclosed | ~$4.0M/yr | $142K/mo net | ~43% | Digital/affiliate | HARD-REJECT | B2C + pending sold |
| Empire Flippers | #83512 Home / Romance | undisclosed | ~$5.8M/yr | $122K/mo net | ~25% | eCommerce/FBA | HARD-REJECT | DTC + pending sold |
| Empire Flippers | #88296 Supplements / Health / Beauty | undisclosed | ~$3.3M/yr | $116K/mo net | ~42% | eCommerce/subscription | HARD-REJECT | DTC + pending sold |
| Empire Flippers | #92853 Home / Outdoors | undisclosed | ~$3.1M/yr | $258K/mo net | undisclosed | Amazon FBA | HARD-REJECT | DTC exclude |
| Empire Flippers | #94296 Sports / Hospitality | undisclosed | ~$1.2M/yr | $99K/mo net | undisclosed | eCommerce | HARD-REJECT | DTC + below scale |
| Empire Flippers | #94619 Pet Care | undisclosed | ~$0.7M/yr | $59K/mo net | undisclosed | Amazon FBA | HARD-REJECT | DTC + below floor |
| Empire Flippers | #94796 Apparel | undisclosed | ~$0.7M/yr | $59K/mo net | undisclosed | eCommerce | HARD-REJECT | DTC + below floor |
| Empire Flippers | #94797 Apparel / Children | undisclosed | ~$0.4M/yr | $30K/mo net | undisclosed | eCommerce | HARD-REJECT | DTC + below floor |
| Empire Flippers | #94174 News / Education (KDP) | undisclosed | ~$0.1M/yr | $10K/mo net | undisclosed | Digital content | HARD-REJECT | B2C + below floor |
| Empire Flippers | #94707 Home / Art Affiliate | undisclosed | ~$66K/yr | $5.5K/mo net | undisclosed | Affiliate content | HARD-REJECT | B2C + below floor |
| Empire Flippers | #94577 Entertainment (YouTube) | undisclosed | ~$61K/yr | $5.1K/mo net | undisclosed | Digital content | HARD-REJECT | B2C + below floor |
| Synergy BB Real Estate | Short-Term Rental Property Mgmt (80+ locations, ACTIVE) | Midwest | $3.23M | $370K (cash flow) | 11% | STR property mgmt | HARD-REJECT | Below floor + STR/B2C (not HNW estate mgmt) |
| Synergy BB Real Estate | Full-Service Event Rental Company (ACTIVE) | South FL | $1.63M | $486K (cash flow) | 30% | Event rental | HARD-REJECT | Below floor + B2C |
| Synergy BB Real Estate | Property Mgmt Company w/ Real Estate (SOLD) | VT | $1.56M | $299K | ~19% | Property management | HARD-REJECT | Already sold + below floor |
| Synergy BB Real Estate | Property Management Firm (SOLD) | NYC, NY | $0.60M | $300K | ~50% | Property management | HARD-REJECT | Already sold + below floor |
| Synergy BB Real Estate | Real Estate Property Mgmt Office (SOLD) | Ulster County, NY | $0.89M | undisclosed | undisclosed | Property management | HARD-REJECT | Already sold + below floor |
| Synergy BB Real Estate | Real Estate Investment Co, Semi-Absentee (SOLD) | Harrisburg, PA | $2.37M | $395K | ~17% | Real estate investment | HARD-REJECT | Already sold + below floor |
| Synergy BB Real Estate | Groundwater Treatment Equipment Rental (SOLD) | Jacksonville, FL | $3.5M | $1.3M | ~37% | Equipment rental/environmental | HARD-REJECT | Already sold + rev <$10M |
| Synergy BB Real Estate | Musical Instrument Rental & Repair (SOLD) | Union County, NJ | $2.35M | $284K | ~12% | Rental/repair services | HARD-REJECT | Already sold + below floor |
| Everingham & Kerr (email) | Southern NJ Residential Landscaping Company | Southern NJ | $1M | ~$300K cash flow | ~30% | Residential landscaping | HARD-REJECT | B2C + labor-heavy + below floor |
| Transworld (email) | High-Growth Distribution Co. Operating Partner Needed | Suffolk County, NY | undisclosed | $1.45M SDE | undisclosed | Distribution | HARD-REJECT | Operating-partner (not majority/full acquisition) |
| Transworld (email) | Growing Multi-Location Restaurant Portfolio | Norfolk County, MA | ~$4M | $459K SDE | undisclosed | Restaurant | HARD-REJECT | Restaurant + B2C + below floor |
| Transworld (email) | Established Commercial Restroom Partitions Business | Suffolk County, NY | $2.3M | -$25K SDE | negative | Building products | HARD-REJECT | Negative earnings + below floor |
| Transworld (email) | Established Eatery with Strong Local Following | Fairfield County, CT | undisclosed | $74.5K SDE | undisclosed | Restaurant | HARD-REJECT | Restaurant + B2C + below floor |
| Transworld (email) | Absentee Run Recording Studio (20-yr, Brooklyn) | Kings County, NY | undisclosed | $135K SDE | undisclosed | Recording studio | HARD-REJECT | Below floor + B2C |
| Transworld (email) | Established Legal Funding Firm Seeking Partner | NY | undisclosed | $1.47M SDE | undisclosed | Legal funding | HARD-REJECT | Lending hard-exclude |
| Transworld (email) | High-End Midtown Med. Skincare Spa (UNDER CONTRACT) | New York County, NY | undisclosed | $0 SDE | undisclosed | Med spa | HARD-REJECT | Under contract + B2C |
| Transworld (email) | Gov Con & Corporate B2B Interiors Firm | NY | undisclosed | $389K SDE | undisclosed | Commercial interiors | HARD-REJECT | EBITDA below floor |
| Transworld (email) | Multilingual Translation & Language Services | PA | undisclosed | $2.4K SDE | undisclosed | Translation services | HARD-REJECT | Below floor |
| Transworld (email) | Authentic Asian Restaurant, Upper West Side | New York County, NY | undisclosed | $103K SDE | undisclosed | Restaurant | HARD-REJECT | Restaurant + B2C + below floor |
| Transworld (email) | Profitable Home-Based Production & Animation | New York County, NY | undisclosed | $53.6K SDE | undisclosed | Production/animation | HARD-REJECT | Below floor |
| Transworld (email) | Seafood Restaurant, A+ Suffolk Location | Suffolk County, NY | undisclosed | $265K SDE | undisclosed | Restaurant | HARD-REJECT | Restaurant + B2C + below floor |
| Transworld (email) | Semi-Passive Multi-Territory Services Franchise | NY/CT | undisclosed | $0 SDE | undisclosed | Services franchise | HARD-REJECT | Franchise + below floor |
| Transworld (email) | Solo Electrical Practice (Net $150k, Turnkey) | Suffolk, NY | undisclosed | $126K SDE | undisclosed | Electrical contracting | HARD-REJECT | Construction + below floor |
| Transworld (email) | Boutique Nail Studio (Premium Build-Out) | New York County, NY | undisclosed | $0 SDE | undisclosed | Nail salon | HARD-REJECT | B2C salon + below floor |
| Transworld (email) | High-Volume Queens Collision Center | Queens, NY | undisclosed | $809K SDE | undisclosed | Auto collision repair | HARD-REJECT | B2C + below floor |
| Transworld (email) | Established Sign & Graphics Franchise | Erie County, NY | undisclosed | $261K SDE | undisclosed | Sign & graphics franchise | HARD-REJECT | Franchise + below floor |
| Transworld (email) | Profitable Industrial Cleaning Business | Rensselaer County, NY | undisclosed | $80.8K SDE | undisclosed | Industrial cleaning | HARD-REJECT | Below floor; not high-end (off cleaning niche) |
| Transworld (email) | Upscale Skincare & Aesthetics Spa | Saratoga County, NY | undisclosed | $231K SDE | undisclosed | Skincare/aesthetics spa | HARD-REJECT | B2C + below floor |
| Transworld (email) | Exquisite High-End Kitchen Cabinet Business | Richmond County, NY | undisclosed | $0 SDE | undisclosed | Kitchen cabinetry | HARD-REJECT | Mfg/retail + below floor |

## Source Scorecard

One row per source. Matches / Last Match Date pulled from `deal-aggregator-fingerprints.jsonl` (only DealsX-channel entries exist; all marketplace sources = 0 / —).

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Website Closers | General | active | 200 | 12 | 0 | — |
| Empire Flippers | General | active | 200 | 16 | 0 | — |
| FE International | General | blocked (verified) | 404/gated | 0 | 0 | — |
| BizBuySell | General | blocked (single-attempt) | 403 | 0 | 0 | — |
| Everingham & Kerr | General (email) | active (via email-intel) | — | 1 | 0 | — |
| Flippa | General (email) | active (via email-intel) | — | 0 | 0 | — |
| Quiet Light | General (email) | active (via email-intel) | — | 0 | 0 | — |
| Rejigg | General (email) | active (via email-intel) | — | 0 | 0 | — |
| Viking Mergers | General (email) | active (via email-intel) | — | 0 | 0 | — |
| IAG M&A Advisors | General (email) | active (via email-intel) | — | 0 | 0 | — |
| SMB Deal Hunter | General (email) | active (via email-intel) | — | 0 | 0 | — |
| DealForce | General (email) | active (via email-intel) | — | 0 | 0 | — |
| Transworld (Samuel Curcio) | General (email) | active (via email-intel) | — | 20 | 0 | — |
| Searchfunder | General | login-gated | — | 0 | 0 | — |
| Benchmark International | General | dormant | — | 0 | 0 | — |
| Acquire.com | General/SaaS | login-gated | — | 0 | 0 | — |
| Axial | General | login-gated | — | 0 | 0 | — |
| BizScout (DealOS) | General | login-gated | — | 0 | 0 | — |
| Kumo | General | login-gated | — | 0 | 0 | — |
| Paine Pacific | General | no public listings | — | 0 | 0 | — |
| Woodbridge (Mariner) | General | no public listings | — | 0 | 0 | — |
| Sica Fletcher | Niche (Insurance) | active | 200 | ~30 (closed-deal intel) | 0 | — |
| GP Bullhound | Niche (SaaS) | active | 200 | 6 (closed-deal intel) | 0 | — |
| Synergy BB Real Estate | Niche (Estate Mgmt) | active | 200 | 8 | 0 | — |
| Exit Strategies Group | Niche (Estate Mgmt) | active | 200 | 0 | 0 | — |
| Software Equity Group | Niche (SaaS) | active | 200 | 8 (closed-deal intel) | 0 | — |
| PCO Bookkeepers | Niche (Pest) | active | 200 | 0 (image tombstones) | 0 | — |
| Cetane | Niche (Pest) | blocked (single-attempt) | 403 | 0 | 0 | — |
| Agency Checklists | Niche (Insurance) | active (intel) | 200 | 0 | 0 | — |
| Anticimex US | Niche (Pest) | active (intel) | 200 | 0 | 0 | — |
| CMM Online | Niche (Cleaning) | active (intel) | 200 | 0 | 0 | — |
| IA Magazine | Niche (Insurance) | active (intel) | 200 | 0 | 0 | — |
| Inside Self-Storage | Niche (Storage) | active (intel) | 200 | 0 | 0 | — |
| MarshBerry | Niche (Insurance) | active (intel) | 200 | 0 | 0 | — |
| MidCap Advisors | Niche (Storage/Art) | active (intel) | 200 | 0 | 0 | — |
| Reagan Consulting | Niche (Insurance) | active (intel) | 200 | 0 | 0 | — |
| Tyton Partners | Niche (SaaS) | active (intel) | 200 | 0 | 0 | — |
| Calder Capital | Niche (Cleaning) | not yet scanning | — | 0 | 0 | — |
| Green Bridge Advisors | Niche (Cleaning) | not yet scanning | — | 0 | 0 | — |
| Union Square Advisors | Niche (SaaS) | not yet scanning | — | 0 | 0 | — |
| Keystone Business Advisors | Niche (Pest) | pending G&B decision | — | 0 | 0 | — |
| Private Art Advisory | Niche (Art Advisory) | structural gap (no source) | — | 0 | 0 | — |
| Specialty Coffee Equipment | Niche (Coffee) | structural gap (no source) | — | 0 | 0 | — |

## Volume Check
- Deals surfaced today: 0
- 7-day rolling average: 0.0/day (prior daily artifacts 5/22, 5/25, 5/26, 5/27, 5/28 all deals_found=0; 5/23–5/24 weekend, no run)
- Target: 1-3/day — **BELOW TARGET**
- Note: Sustained zero-volume is driven by structural mismatch — G&B's active theses (premium pest, art advisory, estate management, specialty coffee equipment service, high-end cleaning, luxury vertical SaaS, art/collectibles insurance, high-value storage) are largely NOT M&A-intermediated on the scrapable general marketplaces, which skew construction/healthcare/B2C/DTC. Confirmed structural gaps for Private Art Advisory + Specialty Coffee Equipment Service (no M&A source exists). Plus the BizBuySell scan gap (agent-browser uninstalled). Flow for these niches is expected to come from direct/proprietary channels (DealsX, JJ, conferences, warm intros), not deal-aggregator marketplace scanning.
