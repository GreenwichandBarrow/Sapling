---
schema_version: 1.0.0
date: 2026-08-10
task: Headless Monday full Niche Intelligence run
agents: [niche-intel-recent, niche-intel-historical, niche-intel-synthesizer, niche-intel-identifier, niche-intel-onepager, niche-intel-scorer, niche-intel-tracker]
status: completed
run_mode: monday
runtime: Codex/systemd
linked_output: brain/outputs/2026-08-10-niche-intelligence-report.md
---

# Agent Chatroom: Niche Intelligence Full Run

## Coordination Log

## [22:30] orchestrator
Starting headless Monday full run under Codex/systemd. Credentials resolved through `scripts/op-env.sh`; `gog auth list --check` confirms Workspace access for `kay.s@greenwichandbarrow.com`.

Mandatory sequence in force: RECENT + HISTORICAL gather, synthesize, identify, one-pager, industry score, tracker update, markdown report, JSON sidecar.

---
## [niche-intel-recent] — 2026-08-10 23:05 ET
**Source:** Last-14-days recent intelligence across web/social, Gmail, Granola, vault, inbox passive signals, and live tracker context
**Status:** complete

### Tracker Duplicate Context
Live `WEEKLY REVIEW` was read before synthesis. Active/pending rows already cover the main duplicate lanes surfaced this cycle: specialty/HNW insurance, high-value storage, building services, fire/life safety, broker-dealer compliance, insurance SIU, CMMC/FAR compliance, contents restoration, vegetation management, beauty 3PL/kitting, luxury packaging/testing, jeweler's block insurance, yacht property management, and related property/compliance services.

### Source 1 - Web / Social
- **CMMC/FAR managed compliance - existing row, timing changed not dead.** Web search found recent CMMC Phase 2 suspension coverage. ITPro reported the July 13, 2026 pause of the C3PAO requirement, but self-assessments, SPRS scoring, annual affirmations, NIST 800-171 obligations, and False Claims Act risk remain live. SBA estimated CMMC certification costs can reach about **$593.8K** for small firms needing third-party certification and **$388.6K** for self-assessment-eligible firms. **Why it matters:** tailwind shifts from "assessment deadline scramble" to "evidence-backed compliance liability management." Keep, but re-score urgency.
- **Luxury circularity / authentication / repair - potential new or Berkshire-proxy expansion, adjacent to jewelry and high-value assets.** Web results showed ongoing luxury resale, repair, authentication, and jewelry/watch repair signals: The Fashion Law covered Worthy/CIRCA fine jewelry and watch marketplace merger above **$100M** implied value; market-report snippets estimate luxury authentication at **$1.81B in 2026**, growing to **$4.22B by 2035** at **9.7% CAGR**. **Why it matters:** better G&B fit may be back-end authentication, repair, refurbishment, documentation, and lifecycle services, not owning retail brands.
- **Insurance M&A - existing rows reinforced.** Deloitte/PwC/MarshBerry sources point to broker consolidation and continued insurance distribution demand, but this is broad and already mapped to specialty insurance, HNW personal lines, trade credit/customs/cargo brokerage, SIU, and jeweler's block.
- **Diagnostics:** `last30days` ran for "private equity acquisitions small business services 2026" with Reddit/HN/Polymarket. Reddit returned **403**, X/YouTube unavailable, Polymarket no data, and only one HN item appeared; output is low-confidence and used only as a source-gap diagnostic. Web search supplemented successfully.

### Source 2 - Gmail Newsletters
- **Title insurance / title agency - potential watchlist, not net-new tracker add yet.** Acquiring Minds profiled Randy Rempp buying **Meridian Title**, a **$30M+** acquisition. Pre-close company averaged about **$30M revenue** and **$2-3M EBITDA**; COVID temporarily lifted EBITDA to about **$8M**; purchase price was roughly **$30-31M** at about **6x normalized EBITDA**, funded with **$14M senior debt**, **$13M investor equity**, and **$4M+ seller note**. **Why it matters:** title agencies have repeat service revenue, cash flow, fragmented competition, and insurance adjacency, but housing cyclicality is material. Could be an adjacent read-through to property closing services, not necessarily G&B's next lane.
- **Trades operator-growth infrastructure - existing/local-services reinforcement.** This Week in ETA described an HVAC company moving from **$220K EBITDA to $1M+ EBITDA in 14 months** with process/people/technology and a 12-week HVAC/plumbing accelerator. Also noted a residential sprinkler investment. **Why it matters:** validates process lift in trades, but HVAC/plumbing are not current G&B differentiated lanes; fire/sprinkler may reinforce fire/life safety.
- **PE Hub business-services activity - existing row reinforcement.** PE Hub noted Broad Sky grew Smith + Howard **4x** before TPG exit, citing durable tax/audit advisory; also flagged Saber Power Services, Facility Grid/PingCx commissioning, healthcare workforce services, and AI services. **Why it matters:** confirms sponsor appetite for essential compliance/admin/services, but most are too PE-visible or software-heavy.
- **Diagnostics:** subscription label returned **45** threads; industry-research label returned **5** XPX threads, mostly owner/exit-planning community content with limited direct niche signal.

### Source 3 - Granola Calls
- **Legacy fine jewelry / Sidney Garber - deal-specific, not clean search niche.** Multiple calls from July 29-August 5 discussed a jewelry company at roughly **$18M revenue**, **$3.4M EBITDA** or about **18% margin**, and **$5.5M cash**. Upside: wholesale distribution, e-commerce, marketing, CRM, merchandising, Kay's luxury background. Concerns: no durable recurring revenue, retail/inventory risk, investor mixed/hard-pass signals, SBA personal guarantee risk, inventory valuation, channel mix not broken out.
- **Luxury back-end services - stronger thesis signal than retail brand ownership.** Calls repeatedly resurfaced specialty jewelry insurance, art/high-value storage, repairs, inventory in transit, and potential luxury holdco add-ons. **Why it matters:** maps to existing specialty insurance / storage rows and the Berkshire proxy inbox, with better recurring/sticky economics than a branded jewelry retailer.
- **maxRTE / BK Growth - diligence lesson, not niche add.** Carla Larin/maxRTE discussion emphasized customer concentration, lender selection, services vs software, team build, and long sales cycles. **Why it matters:** apply as diligence filter across all new niches, especially customer concentration and lender flexibility.
- **Diagnostics:** `~/.local/bin/granola-api` worked after UTC timestamp retry and returned **10** recent notes; direct notes matched vault-synced call notes.

### Source 4 - Gmail Deal Flow / Investors
- **Insurance-driven contents restoration - existing row, strong reinforcement.** Axial surfaced a South Atlantic contents restoration specialist with about **$5.5M LTM revenue**, **$2.5M LTM EBITDA**, about **44% EBITDA margin**, pack-out, inventory, off-site cleaning, climate-controlled storage, and pack-back. Insurance-funded channel and remediation-contractor referrals route work without competitive bidding. **Why it matters:** this is exactly the existing contents restoration row and materially validates margin and channel quality.
- **Commercial property damage recovery / restoration - existing adjacent reinforcement.** Axial "Regional Building Services Platform" showed about **$6M revenue**, **$2M EBITDA**, roughly **40% margin**, water/fire/mold/storm/trauma/reconstruction, multi-office Southeast platform, carrier-valued one-provider claims handling, rollover openness. **Why it matters:** reinforces restoration/building-services platform economics, but broader reconstruction may be more construction-heavy than the cleaner contents niche.
- **Local-services bundle from SMB Deal Hunter - mostly park, with two useful wedges.** Relevant data: HOA painting contractor **$7.1M revenue / $1.4M EBITDA** with Florida reserve-law tailwind; stormwater pond management **$1.62M revenue / $732K EBITDA** with compliance permit obligations; roadside locksmith **$2.25M revenue / $427K EBITDA** with AAA relationships and NASTF access; auto collision **$2.2M revenue / $900K EBITDA**; express car wash membership **$850K revenue / $375K EBITDA**; home staging **$1.9M revenue / $642K EBITDA**; salon-suite leasing **$1.2M revenue / $429K EBITDA** at **95-100% occupancy**. **Why it matters:** stormwater/HOA reserve compliance may deserve future property-compliance clustering; car wash/locksmith/auto/body/staging/salon are useful market data but not Deal 1 lanes.
- **Business services outsourcing - potential new watchlist but AI-disruption risk.** Calder listed a Mid-South B2B go-to-market outsourcing company with **$3.27M EBITDA**, CRM optimization, data/lead generation, marketing execution, appointment setting, sales support, 100% onshore remote model, VP-led bench with 13-year average tenure. **Why it matters:** recurring managed-team revenue and succession fit, but AI/substitution risk is high.
- **Clinical research center - potential watchlist, healthcare/regulatory but likely low G&B edge.** Everingham & Kerr listed a Florida Phase II-IV clinical research center with **$1M revenue** and **>$350K normalized cash flow**, endocrinology/internal medicine trials. **Why it matters:** recurring sponsor/site workflow possible, but clinical PI dependence and healthcare specialization are concerns.
- **Fire alarm / low-voltage / cabling - existing fire/life safety reinforcement.** SMB Deal Hunter listed a TX fire alarm security company with every customer under contract and **$1M revenue / $500K EBITDA**, plus cabling infrastructure with Siemens/Honeywell partnerships, **$1.5M revenue / $500K EBITDA**, and data-center projects paying **25-30%** above standard rates. **Why it matters:** reinforces fire/life safety and premium technical infrastructure maintenance.
- **Investor signal: Anacapa AI update.** Anacapa cited 30+ PE firms discussing AI adoption; only **10%** reported high-ROI AI projects in more than half their portfolio companies. Buyers are diligencing AI adoption and discounting laggards. **Why it matters:** treat AI adoption/readiness as diligence/value-creation lens, not a niche by itself.
- **Diagnostics:** deal-flow label returned **50** threads; investor label returned **8**. A few broker/marketing bodies were snippet-limited or noisy, but key deal bodies decoded.

### Source 5 - Vault Research
- **2026-08-07 thesis scan explicitly queued Berkshire/luxury recurring-model proxy cluster and CMMC re-screen.** This is the strongest internal instruction for Monday: test insurance/protection, regulated communications, customs/trade compliance, premium rental infrastructure, technical distribution, retail display lifecycle, art framing supply chain, and luxury circularity as business-model proxies.
- **2026-08-04 Niche Intelligence added/validated CMMC, contents restoration, and vegetation management.** Recent external and email signals mostly reinforce these rather than create net-new rows.
- **2026-07-28 Niche Intelligence already added broker-dealer compliance / outsourced FinOp and outsourced insurance SIU.** Current insurance and compliance signals should not duplicate them unless new evidence changes score/channel.

### Source 6 - Passive Inbox Signals Since Last Tuesday
- **Berkshire and luxury recurring-model proxy cluster - process this cycle.** `brain/inbox/2026-08-06-niche-signal-berkshire-luxury-recurring-models.md` is the only in-window `topic/niche-signal` passive item since Tuesday. It is high-value because it starts from business-model mechanics: renewal revenue, compliance urgency, trade complexity, rental contracts, technical distribution, installed-base service, retail display lifecycle, art framing supply, repair/refurbishment/authentication/documentation.
- **Legacy jewelry brand inbox note - in 14-day vault window but not since last Tuesday passive bucket.** It should be treated as deal-specific pressure test plus a prompt to map jewelry-adjacent infrastructure, not as proof that legacy jewelry retail belongs in WEEKLY REVIEW.

### Industries / Companies Mentioned
Meridian Title; Sidney Garber; Chenmark jewelry-store precedent; Worthy; CIRCA Jewels; maxRTE; Smith + Howard; TPG; Saber Power Services; Facility Grid; PingCx; Hoppers Hauling; Everingham & Kerr; Calder Capital; Axial; SMB Deal Hunter; Anacapa; PE Hub; Acquisition Lab; Entrepreneurial Capital.

### Data Points for Scoring
Contents restoration **$5.5M revenue / $2.5M EBITDA / 44% margin**; building damage recovery **$6M revenue / $2M EBITDA / 40% margin**; jewelry company **$18M revenue / $3.4M EBITDA / 18% margin / $5.5M cash**; title company precedent **$30M revenue / $2-3M normalized EBITDA / ~6x purchase**; stormwater **$1.62M revenue / $732K EBITDA**; HOA painting **$7.1M revenue / $1.4M EBITDA**; fire alarm **$1M revenue / $500K EBITDA**; cabling **$1.5M revenue / $500K EBITDA**; clinical research **$1M revenue / >$350K cash flow**; business-services outsourcing **$3.27M EBITDA**; luxury authentication market snippets **$1.81B 2026 to $4.22B 2035 / 9.7% CAGR**; CMMC small-firm compliance cost estimates **$388.6K-$593.8K**.

### Net RECENT Judgment
Strongest new-to-this-cycle signal is not a single new row; it is the **Berkshire/luxury recurring-model proxy expansion**. Best candidates for synthesizer expansion: luxury authentication/repair/documentation, specialty jewelry insurance and claims workflows, art/high-value-asset storage, customs/trade compliance for specialty goods, premium rental/display lifecycle infrastructure, and technical distribution/service. Strongest duplicate reinforcement: **contents restoration**, **fire/life safety**, **CMMC/FAR compliance**, **specialty insurance**, and **property compliance/stormwater/HOA reserve-adjacent services**.

→ READY

---
## [niche-intel-scorer] — 2026-08-10 22:51 ET
**Source:** Step 4 SCORE using G&B INDUSTRY scorecard only; inputs from identifier, one-pager, `scorecard-structure.md`, and `brain/context/learnings.md`
**Status:** complete

### Final Industry Score

**Stormwater Control Measure Inspection, Maintenance, and Compliance O&M for HOAs, multifamily, retail centers, and commercial campuses**

- **Weighted score:** **2.52 / 3.0 (84%)**
- **Status:** **New - Pending Review**
- **Initial Screen:** PASS on all four gates
  - Margins: PASS / validate. Service-heavy O&M should clear 15% EBITDA; SMB Deal Hunter comp was about $1.62M revenue / $732K EBITDA (~45%), likely unusually strong but validates margin ceiling.
  - Recurring / reoccurring revenue: PASS. Monthly/quarterly/annual inspection, maintenance, reporting, cleaning, and corrective repair cycles tied to permits, HOA/commercial obligations, and violation avoidance.
  - Industry growth: PASS. U.S. stormwater market sources cite ~7.8%-8.72% CAGR; maintenance contracting source cites ~6.7% CAGR.
  - Growth TAM: PASS. U.S. stormwater management market estimated ~$7.0B-$8.25B in 2025; global maintenance contracting estimated $7.4B in 2024.

### Detailed Industry Scorecard Summary

- **Growth, penetration & catalyst:** 3.00 / 3.0. Strong regulatory and climate/flood-resilience tailwinds; MS4/NPDES maintenance obligations and HOA/commercial liability create a durable catalyst.
- **Size & fragmentation:** 2.00 / 3.0. Likely hundreds of qualified providers after filters, but PE platform activity is already visible.
- **Industry economics:** 2.00 / 3.0. Margins likely good when service-heavy, but vacuum trucks, dredging, sediment removal, repair work, and field labor can reduce asset-light quality.
- **Mission criticality:** 2.67 / 3.0. Clear value proposition and violation/flood-risk avoidance; switching costs are moderate rather than high.
- **Exogenous risks:** 2.40 / 3.0. Low technology/trend risk; moderate regulatory variation, liability, and property-cycle exposure.
- **Porter’s Five Forces:** 2.17 / 3.0. Low VC threat, but meaningful competition from local contractors, consultants, landscapers, engineers, facilities vendors, and PE platforms.
- **Value creation:** 2.50 / 3.0. Strong professionalization levers: route density, inspection/reporting software, asset inventories, property-manager channels, recurring PM contracts, repair pull-through, and add-ons.
- **Impact/externalities:** 3.00 / 3.0. Positive flood mitigation, water-quality, and infrastructure-maintenance externalities.

### Deliverables

- **Scorecard local path:** `/tmp/stormwater-control-measure-o-and-m-scorecard.xlsx`
- **Scorecard Drive file:** `1cpVwJ324-oKKW5mm3QidQBvwVT_FNJir`
- **Scorecard Drive link:** https://docs.google.com/spreadsheets/d/1cpVwJ324-oKKW5mm3QidQBvwVT_FNJir/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **Updated one-pager local path:** `/tmp/stormwater-control-measure-o-and-m-onepager.pptx`
- **Updated one-pager Drive file:** `1kfh6tDiH0QHpcTuE0ymAC0iv_eWf5vW7`
- **Updated one-pager Drive link:** https://docs.google.com/presentation/d/1kfh6tDiH0QHpcTuE0ymAC0iv_eWf5vW7/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- **Folder verification:** Drive folder `1YWvgpkdYQ5BDoUWmjVXSMglitObIcQ9t` contains exactly one PPTX and one XLSX after replacement/upload.
- **One-pager update:** Assessment/Status row updated to `Assessment: 2.52 / 3.0 (84%)` and `Status: New - Pending Review`; Sources slide preserved.

### Tracker-Ready Row Values

- **Margins:** PASS / likely 15%+; validate service-heavy scope and equipment intensity.
- **Recurring Revenue:** PASS; monthly/quarterly/annual inspection, maintenance, reporting, cleaning, and repair cycles.
- **AI Defensibility:** Medium-high. AI can improve reporting, routing, asset inventories, and compliance documentation, but field inspection/maintenance is physical and locally delivered.
- **Right to Win (G&B):** Medium. Strong property-compliance / trust-and-verification fit; lower personal luxury/network edge than HNW/luxury-adjacent theses.
- **Network Access:** Medium. Guillermo/property-services adjacency plus HOA/property-compliance lanes; needs river-guide validation through CAI, stormwater associations, property managers, and regional operators.
- **Target Pool:** 100-250 likely independent potential targets; validate 50+ service-heavy firms at $750K-$3M EBITDA after excluding construction-heavy, engineering, landscaping, municipal-heavy, and PE-backed platforms.
- **QSBS:** Indeterminate. Likely service business; QSBS eligibility depends on entity structure, C-corp status, active business tests, and excluded-service interpretation. Requires tax/legal review.
- **Recommended next validation:** Promote only after target-density proof: 50+ independent, service-heavy SCM/BMP O&M providers with recurring private-property relationships and acceptable equipment intensity.

→ READY

---
## [niche-intel-historical] — 2026-08-10 23:43 ET
**Source:** historical calls, Gmail history, tracker state, diagnostics for unavailable OneNote/ChatGPT
**Status:** complete

### Consolidated Historical Report By Niche

#### Premium pest / specialty pest for luxury, commercial, and specialty environments
- **Sources appeared:** calls with Jay Davis, Sara Rosenthal, Guillermo Lavergne, Doug Tudor, NPMA Women's Forum notes; Gmail NPMA/event and broker-flow signals.
- **Lifecycle status:** LIVE / already tracked as `Premium Pest Management (Luxury Hospitality & Commercial Properties)` and under active outreach. Do not duplicate.
- **Key intelligence:** Broad pest is crowded and expensive; Jay Davis explicitly said generic pest is hard for a searcher because majors and PE-backed platforms can outbid, while bird control, rat-only, aquatic weed management, mosquito, and other narrower wedges can trade below the majors' radar. Sara Rosenthal framed the real wedge as ICP, not subtype: luxury/high-discretion clients want premium, branded, discreet service rather than "extermination." Guillermo call validated a NYC operator with ~$1.5M revenue, ~$500K EBITDA, 98% retention, Cartier via Richemont referral, Chelsea Market/Google clients, higher visit frequency, photo-reporting trap software, and underpricing upside. Melissa model note captured 40% labor COGS and acquisition-cohort modeling. NPMA Women's Forum is a confirmed network surface.
- **People/contacts:** Jay Davis; Sara Rosenthal; Guillermo Lavergne; Albert Kim; Paul at Potomac; Melissa Rosenblatt; NPMA Women's Forum contacts.
- **Why overlooked:** It may have looked like a generic PE-hot pest roll-up until repeated calls narrowed it to luxury/discretion, women-led relationships, and specialty/premium routes.

#### HNW / fine-art / collectibles insurance brokerage and carve-outs
- **Sources appeared:** August Felker calls, Hunter Hartwell call, Jeremy Black call, Warren Chan call, Deloitte Art & Finance conference email/call context, Gmail insurance queries.
- **Lifecycle status:** LIVE but already tracked across `Specialty Insurance Brokerage (Art & Collectibles)`, `HNW Personal Lines Concierge Insurance Brokerage`, and jewelry/block insurance child wedge. Do not create a new row unless re-scoped to a carve-out.
- **Key intelligence:** August validated a women-run HNW personal-lines brokerage target near retirement and said HNW personal lines are extremely sticky with near-100% renewal behavior; wealth transfer and climate pricing are demand tailwinds. Deloitte Art & Finance signal: 80% of family offices/wealth managers asked to manage hard assets; protection/insurance is first priority. Bank of America art services team recommended 4 large + 3 small specialty brokerages. Hunter provided the critical negative lifecycle: specialty brokerages often trade at 12x-14x EBITDA and his search came up empty; carve-outs may be more realistic than buying a whole firm. Warren confirmed art-world credibility and Anacapa network value but did not create immediate deal flow.
- **People/contacts:** August Felker; Hunter Hartwell; Jonathan Crystal potential intro; Warren Chan; Bank of America Art Services contact; Art Basel strategy contact.
- **Why overlooked:** Positive source volume is high, but economics and QSBS/multiple concerns repeatedly demoted it. The overlooked live angle is not "buy an insurance brokerage"; it is carve-outs, smaller personal-lines brokers, or high-touch independents reacting against PE roll-ups.

#### Trade credit, customs bonds, cargo insurance, and trade-risk brokerage
- **Sources appeared:** Jeremy Black email/thread, Camilla calls on 2026-02-09 and 2026-02-17, tracker `Domestic Trade Credit Insurance` tabled, tracker `Trade Credit, Customs Bonds & Cargo Insurance Brokerage` live/new.
- **Lifecycle status:** LIVE as unified trade-risk brokerage; tabled/killed precursor should not be revived standalone.
- **Key intelligence:** Camilla found continuous bond premiums of ~$500-$2,000 annually, cargo commissions of 10%-20%, and importer target profile of $10M-$200M import value. She also flagged fragmentation but credit/liability risk. Jeremy signal: trade credit may be normal in some industries rather than underutilized, so demand thesis must segment by vertical. Tracker notes now show bundled cross-sell fixing the old unit-econ concern: 20%-35% EBITDA, 90%+ retention, 7%-8% CAGR, 200-500 trade-credit specialists plus 3,000 CBP customs brokers, with 100-200 tristate prospects.
- **People/contacts:** Jeremy Black; Camilla de Sanna; Kay's brother as logistics/import context.
- **Why overlooked:** It was previously split into separate customs/cargo/trade-credit lanes and killed/tabled for no right-to-win or thin economics; combined trade-risk brokerage is the stronger formulation.

#### Jewelry brand / luxury jewelry manufacturing, wholesale, and adjacent services
- **Sources appeared:** Andrew Freiman, Jackie Hirsch, WSN group, Guillermo 2026-07-31, Jeremy Black heat-transfer/manufacturing call, Gmail/broker flow around manufacturing/distribution.
- **Lifecycle status:** LIVE opportunity, but not a normal niche-intel row unless converted into a services/picks-and-shovels thesis. Current lead is deal-specific.
- **Key intelligence:** The live jewelry company is roughly $18M revenue / $3.4M EBITDA; diligence questions are channel mix, e-commerce vs. wholesale vs. physical retail, inventory, charity treatment, working cash, and whether a ~3x EBITDA IOI is viable. Jackie and Andrew both validated that luxury/manufacturing positioning is credible for Kay. Historical heat-transfer apparel label company was $3.2M revenue, long-lived, made-to-order, strong reoccurring customers, and about 30%-40% custom/recurring design work, but investor appetite for non-recurring manufacturing was a concern.
- **People/contacts:** Andrew Freiman; Jackie Hirsch; Guillermo Lavergne; WSN group; jewelry founder/broker unnamed in call notes.
- **Why overlooked:** It sits outside the classic B2B recurring-services screen. Treat as deal-led exception or use it to mine dull jewelry/fashion infrastructure such as repair, testing, packaging validation, compliance, or wholesale ops.

#### Marine/yacht services, boat transport, and marina-adjacent operations
- **Sources appeared:** Doug Tudor call, Mike Horowitz call, tracker rows for boat/yacht transport and yacht property management.
- **Lifecycle status:** LIVE/WATCH, already tracked in `Asset-Light Boat and Yacht Transport Coordination` and `Yacht Property Management`; do not duplicate.
- **Key intelligence:** Doug observed a fragmented ecosystem around marinas: maintenance, detailing, repair, provisioning, parts, upholstery. His strongest idea was boat transport/shipping, analogized to car moving, with PE-backed players, good margins, and strong exit multiples. Mike independently noted Kay's domain credibility: yacht clubs growing up, brother in marine shipping/logistics, marina/private-club software interest, and boat shrink-wrapping recently acquired by a holding-company buyer. Main concern: mom-and-pop fragmentation and seasonality make platform scale hard, especially outside Florida/Southern California.
- **People/contacts:** Doug Tudor; Mike Horowitz; Kay's brother.
- **Why overlooked:** It sounded too lifestyle/seasonal until reframed as asset-light coordination, transport brokerage, or recurring yacht stewardship.

#### Luxury amenity management and premium physical security integration
- **Sources appeared:** Mike Horowitz call; tracker rows for luxury amenity management and premium physical security.
- **Lifecycle status:** LIVE/WATCH, already tracked.
- **Key intelligence:** Mike called amenity management the most compelling new idea from that session. Arch Amenity Group manages 20,000+ sq ft amenity packages; tailwinds include post-COVID commercial landlords adding tenant amenities and trophy HQ buildouts. Premium physical security for luxury retail was also surfaced: escalating theft, security-driven store design, recurring testing/reconfiguration/maintenance, and 5-7 year store renovation cycles. Both need proof of independent target pool and margin/revenue mix.
- **People/contacts:** Mike Horowitz.
- **Why overlooked:** These were embedded inside a broad luxury-retail vendor brainstorm; downstream rows exist, but historical context shows why Arch/premium-security comps matter.

#### Specialty facility cleaning: medical/lab/IVF/GMP, not luxury boutique
- **Sources appeared:** Guillermo brainstorm, Gmail deal flow, tracker row for `Medical/Lab/IVF Specialty Cleaning`.
- **Lifecycle status:** LIVE/WATCH, already tracked.
- **Key intelligence:** Guillermo/Kay ruled out luxury boutique cleaning because national players dominate; medical/lab/IVF clinic cleaning was flagged as genuinely differentiated. Tracker now scopes it to healthcare/lab/cleanroom/GMP specialty cleaning, with 50-150+ possible targets if broadened beyond IVF. Needs validation of target density and margin premium.
- **People/contacts:** Guillermo Lavergne; Camilla/Kay internal.
- **Why overlooked:** It was initially tangled with commercial cleaning and luxury boutiques; the compliance/infection-control wedge is the actual signal.

#### Apparel/fashion supply-chain compliance, testing, certification, and logistics
- **Sources appeared:** Guillermo brainstorm, Camilla licensing/software calls, Kay fashion/manufacturing call history.
- **Lifecycle status:** PARTLY DEAD / partly already tracked through beauty/fragrance/package testing and MoCRA 3PL. Apparel supply-chain services broadly were killed in Guillermo brainstorm due to low fashion margins and weak third-party willingness to pay.
- **Key intelligence:** Positive signal: thread count, cashmere claims, fire retardancy, customs compliance, paperwork accuracy, and warehousing/logistics stability. Negative signal: Chanel kept compliance in-house for confidentiality; fashion margins are chronically challenged; third-party services may lack budget. This should not advance as "fashion compliance" without narrowing to regulated product testing or customs/trade-risk workflows.
- **People/contacts:** Guillermo Lavergne; Camilla de Sanna; Kay's Chanel/fashion network.
- **Why overlooked:** Strong Kay right-to-win but weak customer willingness-to-pay; only picks-and-shovels with mandated testing/documentation deserve more work.

#### Geotechnical engineering / construction materials testing
- **Sources appeared:** Gmail E&K acquisition opportunity 2026-06-25; tracker row.
- **Lifecycle status:** LIVE/WATCH, already tracked.
- **Key intelligence:** E&K teaser: NJ geotechnical engineering services company, over $3.6M revenue, approximately $1M normalized EBITDA, consulting through geotechnical investigations plus construction materials testing/inspection, operating mainly NJ/PA/DE. Tracker already notes ~$9B geotech TAM, ~$2B materials-testing TAM, 3%-6% growth, and need to validate 50+ acquirable regional firms plus repeat-revenue quality.
- **People/contacts:** Everingham & Kerr source only; no warm relationship identified.
- **Why overlooked:** Came through generic broker flow, but it is one of the few deal-flow items with concrete buy-box scale and infrastructure/QA adjacency.

#### Truck licensing / IFTA / IRP / DOT compliance
- **Sources appeared:** Gmail SMB Deal Hunter 2026-05-26; tracker row.
- **Lifecycle status:** LIVE/WATCH, already tracked but single-source caveat.
- **Key intelligence:** Listed CA remote business: $1.039M revenue, $412K EBITDA, $1.425M asking price, established 2021. Handles federal/state registrations, business formations, drug/alcohol testing programs, truck plates, driver qualification docs, annual filings, same-day filings, and compliance tracking. Recurring by regulatory cycle, but tracker correctly flags single-source signal, no documented network access, and TAM extrapolation.
- **People/contacts:** Helen Guo / SMB Deal Hunter.
- **Why overlooked:** Looks small and single-source, but it is a clean example of mandated SMB compliance services.

#### Dead / do-not-resurface lanes from historical context
- **Art storage as real-estate-heavy storage:** proposed repeatedly, then challenged by Camilla/Doug/Kay; moved on because margins in practice looked low (~8% in one call), owners wanted real estate value, and economics were not service-clean. Current `Storage & Related Services for High Value Assets` survives only as ops/AI or services/logistics rescope.
- **Luxury collectibles/authentication / art advisory / collection software:** Warren/Guillermo/Killed tab show no actionable sizeable target, key-person risk, AI disruption or startup/software dynamics. Private art advisory is explicitly killed per Kay.
- **Women’s health/fertility:** Guillermo brainstorm killed most sub-sectors as too early-stage, regulatory environment unfavorable, and fertility already searched by others.
- **Fashion/apparel supply-chain services broadly:** killed unless narrowed to mandated testing/documentation/logistics.
- **General compliance e-learning / workplace safety eLearning:** killed in tracker despite prior high score; do not advance without Kay-specific reversal.

### Missing-Source Diagnostics
- **OneNote SEARCH FUND notebook:** No OneNote MCP/tools are available in this Codex session, so `hist-onenote` could not be mined. Gap documented; not treated as blocker.
- **ChatGPT export:** `~/Downloads/031aafe3.../selected_business_conversations.json` was not present; `/home/ubuntu/Downloads` does not exist and broader `/home/ubuntu` search found no selected-business export. Gap documented.
- **Granola:** `~/.local/bin/granola-api` works, but exposes `since`/`get-note` and returned recent updated notes only. Historical Granola coverage was taken from synced `brain/calls/*.md` notes with `source: granola`; no separate older Granola-only backfill was available.
- **Gmail:** Required historical searches were run read-only with `--gmail-no-send` using this install's positional query syntax. Relevant threads were read selectively; many broker/newsletter results were promotional or already reflected in tracker rows.

→ READY

---
## [niche-intel-synthesizer] — 2026-08-10 22:38 EDT
**Source:** synthesis of RECENT + HISTORICAL posts, `brain/context/learnings.md`, live WEEKLY REVIEW / IDEATION / KILLED / TABLED tracker tabs  
**Status:** complete

### 1. Cross-Source Signal Matrix

| Niche/Industry | RECENT Sources | HISTORICAL Sources | Total Source Count | Strength |
|---|---|---|---:|---|
| Luxury/high-value-asset insurance brokerage, HNW personal lines, jeweler's block | web, granola, vault, passive | calls, email | 5 | VERY STRONG |
| Insurance-driven contents restoration / property damage recovery | gmail deal flow, vault | email adjacent | 2.5 | STRONG |
| CMMC/FAR managed compliance for SMB federal contractors | web, vault | tracker history | 2 | STRONG |
| Luxury authentication, repair, refurbishment, documentation | web, granola, passive | calls | 4 | VERY STRONG |
| Trade credit/customs bonds/cargo insurance brokerage | vault/passive | calls, email | 3 | STRONG |
| Fire/life safety inspection, low-voltage, fire-pump/hydrant MRO | gmail deal flow/newsletter | tracker/calls | 2.5 | STRONG |
| Premium pest / specialty pest for luxury/commercial | tracker context | calls, email | 3 | STRONG |
| Yacht/marine stewardship and transport coordination | passive | calls | 2 | STRONG |
| Specialty facility cleaning: medical/lab/IVF/GMP | newsletter/deal-flow adjacent | calls/email | 2 | STRONG |
| Beauty/fragrance packaging, testing, 3PL/kitting | vault/passive | calls | 2 | STRONG |
| Title agency / closing services | newsletter | none | 1 + quant | MODERATE |
| HOA reserve/property compliance: stormwater, reserve studies, LL97 | gmail deal flow | tracker/history | 2 | STRONG |
| Geotechnical / construction materials testing | deal flow | email | 2 + quant | STRONG |
| Business-services outsourcing / GTM BPO | gmail deal flow | killed/BPO history | 1 + quant | MODERATE |

### 2. Named Company Registry

Attio diagnostic: no safe Attio lookup was run; the prompt's `.env | grep ATTIO_API_KEY` pattern would expose local secret handling risk. Routing below uses vault and live tracker cross-reference; Attio remains a gap for the next CRM-safe agent.

| Company Name | Niche | Source | Independence / Scale | Outreach Flag | Warm Contact | Notes |
|---|---|---|---|---|---|---|
| Sidney Garber | legacy jewelry brand | Granola/calls | ~$18M rev / $3.4M EBITDA | ACTIVE_DEAL | Brooke Garber Neidich | Vault entity says Active Deals / Financials Received; do not add outreach. |
| Meridian Title | title agency | newsletter | $30M+ acquisition precedent | VAULT_UNKNOWN | none | Sourced fact: acquisition precedent; not target without housing cyclicality screen. |
| Worthy / CIRCA Jewels | luxury resale/authentication comp | web | merged, >$100M implied value | COMP_ONLY | none | Sourced fact: validates authentication/resale complexity, not outreach target. |
| Smith + Howard | tax/audit advisory comp | PE Hub | scaled 4x before TPG exit | COMP_ONLY | none | Sponsor appetite proof; likely too large/PE-visible. |
| Saber Power Services | power services comp | PE Hub | PE activity | COMP_ONLY | none | Infrastructure-service comp only. |
| Facility Grid / PingCx | commissioning/customer-experience comp | PE Hub | PE activity | COMP_ONLY | none | Comp for commissioning/compliance workflows. |
| Hoppers Hauling | local services comp | newsletter | HVAC growth case | COMP_ONLY | none | Trades process-lift proof; not a priority G&B lane. |
| Everingham & Kerr | broker/source | deal flow | existing vault broker entity | VAULT_HISTORY | Joe Vanore/source only | Source repeatedly appears in vault; use for broker intelligence, not outreach target. |
| Calder Capital | broker/source | deal flow | existing vault broker entity | VAULT_HISTORY | broker channel | Source of B2B outsourcing lead; not target. |
| NEIS | premium audit/loss control | historical/vault | family-owned since 1945 | VAULT_HISTORY | Jeremy/Hunter adjacency | Prior target-discovery target; route via existing insurance infrastructure context. |
| Trade Acceptance Group | trade credit brokerage | historical/vault | independent candidate | WARM_INTRO | Jeremy Black | Existing vault target; warm intro route, not cold. |
| Texel / Meridian | trade credit/cargo | historical/vault | acquired | COMP_ONLY | Jeremy Black history | Acquired; exit validation, not target. |
| Arch Amenity Group | amenity management comp | calls/tracker | large player | COMP_ONLY | Mike Horowitz | Comp for luxury amenity management. |
| IntelliGreen Partners | LL97 compliance | tracker/vault | WBE named target | VAULT_HISTORY | none named | Existing energy-compliance row; target already identified. |

### 3. Contact-to-Niche Map

| Contact | Warmth | Niches They Can Help With | What to Ask | Last Contact |
|---|---|---|---|---|
| August Felker | HOT/WARM | HNW personal lines, art/collectibles insurance | Current independent brokers/carve-out angles | historical 4mo stale |
| Hunter Hartwell | WARM | insurance brokerage economics | Reality-check multiples/carve-outs | historical |
| Jeremy Black | HOT | trade credit/customs/cargo, insurance infrastructure | Intro to Trade Acceptance / vertical demand segmentation | historical |
| Camilla de Sanna | HOT/internal | trade-risk economics, compliance screens | Validate unit economics/QSBS risks | Feb 2026/history |
| Warren Chan | WARM | art world, luxury services, Anacapa | Credibility checks and service-provider map | historical/recent |
| Mike Horowitz | WARM | yacht/marine, amenity mgmt, luxury security | Target-density and operator intros | 2026-06-22 |
| Doug Tudor | WARM | pest, yacht/marina ops | Specialty wedge and buyer competition filter | historical |
| Sara Rosenthal | WARM | premium pest/luxury service positioning | ICP and messaging validation | historical |
| Guillermo Lavergne | HOT | HOA/property services, jewelry deal pressure test | Domain calls and investor lens | recent/history |
| Andrew Freiman / Jackie Hirsch | WARM | jewelry/luxury manufacturing credibility | Brand/operator diligence reads | recent |

### 4. Lead Lifecycle Tracker

| Niche/Strategy | Proposed By | When | Challenged By | When | Reason | Status |
|---|---|---|---|---|---|---|
| Art storage as real-estate-heavy storage | multiple calls | historical | Camilla/Doug/Kay | historical | Capital intensity, 5-8% EBITDA, owners price real estate | DEAD except services-only rescope |
| Private art advisory / collection software | Warren/Guillermo/history | historical | Kay/Killed tab | 2026-06-18 | Key-person, small TAM, no actionable target | KILLED |
| Broad fashion/apparel supply-chain services | Guillermo/Camilla | historical | Kay/investor logic | historical | Low margins, in-house confidentiality, weak WTP | DEAD unless mandated testing/docs |
| Jewelry brand ownership | live deal/calls | recent | investors/working-capital screen | recent | No durable recurring revenue; inventory/retail risk | LIVE as deal-specific exception |
| Domestic trade credit standalone | Jeremy/Camilla | Mar-May | tracker | 2026-04 | Thin pool/QSBS/no RTW | TABLED; LIVE only as bundled trade-risk brokerage |
| Workplace/compliance eLearning generic | IDEATION/history | historical | KILLED tab | 2026-03/05 | Consolidated/no edge; later OSHA carve-out debated | KILLED unless Kay reverses |
| Luxury watch repair standalone | family call | historical | learnings | historical | Embedded inside retailers, not acquirable standalone | DEAD |
| CMMC/FAR compliance | recent web/vault | 2026-08 | policy timing | 2026-07 pause | Certification pause changes urgency, not obligation | LIVE / re-score timing |

### 5. Picks-and-Shovels / Edge-Niche Expansion

| Umbrella Theme | Growth Trend | Operational Complexity Created | Obvious Niches | Picks-and-Shovels / Edge Niches | Compliance / Risk Niches | Target-Density Clues | G&B Fit |
|---|---|---|---|---|---|---|---|
| Luxury/high-value assets | More resale, inheritance, insurance, circularity | Authenticity, condition, custody, repair history, claims evidence | jewelry brands, art dealers, resale marketplaces | authentication ops, repair/refurbishment coordinators, appraisal/documentation bureaus, inventory-in-transit logistics | jeweler's block, HNW property, claims documentation, provenance QA | Worthy/CIRCA, BofA broker list, specialty broker rows | Strong |
| Insurance/property loss | Carrier pressure + outsourced claims workflows | Pack-out, inventory, restoration, storage, referral coordination | restoration contractors | contents-only pack-out, climate-controlled contents cleaning, inventory tech-enabled service teams | carrier panel compliance, SIU/fraud, loss control | Axial deals at 40-44% EBITDA; 100-300 tracker pool | Strong |
| Federal/regulatory compliance | CMMC/FAR obligations remain despite pause | Evidence collection, affirmations, SPRS scoring, liability documentation | cyber MSPs | managed evidence/documentation services for SMB contractors, audit-prep retainers | False Claims Act risk, NIST 800-171 controls | 75-250 boutiques in tracker | Medium-Strong |
| Beauty/luxury CPG | MoCRA, launches, sampling, e-commerce returns | Lot traceability, kitting, package validation, allergen/docs | beauty brands, packaging suppliers | specialized beauty 3PL/kitting, package testing, formulation/testing labs, sampling fulfillment | FDA/MoCRA/IFRA docs, QA, claims substantiation | A2LA/package/testing rows; 40-100 3PL estimate | Strong if service-only |
| Property/compliance | LL97, Surfside, HOA reserve laws, stormwater permits | Mandated studies, reporting, inspections, recurring board obligations | property managers, contractors | reserve study firms, stormwater permit O&M, energy benchmarking boutiques | FISP/LL97, reserve studies, stormwater compliance | CAI, named NY/NJ firms, stormwater deal at $732K EBITDA | Medium-Strong |
| Marine/HNW stewardship | Yacht ownership/professionalization | Maintenance scheduling, transport, captain/vendor coordination | marinas, yacht brokers | asset-light transport coordination, yacht property management, shrink-wrap/service scheduling | insurance/liability/compliance logs | Doug/Mike signals; 75-250 transport estimate | Medium |

Answer to required question: the money-makers are the vendors who absorb documentation, coordination, compliance, repair, testing, logistics, and claims complexity created by growth in visible luxury/property/beauty/insurance end-markets.

### 6. Convergence Report: Top Signals for Identifier

1. **Luxury/high-value-asset protection infrastructure.** Sourced fact: this appears across web, calls, vault, passive inbox, and historical insurance work; inference: the better G&B lane is not retail jewelry or art storage, but authentication, repair/refurbishment coordination, documentation, specialty insurance, and claims workflows. Test service vendors first where Kay's luxury credibility opens doors and recurring/reoccurring risk-management work exists.
2. **Insurance-driven contents restoration and property-loss services.** Sourced fact: recent deal flow showed contents restoration at ~$5.5M revenue / ~$2.5M EBITDA and broader property damage recovery at ~$6M / ~$2M EBITDA. Inference: contents-only pack-out/inventory/cleaning/storage is cleaner than reconstruction because insurance-funded referrals and documentation complexity create stickier, less bid-driven work.
3. **Beauty/fragrance compliance infrastructure.** Sourced fact: tracker already has MoCRA beauty 3PL, package testing, product testing, packaging, and fragrance distribution rows; passive Berkshire proxy reinforces the same second-order thesis. Inference: identify only one non-duplicative edge niche, likely beauty regulatory documentation + kitting/lot-traceability service providers or package-testing labs, not brands or generic 3PL.
4. **Trade-risk brokerage bundle.** Sourced fact: Jeremy + Camilla + tracker convergence supports bundled trade credit, customs bonds, and cargo insurance with high retention; lifecycle warning: standalone customs/cargo was killed/tabled for no RTW and thin economics. Identifier may advance only the bundled brokerage thesis and should route via Jeremy/warm network, not cold.
5. **Property compliance services.** Sourced fact: LL97, reserve studies, stormwater, HOA reserve laws, and geotech/CMT all recur across tracker and recent deal flow. Inference: the strongest new angle is not broad property management, but mandated inspection/study/reporting vendors where operational complexity is legal/regulatory and target density can be proven through associations/directories.

Missing-source diagnostics to carry forward: OneNote and ChatGPT export were unavailable to the historical gatherer; Attio was not queried by synthesizer due unsafe secret-access pattern. These gaps should reduce confidence, not block identification.

→ READY
---
## [niche-intel-identifier] — 2026-08-11 00:42 ET
**Source:** Step 2 IDENTIFY + INDUSTRY VALIDATION from synthesizer outputs, `brain/context/learnings.md`, live WEEKLY REVIEW / IDEATION / KILLED / TABLED duplicate check, and web validation
**Status:** complete

### Candidate 1

- **Niche Name:** Stormwater Control Measure Inspection, Maintenance, and Compliance O&M for HOAs, multifamily, retail centers, and commercial campuses
- **Umbrella Theme:** Trust, Compliance & Verification / property-compliance infrastructure
- **Growth Trend / Tailwind:** More urban flooding, water-quality enforcement, MS4/NPDES maintenance obligations, HOA reserve/maintenance accountability, and green-infrastructure adoption.
- **Operational Complexity Created:** Property owners and boards must keep detention ponds, underground systems, bioswales, drains, and BMP/SCM assets functional, inspected, documented, and violation-free across monthly/quarterly/annual cycles.
- **Why This Is Picks-and-Shovels / Edge:** This is not buying property management, HOA management, landscaping, engineering design, or construction. It is the recurring service vendor that inspects, cleans, documents, repairs, and coordinates compliance for installed stormwater assets.
- **Thesis:** Stormwater O&M looks like a dull, regulatory, repeat-service property infrastructure niche with local fragmentation and increasing penalty risk. It benefits from the same HOA/property compliance tailwinds already appearing in the tracker, but targets specialized maintenance contractors rather than reserve-study engineers, HOA managers, environmental sampling firms, or broad facilities services.
- **Source Signal:** Synthesizer property/compliance row; recent SMB Deal Hunter stormwater pond management deal at about $1.62M revenue / $732K EBITDA; recent web validation of dedicated stormwater O&M providers and PE platform activity.
- **Independent Validation:** U.S. stormwater management market sources estimate 2025 market sizes around $7.0B-$8.25B with 7.8%-8.72% CAGR; stormwater maintenance contracting source estimates global $7.4B in 2024 growing 6.7% CAGR to $13.1B by 2033. ASCE notes NPDES/MS4 permits require maintenance plans, and HOA/commercial guidance describes third-party inspection, reporting, and maintenance cycles. PE validation: Warren Equity invested in Dragonfly Pond Works in Aug. 2024; Dragonfly has 6 add-ons; AQUALIS was sold by DFW to Fusion Capital in 2026; Apex acquired SWIMS in California; Silver Peak bought StormWater Pros.
- **Duplicate Check:** Checked live WEEKLY REVIEW, IDEATION, KILLED, TABLED. Distinct from `HOA / Community Association Management` (manager, not stormwater vendor), `Reserve Study & Building Engineering Studies` (study/engineering cycle, not O&M), `Building Energy & Emissions Compliance Services` (energy laws), `Environmental Field Sampling & Compliance Services` (samples/reports, not infrastructure maintenance), `Facilities Management / Commercial Building Services` (broad building services), and `Permit Expediting` (project filings). No semantic duplicate found.
- **Key Question:** Is there a 50+ pool of independently owned, service-heavy stormwater O&M firms at or near $750K-$3M EBITDA after excluding landscaping add-ons, engineering firms, construction-heavy erosion control, and PE-backed platforms?
- **Preliminary Fit Assessment:** Meets B2B, compliance-driven, recurring/reoccurring, fragmented, asset-light if scoped to inspection/maintenance/coordination, and 15%+ EBITDA likely in strong operators. Needs validation on fleet/equipment intensity, customer concentration, and whether PE platforms have already made the best regional independents expensive.

**INITIAL SCREEN**
- **Margins:** PASS / validate. Deal-flow comp implies ~45% EBITDA, likely unusually strong; service-heavy O&M should clear 15% if not construction-heavy.
- **Recurring/Reoccurring Revenue:** PASS. Monthly/quarterly/annual inspection, maintenance, reporting, and repair cycles; permits and HOA obligations create repeat behavior.
- **Industry Growth:** PASS. U.S. stormwater market reported at 7.8%-8.72% CAGR; maintenance contracting at 6.7% CAGR.
- **Growth TAM:** PASS. Multi-billion stormwater and O&M market; growth tied to urbanization, climate/flood events, aging infrastructure, water-quality regulation, and green infrastructure.

**TARGET TAM**
- **Total Firms:** Initial estimate 300-800 U.S. stormwater maintenance / pond management / SCM inspection providers after excluding pure civil engineering and generic landscaping; directory evidence shows many regional certified-maintenance and contractor lists.
- **Independently Owned / Potential Targets:** Initial estimate 100-250; likely concentrated in Southeast, Mid-Atlantic, Texas, California, Colorado, and high-growth stormwater-regulated metros.
- **Already PE-Backed / Acquired:** Dragonfly Pond Works / Warren Equity, AQUALIS / DFW then Fusion, StormWater Pros / Silver Peak, SWIMS / Apex, CWES / Rockwood add-ons.
- **PE Consolidation Risk:** Medium and rising. Platform activity validates exit but requires going below platform radar and avoiding exact geographies where Dragonfly/AQUALIS/Apex are active.
- **5 Named Examples:** Dragonfly Pond Works, AQUALIS, Storm Water Inspection & Maintenance Services (SWIMS), StormWater Pros, Storm Water Compliance Inc. (SWC).

**MARKET TAM**
- **Market Size:** U.S. stormwater management estimates: ~$6.98B-$8.25B in 2025; global maintenance contracting: $7.4B in 2024.
- **CAGR:** U.S. market 7.8%-8.72%; maintenance contracting 6.7%.
- **Key Demand Drivers:** NPDES/MS4 maintenance-plan requirements, HOA/commercial property liability, urban flooding, aging detention/pond assets, green infrastructure, fines/violations, and insurer/property-owner pressure to prevent water damage.

Sources used for validation: SNS Insider U.S. stormwater market; Yahoo/BlueWeave U.S. stormwater market; Growth Market Reports stormwater maintenance contracting; ASCE stormwater infrastructure; Warren Equity Dragonfly; Fusion/AQUALIS; Apex/SWIMS; Silver Peak/StormWater Pros; Dragonfly and AQUALIS service pages.

→ READY

---
## [niche-intel-onepager] — 2026-08-10 22:46 EDT
**Source:** Step 3 ONE-PAGER for Stormwater Control Measure Inspection, Maintenance, and Compliance O&M for HOAs, Multifamily, Retail Centers, and Commercial Campuses
**Status:** complete

### Deliverable Created
- Drive folder ID: `1YWvgpkdYQ5BDoUWmjVXSMglitObIcQ9t`
- Drive folder link: https://drive.google.com/drive/folders/1YWvgpkdYQ5BDoUWmjVXSMglitObIcQ9t
- One-pager file ID: `1kfh6tDiH0QHpcTuE0ymAC0iv_eWf5vW7`
- One-pager link: https://docs.google.com/presentation/d/1kfh6tDiH0QHpcTuE0ymAC0iv_eWf5vW7/edit?usp=drivesdk&ouid=108110832334532716154&rtpof=true&sd=true
- Local path: `/tmp/stormwater-control-measure-o-and-m-onepager.pptx`
- Template cloned from: `brain/library/internal/one-pager-template/customs-bonds-template.pptx`

### Pre-Flight / Duplicate Check
- Checked WEEKLY REVIEW parent `1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT`; no exact stormwater niche folder existed.
- Checked Drive search for `Stormwater Control Measure Inspection Maintenance Compliance`, `stormwater control measure`, `stormwater`, and `pond management`.
- No exact or clear variant folder/one-pager was found, so a new WEEKLY REVIEW folder was created.
- Post-upload folder verification shows exactly one PPTX in the niche folder.

### One-Pager Notes
- Assessment left as `Pending Scoring`.
- Status left as `Pending Scoring`.
- Added a dedicated `Sources` slide because the template table has no source row.
- Sources slide contains live hyperlinks for all external and internal sources used.

### Key Source List
- `brain/traces/agents/2026-08-10-niche-intelligence.md` - identifier output, SMB Deal Hunter stormwater comp, duplicate context, synthesized thesis.
- SNS Insider U.S. stormwater management market: https://www.snsinsider.com/reports/stormwater-management-market-3051
- Growth Market Reports stormwater maintenance contracting market: https://growthmarketreports.com/report/stormwater-maintenance-contracting-market
- ASCE stormwater infrastructure / MS4 maintenance plans: https://infrastructurereportcard.org/cat-item/stormwater-infrastructure/
- EPA stormwater maintenance guidance: https://www.epa.gov/npdes/stormwater-maintenance
- BMPClean national stormwater maintenance directory: https://www.bmpclean.org/
- AUE Land HOA stormwater compliance documentation: https://aueland.com/hoa-stormwater
- Warren Equity / Dragonfly Pond Works: https://warrenequity.com/portfolios/dragonfly-pond-works/
- Dragonfly Pond Works services: https://www.dragonflypondworks.com/
- DFW / Fusion sale of AQUALIS: https://dfwcapital.com/dfw-completes-sale-of-aqualis-to-fusion-capital-partners/
- AQUALIS inspections and compliance services: https://aqualisco.com/service/stormwater-management/stormwater-services/stormwater-inspections/
- Apex / SWIMS acquisition: https://apexcos.com/press-release/apex-acquires-storm-water-inspection-maintenance-services-inc/
- Silver Peak / StormWater Pros: https://www.foxfin.com/news/stormwater-pros

→ READY

---
## [niche-intel-tracker] — 2026-08-11 01:08 ET
**Source:** Step 5 UPDATE to Industry Research Tracker `WEEKLY REVIEW`
**Status:** complete

### Tracker Update Confirmation
- Pre-write live tab snapshot saved to `/tmp/niche-intel-2026-08-10-weekly-review-before.json`.
- Added `Stormwater Control Measure Inspection, Maintenance, and Compliance O&M for HOAs, Multifamily, Retail Centers, and Commercial Campuses` to `WEEKLY REVIEW`.
- Google Sheets append returned updated range: `'WEEKLY REVIEW'!A49:K49`.
- Post-write verification re-read `WEEKLY REVIEW` and confirmed the niche appears exactly once.
- Determined row: 49.
- Rank: 46.
- Status: `New - Pending Review`.

→ READY

## [01:14] orchestrator
All mandatory steps completed. Final markdown report and JSON sidecar written; wrapper integrity validator passed for 2026-08-10.
→ CLOSE
