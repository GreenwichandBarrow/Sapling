---
schema_version: 1.1.0
date: 2026-09-07
type: trace
tags: [date/2026-09-07, trace, topic/niche-intelligence, status/completed]
task: Monday full Niche Intelligence scheduled run
agents: [niche-intel-recent, niche-intel-historical, niche-intel-synthesizer, niche-intel-identifier, niche-intel-onepager, niche-intel-scorer, niche-intel-tracker]
status: completed
output: "[[outputs/2026-09-07-niche-intelligence-report]]"
run_mode: monday
runtime: Codex/systemd
---

# Agent Chatroom: Niche Intelligence

## Coordination Log

## [22:31] orchestrator
Starting headless Monday full run under Codex/systemd. Mandatory sequence is SKILL.md, 1Password credential resolution, chatroom creation, parallel RECENT + HISTORICAL gather, sequential synthesis, identification, one-pagers, industry scoring, tracker update, report, then JSON sidecar.
→ READY

## [Recovery] orchestrator
Supervised recovery for operating date 2026-09-07. Prior initialization preserved. Credentials resolved via op-env.sh. No external notifications, activation, channel changes, or outreach. Final report will be [[outputs/2026-09-07-niche-intelligence-report]].
→ READY

---
## [hist-calls] — 2026-09-08 recovery for 2026-09-07
**Source:** Historical vault calls + live older Granola
**Status:** partial

### Signals Found
- Screened 186 pre-Aug25 vault calls; selected relevant bodies read in depth. Live Granola returned 10 records, 3 historical; fetched all 3. Not full historical API coverage.
- **Hypothesis:** jewelry production QA/incoming inspection/vendor-documentation services: [[calls/2026-08-18-brooke-garber-neidich-sidney-garber]] and [live source](https://notes.granola.ai/d/a52d727e-6be6-4d11-88bb-2224c48bd24b) report factory concentration, repeated design leakage and every-piece incoming QC. No dedicated target or TAM; must distinguish from rejected apparel outsourcing and tracked aftercare.
- **Hypothesis:** trash-chute/compactor cleaning for dense properties: operator add-on explicitly mentioned in [[calls/2026-06-17-guillermo-lavergne-brainstorm]]. No margin/target proof; distinct scope requires validation against broad property cleaning.
- Women’s health including pelvic floor rejected in June17 after April/May exploration because early/subscale pool. New clinic growth does not establish administrative vendor pool.
- Preserve lifecycle: pest now TABLED; coffee/art advisory KILLED; authentication parked; apparel outsourcing rejected. Existing jewelry deal [[entities/sydney-garber]] had investor hard passes and remains deal-specific, not generic niche validation.

### Industries/Companies Mentioned
- [[entities/sydney-garber]], [[entities/guillermo-lavergne]], [[entities/camilla-de-sanna]], [[entities/matt-luczyk]], [[entities/august-felker]]. Exact named-company/other-contact detail and historical source paths in specialist handoff.

### Data Points for Scoring
- Single pest target historical ~$1.5M revenue/$500K EBITDA/98% retention, not industry-wide. Single jewelry brand owner reported $18.5M revenue/$3.3M EBITDA, not QA-service TAM. No validated numeric floors for either new edge hypothesis.
- Detailed handoff: `/tmp/niche-intel-2026-09-07-historical/hist-calls.md`.

**READY**
---

---
## [niche-intel-recent / RECENT] — 2026-09-09T00:09:46.087140+00:00
**Source:** six recent buckets, operating window 2026-08-25 through 2026-09-07
**Status:** partial (Reddit unavailable; all six buckets attempted)

## RECENT evidence, operating date 2026-09-07

Coverage: all six buckets attempted. Gmail live searches returned 31 newsletter threads (Aug31 onward), 10 industry-research (7 within Aug25-Sep7), 63 deal-flow (50 within), 10 investor (8 within). 96 unique in-window threads fetched and decoded text/plain or HTML. Thread search uses inclusive midnight behavior, so Aug24 messages excluded at extraction; messages after Sep7 excluded. No pagination remaining. Initial documented CLI --query flag unsupported; corrected to positional query and succeeded. HTML fallback initially lacked bs4; stdlib parser succeeded. Granola live returned 7 notes, 6 within window fetched with transcript and summary; Sep8 excluded. Vault: 4 outputs, 7 call files (6 unique calls, one duplicate team sync), 1 inbox item (budget, not niche). No recent niche inbox items; older signals belong HISTORICAL.

### Source 1 web/social
Eight last30days query-plan runs covered three mandatory broad questions plus five live active lanes. Reddit returned 403 on all (repeated attempt once); HN returned 28 raw items across queries, mostly irrelevant lexical matches; Polymarket 0. Two broad HN PE stories concern unsold assets and apartment neglect; no quantified niche discovery. Exclude Sep8/9 content from engine current-clock range. Web supplements found the following primary releases:
- Truvant acquired Multi-Pak Packaging, Aug25. Beauty/wellness/VMS/OTC contract packaging; 180,000 sq ft; probiotic cold-chain center; founded by John and Debbie Culligan. Acquired company is NOT independent target supply. https://www.truvant.com/news/truvant-acquires-new-jersey-based-multi-pak-packaging-a-specialist-in-vitamins-supplements-and-otc
- Fort Point-backed AMS acquired Vox Fulfillment Sept3; 200,000+ sq ft Utah; beauty/wellness kitting, inventory, fulfillment, integrations. Confirms backend supplier demand and PE competition. https://fortpointcapital.com/news/ams-fulfillment-acquires-vox-fulfillment
- West Physics acquired Radiographic Testing Services, Albany NY (announcement Sept2; company post Sept3). Medical imaging testing / CRESO outsourced safety/compliance. Acquired target is exit comp, not available independent. https://westphysics.com/west-physics-announces-acquisition-of-radiographic-testing-services-inc/
- Aon announced USI agreement Aug31, $17B; scale consolidator, not HNW target supply. https://aon.mediaroom.com/2026-08-31-Aon-to-acquire-USI-to-establish-the-premier-U-S-middle-market-platform
- Brown & Brown MacKay acquisition Sept7 includes HNW cover; UK-only PE heat context. https://us.bbrown.com/blog/brown-brown-acquires-mackay-corporate-insurance-brokers
Estate management current search returned no strong dated niche signal; fine-art logistics/storage results mostly pre-window or Sept8 and excluded. Sept7 Fine Art Shippers holiday post is not intelligence.

### Source 2 newsletters
PE Hub Sept4 thread 1a06d28dccc6d169 independently surfaces the SAME AMS/Vox and West Physics events (do not count newsletter + release as independent events). Other source claims: CVC investment Unitex, healthcare textile management serving 5,000 facilities; M|C Partners/DivergeIT MSP platform; Blackstone/DarkVision asset-integrity inspection; Bridgepoint/VIPR insurance bordereaux handling; Broad Sky/Smith+Howard tax/audit. These are supplier/control-process signals, not proof of SMB margins or available targets.
Amboy Street Aug26 thread 1a03f2e9df864a43: investor-reported Origin pelvic-floor/MSK record visits, new payer partner, CA/TX expansion; Aunt Flow national commercial agreement; Alloy retention/margin growth with no values; Hey Jane billing specialist and revenue-ops recruitment. Hypotheses: specialty clinic billing/credentialing; recurring restroom menstrual-product replenishment; clinical equipment safety/QA. VC portfolio companies are market signals, not SMB acquisition candidates. Public links: https://www.theoriginway.com/2026-state-of-pelvic-health-report ; https://goauntflow.com/ ; https://www.amboystreet.vc/portfolio
SBA newsletter discussion is seller/newsletter claim only; no regulatory recommendation or legal conclusion made in this gather.

### Source 3 Granola
Six live notes retrieved. Sept3 Tank Track discussion: operator reports zero churn post-close, only 2-3 suitable software targets, narrow search, trade-magazine sourcing. Software is already acquired; process lesson, not new approved thesis. https://notes.granola.ai/d/2f7feff5-5915-4a0e-8df8-13aa46c73db3
Aug28 Brooke call: jewelry factory QA issue, inventory scan/conversion and valuation pain. Aug31 Camilla sync: no manufacturer contracts confirmed, specialized jewelry inventory diligence gap, weak inventory-turn visibility, wholesale concentration; after-sales interest. These are DIRECT operating-workflow evidence for luxury inventory verification / QA / aftercare hypotheses. No growth TAM demonstrated. SG is active deal; no new-target classification. https://notes.granola.ai/d/9ad6563f-c783-478c-98d6-6defae2e3d38 ; https://notes.granola.ai/d/8edd1384-f7b6-4ee7-b794-dc6e888ecc76
Aug25 Guillermo/Aug27 Jeff calls: capital structure and inventory-heavy cyclicality; no independent new niche. Named known relationship contacts: Brooke Garber Neidich, Camilla de Sanna, Jeff Stevens, Guillermo Lavergne; retain existing CRM lifecycle. Rohit/Austin Tank Track are group-session contacts, no assumed warm intro.

### Source 4 deal flow
- E&K beauty/fragrance/skincare strategic BUYER mandate Sep3 thread 1a068689b4068dc4 repeats Aug28 thread 1a049435c3413b67. One signal, NOT seller business or independent convergence; no buyer name/TAM. Reinforces beauty infrastructure alongside AMS/Vox and Truvant/Multi-Pak.
- E&K managed cyber NJ Aug26 thread 1a04014c8203457c: broker claims ~$2M revenue, ~$350K normalized EBITDA (17.5% arithmetic), all ARR; SOC/email-security platform. Separate New England MSP thread 1a03ed0c3a7fbfdb: $1.8M revenue/$850K normalized EBITDA, 100 municipal/SMB clients, recurring MSP/maintenance. Listing-specific, not industry-wide margins. Overlap existing CMMC lane must be checked.
- E&K pediatric NJ Aug25 thread 1a03a873fb944677: $1M revenue; 30+ years reputation; psychology/speech/OT/evaluations, NJDOE-approved school contracts and IEE demand. School-funded evaluation/admin complexity is an edge hypothesis; exact target count and margins missing.
- Business Exits Aug25 thread 1a039de867dae84c: actual recently closed TX home-health staffing ($1.05M), SE electrical contractor ($3M). Saleability only. Aerospace distribution and vocational-school listings present, not chosen solely because sale.
- Other blasts: NEMT, plumbing emergency repair, property management, chauffeur/carwash, niche publication, ecommerce/retail. No automatic kills or status moves.

### Source 5 vault outputs/calls
Aug28 and Sep4 thesis-scan outputs repeat underlying Gmail signals; not independent evidence. Sep4 wrongly framed beauty buyer thread as fresh since Sep3; Aug28 live email corrects lifecycle. Budget outputs add no niche signal. Seven call files include duplicate Aug31 team sync; six distinct calls.

### Source 6 passive signals
No Aug25-Sep7 niche-signal inbox records; Aug28 only budget trigger. Nothing marked processed.

### Discovery handoff
Strong broad themes: Beauty/wellness infrastructure (two independent supplier acquisitions plus investor update and buyer mandate); Trust/compliance (cyber listing + platform deals; medical physics acquisition); Luxury/heritage stewardship (direct factory QA/inventory pain; already tracked aftercare). Family/education child-services is one broker signal, not validated convergence. Potential edge universe for synthesizer: primary VMS/beauty contract packaging; beauty returns/rework; outsourced radiation-safety/testing; specialist clinic billing; menstrual-product managed replenishment; jewelry inventory auditing/QA; school evaluation administration; managed cyber compliance. Existing beauty3PL/testing/packaging lanes are already tracked; avoid duplicates. Target-density, NAICS and workflow-map proofs delegated to synthesis/identifier; this gather makes no claims of independent target counts or proven Deal1 fit.

**READY:** RECENT gather complete; full evidence and diagnostics /tmp/niche-intel-2026-09-07-recent/.
---

---
## [HIST-EMAIL] — 2026-09-08 recovery for 2026-09-07
**Source:** Read-only historical Gmail
**Status:** partial

### Signals Found
- Executed five required bounded searches + two targeted, read 4 threads / 7 messages. Additional pages remain; no full-mailbox claim.
- [Aug24 PE Hub](https://mail.google.com/mail/u/0/#all/1a0344b1f5883c2c) explicitly reports 8 specialty-healthcare RCM deals and names major PE sponsors. Supports actual admin-vendor category; does not validate rehabilitation-specific target pool or economics; PE competition warning.
- [Aug19 E&K teaser](https://mail.google.com/mail/u/0/#all/1a01bd7b7605d215) lists an unnamed electrical testing/power reliability service company: planned/24x7 maintenance, relay calibration, arc-flash, thermography. Potential narrow installed-base edge distinct from construction; check broad equipment/SCADA overlaps.
- [Jeremy thread](https://mail.google.com/mail/u/0/#all/19c250d5143e6b7a) confirms tracked trade-risk brokerage; original FMO/IMO founder contact deceased, company sold long ago. No new contact lead.
- Targeted chute/compactor/jewelry-testing search returned 0; historical-call hypotheses have no email corroboration here.

### Data Points for Scoring
- Single electrical target: $6.1M revenue/$3.5M normalized EBITDA (~57.4%, unusually high, unverified broker claim); recurring amount unspecified. Not industry average.
- Jeremy reported $10–13K/year premiums, not broker revenue. GPO 86% title is undefined and not usable industry economics.
- Full evidence, named-company references and diagnostics: `/tmp/niche-intel-2026-09-07-historical/hist-email.md`.

**READY**
---

---
## [HIST-ONENOTE] — 2026-09-08 recovery for 2026-09-07
**Source:** OneNote capability discovery; bounded vault fallback
**Status:** no data (live OneNote)

### Signals Found
- Two tool-discovery attempts: no callable OneNote or generic tool-search capability. Zero live notebooks/sections/pages read; source unavailable, not empty.
- Template claims 16 sections but enumerates 17 labels; actual notebook topology unverified. Every named section marked unavailable in handoff.
- Source-coverage passages in [[outputs/2026-08-24-niche-intelligence-report]], [[outputs/2026-08-17-niche-intelligence-report]], [[outputs/2026-06-23-niche-intelligence-report]] confirm derivative fallback only. No independent source-count credit, no new niche asserted.
- Detailed handoff: `/tmp/niche-intel-2026-09-07-historical/hist-onenote.md`.

**READY**
---

---
## [HIST-CHATGPT] — 2026-09-08 recovery for 2026-09-07
**Source:** Raw-export discovery; memory fallback
**Status:** no data (raw export)

### Signals Found
- Expected Downloads absent; home-wide filename retry found no raw export. **0/16 original conversations read.** Four derivative memory files reviewed; no independent source-count credit.
- Historical summary identifies medical billing/coding and B2B women's-health support as 2024 explored lanes, but no viable foundational SaaS target found. Old 28/30 score is unsupported historical model output, not scoring evidence.
- Love Transfers historical lead was passed and referred onward; art/storage/software and insurance references overlap established tracker context.
- Full coverage and lifecycle handoff: `/tmp/niche-intel-2026-09-07-historical/hist-chatgpt.md`; existing [[outputs/2026-08-24-niche-intelligence-report]] also documents prior export access gap.

**READY**
---

---
## [HISTORICAL] — Codex/systemd supervised recovery 2026-09-07
**Source:** historical calls, Gmail, OneNote availability audit, ChatGPT export availability audit
**Status:** partial source coverage; all four specialist roles finished

### Signals Found
- **Hypothesis: fine-jewelry production QA / supplier documentation.** Aug18 owner call establishes incoming QC, defects, supplier consolidation and tooling/IP pain. RECENT related same-deal QA evidence can reinforce operating pain, but is not independent proof of outsourced demand. Prior June17 apparel-outsourcing rejection (in-house/confidentiality economics) remains a material counterargument. Existing live jewelry deal must not enter target outreach.
- **Hypothesis: specialty rehabilitation revenue-cycle support.** Aug24 PE Hub email explicitly reports eight specialty healthcare RCM deals and names major sponsors; an actual vendor-category signal, with substantial PE heat. RECENT clinic expansion/billing hiring may support demand; rehab-specific independent target pool unproven. Historical June17 pelvic-floor clinic rejection remains in force.
- **Hypothesis: electrical testing/power reliability services.** Aug19 actual unnamed seller teaser describes maintenance, relay calibration, thermography, dielectric-fluid analysis and emergency service. Seller reports $6.1M revenue/$3.5M normalized EBITDA; exceptional margin is NOT an industry estimate. Semantic overlap with equipment maintenance/water SCADA must be checked.
- **Hypothesis: trash-chute/compactor sanitation.** June17 operator/investor call names add-on workflow; no historical email corroboration. Separate narrow installed-property workflow from tabled broad cleaning/pest only if target/economic evidence supports distinction.

### Coverage and safeguards
186 historical vault calls screened; three older live Granola notes fetched out of only ten endpoint records. Seven anchored Gmail queries returned 149 unique threads; four threads/seven messages read, six queries have further pages. OneNote unavailable after two discovery attempts: 0 live sections/pages. Raw ChatGPT export unavailable after two path searches: 0/16 conversations. Derivative summaries carry no independent-source credit. Live tracker read by headers: 42 WEEKLY REVIEW, 37 IDEATION, 44 KILLED, 21 TABLED names. Four specialist roles executed sequentially in one reused child thread because new thread spawn was rejected at platform limit. No notifications, tracker writes, activation or outreach.

Detailed evidence and source URLs: `/tmp/niche-intel-2026-09-07-historical/consolidated.md` and `hist-{calls,email,onenote,chatgpt}.md`. Source call crosslinks: [[calls/2026-08-18-brooke-garber-neidich-sidney-garber]], [[calls/2026-06-17-guillermo-lavergne-brainstorm]].
→ READY

## [HISTORICAL-PREPARATION] — Codex/systemd 2026-09-07
Live Drive Industry Research parent verified: WEEKLY REVIEW (`1eq7FjekjFhkV0RoBfgr9n6AXPtENEenT`), IDEATION, TABLED, KILLED, DRAFTS and SAMPLE; no ACTIVE SPRINTS folder. Both master template Drive IDs healthy; local one-pager and scorecard open with python-pptx/openpyxl. Industry template has eight weighted groups totaling 100%, rows8–43; rows45+ are unrelated stale company scorecard examples. SWITCH array formulas and blank supplier-power D34 need explicit handling in derived workbook. No LibreOffice/soffice executable available, so formula caches/recalculation verification must use an alternative and be reported accurately. Existing `scripts/build_truck_licensing_onepager.py` formatting helpers can be adapted, but script includes stale thesis data and should not run unchanged.
→ READY

---
## [niche-intel-synthesizer] — 2026-09-09T00:17:50.665364+00:00
**Source:** RECENT + HISTORICAL, live tracker negative memory, read-only Attio
**Status:** complete synthesis with explicit coverage gaps

# Niche intelligence synthesis - 2026-09-07

Codex/systemd supervised recovery. Hypotheses for industry validation, not activation decisions. Live-state dedup is current recovery state, not an as-of reconstruction.

## 1. Cross-Source Signal Matrix

| Niche | RECENT | HISTORICAL | Independent count | Strength | Caveat |
|---|---|---|---:|---|---|
| Beauty fulfillment / primary packaging / compliance | E&K buyer mandate; AMS/Vox; Truvant/Multi-Pak | Existing lanes only | 3 | STRONG | 3 independent events; separate niches not individually validated |
| Specialty rehabilitation revenue-cycle services | Amboy portfolio clinic expansion + billing hiring | Aug24 specialty RCM deal newsletter | 2 | STRONG | Macro/vendor convergence; rehab vendor pool unverified |
| Fine-jewelry QA / inventory verification | Brooke Aug28 + Camilla Aug31 same deal | Brooke Aug18 same deal | 1.5 | MODERATE | One deal, multiple participants; NOT independent market validation |
| Managed cyber/compliance services | 2 E&K distinct teasers; DivergeIT platform | Existing/tabled IT and active CMMC | 2 | STRONG | Same broker discounted; semantic duplicate constraints |
| Medical physics / outsourced radiation safety | West Physics/RTS event (release+newsletter once) | No independent historical corroboration | 1 | MODERATE | Named acquired supplier, not acquirable count |
| Electrical testing / power reliability | Energy/inspection PE activity adjacent, not same niche | Aug19 named-services unnamed seller | 1 | MODERATE | Only exact-niche seller signal credited |
| Healthcare textile management | Unitex investment newsletter | None | 1 | MODERATE | 5000 customer facilities is NOT target count |
| Menstrual-product replenishment | Aunt Flow commercial agreement investor newsletter | None | 1 | WEAK | Demand thesis only |
| Pediatric independent evaluations / school administration | E&K $1M practice seller teaser | None | 1 | MODERATE | Practice sale is not proof of admin service firms |
| Trash chute / compactor sanitation | None | June17 call mention | 1 | WEAK | Tabled pest/cleaning adjacency |
| Specialty/HNW insurance / trade-risk brokerage | Aon/USI; MacKay | Jeremy broker referrals; existing tracker | 3 | STRONG | Tracked; no fresh mandate |
| Fine art logistics/storage | No eligible fresh change | Acumen/Hangman prior deal lessons | 1.5 | MODERATE | Tracked with capital intensity counterevidence |
| Estate / property management | Property listing; no fresh estate signal | Existing tracker | 1 | MODERATE | Tracked |
| Septic software | Tank Track group session | None | 1 | MODERATE | Operating lesson; acquired software not new niche |
| Jewelry/luxury aftercare | Aug31 explicit interest | Existing aftercare lane | 1 | WEAK | Existing lane; no duplicate |
| Power conversion / aerospace distribution | PE newsletter and sale listing | None | 1 | MODERATE | Product-heavy; no service niche validated |
| Asset integrity inspections | DarkVision newsletter | None | 1 | WEAK | Platform comp; narrow pool unverified |
| Tax/audit / QoE services | Smith+Howard PE; acquisition newsletters | None | 1 | WEAK | General professional-service context |
| Bordereaux / insurance administration | VIPR newsletter | Existing back-office/trade-risk themes | 1 | MODERATE | Software comp, not authorization |
| Hotel CRM / booking support | Edita newsletter | None | 1 | WEAK | Software category, prior constraints |
| NEMT / home-health staffing | Business Exits and deal newsletter | None | 1.5 | MODERATE | Buyer/seller anecdotes; no verified niche growth |
| Chauffeur / carwash / plumbing | Deal newsletters | Prior tabled/killed adjacency | 1 | MODERATE | No strong Kay-specific edge |
| Ecommerce / retail / publications | Deal blasts | Existing exclusions | 1 | WEAK | No nomination; not automatic sheet kill |

Same event in release, newsletter and vault copy counts once. Same active-deal owner/team history receives 1.5 contextual credits, never two independent markets. OneNote and raw ChatGPT unavailable: zero source credits.

## 2. Named Company Registry

Attio read-only company queries completed; exact-name filtering rejects Aon/Aone and USI substring false positives. Active Deals list read; list membership alone does not imply live commercial stage. Unverified companies are not labeled NEW_TARGET or eligible for outreach. Source assertions, not audited financials; revenue left unknown rather than inferred.

| Company | Source | Independence | Routing flag | Location |
|---|---|---|---|---|
| [[entities/sidney-garber|Sidney Garber]] | RECENT primary release / newsletter | Independence unverified | ACTIVE_DEAL | Not validated |
| [[entities/tank-track|Tank Track]] | RECENT primary release / newsletter | Acquired; comp only | VAULT_HISTORY | Not validated |
| [[entities/truvant|Truvant]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/multi-pak|Multi-Pak]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | West Caldwell, NJ |
| [[entities/ams-fulfillment|AMS Fulfillment]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | IN_CRM | Not validated |
| [[entities/vox-fulfillment|Vox Fulfillment]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Provo, UT |
| [[entities/west-physics|West Physics]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Atlanta, GA |
| [[entities/radiographic-testing-services|Radiographic Testing Services]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Albany, NY |
| [[entities/origin|Origin]] | RECENT primary release / newsletter | Venture portfolio signal; not proven SMB target | UNVERIFIED_TARGET | Not validated |
| [[entities/aunt-flow|Aunt Flow]] | RECENT primary release / newsletter | Venture portfolio signal; not proven SMB target | UNVERIFIED_TARGET | Not validated |
| [[entities/alloy|Alloy]] | RECENT primary release / newsletter | Venture portfolio signal; not proven SMB target | VAULT_HISTORY | Not validated |
| [[entities/hey-jane|Hey Jane]] | RECENT primary release / newsletter | Venture portfolio signal; not proven SMB target | UNVERIFIED_TARGET | Not validated |
| [[entities/unitex|Unitex]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/divergeit|DivergeIT]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/darkvision|DarkVision]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/vipr|VIPR]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/smith-howard|Smith + Howard]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/kering|Kering]] | HISTORICAL calls/email | Strategic/platform context; not independent supply | VAULT_HISTORY | Not validated |
| [[entities/boucheron|Boucheron]] | HISTORICAL calls/email | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/trade-risk-group|Trade Risk Group]] | HISTORICAL calls/email | Independence unverified | VAULT_HISTORY | Not validated |
| [[entities/trade-acceptance-group|Trade Acceptance Group]] | HISTORICAL calls/email | Independence unverified | VAULT_HISTORY | Not validated |
| [[entities/texel|Texel]] | HISTORICAL calls/email | Independence unverified | VAULT_HISTORY | Not validated |
| [[entities/allianz-trade|Allianz Trade]] | HISTORICAL calls/email | Independence unverified | VAULT_HISTORY | Not validated |
| [[entities/atradius|Atradius]] | HISTORICAL calls/email | Independence unverified | VAULT_HISTORY | Not validated |
| [[entities/coface|Coface]] | HISTORICAL calls/email | Independence unverified | VAULT_HISTORY | Not validated |
| [[entities/acumen-fine-art-logistics|Acumen]] | HISTORICAL calls/email | Existing prior deal; lifecycle restrictions retained | ACTIVE_DEAL | Not validated |
| [[entities/hangman|Hangman]] | HISTORICAL calls/email | Existing prior deal; lifecycle restrictions retained | ACTIVE_DEAL | Not validated |
| [[entities/momart|Momart]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/aon|Aon]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/usi|USI]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/mackay|MacKay]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/lincoln-investment|Lincoln Investment]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/cordoba|Cordoba]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/queue-it|Queue-It]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/edita|Edita]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/carrot|Carrot]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/epc-power|EPC Power]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/airswift|Airswift]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/new-tech-global|New Tech Global]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/greenarrow|GreenArrow]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/msl-electric|MSL Electric]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/lumberworld|Lumberworld]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/schatz-bearing|Schatz Bearing]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/stratedge|StratEdge]] | RECENT primary release / newsletter | Acquired; comp only | UNVERIFIED_TARGET | Not validated |
| [[entities/trident-solutions|Trident Solutions]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |
| [[entities/nordic-bioscience|Nordic Bioscience]] | RECENT primary release / newsletter | Strategic/platform context; not independent supply | UNVERIFIED_TARGET | Not validated |

Unnamed seller firms (electrical reliability, two IT/cyber, pediatric practice) remain unnamed. Buyer identity in beauty mandate is undisclosed. Sponsors are contextual buyers, not target supply. Detailed CRM record evidence: /tmp/niche-intel-2026-09-07-company-crosscheck.json.

## 3. Contact-to-Niche Map

| Contact | Warmth / last evidence | Applicable expertise | Research question only |
|---|---|---|---|
| [[entities/brooke-garber-neidich|Brooke Garber Neidich]] | Active owner relationship; Aug28 | Jewelry manufacturing/inventory | Which QC and counting workflows are actually outsourced? |
| [[entities/camilla-de-sanna|Camilla de Sanna]] | Active internal; Aug31 | Luxury operations | Which recurring vendor spend is material? |
| [[entities/jeff-stevens|Jeff Stevens]] | Active investor; Aug27 | Capital structure / transition | What resilience funds the J curve? |
| [[entities/guillermo-lavergne|Guillermo Lavergne]] | Active investor; Aug25 | Niche/pest/network history | Does sanitation supplier differ from tabled pest? |
| [[entities/jeremy-black|Jeremy Black]] | Historical relationship; date not refreshed | Trade-risk ecosystem | Existing theme only, no new task |
| [[entities/carli-sapir|Carli Sapir]] | Newsletter subscriber evidence; warmth unverified Aug26 | Women health investor ecosystem | Who supplies independent clinics? |
| [[entities/rohit-tank-track|Rohit]] | Group-session exposure Sep3; no warm intro assumed | Vertical focus / retention | Process lessons only |
| [[entities/austin-tank-track|Austin]] | Group-session mention Sep3; no warm intro assumed | Vertical software operations | Process lessons only |

John/Debbie Culligan and Christina Pai are public source names only; no verified relationship or task. Historical Maria/Michael/Colleen first-name references are unresolved identities and not contact leads. No external questions sent.

## 4. Lead Lifecycle Tracker

| Theme | Proposal/evidence | Challenge | Current constraint |
|---|---|---|---|
| Jewelry QA | Aug18/Aug28/Aug31 same deal | June17 apparel in-house/confidentiality rationale | Hypothesis only; authentication/art advisory killed; aftercare tracked |
| Rehab billing | Aug24 RCM + Aug26 clinic growth | Women health clinics nascent; back-office SaaS tabled | Service scope may be distinct; not clinic revival |
| Electrical reliability | Aug19 seller | Equipment parent broad; fire/sign lanes killed Aug23 | Narrow test/calibration scope only |
| Trash/chute sanitation | June17 add-on idea | Pest/cleaning tabled Aug23 | No automatic revival; weak single source |
| Beauty supplier services | New supplier events | Existing packaging/3PL/testing rows | Refresh current rows; new scope only if distinct |
| Managed cyber | Two Aug26 teasers + platform | Broad IT tabled; CMMC active/new | Do not duplicate/activate |
| Trade risk | Jeremy referrals | Domestic trade credit tabled, small pool | Preserve live statuses; deceased founder not a lead |
| Software, coffee, art advisory, fire MRO, vegetation, auto repair | Historical mentions | Explicit killed tracker rows | No automatic re-entry |

## 5. Picks-and-Shovels / Edge-Niche Expansion

### Customer-environment map completed before final niche nomination

Environment: heritage fine-jewelry brand with external factories, wholesale distribution and own retail. Direct anchors: Aug18/Aug28 owner and Aug31 team calls. The following 50 recurrent workflow touchpoints are an analytical map; only source-described issues are observed facts, remaining operational steps are explicit hypotheses. They are not 50 verified outsourced services.

1. supplier onboarding
2. supplier ownership checks
3. vendor insurance review
4. manufacturer agreement renewal
5. tooling ownership records
6. design-file access control
7. design revision approvals
8. prototype approval
9. production capacity planning
10. material sourcing
11. metal purity documentation
12. stone provenance documentation
13. purchase order control
14. deposit reconciliation
15. foreign currency settlements
16. production milestone tracking
17. factory inspection coordination
18. incoming piece counts
19. incoming visual quality inspection
20. stone setting checks
21. clasp/function checks
22. weight/specification reconciliation
23. defect photography
24. defect returns authorization
25. local repair dispatch
26. repair cost allocation
27. lot/serial traceability
28. SKU catalog maintenance
29. inventory tagging
30. barcode scanning
31. cycle counts
32. annual physical inventory
33. inventory valuation reconciliation
34. slow-moving stock review
35. core versus bespoke turn analysis
36. wholesale consignment tracking
37. wholesale inventory reconciliation
38. retailer replenishment
39. trunk-show stock allocation
40. insured outbound shipping
41. customs documentation
42. inbound shipment insurance
43. display/vitrine installation
44. retail security checks
45. customer repair intake
46. warranty eligibility review
47. aftercare scheduling
48. product condition reporting
49. supplier performance scorekeeping
50. recall/defect escalation

| Umbrella | Trend | Complexity | Mainline | Edge vendors | Risk/compliance | Density evidence | G&B fit judgment |
|---|---|---|---|---|---|---|---|
| Beauty, Wellness & Longevity Infrastructure | Beauty/wellness brands expanding and outsourcing (two supplier acquisitions) | lot control, QA, packaging formats, returns and cold chain | Brands, clinics | primary supplement contract packaging; beauty returns/rework; specialty rehab billing | label QA / batch documentation | Acquired Multi-Pak and Vox prove supplier existence only; independent density pending | Medium; 3PL/packaging already tracked |
| Luxury, Heritage & Personal Goods | Heritage-brand distribution expansion in active deal; broader growth unproven | factory defects, supplier contracts, inventory turns and valuation | Jewelry brands/retailers | jewelry incoming QA; inventory verification; aftercare coordination | purity/provenance supplier documentation | Owner call proves pain; standalone vendors not yet counted | Strong contextual access; outsourcing and TAM unproved |
| Asset Protection & Stewardship | Large insurance consolidators growing; healthcare infrastructure investment | policy servicing, equipment safety and asset integrity | Brokers, imaging clinics | radiation-safety testing; power reliability maintenance; specialized asset inspection | outsourced RSO / periodic physics compliance | RTS comp and electrical seller prove categories; no independent count | Medium technical access; credential dependence |
| Family Wealth, Legacy & Life Infrastructure | School-service demand claimed by pediatric seller; clinic expansion investor-reported | evaluations, authorizations, school records, coordination | Therapy/education practices | specialty rehabilitation authorizations/billing; school-evaluation administration; menstrual replenishment | payer evidence / privacy / eligibility workflows | Single practice and venture examples; administrative target pool pending | Medium/uncertain; do not revive rejected clinic thesis |
| Trust, Compliance & Verification | Regulated operators outsource technical/evidence work | monitoring, reporting, equipment inspection, remediation records | MSPs, labs, contractors | medical physics testing; electrical relay/transformer testing; cyber evidence services; chute sanitation | audit readiness / chain of custody / scheduled inspections | Supplier transaction and seller evidence; directories still needed | Medium; avoid active CMMC, killed fire/sign lanes |

Expansion asks who earns revenue from complexity. Directory membership is not an independent acquisition count. Directory and taxonomy validation remain Step2 work. All five themes reviewed; 23 source-category clusters evaluated; 13 distinct edge scopes considered: primary packaging, beauty returns/rework, rehab billing, jewelry QA, jewelry inventory verification, aftercare coordination, radiation testing, electrical testing, asset inspection, school-evaluation admin, menstrual replenishment, cyber evidence, chute sanitation. No automatic kills: count removed by agent for no-tailwind/no-density/PE/revenue/searcher fit = 0 each. These reasons remain evidence flags; five preliminary scopes below, not five approved or validated niches.

## 6. Convergence Report

Ranking is analytical judgment of research priority; independent source count is one factor, novelty and overlap are others.

### 1. Specialty outpatient rehabilitation billing, authorizations and payer revenue-cycle services

Independent specialty-RCM transaction reporting and current clinic expansion/hiring suggest a necessary administrative supplier layer. Investigate outsourced rehab-specific vendors rather than the previously challenged venture clinic operators.

- Independent source count: 2.
- Lifecycle/overlap: Medical credentialing IDEATION; concierge back-office/healthcare SaaS TABLED. Separate full-service claim/authorization operations from credentialing-only or software.
- Unresolved: PE saturation; rehab-specific target pool unverified; billing collection dependence.
- Sources: [source 1](https://mail.google.com/mail/u/0/#all/1a0344b1f5883c2c), [source 2](https://mail.google.com/mail/u/0/#all/1a03f2e9df864a43)

### 2. Outsourced diagnostic medical physics testing and radiation-safety services for outpatient imaging

A fresh regional testing-company acquisition identifies a necessary vendor, and its service catalog includes repeat physics inspections and outsourced safety roles. This is a focused technical service hypothesis; growth, standalone TAM and independent target pool require validation.

- Independent source count: 1.
- Lifecycle/overlap: Commercial Equipment Maintenance umbrella; Medical/Lab/IVF Cleaning does not perform physics QA.
- Unresolved: Licensed talent dependence; PE platform competition; niche TAM unverified.
- Sources: [source 1](https://westphysics.com/west-physics-announces-acquisition-of-radiographic-testing-services-inc/)

### 3. Electrical power-system testing and preventive reliability services for installed commercial/industrial assets

Historical seller teaser describes recurring maintenance, relay calibration and fluid testing rather than new construction. Recent inspection/power deal flow is adjacent context only; the unusually high seller margin must not become the industry assumption.

- Independent source count: 1.
- Lifecycle/overlap: Commercial Equipment Maintenance parent; existing water SCADA; killed fire protection and sign/lighting explicitly excluded.
- Unresolved: Exceptional unverified seller margin; hazardous licensed labor; equipment/project mix.
- Sources: [source 1](https://mail.google.com/mail/u/0/#all/1a01bd7b7605d215)

### 4. Fine-jewelry incoming QA and inventory verification services for independent heritage brands

Repeated owner and team evidence shows real defects, inventory and supplier-documentation pain with strong Kay access. Evidence comes from one active deal; outsourcing willingness, recurring vendor revenue and firm density remain unknown, with prior in-house confidentiality objections retained.

- Independent source count: 1.5.
- Lifecycle/overlap: Jewelry aftercare and pure authentication; do not rename an existing/killed lane.
- Unresolved: Same-deal source concentration; in-house substitute; thin standalone pool.
- Sources: [source 1](https://notes.granola.ai/d/a52d727e-6be6-4d11-88bb-2224c48bd24b), [source 2](https://notes.granola.ai/d/8edd1384-f7b6-4ee7-b794-dc6e888ecc76)

### 5. Primary consumer-health supplement contract packaging with lot-control and specialty-format services

Multi-Pak and broader beauty-fulfillment transactions show suppliers capturing growth-related operational complexity. Existing beauty packaging and 3PL rows require strict deduplication: only a distinct primary fill/pack consumer-health service scope should proceed as new.

- Independent source count: 2.
- Lifecycle/overlap: High-End Beauty & Fragrance Packaging and MoCRA Beauty 3PL already Under Review.
- Unresolved: Capital intensity; PE rollups; potential semantic duplicate.
- Sources: [source 1](https://www.truvant.com/news/truvant-acquires-new-jersey-based-multi-pak-packaging-a-specialist-in-vitamins-supplements-and-otc), [source 2](https://fortpointcapital.com/news/ams-fulfillment-acquires-vox-fulfillment)

No candidate has a verified industry TAM, normalized margin or independent target count at synthesis. Identifier must supply INITIAL SCREEN, TARGET TAM, MARKET TAM and the precise second-order rationale before nomination. No outreach channel changed.

Coverage limitations: historical Gmail bounded (4 threads read/149 surfaced; pagination outstanding), incomplete historical API archive, OneNote unavailable, ChatGPT raw export absent, Reddit403. Recent Gmail/Granola are accessible. /tmp/niche-intel-2026-09-07-recent/diagnostics.json and historical consolidated.md retain exact coverage.

**READY:** all six synthesis outputs present.
---

---
## [niche-intel-synthesizer] Registry identity correction

Supersedes routing/source columns in prior synthesis registry; full corrected registry in /tmp/niche-intel-2026-09-07-synthesis.json and .md. Origin, Alloy, USI, Edita and Carrot prior vault matches were unrelated; removed from verified history and retained only under rejected_vault_matches. Aon genuine broker history retained; Aone Partners excluded. All companies now explicitly outreach_eligible=false; acquired/platform/venture companies COMP_ONLY_NO_OUTREACH; Acumen stalled and Hangman passed, independent of legacy list membership. Six research stubs now identify exact business context and domains where known. No source facts deleted, no CRM/external writes.
---

## [IDENTIFIER] — Codex/systemd 2026-09-07
Three candidates independently validated as real supplier categories: outpatient PT/OT/SLP revenue-cycle operations; diagnostic medical physics QA/RSO; commercial/industrial electrical reliability testing. Five named provider examples each, primary-source services and explicit ownership uncertainty. All INITIAL SCREEN, TARGET TAM, MARKET TAM blocks present; all screens INCOMPLETE, not fictional pass. Electrical broader North America proxy $2.66B/6.5% CAGR; exact US niche remains uncarved. Jewelry QC has at least one US services division but no specialist pool established; packaging duplicate/capital concerns retained as un-nominated research, not killed/tabled. 23 category clusters/13 edge scopes reviewed, five preliminary scopes and three final review candidates. Live four-tab semantic dedup re-fetched. Full evidence and source links `/tmp/niche-intel-2026-09-07-identified.json` and `.md`. No outreach/activation/channel changes.
→ READY

---
## [niche-intel-onepager / outpatient rehab RCM]
**Status:** complete / READY

Cloned actual master template; retained six original shapes and16x2 table; three-slide PPTX includes19 live source hyperlinks. Assessment Pending Scoring. Family-company evidence and five provider brands retained without invented margins, TAM or independent acquisition count. Live folder dedup checked; new folder under established WEEKLY REVIEW (ACTIVE SPRINTS name absent).

- Folder: https://drive.google.com/drive/folders/1PWSIDJ5jHIkoHI7wHr9FDxnmncuCGHZ5
- PPTX: https://drive.google.com/file/d/10nsJpj0t9EYdoPb3qGTZfUin3Y3cAjvT/view
- Verified upload ID: 10nsJpj0t9EYdoPb3qGTZfUin3Y3cAjvT
- Manifest: /tmp/niche-intel-2026-09-07-deliverables/outpatient-rehabilitation-revenue-cycle-services/manifest.json
No notification, outreach or channel change.
---

## [ONEPAGER — DIAGNOSTIC MEDICAL PHYSICS] — Codex/systemd 2026-09-07
Live broad Drive name search and WEEKLY REVIEW listing found no existing physics/radiation/diagnostic artifact. Created niche folder in established WEEKLY REVIEW (requested ACTIVE SPRINTS absent): https://drive.google.com/drive/folders/1LwrGK216ooVbfFE2D8v8XFELhlqFpWSh. Uploaded pending-scoring PPTX `1GybDMX4zJ8TU8dxxX4FaYzJM7NLybAHR`; three slides, original six main-slide shapes retained, 15 linked sources. Reopened content and hyperlink checks pass; exactly one PPTX verified live. No score/activation/outreach changes. Manifest: `/tmp/niche-intel-2026-09-07-deliverables/outpatient-diagnostic-medical-physics/manifest.json`.
→ READY

---
## [niche-intel-onepager: electrical-power-reliability-testing] — recovery 2026-09-07
**Source:** Identifier, historical seller evidence, NETA/provider/EIA/sponsor sources
**Status:** complete

Existing Sept1 folder and PPTX recovered and conservatively revised in place; original backup retained. Six template shapes preserved; 18 linked sources across three source slides. Pending Scoring only; exact niche TAM, typical margins and independent scaled pool explicitly unknown. A&F union agreements flagged from primary website. Single-file live dedup and remote SHA256 readback verified.

[PPTX](https://drive.google.com/file/d/18OY6lg50DAdEGI11QNlDgHYBbnQidZ5H/view) | [existing folder](https://drive.google.com/drive/folders/1N9YKYVqdMZbMLpvzjmZ8MbNUUtT1i7AI). ACTIVE SPRINTS absent; established WEEKLY REVIEW parent mapping retained. Referenced [[traces/agents/2026-09-07-niche-intelligence]] source trace. Manifest `/tmp/niche-intel-2026-09-07-deliverables/electrical-power-reliability-testing/manifest.json`. No new file or folder; one content revision. Native rendering unavailable; programmatic bounds/table validation performed.

**READY**
---

### SCORER READY — 2026-09-07

INDUSTRY scoring completed 3/3. Eight weighted groups; target TAM unscored; incomplete screens retained. Workbook caches and in-place PPTX replacements verified. Handoff `/tmp/niche-intel-2026-09-07-scored.json` and `.md`. No activation or outreach.

SCORER verification addendum: all three deck status cells now read Research / Scored, initial screen incomplete; stale Pending Scoring removed. Final replacements downloaded and byte-verified. Source hyperlink counts RCM20, physics16, electrical19. READY for tracker.

## [TRACKER] — Codex/systemd 2026-09-07
UPDATED Industry Research Tracker: three IDEATION rows at A25:L27 inserted inside Compliance section; three WEEKLY REVIEW rows at A46:K48, status New, blank Current Outreach Channel and DealsX Niche. Each contains verified scorecard/one-pager links, INCOMPLETE initial-screen language, unknown exact niche TAM/typical EBITDA/independent scaled pool, and five-provider-count caveat. Electrical explicitly marked recovered/narrowed Sept1 research, missing-row reconciliation. Full live values and FORMULA snapshots taken immediately before mutations; every existing unrelated cell/formula, channel, status and rank verified unchanged. Each niche exactly once in each destination; name-count delta +3 each. Actual tracker_updated=true. Detailed audit: `/tmp/niche-intel-2026-09-07-tracker-result.json`; backups `/tmp/niche-intel-2026-09-07-tracker-execution/`. No activation, channel selection or notifications.
→ READY

## [Finalization] orchestrator
Three research candidates completed: two new, one recovered/narrowed. Three one-pagers and three industry scorecards verified. IDEATION and WEEKLY REVIEW each gained three deduplicated rows; existing formulas/status/channels preserved. [[outputs/2026-09-07-niche-intelligence-report]] and [[outputs/2026-09-07-niche-intelligence-supporting-evidence]] retain results. No notifications, activation or outreach.
→ CLOSE
