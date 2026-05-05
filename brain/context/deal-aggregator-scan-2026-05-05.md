---
date: 2026-05-05
deals_found: 0
sources_scanned: 17
sources_blocked_verified: 2
sources_blocked_single_attempt: 0
email_deals: 0
buy_box_source: live
notes: "email-scan-results-2026-05-05.md not yet written at 6am ET fire (email-intelligence runs 7am ET) — email-channel inbound deals will be picked up by afternoon top-up run. Scan focused on web-scrapable General + Niche-Specific + Intel sources."
tags: [date/2026-05-05, deal-aggregator, scan-artifact]
---
# Deal Aggregator Scan — 2026-05-05

## Deals Surfaced (sent to Slack individually)

None today. 0 listings cleared the buy-box gate AND matched an active-niche corpus across all web-scrapable sources. Email-channel sources (Everingham & Kerr, Quiet Light, Flippa, Viking Mergers, DealForce, IAG, SMB Deal Hunter, Searchfunder) will surface in the afternoon top-up via email-scan-results-2026-05-05.md.

## Email Inbound Deals

None today. The email-scan-results-2026-05-05.md artifact does not yet exist at 6am ET fire — email-intelligence runs 7am ET. Email-channel deal flow (CIMs, broker blasts, intro forwards) will be picked up at the 2pm ET afternoon top-up. Per Channel 2 / Cross-Day Dedup rules, any inbound deals already fingerprinted from prior runs would not double-Slack.

## Near Misses (not Slacked)

- **Synergy BB #8 — Telecom Caller Trust SaaS** (Vertical SaaS, telecom anti-fraud) — ARR ~$2.71M (just below $3M SaaS floor), EBITDA $1.61M / 59% margin, 120% NRR. Strongest near-miss of the run; clears every SaaS criterion except ARR floor (data-availability rule means flag, not auto-reject if you treat the ARR proxy generously). No active-niche corpus match (anti-fraud telecom ≠ luxury vertical SaaS). Worth tracking as thesis-drift signal.
- **Business Exits #3 — California Property Tax Consultants** — Revenue $6.68M (below $10M Services floor), EBITDA $4.68M / ~70% margin. Disclosed below floor → HARD-REJECT despite strong unit econ; CA soft-flag also applies. Recategorized as near-miss for unit-economics interest.
- **Business Exits #6 — GovCon IT Firm (Judiciary & VA)** — Revenue $19.7M, EBITDA $3.45M / ~17.5%. Clears Services buy-box numerically. No active-niche corpus match.
- **Business Exits #7 — B2B Experiential Marketing Vendor** — Revenue $14.3M, EBITDA $3.30M / ~23%. Clears Services. No niche match.
- **Business Exits #12 — Government Contract ERP Service Business** — Revenue $14M, EBITDA $2.57M / ~18%. Clears Services. No niche match.
- **Synergy BB #3 — LED Display Solutions Co (FL)** — Revenue $11.2M, EBITDA $4.63M / ~41%. Clears Services. No niche match.
- **0 wine/art/climate-controlled deals** in Inside Self-Storage feed this run (Specialty Storage corpus drew zero hits — flagged April monthly roundup for deeper scan).
- **0 active fine-art-logistics deals** in MidCap Advisors news-releases (most recent comp remains Artemis → Cadogan Tate, 2023).
- **0 deal-flow stories** in CMM Online (full week of regulatory/policy/sustainability news, no M&A).
- **GP Bullhound confirmed wrong tier** ($100M+ deal sizes, PE/strategic acquirers throughout) — recommend dropping from daily SaaS rotation.
- **Synergy Real Estate sub-page confirmed weak channel for Estate Mgmt** — 2 active listings both fail revenue floor, 6 sold, 0 HNW/UHNW/family-office mentions across 8 listings.
- **PCO Bookkeepers** — site live but tombstones are images (not WebFetch-extractable). Recommend monthly /blog/ cadence + direct Dan Gordon contact for William Blair index report.

## Listings Reviewed (full log)

| Source | Headline | Geo | Revenue | EBITDA | Margin | Industry | Verdict | Reject Reason |
|--------|----------|-----|---------|--------|--------|----------|---------|---------------|
| Synergy BB | Telecom Caller Trust Platform (SaaS) | USA | $2.71M ARR | $1.61M | 59% | Vertical SaaS — telecom anti-fraud | NEAR-MISS | ARR ~$2.71M just below $3M SaaS floor (disclosed); strong unit econ (59% EBITDA, 120% NRR); no active-niche corpus match |
| Business Exits | California Property Tax Consultants | California | $6.68M | $4.68M | ~70% | Marketing & Consulting / property tax | NEAR-MISS | Revenue $6.68M < $10M Services floor (disclosed); CA soft-flag |
| Business Exits | GovCon IT Firm – Judiciary & VA Contracts | undisclosed | $19.7M | $3.45M | ~17.5% | GovCon IT services/software | NEAR-MISS | Clears Services buy-box; no niche corpus match |
| Business Exits | B2B Experiential Marketing Vendor | undisclosed | $14.3M | $3.30M | ~23% | B2B experiential marketing | NEAR-MISS | Clears Services buy-box; no niche match |
| Business Exits | Government Contract ERP Service Business | undisclosed | $14M | $2.57M | ~18% | ERP services / govcon | NEAR-MISS | Clears Services buy-box; no niche match |
| Synergy BB | LED Display Solutions Company | Florida | $11.2M | $4.63M | ~41% | LED display tech/distribution | NEAR-MISS | Clears Services buy-box; no niche match |
| Empire Flippers | #84831 Digital Media — Service + Digital Product + Affiliate | undisclosed | $3.76M | $1.78M | ~47% | Digital media / affiliate / service hybrid | FLAG | Affiliate-heavy mix likely fails B2B test; revenue below floor; ambiguous service component |
| Website Closers | Category-Leading National Push-to-Talk Communications Platform | undisclosed | undisclosed | $12.5M cash flow | undisclosed | B2B push-to-talk, 30% recurring | FLAG | $160M ask + $12.5M cash flow implies revenue likely >$50M; only 30% recurring; surface for human review |
| Website Closers | SBA Pre-Qualified Procurement Services & Distribution | undisclosed | undisclosed | $200K | 36% | B2B procurement + distribution | FLAG | Cash flow $200K implies revenue well below floor; surfacing because B2B/recurring shape was on-thesis |
| Sica Fletcher | Safe Harbour Insurance Mgmt → ALKEME (closed) | MA | undisclosed | undisclosed | undisclosed | insurance brokerage | FLAG | Closed-deal tombstone (intel); ALKEME = PE-consolidator (would HARD-REJECT if active) |
| Sica Fletcher | O'Neill Associates Consulting → ALKEME (closed) | FL | undisclosed | undisclosed | undisclosed | insurance brokerage | FLAG | Closed-deal tombstone; ALKEME consolidator |
| Sica Fletcher | Surety Bonds LLC → The Hilb Group (closed) | GA | undisclosed | undisclosed | undisclosed | surety specialty brokerage | FLAG | Closed-deal tombstone; Hilb is PE-consolidator; specialty surety is sub-vertical worth tracking |
| Sica Fletcher | Quantum Resource Group → ALKEME (closed) | MD | undisclosed | undisclosed | undisclosed | insurance brokerage | FLAG | Closed-deal tombstone; ALKEME consolidator |
| Sica Fletcher | Centennial State Insurance Group → ALKEME (closed) | CO | undisclosed | undisclosed | undisclosed | insurance brokerage | FLAG | Closed-deal tombstone; ALKEME consolidator |
| MidCap Advisors | Artemis Fine Arts Services → Cadogan Tate (2023, historical) | undisclosed | undisclosed | undisclosed | undisclosed | fine art logistics & museum services | FLAG | 2023 closed deal, intel-only; direct comp for Specialty Storage niche; Cadogan Tate is the consolidator to track |
| Inside Self-Storage | Self-Storage Real Estate Acquisitions and Sales: April 2026 (roundup) | multi | undisclosed | undisclosed | undisclosed | self-storage real estate | FLAG | Intel-only; flagged for human deeper-scan to surface specialty wine/art/climate sub-deals not in headline |
| Agency Checklists | Paradiso Insurance Acquired by Trucordia (closed) | New England | undisclosed | undisclosed | undisclosed | insurance agency | FLAG | Intel-only; Trucordia = PE-consolidator; Paradiso now off-market (blacklist signal) |
| Agency Checklists | Insurance Agency M&A in Massachusetts Q1-2026 (roundup) | MA / New England | undisclosed | undisclosed | undisclosed | insurance agency M&A roundup | FLAG | Intel-only; quarterly roundup; deeper scan needed for any specialty/HNW/personal-lines targets |
| Agency Checklists | OPTIS: Insurance Agency M&A Down 6% in Q1 2026 | national | undisclosed | undisclosed | undisclosed | insurance agency M&A market report | FLAG | Intel-only; market-pace data: 148 deals Q1, -6% YoY; PE still driving activity |
| MarshBerry News | Insurance Growth Network → People Corporation (sell-side) | undisclosed | undisclosed | undisclosed | undisclosed | insurance brokerage partnership | FLAG | Intel-only; consolidator-side deal pattern |
| MarshBerry News | Long Run Wealth Advisors → Mercer Global Advisors (sell-side) | undisclosed | undisclosed | undisclosed | undisclosed | wealth advisory (not P&C) | FLAG | Intel-only; out-of-niche but tracked for MarshBerry deal-flow pattern |
| MarshBerry News | The Richards Group → IMA Financial Group (sell-side) | undisclosed | undisclosed | undisclosed | undisclosed | insurance brokerage partnership | FLAG | Intel-only; IMA is mid-market consolidator; Richards Group now off-market |
| IA Magazine | Insurance Agency M&A Falls 6% in First Quarter | national | undisclosed | undisclosed | undisclosed | insurance agency M&A market report | FLAG | Intel-only; Q1 2026 -6% data point cross-confirmed against OPTIS |
| IA Magazine | Insurance Agency M&A and Preventing E&O Claims | n/a | undisclosed | undisclosed | undisclosed | insurance M&A operational guidance | FLAG | Intel-only; operational article, not deal flow |
| IA Magazine | Art of The Exit: Ensuring a Smooth Transition When It's Time to Sell | n/a | undisclosed | undisclosed | undisclosed | agency sale guidance | FLAG | Intel-only; owner-prep content; useful as broker-channel context |
| Business Exits | Midwest-Based Multi-Location Wellness Practice | Midwest | $21.3M | $12.97M | ~61% | Healthcare/wellness multi-location | HARD-REJECT | Physician-practice hard-exclude |
| Business Exits | Ireland Construction Business | Ireland | €25M | €6.15M | ~25% | Construction | HARD-REJECT | Construction hard-exclude; non-US |
| Business Exits | Luxury Wedding Venue | undisclosed | $3.18M | $2.35M | ~74% | Wedding venue / hospitality | HARD-REJECT | Hospitality hard-exclude; revenue below floor |
| Business Exits | Metal Building Supplier with US Manufacturing | undisclosed | $33.7M | $3.97M | ~12% | Construction / manufacturing | HARD-REJECT | Capital-intensive manufacturing + construction-adjacent |
| Business Exits | Texas Non-Emergency Medical Transport | Texas | $7.74M | $2.87M | ~37% | NEMT/medical transport | HARD-REJECT | Revenue $7.74M < $10M floor (disclosed); medical/transport labor-heavy |
| Business Exits | California Staffing Firm with Recurring Revenue | California | $7.82M | $3.20M | ~41% | Staffing services | HARD-REJECT | Revenue < $10M floor (disclosed); CA soft-flag |
| Business Exits | Northeast Commercial Contractor (Healthcare/Financial) | Northeast | $22M | $2.78M | ~13% | Commercial contracting/construction | HARD-REJECT | Construction hard-exclude |
| Business Exits | Atlanta Residential Plumbing & Septic | Atlanta GA | $11.7M | $2.41M | ~21% | Residential plumbing/septic | HARD-REJECT | Construction/labor-heavy hard-exclude |
| Business Exits | Design & Build Studio for Themed Props | undisclosed | $10M | $3.06M | ~31% | Design/build manufacturing | HARD-REJECT | Capital-intensive manufacturing + construction hard-exclude |
| Business Exits | Texas HVAC Company | Texas | $22M | $2.28M | ~10% | Residential HVAC | HARD-REJECT | Construction/labor-heavy hard-exclude |
| Business Exits | Cell Phone Tower Installation & Repair | undisclosed | $8.93M | $1.95M | ~22% | Tower install/repair construction | HARD-REJECT | Construction hard-exclude + revenue <$10M floor |
| Business Exits | Military and Aerospace Parts Distributor | undisclosed | $8.23M | $1.90M | ~23% | Aerospace/military parts distribution | HARD-REJECT | Revenue < floor; aerospace excluded |
| Business Exits | Window Manufacturer | undisclosed | $4.90M | $1.54M | ~31% | Window manufacturing/retail | HARD-REJECT | Capital-intensive manufacturing + below floor |
| Business Exits | Arizona Addiction Treatment | Arizona | $4.45M | undisclosed | undisclosed | Healthcare addiction treatment | HARD-REJECT | Physician-practice hard-exclude + below floor |
| Business Exits | Southeast Electrical Contractor | Southeast | $5.28M | undisclosed | undisclosed | Electrical contracting | HARD-REJECT | Construction hard-exclude + below floor |
| Business Exits | Pet Travel Products Distribution | undisclosed | $1.67M | undisclosed | undisclosed | Consumer retail / pet | HARD-REJECT | Consumer retail/DTC + below floor |
| Business Exits | Nevada Fireproofing Contractor | Nevada | $3.06M | undisclosed | undisclosed | Construction/fireproofing | HARD-REJECT | Construction + below floor |
| Business Exits | Government Promotional Products | undisclosed | $8.18M | undisclosed | undisclosed | Promotional retail | HARD-REJECT | Consumer/retail + below floor |
| Business Exits | Canadian Recruitment Agency | Canada | $2.28M CAD | undisclosed | undisclosed | Recruitment / staffing | HARD-REJECT | Non-US + below floor |
| Business Exits | Florida Med Spa | Florida | $1.07M | undisclosed | undisclosed | Med spa / healthcare | HARD-REJECT | Physician-practice + below floor |
| Business Exits | Landscape Architecture | undisclosed | $5.5M | undisclosed | undisclosed | Landscape architecture / construction | HARD-REJECT | Construction hard-exclude + below floor |
| Business Exits | CA Multi-Location Gym Franchise | California | $2.07M | undisclosed | undisclosed | Gym franchise | HARD-REJECT | Franchise + hospitality-adjacent + below floor |
| Business Exits | Restaurant/Juice Bar Franchise | undisclosed | $4.14M | undisclosed | undisclosed | Restaurant/juice franchise | HARD-REJECT | Restaurant + franchise hard-excludes |
| Business Exits | Colorado Regenerative Medicine | Colorado | $895K | undisclosed | undisclosed | Healthcare regenerative | HARD-REJECT | Physician-practice + below floor |
| Business Exits | Bay Area Roofing | Bay Area CA | $2.5M | undisclosed | undisclosed | Construction/roofing | HARD-REJECT | Construction + below floor |
| Business Exits | Texas Home Health Staffing | Texas | $2.49M | undisclosed | undisclosed | Healthcare staffing | HARD-REJECT | Healthcare staffing + below floor |
| Synergy BB | Seafood Processing And Distribution | Portugal | $165M | $5.9M | ~3.6% | Seafood processing/distribution | HARD-REJECT | Revenue >$50M ceiling; margin <10% floor; non-US; capital-intensive |
| Synergy BB | Oil & Gas Equipment Rental & Trucking | Midland TX | $15.3M | $6.56M | ~43% | Oil & gas equipment rental | HARD-REJECT | Capital-intensive + construction/field-labor hard-exclude |
| Synergy BB | Concrete & Masonry Contractor | Florida | $18.5M | $5.7M | ~31% | Concrete/masonry construction | HARD-REJECT | Construction hard-exclude |
| Synergy BB | Commercial Plumbing Company | New Jersey | $13.6M | $4.03M | ~30% | Commercial plumbing | HARD-REJECT | Construction/field-labor hard-exclude |
| Synergy BB | OB/GYN & Urogynecology Multi-Physician Clinic | Central FL | $6.58M | $3.38M | ~51% | OB/GYN physician practice | HARD-REJECT | Physician-practice hard-exclude; revenue below floor |
| Synergy BB | Precision Machine Shop | Arizona | $7.5M | $2.3M | ~31% | Precision machining | HARD-REJECT | Capital-intensive manufacturing + below floor |
| Synergy BB | Ethanol Producer | India | $10.5M | $3M | ~29% | Ethanol manufacturing | HARD-REJECT | Capital-intensive manufacturing + non-US |
| Synergy BB | Industrial Minerals Producer | Peru | $7M | $4.5M | ~64% | Mining/minerals manufacturing | HARD-REJECT | Capital-intensive + non-US + below floor |
| Synergy BB | NYC High-End Renovation Design/Build | NYC | $8.5M | $2.34M | ~28% | Renovation/design-build | HARD-REJECT | Construction hard-exclude + below floor |
| Synergy BB | Tech-Enabled Behavioral Health Firm | DC | $5M | $1M | ~20% | Behavioral health + tech | HARD-REJECT | Healthcare/physician-adjacent + below floor |
| Synergy BB | Admissions Consulting Practice (Remote) | USA remote | $2M | $1.3M | ~65% | Admissions consulting | HARD-REJECT | Revenue $2M < $10M Services floor |
| Synergy BB | Garment Manufacturing | Bangladesh | undisclosed | undisclosed | undisclosed | Garment manufacturing | HARD-REJECT | Non-US + capital-intensive manufacturing |
| Synergy BB | Railroad Construction | MO | undisclosed | undisclosed | undisclosed | Railroad construction | HARD-REJECT | Construction hard-exclude |
| Synergy BB | B2B Health & Beauty Manufacturer | Dubai | undisclosed | undisclosed | undisclosed | Manufacturing | HARD-REJECT | Non-US + manufacturing |
| Synergy BB | Specialty Copper Alloy Wire | India | undisclosed | undisclosed | undisclosed | Specialty wire mfg | HARD-REJECT | Non-US + capital-intensive manufacturing |
| Synergy BB | Travel & Tourism | Saudi Arabia | undisclosed | undisclosed | undisclosed | Travel / tourism | HARD-REJECT | Non-US + hospitality |
| Synergy BB | 40-Year Pediatric Practice | NY | undisclosed | undisclosed | undisclosed | Pediatric physician practice | HARD-REJECT | Physician-practice hard-exclude |
| Synergy BB | Utility Construction | Nassau NY | undisclosed | undisclosed | undisclosed | Utility construction | HARD-REJECT | Construction hard-exclude |
| Empire Flippers | (15 FBA / eCommerce / DTC consumer listings, batch) | undisclosed | varies | varies | varies | Consumer retail / DTC eCommerce / FBA | HARD-REJECT | Consumer retail/DTC hard-exclude (15 listings batch-rejected) |
| Empire Flippers | (2 YouTube content brands, batch) | undisclosed | varies | varies | varies | Content / digital media | HARD-REJECT | Consumer/B2C + DTC content + below floor |
| Empire Flippers | (1 cryptocurrency newsletter) | undisclosed | varies | varies | varies | Crypto/finance content | HARD-REJECT | B2C consumer content + below floor |
| Empire Flippers | (1 music digital product) | undisclosed | varies | varies | varies | Digital product / music | HARD-REJECT | Consumer/DTC digital product + below floor |
| Empire Flippers | (1 finance display-ads property) | undisclosed | varies | varies | varies | Display-ads / finance content | HARD-REJECT | B2C consumer content + below floor |
| Website Closers | Towels & Socks eCommerce | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Collectible Merchandise | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC collectibles | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Proprietary Home Products | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC home goods | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Guided Fitness Journals | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC fitness content | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Multi-Label Women's Apparel | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC apparel | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Global B2B Advertising Franchise | undisclosed | undisclosed | undisclosed | undisclosed | Advertising franchise | HARD-REJECT | Franchise hard-exclude |
| Website Closers | Military/Firing Range Apparel | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC apparel | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | Vineyard & Brewery (NZ) | New Zealand | undisclosed | undisclosed | undisclosed | Hospitality / beverage | HARD-REJECT | Hospitality + non-US |
| Website Closers | Special Occasion Gifts/Jewelry | undisclosed | undisclosed | undisclosed | undisclosed | Consumer DTC gifts/jewelry | HARD-REJECT | Consumer retail/DTC hard-exclude |
| Website Closers | European Furniture Brand | Europe | undisclosed | undisclosed | undisclosed | Consumer DTC furniture | HARD-REJECT | Consumer retail/DTC + non-US |
| Website Closers | SBA Pre-Qualified AI SaaS — Humanizing AI Content | undisclosed | $600K ARR | $403K | 63% | Horizontal AI SaaS / prosumer | HARD-REJECT | ARR $600K << $3M SaaS floor; horizontal/prosumer |
| Synergy BB Real Estate | Event Rental Company: Full-Service | South Florida | $1.63M | $486K | undisclosed | Event rental | HARD-REJECT | Revenue < $10M floor; event rental is hospitality-adjacent, not estate management |
| Synergy BB Real Estate | Short-Term Rental Property Mgmt Co (80+ locations) | Midwest | $3.23M | $370K | ~11% | Short-term rental property management | HARD-REJECT | Revenue < $10M floor; STR/Airbnb mgmt is consumer-rental adjacent, not HNW estate mgmt |
| GP Bullhound | AB Tasty + VWO merger (Everstone Capital) | Europe | undisclosed | undisclosed | undisclosed | Experimentation / CRO software | HARD-REJECT | PE-backed (Everstone Capital); horizontal CRO, not luxury vertical |
| GP Bullhound | The Bliss Group → Highwire (sale) | US | undisclosed | undisclosed | undisclosed | PR / digital services | HARD-REJECT | PR/comms agency, not software, no niche match |
| GP Bullhound | Instaleap → Instacart (closed) | Global | undisclosed | undisclosed | undisclosed | Omnichannel retail tech | HARD-REJECT | Acquired by strategic — closed deal; consumer-grocery tech, horizontal |
| GP Bullhound | Sdui fundraise (Bain Capital) | Europe | undisclosed | undisclosed | undisclosed | Education software | HARD-REJECT | Bain Capital growth = institutional; EdTech not in luxury vertical corpus |
| GP Bullhound | Peak → UiPath (acquisition) | UK/US | undisclosed | undisclosed | undisclosed | AI decision intelligence | HARD-REJECT | Closed deal to public strategic; horizontal AI |
| GP Bullhound | Flo Health investment (General Atlantic, $200M) | US | undisclosed | undisclosed | undisclosed | Consumer femtech | HARD-REJECT | $200M GA investment; B2C femtech (SaaS hard-exclude) |
| GP Bullhound | Runna → Strava (acquisition) | UK/US | undisclosed | undisclosed | undisclosed | Running app B2C | HARD-REJECT | B2C consumer fitness, hard-excluded |

## Source Scorecard

| Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date |
|--------|----------|--------|------|-------------------|---------|-----------------|
| Business Exits | General | active | 200 | 30 | 0 | — |
| Synergy Business Brokers | General | active | 200 | 20 | 0 | — |
| Empire Flippers | General | active | 200 | 21 | 0 | — |
| Website Closers | General | active | 200 | 13 | 0 | — |
| Rejigg | General | blocked (verified) | 200 (homepage) / NDA-gated marketplace | 0 | — | — |
| BizBuySell | General | blocked (verified) | edge-WAF "Access Denied" across 4 attempts (homepage / browse-index / insurance category / keyword search) | 0 | — | — |
| Everingham & Kerr | General — email-only | not scanned this run | n/a | 0 | — | — |
| Flippa | General — email-only (web broken) | not scanned this run | n/a (web JS-shell, email channel only) | 0 | — | — |
| Quiet Light | General — email-only (Cloudflare) | not scanned this run | n/a (web 403, email channel only) | 0 | — | — |
| Viking Mergers | General — email-only | not scanned this run | n/a | 0 | — | — |
| DealForce | General — email alerts | not scanned this run | n/a | 0 | — | — |
| IAG M&A Advisors | General — email alerts | not scanned this run | n/a | 0 | — | — |
| SMB Deal Hunter | General — newsletter blast | not scanned this run | n/a | 0 | — | — |
| Searchfunder | General — community + email digest | not scanned this run (alerts pending enablement) | n/a | 0 | — | — |
| Sica Fletcher | Niche-Specific (Insurance) | active | 200 | 5 | 0 | — |
| Synergy BB Real Estate | Niche-Specific (Estate Mgmt) | active | 200 | 8 (2 active, 6 sold) | 0 | — |
| GP Bullhound | Niche-Specific (Vertical SaaS) | active | 200 | 7 | 0 | — |
| PCO Bookkeepers | Niche-Specific (Pest) | active | 200 | 0 actionable (tombstones are images; no parseable 2026 mandates) | 0 | — |
| MidCap Advisors | Niche-Specific (Storage) intel | active | 200 | 11 (most recent 2026 deals: 0; Q4 2025 most recent activity) | 0 | — |
| Inside Self-Storage | Intel (Storage) | active | 200 | 20 (1 specialty-relevant flag — April monthly roundup) | 0 | — |
| CMM Online | Intel (Cleaning) | active | 200 | 10 (0 deal stories) | 0 | — |
| Agency Checklists | Intel (Insurance) | active | 200 | 3 | 0 | — |
| Anticimex US | Intel (Pest blacklist) | active | 200 | 0 (page is owner-marketing, no announcement log; need press release archive instead) | 0 | — |
| MarshBerry News | Intel (Insurance) | active | 200 (after `/news-insights/` 404 → `/news/` path correction) | 3 | 0 | — |
| IA Magazine | Intel (Insurance) | active | 200 | 3 | 0 | — |

## Volume Check

- Deals surfaced today: 0
- 7-day rolling average: not yet calculated (insufficient prior fingerprint history; store size 0 bytes — populated from 2026-04-22 forward as runs accumulate)
- Target: 1-3/day — **BELOW TARGET**
- Drivers: (1) email channel not yet scanned today (email-intel artifact lands at 7am ET — afternoon top-up will pick up Everingham & Kerr / Quiet Light / Flippa / Viking / DealForce / IAG / SMB Deal Hunter inbound), (2) BizBuySell hard-blocked at edge across 4 distinct agent-browser attempts (Access Denied DOM, no captcha surface), (3) niche-specific channels structurally weak today — Sica/Synergy-RE/GP-Bullhound confirmed wrong tier or wrong corpus, no 2026 fine-art-logistics deals at MidCap, no specialty-storage signal at Inside Self-Storage, and no deal flow at CMM
- Action items for follow-up runs (NOT for Slack today): (a) re-evaluate Synergy Real Estate sub-page and GP Bullhound for daily rotation given zero-signal pattern, (b) consider Anticimex press-release archive path instead of `/selling-your-business/` for blacklist signal, (c) move PCO Bookkeepers to monthly cadence + direct Dan Gordon outreach for William Blair index, (d) BizBuySell verified blocked across 4 web-attempts — keep on General tab if email channel remains active per `feedback_blocked_sources_tab_rule`
