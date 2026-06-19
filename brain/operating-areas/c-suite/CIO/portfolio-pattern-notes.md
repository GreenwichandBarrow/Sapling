# Search Fund Portfolio Pattern Notes

Date: 2026-06-15

Approved source set:
- Pacific Lake Partners: https://www.pacificlake.com/operating-companies
- BK Growth: https://www.bkgrowth.com/portfolio
- TTCER Partners: https://ttcerpartners.com/

Scope control:
- This is an approved-source database, not a broad market map.
- Rows in `portfolio-company-database.csv` are curated seed rows for analysis.
- Rows in `raw-bkgrowth-extract.csv` are the full BK Growth approved-source extraction queue from its page HTML; they are not all promoted into the curated database.

Early Pattern Read

1. Vertical and workflow software repeats across all three approved sources.
   Examples: Merit Holdings, Banyan Software, Datacor, FluidSecure, NovoPath, StaffScheduleCare, TaskRay, Triyam, Team Management Systems, Scribbles Software, IT Pipes.
   Fit read: attractive pattern, especially where software is tied to regulated, infrastructure, healthcare, fleet, education, or field-service workflows.

2. Compliance-driven services/training/security appears repeatedly.
   Examples: Kantola, CyberData Pros, Eventus, Mas Labor, Advanced Aircrew Academy, Page Vault, Triyam.
   Fit read: strong G&B signal when demand is recurring, regulatory, safety-critical, or embedded in customer workflows.

3. Technical B2B and infrastructure services show up as high-signal non-software patterns.
   Examples: O&W Heat Treat, ASI Group, Central Storage & Warehouse, Peak Propane, ADAS Safe, Atlantic Duct Cleaning, Allied Electric.
   Fit read: worth studying where revenue is repeat/contracted, markets are fragmented, and customer concentration is manageable.

4. Healthcare services and healthcare software are common, but fit varies.
   Stronger fit signals: healthcare software/data workflows such as NovoPath, Triyam, StaffScheduleCare, FreeBalance-adjacent public financial management if treated as govtech rather than healthcare.
   Fit cautions: dermatology, fertility, elective procedures, ketamine/wellness, pediatric/dental clinics may be consumer/provider-dependent and less aligned unless recurring payer/referral dynamics are unusually durable.

5. Consumer-facing education, wellness, retail-like services, and experiential businesses should stay in the database but be tagged rather than prioritized.
   Examples: WonderPlay Brands, Christopher Kimball's Milk Street, Spanish Schoolhouse, Apex Fundraiser, 4EverYoung.
   Fit read: useful boundary cases from respected portfolios, but not obvious G&B niche-intelligence candidates.

Recommended Next Study Queue

1. Fuel/fluid/fleet operations software and monitoring
   Source signals: FluidSecure, Tank Track, Frotcom.
   Why: recurring software/monitoring, operationally embedded, boring B2B customers.

2. Compliance and safety training platforms
   Source signals: Kantola, Advanced Aircrew Academy, Page Vault.
   Why: recurring regulatory/safety demand, content/workflow embeddedness, possible fragmented provider landscape.

3. Infrastructure inspection, maintenance, and industrial specialty services
   Source signals: ASI Group, O&W Heat Treat, IT Pipes, Central Storage & Warehouse.
   Why: mission-critical, technical, potentially repeat-driven, harder to displace.

4. Healthcare data retention and lab/records workflow software
   Source signals: Triyam, NovoPath, StaffScheduleCare.
   Why: compliance-critical, high switching costs, recurring software/services potential.

5. Cybersecurity/privacy managed services
   Source signals: CyberData Pros, Eventus, Stage2Data.
   Why: recurring, compliance-driven, fragmented, but customer concentration and labor intensity need scrutiny.

Suggested Action

RECOMMEND: Run `niche-intelligence` first on fuel/fluid/fleet operations software and monitoring.

Reason: it has the clearest cross-source cluster from approved portfolios, likely recurring revenue, operational criticality, and a boring B2B customer base without immediately drifting into consumer healthcare or pure SaaS abstraction.

## Addendum: Saltoun and Anacapa Approved Sources

Added approved sources:
- Saltoun Capital Partners: https://www.saltouncapital.com/portfolio
- Anacapa Partners: https://anacapapartners.com/site/global/anacapa/portfolio/index.gsp

New pattern read:

6. Anacapa adds a clear outsourced back-office and route-based services pattern.
   Examples: Advanced Network Solutions, Charter Impact, HelpSide, Answer1, Spivey Services.
   Fit read: attractive where services are contracted, recurring, compliance-adjacent, and delivered to business or institutional customers rather than consumers.

7. Environmental and regulated field services are now a stronger cluster.
   Examples: Dragonfly Pond Works, Lion Industrial Resources, Castle Tire Recycling, VDCI, ASI Group, O&W Heat Treat.
   Fit read: likely high-fit for G&B if markets are fragmented and customer concentration is manageable.

8. Saltoun reinforces vertical market software and ETA/search funds as the dominant respected-portfolio pattern.
   Examples: Datacor, Banyan Software, Max RTE, FileOnQ, Ctaima, Performance Systems Integration.
   Fit read: the most repeated software pattern is not generic SaaS; it is niche workflow software tied to regulated, technical, operational, or back-office workflows.

Updated study queue:

1. Fuel/fluid/fleet operations software and monitoring
   Source signals: FluidSecure, Tank Track, Frotcom.
   Why: clean cross-source software/monitoring cluster with recurring revenue potential and operational B2B criticality.

2. Stormwater, vector, tire/waste, and industrial environmental services
   Source signals: Dragonfly Pond Works, VDCI, Lion Industrial Resources, Castle Tire Recycling.
   Why: boring services, regulatory/public-health demand, recurring maintenance potential, fragmented local markets.

3. Compliance and safety training/software
   Source signals: Kantola, Advanced Aircrew Academy, Workplace Answers, eCompliance, Ctaima, PEC Safety.
   Why: regulatory/safety-driven demand with recurring training, certification, or workflow software potential.

4. Outsourced SMB and vertical back-office services
   Source signals: Advanced Network Solutions, Charter Impact, HelpSide, Answer1.
   Why: recurring service contracts, operational importance, and vertical specialization potential.

RECOMMEND: Keep fuel/fluid/fleet operations software as the first `niche-intelligence` run, then run stormwater/vector/industrial environmental services as the first non-software services study.

## Addendum: WSC, Trilogy, Search Fund Partners, and Relay

Added approved sources:
- WSC & Company: https://wscandcompany.com/portfolio/
- Trilogy Search Partners: https://trilogy-search.com/portfolio
- Search Fund Partners: https://www.searchfunds.net/portfolio
- Relay Investments: https://www.relayinvestments.com/portfolio

New pattern read:

9. Fire, life-safety, gas detection, and facility safety services are now a major non-software cluster.
   Examples: ACES Monitoring, Multi-Service-Gummersbach, All Essential Fire & Security, Performance Systems Integration, The Hose Monster Company.
   Fit read: high-priority G&B pattern because it combines code/regulatory demand, recurring inspection/maintenance, local fragmentation, and mission-critical service.

10. Public-sector and regulated workflow software repeats across investors.
   Examples: FileOnQ, Clariti, BP Logix, AdComp Systems, Page Vault, LeCorpio.
   Fit read: strong evidence that respected search investors like niche software embedded in government, legal, evidence, licensing, and compliance workflows.

11. Property/utility back-office and submetering services are emerging as a concrete services niche.
   Examples: Utility Management Solutions, Premiere Property Services, Singu, Charter Impact, Botanical Designs.
   Fit read: attractive where buyer is institutional and contracts recur; lower priority when work is labor-only, discretionary, or property-cycle exposed.

12. Specialty industrial and mission-critical manufacturing services deserve a separate watchlist.
   Examples: BSU Electronics, P&S Machining and Fabrication, IMMSA, Dynamic Rubber, O&W Heat Treat.
   Fit read: technically attractive but diligence must focus on customer concentration, certifications, cyclicality, and capex.

Updated recommendation:

RECOMMEND: After fuel/fleet monitoring, prioritize fire/life-safety and facility safety services before broader environmental services.

Reason: the newly approved sources create a denser, more directly G&B-relevant cluster around mandatory inspection, testing, calibration, repair, and safety-code compliance.

## Addendum: Hunter, Endurance, Next Coast, Futaleufu, Maven, and Peterson

Added approved sources:
- Hunter Search Capital: https://www.huntersearchcapital.com/portfolio-companies
- Endurance Search Partners: https://www.endurancesearchpartners.com/investments
- Next Coast Ventures: https://www.nextcoastventures.com/portfolio
- Futaleufu Partners: https://futaleufu-partners.com/our-investments/
- Maven Equity Partners: https://www.mavenequitypartners.com/portfolio
- Peterson Partners: https://www.petersonpartners.com/portfolio/

New pattern read:

13. Managed IT, cybersecurity, and infrastructure software/services are now a stronger cluster.
   Examples: 360 Smart Networks, Advanced Network Solutions, Beryllium InfoSec, Judy Security, No-IP, ISI Telemanagement Solutions.
   Fit read: attractive where revenue is recurring and the provider is embedded in SMB or regulated-customer operations; watch labor intensity and commoditization.

14. Industrial distribution and equipment service is emerging separately from generic field services.
   Examples: Canadian Industrial Pumps, Emission & Cooling Solutions, Seqent, O&W Heat Treat, P&S Machining and Fabrication, IMMSA.
   Fit read: strong if tied to maintenance/replacement cycles, technical certifications, or mission-critical industrial workflows.

15. Customs, tax, claims, and property/insurance administration are repeated specialty back-office services.
   Examples: Capin-Vyborny, CITTA Brokerage, Resolute Property Tax Solutions, Reliable Premium Management, Automotive Business Solutions, Atticus.
   Fit read: attractive when compliance-driven, repeatable, and B2B; diligence should focus on customer concentration and dependence on contingency fees.

16. Broad venture portfolios are useful only as pattern corroboration.
   Examples: Next Coast and Peterson add useful signals in safety/risk software, emergency communications, fleet compliance, cybersecurity, and hospital facilities software, but should not drive the database volume or niche prioritization alone.

Updated recommendation:

RECOMMEND: Move fire/life-safety and facility safety services to the top non-software services study queue, ahead of broader environmental services.

Reason: Endurance, Trilogy, Relay, WSC, and Peterson now all reinforce mandatory inspection, monitoring, alarm, gas detection, and life-safety services as a dense recurring-services pattern.

## Addendum: Footbridge, M2O, and Aspect

Added approved sources:
- Footbridge Partners: https://www.footbridgepartners.com/investments
- M2O Inc.: https://www.m2oinc.com/our-portfolio/
- Aspect Investors: https://www.aspectinvestors.com/operating-companies/

New pattern read:

17. M2O materially strengthens regulated workflow software as the dominant software theme.
   Examples: Anaqua, Anterra, Beaconcure, FieldFlo, GovSoft, Datacor, Cornerstone Support.
   Fit read: the attractive pattern is not generic SaaS; it is software embedded in legal/IP, construction accounting, clinical trials, public safety, compliance, and specialty contractor workflows.

18. Outsourced technical infrastructure services now has a clearer niche shape.
   Examples: Agasus/Voke, Harbor IT, ISPN, 360 Smart Networks, Advanced Network Solutions, No-IP.
   Fit read: recurring infrastructure support to SMBs, rural ISPs, or enterprise endpoint fleets may fit if contracts are sticky and labor can scale.

19. Marine/port services and cross-border/logistics services are becoming watchlist clusters.
   Examples: DCL Inc., Honolulu Ship Supply, Capin-Vyborny, TACNA, Cloudstore/EZRack as adjacent logistics infrastructure.
   Fit read: attractive where services are essential, recurring, and geographically protected; diligence must test customer concentration and cyclicality.

20. Industrial support products/services continue to appear across respected portfolios.
   Examples: Checksum, Orion Cordage, Canadian Industrial Pumps, O&W Heat Treat, P&S Machining, BSU Electronics.
   Fit read: promising but diligence-heavy because certifications, customer concentration, and capex intensity can dominate returns.

Updated recommendation:

RECOMMEND: Keep fire/life-safety and facility safety services as the top non-software `niche-intelligence` candidate; add regulated workflow software as the top software pattern watchlist rather than one single software niche.

Reason: M2O and Aspect add strong evidence that high-quality investors favor compliance-heavy, workflow-embedded software across multiple verticals, while services-side density still looks strongest in mandatory safety/inspection/monitoring.
