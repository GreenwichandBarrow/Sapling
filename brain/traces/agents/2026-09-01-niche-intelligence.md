---
schema_version: 1.1.0
date: 2026-09-01
type: trace
today: "[[notes/daily/2026-09-01]]"
task: Headless Monday full niche-intelligence run
had_human_override: false
tags: [date/2026-09-01, trace, status/in-progress, topic/niche-intelligence, source/codex-systemd]
---

## Context

Codex/systemd headless Monday full run for [[outputs/2026-09-01-niche-intelligence-report|2026-09-01 Niche Intelligence Report]].

## Decisions

### Headless Run Mode
**AI proposed:** Execute the scheduled five-step niche-intelligence pipeline without human approval gates.
**Chosen:** Run the mandated headless sequence and write validator-readable artifacts.
**Reasoning:** Scheduled runner has no human in the loop; validation depends on concrete markdown and JSON sidecar outputs.
**Pattern:** #scheduled-skill-hardening

## Agent Posts

### Orchestrator Start
- Timestamp: 2026-09-01
- Runtime: Codex/systemd
- Status: chatroom created before Step 1 gather

## [13:12] niche-intel-historical
**Source:** historical calls/email/OneNote/ChatGPT
**Status:** partial

### Signals Found

Source coverage diagnostics:
- `hist-calls`: covered `brain/calls/*.md` with 192 total call files and 181 files older than the 14-day cutoff (`2026-08-18`). Direct Granola API wrapper is installed, but `granola-api since 2025-01-01T00:00:00Z` returned only 10 recent note metadata records from `2026-08-18` onward, so older Granola content is covered through vault-synced call notes, not direct raw API retrieval.
- `hist-email`: completed all five required Gmail searches with `--gmail-no-send`: acquisition/deal max 50, teaser/CIM/opportunity max 30, insurance/compliance/regulatory max 30, conference/association/summit max 20, Axial/DealStream/BizBuySell max 20. Read selected relevant threads only, including Jeremy Black insurance ideas, air purification, geotech/CMT, HOA/community association management, safety/PPE distribution, healthcare regulatory compliance SaaS, CorpNet compliance filings, hyperbaric oxygen therapy, security solutions, niche trade publication, legal marketing, and Axial GPO. Axial GPO body had `No Text Available`, so only metadata is usable.
- `hist-onenote`: no OneNote MCP/resource is available in this session. MCP discovery exposed bundled app/plugin resources only; no SEARCH FUND notebook surface was callable. This is an evidence gap.
- `hist-chatgpt`: `~/Downloads` does not exist and `find /home/ubuntu -name selected_business_conversations.json` returned zero files. This is an evidence gap.
- Tracker exclusion checked live against `WEEKLY REVIEW`, `KILLED`, `TABLED`, and `IDEATION`. Most historical signals are already-tracked, killed, or tabled.

Organized by niche:

- **Specialty/HNW/art insurance brokerage cluster** - strong historical signal, already tracked. Calls from August Felker, Hunter Hartwell, Chris Wise, Amanda Lo Iacono, and insurance deal-history repeatedly validate wealth-transfer demand, sticky recurring personal-lines revenue, art/jewelry underinsurance, and independent-service white space. Lifecycle status: already represented by active rows for Specialty Insurance Brokerage (Art & Collectibles), HNW Personal Lines Concierge Insurance Brokerage, Jeweler's Block Insurance Brokerage, and related specialty insurance rows. New data does not justify a duplicate row; it reinforces warm-network/channel priority.
- **Trade credit / customs bonds / cargo insurance brokerage** - strong historical signal, already tracked. Jeremy Black email thread gives named firsthand customer evidence: Trade Risk Group, Trade Acceptance Group, Meridian/Texel, Allianz Trade/Euler Hermes, Atradius, Coface; he called customs/cargo insurance very recurring and trade credit under-utilized in the U.S. Prior research brief adds 20-50 U.S. specialist independent TCI brokers, 85-95% renewal, 20-35% EBITDA, and low U.S. penetration. Lifecycle status: already in `WEEKLY REVIEW` as Trade Credit, Customs Bonds & Cargo Insurance Brokerage; do not resurface as net-new.
- **FMO/IMO insurance distribution aggregator** - moderate historical signal, already tracked. Jeremy Black surfaced a prior insurance marketing organization that assembled broker/agent groups for annuity and life policy distribution. Lifecycle status: already in `WEEKLY REVIEW` as Insurance FMO/IMO Distribution-Aggregator; signal remains thin but directionally supports the existing row.
- **Art transaction KYC / escrow / back-office services** - two-source operator pain signal, but rejected/protected. Chris Wise and Amanda Lo Iacono independently surfaced KYC, wire, reporting, escrow, and secondary-art transaction workflow gaps. Prior lifecycle analysis rejected the niche as a standalone acquisition lane because the same thin-market/willingness-to-pay problem that killed Fine Art Escrow Software applies to the services frame. Treat Amanda/Chris as river-guide assets for art/insurance rows, not as a live niche.
- **Luxury amenity management / premium physical security / luxury retail vendor ecosystem** - strong call signal, already tracked. Mike Horowitz's call specifically surfaced amenity management, premium security for luxury retail, signage/logo installs, quick millwork/repair, seasonal display, and private-tenant club operations; E&K later provided security-solutions deal evidence with 450 systems under service contracts. Lifecycle status: amenity management and premium physical security are already in `WEEKLY REVIEW`; sign/lighting was later killed; visual merchandising is low priority/project-heavy.
- **Marine/yacht services** - recurring historical signal, already tracked. Mike Horowitz flagged Kay's genuine right-to-win through family marine logistics and yacht-club background, with yacht/marina software, boat shrink wrapping, boat transport, and marine services as sublanes. Lifecycle status: yacht transport and yacht property management are already tracked; yacht/fleet maintenance software is tabled. No net-new.
- **Beauty/fragrance/packaging compliance infrastructure** - strong convergence from calls and tracker history, already tracked. Jeff Stevens and Clayton Sachs both pointed away from crowded pest and toward fragrance testing, packaging, specialty chemical distribution, and collectibles insurance as more credible adjacent lanes. Lifecycle status: already covered by Fragrance & Cosmetic Product Testing Labs, Luxury Package Testing & Validation Labs, MoCRA Beauty 3PL/Kitting/Fulfillment, High-End Beauty & Fragrance Packaging, and Value-Added Fragrance Distribution.
- **Property/facilities compliance and real-estate services** - strong historical/tracker signal, already tracked. Existing rows cover Building Energy & Emissions Compliance, HOA/Community Association Management, Property Management, Reserve Study/Building Engineering, Stormwater O&M, Submetering, Permit Expediting, Lease Administration, Facilities Management, and Luxury Amenity Management. Gmail read of E&K HOA deal validates saleability at ~$750K revenue with dues/fees collection, maintenance coordination, vendor management, and reporting. Lifecycle: most sublanes are already in `WEEKLY REVIEW`; sign/lighting, fire-protection MRO, vegetation management were killed; high-end commercial cleaning is tabled.
- **Technical MRO / equipment service / controls** - strong pattern, mostly already tracked. Jeff Stevens pushed concentric-circle adjacencies around MRO/service-heavy models; Mike Horowitz framed mission-critical equipment repair as attractive when downtime is costly. Gmail validated specific saleability data: Air Purification Systems Company at $8M revenue / ~$2.5M EBITDA, Geotechnical Engineering Services at >$3.6M revenue / ~$1M EBITDA, Industrial & Safety Equipment Distribution at $2M revenue / ~$650K profit. Lifecycle status: air purification, geotech/CMT, SCADA/controls, and facilities rows already exist; industrial safety/PPE distribution is a watchlist signal but not a clean new niche because product distribution/inventory risk and weak Kay fit are unresolved.
- **Pest and pest-adjacent commercial property services** - historically strongest volume signal but lifecycle constrained. 71 older call files matched pest/commercial property terms. Calls with Jeff, Clayton, Andrew Freiman, Albert Kim, NoFo, Camilla, and others show active pressure-testing plus market crowding. Lifecycle status: Premium Pest Management is tabled, not live; do not re-present as active. Pest-adjacent lessons should inform property/facilities/MRO screens.
- **Healthcare/wellness services and software** - mostly dead/protected; one watchlist signal. Historical women's-health/fertility/health-tech lanes remain killed or weak because targets are early-stage/software/healthcare-heavy. Gmail HBOT deal shows a medical-grade hyperbaric oxygen therapy company with insurance contracts: $754,850 revenue, $369,451 profit, 3.2x ask, 20% of patient volume producing >70% of revenue, and recurring multi-session protocols. This is actionable deal evidence but off-core as a broad niche unless Kay wants healthcare/wellness. Healthcare regulatory compliance SaaS deal at $700K recurring revenue and 1,500 facilities reinforces software/compliance history but remains software-caution.
- **Legal marketing / lead generation, trade publishing, generic managed IT/cyber, self-storage, solar/plumbing/HVAC/landscaping** - deal-flow evidence only, not recommended. These appeared in historical email search results and selected reads. Legal marketing was $65M revenue / $5M EBITDA but is marketing/lead-gen exposure; niche trade publication was $1M revenue / $300K EBITDA but ad/media and AI disruption risk are material; managed IT/cyber is crowded and already tabled/ideation; broad trades are off-thesis unless a proprietary target appears.

### Industries/Companies Mentioned

- Specialty/HNW/art insurance: August Felker, Hunter Hartwell, Jonathan Crystal, Chris Wise, Amanda Lo Iacono; targets/refs include PRMS, J.W. Allen, Genser, Grober Imbey, Hamptons Risk, DRO, Huntington Block/Aon, Chubb, BofA art services. Status: already tracked; warm-network priority.
- Trade-risk brokerage: Jeremy Black, Trade Risk Group, Trade Acceptance Group, Meridian/Texel, Allianz Trade/Euler Hermes, Atradius, Coface, Great American, QBE, Chubb, Zurich. Status: already tracked.
- FMO/IMO: Jeremy Black/Jolene historical operator reference; annuity/life broker-agent aggregation. Status: already tracked, thin target proof.
- Art transaction back office: Amanda Lo Iacono, Chris Wise; KYC, escrow, wire transfers, reporting, independent advisors/galleries/family offices. Status: rejected as standalone; use as river-guide intelligence.
- Luxury amenity/security/vendor ecosystem: Mike Horowitz; Arch Amenity Group, American Christmas, premium security providers, signage/millwork/seasonal display vendors. E&K security-solutions deal had $7.1M revenue / $1.5M EBITDA and 450 service-contract systems, but Hong Kong/Macau geography is out-of-box. Status: already tracked/protected.
- Marine/yacht: Mike Horowitz; boat shrink wrapping/covering, boat transport, marina/private club software, yacht property management. Status: already tracked or tabled.
- Beauty/fragrance/packaging: Clayton Sachs, Jeff Stevens; fragrance testing, packaging, specialty chemical distribution, MoCRA-compliant beauty 3PL/kitting/fulfillment. Status: already tracked.
- Property/facilities: E&K Residential & Commercial Association Management Company, CorpNet compliance, Building Energy/LL97, HOA/CAI, Reserve Advisors, Milrose, RE BackOffice, stormwater platforms. Status: mostly tracked; killed/tabled guardrails apply.
- Technical MRO/equipment: E&K Air Purification Systems Company, E&K Geotechnical Engineering Services Company, E&K Industrial & Safety Equipment Distribution Company, SCADA/controls, specialty steel/machinery, air filtration. Status: already tracked except safety/PPE distribution watchlist.
- Healthcare/wellness: Business Exits hyperbaric oxygen therapy listing, E&K healthcare regulatory compliance SaaS/ECA automation. Status: off-core/watchlist, not net-new.
- Other brokered deal-flow: legal marketing lead-gen, drilling trade publication, managed IT/VAR, medical animation/digital media, self-storage, landscaping/construction, HVAC, plumbing, solar/electrical, plastic manufacturing, home decor/textiles. Status: no clean historical niche signal for G&B.

### Data Points for Scoring

- HNW personal lines insurance: August Felker call states HNW personal lines are very sticky, near-100% recurring, and valuable; target archetype is two women near retirement, HNW personal lines only, not PE-seeking. Hunter Hartwell adds 12x-14x EBITDA whole-brokerage multiple wall and carve-out workaround. Sources: `brain/calls/2025-11-19-august-felker-insurance-dd-2.md`, `brain/calls/2026-01-12-hunter-kay-insurance.md`.
- Trade credit insurance: global premiums ~$13B in 2025, projected $31B-$38B by 2033-2035; U.S. penetration 2%-5% vs Europe 10%-15%; 20-50 U.S. specialist independent brokers; 85%-95% renewal; 20%-35% EBITDA. Sources: Jeremy Black Gmail thread `19c250d5143e6b7a`, `brain/outputs/2026-03-15-trade-credit-insurance-niche-research.md`.
- Art transaction/KYC/escrow: two independent call sources confirm pain, but prior identifier found acquirable art-specific provider count <5 and TAM around $15M-$30M for the art-specific segment. Sources: `brain/calls/2026-01-22-call-with-chris-wise.md`, `brain/calls/2026-01-29-amanda-i-kay.md`, `brain/outputs/2026-05-26-niche-intelligence-report.md`.
- Amenity management: Mike Horowitz cited Arch Amenity Group and 20,000+ sq ft luxury condo amenity packages; post-COVID commercial landlords add amenities for tenant retention. Current tracker score 2.28, target pool 30-100. Source: `brain/calls/2026-06-22-michael-horowitz.md`, live `WEEKLY REVIEW`.
- Premium security: E&K security-solutions listing: $7.1M revenue, $1.5M normalized EBITDA, 450 systems under service contracts, ISO 9001, 24/7 support. Current tracker row is premium physical security integration/lifecycle maintenance at 2.31 with 50-150 luxury/Class-A specialists inside 700-1,000+ independent integrators. Sources: Gmail thread `19f3964e4b574386`, live `WEEKLY REVIEW`.
- Air purification: E&K listing: $8M revenue, ~$2.5M normalized EBITDA; designs, supplies, installs, and services air filtration/air-quality systems for municipalities, fire departments, schools, labs, manufacturers, pharma/process facilities, vehicle-service operations, and research labs. Current tracker score 2.44, target pool 100-300. Source: Gmail thread `19ff7628e003cc90`, `brain/outputs/2026-08-24-niche-intelligence-report.md`.
- Geotech/CMT: E&K listing: >$3.6M revenue, ~$1M normalized EBITDA; geotechnical investigations plus CMT inspections across NJ/PA/DE. Current tracker score 2.31, market TAM proxies $9.05B U.S. geotech in 2025 and $2.01B U.S. material testing in 2025. Sources: Gmail thread `19f00b55a11762b4`, `brain/outputs/2026-06-30-niche-intelligence-report.md`.
- HOA/community association management: E&K listing validates saleability at ~$750K annual revenue with dues/fees collection, maintenance coordination, vendor management, and on-demand reporting. Current tracker score 2.45, target pool 100+ LI/NYC small firms, 365K U.S. associations, $54B market growing toward $73B by 2030. Sources: Gmail thread `19e98e44c9c20e66`, live `WEEKLY REVIEW`.
- Stormwater O&M: current tracker score 2.52; estimated 100-250 independent stormwater O&M/SCM providers; market estimates $6.98B-$8.25B U.S. stormwater management in 2025 and 6.7%-8.72% growth proxies. Source: `brain/outputs/2026-08-10-niche-intelligence-report.md`.
- Healthcare HBOT: $754,850 revenue, $369,451 profit, 3.2x ask; 20% insurance patients generate >70% revenue; multi-session protocols; major insurer/Medicare contracts. Source: Gmail thread `19ecc7e7deb7b3c9`. Classification: watchlist/off-core, not promoted.

Historical verdict: **no clean net-new historical niche** should be advanced from this pass. The strongest evidence reinforces already-tracked rows and should feed synthesis/scoring priority rather than create duplicates. Only two watchlist fragments are not already represented: industrial/PPE injury-prevention distribution and medical-grade HBOT with insurance contracts; both need stronger G&B fit and target-density proof before one-pager consideration.

→ READY

## [13:14] niche-intel-recent
**Source:** last-14-days mixed sources
**Status:** partial

### Signals Found

Source coverage diagnostics:
- Time window enforced as `2026-08-18` through `2026-09-01`.
- `last30days`: script available at `/home/ubuntu/.codex/skills/last30days/skills/last30days/scripts/last30days.py`; ran the three required queries with `--days 14 --quick` and saved raw outputs under `/tmp/niche-last30days/`. Coverage degraded: Reddit public fetch returned 403, X/YouTube were unavailable in this environment, TikTok/Instagram required ScrapeCreators keys, Polymarket had no useful hits, and Hacker News returned irrelevant/zero-score items. Treat as no useful social signal, not silence in the market.
- Web/news search: usable current acquisition/trend coverage found. Relevant links: Axios on Aon/USI (`https://www.axios.com/2026/08/31/aon-17-billion-usi-kkr`), SI Global business-services PE report (`https://www.siglobal.com/insights/private-equity-business-services-2026-report`), ITPro on Basware/Trustpair (`https://www.itpro.com/business/acquisition/basware-to-acquire-trustpair-to-strengthen-payment-fraud-prevention`), Accel-KKR/Trustpair (`https://www.accel-kkr.com/basware-signs-agreement-to-acquire-trustpair/`), Channel Dive on MSP consolidation (`https://www.channeldive.com/news/channel-acquistions-consolidation-managed-services-omdia/828297/`), Auxo MSP guide (`https://auxocapitaladvisors.com/private-equity-msps/`), and SLB/Kelvion data-center cooling coverage (`https://www.barrons.com/articles/slb-ai-strategy-4-billion-data-center-deal-b6b99c63`).
- Newsletters via Gmail: all mandated read-only searches were run with `--gmail-no-send` after sourcing `scripts/op-env.sh`. Search syntax had changed from `--query` to positional query; reran successfully. Covered `auto/subscriptions & education` newer_than:7d, `auto/industry research` newer_than:14d, `auto/deal flow` newer_than:14d, and `auto/investors` newer_than:14d. Read relevant threads only: E&K fragrance/beauty buyer search, E&K managed cybersecurity, E&K electrical testing/power systems, E&K plumbing contractor, Acquiring Minds signage acquisition, SMB Deal Hunter property/warehousing/software/pool/landfill bundle, SMB Deal Hunter chauffeur/car wash/oil-change bundle, and Rejigg humane wildlife removal.
- Granola: `granola-api since 2026-08-18T00:00:00-04:00` failed as invalid date; UTC retry `2026-08-18T00:00:00Z` succeeded. Ten notes were available, all from `2026-08-18` onward. Retrieved relevant notes for WSN Group, Jeff, Camilla, and Brooke; they reinforce current Sydney Garber/luxury-jewelry deal diligence and investor framing, not net-new niche discovery.
- Vault research: scanned recent `brain/outputs/` and `brain/calls/` files dated within the window. Key files: `brain/outputs/2026-08-21-thesis-signal-scan.md`, `brain/outputs/2026-08-24-niche-intelligence-report.md`, `brain/outputs/2026-08-28-thesis-signal-scan.md`, and recent calls from 2026-08-18 through 2026-08-31.
- Passive signals: `brain/inbox/` since last Tuesday contained `brain/inbox/2026-08-28-july-management-report-budget-trigger.md`; no `topic/niche-signal` match. No passive niche-signal inbox items found.

By source:

- Web/news: Large current insurance brokerage consolidation is active but already covered by existing specialty/HNW/art/jewelry insurance rows. Aon announced a ~$17B USI acquisition from KKR on 2026-08-31; KKR reportedly achieved a large strategic-holdings outcome. This confirms insurance-distribution PE heat, not a new row.
- Web/news: Business-services PE is selective rather than broadly hot. SI Global reports business-services PE deal volumes down 29% YoY, first-time platform investments down 48%, refinancing up 125%, exits improved, and longer hold periods. Evidence suggests buyers still like resilient recurring service models but new-platform bar is higher.
- Web/news: Supplier payment fraud / vendor bank-account validation is a current, AI-driven risk lane. Basware signed to acquire Trustpair in late August for invoice-to-payment assurance, supplier-bank validation, and impersonation/payment-instruction fraud prevention. This is software-heavy, but it points to a possible managed vendor-master/payment-controls services niche if target density exists.
- Web/news: Managed services consolidation remains active. Channel Dive/Omdia reported MSP acquisitions up 73% YoY in Q1 2026, with private equity and cybersecurity as drivers. Auxo's MSP market commentary reinforces recurring revenue, retention, fragmentation, and cybersecurity/compliance as buyer-interest factors.
- Web/news: Data-center cooling and power infrastructure demand remains a strategic tailwind. SLB/Kelvion coverage is larger industrial equipment, not SMB services, but supports broader power/electrical testing and thermal-management demand.
- Gmail deal flow: E&K managed cybersecurity services/company in NJ: ~$2M revenue, ~$350K normalized EBITDA, annual recurring revenue, monthly payments, managed SOC, email security/compliance platform, hundreds of customers. Existing overlap with CMMC/FAR Managed Compliance and managed compliance-adjacent MSP; useful reinforcement, not clean net-new.
- Gmail deal flow: E&K electrical testing and power-system services in Mid-Atlantic: $6.1M revenue, $3.5M normalized EBITDA, recurring planned maintenance plus 24/7 emergency support. Services include diagnostics, repairs, upgrades, thermographic inspections, dielectric fluid analysis, relay calibration, arc-flash studies, power-quality monitoring, protection upgrades, and commissioning. This is the strongest potential net-new recent niche.
- Gmail deal flow: E&K residential/commercial plumbing contractor in NY: $3M revenue, >$500K normalized EBITDA, licensed plumbing services for residential/commercial/institutional/healthcare/government work. Evidence of availability, but broad trades are crowded and not G&B-differentiated unless reframed around institutional/compliance maintenance.
- Gmail deal flow: Rejigg humane wildlife removal specialists in Columbia Metro Area, SC: $1.29M revenue, $335K EBITDA / $454K SDE signal, 24/7 emergency response, removal, exclusion, remediation, residential/commercial, recurring prevention contracts, limited direct competition. Potential new pest-adjacent niche; needs target density and premium/commercial angle before promotion.
- Gmail deal flow: SMB Deal Hunter property-management/warehousing/pool/landfill bundle: absentee-run military-family property management at $2.9M ask / $692K EBITDA / $2.55M revenue / ~550 homes; food-grade warehousing and fulfillment at $2.1M ask / $595K EBITDA / $3.23M revenue / SQF certification; pool cleaning with monthly billing and ~$814K EBITDA; landfill-gas equipment maker with compliance-driven demand and ~$400K EBITDA. These are deal-level signals; property management is already tracked and food-grade warehousing/landfill gas are watchlist only.
- Gmail deal flow: SMB Deal Hunter chauffeur/car wash/oil-change bundle confirmed current lower-middle-market activity in luxury chauffeur, car wash, oil-change, and a sponsor's commercial HVAC/plumbing/electrical roll-up with 3 initial acquisitions and 28 more in pipeline. Signal supports crowding/PE heat in broad trades and automotive services more than a G&B-specific niche.
- Gmail newsletters: Acquiring Minds Windsor Fireform case: 40-year Seattle-area durable sign/public-art fabrication business; 16 employees, 100-150 projects/year, mid-single-digit millions revenue, ~55% gross margin, historical EBITDA margin ~25-33%, 30% equity / 60% SBA / 10% seller note. Operator digitized records, rebuilt pricing model, and expanded quote pipeline. Interesting durable civic/architectural fabrication signal, but project-based/manufacturing-heavy and low recurring revenue.
- Vault/calls/Granola: Recent calls are dominated by the live Sydney Garber luxury-jewelry acquisition. Evidence reinforces current deal risks and possible second-order bolt-ons: jeweler's block insurance, art storage, repair/aftercare, legacy brand operational systems, inventory finance/controls, manufacturing QA, retail relationship transition. Do not recycle as net-new; use as thesis evidence for existing luxury/luxury-infrastructure rows.
- Vault outputs: `2026-08-28-thesis-signal-scan.md` independently queued managed cybersecurity/compliance-adjacent MSPs for this Monday. `2026-08-24-niche-intelligence-report.md` already advanced air-purification service and held art-dealer cultural-goods compliance; both are existing/tracked after last week's run.

### Industries/Companies Mentioned

- **Electrical Testing and Power-System Services** - potential new. Evidence: E&K Mid-Atlantic listing with $6.1M revenue / $3.5M normalized EBITDA, recurring planned maintenance, 24/7 emergency support, arc-flash/power-quality/relay-calibration/testing scope. Adjacent to infrastructure compliance and data-center/power demand; not on active exclusion list.
- **Managed Cybersecurity / Compliance MSP** - existing/adjacent. Evidence: E&K NJ listing; web MSP consolidation. Overlaps with CMMC/FAR Managed Compliance and managed compliance/service-provider screens.
- **Supplier Payment Fraud Validation / Vendor Master Controls** - potential new, service-model unproven. Evidence: Basware/Trustpair acquisition around supplier bank-account validation and invoice-to-payment assurance. Needs target-density proof outside software.
- **Humane Wildlife Removal / Exclusion / Remediation** - potential new pest-adjacent. Evidence: Rejigg listing with recurring prevention contracts, 24/7 response, limited direct competition. Needs commercial/premium focus and independence from generic pest.
- **Food-Grade Warehousing and SQF Fulfillment** - potential new/watchlist. Evidence: SMB Deal Hunter listing with $3.23M revenue / $595K EBITDA / SQF certification / recurring food-retail-industrial clients. May overlap with MoCRA Beauty 3PL/Kitting/Fulfillment; not enough G&B fit yet.
- **Durable Civic / Architectural Signage and Public-Art Fabrication** - potential new/watchlist but weak fit. Evidence: Windsor Fireform acquisition; attractive margins and operational improvement, but project-based revenue and manufacturing/WIP complexity.
- **Residential/Commercial/Institutional Plumbing** - broad-trades existing-market signal, not new. Evidence: E&K NY listing and SMB roll-up note; high PE crowding and weak differentiation.
- **Luxury Chauffeur / Black Car** - watchlist/park. Evidence: SMB Deal Hunter bundle; prior thesis scan already parked this as operations-heavy with dispatch/fleet/partner coordination complexity.
- **Car Wash / Oil Change / Pool Cleaning / Landfill Gas Equipment** - watchlist only. Evidence from SMB Deal Hunter; monthly recurring pool billing and compliance-driven landfill-gas demand are notable, but current data is isolated.
- **Specialty/HNW/Jewelry Insurance, Art Storage, Jewelry Repair/Aftercare, Luxury Brand Operational Stack** - existing/strategic adjacency. Evidence from current Sydney Garber calls/Granola; use for deal thesis, not new niche creation.
- **Aon, USI, KKR** - current insurance brokerage consolidation comps; existing insurance thesis support.
- **Basware, Trustpair, Accel-KKR** - supplier/payment fraud validation acquisition comp; potential new services question.
- **SLB, Kelvion** - large industrial data-center cooling comp; tailwind only, not direct SMB target.
- **Windsor Fireform** - acquired durable signage/public-art fabrication example; watchlist.

### Data Points for Scoring

- Electrical testing/power systems: $6.1M revenue; $3.5M normalized EBITDA; planned maintenance plus 24/7 emergency support; services include thermographic inspections, dielectric fluid analysis, component testing, relay calibration, arc-flash studies, power-quality monitoring, system protection upgrades, and commissioning. Source: Gmail thread `1a048fefa5e1152d`.
- Humane wildlife removal: $1.29M revenue; $335K EBITDA / $454K SDE signal; 35% margin on SDE; 24/7 response; recurring prevention contracts; residential and commercial markets; limited direct competition. Source: Gmail thread `1a0451fd6283428f`.
- Managed cybersecurity: ~$2M revenue; ~$350K normalized EBITDA; annual recurring revenue with monthly payments; managed SOC; proprietary email security/compliance platform; hundreds of SMB-to-enterprise customers. Source: Gmail thread `1a04014c8203457c`.
- Plumbing contractor: $3M revenue; >$500K normalized EBITDA; residential, commercial, institutional, healthcare, city/state/federal customers; real estate optional. Source: Gmail thread `1a05980da14f76f3`.
- Food-grade warehousing/fulfillment: $3.23M revenue; $595K EBITDA; $2.1M asking price; two buildings; SQF certification; repeat/reorder customers across food, retail, and industrial. Source: Gmail thread `1a03ac45213e5271`.
- Military-family property management: $2.55M revenue; $692K EBITDA; $2.9M asking price; ~550 single-family homes across West Texas/New Mexico; revenue from management fees, in-house maintenance, lease/renewal fees, resident benefits package. Existing Property Management row, not new. Source: Gmail thread `1a03ac45213e5271`.
- Windsor Fireform / durable signage: 16 employees; 100-150 projects/year; mid-single-digit-millions revenue; ~55% gross margins; historical EBITDA margins ~25-33%; ~40% deposits; financing 30% equity / 60% SBA / 10% seller note; quote value reached $9.5M by June 30 after operating improvements. Source: Gmail thread `1a043defb55fcdc4`.
- Insurance brokerage consolidation: Aon/USI at ~$17B announced 2026-08-31; USI cited at ~$3B revenue, 10,500 employees, ~200 offices. Source: Axios link above. Classification: existing insurance thesis support.
- Business-services PE backdrop: deal volume -29% YoY, first-time platform investments -48%, refinancing +125%, exits improved, assets held >5 years at 26%. Source: SI Global link above. Classification: macro scoring guardrail: high-quality recurring service models still matter, but platform selectivity is elevated.
- MSP consolidation: Omdia/Channel Dive reports MSP acquisitions up 73% YoY in Q1 2026; PE/cybersecurity are main drivers. Source: Channel Dive link above. Classification: heat/crowding evidence for managed cyber/compliance MSP.
- Supplier-payment fraud: Basware/Trustpair acquisition validates current demand for supplier bank-account validation, invoice-to-payment assurance, impersonation fraud prevention, and shared supplier intelligence. Sources: ITPro, Accel-KKR, PRNewswire links above. Classification: potential new niche only if service/operator targets exist.

Recent-intelligence verdict: advance **Electrical Testing and Power-System Services** as the strongest potential net-new candidate for synthesis. Keep **Supplier Payment Fraud / Vendor Master Controls** and **Humane Wildlife Removal / Exclusion** as evidence-backed watchlist lanes requiring target-density checks. Treat managed cyber/compliance MSP, insurance brokerage, luxury/jewelry infrastructure, air purification, property management, and beauty/fragrance as existing-row reinforcement, not net-new.

→ READY

## [13:17] niche-intel-synthesizer
**Source:** Step 1b pattern recognition across `niche-intel-recent`, `niche-intel-historical`, `brain/context/learnings.md`, and tracker status embedded in gather posts/run prompt
**Status:** complete

### 1. Cross-Source Signal Matrix

| Niche/Industry | RECENT Sources | HISTORICAL Sources | Total Source Count | Strength |
|---|---:|---:|---:|---|
| Specialty / HNW / art / jewelry insurance brokerage | 3: Aon/USI news; Sydney Garber diligence; recent vault/calls | 5: August Felker; Hunter Hartwell; Chris Wise; Amanda Lo Iacono; prior insurance deal history | 8 | VERY STRONG, but already tracked; reinforce channel/warm-network priority only |
| Trade credit / customs bonds / cargo insurance brokerage | 0 | 2: Jeremy Black Gmail; prior TCI research output | 2 | STRONG historical, but already tracked |
| Beauty / fragrance / packaging / testing / MoCRA infrastructure | 1: E&K fragrance/beauty buyer search | 2: Jeff Stevens; Clayton Sachs | 3 | STRONG, but already tracked across multiple rows |
| Property / facilities compliance and real-estate services | 1: property-management listing | 4: E&K HOA; LL97/building-energy tracker; reserve study/building engineering; stormwater/facilities history | 5 | VERY STRONG, but already tracked; killed/tabled guardrails apply |
| Technical MRO / air purification / geotech / controls | 3: electrical testing listing; data-center/power tailwind; recent prior air-purification report | 3: Jeff Stevens MRO lens; Mike Horowitz mission-critical repair; historical air/geotech/SCADA deal flow | 6 | VERY STRONG theme; most rows already tracked |
| Electrical testing and power-system services | 2: E&K Mid-Atlantic listing; data-center/power infrastructure news | 2: technical MRO/operator-call pattern; facilities/compliance tracker adjacency | 4 | STRONG and most actionable net-new edge candidate |
| Managed cybersecurity / compliance-adjacent MSP | 4: E&K NJ listing; Channel Dive/Omdia; Auxo; 2026-08-28 thesis scan | 2: CMMC/FAR managed compliance history; generic cyber/MSP tabled history | 6 | STRONG evidence but crowded/existing-adjacent; not clean net-new |
| Supplier payment fraud / vendor-master controls | 2: Basware/Trustpair; business-services PE macro | 1: CorpNet / compliance-filing adjacency | 3 | MODERATE signal; software-heavy and service target model unproven |
| Humane wildlife removal / exclusion / remediation | 1: Rejigg listing | 1: pest-adjacent historical lessons | 2 | MODERATE evidence, but pest-adjacent lifecycle risk; watchlist only |
| Food-grade warehousing / SQF fulfillment | 1: SMB Deal Hunter listing | 1: beauty/MoCRA 3PL overlap | 2 | WEAK to MODERATE; target may be real but G&B fit thin |
| Durable civic / architectural signage and public-art fabrication | 1: Windsor Fireform / Acquiring Minds | 1: Mike Horowitz luxury-vendor ecosystem, with sign/lighting killed guardrail | 2 | WEAK; project-based and sign/lighting adjacency already killed |
| Medical-grade HBOT with insurance contracts | 0 recent new beyond historical window artifact | 1: Business Exits HBOT listing | 1 | WEAK/off-core watchlist |
| Industrial safety / PPE injury-prevention distribution | 0 recent | 1: E&K industrial safety equipment distribution listing | 1 | WEAK; distribution/inventory risk and Kay fit unresolved |
| Plumbing / HVAC / broad trades roll-up activity | 2: E&K plumbing; sponsor roll-up note | 1: broad trades historical exclusion/crowding | 3 | WEAK for G&B; broad trades are crowded and weakly differentiated |
| Luxury chauffeur / black car, car wash, oil change, pool cleaning, landfill-gas equipment | 1: SMB Deal Hunter bundle | 0-1: prior thesis scan parked chauffeur | 1-2 | WEAK/watchlist; isolated deal-level signals |

Source gaps carried forward: RECENT social coverage was degraded or unavailable; OneNote SEARCH FUND notebook was unavailable; ChatGPT selected conversation export was absent; older Granola raw API coverage was unavailable beyond vault-synced calls. These gaps reduce confidence in "absence of signal" claims.

### 2. Named Company Registry

Attio status was not safely checked in this headless session because no Attio MCP/tool was exposed and credential-file inspection is prohibited. Outreach flags below use only gather posts, vault/tracker-visible status, and named warm contacts.

| Company | Niche | Source | Independence if known | Outreach Flag | Warm Contact | Notes |
|---|---|---|---|---|---|---|
| PRMS | Specialty/HNW/art insurance | Historical | Unknown | WARM_INTRO | August Felker / insurance network | Named specialty insurance reference; already-tracked thesis support |
| J.W. Allen | Specialty/HNW/art insurance | Historical | Unknown | WARM_INTRO | August Felker / insurance network | Named specialty insurance reference |
| Genser | Specialty/HNW/art insurance | Historical | Unknown | WARM_INTRO | August Felker / insurance network | Named specialty insurance reference |
| Grober Imbey | Specialty/HNW/art insurance | Historical | Unknown | WARM_INTRO | August Felker / insurance network | Named specialty insurance reference |
| Hamptons Risk | Specialty/HNW personal lines | Historical | Unknown | WARM_INTRO | August Felker / insurance network | HNW/geographic fit; already-tracked row support |
| DRO | Specialty/HNW/art insurance | Historical | Unknown | WARM_INTRO | August Felker / insurance network | Named specialty insurance reference; exact entity not validated |
| Huntington Block | Art/jewelry insurance | Historical | Aon-owned per gather label | ACTIVE_DEAL | Insurance/art contacts | Existing thesis comp, not cold target |
| Aon | Insurance brokerage | Recent + historical | Public / consolidator | ACTIVE_DEAL | None needed | Announced USI acquisition; comp/PE heat only |
| USI | Insurance brokerage | Recent | KKR-backed before Aon transaction | ACTIVE_DEAL | None known | Consolidation comp; not target |
| KKR | Sponsor / insurance comp | Recent | Sponsor | ACTIVE_DEAL | None known | Sponsor comp only |
| Chubb | Insurance carrier | Historical | Public carrier | UNKNOWN | Jeremy Black / insurance contacts | Carrier/reference, not SMB target |
| BofA art services | Art services / insurance river-guide source | Historical | Large institution | WARM_INTRO | BofA contact via prior network | River-guide/reference source, not target |
| Trade Risk Group | Trade credit / customs / cargo insurance | Historical | Unknown | ACTIVE_DEAL | Jeremy Black | Existing tracked trade-risk lane |
| Trade Acceptance Group | Trade credit insurance | Historical | Unknown | ACTIVE_DEAL | Jeremy Black | Existing tracked trade-risk lane |
| Meridian/Texel | Trade credit insurance | Historical | Unknown | ACTIVE_DEAL | Jeremy Black | Existing tracked trade-risk lane; entity label may combine Meridian and Texel |
| Allianz Trade / Euler Hermes | Trade credit insurance | Historical | Large carrier/platform | UNKNOWN | Jeremy Black | Market comp/source, not SMB target |
| Atradius | Trade credit insurance | Historical | Large carrier/platform | UNKNOWN | Jeremy Black | Market comp/source, not SMB target |
| Coface | Trade credit insurance | Historical | Large carrier/platform | UNKNOWN | Jeremy Black | Market comp/source, not SMB target |
| Great American | Customs/cargo/trade insurance | Historical | Large carrier/platform | UNKNOWN | Jeremy Black | Carrier/reference |
| QBE | Customs/cargo/trade insurance | Historical | Large carrier/platform | UNKNOWN | Jeremy Black | Carrier/reference |
| Zurich | Customs/cargo/trade insurance | Historical | Large carrier/platform | UNKNOWN | Jeremy Black | Carrier/reference |
| Arch Amenity Group | Luxury amenity management | Historical | Unknown / likely platform-scale | ACTIVE_DEAL | Mike Horowitz | Existing tracker comp; not new target |
| American Christmas | Seasonal display / signage / luxury vendor services | Historical | Unknown | VAULT_HISTORY | Mike Horowitz | Vendor-ecosystem example; sign/lighting guardrail applies |
| E&K Security Solutions Company | Premium physical security integration | Historical email | Unknown; brokered listing | ACTIVE_DEAL | E&K | Existing premium-security row reinforcement; Hong Kong/Macau geography out-of-box |
| E&K Residential & Commercial Association Management Company | HOA/community association management | Historical email | Unknown; brokered listing | ACTIVE_DEAL | E&K | Existing HOA/property management row reinforcement |
| CorpNet | Compliance filings | Historical email | Unknown | VAULT_HISTORY | None known | Compliance/admin adjacency, not advanced |
| CAI | HOA/community association ecosystem | Historical | Association, not target | UNKNOWN | Property/HOA contacts not named | Directory/target-density clue |
| Reserve Advisors | Reserve study/building engineering | Historical | Unknown | ACTIVE_DEAL | None known | Existing reserve-study/building-engineering row context |
| Milrose | Permit expediting | Historical | Unknown / platform-scale possible | ACTIVE_DEAL | None known | Existing permit-expediting row context |
| RE BackOffice | Lease administration / RE admin outsourcing | Historical | Unknown | ACTIVE_DEAL | None known | Existing lease-admin row context |
| E&K Air Purification Systems Company | Technical MRO / air purification | Historical + recent prior output | Unknown; brokered listing | ACTIVE_DEAL | E&K | Existing/tracked air-purification row |
| E&K Geotechnical Engineering Services Company | Geotech/CMT | Historical email | Unknown; brokered listing | ACTIVE_DEAL | E&K | Existing/tracked geotech/CMT row |
| E&K Industrial & Safety Equipment Distribution Company | Safety/PPE distribution | Historical email | Unknown; brokered listing | NEW_TARGET | E&K | Watchlist only; product distribution/inventory risk |
| Business Exits HBOT listing | Medical-grade HBOT | Historical email | Unknown; brokered listing | NEW_TARGET | Business Exits | Off-core watchlist; company name not disclosed in gather post |
| E&K Healthcare Regulatory Compliance SaaS / ECA Automation | Healthcare compliance SaaS | Historical email | Unknown; brokered listing | UNKNOWN | E&K | Software caution; do not promote without service model |
| Basware | Supplier payment fraud / AP automation | Recent web | Platform/software | UNKNOWN | None known | Acquirer; validates demand, not target |
| Trustpair | Supplier bank-account validation | Recent web | Software; acquired by Basware | UNKNOWN | None known | Demand comp; service-model question remains |
| Accel-KKR | Sponsor / software comp | Recent web | Sponsor | UNKNOWN | None known | Source/ownership context only |
| SLB | Data-center cooling / industrial infra | Recent web | Public / large industrial | UNKNOWN | None known | Tailwind comp only |
| Kelvion | Data-center cooling | Recent web | Large industrial | UNKNOWN | None known | Tailwind comp only |
| Omdia | MSP market intelligence | Recent web | Research firm | UNKNOWN | None known | Source only |
| Channel Dive | MSP market intelligence | Recent web | Publication | UNKNOWN | None known | Source only |
| Auxo Capital Advisors | MSP market commentary | Recent web | Advisory/source | UNKNOWN | None known | Source only |
| SI Global | Business-services PE report | Recent web | Advisory/source | UNKNOWN | None known | Macro source only |
| ITPro | Supplier payment fraud acquisition coverage | Recent web | Publication | UNKNOWN | None known | Source only |
| E&K Managed Cybersecurity Services Company | Managed cyber/compliance MSP | Recent email | Unknown; brokered listing | ACTIVE_DEAL | E&K | Existing-adjacent/crowded; not clean new row |
| E&K Electrical Testing and Power-System Services Company | Electrical testing/power-system services | Recent email | Unknown; brokered listing | NEW_TARGET | E&K | Strongest net-new candidate; target identity not disclosed |
| E&K Plumbing Contractor | Plumbing / broad trades | Recent email | Unknown; brokered listing | UNKNOWN | E&K | Broad-trades signal; not G&B-differentiated |
| Rejigg Humane Wildlife Removal Specialists | Wildlife removal/exclusion | Recent email | Unknown; brokered listing | NEW_TARGET | Rejigg | Watchlist; pest-adjacent risk |
| SMB Deal Hunter Military-Family Property Management Company | Property management | Recent email | Unknown; brokered listing | ACTIVE_DEAL | SMB Deal Hunter | Existing property-management row reinforcement |
| SMB Deal Hunter Food-Grade Warehousing / Fulfillment Company | Food-grade warehousing/SQF fulfillment | Recent email | Unknown; brokered listing | NEW_TARGET | SMB Deal Hunter | Watchlist; G&B fit and target density thin |
| SMB Deal Hunter Pool Cleaning Company | Pool cleaning | Recent email | Unknown; brokered listing | UNKNOWN | SMB Deal Hunter | Isolated deal signal; monthly billing noted |
| SMB Deal Hunter Landfill-Gas Equipment Maker | Landfill gas compliance equipment | Recent email | Unknown; brokered listing | NEW_TARGET | SMB Deal Hunter | Isolated compliance-driven equipment signal |
| SMB Deal Hunter Luxury Chauffeur / Black Car Company | Luxury chauffeur / transport | Recent email | Unknown; brokered listing | UNKNOWN | SMB Deal Hunter | Park/watchlist; fleet/dispatch complexity |
| SMB Deal Hunter Car Wash Company | Automotive services | Recent email | Unknown; brokered listing | UNKNOWN | SMB Deal Hunter | Watchlist only; auto repair/services excluded historically |
| SMB Deal Hunter Oil-Change Company | Automotive services | Recent email | Unknown; brokered listing | UNKNOWN | SMB Deal Hunter | Watchlist only; auto repair/services excluded historically |
| Sponsor HVAC/Plumbing/Electrical Roll-Up | Broad trades | Recent email | Sponsor-backed | UNKNOWN | SMB Deal Hunter | PE heat/crowding clue, not target |
| Windsor Fireform | Durable signage/public-art fabrication | Recent newsletter | Independently acquired by searcher/operator | VAULT_HISTORY | Acquiring Minds source | Searcher-acquired comp; negative/caution signal under learnings |
| Acquiring Minds | Search/acquisition source | Recent newsletter | Media/source | UNKNOWN | None known | Source only |
| WSN Group | Current deal/call context | Recent Granola | Unknown | ACTIVE_DEAL | Current deal network | Reinforces Sydney Garber/jewelry diligence, not new niche |
| Sydney Garber | Luxury jewelry / current deal | Recent Granola/vault | Active deal | ACTIVE_DEAL | Kay/current deal team | Current deal, do not treat as target-discovery lead |

### 3. Contact-to-Niche Map

| Contact | Relationship Warmth | Niche(s) | How They Help | Current Use |
|---|---|---|---|---|
| August Felker | Met/call history | HNW personal lines; art/jewelry insurance | Validates sticky recurring HNW insurance and named independent broker universe | River guide for existing insurance rows |
| Hunter Hartwell | Met/call history | Insurance brokerage acquisitions; carve-outs | Explains multiple wall and carve-out strategy | Diligence / thesis calibration |
| Jonathan Crystal | Historical insurance contact | Specialty/HNW/art insurance | Named in insurance contact cluster | Warm-network asset, details thin |
| Chris Wise | Met/call history | Art insurance; art transaction workflows | Validated KYC/wire/reporting pain and art ecosystem dynamics | River guide for art/insurance, not standalone escrow niche |
| Amanda Lo Iacono | Met/call history | Art transaction workflows; galleries/advisors/family offices | Independently validated KYC/escrow/back-office pain | River guide only; standalone niche rejected |
| Jeremy Black | Email/call thread | Trade credit; customs bonds; cargo insurance; FMO/IMO | Firsthand customer/operator evidence and named market participants | River guide for trade-risk row |
| Jolene | Historical operator reference via Jeremy Black | FMO/IMO | Context on insurance marketing organization aggregator | Thin lead; not enough for independent action |
| Mike Horowitz | Met/call history | Luxury amenity; security; marine/yacht; physical plant vendor ecosystem | Supplies Kay-fit operating environments and second-order vendor logic | River guide for luxury infrastructure / marine / security |
| Jeff Stevens | Investor/call history | MRO/service-heavy models; fragrance/packaging; pest caution | Challenges crowded pest and pushes asset-light service/MRO adjacencies | Thesis calibration |
| Clayton Sachs | Investor/call history | Fragrance testing; packaging; specialty chemical distribution; collectibles insurance | Points toward G&B-specific adjacent lanes | Thesis calibration |
| Andrew Freiman | Call history | Pest/commercial property services | Historical pressure-testing of pest thesis | Lifecycle guardrail; do not resurface pest as live |
| Albert Kim | Call history | Pest/commercial property services | Historical pressure-testing of pest thesis | Lifecycle guardrail |
| NoFo | Call/source history | Pest/commercial property services | Historical pest signal | Lifecycle guardrail |
| Camilla | Internal/advisor call context | Pest, deal screens, economics/diligence | Can support economics/diligence if Kay requests | Not default owner for new thesis |
| Brooke | Recent call context | Sydney Garber/luxury jewelry diligence | Current deal support, not broad niche source | Active-deal context only |
| E&K | Broker/source | Electrical testing; managed cyber; plumbing; HOA; security; air purification; geotech; safety distribution | Deal-flow source with concrete listings | Source for target-density and saleability clues |
| SMB Deal Hunter | Broker/source | Property management; food-grade warehousing; pool; landfill gas; chauffeur; car wash; oil change | Deal-flow source with isolated saleability signals | Watchlist/source only |
| Business Exits | Broker/source | HBOT / healthcare wellness | Deal-level evidence | Off-core watchlist |
| Rejigg | Broker/source | Humane wildlife removal | Deal-flow source for wildlife/exclusion niche | Watchlist/source only |

### 4. Lead Lifecycle Tracker

| Niche / Strategy | Proposed By / Source | Challenged By / Constraint | Lifecycle Status | Outcome / Guardrail |
|---|---|---|---|---|
| Specialty/HNW/art/jewelry insurance brokerage | August Felker, Hunter Hartwell, Chris Wise, Amanda Lo Iacono, Aon/USI news | PE heat and existing tracker saturation | ACTIVE / already tracked | Reinforce existing rows; do not create duplicate |
| Trade credit / customs bonds / cargo insurance | Jeremy Black + prior research | Existing `WEEKLY REVIEW` row | ACTIVE / already tracked | Use as warm-network priority, not net-new |
| FMO/IMO insurance distribution aggregator | Jeremy Black/Jolene | Thin target proof | ACTIVE / already tracked but thin | Do not advance without target-density proof |
| Art transaction KYC / escrow / back-office services | Chris Wise, Amanda Lo Iacono | Prior identifier: <5 acquirable art-specific providers, low willingness to pay | REJECTED as standalone | Use pain as art/insurance river-guide context only |
| Luxury amenity management | Mike Horowitz | Existing tracker row; operational intensity | ACTIVE / already tracked | No duplicate |
| Premium physical security integration/lifecycle maintenance | Mike Horowitz, E&K security listing | Existing tracker row; geography caveat on E&K listing | ACTIVE / already tracked | Reinforcement only |
| Marine/yacht services | Mike Horowitz | Existing tracked/tabled sublanes | ACTIVE / already tracked | No duplicate; yacht software remains tabled |
| Beauty/fragrance/package testing/MoCRA infrastructure | Jeff Stevens, Clayton Sachs, E&K buyer search | Existing tracker rows | ACTIVE / already tracked | Reinforcement only |
| Property/facilities compliance and real-estate services | E&K HOA, LL97, reserve/permit/stormwater history | Existing tracker rows; sign/lighting, vegetation, fire/life safety, cleaning guardrails | ACTIVE / already tracked | Reinforcement only |
| Air purification / filtration service | E&K air listing, 2026-08-24 report | Existing tracked row | ACTIVE / already tracked | No duplicate |
| Geotech/CMT | E&K geotech listing, prior report | Existing tracked row | ACTIVE / already tracked | No duplicate |
| Water SCADA / controls | Prior tracker context | Existing tracked row | ACTIVE / already tracked | Electrical testing should be kept distinct from SCADA |
| Electrical testing and power-system services | E&K listing + data-center/power tailwind + MRO pattern | Must prove independent U.S. target density and avoid broad electrical contractor roll-up crowding | PROPOSED / advance to Step 2 | Strongest net-new edge candidate |
| Managed cyber/compliance MSP | E&K listing, Channel Dive/Omdia, Auxo, thesis scan | Crowded MSP consolidation; overlaps CMMC/cyber compliance rows | CHALLENGED / existing-adjacent | Do not create duplicate unless reframed as non-software managed compliance |
| Supplier payment fraud / vendor-master controls | Basware/Trustpair | Software-heavy; service-provider target density unproven | PROPOSED / watchlist | Step 2 only if identifier can prove service businesses, not SaaS |
| Humane wildlife removal / exclusion / remediation | Rejigg listing | Pest-adjacent; premium pest was tabled/killed guardrail; target density and G&B fit unproven | PROPOSED / watchlist | Hold unless commercial/premium exclusion services prove distinct from pest |
| Food-grade warehousing / SQF fulfillment | SMB Deal Hunter | Capital/real-estate exposure; overlaps 3PL; weak Kay fit | PROPOSED / watchlist | Do not advance without asset-light compliance/service wedge |
| Durable civic / architectural signage/public-art fabrication | Windsor Fireform / Acquiring Minds | Project-based/manufacturing-heavy; sign/lighting maintenance killed; searcher-acquired comp is negative signal | CHALLENGED / likely reject | Do not advance as live niche absent recurring maintenance model |
| Industrial safety / PPE distribution | E&K safety equipment listing | Product distribution/inventory risk; weak Kay fit | PROPOSED / watchlist | Park unless injury-prevention compliance service wrapper exists |
| Medical-grade HBOT with insurance contracts | Business Exits listing | Healthcare/operator and concentration risk; off-core | PROPOSED / off-core watchlist | Do not advance without Kay choosing healthcare/wellness lane |
| Plumbing / HVAC / broad trades | E&K plumbing, sponsor roll-up | PE crowding and weak G&B differentiation | REJECTED for broad thesis | Only proprietary target exception |
| Pest / pest-adjacent commercial property services | Historical calls | Premium pest tabled; market crowding | TABLED / protected | Do not resurface as active |
| General compliance e-learning, ADA doc remediation, auto repair, fire/life safety, fire-pump/hydrant testing equipment, vegetation management, sign/lighting maintenance, high-end commercial cleaning | Prior tracker killed/table rows | Killed/tabled tracker status | REJECTED / protected | Must not advance without materially new evidence |

### 5. Picks-and-Shovels / Edge-Niche Expansion

| Umbrella Theme | Growth Trend | Operational Complexity Created | Obvious Niches | Picks-and-Shovels / Edge Niches | Compliance / Risk Niches | Target-Density Clues | G&B Fit |
|---|---|---|---|---|---|---|---|
| Asset Protection & Stewardship | HNW wealth transfer and valuable-asset ownership | Collections, jewelry, homes, and legacy assets need coverage, appraisals, renewal workflows, and claims support | HNW insurance brokers; art insurance; jewelry insurance | Appraisal-update admin, jewelry insurance documentation, claims prep, collection risk audits | Underinsurance review, carrier placement, estate-triggered policy transition | Existing insurance rows and named brokers from August/Jeremy; PE heat from Aon/USI | Strong, but existing; money-maker answer: specialist brokers and admin vendors profit when asset complexity exceeds household-policy capability |
| Trust, Compliance & Verification | AI-enabled supplier impersonation and payment fraud | Vendor master data, bank-account changes, AP approvals, and invoice-to-payment controls become risk workflows | AP automation software; fraud detection SaaS | Managed vendor-master cleanup, supplier onboarding verification, outsourced payment-control reviews | Bank-account validation, payment-instruction change controls, audit trails | Basware/Trustpair validates demand; no service-provider density yet | Medium if service-led; money-maker answer: outsourced controls vendors profit when finance teams cannot trust supplier-payment data |
| Trust, Compliance & Verification / Facilities | Power reliability, data-center load, electrification, and insurance/safety scrutiny | Facilities must test, document, maintain, and certify electrical systems before failures | Electrical contractors; power equipment OEMs | Electrical testing firms, relay calibration, thermography, dielectric fluid analysis, arc-flash studies, commissioning support | OSHA/NFPA/insurance-driven arc-flash and power-quality documentation | E&K listing proves saleability; adjacent MRO/facilities rows show recurring maintenance demand | Strong; money-maker answer: independent testing/service firms profit because customers need proof that power systems are safe and reliable |
| Beauty, Wellness & Longevity Infrastructure | Beauty/fragrance growth plus MoCRA and premium packaging complexity | Brands need testing, documentation, packaging validation, kitting, fulfillment, and quality records | Beauty brands; fragrance brands; retailers | Testing labs, package validation, specialty chemical distribution, premium kitting/assembly, sampling fulfillment | MoCRA compliance, ingredient/label testing, stability testing, QA documentation | Existing tracker rows and Jeff/Clayton/E&K buyer-search evidence | Strong, but existing; money-maker answer: labs and specialty service vendors profit when brands outsource regulated complexity |
| Luxury, Heritage & Personal Goods | Luxury jewelry deal activity and legacy-brand transition | Product provenance, inventory controls, repair, insurance, retail relationships, and aftercare must professionalize | Jewelry retailers/brands | Repair/aftercare networks, inventory-control services, jeweler's block brokerage, manufacturing QA, specialty logistics | Insurance, provenance, security, quality records | Sydney Garber active deal and recent calls; existing jewelry/art insurance rows | Strong but active-deal-adjacent; money-maker answer: aftercare, insurance, and QA vendors profit when legacy luxury businesses need institutional systems |
| Property / Community Infrastructure | Aging buildings, HOA complexity, climate/water rules, tenant amenity competition | Owners/boards need administration, engineering, reserve studies, inspections, O&M, and vendor coordination | Property management; facilities management | Reserve studies, building engineering, stormwater O&M, submetering admin, lease admin, amenity operations | LL97/building energy, stormwater compliance, inspection documentation | Existing rows, HOA listing, stormwater target estimates | Medium to strong, but existing; money-maker answer: specialized compliance/O&M vendors profit when property owners cannot manage documentation and vendors internally |
| Technical MRO / Mission-Critical Equipment | Institutional air quality, lab/pharma/process controls, municipal/school infrastructure | Equipment must be designed, installed, serviced, documented, and repaired under downtime pressure | HVAC, filters, general maintenance | Air purification service, calibration, controls service, preventative maintenance, emergency repair | Indoor air quality, lab/process safety, municipal procurement documentation | E&K air listing, geotech listing, existing tracker rows | Medium to strong, mostly existing; money-maker answer: service firms profit because downtime and failed inspections are costly |
| Pest / Building Envelope Edge | Health/safety sensitivity and property damage from wildlife intrusion | Removal, exclusion, remediation, emergency response, and prevention contracts | Pest control; wildlife removal | Commercial exclusion specialists, attic/crawl remediation, prevention maintenance | Zoonotic risk, property damage, tenant complaints | Rejigg listing only plus historical pest evidence | Weak to medium; money-maker answer: exclusion/remediation specialists profit when customers need more than one-time pest treatment |
| Food / Regulated Fulfillment | Food brands and specialty retail need compliant storage and repeat replenishment | SQF documentation, inventory, traceability, fulfillment, and customer reorder workflows | Warehousing; 3PL | Food-grade fulfillment, kitting, cold-chain-light services, quality documentation outsourcing | SQF compliance, traceability, recalls, sanitation records | One SMB listing; no broad target count | Weak; money-maker answer: compliant fulfillment vendors profit when brands cannot run certified logistics themselves |
| Civic / Architectural Environment | Public art, durable signage, placemaking, and custom fabrication | Estimating, deposits, project WIP, field installation, records, and municipal/customer coordination | Signage fabricators; public-art studios | Maintenance contracts, install/repair vendors, permitting support, design-to-fabrication ops | Permits, safety, public procurement | Windsor Fireform only; sign/lighting killed history | Weak; money-maker answer: maintenance/permitting vendors would profit, but current evidence is project-manufacturing rather than recurring service |

### 6. Convergence Report

| Rank | Signal | Independent Source Count | Named Companies | Contacts | Buy-Box Alignment | Picks-and-Shovels Strength | Actionability | Verdict |
|---:|---|---:|---|---|---|---|---|---|
| 1 | Electrical testing and power-system services | 4 | E&K Electrical Testing and Power-System Services Company; SLB/Kelvion as tailwind comps | E&K; Jeff/Mike pattern context | Strong: recurring planned maintenance, emergency service, compliance/safety documentation, high EBITDA in listing | Strong | High | Advance to Step 2 as the one clean net-new candidate. Keep distinct from broad electrical contracting and water SCADA. |
| 2 | Supplier payment fraud / vendor-master controls services | 3 | Basware; Trustpair; Accel-KKR | None identified | Medium if service-led; weak if pure software | Strong conceptual shovel, unproven target base | Medium-low | Watchlist/conditional Step 2. Identifier must prove service-provider target density before promotion. |
| 3 | Humane wildlife removal / exclusion / remediation | 2 | Rejigg Humane Wildlife Removal Specialists | Rejigg/source only | Medium on recurring prevention and emergency need; weak Kay fit unless premium/commercial | Medium | Medium-low | Watchlist. Do not advance unless distinct from killed/tabled pest and target density is proven. |
| 4 | Food-grade warehousing / SQF fulfillment | 2 | SMB Deal Hunter Food-Grade Warehousing / Fulfillment Company | SMB Deal Hunter/source only | Medium revenue repeat; weak due to facilities/capital exposure and thin G&B fit | Medium | Low | Park unless an asset-light compliance/kitting edge appears. |
| 5 | Durable civic / architectural signage and public-art fabrication | 2 | Windsor Fireform; American Christmas as adjacent vendor example | Acquiring Minds; Mike Horowitz | Weak to medium: margins exist, but project/manufacturing heavy and recurring revenue thin | Weak to medium | Low | Likely reject for this run; maintain as negative/caution evidence. |

Strict synthesis verdict: convergence is strongest overall in already-tracked insurance, beauty/fragrance, property/facilities, and technical MRO lanes. The run does not support multiple net-new one-pagers. **Electrical testing and power-system services** is the only candidate with enough recent evidence, operational-complexity logic, and distinctness from existing tracker rows to proceed to Step 2. Supplier payment fraud/vendor-master controls and humane wildlife removal have real but incomplete signals and should be challenged hard before any tracker promotion.

→ READY

## [13:31] niche-intel-identifier
**Source:** Step 2 identify + industry validation across synthesizer outputs, tracker context in chatroom, `brain/context/learnings.md`, and current web validation
**Status:** complete

### Step 2 Candidate Verdict

Advanced candidates: **1**

1. **Electrical Testing and Power-System Services**

Watchlist lanes reviewed but **not advanced this cycle**:
- **Supplier Payment Fraud / Vendor-Master Controls:** real demand signal, but current evidence is software/platform-led rather than acquirable SMB services. Basware/Trustpair validates AI-enabled payment-fraud pain and supplier-bank validation demand, but the target universe surfaced so far is mostly SaaS, AP automation, MDM, bank-verification platforms, and enterprise BPO/service wrappers rather than independent recurring service providers. Keep as watchlist until a service-led vendor-master cleanup/payment-control review target pool is proven.
- **Humane Wildlife Removal / Exclusion:** real deal-flow signal and recurring-prevention possibility, but not advanced because it is too close to the protected pest/pest-adjacent lane without enough proof of a distinct commercial/premium exclusion niche. NWCOA confirms a dedicated wildlife-control industry, and pest-control market growth is healthy, but this cycle only has one listing plus historical pest adjacency; G&B fit and PE/crowding guardrails remain unresolved.

### Advanced Candidate 1

**Niche name:** Electrical Testing and Power-System Services

**Umbrella theme:** Trust, Compliance & Verification / Facilities and Mission-Critical Infrastructure

**Growth trend / tailwind:** Power reliability burden is rising as data centers, electrification, aging grid assets, industrial automation, healthcare/lab uptime needs, and insurance/safety documentation all increase the cost of electrical-system failure. Future Market Insights estimates the global electrical testing services market at $9.6B in 2026, growing to $19.6B by 2036 at 7.4% CAGR; Market Data Forecast estimates North America at $2.98B in 2025, $5.53B by 2034, and says the U.S. represents 70.5% of North American revenue. IEA adds the macro power-load tailwind: global data-center electricity consumption is projected to double to about 945 TWh by 2030, with data-center electricity consumption growing around 15% annually from 2024-2030. Sources: [Future Market Insights](https://www.futuremarketinsights.com/reports/electrical-testing-services-market), [Market Data Forecast](https://www.marketdataforecast.com/market-reports/north-america-electrical-testing-services-market), [IEA Energy and AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai).

**Operational complexity created:** Facilities with critical electrical infrastructure need acceptance testing, maintenance testing, relay calibration, thermography/infrared scanning, dielectric fluid/oil analysis, transformer and circuit-breaker testing, power-quality monitoring, arc-flash studies, protective-device coordination, commissioning support, emergency troubleshooting, and audit-ready documentation. NFPA 70B specifically covers preventive maintenance for electrical, electronic, and communication systems and equipment; NETA defines accredited companies as third-party independent power-system testing, analysis, and maintenance providers across low-, medium-, and high-voltage distribution, substation, and generation equipment. Sources: [NFPA 70B](https://www.nfpa.org/codes-and-standards/nfpa-70b-standard-development/70b), [NETA accreditation overview](https://www.netaworld.org/accreditation/overview).

**Why it is a picks-and-shovels / edge beneficiary rather than visible end-market:** The visible end-markets are data centers, utilities, hospitals, labs, commercial facilities, industrial plants, renewable/grid infrastructure, and electrical construction. This niche sells the required verification and reliability shovel: customers do not buy testing for branding; they buy it because downtime, fire risk, failed commissioning, failed insurance review, OSHA/NFPA exposure, or unplanned outage is expensive. It also avoids broad electrical construction by focusing on B2B recurring/reoccurring testing, maintenance, commissioning, protection, documentation, and emergency response for installed electrical infrastructure.

**Thesis:** Acquire a regional B2B electrical testing and power-system services provider serving mission-critical facility, industrial, utility, healthcare/lab, data-center, and insurance/compliance-driven customers. The attractive wedge is planned maintenance plus compliance/reporting plus emergency response, not project electrical contracting. The category fits the "shovel seller" learning because customers must repeatedly prove that complex electrical assets are safe, reliable, and maintained.

**Source signal:** Current E&K listing in recent gather: $6.1M revenue, $3.5M normalized EBITDA, planned maintenance plus 24/7 emergency support; services include thermographic inspections, dielectric fluid analysis, component testing, relay calibration, arc-flash studies, power-quality monitoring, system protection upgrades, and commissioning. External validation: Blackstone agreed to acquire Shermco for about $1.6B in 2025; Blackstone describes Shermco as electrical system maintenance, repair, testing, commissioning, and design with 600+ NETA technicians and 200 engineers across 40 U.S./Canada service centers. Shermco also bought Power Test in 2024, a NETA-accredited electrical testing business in North Carolina, and R3L Engineering in 2025. Sources: chatroom `niche-intel-recent`; [Blackstone/Shermco](https://www.blackstone.com/news/press/blackstone-announces-agreement-to-acquire-shermco-for-approximately-1-6-billion/), [Shermco/Power Test](https://www.prnewswire.com/news-releases/shermco-industries-acquires-power-test-a-leading-neta-testing-company-302105319.html), [Shermco/R3L](https://www.prnewswire.com/news-releases/shermco-expands-power-systems-engineering-capabilities-with-acquisition-of-r3l-engineering-302459461.html).

**Key question:** Can we find 20-50 independent, owner-led regional firms where recurring/reoccurring maintenance, testing, emergency response, and compliance documentation are the majority of revenue, excluding construction-heavy electrical contractors and PE-platform add-ons?

**Preliminary fit assessment:** **Medium to Strong.** Strong on revenue quality, mission criticality, growth tailwind, B2B repeat behavior, exit path, and operational repeatability. Medium on Kay-specific right-to-win: this is less luxury/trust-network native than insurance/beauty/property lanes, but it is explainable through facility risk, reliability, documentation, and customer-service professionalism. Likely hair: technician recruiting, safety culture, specialty equipment, licensing/certifications, owner technical dependence, and outage/emergency scheduling. What absorbs the J curve: reoccurring maintenance/testing schedules, compliance documentation, high cost of failure, emergency response demand, and expanding power-infrastructure load.

**QUICK SCREEN:**
- **Margins:** Strong to Moderate. E&K listing shows unusually high normalized EBITDA ($3.5M on $6.1M revenue), likely requiring diligence. Sponsor-scale Shermco reportedly generated 10.4%-12.3% EBITDA margins in 2024/LTM 2025 per S&P search result, while service-heavy specialist firms can price above broad electrical contracting. Initial screen view: likely capable of 15%+ EBITDA at well-run regional specialist scale, but do not underwrite the E&K margin as typical without company-level proof.
- **Recurring / Reoccurring Revenue:** High. Revenue is often reoccurring through planned maintenance, scheduled testing, arc-flash updates/reviews, periodic thermography, power-system commissioning, emergency response, and inspection/documentation cycles. NETA/NFPA framing supports testing and maintenance as ongoing reliability/compliance work, not one-time installs.
- **Industry Growth:** Strong. External market sources indicate 6.4%-7.4% U.S./global CAGR, with North America/U.S. driven by grid modernization, industrial modernization, regulatory enforcement, predictive maintenance, data centers, and power continuity.

**TARGET TAM:**
- **Total firms in market:** Estimate / inference: 300-700 U.S. firms if including NETA-accredited companies, non-NETA regional power-system testing firms, relay/calibration specialists, arc-flash engineering/testing shops, and testing-heavy electrical maintenance providers. This excludes broad electrical contractors whose revenue is mainly installation or construction.
- **Independently owned potential targets:** Estimate / inference: 75-200 plausible independent/regional targets nationally after removing large OEMs, global testing firms, sponsor-backed platforms, utility in-house groups, and construction-heavy contractors. A tighter first sprint should start with NETA directory companies plus regional "power system testing", "relay testing", "arc flash", "infrared electrical inspection", and "transformer oil analysis" providers in Mid-Atlantic, Northeast, Southeast, Texas, and Midwest industrial corridors.
- **Already PE-backed/acquired:** Estimate / inference: 20-40 relevant firms/platform locations have been acquired or are sponsor-backed across Shermco/Gryphon/Blackstone, RESA/Investcorp, Vertiv ERS, and related electrical infrastructure service platforms. Named recent activity includes Shermco acquiring Power Test, R3L, Power Products & Solutions, and Eastern High Voltage; RESA has an active acquisitions page and recent field-service acquisitions.
- **PE consolidation risk:** Medium-High. There is active sponsor validation and a clear exit path, but also a closing window. The niche is less picked over than generic HVAC/plumbing/electrical contracting, but platforms are already rolling up high-quality NETA and regional power-service firms.
- **Named examples:** American Electrical Testing (Massachusetts), A&F Electrical Testing (California), 360 Electrical & Engineering Services (Florida), Potomac Testing (Maryland), Power Solutions Group (Ohio), Saber Power Field Services (Texas), Quad Plus electrical power testing (Illinois/Indiana), Power Test (North Carolina, acquired by Shermco), Eastern High Voltage (New Jersey, acquired by Shermco), Electrical Reliability Services / Vertiv (national platform). Ownership must be verified before outreach; these are target-universe examples, not cleared targets.

**MARKET TAM:**
- **Market size:** $9.6B global electrical testing services market in 2026; $2.98B North America in 2025, implying roughly $2.1B U.S. using Market Data Forecast's 70.5% U.S. share. This clears the $500M investor floor.
- **Growth rate:** 7.4% global CAGR 2026-2036; 7.11% North America CAGR 2025-2034; FMI cites U.S. electrical testing services growth at 6.4%.
- **Key demand drivers:** Data-center power density and uptime requirements; grid modernization and electrification; aging transformers/switchgear; industrial automation; renewable/storage interconnection; NFPA/OSHA/insurance documentation; predictive maintenance adoption; customer need to avoid downtime, outages, fires, and failed commissioning.

**Checked against active niches:**
- **Water SCADA / controls:** Distinct. SCADA/control systems monitor and automate water/utility operations; electrical testing validates power equipment, protective devices, switchgear, transformers, relays, arc-flash conditions, and maintenance state across many facility types.
- **Air Purification / Filtration Service:** Distinct. Both are technical MRO, but air purification is HVAC/IAQ equipment design/service; this is electrical distribution and power-system reliability/testing.
- **Geotech / Construction Materials Testing:** Distinct. Both are testing services, but geotech/CMT serves soil/materials/construction QA; this serves live electrical infrastructure and facility power systems.
- **Premium Physical Security Integration / Lifecycle Maintenance:** Distinct. Both involve mission-critical systems and service contracts, but security integration is access/camera/alarm hardware; this is electrical power testing and compliance.
- **Building Energy & Emissions Compliance / LL97:** Distinct. LL97 is building energy reporting/decarbonization compliance; electrical testing is safety/reliability/maintenance of electrical assets.
- **Reserve Study / Building Engineering / Facilities Management:** Adjacent but distinct. Those lanes assess buildings and manage operations broadly; this is specialized technical testing/maintenance with NETA/NFPA-driven credentials.
- **Broad electrical contracting / sponsor HVAC-plumbing-electrical roll-ups:** Explicitly excluded. Candidate only includes testing/service-led firms with recurring/reoccurring maintenance, documentation, and emergency response; construction/project contractors should not be included.
- **Fire/life safety and fire-pump/hydrant testing equipment protected lanes:** Distinct risk domain and equipment set; avoid reframing this as fire/life safety.

### Watchlist Evaluation

**Supplier Payment Fraud / Vendor-Master Controls**
- **Reason not advanced:** Demand is validated, but the acquirable service-provider niche is not. Basware's proposed Trustpair acquisition supports a real trend: AI-enabled supplier impersonation, bank-account changes, AP controls, and invoice-to-payment assurance. Trustpair validates supplier accounts during onboarding, account changes, and payment authorization; Basware says the combination adds end-to-end invoice-to-payment assurance. However, named companies surfaced in the scan are mainly software/platform vendors (Trustpair, Basware, apexanalytix, PaymentWorks, GraphiteConnect, Eftsure, Trustmi, Supplier.io) or enterprise procurement/MDM tools. No 20-50 independent SMB services universe has been proven.
- **What would change the call next cycle:** Evidence of recurring outsourced vendor-master cleanup, supplier onboarding verification, payment-control review, AP fraud managed service, or finance-operations BPO providers with non-software revenue and 15%+ EBITDA potential.
- **Sources:** [Basware/Trustpair PRNewswire](https://www.prnewswire.com/news-releases/basware-signs-agreement-to-acquire-trustpair-302859775.html), [Trustpair vendor master governance](https://trustpair.com/master-data-management/), [GraphiteConnect bank verification overview](https://www.graphiteconnect.com/blog/10-bank-account-verification-services-that-help-prevent-vendor-fraud).

**Humane Wildlife Removal / Exclusion**
- **Reason not advanced:** The Rejigg listing has attractive signals ($1.29M revenue, $335K EBITDA / $454K SDE signal, 24/7 response, prevention contracts), and NWCOA confirms a dedicated wildlife-control professional ecosystem. But the broader market data rolls into pest control, where G&B already has tabled/protected guardrails due to crowding and weak differentiation. This cycle did not prove enough separation around B2B/commercial exclusion, attic/crawl remediation, prevention maintenance, insurance/restoration adjacency, or premium property service.
- **What would change the call next cycle:** A target-density pass showing 20-50 independent commercial/premium exclusion specialists whose economics come from prevention, exclusion, remediation, and maintenance contracts rather than one-off residential removal or generic pest routes.
- **Sources:** [NWCOA](https://www.nwcoa.com/), [NWCOA hiring guidance](https://www.nwcoa.com/Hiring-a-professional), [FMI U.S. & Canada Pest Control Services Market](https://www.futuremarketinsights.com/reports/united-states-and-canada-pest-control-services-market).

### Identifier Close

This Step 2 pass advances exactly one candidate: **Electrical Testing and Power-System Services**. It is specific enough to be a niche, passes the initial screen at the industry level, has a credible target-density hypothesis, and is distinct from existing tracker rows when narrowed to B2B power-system testing/maintenance providers rather than broad electrical contractors.

→ READY

## [13:34] niche-intel-onepager
**Source:** Step 3 one-pager creation / python-pptx template clone
**Status:** complete

Created the required one-pager for **Electrical Testing and Power-System Services** using the local template `brain/library/internal/one-pager-template/customs-bonds-template.pptx`.

- **Local PPTX path:** `/home/ubuntu/projects/Sapling/brain/library/internal/one-pagers/Electrical Testing and Power-System Services September 2026.pptx`
- **Drive folder:** `1N9YKYVqdMZbMLpvzjmZ8MbNUUtT1i7AI`
- **Drive folder URL:** https://drive.google.com/drive/folders/1N9YKYVqdMZbMLpvzjmZ8MbNUUtT1i7AI
- **Uploaded presentation ID:** `18OY6lg50DAdEGI11QNlDgHYBbnQidZ5H`
- **Uploaded presentation URL:** https://docs.google.com/presentation/d/18OY6lg50DAdEGI11QNlDgHYBbnQidZ5H/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **Template handling:** cloned the local PPTX template; populated the existing table structure; set title run to explicit black; added a second slide titled `Sources`.
- **Duplicate handling:** no exact existing folder or one-pager was found in the WEEKLY REVIEW parent; created a new niche folder under WEEKLY REVIEW folder `1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT`. Post-upload verification shows the folder contains exactly one PPTX one-pager.
- **Source coverage:** included linked sources for the chatroom trace, E&K Gmail thread, Future Market Insights, Market Data Forecast, IEA, NFPA 70B, NETA overview, NETA directory, Blackstone/Shermco, Shermco/Power Test, Shermco/R3L, Shermco acquisition program, RESA Power acquisition activity, Vertiv ERS, the one-pager template reference, and the prior deal-tape market signal scan.

→ READY
