---
date: 2026-05-06
deals_found: 0
sources_scanned: 25
sources_blocked_verified: 4
sources_blocked_single_attempt: 6
email_deals: 0
buy_box_source: live
notes: "email-scan-results-2026-05-06.md not yet written at 6am ET fire (email-intelligence runs 7am ET) — email-channel inbound deals (Everingham & Kerr, Quiet Light email, Flippa email, Viking Mergers, DealForce, IAG, Rejigg, SMB Deal Hunter) will surface in afternoon top-up. BizBuySell + Quiet Light web verified blocked via WebFetch (403) + agent-browser fallback (Access Denied / Cloudflare challenge); Flippa web verified blocked via WebFetch (JS shell) + agent-browser (0 results in static markup). GP Bullhound /transactions/ returned 404 — second consecutive day verified-dead path; recommend retire from daily SaaS rotation per Friday digest queue."
tags: [date/2026-05-06, deal-aggregator, scan-artifact]
---
# Deal Aggregator Scan — 2026-05-06

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box gate AND matched an active-niche corpus across all web-scrapable sources. Email-channel sources (Everingham & Kerr, Quiet Light email, Flippa email, Viking Mergers, DealForce, IAG, Rejigg, SMB Deal Hunter) will surface in the 2pm afternoon top-up via email-scan-results-2026-05-06.md (not yet written — email-intelligence runs 7am ET). Per Channel 2 / Cross-Day Dedup rules, any inbound deals already fingerprinted from prior runs would not double-Slack.

## Email Inbound Deals

None today. The email-scan-results-2026-05-06.md artifact does not yet exist at 6am ET fire — email-intelligence runs 7am ET. Email-channel deal flow (CIMs, broker blasts, intro forwards) will be picked up at the 2pm ET afternoon top-up.

## Near Misses (not Slacked)

- **Synergy BB #8 — Telecom Caller Trust SaaS** (Vertical SaaS, telecom anti-fraud) — ARR $2.71M (just below $3M SaaS floor), EBITDA $1.61M / 59% margin, 120% NRR. Strongest near-miss of the run; clears every SaaS criterion except ARR floor. No active-niche corpus match (telecom anti-fraud ≠ luxury vertical SaaS). Repeat appearance from 5/5 — same listing still on market.
- **Business Exits #3 — California Property Tax Consultants** — Revenue $6.68M (below $10M Services floor), EBITDA $4.68M / ~70% margin. Disclosed-and-fails on revenue floor; CA soft-flag also applies. Repeat from 5/5.
- **Business Exits #6 — GovCon IT Firm (Judiciary & VA)** — Revenue $19.7M, EBITDA $3.45M / ~17.5%. Clears Services buy-box numerically. No active-niche corpus match. Repeat from 5/5.
- **Business Exits #7 — B2B Experiential Marketing** — Revenue $14.3M, EBITDA $3.30M / ~23%. Clears Services. No niche match. Repeat from 5/5.
- **Business Exits #12 — Government Contract ERP Service Business** — Revenue $14M, EBITDA $2.57M / ~18%. Clears Services. No niche match. Repeat from 5/5.
- **Synergy BB #3 — LED Display Solutions Co (FL)** — Revenue $11.2M, EBITDA $4.63M / ~41%. Clears Services. No niche match. Repeat from 5/5.
- **0 wine/art/jewelry/climate-controlled deals** in Inside Self-Storage feed this run (Specialty Storage corpus drew zero hits despite 15 transactions logged — all general self-storage REIT/PE consolidation $50M+).
- **0 active fine-art-logistics deals** in MidCap Advisors news-releases (most recent comp remains Artemis → Cadogan Tate).
- **0 deal-flow stories** in CMM Online (full week of regulatory/policy/sustainability news, no M&A).
- **0 M&A blog posts** on PCO Bookkeepers in past 60 days (only pest-index reports + scholarship news).
- **GP Bullhound /transactions/ 404 second consecutive day** — confirmed-dead path. Recommend retire from daily SaaS rotation in Friday 5/8 digest.
- **email-scan-results-2026-05-06.md not present** at 6am fire (email-intelligence runs 7am). Email-channel inbound deals (CIMs, broker blasts, intro forwards) will surface in afternoon top-up.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Synergy BB | Telecom Caller Trust Platform (SaaS) | USA | $2.71M ARR | $1.61M | 59% | Vertical SaaS — telecom anti-fraud | NEAR-MISS | ARR ~$2.71M just below $3M SaaS floor (disclosed); strong unit econ (59% EBITDA, 120% NRR); no active-niche corpus match |
| Business Exits | California Property Tax Consultants | California | $6.68M | $4.68M | ~70% | Marketing & Consulting / property tax | NEAR-MISS | Revenue $6.68M < $10M Services floor (disclosed); CA soft-flag |
| Business Exits | GovCon IT Firm – Judiciary & VA Contracts | undisclosed | $19.7M | $3.45M | ~17.5% | GovCon IT services/software | NEAR-MISS | Clears Services buy-box; no niche corpus match |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.3M | $3.30M | ~23% | B2B experiential marketing | NEAR-MISS | Clears Services buy-box; no niche match |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14M | $2.57M | ~18% | ERP services / govcon | NEAR-MISS | Clears Services buy-box; no niche match |
| Synergy BB | LED Display Solutions Company | Florida | $11.2M | $4.63M | ~41% | LED display tech/distribution | NEAR-MISS | Clears Services buy-box; no niche match |
| Empire Flippers | #84831 Digital Media — Service + Digital Product + Affiliate | undisclosed | $3.76M | $1.78M | ~47% | Digital media / affiliate / service hybrid | FLAG | Affiliate-heavy mix likely fails B2B test; ambiguous service component |
| Empire Flippers | #90682 Crypto News Platform/Wire Service | undisclosed | $8.30M | $5.20M | ~63% | Crypto-native news platform | FLAG | High margin but B2C/consumer info media; fintech-adjacent — surface for human review |
| Website Closers | Category-Leading National Push-to-Talk Communications Platform | USA national | undisclosed | $12.5M cash flow | undisclosed | B2B push-to-talk / wireless comms | FLAG | $160M ask + $12.5M cash flow implies revenue >$50M ceiling; only 30% recurring; surface for human review |
| Website Closers | SBA Pre-Qualified Procurement Services & Distribution | undisclosed | undisclosed | $200K | 36% | B2B procurement + distribution | FLAG | Cash flow $200K well below $1.5M EBITDA floor; B2B/recurring shape on-thesis but financials too small |
| Sica Fletcher | Safe Harbour Insurance Mgmt → ALKEME (closed 2/27/26) | MA | undisclosed | undisclosed | undisclosed | retail insurance brokerage | FLAG | Closed-deal tombstone (intel-only); ALKEME = PE-consolidator |
| Sica Fletcher | O'Neill Associates Consulting → ALKEME (closed 2/27/26) | FL | undisclosed | undisclosed | undisclosed | retail insurance brokerage | FLAG | Closed-deal tombstone; ALKEME consolidator |
| Sica Fletcher | Surety Bonds LLC → The Hilb Group (closed 2/15/26) | GA | undisclosed | undisclosed | undisclosed | specialty surety brokerage | FLAG | Closed-deal tombstone; Hilb is PE-consolidator; specialty surety is sub-vertical worth tracking |
| Sica Fletcher | Quantum Resource Group → ALKEME (closed 2/13/26) | MD | undisclosed | undisclosed | undisclosed | retail insurance brokerage | FLAG | Closed-deal tombstone; ALKEME consolidator |
| Sica Fletcher | Centennial State Insurance Group → ALKEME (closed 1/9/26) | CO | undisclosed | undisclosed | undisclosed | retail insurance brokerage | FLAG | Closed-deal tombstone; ALKEME consolidator |
| MidCap Advisors | Artemis Fine Arts Services → Cadogan Tate (historical) | undisclosed | undisclosed | undisclosed | undisclosed | fine art logistics & museum services | FLAG | 2023 closed deal, intel-only; direct comp for Specialty Storage niche; Cadogan Tate is the consolidator to track |
| MidCap Advisors | Meritage Life Insurance GA → AmeriLife (06/2024) | undisclosed | undisclosed | undisclosed | undisclosed | life insurance general agency | FLAG | Closed deal, intel-only; consolidator buyer |
| MidCap Advisors | EMG Insurance Brokerage → Senior Market Sales | undisclosed | undisclosed | undisclosed | undisclosed | insurance brokerage | FLAG | Closed deal, intel-only |
| MidCap Advisors | Pavese-McCormick → King Insurance Partners | undisclosed | undisclosed | undisclosed | undisclosed | P&C insurance agency | FLAG | Closed deal, intel-only; consolidator buyer |
| MidCap Advisors | (k)RPG → OneDigital Investment Advisors (10/2023) | undisclosed | undisclosed | undisclosed | undisclosed | wealth/retirement plan services | FLAG | Closed deal, intel-only; out-of-niche (wealth mgmt) |
| MidCap Advisors | Patriot Pension Advisors → CAPTRUST (10/2023) | MA | undisclosed | undisclosed | undisclosed | retirement plan advisory | FLAG | Closed deal, intel-only; out-of-niche |
| MidCap Advisors | GRP Financial / Global Retirement Partners → Hub International (10/2023) | undisclosed | undisclosed | undisclosed | undisclosed | retirement plan services | FLAG | Closed deal, intel-only; out-of-niche |
| Inside Self-Storage | Skyview launches 'Deal Lead in Residency' program (5/4/26) | n/a | n/a | n/a | n/a | self-storage advisory | FLAG | Intel-only; advisory program announcement, not a transaction |
| Inside Self-Storage | Self-Storage Real Estate Acquisitions and Sales: April 2026 (roundup) | multi | undisclosed | undisclosed | undisclosed | self-storage real estate | FLAG | Intel-only; monthly roundup; deeper scan needed for any specialty wine/art/climate sub-deals not in headline |
| Inside Self-Storage | National Storage REIT court approval for Brookfield/GIC sale (4/21/26) | AU/NZ | undisclosed | undisclosed | undisclosed | self-storage REIT | FLAG | Intel-only; non-US REIT-level deal; out of size band |
| Inside Self-Storage | Flexistockage Paris → Zebrabox France JV (4/14/26) | France | undisclosed | undisclosed | undisclosed | self-storage | FLAG | Intel-only; non-US |
| Inside Self-Storage | Public Storage acquires National Storage Affiliates Trust ($10.5B all-stock, 3/16/26) | USA multi | undisclosed | undisclosed | undisclosed | general self-storage | FLAG | Intel-only; deal size $10.5B dwarfs buy-box; REIT-level consolidation |
| Inside Self-Storage | Washington Street Investment Partners/LocalStorage acquires SROA portfolio ($98M, 3/26/26) | USA multi | undisclosed | undisclosed | undisclosed | general self-storage portfolio | FLAG | Intel-only; portfolio deal |
| Inside Self-Storage | Clear Sky Capital/QuadReal acquire Padlock Euro Storage ($276M, 3/23/26) | Europe | undisclosed | undisclosed | undisclosed | general self-storage portfolio | FLAG | Intel-only; non-US |
| Inside Self-Storage | CapitaLand acquires Access Self Storage UK portfolio ($1B+, 3/23/26) | UK | undisclosed | undisclosed | undisclosed | general self-storage | FLAG | Intel-only; non-US |
| Inside Self-Storage | Ardian acquires majority stake in Casaforte (3/10/26) | Italy | undisclosed | undisclosed | undisclosed | self-storage | FLAG | Intel-only; non-US |
| Inside Self-Storage | Centerbridge Partners/Reframe Holdings funding ($350M, 3/19/26) | USA multi | undisclosed | undisclosed | undisclosed | self-storage growth platform | FLAG | Intel-only; growth-equity, not acquisition |
| Inside Self-Storage | StorageMart acquires 15 NYC facilities ($1B, 1/29/26) | NY | undisclosed | undisclosed | undisclosed | general self-storage | FLAG | Intel-only; portfolio at $1B level |
| Inside Self-Storage | 10 Federal Self-Storage enters Arkansas (7-facility, 1/27/26) | AR | undisclosed | undisclosed | undisclosed | general self-storage | FLAG | Intel-only |
| Inside Self-Storage | BlackRock's StoreLocal acquires KeepSafe Australia (A$150M, 1/7/26) | AU | undisclosed | undisclosed | undisclosed | general self-storage | FLAG | Intel-only; non-US |
| Inside Self-Storage | Glacier Global Partners/Next Century JV (1/6/26) | USA multi | undisclosed | undisclosed | undisclosed | self-storage JV | FLAG | Intel-only; partnership formation |
| Inside Self-Storage | Strategic Storage Trust X initial acquisition (11/24/25) | USA multi | undisclosed | undisclosed | undisclosed | general self-storage REIT | FLAG | Intel-only; aspiring-REIT initial deal |
| Agency Checklists | Paradiso Insurance acquired by Trucordia (5/4/26) | New England | undisclosed | undisclosed | undisclosed | insurance agency | FLAG | Intel-only; Trucordia = PE-consolidator; Paradiso now off-market (blacklist signal) |
| Agency Checklists | Insurance Agency M&A in Massachusetts Q1-2026 (4/28/26) | MA / New England | undisclosed | undisclosed | undisclosed | insurance agency M&A roundup | FLAG | Intel-only; quarterly roundup |
| Agency Checklists | OPTIS: Insurance Agency M&A Down 6% in Q1 2026 (4/27/26) | national | undisclosed | undisclosed | undisclosed | insurance agency M&A market report | FLAG | Intel-only; market-pace data |
| Agency Checklists | ACORD: Carrier M&A becoming smaller-volume, higher-risk (4/13/26) | national | undisclosed | undisclosed | undisclosed | insurance carrier M&A market analysis | FLAG | Intel-only; carrier-level analysis (out-of-niche but tracked) |
| MarshBerry News | Inaugural Tech & Governance Report for Insurance Distribution (2/23/26) | n/a | n/a | n/a | n/a | insurance distribution research | FLAG | Intel-only; market research, not transaction |
| MarshBerry News | Insurance Growth Network → People Corporation (1/29/26) | undisclosed | undisclosed | undisclosed | undisclosed | retail/specialty insurance brokerage partnership | FLAG | Intel-only; specialty buyer transaction |
| MarshBerry News | Compensation Study for Insurance Agents & Brokers (1/13/26) | n/a | n/a | n/a | n/a | insurance research product | FLAG | Intel-only; market research |
| MarshBerry News | Lincoln International promotes six to MD (1/12/26) | n/a | n/a | n/a | n/a | banking personnel announcement | FLAG | Intel-only; firm news |
| MarshBerry News | Long Run Wealth Advisors → Mercer Global Advisors (1/7/26) | undisclosed | undisclosed | undisclosed | undisclosed | wealth management | FLAG | Intel-only; out-of-niche (wealth mgmt) |
| MarshBerry News | The Richards Group → IMA Financial Group (1/5/26) | undisclosed | undisclosed | undisclosed | undisclosed | retail/specialty insurance brokerage partnership | FLAG | Intel-only; IMA mid-market consolidator |
| IA Magazine | Art of The Exit: Smooth Transition When It's Time to Sell (5/1/26) | n/a | n/a | n/a | n/a | agency sale guidance | FLAG | Intel-only; owner-prep content |
| IA Magazine | Insurance Agency M&A and Preventing E&O Claims (5/1/26) | n/a | n/a | n/a | n/a | insurance M&A operational guidance | FLAG | Intel-only; operational article |
| IA Magazine | Insurance Agency M&A Falls 6% in First Quarter (4/30/26) | national | undisclosed | undisclosed | undisclosed | insurance agency M&A market report | FLAG | Intel-only; cross-confirmed against OPTIS data |
| Synergy BB Real Estate | Event Rental Company - Full-Service | South Florida | $1.63M | $0.49M | ~30% | event rental services | HARD-REJECT | Revenue $1.63M < $10M floor (disclosed); hospitality-adjacent |
| Synergy BB Real Estate | Short-Term Rental Property Management 80+ Locations | Midwest | $3.23M | $0.37M | ~11% | short-term rental property mgmt | HARD-REJECT | Revenue $3.23M < $10M floor (disclosed); STR ≠ HNW estate-mgmt corpus |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest | $21.3M | $12.97M | ~61% | Healthcare/wellness multi-location | HARD-REJECT | Physician-practice hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | ~25% | Construction | HARD-REJECT | Construction hard-exclude; non-US |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | ~74% | Wedding venue / hospitality | HARD-REJECT | Hospitality hard-exclude; revenue below floor |
| Business Exits | Metal Building Supplier with US Manufacturing | undisclosed | $33.7M | $3.97M | ~12% | Construction / manufacturing | HARD-REJECT | Capital-intensive manufacturing + construction-adjacent |
| Business Exits | Texas Non-Emergency Medical Transport | Texas | $7.74M | $2.87M | ~37% | NEMT/medical transport | HARD-REJECT | Revenue $7.74M < $10M floor (disclosed); medical/transport labor-heavy |
| Business Exits | California Staffing Firm with Recurring Revenue | California | $7.82M | $3.20M | ~41% | Staffing services | HARD-REJECT | Revenue < $10M floor (disclosed); CA soft-flag |
| Business Exits | Northeast Commercial Contractor (Healthcare/Financial) | Northeast | $22M | $2.78M | ~13% | Commercial contracting/construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Atlanta Residential Plumbing & Septic | GA | $11.7M | $2.41M | ~21% | Residential plumbing/septic | HARD-REJECT | Construction/labor-heavy hard-exclude |
| Business Exits | Design & Build Studio for Themed Props | undisclosed | $10M | $3.06M | ~31% | Design/build manufacturing | HARD-REJECT | Capital-intensive manufacturing + construction hard-exclude |
| Business Exits | Texas HVAC Company | Texas | $22M | $2.28M | ~10% | Residential HVAC | HARD-REJECT | Construction/labor-heavy hard-exclude; margin at floor |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | ~22% | Tower install/repair construction | HARD-REJECT | Construction hard-exclude + revenue <$10M floor |
| Business Exits | Specialized Military/Aerospace Parts Distributor | undisclosed | $8.23M | $1.90M | ~23% | Aerospace/military parts distribution | HARD-REJECT | Revenue < floor; aerospace adjacent |
| Business Exits | Window Manufacturer | undisclosed | $4.90M | $1.54M | ~31% | Window manufacturing/retail | HARD-REJECT | Capital-intensive manufacturing + below floor |
| Business Exits | Arizona Addiction Treatment | Arizona | $4.45M | $1.10M | ~25% | Healthcare addiction treatment | HARD-REJECT | Physician-practice hard-exclude + below floor |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | $1.91M | ~36% | Electrical contracting | HARD-REJECT | Construction hard-exclude + below floor |
| Business Exits | Pet Travel Products Distribution | undisclosed | $1.67M | $1.03M | ~62% | Consumer retail / pet | HARD-REJECT | Consumer retail/DTC + below floor |
| Business Exits | Nevada Fireproofing Contractor | Nevada | $3.06M | $0.93M | ~31% | Construction/fireproofing | HARD-REJECT | Construction + below floor |
| Business Exits | Government Promotional Products | undisclosed | $8.18M | $0.79M | ~10% | Promotional retail | HARD-REJECT | Consumer/retail + below floor + margin at floor |
| Business Exits | Canadian Recruitment Agency | Canada | $2.28M CAD | $0.76M CAD | ~33% | Recruitment / staffing | HARD-REJECT | Non-US + below floor |
| Business Exits | Florida Med Spa | Florida | $1.07M | $0.68M | ~64% | Med spa / healthcare | HARD-REJECT | Physician-practice + below floor |
| Business Exits | Landscape Architecture | undisclosed | $5.5M | $1.8M | ~33% | Landscape architecture / construction | HARD-REJECT | Construction hard-exclude + below floor |
| Business Exits | CA Multi-Location Gym Franchise | California | $2.07M | $0.66M | ~32% | Gym franchise | HARD-REJECT | Franchise + hospitality-adjacent + below floor |
| Business Exits | Restaurant/Juice Bar Franchise | undisclosed | $4.14M | $0.71M | ~17% | Restaurant/juice franchise | HARD-REJECT | Restaurant + franchise hard-excludes |
| Business Exits | Colorado Regenerative Medicine | Colorado | $0.89M | $0.49M | ~55% | Healthcare regenerative | HARD-REJECT | Physician-practice + below floor |
| Business Exits | Bay Area Roofing | California | $2.5M | $0.47M | ~19% | Construction/roofing | HARD-REJECT | Construction + below floor |
| Business Exits | Texas Home Health Staffing | Texas | $2.49M | $0.34M | ~14% | Healthcare staffing | HARD-REJECT | Healthcare staffing + below floor |
| Empire Flippers | #94170 Health & Fitness Amazon FBA brand | undisclosed | $17.59M | $4.60M | ~26% | DTC/Amazon FBA wellness | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Empire Flippers | #93931 Lifestyle/Travel Amazon FBA | undisclosed | $14.35M | $2.17M | ~15% | DTC/Amazon FBA travel | HARD-REJECT | Consumer retail/DTC |
| Empire Flippers | #93714 DTC health/lifestyle brand | undisclosed | $3.37M | $0.51M | ~15% | DTC consumer brand | HARD-REJECT | Consumer/DTC + below floor |
| Empire Flippers | #93968 YouTube food channel | undisclosed | $0.21M | $0.20M | ~95% | digital media/YouTube | HARD-REJECT | Below floor; consumer media |
| Empire Flippers | #93813 B2B Newsletter for Amazon/eComm | undisclosed | $0.11M | $0.11M | ~96% | B2B newsletter | HARD-REJECT | Below floor |
| Empire Flippers | #93891 DTC beauty | undisclosed | $1.18M | $0.21M | ~18% | DTC beauty | HARD-REJECT | Consumer retail + below floor |
| Empire Flippers | #91305 Calculator website | undisclosed | $0.05M | $0.04M | ~95% | content/tool website | HARD-REJECT | Below floor |
| Empire Flippers | #94001 Amazon FBA grooming UK | UK | $0.30M | $0.04M | ~13% | DTC grooming Amazon FBA | HARD-REJECT | Consumer retail + below floor + non-US |
| Empire Flippers | #93682 Music digital product | undisclosed | $0.03M | $0.03M | ~90% | digital product | HARD-REJECT | Below floor |
| Empire Flippers | #94003 Faceless YouTube channel | undisclosed | $0.025M | $0.025M | ~100% | content/YouTube | HARD-REJECT | Below floor |
| Empire Flippers | #92497 French automotive YouTube | undisclosed | $0.05M | $0.027M | ~53% | content/YouTube | HARD-REJECT | Below floor |
| Empire Flippers | #92985 Amazon FBA private-label portfolio | undisclosed | $24.46M | $2.57M | ~11% | DTC/Amazon FBA portfolio | HARD-REJECT | Consumer retail/DTC; margin marginal |
| Empire Flippers | #94115 DTC pet wellness eCommerce | undisclosed | $19.40M | $4.11M | ~21% | DTC pet wellness | HARD-REJECT | Consumer retail/DTC |
| Empire Flippers | #89990 Amazon FBA cooking utensils | undisclosed | $13.10M | $2.82M | ~22% | DTC kitchenware | HARD-REJECT | Consumer retail |
| Empire Flippers | #88177 Amazon FBA pest control products | undisclosed | $8.10M | $1.91M | ~24% | DTC pest products | HARD-REJECT | Consumer retail; pest products ≠ pest services niche |
| Empire Flippers | #89855 Amazon FBA kitchenware | undisclosed | $13.79M | $1.84M | ~13% | DTC kitchenware | HARD-REJECT | Consumer retail |
| Empire Flippers | #88296 Supplement brand (anti-aging) | undisclosed | $3.32M | $1.39M | ~42% | DTC supplements | HARD-REJECT | Consumer retail/DTC |
| Empire Flippers | #83512 Global eCommerce/FBA home products | undisclosed | $5.84M | $1.47M | ~25% | DTC home products | HARD-REJECT | Consumer retail/DTC |
| Empire Flippers | #91643 Amazon FBA hobbies/gaming | undisclosed | $4.05M | $1.17M | ~29% | DTC hobbies | HARD-REJECT | Consumer retail/DTC |
| Synergy BB | Seafood Processing And Distribution | Portugal | $165M | $5.9M | ~3.6% | Seafood processing/distribution | HARD-REJECT | Revenue >$50M ceiling; margin <10% floor; non-US; capital-intensive |
| Synergy BB | Oil & Gas Equipment Rental & Trucking | Midland TX | $15.3M | $6.56M | ~43% | Oil & gas equipment rental | HARD-REJECT | Capital-intensive + construction/field-labor hard-exclude |
| Synergy BB | Concrete & Masonry Contractor | Florida | $18.5M | $5.7M | ~31% | Concrete/masonry construction | HARD-REJECT | Construction hard-exclude |
| Synergy BB | Commercial Plumbing Company | New Jersey | $13.6M | $4.03M | ~30% | Commercial plumbing | HARD-REJECT | Construction/field-labor hard-exclude |
| Synergy BB | OB/GYN & Urogynecology Multi-Physician Clinic | Central FL | $6.58M | $3.38M | ~51% | OB/GYN physician practice | HARD-REJECT | Physician-practice hard-exclude; revenue below floor |
| Synergy BB | Precision Machine Shop | Arizona | $7.5M | $2.3M | ~31% | Precision machining | HARD-REJECT | Capital-intensive manufacturing + below floor |
| Synergy BB | Ethanol Producer | India | $10.5M | $3M | ~29% | Ethanol manufacturing | HARD-REJECT | Capital-intensive manufacturing + non-US |
| Synergy BB | Industrial Minerals Producer | Peru | $7M | $4.5M | ~64% | Mining/minerals manufacturing | HARD-REJECT | Capital-intensive + non-US + below floor |
| Synergy BB | NYC High-End Renovation Design/Build | NYC | $8.5M | $2.34M | ~28% | Renovation/design-build | HARD-REJECT | Construction hard-exclude (NYC explicitly) + below floor |
| Synergy BB | Garment Manufacturing Bangladesh | Bangladesh | $12.5M | $1.95M | ~16% | Garment manufacturing | HARD-REJECT | Non-US + capital-intensive manufacturing |
| Synergy BB | Railroad Construction Business | Missouri | $7.83M | $1.50M | ~19% | Railroad construction | HARD-REJECT | Construction hard-exclude + below floor |
| Synergy BB | B2B Health/Beauty Ingredient Mfg/Dist | Dubai | $3.09M | $2.25M | ~73% | Health/beauty ingredient mfg | HARD-REJECT | Non-US + capital-intensive + below floor |
| Synergy BB | Specialty Copper Alloy Wires Mfg | India | $20M | $2M | ~10% | Non-ferrous wire manufacturing | HARD-REJECT | Non-US + capital-intensive; margin at floor |
| Synergy BB | Travel/Tourism Saudi Arabia | Saudi Arabia | $7.94M | $2.95M | ~37% | Travel/tourism services | HARD-REJECT | Non-US + below floor + hospitality-adjacent |
| Synergy BB | Tech-Enabled Behavioral Health (Telehealth Psych) | Washington DC | $5M | $1M | ~20% | Telehealth psychiatry | HARD-REJECT | Physician-practice hard-exclude + below floor |
| Synergy BB | Admissions Consulting Practice (Global Remote) | USA | $2M | $1.3M | ~65% | Admissions consulting | HARD-REJECT | Revenue $2M < $10M floor (disclosed) |
| Synergy BB | Pediatric Practice 40-Year | New York | $5.83M | $1.65M | ~28% | Pediatric medical practice | HARD-REJECT | Physician-practice hard-exclude + below floor |
| Synergy BB | Utility Support Construction (heavy civil) | Nassau NY | $12M | $2M | ~17% | Utility construction | HARD-REJECT | Construction hard-exclude |
| Synergy BB Real Estate | Groundwater Treatment Equipment Rental (SOLD) | Jacksonville FL | $3.5M | $1.3M | ~37% | equipment rental services | FLAG | Already sold (intel) |
| Synergy BB Real Estate | Musical Instrument Rental & Repair (SOLD) | Union County NJ | $2.35M | $0.28M | ~12% | musical instrument rental | FLAG | Already sold (intel) |
| Synergy BB Real Estate | Property Management Co with Real Estate (SOLD) | Vermont | $1.56M | $0.30M | ~19% | property management | FLAG | Already sold (intel) |
| Synergy BB Real Estate | Real Estate Investment Co Semi-Absentee (SOLD) | Harrisburg PA | $2.37M | $0.39M | ~17% | RE investment company | FLAG | Already sold (intel) |
| Synergy BB Real Estate | NYC Property Management Firm (SOLD) | NYC | $0.60M | $0.30M | ~50% | property management | FLAG | Already sold (intel); below floor |
| Synergy BB Real Estate | Real Estate Property Management Office (SOLD) | Ulster County NY | $0.89M | undisclosed | undisclosed | property management | FLAG | Already sold (intel); below floor |
| Website Closers | 67-Year Cayman Architectural Design Firm | Cayman Islands | undisclosed | $0.39M | undisclosed | architecture/design | HARD-REJECT | Non-US + below floor + design-services adjacent to construction |
| Website Closers | Towels & Socks eCommerce Brand | undisclosed | undisclosed | $0.53M | undisclosed | DTC eCommerce | HARD-REJECT | Consumer retail/DTC + below floor |
| Website Closers | SBA Pre-Qualified Collectible Merchandise Brand | undisclosed | undisclosed | $0.72M | 36% | DTC eCommerce/collectibles (95% Amazon) | HARD-REJECT | Consumer retail + below floor |
| Website Closers | Proprietary Home Products eCommerce Brand | undisclosed | undisclosed | $5.81M | undisclosed | DTC eCommerce home goods | HARD-REJECT | Consumer retail/DTC |
| Website Closers | eCommerce Brand - Guided Fitness Journals | undisclosed | undisclosed | $0.30M | undisclosed | DTC fitness publishing | HARD-REJECT | Consumer retail + below floor |
| Website Closers | SBA Pre-Qualified Multi-Label Women's Apparel | undisclosed | undisclosed | $0.89M | 30% | DTC/wholesale apparel | HARD-REJECT | Consumer retail + below floor |
| Website Closers | Global Franchise System - City-Focused B2B Advertising | International (27 countries) | undisclosed | $0.28M | undisclosed | franchise/B2B advertising | HARD-REJECT | Franchise hard-exclude + below floor |
| Website Closers | Military Training & Firing Range Apparel Brand | undisclosed | undisclosed | $0.17M | undisclosed | DTC apparel | HARD-REJECT | Consumer retail + below floor |
| Website Closers | SBA Pre-Qualified AI SaaS Company - Humanizing AI | undisclosed | $0.60M ARR | $0.40M | 63% | horizontal AI SaaS | HARD-REJECT | ARR <$3M SaaS floor; horizontal SaaS hard-exclude |
| Website Closers | Award Winning Vineyard & Brewery Estate | New Zealand | undisclosed | $0.61M | undisclosed | wine/hospitality/tourism | HARD-REJECT | Hospitality + non-US + below floor |
| Website Closers | SBA Pre-Qualified eCommerce Gifts & Jewelry | undisclosed | undisclosed | $0.10M | undisclosed | DTC eCommerce | HARD-REJECT | Consumer retail + below floor |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| Empire Flippers | General | active | 200 | 21 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Website Closers | General | active | 200 | 13 | 0 | — |
| BizBuySell | General | blocked (verified) | 403 | 0 | 0 | — |
| Flippa (web) | General | blocked (verified) | 200 (JS shell, 0 results) | 0 | 0 | — |
| Quiet Light (web) | General | blocked (verified) | 403 | 0 | 0 | — |
| DealForce | General | blocked (single-attempt) | — | 0 | 0 | — |
| IAG M&A Advisors | General | blocked (single-attempt) | — | 0 | 0 | — |
| Rejigg | General | blocked (single-attempt) | — | 0 | 0 | — |
| Everingham & Kerr | General | blocked (single-attempt) | — | 0 | 0 | — |
| Viking Mergers | General | blocked (single-attempt) | — | 0 | 0 | — |
| SMB Deal Hunter | General | blocked (single-attempt) | — | 0 | 0 | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 5 | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 | 0 | — |
| GP Bullhound | Niche-Specific (SaaS) | blocked (verified) | 404 | 0 | 0 | — |
| Agency Checklists | Intel-only (Insurance) | active | 200 | 4 | 0 | — |
| MarshBerry News | Intel-only (Insurance) | active | 200 | 6 | 0 | — |
| IA Magazine | Intel-only (Insurance) | active | 200 | 3 | 0 | — |
| Reagan Consulting | Intel-only (Insurance) | active | 200 | 0 | 0 | — |
| MidCap Advisors | Intel-only (Storage) | active | 200 | 7 | 0 | — |
| Inside Self-Storage | Intel-only (Storage) | active | 200 | 15 | 0 | — |
| CMM Online | Intel-only (Cleaning) | active | 200 | 0 | 0 | — |
| Anticimex US | Intel-only (Pest) | active | 200 | 0 | 0 | — |

**Email-channel sources** (Everingham & Kerr, Quiet Light email, Flippa email, Viking Mergers, DealForce, IAG M&A, Rejigg, SMB Deal Hunter): marked `blocked (single-attempt)` because email-scan-results-2026-05-06.md does not yet exist at 6am ET fire (email-intelligence runs 7am ET). Afternoon top-up will pick them up.

**Fingerprint store status:** `brain/context/deal-aggregator-fingerprints.jsonl` is empty (0 records). All Last Match Date values therefore "—". When a future PASS lands, it'll establish the first fingerprint record.

## Volume Check
- Deals surfaced today: 0
- 7-day rolling average: 0/day (last 5 morning fires: 4/29 = 0, 5/1 = 0, 5/4 = 0, 5/5 = 0, 5/6 = 0)
- Target: 1-3/day — **BELOW TARGET** (5 consecutive zero-PASS mornings on web-scrapable channels). Email channel is the volume engine; afternoon top-up + Friday digest will surface what 6am web-scrape misses. Friday 5/8 digest should propose retiring GP Bullhound (verified-dead /transactions/) and reviewing Inside Self-Storage productivity (15 logged, 0 specialty wine/art/jewelry hits across 30+ days).
