---
schema_version: 1.0.0
date: 2026-07-21
task: Headless Tuesday niche-intelligence run
agents: [orchestrator, niche-intel-recent, niche-intel-historical, niche-intel-synthesizer, niche-intel-identifier, niche-intel-onepager, niche-intel-scorer, niche-intel-tracker]
status: completed
linked_trace: brain/outputs/2026-07-21-niche-intelligence-report.md
run_metadata:
  runner: Codex/systemd
  mode: tuesday
---

# Agent Chatroom: Niche Intelligence — 2026-07-21

## Coordination Log

## [22:30] orchestrator
Starting headless Tuesday run under Codex/systemd. Mandatory sequence: RECENT + HISTORICAL gather in parallel, synthesize, identify, one-pagers, industry scorecards, tracker update, markdown report, JSON integrity sidecar.
→ READY

## [23:13] orchestrator
All required Tuesday headless steps completed: gather, synthesize, identify, one-pagers, industry scoring, tracker update, markdown report, and JSON sidecar. Wrapper validator passed for 2026-07-21.
→ CLOSE

## [23:10] orchestrator
All required Tuesday headless steps completed: gather, synthesize, identify, one-pagers, industry scoring, tracker update, markdown report, and JSON sidecar. Final artifacts: `brain/outputs/2026-07-21-niche-intelligence-report.md` and `brain/trackers/niches/niche-intel-2026-07-21.json`.
→ CLOSE

## [niche-intel-onepager] — 2026-07-21 22:54 EDT
**Niche:** Yacht Property Management for Private Yacht Owners in Coastal HNW Markets
**Status:** complete

Created the professional one-pager from the local customs bonds template, preserving the table-based layout and template shapes. Assessment and Status are both `Pending Scoring`; no score was included. The generated one-pager uses G&B/Greenwich & Barrow framing only and contains no "Kay" references.

- Local path: `/tmp/yacht-property-management-onepager.pptx`
- Drive folder ID: `1rlCxKK2lYH2XHz33q17ZzhO9Gf10ukSQ`
- Drive folder link: https://drive.google.com/drive/folders/1rlCxKK2lYH2XHz33q17ZzhO9Gf10ukSQ
- Uploaded PPTX ID: `1ksSfraVCWKxlBen-1GKoLe0VvY6_D8MA`
- Uploaded PPTX link: https://docs.google.com/presentation/d/1ksSfraVCWKxlBen-1GKoLe0VvY6_D8MA/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- Upload verification: `gog drive get` confirmed MIME type `application/vnd.openxmlformats-officedocument.presentationml.presentation`, parent `1rlCxKK2lYH2XHz33q17ZzhO9Gf10ukSQ`, size `165802`.
- Upload errors: Google Drive connector was unavailable (`USER_NOT_LOGGED_IN`), then retry through `source /home/ubuntu/projects/Sapling/scripts/op-env.sh && gog ...` succeeded.

### Key Research Findings

- The niche is distinct from asset-light yacht transport because the customer is the yacht owner/family office and the recurring behavior is ongoing vessel stewardship: maintenance, crew, compliance, financial administration, vendor coordination, and owner reporting.
- Market growth is moderate/strong: Fortune Business Insights estimates yacht management services at $1.25B in 2025, growing to $2.05B by 2034 at 5.7% CAGR; Mordor estimates the U.S. luxury yacht market at $4.82B in 2025, growing to $7.16B by 2030 at 8.25% CAGR.
- Service recurrence is high in behavior even where contracts need diligence: management pages consistently describe planned maintenance, inspections, compliance, accounting, budgeting, crew, and documentation functions.
- Target-pool caveat remains material: likely enough named regional operators to justify a build, but many may be small captain-service or yacht-care shops below platform scale.
- PE saturation appears lower than pest, fire/life safety, or insurance brokerage, but strategic yacht brokerages and global management houses can bundle this service and may be competitors/acquirers.

### Source Coverage

- Gathering/internal: identifier block in `brain/traces/agents/2026-07-21-niche-intelligence.md`.
- Market sizing/fleet base: Fortune Business Insights, Mordor Intelligence, USCG 2024 Recreational Boating Statistics, Monaco Yacht Show / SuperYacht Times 2025 market report.
- Service model/company examples: IYC BLUE, Denison Yacht Management, Elite Yacht USA, Onboard Marine, Blue Oceans Yachting, Moran Yacht & Ship.
- One-pager source implementation: second Sources slide includes 11 live hyperlink entries covering every source used.

→ READY

---
## [niche-intel-historical] — 2026-07-21 22:35 EDT
**Source:** Historical calls, historical Gmail, OneNote availability check, ChatGPT export availability check
**Status:** partial

### Signals Found

#### Trade Credit, Customs Bonds & Cargo Insurance Brokerage
- **Sources:** Jeremy Black Gmail thread `Insurance Contact & Two Insurance Ideas` (2026-02-03/04); `brain/outputs/2026-03-15-trade-credit-insurance-niche-research.md`; `brain/calls/2026-02-09-camilla-i-kay-tb.md`; active tracker context lists this as already live in WEEKLY REVIEW.
- **Key intelligence:** Jeremy Black specifically named Trade Risk Group for customs bonds/cargo insurance and trade credit insurance as under-utilized in the US, recurring, and bank/CFO-education-led. The March research brief estimated US broker TAM at roughly `$200M-$400M`, gross margins `60%-80%`, EBITDA margins `20%-35%`, 90%+ retention as a bull-case target, and only `30-50` US specialists as a bear-case constraint.
- **Companies / carriers / contacts:** Jeremy Black; Trade Risk Group; Trade Acceptance Group; Meridian/Texel; Euler Hermes/Allianz Trade; Atradius; Coface; Kay's brother as marine-logistics validation source.
- **Lifecycle status:** proposed by Jeremy Black -> researched by Camilla/G&B -> promoted into active tracker context. Not a new candidate; useful as strong historical validation and as an example of a source-backed insurance-infrastructure niche.
- **Why overlooked:** The signal began as a warm-contact email rather than a broker teaser, and the attractive recurring economics sit inside insurance distribution, where broader insurance-brokerage multiples/QSBS concerns created hesitation.

#### Truck Licensing & Compliance Platform / Transportation Compliance Services
- **Sources:** SMB Deal Hunter Gmail newsletter (2026-05-26) read from thread `19e656820ec74fd6`; prior niche-intel output and active tracker context list Truck Licensing & Compliance Platform as already live.
- **Key intelligence:** Newsletter described a California/remote trucking licensing and compliance platform with annual recurring filings, federal/state registrations, business formations, drug/alcohol testing programs, truck plates, and driver qualification documentation. Deal data: `$1.039M` revenue, `$412K` EBITDA, `$1.425M` asking price, established 2021. The writeup framed filings as annual/repeating and compliance risk as a retention driver.
- **Companies / contacts:** SMB Deal Hunter / Helen Guo; no named operator exposed beyond listing.
- **Lifecycle status:** proposed from newsletter/deal-flow signal -> already in WEEKLY REVIEW. Not new, but historical Gmail confirms the original source had concrete economics.
- **Why overlooked:** The EBITDA is below classic buy-box size and the company is young, so it reads as proof of business-model existence rather than a standalone platform target.

#### Geotechnical Engineering & Construction Materials Testing
- **Sources:** Everingham & Kerr Gmail teaser (2026-06-25) thread `19f00b55a11762b4`; active tracker context lists Geotechnical Engineering & Construction Materials Testing as already live.
- **Key intelligence:** NJ-based geotechnical engineering services company with over `$3.6M` revenue and approximately `$1M` normalized EBITDA. Services include geotechnical engineering investigations during design phase plus construction materials testing/inspections during construction phase. Geography: NJ, PA, DE.
- **Companies / contacts:** Everingham & Kerr; unnamed NJ geotechnical/CMT company.
- **Lifecycle status:** broker-sourced deal signal -> already in WEEKLY REVIEW. Not a net-new niche.
- **Why overlooked:** It may have been treated as one broker deal rather than a broader compliance/professional-services lane. It also has construction-cycle exposure, so it needs a tighter recurring/reoccurring revenue test.

#### HOA / Community Association Management
- **Sources:** Everingham & Kerr Gmail teaser (2026-06-03) thread `19e8f736222f4096`; active tracker context lists HOA / Community Association Management already live.
- **Key intelligence:** NJ residential and commercial association management company with approximately `$750K` annual revenue. Services include dues/fee collection, maintenance coordination, vendor management, and on-demand reporting.
- **Companies / contacts:** Everingham & Kerr; unnamed NJ association-management company.
- **Lifecycle status:** broker-sourced deal signal -> already in WEEKLY REVIEW. Not new.
- **Why overlooked:** The individual teaser is too small for platform acquisition, but the operating model maps to recurring administration and vendor coordination. It should inform target-count and size-distribution validation, not be resurfaced as a separate candidate.

#### Institutional Commercial Facility Services / Facilities Maintenance
- **Sources:** Axial Gmail teaser (2026-06-11) thread `19eb71a4e80dbafe`; SMB Deal Hunter 2026-05-26 facility-maintenance listing; `brain/outputs/2026-06-25-thesis-industry-inventory-full-corpus-pass.md`; active tracker context lists Facilities Management / Commercial Building Services and High-End Commercial Cleaning already live.
- **Key intelligence:** Axial teaser described an institutional commercial facility services provider with revenue table in email showing `$15.3M` in 2024; categories visible included janitorial services, facilities support services, other services to buildings/dwellings, and landscaping. SMB Deal Hunter separately listed a Utah facility maintenance contractor with national grocery-chain contracts, `$4.514M` revenue and `$838K` EBITDA.
- **Companies / contacts:** Axial; SMB Deal Hunter / Helen Guo; unnamed institutional facility-services provider; unnamed UT facility-maintenance contractor.
- **Lifecycle status:** repeated broker/newsletter signal -> already represented by active facilities/commercial cleaning rows. Treat as validation and potential target-source pattern, not a new lane.
- **Why overlooked:** The broad label hides several different businesses. The attractive pattern is multi-site commercial-contract maintenance with sticky vendor approval, not generic janitorial or landscaping.

#### Sign and Lighting Maintenance Programs for Multi-Location Brands
- **Sources:** SMB Deal Hunter Gmail newsletter (2026-05-26); Axial search result `Highly Successful Full-Service Architectural Sign Company` (2026-06-26); `brain/calls/2026-06-22-michael-horowitz.md`; active tracker context lists Sign and Lighting Maintenance Programs already live.
- **Key intelligence:** SMB Deal Hunter listed an absentee-run commercial sign manufacturer in Missouri with `$4.364M` revenue, `$661K` EBITDA, established 1978. The commentary called out maintenance and lighting service as the reoccurring layer on top of project manufacturing, including regular commercial sign upkeep, lighting repairs, and LED retrofit tailwinds. Mike Horowitz separately flagged signage/logo installation and quick repair as luxury-retail vendor ecosystem adjacencies.
- **Companies / contacts:** SMB Deal Hunter / Helen Guo; Axial; Mike Horowitz; unnamed MO sign manufacturer.
- **Lifecycle status:** historical Gmail + call convergence -> already in WEEKLY REVIEW. Not new.
- **Why overlooked:** The manufacturing headline can obscure the better service thesis. The right niche is maintenance/lighting programs for multi-location commercial brands, not sign fabrication alone.

#### Luxury Amenity Management / Private Tenant Club Operations
- **Sources:** `brain/calls/2026-06-22-michael-horowitz.md`; `brain/calls/2026-06-22-doug-tudor.md`; active tracker context lists Luxury Amenity Management already live.
- **Key intelligence:** Mike Horowitz called amenity management for luxury real estate the most compelling new idea from the session. Arch Amenity Group was cited as a large player managing 20,000+ sq ft amenity packages. Tailwinds: post-COVID commercial landlords adding amenities to retain tenants, trophy HQ buildouts, and outsourcing hospitality-like services. Doug Tudor separately noted third-party managers of fitness/spa amenities in commercial buildings as not yet explored.
- **Companies / contacts:** Mike Horowitz; Doug Tudor; Arch Amenity Group; Paramount Group example; Chanel office gym/private chef context.
- **Lifecycle status:** proposed by Mike/Doug -> active tracker context. Not new.
- **Why overlooked:** It sounds consumer/discretionary until framed as B2B outsourced operations for landlords and corporate HQs. Needs proof that revenue is contracted and margins are not labor-compressed.

#### Premium Physical Security Integration for Luxury Retail / Commercial Property
- **Sources:** `brain/calls/2026-06-22-michael-horowitz.md`; Everingham & Kerr Gmail search result `Provider of Security Solutions` (2026-07-06); `brain/outputs/2026-06-25-thesis-industry-inventory-full-corpus-pass.md`; active tracker context lists Premium Physical Security Integration.
- **Key intelligence:** Mike identified escalating high-end retail theft and store design already being security-driven. Potential recurring/reoccurring layer: sensor testing, reconfiguration, monitoring/maintenance, and store-renovation cycles every 5-7 years. Historical inventory cautions that commercial-property security systems have CAC/outcome risk.
- **Companies / contacts:** Mike Horowitz; Everingham & Kerr; standard ADT-type competitor cited as the undifferentiated baseline.
- **Lifecycle status:** proposed -> active tracker context, but challenged by risk of commodity alarm/security competition. Keep lifecycle as live-with-caution.
- **Why overlooked:** The luxury-retail specificity matters; generic security is too crowded.

#### Fire Safety Inspection / Testing, Fire Extinguisher Recharge, Hood / Grease / Grease-Trap Services
- **Sources:** `brain/outputs/2026-06-25-thesis-industry-inventory-full-corpus-pass.md`; `brain/calls/2026-06-25-jeff-i-kay-mtg.md`; `brain/inbox/2026-06-18-niche-signal-ev-charger-fire-safety-testing.md`; active tracker context includes Commercial Fire & Life Safety Inspection/Compliance + EV-Charging Garage/Lot Wedge and Fire-Protection-Adjacent Industrial MRO.
- **Key intelligence:** Jeff pushed adjacent circles from pest/commercial-property services into fire safety and fragrance testing. Prior inventory separated fire inspection/testing, extinguisher recharge, restaurant hood/grease cleaning, and grease-trap service as discovery-with-caution lanes. The EV-charger safety inbox note framed inspection/testing/certification/commissioning and ongoing compliance for garages, multifamily, commercial properties, fleet depots, hotels, retail centers, and municipal facilities.
- **Companies / contacts:** Jeff Stevens; no single company from the historical scan besides active tracker rows.
- **Lifecycle status:** proposed by Jeff/Kay correction -> active tracker context. Live, but needs recurring mandate validation.
- **Why overlooked:** The EV-charging wedge can get confused with EV software/charging, which is tabled for political/climate and software concerns. This historical signal is narrower: fire/electrical compliance services, not charger ownership/software.

#### Specialty Facility Cleaning, Medical/Lab/IVF Specialty Cleaning, Waste-Area Sanitation
- **Sources:** `brain/calls/2026-06-17-guillermo-lavergne-brainstorm.md`; `brain/outputs/2026-06-25-thesis-industry-inventory-full-corpus-pass.md`; active tracker context lists High-End Commercial Cleaning and Medical/Lab/IVF Specialty Cleaning.
- **Key intelligence:** Guillermo/Kay ruled out luxury boutique cleaning because national players dominate and commercial cleaning lead generation is difficult. Medical/lab/IVF clinic cleaning was flagged as more differentiated. Pest operator mentioned trash chute/compactor cleaning as a natural add-on; waste-area sanitation may tie back to pest prevention.
- **Companies / contacts:** Guillermo Lavergne; pest operator signal; no named cleaning company.
- **Lifecycle status:** proposed -> luxury boutique cleaning challenged/rejected -> medical/lab/IVF and waste-area sanitation remain live discovery branches. Do not resurface generic luxury boutique cleaning.
- **Why overlooked:** Prior cleaning labels are too broad; the revived idea is regulated/specialty environments or pest-adjacent sanitation with service necessity.

#### Marine Services / Boat Transport / Boat Covers / Yacht Services
- **Sources:** `brain/calls/2026-06-22-doug-tudor.md`; `brain/calls/2026-06-22-michael-horowitz.md`; active tracker context lists Asset-Light Boat and Yacht Transport Coordination.
- **Key intelligence:** Doug observed fragmented local marina ecosystems and recommended boat transport/shipping as the strongest branch, analogizing it to car moving with PE-backed players, good margins, and strong exit multiples. Other branches: boat maintenance, detailing, repair, provisioning, parts, upholstery, shrink-wrapping/boat covers. Mike independently flagged marine/yachting as a Kay right-to-win area through yacht-club background and family shipping/logistics connection.
- **Companies / contacts:** Doug Tudor; Mike Horowitz; unnamed holding company that acquired a boat-covering business; Kay's brother in cargo/marine shipping.
- **Lifecycle status:** proposed -> narrowed into active asset-light transport-coordination row. Do not promote seasonal maintenance/detailing unless target pool and recurring revenue are proven.
- **Why overlooked:** Marine can read B2C/seasonal. The historically strongest formulation is coordination/logistics, not asset-heavy boatyards or discretionary recreation.

#### Art Storage / Fine-Art Logistics / High-Value Asset Services
- **Sources:** `brain/calls/2025-09-17-levi-acumen-discovery.md`; `brain/calls/2025-10-30-levi-acumen-industry-deep-dive.md`; `brain/calls/2026-06-09-warren-chan-art-in-search.md`; killed/tabled snapshots; active tracker context lists Storage & Related Services for High Value Assets and Fine-Art Logistics Services.
- **Key intelligence:** Acumen had `75` employees, NY/LA/Miami/Hudson Valley footprint, sticky storage clients with `8-9k` items in custody per client, and Queens storage margin around `16%`. Blended net margins were `8%-11%`; Poughkeepsie was `90%-95%` full; capex for a new warehouse estimated `$600K-$750K+`; LOI context cited `$13.158M` revenue and `$1.115M` EBITDA. Warren later summarized art storage as still one of the cleanest art-world fits, while art advisers, galleries, fairs, collection-management software, and logistics-only variants had been ruled out or parked for structural reasons.
- **Companies / contacts:** Levi Phelps; Acumen International; Voxme; Maquette; SAT/Safe Art Transport; Art Crating; Crozier; UOVO; Warren Chan.
- **Lifecycle status:** deeply pursued -> Acumen deal/LOI context -> challenged by low blended margins, capex/real-estate intensity, labor bottlenecks, partner complexity -> still active only in narrower high-value-asset infrastructure rows.
- **Why overlooked:** This has the richest company-level diligence, but the core lesson is negative/conditional: storage can be sticky but often too asset-heavy and margin-thin unless paired with differentiated services or software/process improvement.

#### HNW Personal Lines / Fine Art / Specialty Insurance Brokerage
- **Sources:** `brain/calls/2025-10-15-august-felker-insurance-dd.md`; `brain/calls/2025-11-19-august-felker-insurance-dd-2.md`; `brain/calls/2026-01-12-hunter-kay-insurance.md`; `brain/calls/2026-01-22-call-with-chris-wise.md`; `brain/calls/2026-03-31-tobias-marshberry-insurtech.md`; active tracker context lists Specialty Insurance Brokerage and HNW Personal Lines Concierge Insurance Brokerage.
- **Key intelligence:** August validated HNW personal lines as highly sticky and near-100% recurring, with a specific women-led specialty brokerage target identified near retirement age and a potential producer partner. Bank of America art services reportedly recommended 4 large and 3 small specialty brokerages; Kay had narrowed a broader list to roughly 30 targets. Pushback: investor concern on multiples, QSBS non-qualification, industry preference for experienced operators, heavy roll-up activity, and repeated "start your own brokerage" advice. Chris Wise added that fine-art insurance can be higher-margin than general lines but hard to enter without client relationships; Tobias MarshBerry said the brokerage space is heavily rolled up and owners know their value.
- **Companies / contacts:** August Felker; Hunter Hartwell; Chris Wise; Tobias MarshBerry; Richard Augustine; Bank of America art services team; unnamed women-led HNW brokerage target.
- **Lifecycle status:** proposed and deeply pursued -> challenged by valuation/access/QSBS/operator-credibility -> still active only when proprietary/specialty target access exists.
- **Why overlooked:** This was not overlooked so much as repeatedly challenged. Historical value is lifecycle safety: do not let generic insurance brokerage reappear as new; only narrow specialty/HNW proprietary angles remain live.

#### MRO / Specialty Equipment Service / Specialty Steel Machinery Service
- **Sources:** `brain/calls/2026-06-22-michael-horowitz.md`; `brain/calls/2026-06-25-jeff-i-kay-mtg.md`; `brain/outputs/2026-06-25-thesis-industry-inventory-full-corpus-pass.md`; active tracker context lists Fire-Protection-Adjacent Industrial MRO and AEROSPACE DEFENSE.
- **Key intelligence:** Mike framed "mission critical to a process" businesses: if equipment failure stops assembly lines, energy production, cranes, or robots, customers pay quickly. Jeff's concentric-circle framing pointed toward specialty steel machinery and MRO/service-heavy models connected to existing relationships. Current active tracker already has fire-protection-adjacent industrial MRO; aerospace/defense surfaced repeatedly but has been treated with caution/hard-exclude in prior calls.
- **Companies / contacts:** Mike Horowitz; Jeff Stevens; Lisa/Peapack lead referenced in inventory; no specific company surfaced in this pass.
- **Lifecycle status:** live as a filter, not a single niche. Aerospace/defense is challenged due to GovCon/defense/aviation fit risk; MRO service-heavy niches remain viable if tied to criticality and recurring maintenance.
- **Why overlooked:** "MRO" is too broad. The useful historical insight is to map vertical-specific equipment failure modes and service vendors.

#### Apparel / Fashion Supply-Chain Testing, Customs Compliance, Warehousing
- **Sources:** `brain/calls/2026-06-17-guillermo-lavergne-brainstorm.md`; killed/tabled snapshots; `brain/outputs/2026-06-25-thesis-industry-inventory-full-corpus-pass.md`.
- **Key intelligence:** Kay has deep apparel/fashion network, and the team explored testing/certification angles such as thread count, cashmere claims, and fire retardancy, plus customs compliance as mission-critical because wrong paperwork or undisclosed contents can freeze inventory. Chanel kept compliance in-house for confidentiality. Consensus in the call: fashion industry margins are chronically challenged, third-party-service willingness to pay is low, and no clear target was identified; logistics/warehousing looked more stable but remained unresolved.
- **Companies / contacts:** Guillermo Lavergne; Chanel as operating-history context.
- **Lifecycle status:** proposed -> challenged/rejected for apparel supply-chain services broadly. Active tracker has High-End Beauty & Fragrance Packaging, Value-Added Fragrance Distribution, and testing labs, which are distinct and should not inherit this rejection automatically.
- **Why overlooked:** Kay's right-to-win is high, but the business-model evidence was weak. Do not revive apparel supply-chain testing without a concrete recurring compliance buyer and target list.

#### Women's Health / Fertility / Post-Operative Care
- **Sources:** `brain/calls/2026-06-17-guillermo-lavergne-brainstorm.md`; killed snapshot; historical inventory.
- **Key intelligence:** Doulas, pelvic floor, menopause, fertility/IVF/surrogacy and women's health tech were discussed as early thesis lanes. The June 17 brainstorm explicitly killed women's health and fertility for now: many sub-sectors are too early-stage with little to acquire, regulatory environment is unfavorable, and fertility is already heavily searched by other searchers.
- **Companies / contacts:** Guillermo Lavergne; no target company from this pass.
- **Lifecycle status:** rejected/killed for now. Do not surface as live.
- **Why overlooked:** It is emotionally and network-adjacent, but fails current acquisition-fit and target-availability tests.

#### Art Advisory / Collection Management / Authentication / Galleries / Fairs
- **Sources:** `brain/calls/2026-06-09-warren-chan-art-in-search.md`; killed/tabled snapshots; historical inventory.
- **Key intelligence:** Warren and Kay discussed art-world search subthreads. Collection-management software, art advisers, logistics-only variants, galleries, and fairs were ruled out for different structural reasons. Luxury collectibles and authentication remain interesting intellectually, but AI disruption, key-person risk, and weak scalable target evidence persist. Fine Art Escrow Software was killed for no market, with TAM noted around `$15M-$30M`; conservation/restoration was killed for labor model.
- **Companies / contacts:** Warren Chan; no new acquisition target from this pass.
- **Lifecycle status:** mostly rejected/parked. Only storage/fine-art logistics and specialty insurance remain active rows.
- **Why overlooked:** These ideas are close to Kay's background and therefore recur, but the historical record repeatedly narrowed away from them.

#### Medical Certification / Training Providers
- **Sources:** `brain/calls/2025-04-24-womens-search-network-how-to-set-up-for-a-search.md`; historical inventory.
- **Key intelligence:** Women's Search Network panel noted that traditional searchers often gravitate to training, testing, and certification because recurring revenue, loyalty, and low churn fit investor criteria. A cited example was a certification/medical certification training provider with search-fund-world connections.
- **Companies / contacts:** Iris Li; Elise Testa; Women's Search Network participants; unnamed certification provider.
- **Lifecycle status:** watchlist only; not in active tracker context unless folded into compliance/training rows.
- **Why overlooked:** It is generic search-fund consensus rather than G&B-specific right-to-win. Needs a narrower vertical, e.g. mandated certification for a specific regulated workforce.

#### Dead / Low-Priority Historical Lanes to Suppress
- **Sources:** killed/tabled snapshots and historical inventory.
- **Signals:** Family Office Enablement Services (custom-heavy, poor repeatability), Luxury Property Maintenance (labor/geographic scaling issues), Art Tech Platforms (shrinking/low TAM), Fine Art Escrow Software (TAM `$15M-$30M`, no targets), Conservation/Restoration Services (labor-constrained), generic legal software/high-end property-management platform (software caution), EV charging software (political/climate/software concern), luxury boutique cleaning (dominated by national players), drone services/Project Drone (failed thesis-shape gate), generic aerospace/defense (hard-exclude/caution unless a very narrow service-heavy MRO wedge is proven).

### Industries/Companies Mentioned
- Trade Risk Group; Trade Acceptance Group; Meridian/Texel; Euler Hermes/Allianz Trade; Atradius; Coface.
- Acumen International; Voxme; Maquette; Safe Art Transport; Art Crating; Crozier; UOVO.
- Arch Amenity Group; Paramount Group; Chanel.
- Everingham & Kerr; Axial; SMB Deal Hunter; unnamed NJ geotechnical/CMT company; unnamed NJ association-management company; unnamed institutional facility-services provider; unnamed UT facility-maintenance contractor; unnamed MO sign manufacturer; unnamed trucking compliance platform.
- August Felker; Hunter Hartwell; Chris Wise; Tobias MarshBerry; Richard Augustine; Jeremy Black; Mike Horowitz; Doug Tudor; Guillermo Lavergne; Jeff Stevens; Warren Chan; Levi Phelps.

### Data Points for Scoring
- Trade credit insurance brokerage: US broker TAM roughly `$200M-$400M`; gross margins `60%-80%`; EBITDA margins `20%-35%`; possible `90%+` retention; only `30-50` US specialists.
- Truck licensing/compliance listing: `$1.039M` revenue; `$412K` EBITDA; `$1.425M` asking price; annual recurring filings.
- Geotechnical/CMT teaser: over `$3.6M` revenue; approximately `$1M` normalized EBITDA.
- HOA/association-management teaser: approximately `$750K` annual revenue.
- Facility maintenance listing: `$4.514M` revenue; `$838K` EBITDA; national grocery-chain contracts. Axial institutional facilities teaser showed `$15.3M` 2024 revenue in the visible table.
- Sign manufacturer listing: `$4.364M` revenue; `$661K` EBITDA; established 1978; recurring layer is sign maintenance/lighting/LED retrofit work.
- Acumen/fine-art logistics: 75 employees; Queens storage margin `16%`; blended net margin `8%-11%`; Poughkeepsie `90%-95%` full; new warehouse capex `$600K-$750K+`; LOI context `$13.158M` revenue / `$1.115M` EBITDA.
- Pest historical context: NJ/NYC commercial pest target around `$1.5M` revenue / `$500K` EBITDA, 98% client retention, high-end clients including Cartier/Chelsea Market/Google; already active and included here only as source-context overlap.

### Missing-Source Diagnostics
- **Historical calls:** Covered via 158 pre-2026-07-07 vault call notes across Fireflies, Granola, and manual notes. Granola wrapper was reachable, but the list command returned newest notes first and pagination was not separately exhausted; older Granola meetings appear synced in `brain/calls` and were covered there.
- **Historical Gmail:** Covered with required read-only `gog gmail search/read` using `source /home/ubuntu/projects/Sapling/scripts/op-env.sh` and `--gmail-no-send`. Skill prompt syntax was stale (`--query` is unsupported in installed `gog`), so searches were rerun with positional query syntax. Read key threads for Jeremy insurance ideas, Truck Licensing & Compliance, Geotechnical Engineering, Association Management, and Institutional Facility Services; broader result sets were scanned by subject/source.
- **OneNote SEARCH FUND:** BLOCKED as a source cluster in this session because no OneNote MCP tools are exposed. No local OneNote export was found during this pass.
- **ChatGPT export:** BLOCKED as a source cluster because `~/Downloads` does not exist on this VPS and no `selected_business_conversations.json` was found under `/home/ubuntu`.

→ READY
## [niche-intel-recent] — 2026-07-21 22:36 EDT
**Source:** RECENT: last-14-days web/social, newsletters, Granola calls, Gmail deal flow/investors, vault research, passive signals
**Status:** complete

### Signals Found

#### Source 1: Web / Social Research

- **Search-fund / small-business services acquisition environment (existing context, not a niche):** last30days produced only thin HN evidence and no useful Reddit/Polymarket niche signals. Public web search found the WSJ search-fund / independent-sponsor coverage published July 2026, Stanford's 2026 Search Fund Study page, and related commentary that formation/activity remain high while acquisition competition has increased.
  - **Why it matters for G&B:** reinforces the need for industry focus and proprietary channels. This aligns with BK Growth and Clayton call feedback that generic search and brokered processes are weaker.
  - **Quantitative data:** Stanford/secondary summaries cite high formation through 2025 and declining acquisition rates; BK Growth call separately cited 48% Stanford acquisition rate vs. Yale active-search adjustment closer to ~30%.
  - **Named companies/contacts:** Stanford GSB; WSJ examples included small-business acquisitions in plumbing/manufacturing; not directly targetable from this source.
  - **Gaps:** last30days Reddit returned 403; X/Twitter and YouTube unavailable in this environment; Polymarket produced no relevant markets.

- **Specialty insurance brokerage / specialty programs (existing: Specialty Insurance Brokerage, HNW Personal Lines, Surplus Lines Compliance; potential adjacency: jewelry block):** public web search found July 2026 specialty-insurance consolidation signals: ALKEME acquired Virtue Risk Partners, an MGA in general casualty, professional, environmental, excess lines, and workers' comp; ALKEME also announced eight Q2 acquisitions; American Growth Insurance launched with nearly $70M committed equity as an AI-enabled specialty insurance brokerage growth platform.
  - **Why it matters for G&B:** sponsor-backed distribution platforms remain active. This supports the insurance-distribution thesis, but also warns that generic brokerage is crowded. The G&B angle should stay narrow: jeweler's block, art/collectibles, HNW personal lines, surplus-lines compliance or back-office friction.
  - **Quantitative data:** AGI launch: nearly $70M committed equity; ALKEME: eight Q2 2026 acquisitions.
  - **Named companies/contacts:** ALKEME Insurance, Virtue Risk Partners, American Growth Insurance, Rockbridge Growth Equity, Atomic.
  - **Gaps:** web evidence supports consolidation trend but not target density for independent jeweler's-block specialists.

- **Fire & life safety / premium security integration (existing):** public web search found 2026 consolidation maps and market commentary citing FLS/security as one of the most aggressively consolidated B2B service categories, driven by recurring code-mandated inspection/testing/monitoring revenue. One source cited roughly 125 FLS transactions in 2025 and a 66.7% YoY increase; security M&A commentary cited PE platform transactions up 33.3% YoY to 20 deals.
  - **Why it matters for G&B:** reinforces the existing FLS/security rows but does not create a new niche. Attractive recurring compliance economics are real, but competition for platforms/add-ons is intense.
  - **Quantitative data:** ~125 FLS transactions in 2025; +66.7% YoY; security PE platform transactions +33.3% YoY to 20 deals.
  - **Named companies:** Pye-Barker, Summit Companies, BlackRock Long Term Private Capital, Capstone-cited security platforms.
  - **Gaps:** most data is from advisory/market-map sources rather than fresh primary filings.

- **Submetering / utility billing compliance (existing):** public web search found regulatory developments in utility billing/submetering: Colorado HB26-1284 requiring individual water submeters for new residential construction from Jan. 1, 2027; state-level activity in Massachusetts/Ohio/Virginia and utility-billing compliance commentary.
  - **Why it matters for G&B:** reinforces the submetering and utility-billing row. Regulation is still moving from optional operational savings to compliance requirement in some states, supporting demand for billing, meter installation, tenant notification and compliance workflows.
  - **Quantitative data:** Colorado effective date Jan. 1, 2027 for new residential water submetering.
  - **Named companies/contacts:** no acquisition targets from web; source set includes NCSL and state legislative pages.
  - **Gaps:** no fresh July 7-21 M&A transaction found in submetering; this is a regulatory signal, not deal-flow evidence.

#### Source 2: Newsletters

- **Direct mail / local advertising services (potential new or watchlist, overlaps commercial printing/direct mail):** Acquiring Minds covered Brian Jungles acquiring City Publications Atlanta, a direct advertising business serving local home-services customers since 1996.
  - **Why it matters for G&B:** analog local marketing/direct mail may be more defensible than generic digital marketing if customer base is home services and the operator can modernize targeting/data. This is not clearly G&B's highest-right-to-win, but it is a concrete ETA signal.
  - **Quantitative data:** historical revenue $650K-$750K; first-year revenue about $742K; target >$1M next year; estimated pre-acquisition SDE ~$150K; purchase price $400K; financing via securities-backed line at about 7.5% vs. SBA 12-14%.
  - **Named companies/contacts:** City Publications Atlanta; Brian Jungles; Acquiring Minds / Will Smith.
  - **Gaps:** one case study; not enough to promote without target-density and margin screen.

- **Franchise holdco / small franchise acquisitions (potential context, likely not new):** Acquiring Minds webinar promoted franchise acquisition strategy: single-brand roll-ups, multi-brand portfolios, diligence/integration and institutional capital in franchising.
  - **Why it matters for G&B:** relevant to Mosquito Sheriff and other pest/franchise leads, but franchise systems introduce FDD/franchisor dynamics and may not fit the preferred founder-led operating-company path.
  - **Quantitative data:** none from newsletter excerpt.
  - **Named contacts:** Connor Groce.
  - **Gaps:** not a specific niche signal.

- **ETA deal-quality filters (screening context):** This Week in ETA reiterated criteria: recurring/reoccurring revenue, low customer concentration, healthy margins, below-5x entry multiple, low capital/working-capital intensity, seller motivation, and restrictive covenants.
  - **Why it matters for G&B:** reinforces why inventory-heavy jewelry brand and project-heavy electrical/plumbing opportunities need sharper diligence even if strategically interesting.
  - **Quantitative data:** below-5x entry multiple threshold noted as their starting filter.
  - **Named contacts:** Grant Hensel; Eli Albrecht.
  - **Gaps:** not a niche source.

- **Pest management industry events (existing):** NPMA/PestWorld emails surfaced active education/networking events, including PestWorld 2026, Carolinas/Mid-Atlantic 2026 in Charleston, SPAR regulator-relationship webinar and Responsible Care / sustainability content.
  - **Why it matters for G&B:** confirms the pest industry has strong association infrastructure and regulatory/technical education channels, but recent calls indicate the thesis is being deprioritized because attractive East Coast targets are small and/or picked over.
  - **Quantitative data:** one event mentioned 50+ exhibitors; no M&A data.
  - **Named companies/contacts:** NPMA, PestWorld, NYPMA/PWIPM, Nissus (sponsored content).
  - **Gaps:** event emails do not prove acquisition availability.

- **Fine-art logistics / HVA services (existing):** Crozier Fine Arts newsletter promoted storage, transportation and crating tailored to high-value collections.
  - **Why it matters for G&B:** reinforces active specialty storage/fine-art logistics rows and ties directly to live DealsX response from Stephen Elliott & Company.
  - **Quantitative data:** none in email.
  - **Named companies:** Crozier Fine Arts.
  - **Gaps:** marketing email only; no target economics.

- **Exit-planning / M&A network access (pipeline context):** XPX emails included NJ women in exit networking lunch and regional events.
  - **Why it matters for G&B:** source of intermediary/operator relationships, not a niche itself. Could support sourcing across NJ/NY lower-middle-market owner transitions.
  - **Named contacts:** XPX New Jersey; Katie Noonan; Angie Ellis.
  - **Gaps:** no industry-specific signal.

#### Source 3: Granola Calls

- **High-end jewelry brand and luxury-services holding-company thesis (potential active lead / possible new thesis, not a simple tracker niche):** Multiple calls (Sara Rosenthal, Guillermo, Jackie Hirsch, WSN Group, Andrew Freiman, Camilla) converged on an 80-year-old high-end jewelry business whose owner approached Kay. Business described as ~$18M revenue, ~$13M inventory, $3-4M cash, no debt, two stores (Madison Ave + Chicago), Bergdorf Goodman, independent retailers, e-commerce, 76-year-old second-generation owner, children uninterested, and president in place.
  - **Why it matters for G&B:** not classic search because inventory-heavy, B2C/retail and not recurring, but it may be a Kay-specific proprietary opportunity tied to her luxury background and potential holding-company architecture. Several advisors said "not a hard pass"; diligence hinges on EBITDA, inventory composition/aging, lease terms, ROIC, wholesale/e-commerce mix, and investor appetite.
  - **Quantitative data:** ~$18M revenue; ~$13M inventory; $3-4M cash; owner's son estimated ~$8M inventory liquidation floor; Jackie guessed potentially close to ~$4M EBITDA if healthy; retail multiples discussed around 4x vs. 6-7x for trade businesses.
  - **Named contacts/companies:** Sara Rosenthal, Guillermo, Jackie Hirsch, Andrew Freiman, Camilla, Whitney trustee owner, Bergdorf Goodman, London Jewelers, Bloomingdale's, Chenmark as comparable multi-business owner.
  - **Gaps:** no financial package yet; no confirmed EBITDA; no inventory quality/aging; no lease terms; investor fit unresolved.

- **Jeweler's block / jewelry specialty insurance (existing specialty-insurance adjacency):** Guillermo and Sara calls flagged jeweler's block policies as B2B specialty coverage for jewelry retailers/brands, covering inventory, movement and showings, with antiquated processes and broker friction.
  - **Why it matters for G&B:** stronger fit than buying a generic brokerage because it sits at the intersection of insurance, high-value assets, luxury goods and operational pain. Could be an acquisition niche or an adjacency layered into a luxury-services platform.
  - **Quantitative data:** none yet.
  - **Named contacts:** specialty insurance contact via prior pipeline; Jeff-introduced August Felker and Richard Augustine were mentioned in Andrew call as specialty-insurance connections.
  - **Gaps:** target universe and revenue model not validated; need broker/MGA/carrier workflow map.

- **Beauty/fragrance/cosmetics supply chain and testing (existing: fragrance/cosmetic product testing labs, luxury package testing, high-end packaging, value-added fragrance distribution):** Clayton, Guillermo, Camilla and Andrew calls independently surfaced fragrance testing, packaging testing, third-party cosmetics labs, specialty/value-add chemical distributors, secondary packaging / kitting for imported beauty products, and US-based high-quality packaging with tariff tailwinds.
  - **Why it matters for G&B:** this is the strongest recent non-jewelry thematic cluster because it combines Kay's Chanel background, industry-conference sourcing, compliance/testing, luxury packaging and recurring/reoccurring B2B support.
  - **Quantitative data:** no market size in calls. Named comp Tower Products was cited as a searcher-acquired press-room chemistry company; Guillermo cited an Ashford deal involving Korean beauty 3PL into the US handling customs, FDA compliance and logistics end-to-end.
  - **Named companies/contacts:** Tower Products, Rachel McGrath, Ashford, L'Oreal as customer archetype, Guillermo, Clayton, Camilla.
  - **Gaps:** need target-density work and definition discipline: testing labs vs. packaging vs. specialty distribution vs. 3PL/kitting are adjacent but not identical.

- **Pest management (existing, now negative/deprioritization signal):** Clayton and Guillermo calls: Kay is ~2 months into pest; East Coast targets appear too small, higher multiple and picked over; another West Coast searcher in year 3 confirmed similar dynamics; cold calling hit gatekeepers; mid-market picked over by PE.
  - **Why it matters for G&B:** this is important negative evidence. Do not promote "Premium Pest Management" as a fresh opportunity without resolving target size and competition. Current DealsX responses may be useful leads but do not reverse the thesis-level concern.
  - **Quantitative data:** targets found often under $500K EBITDA; Stanford 48% acquisition rate and Yale ~30% active-search adjustment discussed as broader context.
  - **Named contacts/companies:** Clayton Sachs, Albert Kim (West Coast pest searcher), Mosquito Sheriff, Steel City Wildlife.
  - **Gaps:** no compiled target-count update this run.

- **Storage / services for luxury or retail industries (existing):** Clayton liked storage, services for luxury/retail, insurance and collectibles, packaging testing and third-party labs. Andrew noted art storage pipeline remains open even after two deals fell through.
  - **Why it matters for G&B:** recurring luxury/HVA services remain a coherent architecture. Recent Gmail confirms live fine-art and collector-car storage responses.
  - **Quantitative data:** none.
  - **Named contacts/companies:** Andrew Freiman, Clayton Sachs.
  - **Gaps:** no new financial target data from calls.

- **Search strategy / sourcing channel shift (context):** BK Growth call said Q3/Q4 2025 were record deal-volume periods, current months slower but pipeline building; ~10 deals under LOI, roughly 7 services and 3 software; services deals averaged mean 4.9x EBITDA and median 5.3x EBITDA in BK Growth's 2025 portfolio, with ~90% proprietary sourced. Industry-focused searchers said to have 5-8x better success rate.
  - **Why it matters for G&B:** validates conference/industry-focus doctrine and lower appetite for opportunistic broker blasts.
  - **Quantitative data:** ~10 LOIs; ~7 services / ~3 software; LOI-to-close ~1 in 4; services mean 4.9x EBITDA, median 5.3x; ~90% proprietary; formal-process odds ~1 in 50, front-run odds ~1 in 20; industry focus 5-8x success uplift.
  - **Named contacts:** BK Growth, GJ King, Clayton Sachs.
  - **Gaps:** not a direct niche signal.

#### Source 4: Gmail Deal Flow / Investors

- **Fine-art logistics / specialty storage (existing):** DealsX response from Stephen Elliott & Company / Stephen Elliott Webb: fine-art services across Charleston and New York; services listed storage, receiving, delivery & installation, framing and restoration. Reply was interested in hearing Kay's thoughts.
  - **Why it matters for G&B:** direct live owner/intermediary response in an existing high-value-asset services niche. Strongest recent deal-flow reinforcement for fine-art logistics / HVA storage.
  - **Quantitative data:** none.
  - **Named companies/contacts:** Stephen Elliott & Company LLC, Stephen Elliott Webb.
  - **Gaps:** no revenue/EBITDA/ownership transition detail yet.

- **Collector-car / specialty storage-adjacent services (existing: Storage & Related Services for High Value Assets):** DealsX response from Motoreum / Bobby Wilson to specialty-storage outreach. Motoreum appears to mix collector-car brokerage, storage and related services; reply indicated openness to improvement/personal growth.
  - **Why it matters for G&B:** confirms owner receptivity in an HVA-adjacent category, though reply is soft and not necessarily sale intent.
  - **Quantitative data:** none.
  - **Named companies/contacts:** Motoreum, Bobby Wilson.
  - **Gaps:** business model split and recurring storage revenue unknown.

- **Pest management / wildlife control (existing, mixed signal):** DealsX responses: Mosquito Sheriff / Patrice Rice is open to conversation; company has five franchisees, active FDD, SEO/content asset, all-natural mosquito-control franchise concept and founder succession trigger after stroke at age 74. Steel City Wildlife / Brad Graham responded "Interested."
  - **Why it matters for G&B:** concrete founder-led response and succession trigger for pest/wildlife, but franchise-system and small-scale concerns may limit platform fit. Should be routed as active deal-flow, not as fresh thesis validation.
  - **Quantitative data:** Mosquito Sheriff has five franchisees and active FDD.
  - **Named companies/contacts:** Mosquito Sheriff, Patrice Rice; Steel City Wildlife, Brad Graham.
  - **Gaps:** revenue/EBITDA, geography, owner role, franchise economics, and transferability unknown.

- **Asset-light boat/yacht transport / specialized carriers (existing):** DealsX response from Dun-Rite Specialized Carriers was an out-of-office auto-reply, not substantive interest.
  - **Why it matters for G&B:** source touched the active "Asset-Light Boat and Yacht Transport Coordination" row but is weak evidence only.
  - **Quantitative data:** none.
  - **Named company/contact:** Dun-Rite Specialized Carriers, Anthony.
  - **Gaps:** no real response yet.

- **Commercial cleaning / janitorial services (existing: High-End Commercial Cleaning; Medical/Lab specialty cleaning separate):** Axial sent "Janitorial Commercial Services" opportunity. Snippet showed revenue $7.3M in 2024 and table columns for 2024/2025/2026E; full text body unavailable through plain extraction.
  - **Why it matters for G&B:** reinforces available deal flow in commercial cleaning, but broad janitorial remains less attractive unless scoped to medical/lab/IVF, premium/high-end or compliance-heavy accounts.
  - **Quantitative data:** 2024 revenue $7.3M from snippet; other metrics unreadable from MIME extraction.
  - **Named source:** Axial.
  - **Gaps:** EBITDA, customer concentration, specialty mix and contract recurrence unavailable.

- **Water/wastewater / public-sector electrical contractor (existing: Water/Wastewater SCADA & Controls; possible adjacency, but project-heavy):** Everingham & Kerr sent NJ commercial electrical contractor: >$6M revenue, $1.2M normalized EBITDA, 35+ years, technicians avg. 20 years, focus on commercial/institutional, significant water/wastewater projects and generator installations, NJDPM $15M prequalification and bonding.
  - **Why it matters for G&B:** validates lower-middle-market availability around water/wastewater infrastructure, but it is likely broader/project-based electrical contracting, not the narrower SCADA/controls compliance service provider that scored well last run.
  - **Quantitative data:** >$6M revenue; $1.2M normalized EBITDA; 35+ years; NJDPM $15M prequalification.
  - **Named company/contact:** Everingham & Kerr; target undisclosed.
  - **Gaps:** recurring service mix and controls/SCADA exposure unknown.

- **Plumbing / institutional healthcare projects (potential new only if narrowed, otherwise generic trades):** Everingham & Kerr sent NY residential & commercial plumbing contractor: $3M revenue, >$500K normalized EBITDA; residential/commercial plumbing, repairs/installations, commercial renovations for institutions/healthcare/city/state/federal projects; real estate optional. SMB Deal Hunter separately listed MA plumbing/heating/excavation company with membership program, $1.454M revenue, $633K EBITDA, 5-person crew plus dedicated service tech.
  - **Why it matters for G&B:** recurring membership programs and institutional/healthcare plumbing may be better than generic plumbing. Still not an obvious G&B right-to-win unless tied to building compliance, healthcare facilities, or luxury property stewardship.
  - **Quantitative data:** E&K target $3M revenue / >$500K EBITDA; SMB Deal Hunter target $1.454M revenue / $633K EBITDA / $2.75M ask.
  - **Named sources:** Everingham & Kerr; SMB Deal Hunter.
  - **Gaps:** service membership revenue share and labor bench not known for E&K target.

- **Short-term rental compliance data SaaS (potential new / property-management compliance adjacency):** Quiet Light listing: B2B STR data/compliance SaaS serving lenders, property managers and municipalities. Revenue $429,763, earnings $348,809, asking $1.45M; revenue doubled since 2022; 85% gross revenue retention; lender revenue doubled YoY; municipal competitor pricing 75% higher per seller claim.
  - **Why it matters for G&B:** interesting regulatory-compliance/data wedge adjacent to property management and municipal compliance. Small but high-margin and recurring; however it is software/data and may not fit G&B's current services/luxury focus.
  - **Quantitative data:** $429,763 revenue; $348,809 earnings; $1.45M ask; 85% gross revenue retention; lender segment doubled YoY; claimed 75% lower municipal pricing than competitors.
  - **Named source/contact:** Quiet Light, Brad Wayland.
  - **Gaps:** customer concentration, data defensibility, compliance-law maintenance burden, and AI/data-scraping replication risk need diligence.

- **Mobile veterinary diagnostics (potential new but likely outside current G&B focus):** SMB Deal Hunter listed Indiana mobile veterinary diagnostics business with repeat revenue: $1.08M revenue, $810K EBITDA, $2.52M ask. Thesis: fewer than 1,000 board-certified veterinary radiologists in US; mobile ultrasound + remote reads; demand capacity constrained by credentialed staff.
  - **Why it matters for G&B:** strong scarcity and repeat-referral economics, but key-person clinical producer risk is high and it does not map strongly to Kay's current right-to-win.
  - **Quantitative data:** $1.08M revenue; $810K EBITDA; $2.52M ask; fewer than 1,000 US board-certified veterinary radiologists.
  - **Named source:** SMB Deal Hunter.
  - **Gaps:** seller production dependence, hired-clinician replacement cost, split between ultrasound vs. remote reads.

- **Industrial lathe manufacturer / aftermarket parts-service (potential new watchlist):** SMB Deal Hunter listed 40+ year industrial lathe manufacturer in CA: $1.13M revenue, $507K EBITDA, $2.208M ask; only 1 full-time and 1 part-time employee; installed base of thousands of machines may drive parts/service demand.
  - **Why it matters for G&B:** aftermarket service and installed-base parts could be attractive and defensible, but owner-head knowledge and manufacturing/industrial complexity are high.
  - **Quantitative data:** $1.13M revenue; $507K EBITDA; $2.208M ask; 40+ years.
  - **Gaps:** new machine vs. recurring parts/service split; customer concentration; documentation and owner transition.

- **Investor portfolio / services acquisition signals:** Anacapa Beacon newsletter highlighted Risk Mitigation Consulting acquired by American Bureau of Shipping after growing topline 2.5x to nearly $50M and EBITDA to $8M; HousingWire acquired Keeping Current Matters; Quick Soft acquired Finanblue; Infosel acquired AdSoft.
  - **Why it matters for G&B:** RMC is relevant to risk/cyber/compliance services serving federal/commercial clients; investor update also shows Anacapa formalizing business development sourcing.
  - **Quantitative data:** RMC topline grew 2.5x to nearly $50M; EBITDA more than doubled to $8M.
  - **Named companies/contacts:** Risk Mitigation Consulting, American Bureau of Shipping, HousingWire, KCM, Quick Soft, Finanblue, Infosel, AdSoft, Anacapa, Jack Richardson.
  - **Gaps:** not direct target flow for G&B; RMC already exited.

#### Source 5: Vault Research

- **Medical/Lab/IVF Specialty Cleaning (existing, new as of 2026-07-07 run):** 2026-07-07 Niche Intelligence report advanced this as a new WEEKLY REVIEW row with score 2.37/3.00. Thesis: contamination-control cleaning for medical offices, clinics, IVF/ART labs, life-science labs, cleanrooms and GMP/ISO-adjacent settings.
  - **Why it matters for G&B:** distinct from generic janitorial and supported by healthcare/lab compliance drivers; today's Axial janitorial signal should not be conflated with this unless specialty protocols are present.
  - **Quantitative data:** healthcare EVS market sources cited approximately $6.76B in 2024 to $9.53B by 2029; another source $7.4B in 2023 to >$12.8B by 2033; global medical cleaning $43.1B in 2025 to $78.8B by 2034; GMP cleaning $1.13B in 2025 to $1.68B by 2035; score 2.37.
  - **Named companies:** SourceONE Building Maintenance, Servicon, Controlled Contamination Services, Xanitos, Pritchard Industries.
  - **Gaps:** specialty margin proof and 50+ buy-box target validation remain open.

- **Water/Wastewater SCADA & Controls Compliance Service Providers (existing, new as of 2026-07-14 run):** 2026-07-14 Niche Intelligence report advanced this as a new WEEKLY REVIEW row with score 2.47/3.0 and estimated target pool 75-175.
  - **Why it matters for G&B:** today’s E&K NJ electrical contractor validates adjacent deal flow, but the investable row is narrower: controls integrators and service firms supporting municipal/industrial water/wastewater SCADA, PLC/HMI, telemetry, instrumentation, cybersecurity, emergency troubleshooting, upgrades and compliance.
  - **Quantitative data:** score 2.47/3.0; target pool 75-175; tracker row rank 37.
  - **Named companies:** no new named targets from vault report beyond research artifacts.
  - **Gaps:** recurring/reoccurring revenue share vs. project integration and equipment pass-through remains the key diligence question.

- **Lifecycle warnings from prior reports:** Vault reports explicitly preserved exclusion/avoid-duplicate context for broad insurance brokerage, standalone domestic trade credit/customs/cargo, broad/luxury cleaning, art-storage-heavy logistics, aerospace/defense, Project Drone, specialty coffee equipment, apparel/fashion supply-chain, women's health/fertility, luxury authentication, private art advisory and art SaaS.
  - **Why it matters for G&B:** recent signals should be routed as reinforcement only when they overlap active rows; do not revive killed/tabled ideas without new evidence addressing prior rejection reasons.

#### Source 6: Passive Signals

- **Yacht property management (potential new, queued):** `brain/inbox/2026-07-17-niche-idea-yacht-property-management.md` defines the candidate as management of personally owned or non-yachting-business-owned yachts: maintenance coordination, crewing/staffing, docking/marina decisions, vendor management, regulatory/documentation support, seasonal prep, storage, scheduling and owner reporting.
  - **Why it matters for G&B:** potentially fits luxury asset stewardship, recurring/reoccurring maintenance/vendor coordination, trust and operational complexity. It is adjacent to asset-light boat/yacht transport coordination and HVA services, but not identical.
  - **Quantitative data:** none yet.
  - **Named companies/contacts:** none yet; Kay has personal familiarity with Port Washington / Long Island yacht-club and boating communities.
  - **Gaps:** target density, acquisition-friendly management-layer businesses, recurring revenue quality, fragmentation and NY/Long Island/NYC metro/NJ/CT fit all unvalidated.

- **Other passive inbox items since July 7:** Beth/Jackie intro and budget trigger were not niche-signal files. No additional `topic/niche-signal` items were created in the current 14-day window.

### Industries/Companies Mentioned

- Existing / reinforced: Premium Pest Management; Fine-Art Logistics Services; Storage & Related Services for High Value Assets; Specialty Insurance Brokerage; HNW / art / collectibles / jeweler's-block insurance; Surplus Lines / specialty program distribution; High-End Commercial Cleaning; Medical/Lab/IVF Specialty Cleaning; Water/Wastewater SCADA & Controls Compliance; Submetering & Utility Billing; Commercial Fire & Life Safety / Premium Security; High-End Beauty & Fragrance Packaging; Fragrance & Cosmetic Product Testing Labs; Luxury Package Testing & Validation Labs; Value-Added Fragrance Distribution; Asset-Light Boat and Yacht Transport Coordination; Property Management / STR compliance.
- Potential new / watchlist: high-end jewelry brand / luxury-services holding company; yacht property management; direct mail/local advertising services; STR compliance intelligence SaaS; mobile veterinary diagnostics; industrial machine aftermarket/service; institutional healthcare plumbing/compliance services.
- Named companies/contacts: ALKEME Insurance; Virtue Risk Partners; American Growth Insurance; Rockbridge Growth Equity; Atomic; Pye-Barker; Stephen Elliott & Company; Stephen Elliott Webb; Motoreum; Bobby Wilson; Mosquito Sheriff; Patrice Rice; Steel City Wildlife; Brad Graham; Dun-Rite Specialized Carriers; Everingham & Kerr; City Publications Atlanta; Brian Jungles; Tower Products; Rachel McGrath; Ashford; Risk Mitigation Consulting; American Bureau of Shipping; HousingWire; Keeping Current Matters; Quick Soft; Finanblue; Infosel; AdSoft; Crozier Fine Arts; NPMA/PestWorld; XPX New Jersey; Sara Rosenthal; Guillermo; Jackie Hirsch; Andrew Freiman; Clayton Sachs; Camilla.

### Data Points for Scoring

- Specialty insurance: AGI launch with nearly $70M committed equity; ALKEME eight Q2 2026 acquisitions; Virtue Risk Partners acquired July 8, 2026.
- FLS/security: advisory sources cite ~125 FLS transactions in 2025, +66.7% YoY; security PE platform transactions +33.3% YoY to 20 deals.
- Utility/submetering: Colorado HB26-1284 effective Jan. 1, 2027 for individual water submeters in new residential construction.
- BK Growth / search environment: ~10 current LOIs, ~7 services / ~3 software; LOI-to-close ~1 in 4; services portfolio mean 4.9x EBITDA, median 5.3x; ~90% proprietary sourced; industry focus 5-8x success uplift.
- Jewelry brand lead: ~$18M revenue; ~$13M inventory; $3-4M cash; ~$8M estimated inventory liquidation floor; potential ~$4M EBITDA estimate from Jackie, unverified.
- Medical/Lab/IVF cleaning prior score: 2.37/3.0; healthcare EVS and medical/GMP cleaning market data from 2026-07-07 report.
- Water/Wastewater SCADA prior score: 2.47/3.0; target pool 75-175.
- E&K NJ commercial electrical: >$6M revenue, $1.2M normalized EBITDA, 35+ years, NJDPM $15M prequalification.
- E&K NY plumbing: $3M revenue, >$500K normalized EBITDA.
- SMB Deal Hunter plumbing/heating/excavation: $1.454M revenue, $633K EBITDA, $2.75M ask.
- STR compliance SaaS: $429,763 revenue, $348,809 earnings, $1.45M ask, 85% gross revenue retention, lender revenue doubled YoY.
- Mobile veterinary diagnostics: $1.08M revenue, $810K EBITDA, $2.52M ask, fewer than 1,000 US board-certified veterinary radiologists cited.
- Industrial lathe manufacturer: $1.13M revenue, $507K EBITDA, $2.208M ask, 40+ years.
- Direct mail / City Publications Atlanta: $650K-$750K historical revenue, ~$742K first-year revenue post-close, ~$150K pre-acquisition SDE, $400K purchase price.
- Pest/wildlife direct responses: Mosquito Sheriff has five franchisees and active FDD; Steel City Wildlife interested; target-size concern remains under-$500K EBITDA in many East Coast pest leads.

### Source Gaps / Negative Evidence

- last30days Reddit returned 403; X/Twitter and YouTube were unavailable; Polymarket had no useful markets; web/social evidence is partial.
- Some Gmail HTML bodies were noisy; targeted text/plain extraction worked for most relevant messages, but Axial janitorial full financial table could not be extracted beyond snippet.
- No attachments/CIMs were opened in this RECENT pass.
- Granola was available for last-14-day notes; personal/non-business calls were skimmed by summary and only business-relevant notes were extracted.
- Passive signals contained one new niche idea (`yacht property management`); other recent inbox items were not niche-signal files.
- Active WEEKLY REVIEW niches with no fresh RECENT signal in this pass: Estate Management Companies; NY Metro Multi-Location Independent Auto Repair Succession; Environmental Field Sampling & Compliance Services; Fire-Protection-Adjacent Industrial MRO; Trade Credit / Customs Bonds / Cargo Insurance Brokerage; Property Tax Appeal Services; Building Energy & Emissions Compliance Services; HOA / Community Association Management; Facilities Management / Commercial Building Services beyond broad janitorial; Property Management beyond STR compliance SaaS; Reserve Study & Building Engineering Studies; Truck Licensing & Compliance Platform; Luxury Amenity Management; Sign and Lighting Maintenance Programs; Permit Expediting & Zoning/Land-Use Consulting; Lease Administration & RE Back-Office Services; AED; Aerospace Defense.

→ READY

---
## [niche-intel-synthesizer] — 2026-07-21 22:40 EDT
**Source:** Cross-source synthesis of RECENT + HISTORICAL posts, tracker snapshots, and `brain/context/learnings.md`
**Status:** complete

### 1. Cross-Source Signal Matrix

| Niche / Industry | RECENT Sources | HISTORICAL Sources | Total Source Count | Strength | Lifecycle / Duplicate Control |
|---|---:|---:|---:|---|---|
| Beauty / fragrance / cosmetics supply-chain infrastructure: testing labs, package validation, value-added distribution, 3PL/kitting | Granola calls, vault research | historical calls / inventory | 3 | STRONG | Duplicate of WEEKLY REVIEW rows for Fragrance & Cosmetic Product Testing Labs, Luxury Package Testing & Validation Labs, High-End Beauty & Fragrance Packaging, Value-Added Fragrance Distribution. Materially strong as a cluster, but Identifier should narrow, not add broad duplicate. |
| Specialty insurance infrastructure: HNW/art/collectibles, jeweler's block, surplus lines, trade-risk brokerage | web, Granola calls, vault research | calls, email, prior research | 5 | VERY STRONG | Existing WEEKLY REVIEW / long-term rows. Generic brokerage has known valuation/QSBS/operator-credibility challenge; advance only narrow proprietary or infrastructure wedges. |
| Fine-art logistics / specialty storage / high-value-asset services | newsletters, Gmail deal flow, Granola calls, vault research | calls, prior diligence | 5 | VERY STRONG | Existing active / long-term rows. Storage-heavy core has capex and margin warnings; services-only or HVA operations response is actionable. |
| Commercial fire & life safety / premium security / industrial fire-adjacent MRO | web, vault research | calls, prior inventory | 3 | STRONG | Existing WEEKLY REVIEW rows. Live with caution because PE consolidation and commodity installer risk are high. |
| Water / wastewater SCADA, controls, and compliance-adjacent electrical services | Gmail deal flow, vault research | tracker / prior report context | 2 | STRONG | Duplicate of WEEKLY REVIEW row. E&K electrical contractor validates adjacency but does not prove narrow SCADA/controls revenue mix. |
| Pest / wildlife / mosquito control | newsletters, Gmail deal flow, Granola calls | tracker context / prior search history | 3 | STRONG but NEGATIVE | Existing active outreach. New owner responses are active-deal-flow signals, not thesis validation; target-size and competition concerns persist. |
| Commercial cleaning / medical-lab-IVF specialty cleaning | Gmail deal flow, vault research | calls / inventory | 3 | STRONG | Generic janitorial should not advance. Medical/lab/IVF specialty cleaning remains distinct and live; broad luxury boutique cleaning was challenged. |
| Facilities management / institutional facility services | Gmail deal flow | historical email | 2 | STRONG | Duplicate of WEEKLY REVIEW Facilities row; useful only if narrowed to contracted multi-site maintenance / hard services rather than generic janitorial or landscaping. |
| Sign and lighting maintenance for multi-location brands | Gmail/newsletter mentions | calls, email | 3 | STRONG | Duplicate of WEEKLY REVIEW row. Maintain narrow service/maintenance framing, not sign manufacturing. |
| Luxury amenity management / private tenant club operations | Granola/context | calls | 2 | STRONG | Duplicate of WEEKLY REVIEW row. Needs contracted revenue and margin validation. |
| Yacht property management / asset-light boat-yacht transport coordination | passive inbox | calls | 2 | STRONG | Yacht property management is materially distinct from asset-light transport, but adjacent. New passive signal can be queued as a watchlist/intake branch; do not merge blindly. |
| Geotechnical engineering / construction materials testing | tracker/vault context | historical email | 2 | STRONG | Duplicate of WEEKLY REVIEW row. Continue only after repeat-revenue and cyclicality check. |
| HOA / community association management | tracker context | historical email | 2 | STRONG | Duplicate of WEEKLY REVIEW row. Warm CAI/Guillermo channel remains more appropriate than cold DealsX. |
| STR compliance intelligence SaaS | Gmail deal flow | none | 1 | MODERATE | New/watchlist only. Quantitative listing is attractive but software/data replication and G&B fit are unresolved. |
| High-end jewelry brand / luxury-services holdco | Granola calls | none | 1.5 | MODERATE | Not a niche-intel candidate in the normal sense; active proprietary lead / investment judgment item. Inventory-heavy, B2C, non-recurring. |
| Mobile veterinary diagnostics | Gmail deal flow | none | 1 | MODERATE | Quantitative listing, but high key-person clinical risk and weak G&B right-to-win. Watchlist only. |
| Industrial lathe manufacturer / aftermarket parts-service | Gmail deal flow | none | 1 | MODERATE | Quantitative listing; possible installed-base service economics. Manufacturing complexity and owner-knowledge risk. Watchlist only. |
| Direct mail / local advertising services | newsletter | none | 1 | MODERATE | Quantified ETA case study, but weak G&B right-to-win and only one source. Watchlist only. |
| Institutional healthcare plumbing / compliance plumbing | Gmail deal flow | none | 1 | MODERATE | Quantified deal-flow, but generic trades unless narrowed to contracted healthcare/institutional service. |
| Apparel / fashion supply-chain testing and warehousing | Granola/context | historical calls / killed-tabled context | 2 | SUPPRESS | Prior challenge: poor third-party willingness to pay, low fashion margins, weak target proof. Do not advance without concrete recurring compliance buyer and target list. |
| Women's health / fertility / post-op care | none current | historical calls / killed context | 1 | SUPPRESS | Killed for early-stage company base, regulatory risk, and crowded fertility searcher interest. |
| Art advisory / art SaaS / collection management / conservation / escrow | Crozier marketing adjacent only | historical calls / killed-tabled context | 2 | SUPPRESS | Multiple dead or tabled branches. Only services/logistics/storage/insurance variants remain live. |

### 2. Named Company Registry

| Company Name | Niche | Source | Independence / Buy-Box Read | Outreach Flag | Warm Contact | Notes |
|---|---|---|---|---|---|---|
| Stephen Elliott & Company LLC | Fine-art logistics / HVA services | RECENT Gmail deal flow | Potential independent target; size unknown | WARM_INTRO / ACTIVE_RESPONSE | Stephen Elliott Webb | Direct DealsX response; do not cold-route. Needs qualification call/revenue/ownership transition. |
| Motoreum | Collector-car / HVA storage-adjacent services | RECENT Gmail deal flow | Potential independent target; business-model mix unknown | WARM_INTRO / ACTIVE_RESPONSE | Bobby Wilson | Soft response, not sale intent. Qualify storage vs. brokerage/services revenue. |
| Mosquito Sheriff | Pest / mosquito franchise | RECENT Gmail deal flow | Founder-led but franchise-system complexity; scale unknown | WARM_INTRO / ACTIVE_RESPONSE | Patrice Rice | Active FDD, 5 franchisees, succession trigger. Deal-flow item, not thesis validation. |
| Steel City Wildlife | Wildlife / pest | RECENT Gmail deal flow | Potential independent target; size unknown | WARM_INTRO / ACTIVE_RESPONSE | Brad Graham | "Interested" response. Qualify revenue/EBITDA and service geography. |
| Dun-Rite Specialized Carriers | Boat/yacht transport | RECENT Gmail deal flow | Unknown | VAULT_HISTORY / LOW_SIGNAL | Anthony | Auto-reply only; no outreach flag beyond follow-up queue if already in DealsX. |
| Unnamed 80-year-old high-end jewelry business | High-end jewelry / luxury holdco | RECENT Granola calls | Active proprietary lead; inventory-heavy, B2C/non-recurring | ACTIVE_DEAL | Sara Rosenthal / Whitney trustee owner / Kay network | Treat outside niche-intel tracker. Need EBITDA, inventory aging, leases, ROIC. |
| Bergdorf Goodman | Jewelry customer/channel comp | RECENT Granola calls | Large retailer, not target | VAULT_HISTORY | Luxury network | Customer/channel signal only. |
| London Jewelers | Jewelry retail comp | RECENT Granola calls | Retailer/comp; likely not target from this source | VAULT_HISTORY | Luxury network | Comp for jewelry lead context. |
| Bloomingdale's | Jewelry channel comp | RECENT Granola calls | Large retailer, not target | VAULT_HISTORY | Luxury network | Customer/channel context only. |
| Chenmark | Holdco comp | RECENT Granola calls | PE/holdco comp, not target | VAULT_HISTORY | Advisors | Comparable operating architecture. |
| Tower Products | Beauty/fragrance supply-chain / press-room chemistry comp | RECENT Granola calls | Searcher-acquired comp | VAULT_HISTORY | Rachel McGrath cited | Validation comp, not cold target. |
| Ashford / Ashford Advisors context | Beauty 3PL / HOA expertise context | RECENT Granola calls, historical HOA context | Advisor/company context, not target | WARM_INTRO | Guillermo Lavergne | Use as river-guide source, not target. |
| Crozier Fine Arts | Fine-art logistics / storage | RECENT newsletters; historical context | Large/strategic-owned profile likely not target | VAULT_HISTORY | Art network | Comp / market validator. |
| Acumen International | Fine-art logistics / storage | HISTORICAL calls | Prior pursued deal; partner/capex/margin issues | ACTIVE_DEAL / VAULT_HISTORY | Levi Phelps | Do not cold-route; lifecycle warning. |
| Voxme | Fine-art logistics software/process comp | HISTORICAL calls | Comp/vendor, not target | VAULT_HISTORY | Levi/Acumen context | Process improvement signal. |
| Maquette | Fine-art logistics / storage | HISTORICAL calls | Comp/target universe | VAULT_HISTORY | Art network | Check context before outreach. |
| SAT / Safe Art Transport | Fine-art logistics | HISTORICAL calls | Comp/target universe | VAULT_HISTORY | Art network | Check context before outreach. |
| Art Crating | Fine-art services | HISTORICAL calls | Comp/target universe | VAULT_HISTORY | Art network | Check context before outreach. |
| UOVO | Fine-art storage/logistics | HISTORICAL calls | Large consolidated comp, not target | VAULT_HISTORY | Art network | Exit/competition comp. |
| Trade Risk Group | Trade credit / customs bonds / cargo insurance | HISTORICAL email | Named specialist; likely target/comp | WARM_INTRO | Jeremy Black | Existing live thesis context. Do not cold-route without Jeremy context. |
| Trade Acceptance Group | Trade credit insurance | HISTORICAL email/research | Named specialist/comp | WARM_INTRO | Jeremy Black | Prior tabled domestic trade-credit context; use cautiously. |
| Meridian / Texel | Trade credit insurance | HISTORICAL email/research | Larger specialist/comp | VAULT_HISTORY | Jeremy Black | Comp / market map. |
| Euler Hermes / Allianz Trade | Trade credit carrier | HISTORICAL email/research | Large carrier, not target | VAULT_HISTORY | Jeremy Black | Carrier ecosystem. |
| Atradius | Trade credit carrier | HISTORICAL email/research | Large carrier, not target | VAULT_HISTORY | Jeremy Black | Carrier ecosystem. |
| Coface | Trade credit carrier | HISTORICAL email/research | Large carrier, not target | VAULT_HISTORY | Jeremy Black | Carrier ecosystem. |
| ALKEME Insurance | Specialty insurance brokerage platform | RECENT web | PE-backed/acquisitive platform | VAULT_HISTORY / COMP | none surfaced | Exit/competition signal; not cold target. |
| Virtue Risk Partners | Specialty MGA / programs | RECENT web | Recently acquired by ALKEME | VAULT_HISTORY / COMP | none surfaced | Comp only. |
| American Growth Insurance | Specialty brokerage platform | RECENT web | Sponsor-backed platform | VAULT_HISTORY / COMP | none surfaced | Consolidation signal; not target. |
| Rockbridge Growth Equity | Sponsor | RECENT web | Investor, not target | VAULT_HISTORY | none surfaced | Platform-backing signal. |
| Atomic | Venture studio / sponsor context | RECENT web | Not target | VAULT_HISTORY | none surfaced | Platform-backing signal. |
| Pye-Barker | FLS/security platform | RECENT web | PE-backed consolidator/platform | VAULT_HISTORY / COMP | none surfaced | Exit/competition signal. |
| Summit Companies | FLS/security platform | RECENT web | Platform/comp | VAULT_HISTORY / COMP | none surfaced | Market-map comp. |
| BlackRock Long Term Private Capital | Sponsor | RECENT web | Investor, not target | VAULT_HISTORY | none surfaced | FLS consolidation context. |
| Arch Amenity Group | Luxury amenity management | HISTORICAL calls | Large player / comp | VAULT_HISTORY / COMP | Mike Horowitz / Doug Tudor | Validates market; not likely target. |
| Paramount Group | Commercial real estate / amenity example | HISTORICAL calls | Public/large property owner, not target | VAULT_HISTORY | Mike Horowitz | Demand-side example. |
| Chanel | Luxury operating-history context | RECENT/HISTORICAL calls | Not target | VAULT_HISTORY | Kay background | Right-to-win and customer archetype context. |
| City Publications Atlanta | Direct mail/local advertising | RECENT newsletter | Searcher-acquired small business; likely too small as standalone | VAULT_HISTORY / COMP | Brian Jungles | ETA comp only unless direct-mail lane is researched. |
| Risk Mitigation Consulting | Risk/cyber/compliance services | RECENT investor update | Already exited to American Bureau of Shipping | VAULT_HISTORY / COMP | Anacapa context | Exit validation, not target. |
| American Bureau of Shipping | Risk/compliance acquirer | RECENT investor update | Large acquirer, not target | VAULT_HISTORY / COMP | Anacapa context | Exit buyer signal. |
| HousingWire | Media/data acquisition platform | RECENT investor update | Platform/comp | VAULT_HISTORY / COMP | Anacapa context | Not G&B target. |
| Keeping Current Matters | HousingWire acquisition | RECENT investor update | Already acquired | VAULT_HISTORY / COMP | Anacapa context | Not target. |
| Quick Soft | Software acquirer | RECENT investor update | Acquirer/comp | VAULT_HISTORY / COMP | Anacapa context | Not target. |
| Finanblue | Software acquisition | RECENT investor update | Already acquired | VAULT_HISTORY / COMP | Anacapa context | Not target. |
| Infosel | Software acquirer | RECENT investor update | Acquirer/comp | VAULT_HISTORY / COMP | Anacapa context | Not target. |
| AdSoft | Software acquisition | RECENT investor update | Already acquired | VAULT_HISTORY / COMP | Anacapa context | Not target. |
| NPMA / PestWorld / NYPMA / PWIPM | Pest association ecosystem | RECENT newsletters | Association, not target | WARM_INTRO | pest network | River-guide/channel source. |
| Nissus | Pest industry sponsor/vendor | RECENT newsletters | Vendor/comp, not target from this source | VAULT_HISTORY | pest association context | Ecosystem signal only. |
| XPX New Jersey | Exit-planning network | RECENT newsletters | Network, not target | WARM_INTRO | Katie Noonan / Angie Ellis | Sourcing channel, not niche. |
| Everingham & Kerr | Broker/source | RECENT + HISTORICAL Gmail | Intermediary, not target | IN_CRM? / SOURCE | Existing broker source likely | Source for geotech, HOA, electrical, plumbing. CRM not checked in this pass. |
| Axial | Deal platform/source | RECENT + HISTORICAL Gmail | Platform, not target | SOURCE | n/a | Source only. |
| SMB Deal Hunter | Newsletter/source | RECENT + HISTORICAL Gmail | Source, not target | SOURCE | Helen Guo | Source only. |
| Quiet Light | Broker/source | RECENT Gmail | Source, not target | SOURCE | Brad Wayland | Source for STR compliance SaaS listing. |
| Unnamed STR compliance SaaS | STR compliance data SaaS | RECENT Gmail | Small, high-margin software/data business | NEW_TARGET? | Quiet Light / Brad Wayland | Only brokered listing evidence. Needs software/data defensibility screen before outreach. |
| Unnamed mobile veterinary diagnostics business | Mobile veterinary diagnostics | RECENT Gmail | Small profitable business; key-person risk | NEW_TARGET? | SMB Deal Hunter | Watchlist only; weak G&B fit. |
| Unnamed industrial lathe manufacturer | Industrial aftermarket / MRO | RECENT Gmail | Small manufacturer, installed-base possible | NEW_TARGET? | SMB Deal Hunter | Watchlist only; needs service/parts revenue split. |
| Unnamed NJ commercial electrical contractor | Water/wastewater infrastructure adjacency | RECENT Gmail | $6M+ revenue / $1.2M EBITDA; project-heavy risk | NEW_TARGET? | Everingham & Kerr | Do not confuse with SCADA row until controls/service mix proven. |
| Unnamed NY plumbing contractor | Institutional / healthcare plumbing | RECENT Gmail | $3M revenue / >$500K EBITDA | NEW_TARGET? | Everingham & Kerr | Generic trades unless healthcare/institutional recurring service is material. |
| Unnamed MA plumbing/heating/excavation company | Plumbing/heating/excavation | RECENT Gmail | $1.454M revenue / $633K EBITDA; membership program | NEW_TARGET? | SMB Deal Hunter | Watchlist; service membership mix matters. |
| Unnamed NJ geotechnical/CMT company | Geotech / CMT | HISTORICAL email | $3.6M+ revenue / ~$1M EBITDA | NEW_TARGET? | Everingham & Kerr | Already-informed WEEKLY REVIEW row; check broker process before any outreach. |
| Unnamed NJ association-management company | HOA management | HISTORICAL email | ~$750K revenue, likely subscale | NEW_TARGET? | Everingham & Kerr | Too small as platform but validates model. |
| Unnamed institutional facility-services provider | Facilities maintenance | HISTORICAL email | $15.3M 2024 revenue visible | NEW_TARGET? | Axial | Need EBITDA/service mix. |
| Unnamed UT facility-maintenance contractor | Facility maintenance | HISTORICAL email | $4.514M revenue / $838K EBITDA | NEW_TARGET? | SMB Deal Hunter | Validates multi-site contract thesis. |
| Unnamed MO sign manufacturer | Sign/lighting maintenance | HISTORICAL email | $4.364M revenue / $661K EBITDA | NEW_TARGET? | SMB Deal Hunter | Only attractive if maintenance/lighting service layer is material. |
| Unnamed trucking compliance platform | Truck licensing/compliance | HISTORICAL email | $1.039M revenue / $412K EBITDA | NEW_TARGET? | SMB Deal Hunter / Helen Guo | Existing WEEKLY REVIEW row; low scale and young company. |

**Registry limitation:** Attio was not queried in this pass because the prompt-provided curl pattern reads secrets from `.env` directly, which conflicts with the repo credential rules. Outreach flags therefore use chatroom/vault/warm-contact evidence and should be treated as routing guidance pending CRM verification.

### 3. Contact-to-Niche Map

| Contact | Relationship Warmth | Niches They Can Help With | What to Ask Them | Last Contact / Source |
|---|---|---|---|---|
| Sara Rosenthal | HOT | High-end jewelry lead; jeweler's block insurance; luxury-services holdco | Clarify owner motivations, financial access path, jewelry operating diligence priorities | RECENT Granola |
| Guillermo Lavergne | HOT | Beauty/fragrance supply chain; HOA/property management; pest thesis challenge; jewelry lead judgment | Pressure-test beauty/3PL/testing target definitions and HOA channel; keep pest negative evidence visible | RECENT Granola / historical calls |
| Jackie Hirsch | HOT | Jewelry lead / luxury retail diligence | Validate EBITDA/inventory/lease assumptions and retail multiple appetite | RECENT Granola |
| Andrew Freiman | HOT | Specialty insurance; art storage/logistics; jewelry diligence | Introduce/triage specialty insurance contacts and storage/HVA leads | RECENT Granola |
| Camilla | HOT | Trade-risk insurance, beauty/fragrance, jewelry diligence | Help split testing vs. packaging vs. distribution and identify target-density questions | RECENT Granola / historical research |
| Clayton Sachs | HOT | Beauty/fragrance, storage, pest strategy, search strategy | Validate strongest luxury-compliance branches and sourcing channel focus | RECENT Granola |
| Jeremy Black | WARM/HOT | Trade credit, customs bonds, cargo insurance | Reconfirm whether bundled trade-risk brokerage fixes prior no-RTW / thin-pool objection; ask for target/operator names | HISTORICAL Gmail |
| August Felker | WARM/HOT but stale | HNW personal lines, fine-art/specialty insurance | Refresh named target list and producer/operator angle; avoid generic insurance brokerage | HISTORICAL calls |
| Hunter Hartwell | WARM | Specialty insurance / HNW personal lines | Validate carve-out/proprietary access and operator-credibility path | HISTORICAL calls |
| Chris Wise | WARM | Fine-art insurance brokerage | Ask what specific brokerage profiles are enterable without existing book of business | HISTORICAL calls |
| Tobias MarshBerry | WARM | Insurance brokerage M&A | Pressure-test valuation/QSBS/roll-up saturation for specialty brokerage branches | HISTORICAL calls |
| Richard Augustine | WARM | Specialty insurance / jeweler's block | Map broker/MGA/carrier workflow and independent specialists | RECENT Granola mention / historical insurance context |
| Mike Horowitz | HOT | Luxury amenity management, sign/lighting, security, marine/yacht, MRO | Ask for named vendor/operator referrals and which services are contracted vs. project-only | HISTORICAL calls |
| Doug Tudor | HOT | Luxury amenity management, yacht/boat transport, marine services | Ask for operators in boat transport/management and amenity outsourcing with owner transition | HISTORICAL calls |
| Jeff Stevens | HOT | Fire safety, industrial MRO, specialty steel machinery/service | Narrow concentric-circle MRO niches and validate mission-critical failure modes | HISTORICAL calls |
| Warren Chan | WARM/HOT | Art logistics/storage, art-world suppressions | Use for HVA services introductions, not revived art advisory/SaaS ideas | HISTORICAL calls |
| Levi Phelps | WARM/HOT | Acumen/art logistics lifecycle | Only use for lessons learned / Acumen context; avoid cold re-approach | HISTORICAL calls |
| Stephen Elliott Webb | WARM/ACTIVE RESPONSE | Fine-art logistics / HVA services | Qualify ownership, revenue mix, storage vs. services, willingness to talk | RECENT Gmail |
| Bobby Wilson | WARM/ACTIVE RESPONSE | Collector-car storage / HVA services | Clarify business model split and recurring storage/service revenue | RECENT Gmail |
| Patrice Rice | WARM/ACTIVE RESPONSE | Mosquito franchise / pest | Qualify franchise economics, EBITDA, owner transition, franchisor constraints | RECENT Gmail |
| Brad Graham | WARM/ACTIVE RESPONSE | Wildlife control / pest | Qualify revenue/EBITDA, service mix, geography, reason for interest | RECENT Gmail |
| Anthony at Dun-Rite | COOL | Boat/yacht specialized carrier | Only follow up if already in DealsX queue; auto-reply is not substantive | RECENT Gmail |
| Helen Guo | WARM/SOURCE | SMB Deal Hunter listings: trucking, facilities, sign, plumbing, vet diagnostics, lathe | Ask for broker/listing access only after Identifier chooses a lane | Historical + recent Gmail |
| Brad Wayland | WARM/SOURCE | STR compliance SaaS | Ask for CIM only if software/data-risk screen passes | RECENT Gmail |
| Katie Noonan | WARM/SOURCE | XPX / exit-planning network | Use for NJ owner-transition relationships, not a niche itself | RECENT newsletters |
| Angie Ellis | WARM/SOURCE | XPX / exit-planning network | Same: relationship channel for NJ transition owners | RECENT newsletters |
| Rachel McGrath | COOL/WARM | Beauty/fragrance / Tower Products comp | Ask for searcher/operator lessons from press-room chemistry acquisition if reachable | RECENT Granola mention |
| Brian Jungles | COOL/WARM | Direct mail/local advertising ETA case | Ask only if direct-mail lane is promoted to research | RECENT newsletter |
| Connor Groce | COOL | Franchise acquisition strategy | Use only for franchise-system diligence if Mosquito Sheriff advances | RECENT newsletter |
| Grant Hensel / Eli Albrecht | COOL | ETA filter context | No niche-specific ask; use as framework only | RECENT newsletter |
| Albert Kim | WARM | Pest negative evidence | Validate whether East Coast pest target scarcity mirrors West Coast searcher experience | RECENT Granola |
| Kay's brother | HOT | Marine logistics / cargo / yacht transport | Validate asset-light carrier coordination and marine logistics economics | HISTORICAL / tracker context |

### 4. Lead Lifecycle Tracker

| Niche / Strategy | Proposed By | When | Challenged By | When | Reason | Status |
|---|---|---|---|---|---|---|
| Generic pest management / East Coast premium pest | Prior tracker / active outreach; current DealsX responses | Active since 2026-04 | Clayton Sachs, Guillermo, West Coast searcher Albert Kim | RECENT calls | East Coast targets appear small, picked over, gatekeeper-heavy, and higher multiple; many under $500K EBITDA | LIVE-DEPRIORITIZED. Work active responses only; do not promote as fresh thesis. |
| Beauty/fragrance/cosmetics infrastructure cluster | Clayton, Guillermo, Camilla, Andrew | RECENT calls | Definition discipline challenge from synthesizer/learnings | 2026-07-21 | Testing labs, package validation, distribution, 3PL/kitting have different buyers, margins, working capital, and recurrence | LIVE. Advance only narrowed sub-niches; avoid broad "beauty supply chain" row. |
| High-end jewelry brand / luxury holdco | Owner via Kay network; Sara/Guillermo/Jackie/Andrew context | RECENT calls | Search-model constraints from advisors | RECENT calls | Inventory-heavy, B2C/retail, non-recurring, lease and ROIC risk; financials unconfirmed | LIVE ACTIVE LEAD, not tracker niche. Requires investment judgment, not Identifier promotion. |
| Generic specialty insurance brokerage | August/Hunter/Chris/Tobias and web consolidation | Historical + recent | Investors/advisors / MarshBerry context | Historical | Multiples, QSBS non-qualification, operator credibility, heavy roll-up activity | TABLED / LIVE ONLY IF NARROW. Advance HNW/art/jeweler's-block/surplus-lines/trade-risk only with proprietary angle. |
| Trade credit / customs bonds / cargo insurance | Jeremy Black | 2026-02 to 2026-03 | Prior tracker kill/table rationale | 2026-03 to 2026-05 | Domestic trade credit alone had thin target pool and no right-to-win; customs/cargo killed once as no RTW | LIVE ONLY AS BUNDLED TRADE-RISK BROKERAGE. New data partially addresses unit-econ but not RTW. |
| Fine-art storage/logistics / Acumen-style storage | Art network, Levi/Acumen, Warren | 2025-2026 | Investor feedback / Acumen diligence | 2025-2026 | Asset-heavy storage, low blended margins, capex, partner complexity, labor bottlenecks | LIVE WITH RESCOPE. Services-only / HVA services remain; storage-heavy deals require high margin proof. |
| Art advisory / collection management / art SaaS / conservation / escrow | Warren / art-world research | Historical | Kay and prior killed/tabled tracker | 2026-03 to 2026-06 | Low TAM, labor/key-person risk, weak willingness to pay, no targets, AI/platform risk | KILLED / SUPPRESS. Do not revive except logistics/storage/insurance variants. |
| Medical/lab/IVF specialty cleaning | Guillermo/Kay branch from cleaning discussions and 2026-07-07 run | 2026-06 to 2026-07 | Generic cleaning challenge | Historical + recent | Broad/luxury boutique cleaning dominated by nationals and hard lead-gen; only regulated specialty cleaning is differentiated | LIVE. Keep separate from generic janitorial. |
| Luxury boutique / broad commercial cleaning | Guillermo/Kay | 2026-06 | Guillermo/Kay | 2026-06 | National players dominate; differentiation and lead generation weak | DEAD as broad lane. |
| Fire/life safety / security / fire-adjacent MRO | Jeff, Mike, web deal activity | 2026-06 to RECENT | Market-map/advisory evidence and prior caution | RECENT | Attractive recurring compliance but intense PE consolidation; generic security commodity risk | LIVE WITH CAUTION. Narrow to code-mandated inspection/MRO/luxury-retail lifecycle service. |
| EV-charging garage/lot safety wedge | Passive signal / fire-safety adjacency | 2026-06 | Tabled EV Software/Charging rationale | Tracker snapshot | Political/climate/software concern applies to EV charging/software, not fire/electrical compliance services | LIVE ONLY AS FIRE/ELECTRICAL COMPLIANCE WEDGE. Do not promote EV software. |
| Yacht property management | Passive inbox | 2026-07-17 | Prior Yacht/Fleet Maintenance Software tabled | Tracker snapshot | Software version was tabled; service management layer not yet tested. Need target density and recurring management revenue | WATCHLIST / NEW INTAKE. Distinct enough to research, not advance yet. |
| Marine services / boat maintenance/detailing | Doug/Mike | 2026-06 | Synthesizer / historical framing | 2026-07-21 | B2C/seasonal/asset-heavy risk unless coordination/logistics | TABLED BRANCH. Transport coordination is live; seasonal maintenance not live without proof. |
| Apparel/fashion supply-chain testing/customs/warehousing | Guillermo/Kay and Chanel context | 2026-06 | Guillermo/Kay | 2026-06 | Fashion margins challenged, third-party willingness to pay low, compliance often in-house, no clear target | DEAD / SUPPRESS unless concrete recurring compliance buyer and target list emerge. |
| Women's health / fertility / post-op care | Early thesis lanes / Guillermo brainstorm | Historical | Guillermo/Kay / tracker | 2026-06 | Too early-stage, few acquirable targets, regulatory risk, fertility crowded by searchers | KILLED / SUPPRESS. |
| Direct mail/local advertising services | Acquiring Minds case | RECENT newsletter | Synthesizer / G&B fit screen | 2026-07-21 | One case study, weak right-to-win, not compliance/luxury/HVA | WATCHLIST ONLY. |
| STR compliance data SaaS | Quiet Light listing | RECENT Gmail | Software/data-risk screen | 2026-07-21 | Small software/data asset, AI/scraping replicability, law-maintenance burden | WATCHLIST ONLY. |
| Mobile veterinary diagnostics | SMB Deal Hunter listing | RECENT Gmail | Synthesizer / G&B fit screen | 2026-07-21 | Clinical credential/key-person dependence; weak G&B right-to-win | WATCHLIST ONLY. |
| Industrial lathe manufacturer / aftermarket parts | SMB Deal Hunter listing | RECENT Gmail | Synthesizer / manufacturing complexity screen | 2026-07-21 | Owner knowledge, manufacturing complexity, unknown service/parts recurrence | WATCHLIST ONLY. |

### 5. Convergence Report

1. **Beauty / fragrance / cosmetics infrastructure cluster — RECOMMEND: advance as a narrowing exercise, not a new broad row.**  
   Source count: 3. Named companies/contacts: Tower Products, Ashford, L'Oreal customer archetype; Clayton, Guillermo, Camilla, Andrew, Rachel McGrath. Buy-box fit: strong on Kay right-to-win, compliance/testing, B2B support, luxury adjacency; mixed by sub-segment on working capital and recurrence. Actionability: high if Identifier splits into product testing labs, package validation labs, value-added fragrance distribution, and beauty 3PL/kitting, then selects one.

2. **Specialty insurance infrastructure — RECOMMEND: keep live only in narrow wedges: jeweler's block, HNW/art/collectibles, surplus-lines compliance, or bundled trade-risk brokerage.**  
   Source count: 5. Named companies/contacts: ALKEME, Virtue Risk Partners, AGI, Trade Risk Group, Trade Acceptance Group, Meridian/Texel, carriers; Jeremy Black, August Felker, Hunter Hartwell, Chris Wise, Tobias MarshBerry, Richard Augustine. Buy-box fit: excellent recurring economics and exit pathways, but generic brokerage fails valuation/QSBS/operator-credibility concerns. Actionability: medium-high via warm contacts, but needs CRM check and target-specific proprietary angle.

3. **Fine-art logistics / HVA services / specialty storage-adjacent services — RECOMMEND: route active responses, while preserving storage-heavy caution.**  
   Source count: 5. Named companies/contacts: Stephen Elliott & Company, Motoreum, Crozier, Acumen, UOVO, Maquette, SAT, Art Crating; Stephen Elliott Webb, Bobby Wilson, Warren Chan, Levi Phelps, Andrew Freiman. Buy-box fit: strong Kay right-to-win and proprietary access; recurring/sticky HVA services possible. Red flag: storage-heavy models can be capex-heavy and margin-thin. Actionability: high for active responses; Identifier should not create duplicate rows.

4. **Fire/life safety, premium security, and fire-adjacent industrial MRO — RECOMMEND: continue under existing rows with a stricter "code-mandated recurring service" filter.**  
   Source count: 3. Named companies/contacts: Pye-Barker, Summit, BlackRock LTPC; Jeff Stevens, Mike Horowitz. Buy-box fit: strong compliance/reoccurring demand and mission-critical service; actionability moderate because PE saturation and commodity installer risk are substantial. Best next question: can G&B find sub-platform local specialists with inspection/testing/maintenance revenue rather than project installation.

5. **Yacht property management / marine asset services — RECOMMEND: keep as new intake watchlist, not promotion.**  
   Source count: 2 if combined with historical marine/boat transport; 1 for yacht property management specifically. Named contacts: Doug Tudor, Mike Horowitz, Kay's brother; no companies yet. Buy-box fit: promising HVA/luxury asset stewardship and recurring coordination thesis, but target density, scale, seasonality, and acquisition-friendly management companies are unvalidated. Actionability: medium-low until target discovery proves named independent operators.

### Source Gaps for Sidecar

- OneNote SEARCH FUND was not covered because no OneNote MCP tools were exposed and no local OneNote export was found.
- ChatGPT export was not covered because `~/Downloads` does not exist on the VPS and no `selected_business_conversations.json` was found under `/home/ubuntu`.
- last30days was partial: Reddit returned 403; X/Twitter and YouTube were unavailable; Polymarket had no useful niche markets.
- Historical Granola pagination was not exhausted, though older notes appear represented in `brain/calls/`.
- RECENT Gmail did not open attachments/CIMs, and at least one Axial janitorial HTML body could not be fully extracted beyond snippets.
- Attio CRM / Active Deals cross-reference was not performed by this synthesizer because the skill's example uses unsafe `.env` secret-reading. Routing flags are therefore evidence-backed from chatroom/vault/warm-contact context but require CRM verification before any outreach list write.

→ READY

## [niche-intel-identifier] — 2026-07-21 22:47 EDT
**Source:** Synthesizer convergence report + tracker lifecycle JSON + independent web validation
**Status:** complete

### IDENTIFY + INDUSTRY VALIDATION

I evaluated the five convergence signals against `/tmp/niche-weekly-review.json`, `/tmp/niche-ideation.json`, `/tmp/niche-killed.json`, `/tmp/niche-tabled.json`, `brain/context/learnings.md`, and the synthesizer lifecycle table. Three converged areas are not new candidates: beauty/fragrance testing, packaging, and distribution are already active/ideation rows except for the compliance-enabled fulfillment wedge below; specialty insurance is already active except for the jeweler's block wedge below; fine-art/HVA services, fire/life safety, and pest are active rows or active deal flow, not new niches. I am surfacing three defensible candidates, with target-pool caveats explicit.

#### Candidate 1

- Niche: Yacht Property Management for Private Yacht Owners in Coastal HNW Markets
- Thesis: Private yacht owners need an outsourced operating layer to coordinate planned maintenance, crew, compliance documents, marina/vendor management, budgeting, accounting, seasonal prep, and owner reporting. This is distinct from the active "Asset-Light Boat and Yacht Transport Coordination" row because the buyer is the yacht owner/family office, the recurring behavior is ongoing vessel stewardship, and the service bundle looks more like estate management for a high-value movable asset than transport brokerage.
- QUICK SCREEN:
  - Margins: Moderate — asset-light coordination businesses can be service-fee/retainer based, but public comps rarely disclose EBITDA; labor/captain dependency and vendor pass-throughs likely compress margins versus software or insurance. Treat as 12%-25% EBITDA hypothesis until operator data is found.
  - Recurring / Reoccurring Revenue: High — management pages consistently describe ongoing crew, maintenance, compliance, accounting, inspections, budgeting, and operational oversight rather than one-time projects. IYC describes functions including safety compliance, accounting, planned maintenance, crew management, and vessel documents; Denison frames the need as constant regulatory compliance, crew management, maintenance, and financial oversight.
  - Industry Growth: Moderate/Strong — Fortune Business Insights estimates the yacht management service market at $1.25B in 2025, growing to $2.05B by 2034 at 5.7% CAGR; the broader U.S. luxury yacht market is estimated by Mordor at $4.82B in 2025, growing to $7.16B by 2030 at 8.25% CAGR. USCG reported 11,674,073 state-registered recreational vessels in 2024, and the Monaco Yacht Show market report cited 6,174 operating superyachts over 30m globally as of August 2025.
- TARGET TAM:
  - Total firms in market: Estimated 150-300 U.S. yacht-management / captain-services / yacht-care firms when combining national brokerages, regional yacht-management companies, captain-service companies, and marina-adjacent operators; Ensun and public search directories show enough named U.S. providers to warrant a real target build, but this number is not yet directory-verified.
  - Independently owned potential targets: Estimated 75-150, concentrated in South Florida, New England, Long Island/NY metro, Chesapeake, Great Lakes, Southern California, and Pacific Northwest. Thin risk: many are small owner-operator captain/service shops below platform EBITDA.
  - Already PE-backed/acquired: No obvious PE roll-up surfaced in this pass; large strategic/brokerage platforms include IYC, Denison, Moran, Fraser, and Blue Oceans. Existing large platforms may be acquirers/competitors rather than targets.
  - PE consolidation risk: Moderate-low today; strategic yacht brokerages can add management in-house, but broad PE saturation does not appear comparable to pest, fire/life safety, or insurance brokerage.
  - Named examples: top 5 with company name/location
    - Elite Yacht USA — Fort Lauderdale / South Florida, FL
    - Onboard Marine Services — South Florida, FL
    - Blue Oceans Yachting — Fort Lauderdale, FL / Antibes, France
    - Denison Yacht Sales Yacht Management — Fort Lauderdale, FL / Monaco
    - Moran Yacht & Ship — Fort Lauderdale, FL
- MARKET TAM:
  - Market size and year: Yacht management service market estimated at $1.25B in 2025 by Fortune Business Insights; broader U.S. luxury yacht market estimated at $4.82B in 2025 by Mordor Intelligence.
  - Growth rate CAGR: 5.7% CAGR for yacht management services from 2026-2034; 8.25% CAGR for U.S. luxury yacht market from 2025-2030.
  - Key demand drivers: Growth in luxury yacht ownership, rising vessel complexity, regulatory compliance, crew management, planned maintenance, owner desire for turnkey ownership, and family-office-style reporting.
- Duplicate check: Compared against active "Asset-Light Boat and Yacht Transport Coordination," active "Estate Management Companies," active "Storage & Related Services for High Value Assets," tabled "Yacht/Fleet Maintenance Software," and killed "Luxury Property Maintenance." Distinct from transport because the core service is ongoing management, not shipment; distinct from estate management because the asset and vendor ecosystem are marine-specific; distinct from yacht software because this is services, not SaaS; not a revival of luxury property maintenance because the vessel has documented compliance/crew/maintenance coordination obligations and a dedicated management-service market. Classification: proposed candidate, but flag thin platform-scale target pool until directory validation.
- Source citations / URLs used:
  - Fortune Business Insights yacht management services market: https://www.fortunebusinessinsights.com/yacht-management-service-market-116494
  - Mordor U.S. luxury yacht market: https://www.mordorintelligence.com/industry-reports/united-states-luxury-yacht-market
  - USCG 2024 recreational vessel registrations: https://www.uscgboating.org/library/accident-statistics/Recreational-Boating-Statistics-2024.pdf
  - Monaco Yacht Show / SuperYacht Times 2025 fleet report: https://www.monacoyachtshow.com/media-file/318930/mys-market-report-2025-21-9.pdf
  - IYC BLUE yacht management functions: https://iyc.com/blue/
  - Denison yacht management services: https://www.denisonyachtsales.com/europe-yacht-management/
  - Elite Yacht USA: https://eliteyachtusa.com/
  - Onboard Marine yacht management: https://www.onboardmarine247.com/yacht-management
  - Blue Oceans Yachting yacht management: https://www.blueoceansyachting.com/yacht-management
  - Moran Yacht & Ship yacht management: https://www.moranyachts.com/yacht-management/

#### Candidate 2

- Niche: MoCRA-Compliant Beauty 3PL, Kitting, and Fulfillment for Independent Cosmetics Brands
- Thesis: Beauty brands increasingly need category-specialized fulfillment that handles lot/expiration tracking, climate control, hazmat/fragrance handling, kitting, returns, and FDA/MoCRA documentation workflows. This is distinct from active fragrance testing, package testing, packaging manufacturing, and value-added fragrance distribution because the target is the logistics/fulfillment service provider that becomes embedded in the brand's daily order flow and compliance operations.
- QUICK SCREEN:
  - Margins: Moderate — general 3PL margins are often mid-teens at best, but specialized fulfillment can earn higher fees from kitting, climate control, hazmat handling, returns, account management, and compliance workflows. Treat as 10%-20% EBITDA unless target has tech-enabled productivity or premium kitting mix.
  - Recurring / Reoccurring Revenue: High — recurring storage, pick/pack, kitting, subscription-box cycles, returns, account-management fees, and ongoing brand order flow. Revenue is not contractually recurring like SaaS, but behavior is sticky once inventory, integrations, SOPs, and compliance records are embedded.
  - Industry Growth: Strong — FDA MoCRA creates new ongoing compliance requirements; FDA says responsible persons must list marketed cosmetic products and update listings annually. Grand View Research estimates the U.S. cosmetics market at $62.97B in 2023, growing at 6.1% CAGR to $95.05B by 2030; Statifacts estimates global cosmetics logistics at $18.96B in 2025, growing to $38.28B by 2035 at 7.28% CAGR; Mordor estimates the contract packaging market at $86.16B in 2026, growing to $127.28B by 2031 at 8.12% CAGR.
- TARGET TAM:
  - Total firms in market: 500+ U.S. 3PL/fulfillment/contract-packaging providers; likely 75-150 with credible cosmetics/beauty specialization, and perhaps 25-75 with MoCRA/FDA/hazmat/climate-control positioning. Independent Beauty Association says its 600+ member companies span brands, manufacturers, distributors, retailers, suppliers, and service providers, which supports a large independent beauty ecosystem but not target count directly.
  - Independently owned potential targets: Estimated 40-100 U.S. independent providers with beauty/cosmetics fulfillment or contract-packaging capability; target count needs a directory pull from Fulfill, Partner3PL, IBA, PMMI/CPA, and state-level fulfillment operators.
  - Already PE-backed/acquired: High in generic 3PL and contract packaging; examples include ShipBob, Cart.com, Ryder, Radial, DHL, UPS, and national 3PL platforms. The niche should avoid large generalists and focus on independent beauty specialists.
  - PE consolidation risk: Moderate/high — logistics and contract packaging are active consolidation markets, but beauty-specific MoCRA readiness may still produce subscale independent targets.
  - Named examples: top 5 with company name/location
    - ShipCalm — Carlsbad, CA
    - Awesome Solutions — New Jersey
    - Badger Fulfillment Group — Wisconsin
    - Phase V Fulfillment — Fort Myers, FL
    - Buske Logistics — St. Louis, MO / multi-state
- MARKET TAM:
  - Market size and year: U.S. cosmetics market $62.97B in 2023; global cosmetics logistics market $18.96B in 2025; contract packaging market $86.16B in 2026.
  - Growth rate CAGR: U.S. cosmetics 6.1% CAGR from 2024-2030; cosmetics logistics 7.28% CAGR to 2035; contract packaging 8.12% CAGR to 2031.
  - Key demand drivers: MoCRA registration/listing/adverse-event requirements, e-commerce growth, SKU proliferation, premium unboxing/kitting, subscription boxes, temperature sensitivity, hazmat/fragrance shipping rules, and retailers/brands outsourcing non-core logistics.
- Duplicate check: Compared against active "Fragrance & Cosmetic Product Testing Labs," "Luxury Package Testing & Validation Labs," "High-End Beauty & Fragrance Packaging," "Value-Added Fragrance Distribution," ideation "Compliance & packaging SaaS," and killed/tabled apparel/fashion supply-chain services. Distinct because this is neither lab testing nor package manufacturing nor SaaS; it is outsourced regulated fulfillment/kitting/logistics for cosmetics brands. It does overlap the beauty infrastructure cluster and should not be inserted as "beauty supply chain" broadly. Classification: proposed candidate if narrowed exactly to MoCRA-compliant beauty fulfillment/kitting; suppress as duplicate if tracker owner interprets it as packaging, testing, or fragrance distribution.
- Source citations / URLs used:
  - FDA MoCRA facility registration/product listing: https://www.fda.gov/cosmetics/registration-listing-cosmetic-product-facilities-and-products
  - FDA MoCRA overview: https://www.fda.gov/cosmetics/cosmetics-laws-regulations/modernization-cosmetics-regulation-act-2022-mocra
  - Independent Beauty Association advocacy/member base: https://independentbeauty.org/advocacy/
  - Grand View Research U.S. cosmetics market: https://www.grandviewresearch.com/industry-analysis/us-cosmetics-market-report
  - Statifacts cosmetics logistics market: https://www.statifacts.com/outlook/cosmetics-logistics-market
  - Mordor contract packaging market: https://www.mordorintelligence.com/industry-reports/global-contract-packaging-market-industry
  - ShipCalm beauty/cosmetics fulfillment: https://www.shipcalm.com/beauty-cosmetics-fulfillment/
  - Awesome Solutions cosmetics 3PL/MoCRA: https://awesomesolutionsnj.com/cosmetics-3pl-fda-compliance-lot-tracking/
  - Badger Fulfillment beauty/cosmetic fulfillment: https://badgerfg.com/beauty-products-cosmetic-fulfillment-services/
  - Phase V beauty fulfillment overview: https://phasev.com/blog/top-3pls-for-beauty-product-fulfillment/
  - Buske cosmetics 3PL overview: https://www.buske.com/blog/best-3pl-companies-for-cosmetics-brands

#### Candidate 3

- Niche: Jeweler's Block Insurance Brokerage for Independent Jewelry Retailers, Wholesalers, and Pawn/Jewelry Trade Businesses
- Thesis: Jeweler's block is a narrow commercial insurance wedge covering jewelry inventory, entrusted customer property, goods in transit, trade shows, theft, and related jewelry-trade risk. It is a better expression of the specialty-insurance convergence than generic insurance brokerage because it ties directly to Kay's luxury/jewelry signal, high-value movable assets, and specialty underwriting friction; however, it should be treated as a narrow insurance wedge, not a fresh broad brokerage thesis.
- QUICK SCREEN:
  - Margins: Strong — insurance distribution can support high gross margins and recurring commission revenue; prior G&B insurance research used 60%-80% gross margin and 20%-35% EBITDA margin as a specialty brokerage hypothesis. This specific wedge needs agency financial proof.
  - Recurring / Reoccurring Revenue: High — commercial insurance renews annually, inventory values change, and jeweler risk requires ongoing broker/carrier interaction. First Class Insurance cites typical annual jeweler's block premiums of $3K-$10K for small/mid stores and $20K+ for higher-value jewelers, implying recurring premium/commission behavior.
  - Industry Growth: Moderate — not enough niche-specific CAGR from primary sources. Broader jewelry insurance market estimates are positive, but the more important driver is risk necessity: IRMI defines jeweler's block as inland marine insurance for jewelry stock, and AXA XL/RPS/Jewelers Mutual position it for retailers, wholesalers, manufacturers, and property entrusted to/entrusted by the insured.
- TARGET TAM:
  - Total firms in market: Estimated 40-80 U.S. agencies/MGAs/program administrators with jeweler's block or jewelry-trade specialty capability, based on Jewelers Mutual top-agent lists, MyNewMarkets marketplace listings, carrier/program pages, and named specialist agencies. This is probably a thin target pool.
  - Independently owned potential targets: Estimated 20-40. Many named agencies are local/family-owned independent agencies, but some are already part of large brokerages or carrier-affiliated programs.
  - Already PE-backed/acquired: High in generic insurance distribution; specifically, Jewelers Mutual announced acquisition of CJB Insurance Services in 2026, and large programs exist at RPS, One80, AXA XL, and Jewelers Mutual/JM Insurance Agency Partners.
  - PE consolidation risk: High — insurance brokerage roll-ups are active; this wedge may be too small unless G&B has proprietary access to an independent specialist.
  - Named examples: top 5 with company name/location
    - Riemer Insurance Group — Hallandale Beach, FL / South Florida offices
    - Crosby & Henry Insurance — Grand Rapids, MI
    - M.L. Cutler & Co. — Florham Park / Morris County, NJ
    - First Class Insurance — Florida / nationwide jeweler's block focus
    - Jewelers Insurance Marketplace / JIMA — multi-state jeweler's block provider
- MARKET TAM:
  - Market size and year: No reliable jeweler's-block-only TAM found; broader U.S. jewelry insurance market estimate from Business Research Insights is $2.991B in 2025, but that likely includes consumer jewelry insurance and should not be used as the brokerage TAM. Practical broker TAM is commissionable premium across jewelry retailers/wholesalers/manufacturers/pawnbrokers.
  - Growth rate CAGR: Broader jewelry insurance market sources show growth, but niche CAGR remains unvalidated. Demand drivers are stronger than quantified growth at this stage.
  - Key demand drivers: theft/crime risk, high inventory values, customer entrusted property, transit/trade-show exposure, carrier specialization, appraisal/inventory documentation, and retail jewelry succession/independent retailer fragmentation.
- Duplicate check: Compared against active "Specialty Insurance Brokerage (Art & Collectibles)," "HNW Personal Lines Concierge Insurance Brokerage," "Trade Credit, Customs Bonds & Cargo Insurance Brokerage," active "Surplus Lines Compliance & Tax Filing Services," ideation "Insurance Back-Office Outsourcing & SIU Services," killed "Insurance Claims Specialist Firms," killed "Insurance Producer License Compliance," and killed "Aviation Insurance Brokerage." Distinct because the insured customer is jewelry trade businesses and the coverage is commercial inland marine / jeweler's block, not HNW household/personal collections or fine-art-only brokerage. It is semantically within specialty insurance; classification: proposed narrow candidate only if the tracker allows a child row under specialty insurance. Otherwise classify as active-specialty-insurance adjacency/watchlist, not a new row.
- Source citations / URLs used:
  - IRMI jeweler's block definition: https://www.irmi.com/term/insurance-definitions/jewelers-block-insurance
  - RPS jeweler's block insurance: https://www.rpsins.com/products-and-programs/specialty-insurance-programs/jewelers-block-insurance/
  - Jewelers Mutual business insurance / jeweler's block: https://www.jewelersmutual.com/business/business-insurance
  - Jewelers Mutual 2020 top jeweler's block agents: https://www.jewelersmutual.com/resources/business/insurance/top-jewelers-block-insurance-agents
  - Jewelers Mutual acquisition of CJB Insurance Services: https://www.jewelersmutual.com/newsroom/jewelers-mutual-group-acquires-cjb-insurance-services
  - First Class Insurance jeweler's block: https://firstclassins.com/
  - First Class Insurance premium ranges: https://firstclassins.com/what-you-need-to-know-about-insurance-for-your-jewelry-business-protect-your-jewelry-business-in-florida-with-first-class-insurance-contact-us/
  - Riemer Insurance Group: https://www.riemerinsurance.com/
  - Crosby & Henry Insurance: https://www.crosbyhenry.com/
  - M.L. Cutler & Co.: https://www.mlcutler.com/
  - JIMA jeweler's block marketplace: https://www.jewelersinsurancemarketplace.com/
  - AXA XL jeweler's block: https://axaxl.com/insurance/products/jewelers-block-insurance
  - Broader jewelry insurance market estimate: https://www.businessresearchinsights.com/market-reports/jewelry-insurance-market-119953

### Signals Classified but Not Proposed

- Beauty/fragrance/cosmetics infrastructure cluster: Partially proposed only as MoCRA-compliant beauty 3PL/kitting above. Suppressed as duplicate where it means fragrance/cosmetic product testing labs, luxury package testing, high-end packaging, or value-added fragrance distribution because those already appear in WEEKLY REVIEW.
- Specialty insurance infrastructure: Partially proposed only as jeweler's block above. Generic specialty insurance brokerage, HNW personal lines, surplus-lines compliance, and trade-risk brokerage are active/tabled/killed lifecycle-controlled rows and should not be duplicated.
- Fine-art logistics / HVA services / specialty storage: Active deal-flow / active rows. Stephen Elliott & Company and Motoreum should route through active response handling, not a new candidate.
- Fire/life safety, premium security, and fire-adjacent MRO: Active rows. Continue under existing code-mandated recurring service filter; no new identifier row.
- High-end jewelry brand / luxury-services holdco: Active proprietary deal/investment judgment issue, not a tracker niche. Do not convert the jewelry brand lead into a new industry row.
- Pest management / wildlife / mosquito franchise: Active-deal-flow but thesis-deprioritized. Work Mosquito Sheriff and Steel City Wildlife only as live responses; do not promote pest as a fresh signal.
- STR compliance data SaaS: Watchlist only. Interesting high-margin regulatory data asset, but software/data defensibility and fit risks remain unresolved; also overlaps property-management compliance themes.
- Mobile veterinary diagnostics: Watchlist/suppressed for now. Strong repeat-referral economics but key-person clinical risk and weak G&B right-to-win.
- Industrial lathe aftermarket/service: Watchlist/suppressed for now. Possible installed-base service economics, but manufacturing complexity and owner-knowledge concentration are unresolved.
- Direct mail/local advertising: Watchlist/suppressed for now. One ETA case study, weak compliance/luxury/HVA right-to-win, and unclear target quality.

→ READY

## [niche-intel-onepager] — 2026-07-21 22:55 EDT
**Niche:** MoCRA-Compliant Beauty 3PL, Kitting, and Fulfillment for Independent Cosmetics Brands  
**Status:** complete

### Deliverable

- Local PPTX: `/tmp/mocra-beauty-3pl-kitting-fulfillment-onepager.pptx`
- Drive folder ID: `1Rcp1HYFJnBo60JZDOwyxI61FJGMdxmO2`
- Drive folder link: https://drive.google.com/drive/folders/1Rcp1HYFJnBo60JZDOwyxI61FJGMdxmO2
- Uploaded PPTX ID: `1SIqAK2Fowo747wV6tBMm07o3-PtAIWgU`
- Uploaded PPTX link: https://docs.google.com/presentation/d/1SIqAK2Fowo747wV6tBMm07o3-PtAIWgU/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true

### Key Research Findings

- MoCRA creates ongoing compliance friction for cosmetics brands: facility/product listing, annual updates, adverse-event records, and traceability/documentation needs.
- The target wedge is specialized beauty fulfillment/kitting, not generic warehousing, packaging manufacturing, product testing, or fragrance distribution.
- Demand drivers include DTC/e-commerce growth, SKU proliferation, bundles/samples/subscription cycles, premium unboxing, temperature sensitivity, hazmat/fragrance handling, returns, and retailer compliance.
- Economics are likely moderate until target-specific diligence: recurring/reoccurring storage, pick/pack, kitting, returns, and account-management revenue, but general 3PL margins can be mid-teens unless compliance/kitting mix supports premium pricing.
- Competitive set splits between large generalist 3PLs/contract packagers and independent beauty-specialized providers; diligence should verify true MoCRA workflow support and independent target depth.

### Source Coverage

- Internal: identifier block and convergence context from `brain/traces/agents/2026-07-21-niche-intelligence.md`.
- Regulatory: FDA MoCRA overview; FDA cosmetic facility registration/product listing page.
- Market sizing: Grand View Research U.S. cosmetics market; Statifacts cosmetics logistics market; Mordor contract packaging market.
- Ecosystem/target examples: Independent Beauty Association, ShipCalm, Awesome Solutions, Badger Fulfillment Group, Phase V, Buske.
- The PPTX includes a second Sources slide with 12 live hyperlinks.

### Verification / Upload Notes

- Created from `brain/library/internal/one-pager-template/customs-bonds-template.pptx` using `python-pptx`; main template table, image, line, and text-box structure preserved.
- Assessment and Status both set to `Pending Scoring`; no score included.
- Text scan verified no generated one-pager text contains "Kay"; template-specific stale diligence prompt replaced with niche-specific diligence focus.
- Local PPTX readback: 2 slides, 12 source hyperlinks, file size 165,523 bytes.
- Initial Google Drive connector attempt failed because the connector was not connected (`USER_NOT_LOGGED_IN`); retried with `gog` after `source /home/ubuntu/projects/Sapling/scripts/op-env.sh`, and upload succeeded. Folder listing confirmed the PPTX is present.

→ READY

## [niche-intel-onepager] — 2026-07-21 22:58 EDT
**Niche:** Jeweler's Block Insurance Brokerage for Independent Jewelry Retailers, Wholesalers, and Pawn/Jewelry Trade Businesses  
**Status:** complete

### Deliverable

- Local PPTX: `/tmp/jewelers-block-insurance-brokerage-onepager.pptx`
- Drive folder ID: `1v89CuViXP9UYHAN646RFF-wd6TX4Miac`
- Drive folder link: https://drive.google.com/drive/folders/1v89CuViXP9UYHAN646RFF-wd6TX4Miac
- Uploaded PPTX ID: `1tQZxQ40XQvc7M2GepzyykjuK5vZnEHHT`
- Uploaded PPTX link: https://docs.google.com/presentation/d/1tQZxQ40XQvc7M2GepzyykjuK5vZnEHHT/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true

### Key Research Findings

- Jeweler's block is a narrow commercial inland marine insurance wedge for jewelry-trade inventory, customer entrusted property, goods in transit, trade shows/events, and jewelry stock held or entrusted across retailers, wholesalers, manufacturers, designers, repair/appraisal shops, and pawnbrokers.
- The best brokerage thesis is a specialty-insurance child wedge, not generic P&C distribution: value comes from carrier/program access, jewelry loss-control fluency, inventory/appraisal documentation, claims advocacy, and renewal retention.
- Demand is recurring through annual policy renewals and changing inventory values, with ongoing broker/carrier touchpoints tied to theft/crime risk, high-value movable assets, trade-show exposure, memos/consignment, and adjacent business coverage needs.
- Target-pool risk is real: identifier estimate remains 40-80 U.S. specialist agencies/MGAs/program administrators, and generic insurance distribution is already heavily consolidated.
- Strategic interest is validated by specialist carrier/program landscape and Jewelers Mutual's 2026 CJB Insurance Services acquisition, but diligence should avoid treating broad consumer jewelry-insurance TAM as the brokerage TAM.

### Source Coverage

- Internal: identifier block and convergence context from `brain/traces/agents/2026-07-21-niche-intelligence.md`.
- Definitions/coverage: IRMI jeweler's block definition; RPS jeweler's block program; Jewelers Mutual business insurance and jeweler's block pages.
- Ecosystem/target landscape: Jewelers Mutual top jeweler's block agents; JIMA marketplace; AXA XL jeweler's block; One80 jeweler's block.
- Economics/market context: First Class Insurance premium-range article; Business Research Insights broader jewelry-insurance market estimate used only as caveated context.
- Consolidation signal: Jewelers Mutual 2026 acquisition of CJB Insurance Services.
- The PPTX includes a second Sources slide with 12 live hyperlinks.

### Verification / Upload Notes

- Created from `brain/library/internal/one-pager-template/customs-bonds-template.pptx` using `python-pptx`; main template table, image, line, and text-box structure preserved.
- Assessment and Status both set to `Pending Scoring`; no score included.
- Text scan verified no generated one-pager text contains "Kay".
- Local PPTX readback: 2 slides, 12 source hyperlinks, file size 165,550 bytes.
- Google Drive folder created under WEEKLY REVIEW after `source /home/ubuntu/projects/Sapling/scripts/op-env.sh`; upload succeeded and folder listing confirmed exactly the PPTX is present. No upload errors.

→ READY

## [niche-intel-scorer] — 2026-07-21 23:05 EDT
**Source:** Identifier validation block, one-pager handoffs, `brain/context/learnings.md`, and G&B Industry Scorecard template  
**Status:** complete

Scored the three proposed niches using the G&B INDUSTRY scorecard only. I did not use the company scorecard. Each scorecard XLSX was created from `brain/library/internal/scorecard/G&B Industry & Company Scorecard Template.xlsx`, filled on `INITIAL SCREEN`, renamed `TEMPLATE` to `Industry Scorecard`, trimmed company-scorecard example sections from the industry tab, saved locally, and uploaded to the matching Drive folder. Each Drive folder now has exactly one refreshed PPTX and one XLSX scorecard.

### 1. Yacht Property Management for Private Yacht Owners in Coastal HNW Markets

- **Overall score:** `2.12/3`
- **Initial screen:** Margins PASS; recurring/reoccurring revenue PASS; industry growth PASS; Growth TAM PASS.
- **Category notes:** Growth & Catalyst `2.2` - above-GDP 5.7% yacht-management CAGR and 8.25% U.S. luxury yacht CAGR, with vessel complexity/compliance as catalyst. Size & Fragmentation `2.0` - estimated 75-150 independent potential targets, but many may be too small. Industry Economics `1.9` - asset-light coordination can work, but EBITDA is unverified and likely 12%-25%. Mission Criticality `2.3` - strong owner pain around maintenance, crew, compliance, accounting, and reporting. Exogenous Risks `1.8` - luxury-cycle, labor, key-person, and brokerage-bundling risks. Porter's Forces `2.0` - low VC/PE saturation, but strategic yacht houses and customer power matter. Value Creation `2.5` - reporting, maintenance systems, compliance calendars, procurement controls, and back office are actionable. Impact `2.0` - neutral; better maintenance/compliance is positive but end market is luxury.
- **Local scorecard:** `/tmp/yacht-property-management-scorecard.xlsx`
- **Uploaded scorecard:** `12OeFnnBLYHo3NokwGgYzGR_vLPv5QLl-` - https://docs.google.com/spreadsheets/d/12OeFnnBLYHo3NokwGgYzGR_vLPv5QLl-/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **One-pager score-update status:** Updated local PPTX Assessment to `2.12/3 - See scorecard XLSX` and Status to `Scored - Ready for tracker review`; trashed old Drive PPTX `1ksSfraVCWKxlBen-1GKoLe0VvY6_D8MA`; uploaded refreshed PPTX `1FKtFSjH4ZgaplJZKVcGFBn-9a8m9C4Gx` - https://docs.google.com/presentation/d/1FKtFSjH4ZgaplJZKVcGFBn-9a8m9C4Gx/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **Tracker-ready fields:** Score `2.12`; QSBS `Likely, subject to structure; not a financial-services exclusion`; Target Pool `75-150 estimated independent firms; many may be small captain-service shops`; Quick notes `Ongoing yacht stewardship for HNW owners; recurring service behavior and professionalization levers are attractive. Main diligence is platform-scale target depth and captain/key-person dependency.`; Red flags `Thin platform-scale target pool; labor/key-person dependency; luxury-cycle exposure; strategic brokerages can bundle management.`

### 2. MoCRA-Compliant Beauty 3PL, Kitting, and Fulfillment for Independent Cosmetics Brands

- **Overall score:** `2.13/3`
- **Initial screen:** Margins PASS; recurring/reoccurring revenue PASS; industry growth PASS; Growth TAM PASS.
- **Category notes:** Growth & Catalyst `2.5` - MoCRA plus cosmetics/logistics/contract-packaging growth creates a strong catalyst. Size & Fragmentation `2.2` - broad 3PL universe is large, with estimated 40-100 independent beauty/cosmetics fulfillment or contract-packaging targets. Industry Economics `1.7` - margins likely mid-teens unless kitting/compliance mix earns premium pricing. Mission Criticality `2.2` - sticky once inventory, integrations, SOPs, lot/expiration data, returns, and brand presentation are embedded. Exogenous Risks `1.8` - labor, warehouse execution, hazmat rules, customer concentration, and shallow MoCRA claims. Porter's Forces `1.7` - large generalists and PE-backed logistics platforms compete. Value Creation `2.4` - traceability, MoCRA documentation, kitting quality, integrations, and labor productivity are actionable. Impact `2.2` - neutral/slightly positive through traceability and compliant handling.
- **Local scorecard:** `/tmp/mocra-beauty-3pl-kitting-fulfillment-scorecard.xlsx`
- **Uploaded scorecard:** `1WFZ1xMHTw9aW7OY2uxszdL-4SgcFpAB4` - https://docs.google.com/spreadsheets/d/1WFZ1xMHTw9aW7OY2uxszdL-4SgcFpAB4/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **One-pager score-update status:** Updated local PPTX Assessment to `2.13/3 - See scorecard XLSX` and Status to `Scored - Ready for tracker review`; trashed old Drive PPTX `1SIqAK2Fowo747wV6tBMm07o3-PtAIWgU`; uploaded refreshed PPTX `1msCpE52gq3Tk2kWVG-6oVdhCQSh-pPnO` - https://docs.google.com/presentation/d/1msCpE52gq3Tk2kWVG-6oVdhCQSh-pPnO/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **Tracker-ready fields:** Score `2.13`; QSBS `Likely, subject to structure; avoid distribution-only inventory-heavy models`; Target Pool `40-100 estimated independent targets; 25-75 with credible MoCRA/FDA/hazmat/climate-control positioning`; Quick notes `Strong regulatory and beauty-infrastructure signal; target must be specialized fulfillment/kitting with real lot/traceability workflows, not generic 3PL or packaging/testing duplicate.`; Red flags `Generic 3PL margin compression; PE-backed logistics competition; MoCRA marketing claims may be shallow; overlap with existing beauty testing/packaging/distribution rows.`

### 3. Jeweler's Block Insurance Brokerage for Independent Jewelry Retailers, Wholesalers, and Pawn/Jewelry Trade Businesses

- **Overall score:** `1.93/3`
- **Initial screen:** Margins PASS; recurring/reoccurring revenue PASS; industry growth PASS WITH CAVEAT; Growth TAM PASS WITH CAVEAT.
- **Category notes:** Growth & Catalyst `1.8` - risk-driven renewal demand is real, but jeweler-block-only growth remains unvalidated. Size & Fragmentation `1.5` - likely only 20-40 independent specialist targets, so this is a thin child wedge. Industry Economics `2.6` - specialty brokerage can have strong gross margin, EBITDA, and renewal commission economics. Mission Criticality `2.6` - coverage protects inventory, entrusted property, transit, shows, and theft/loss exposure. Exogenous Risks `1.6` - consolidation, carrier appetite, severe-loss exposure, QSBS/valuation issues, and weak niche TAM data. Porter's Forces `1.4` - roll-ups, carriers/program administrators, and large broker platforms have power. Value Creation `2.1` - renewal workflow, placement discipline, risk-control documentation, cross-sell, claims advocacy, and producer transition are available but known. Impact `2.0` - neutral/slightly positive for protecting independent jewelry businesses and customer property.
- **Local scorecard:** `/tmp/jewelers-block-insurance-brokerage-scorecard.xlsx`
- **Uploaded scorecard:** `19WK6m-g9BmN2PiRFdp-XYb2qFUJcx7rG` - https://docs.google.com/spreadsheets/d/19WK6m-g9BmN2PiRFdp-XYb2qFUJcx7rG/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **One-pager score-update status:** Updated local PPTX Assessment to `1.93/3 - See scorecard XLSX` and Status to `Scored - Ready for tracker review`; trashed old Drive PPTX `1tQZxQ40XQvc7M2GepzyykjuK5vZnEHHT`; uploaded refreshed PPTX `18UhRulGaWoq1vs-3f-lEporgQvTdtMt-` - https://docs.google.com/presentation/d/18UhRulGaWoq1vs-3f-lEporgQvTdtMt-/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **Tracker-ready fields:** Score `1.93`; QSBS `Unlikely / major caveat; insurance brokerage and financial-services exclusions need counsel review`; Target Pool `20-40 estimated independent specialist targets; thin child wedge`; Quick notes `Excellent recurring insurance economics and mission criticality, but target pool is thin and generic brokerage is heavily consolidated. Treat as specialty-insurance child wedge/watchlist unless proprietary access appears.`; Red flags `QSBS likely problematic; high PE/strategic consolidation; thin target pool; niche-only TAM/growth unvalidated; carrier/program power.`

### Verification

- Used `source /home/ubuntu/projects/Sapling/scripts/op-env.sh` before every `gog` Drive call.
- Live Drive folder checks confirmed each folder contains exactly one refreshed PPTX and one XLSX scorecard.
- Local workbook readback confirmed each scorecard has tabs `INITIAL SCREEN` and `Industry Scorecard`.
- Local PPTX readback confirmed first-slide Assessment/Status rows were updated from `Pending Scoring` to scored status.
- No email sending or drafting performed.

→ READY

## [23:13] orchestrator
All required Tuesday headless steps completed: gather, synthesize, identify, one-pagers, industry scoring, tracker update, markdown report, and JSON sidecar. Wrapper validator passed for 2026-07-21.
→ CLOSE

## [niche-intel-tracker] — 2026-07-21 23:12 EDT
**Source:** Live `WEEKLY REVIEW` tab in Industry Research Tracker via `source /home/ubuntu/projects/Sapling/scripts/op-env.sh && gog sheets`
**Status:** complete

### Tracker Update Summary

- Re-fetched live `WEEKLY REVIEW` state immediately before writing and saved rollback snapshot to `/tmp/niche-weekly-review-pre-tracker-2026-07-21.json`.
- Header row resolved at sheet row 3. Headers used: `Rank`, `Niche Hypothesis`, `Current Status`, `Current Outreach Channel`, `Score`, `QSBS`, `Target Pool`, `Quick notes`, `DealsX Niche`, `Start Date`, `Days in Review`.
- `Current Outreach Channel` was present instead of `Outreach Channel`, so it was left blank for all appended rows.
- `Red flags noted` was absent, so red flags were folded into `Quick notes`.
- Appended rows directly to `WEEKLY REVIEW` using `gog sheets append --values-json` with validation copied from `'WEEKLY REVIEW'!A4:K4`.

### Rows Appended

- Sheet row 41 / Rank 38: `Yacht Property Management for Private Yacht Owners in Coastal HNW Markets`
- Sheet row 42 / Rank 39: `MoCRA-Compliant Beauty 3PL, Kitting, and Fulfillment for Independent Cosmetics Brands`
- Sheet row 43 / Rank 40: `Jeweler's Block Insurance Brokerage for Independent Jewelry Retailers, Wholesalers, and Pawn/Jewelry Trade Businesses`

### Verification

- Re-read `WEEKLY REVIEW` after append.
- Confirmed each appended niche appears exactly once.
- All three appended rows have `Current Status` = `New`.
- No email sending or drafting performed.

→ READY
