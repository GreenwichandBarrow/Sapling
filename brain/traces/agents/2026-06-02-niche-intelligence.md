---
schema_version: 1.0.0
date: 2026-06-02
task: Tuesday-night headless niche-intelligence pipeline (gather → synthesize → identify → one-pager → score → write tracker)
agents: [niche-intel-recent, niche-intel-historical, niche-intel-synthesizer, niche-intel-identifier, niche-intel-onepager, niche-intel-scorer, niche-intel-tracker]
status: completed
tags:
  - date/2026-06-02
  - topic/niche-intelligence
  - skill/niche-intelligence
---

# Agent Chatroom: Niche Intelligence 2026-06-02 (Tuesday Headless Run)

## Coordination Log

## [22:34] orchestrator
Tuesday-night headless run starting. Sourced 1Password env (op-env.sh). Read tracker state, learnings.md, scorecard-structure.md, sub-agent prompts. 16 niches currently in WEEKLY REVIEW.

**Active niches (do NOT re-surface as "new" — semantic dedup required):**
1. Premium Pest Management (Luxury Hospitality & Commercial Properties)
2. Private art advisory firms
3. Estate Management Companies
4. Specialty Coffee Equipment Service
5. High-End Commercial Cleaning
6. Vertical SaaS for Luxury & High-Value Asset Service Industries
7. Specialty Insurance Brokerage (Art & Collectibles)
8. Storage & Related Services for High Value Assets
9. Trade Credit, Customs Bonds & Cargo Insurance Brokerage
10. HNW Personal Lines Concierge Insurance Brokerage
11. Property Tax Appeal Services (Commercial-Property)
12. Truck Licensing & Compliance Platform (IFTA/IRP/DOT)
13. Surplus Lines Compliance & Tax Filing Services
14. AED (Funeral Home Management Software / adjacent)
15. EHS — Environmental, Health & Safety Compliance
16. Aerospace Defense

**KILLED (exclude — failed for documented reasons):** Family Office Enablement Services, Luxury Property Maintenance, Art Tech Platforms, Birthing Facility Compliance Auditing, Fertility Clinic Software, Concierge Medicine, Software Publishers (too broad), Interior Design SaaS, and others.

**TABLED (can resurface ONLY if new data addresses original table reason):** EV Software/Charging, Other Computer Related Services, Escrow & Custodial Software, Specialized Document Lifecycle & Archival, Corporate Entity & Record Management, Yacht/Fleet Maintenance Software, Legal Software, High-End Property Management platform, High-End Electrical & Lighting, and others.

**Known headless constraints (from 2026-05-26 run):** Granola MCP unauthenticated (PKCE OAuth interactive-only — use brain/calls/ as 14-day proxy); OneNote MCP unavailable; ChatGPT export may be absent at expected path. Agents document gaps explicitly; partial-source is acceptable, silent skipping is not.

Spawning Step 1 gathering agents (RECENT + HISTORICAL) in parallel now.

---
## [niche-intel-recent] — 2026-06-02 22:58 ET
**Source:** RECENT (6 sources, last 14 days, 2026-05-19 → 2026-06-02)
**Status:** complete (all 6 sources reached). Notes: last30days returned mostly noise on niche-specific queries (Reddit 0 items across all queries; HN entity-miss demotion) — substituted WebSearch for niche market data. Granola MCP unauthenticated in headless — used `brain/calls/` (14 files modified in window) as proxy per standing constraint.

### Signals Found (by source 1-6)

**SOURCE 1 — WEB/SOCIAL (last30days + WebSearch):**
- last30days social yielded no usable niche signal (HN noise: I-Ready PE-backed edtech revolt, generic B2B SaaS Show-HN posts). WebSearch carried the load:
- **Pest control (existing #1):** US market ~$29.7B in 2026, 34,000+ businesses (highly fragmented). Multiples UP 0.5x YoY driven by PE consolidation. Mid-market $500K-$2M EBITDA = 7-10x; multi-market regional $2M-10M EBITDA = 9-12x; platform deals 13-17x. H2-2025 deal volume +12% YoY. 70-85% recurring revenue typical, 85%+ = platform threshold. Active platforms: Anticimex, Rollins, Rentokil/Terminix, Aptive. (Reinforces #1; confirms exit channel + PE-owned-target risk on direct acquisitions.)
- **Specialty insurance brokerage (existing #7/9/10/13):** Avg EBITDA multiple ~11.4x for >$1M EBITDA deals in 2025 (+20% since 2020, now stabilizing). Large-deal compression: AssuredPartners ~14.5x (was 17-19x expected), Risk Strategies ~16x. PE momentum regaining w/ rate cuts: Stone Point/OneDigital, Onex/Integrated Specialty Coverages (from KKR). Buyers shifting from pure-multiple to strategic-fit. (Reinforces insurance cluster + exit-channel thesis.)
- **Carpet/flooring (NEW signal, see below):** US flooring market $117.31B (2025) → $123.90B (2026); global $463B→$646B by 2034 @ 5.7% CAGR. Market fragmented; manufacturer tier concentrated (Mohawk/Shaw/Tarkett/Mannington/AHF). Note: data is product/manufacturing-weighted, not installation-services-specific — installation/contractor layer fragmentation not directly quantified.
- **VA-benefits consulting (NEW signal, see below):** Booming post-PACT-Act, but heavy REGULATORY HEADWIND — CA law (Newsom) bans fees for VA-claim help effective end of 2026; LA first state to cap fees + require disclosures. "Claims sharks" reputational stigma (CNN/WaPo investigations). Major players Veterans Guardian (NC), Veterans Benefit Guide (NV) spending $150K-$372K on lobbying. No PE-acquisition activity surfaced.

**SOURCE 2 — NEWSLETTERS (auto/subscriptions & education 7d, auto/industry research 14d):**
- **This Week in ETA (Grant Hensel, 5/29):** SBA walked back "one-strike" rule for minority investors eff. June 1 — waivers now available if investor owned <20%, not guarantor, no control. Removes a capital-markets blocker for ETA/search-fund acquisition financing. Also: closed 4 SMB acquisitions recently (tombstone engraving, industrial insulation, homecare/hospice, residential HVAC) — signals where ETA capital is flowing.
- **PE Hub / Leader's Edge (industry research):** Carlyle grew iC Consult (identity security) before pending sale to Bridgepoint; Astorg portco Steliau acquiring Acal BFI. Identity-security consolidation = adjacency, not in-box.
- **Acquiring Minds (Will Smith, 6/2):** "Started as SBA Searcher, Built to a PE Fund" + Franchise Holdco webinar — franchise roll-up + ETA convergence theme (G&B excludes franchises, context only).
- **CounterA (Amanda Lo Iacono, 6/2):** "CounterA Concierge is Live" — transaction-infrastructure/escrow-adjacent platform launch, fee waived for deals initiated by Aug 1. (Relates to previously-tabled Art Escrow Services; Amanda is a recurring escrow-infra signal source.)
- **NPMA / PestWorld (industry research):** PestWorld 2026 + Women's Forum follow-ups — reinforces pest #1 network/conference channel; women-network angle live.
- **XPX (multiple, 5/26-6/1):** heavy NY/NJ/CT/LI exit-planning event cadence — intermediary network density in G&B's geography.

**SOURCE 3 — GRANOLA CALLS (proxy: brain/calls/ modified last 14d):**
- **2026-06-02 Matt Luczyk (Peapack IB):** 3 Kay-directed niche signals (see NEW below). Market intel: **pest multiples "still very high, coming down but still high"** (corroborates Source 1). Matt offered to be benchmark resource on multiples for any industry; June 16 Peapack owner event (Summit NJ); insurance-industry contact intro offered.
- **2026-05-29 Megan Lawlor (peer searcher):** Detroit stone-fabrication deal under LOI; ~$500K all-in DD cost data point. Kay narrowing cold outreach to pest-management focus, NAICS-specificity. No new niche.
- **2026-05-27 Camilla pest/drone review, 2026-05-21 Art Business Conference, 2026-05-20 NPMA Women's Forum + WSN:** reinforce pest + art-advisory + insurance(art) network channels; women-led network throughline.

**SOURCE 4 — GMAIL DEAL FLOW (14d) + INVESTORS (14d):**
- **Axial — Multi-Market Commercial Cleaning Services Provider (6/2):** direct in-box teaser for existing #5 High-End Commercial Cleaning. (Body image-only; broker teaser, NDA-gated.)
- **E&K Provider of Security Solutions (5/29):** $7.1M rev / $1.5M EBITDA, ~450 systems under service contracts, ISO-certified, gov/law-enforcement clients — strong recurring-service-contract shape BUT Hong Kong/Macau = outside US-only box. Useful as a SHAPE reference (mission-critical maintenance contracts).
- **E&K Machining/Waterjet (6/2):** $2.3M rev / $500K EBITDA, SE US — manufacturing, below box, not services.
- **Helen Guo SMB Deal Hunter (5/26, 5/28, 6/2):** recurring-service shapes — Multi-State Facility Maintenance Contractor ($838K EBITDA, national chain contracts), Commercial Floor Care w/ recurring service agreements ($483K EBITDA, gov/casino/healthcare), Diversified Industrial Services 24/7 emergency ($1M EBITDA), **Trucking Licensing & Compliance Platform in CA ($412K EBITDA, recurring annual filings)** — corroborates existing #12 Truck Licensing but the listed one is CA (hard-exclude geography).
- **Warren Chan / Anacapa (investor, 5/29):** wants Kay's perspective on "services to the art world and their fit with the search fund model" — validates art-advisory/art-insurance cluster interest from an investor; meeting proposed for/after June 9.
- **BizBuySell NYC-metro match (5/30):** geography-aligned but generic.

**SOURCE 5 — VAULT RESEARCH (last 14d):**
- `brain/outputs/2026-05-26-niche-intelligence-report.md`: last cycle added **Truck Licensing & Compliance (#12)** to WEEKLY REVIEW at 2.33/3 (78%) with thin-pool caveat. Prior cycle verdict = zero net-new; existing pipeline reinforced.
- `brain/outputs/2026-05-26-pest-10-co-june-experiment-plan.md`, `dealsx-vs-jj-performance-analysis.md`: pest operational focus deepening.
- `brain/outputs/2026-05-2*-discussion-women-led-thesis-*.md`: women-led-network-first thesis reframe (industry = output of network access).

**SOURCE 6 — PASSIVE SIGNALS (brain/inbox/ topic/niche-signal, created since 5/19):**
- 3 NEW Kay-directed signals dated 2026-06-02 (all from Matt Luczyk coffee, flagged urgency/high, explicitly queued for THIS run): carpet-installation, warranty-pipe-installation, va-benefits-consultant. (Plus 5/31 backfill: aed-sales-servicing, ehs-compliance, aerospace-defense — already active #14/#15/#16.)

### New Potential Niches (not in active list)
- **Carpet / commercial + multifamily flooring installation (NJ)** — Kay-DIRECTED (inbox 6/2). Growing, retirement-age owner, fragmented, "a couple PE players." Structural caveat: **construction-adjacent soft-exclude** (building products + trades, geography-agnostic) per `feedback_niche_screen_soft_excludes_construction_adjacent_travel`. Kay wants full screen run anyway — apply lens at scoring, don't drop.
- **Insurance-fed warranty residential pipe installation (B2B2C)** — Kay-DIRECTED (inbox 6/2). Attractive structural feature: ALL leads come through insurers (no lead-gen), B2B2C. Caveat: construction/trades-adjacent + residential. Matt sending warranty-company approved-provider list. INDUSTRY shape interesting even if the named co. is fading.
- **Veterans VA-benefits consultancy (MO, ~5x, remote-able)** — Kay-DIRECTED (inbox 6/2). Husband-wife retiring, ex-VA staff, referral lead-gen. Caveats: (a) **likely B2C** end-customer (individual veterans) per `feedback_b2b_b2b2c_ok_no_b2c` — confirm mix; (b) **severe regulatory headwind** — CA fee ban end-2026, LA fee caps, "claims sharks" stigma, active legislation. Web data materially weakens this one.

### Reinforcement of Existing Niches
- **#1 Premium Pest** — fresh quant: $29.7B US market, 34K+ firms, multiples +0.5x YoY, H2-25 volume +12%, 85%+ recurring = platform threshold. Two independent multiple confirmations (WebSearch + Matt Luczyk "still very high"). Exit/comp channel strong; direct-acquisition PE-owned risk elevated.
- **#5 High-End Commercial Cleaning** — live Axial broker teaser (multi-market provider) + Helen Guo commercial floor care w/ recurring service agreements.
- **#7/#9/#10/#13 Insurance cluster** — 11.4x avg multiples, PE momentum regaining (Stone Point, Onex), large-deal compression. Investor Warren Chan validating art-world-services interest.
- **#12 Truck Licensing & Compliance** — second independent sighting (Helen Guo 5/26, CA listing $412K EBITDA) confirms the niche is real and tradeable, though listed example is CA (excluded).
- **EHS/#15, AED/#14, Aerospace/#16** — inbox backfill 5/31 confirms active.

### Data Points for Scoring
- Pest: US $29.7B mkt / 34,000+ firms / 7-10x (mid) / 9-12x (regional) / 13-17x (platform) / +0.5x YoY / +12% H2 volume / 70-85% recurring (85%+ platform).
- Insurance brokerage: 11.4x avg (>$1M EBITDA), AssuredPartners 14.5x, Risk Strategies 16x.
- US flooring market: $123.90B (2026), 5.7% CAGR global; fragmented at install layer (not directly sized).
- VA benefits consulting: post-PACT-Act growth BUT CA fee-ban eff. end-2026 + LA fee caps (hard regulatory risk).
- SBA one-strike walk-back eff. 6/1 (minority-investor waiver <20%/no-control) — improves acquisition financing climate.
- ETA capital flow examples (4 recent closes): tombstone engraving, industrial insulation, homecare/hospice, residential HVAC.
- E&K security-solutions deal shape: $7.1M rev / $1.5M EBITDA (21%) / ~450 service contracts (recurring-maintenance reference, non-US).
---

---
## [niche-intel-historical] — 2026-06-02 22:48
**Source:** HISTORICAL (4 clusters: calls, email, onenote, chatgpt)
**Status:** partial — Calls COMPLETE (brain/calls/, ~50 substantive files <2026-05-19 mined). Gmail COMPLETE (all 5 searches run). OneNote UNAVAILABLE (MCP not installed). ChatGPT export UNAVAILABLE (~/Downloads absent; no selected_business_conversations.json on disk). Granola MCP UNAVAILABLE (interactive OAuth only) — brain/calls/ used as proxy.

### Findings by Niche (NOT by source)

**1. Art Storage & Logistics for High-Value Assets** — STRONG (5+ sources: Levi/Acumen ×2, Graham, Chris Wise, Jeremy Black, Margot, Krupa). *Adjacent-but-richer than tracked "Storage for High Value Assets."*
- Hard data (Acumen/Levi): 75 emp, 4 NY partners, **storage 16% margin (Queens)**, Poughkeepsie 90-95% full, ~8-9k items/client, ~65% galleries/20% estates revenue mix. Capex $600-750k/new climate warehouse. Storage = stickiest line; service (trucking/crating/install) = most revenue. Customs brokerage drives trucking; no tariffs on art currently.
- Comps named: UOVO, Crozier (PE-degraded service = opportunity), Maquette (NY, 2 Wall St owners), SAT/Safe Art Transport, Art Crating, Maspeth. Graham: ~100 staff/12 buildings; 30yr+ staff tenure; labor is the value-killer buyers underestimate (low margin vs self-storage).
- Live deal seen: **Santa Fe art transport listing** (Jeremy Black, strong margins, established team). Krupa Shah (Stream Capital) had an art-storage deal interest (owns warehouses, sale-leaseback angle).
- Contacts: Levi Phelps (Acumen partner, deep DD source), Graham (+1 646-644-7318, via Britta), Chris Wise (212-338-4332, ex-art-world→insurance). Kay sentiment: HIGH/sustained — ~6mo of diligence. Overlooked because tracker entry is generic "storage," not the art-services variant with these margins/comps.

**2. Trade Credit / Customs Bonds / Cargo Insurance** — STRONG (tracked, but NEW named-contact + intel). Jeremy Black "really bullish on trade credit insurance if you can find an agency with the numbers." Kay's **brother works in marine logistics** + interacts with these brokers = warm intel/intro channel (previously unsurfaced asset). Keep tracked; flag the brother as a river-guide node.

**3. HNW Personal Lines Concierge Insurance** — STRONG (tracked). August Felker named a specific target: **two women near retirement running a women-centric HNW personal-lines brokerage (yachts/houses/HVA), anti-PE, personal-lines only.** August: "very sticky, ~100% recurring, some of the most valuable parts." Personal lines = potentially lower multiples than commercial. Risk: 3yr earn-out + 5yr non-compete standard. Overlooked: specific actionable target sitting in an Oct/Nov 2025 call.

**4. Specialty/Fine-Art Insurance Brokerage** — tracked, but LIFECYCLE-CHALLENGED (see flags). Wealth-transfer "silver tsunami" tailwind (Deloitte Art&Finance: 80% of family offices asked to manage hard assets; demand decoupled from art-market growth). Climate driving premiums double-digits = broker commission tailwind. BofA art team recommends 4 large + 3 small specialty brokers (fragmentation confirmed).

**5. Estate Management Companies for HNW** — tracked. Andrew Lowis (5/6) confirms this is Kay's CURRENT active focus post-art ("looking at estate management for wealthy individuals"). Serves same affluent customer profile Kay anchors on. No new quant data but confirms it is the live thread.

**6. Insurance Distribution / Broker-Group Marketing Orgs (FMO/IMO model)** — NEW signal. Jeremy Black's mom's late client "Jolene": a marketing org that **assembled broker/agent groups to write annuity & life policies** (carrier outsourced middleman distribution). Jeremy: "scalable back-office model — multiple agents servicing territories." This is the FMO/IMO/aggregator model, distinct from retail brokerage. Not on any list. Capital-light, recurring override revenue.

**7. Vertical SaaS / Luxury asset software** — tracked. Plexus lender Katie Walker "liked Kay's pitch on vertical software, felt she understood it" — first deal was **Datacor (chemical distribution vertical SaaS)** = warm debt precedent. Caveat: AI-disruption pause — both Carlos Nieto (DCA) and Krupa Shah stopped looking at software ~Jan-Feb 2026.

### Lifecycle Flags (proposed → challenged → outcome)

- **Insurance brokerage ACQUISITION (whole-firm) → REPEATEDLY CHALLENGED → near-dead at G&B size.** Proposed by Kay/August (validating). Challenged hard by: Hunter Hartwell (searched insurance, came up EMPTY — specialty brokerages 12x-14x EBITDA, prohibitive); Chris Wise (entrenched Aon/Huntington Block, books non-portable, low margins, zero-sum client acquisition, "almost no fine-art books for sale"); Tobias (MarshBerry: everything larger than G&B, all owners know their value); investor pushback (multiples + no QSBS + favors experienced operators). **Outcome / recurring counter-thesis: "START your own brokerage / build don't buy"** — heard from Tobias, Mark Gardella (InsurTech accelerators, no-equity), and others. Do NOT surface whole-firm insurance acquisition as a live recommendation. The viable residue = carve-out (fine-art dept from larger firm, per Hunter) OR a specific small anti-PE personal-lines target (#3) OR geographic arbitrage (Margot: buy Midwest brokerage, open NY office — lower valuations outside consolidated NY).

- **Pure Art Advisory → CHALLENGED → DEAD as standalone.** Margot Romano: no money in pure advisory; banks (BofA free, Morgan Stanley Blue Rider, UBS building) erode pricing; no regulation = integration mess. Survives ONLY as advisory + services (valuation/appraisal/collection mgmt) bolt-on. Schwartzman & Associates (~4 ppl, collection-expansion focus) fits buy-box but advisory-only. (Aligns with already-KILLED "Art Tech Platforms.")

- **Art transaction platform (KYC/wire/reporting for family offices) → proposed (Chris Wise → Amanda the CFO-builder) → no pursuit recorded.** Likely falls under KILLED "Art Tech Platforms"; do not resurface as live.

### New Potential Niches (not in tracked/killed/tabled lists)
- **Heat-transfer / on-demand label manufacturing** (Jeremy Black call): beachwear-niche family business, 53yr, $3.5M rev / **30% margins**, no inventory, US-based, sticky customers. Kay actively diligenced it Feb 2026. B2B, recurring-ish. Net new — never scored.
- **Insurance FMO/IMO distribution-aggregator** (finding #6 above) — capital-light broker-group marketing orgs writing annuity/life. New.
- **Collegiate retail & licensing management** (Jeremy Black, brief): license-renewal/licensing-mgmt firms supporting brokers; collegiate retail/licensing as recurring-revenue diversification. Tangential, low-confidence — flag only.
- **Marble & granite fabrication/installation** (Megan Lawlor's live LOI, ~30yr family, recession/tariff-resilient) — comp/intel only, not a Kay niche; logged as ETA-peer datapoint.

### Tabled Niches With New Data (if any)
- None of the formally TABLED niches (EV, Escrow software, Legal software, Yacht/Fleet maintenance software, etc.) received new data addressing their original table reason. No resurfacions warranted.
- Market-context datapoints for the synthesizer/scorer (not niches): XPX/Axial panel (4/23) — individuals/family-office/holdco now ~27% of Axial closes (doubled in 5yr); search funds 14% of Axial closures (7% in 2021); 95% of committed-capital funds chasing $1-3M EBITDA (down-market compression = pricing pressure in G&B zone); buyer "stretch on price" collapsed 25%→11%; AI-defensibility now a universal underwriting hurdle (favors landscapers/contractors/service cos); transportation +20% YoY supply, business services double-digit resurgence, healthcare seller's-market. Pest mgmt seeing 30-40% premium bids from larger players (Carlos Nieto) — pricing-pressure flag for tracked Premium Pest.

---
## [niche-intel-synthesizer] — 2026-06-02 23:20 ET
**Source:** SYNTHESIS of both gathering posts + vault/learnings. Status: complete.

### OUTPUT 1: CROSS-SOURCE SIGNAL MATRIX
| Niche / Industry | RECENT sources | HISTORICAL sources | Total | Strength |
|---|---|---|---|---|
| Premium Pest Mgmt (#1) | WebSearch, Matt Luczyk, NPMA newsletter, Camilla call | Carlos Nieto (30-40% premium bids) | 5 | VERY STRONG |
| Insurance cluster — specialty/art/HNW/trade-credit (#7/9/10/13) | WebSearch (11.4x), Matt intro, Warren Chan, XPX | August Felker, Chris Wise, Hunter Hartwell, Tobias/MarshBerry, Jeremy Black, BofA art team, Deloitte | 9+ | VERY STRONG |
| Art Storage & Logistics (HVA) | Anacapa/Warren art-services interest | Levi/Acumen ×2, Graham, Chris Wise, Jeremy Black, Margot, Krupa | 6.5 | VERY STRONG |
| High-End Commercial Cleaning (#5) | Axial teaser, Helen Guo floor-care | — | 2 | STRONG |
| Truck Licensing & Compliance (#12) | Helen Guo CA listing ($412K EBITDA) | — | 1 (quant) | MODERATE |
| Estate Management for HNW (#3) | — | Andrew Lowis (current active focus) | 1.5 | STRONG |
| Carpet/flooring installation (NEW) | Matt Luczyk + inbox 6/2, WebSearch ($124B mkt) | — | 1.5 | MODERATE |
| Insurance-fed warranty pipe install (NEW B2B2C) | Matt Luczyk + inbox 6/2 | — | 1.5 | MODERATE |
| VA-benefits consultancy (NEW) | Matt Luczyk + inbox, WebSearch (reg headwind) | — | 1.5 | WEAK (reg risk) |
| Heat-transfer/on-demand label mfg (NEW) | — | Jeremy Black (Kay-diligenced, 30% margin) | 1 (quant) | MODERATE |
| Insurance FMO/IMO distribution-aggregator (NEW) | — | Jeremy Black ("Jolene") | 1 | WEAK |
| Vertical SaaS luxury asset (#6) | — | Katie Walker/Plexus (Datacor precedent) | 1.5 | STRONG (AI-pause caveat) |
| Collegiate retail/licensing (NEW) | — | Jeremy Black (brief) | 1 | WEAK |

### OUTPUT 2: NAMED COMPANY REGISTRY
| Company | Niche | Source | Independence | Location | Flag | Notes |
|---|---|---|---|---|---|---|
| Acumen | Art storage | HIST (Levi) | Independent (4-partner) | Queens NY | VAULT_HISTORY | Multi-partner = investor deal-killer; deep DD source |
| UOVO | Art storage | HIST | PE-owned | NY | NEW_TARGET (exclude) | Comp, not target |
| Crozier | Art storage | HIST | PE-owned | NY | NEW_TARGET (exclude) | PE-degraded service = whitespace |
| Maquette | Art storage | HIST | Independent | NY (2 Wall St) | NEW_TARGET | Small, owner-run |
| SAT/Safe Art Transport, Art Crating, Maspeth | Art storage | HIST | Unknown | NY | NEW_TARGET | Fragmentation evidence |
| Santa Fe art-transport listing | Art storage | HIST (Jeremy) | Independent | NM | NEW_TARGET (out-of-geo) | Live listing, strong margins |
| Anticimex/Rollins/Rentokil-Terminix/Aptive | Pest | RECENT | Public/PE | US | exclude | Platform comps/exit channel |
| AssuredPartners, Risk Strategies | Insurance | RECENT | PE roll-up | US | exclude | Exit channel comps |
| Two-women HNW personal-lines brokerage | HNW insurance | HIST (August) | Independent, anti-PE | US | WARM_INTRO | Named retiring target, ~100% recurring |
| Schwartzman & Associates | Art advisory | HIST | Independent (~4 ppl) | US | NEW_TARGET (advisory-only=dead) | Buy-box fit but standalone advisory dead |
| Axial multi-market cleaning provider | Cleaning | RECENT | Unknown | US | NEW_TARGET | NDA-gated teaser |
| Helen Guo: floor-care/facility-maint/trucking-CA | Cleaning/truck | RECENT | Independent | US (truck=CA) | NEW_TARGET (CA excl) | Recurring-service shapes |
| E&K security solutions | Maintenance-contract | RECENT | Independent | HK/Macau | exclude (non-US) | SHAPE reference only |
| Datacor | Vertical SaaS | HIST | — | US | (comp) | Warm debt precedent (Katie Walker) |
| Heat-transfer label co (beachwear) | Label mfg | HIST (Jeremy) | Independent (53yr family) | US | VAULT_HISTORY | Kay-diligenced Feb 2026 |

### OUTPUT 3: CONTACT-TO-NICHE MAP
| Contact | Warmth | Niches | What to ask | Last contact |
|---|---|---|---|---|
| Matt Luczyk (Peapack IB) | HOT | pest, flooring, warranty-pipe, any (benchmark) | Warranty approved-provider list; multiples benchmarks; June 16 Summit NJ owner event | 2026-06-02 |
| Warren Chan (Anacapa investor) | HOT | art-services, art-insurance | Perspective on art-world services fit w/ search model | meeting ~June 9 |
| Levi Phelps (Acumen) | WARM | art storage | Margin/comp DD continuation | 2025-09-17 |
| August Felker | WARM | HNW personal-lines insurance | Intro to two-women anti-PE brokerage | Oct/Nov 2025 |
| Jeremy Black | WARM | trade credit, label mfg, FMO/IMO, art transport | Trade-credit agency leads; FMO model detail | vault |
| Kay's brother (marine logistics) | HOT (internal) | trade credit/customs/cargo | Warm intros to cargo-insurance brokers | n/a |
| Graham (+1 646-644-7318) | COOL | art storage | Labor-margin reality, deal intros | referred via Britta |
| Chris Wise (212-338-4332) | COOL | art insurance/storage | Fine-art book availability | vault |
| Margot Romano | COOL | art advisory/insurance geo-arbitrage | Midwest-brokerage→NY-office play | vault |
| Krupa Shah (Stream Capital) | COOL | art storage (sale-leaseback) | Warehouse/SLB deal interest | vault |
| Camilla de Sanna | WARM (team) | pest, broker triage | Industry eval + listing triage | 2026-05-27 |

### OUTPUT 4: LEAD LIFECYCLE TRACKER
| Niche/Strategy | Proposed by | When | Challenged by | When | Reason | Status |
|---|---|---|---|---|---|---|
| Whole-firm insurance brokerage ACQUISITION | Kay/August | 2025 | Hunter Hartwell, Chris Wise, Tobias/MarshBerry, investors | Oct'25–'26 | 12-14x multiples prohibitive at G&B size; books non-portable; "build don't buy" | DEAD (residue: carve-out / #3 target / geo-arbitrage) |
| Pure Art Advisory (standalone) | exploratory | — | Margot Romano | — | No money in pure advisory; banks erode pricing; survives only as advisory+services bolt-on | DEAD |
| Art transaction/KYC platform | Chris Wise→Amanda | — | (no pursuit) | — | Falls under KILLED Art Tech Platforms | DEAD/KILLED |
| Escrow software (fine-art) | prior | — | learnings.md | — | No smaller providers to grow into; willingness-to-pay absent | TABLED |
| Vertical SaaS (luxury) | tracked #6 | — | Carlos Nieto, Krupa | Jan-Feb'26 | AI-disruption underwriting pause | LIVE (caveat) |
| VA-benefits consultancy | Matt/Kay | 2026-06-02 | WebSearch reg scan | 2026-06-02 | CA fee-ban end-2026, LA caps, B2C, "claims sharks" stigma | LIVE (heavily caveated, likely near-DEAD) |
| Pest direct-acquisition | tracked #1 | — | PE-owned-target risk, 30-40% premium bids | 2026 | Consolidation may have picked low-hanging targets | LIVE (pricing-pressure flag) |

### OUTPUT 5: CONVERGENCE REPORT
1. **Art Storage & Logistics (HVA)** — NET-NEW VARIANT (richer than tracked generic "Storage for HVA"). 6.5 sources, named comps (UOVO/Crozier PE-degraded = whitespace), live listings, 3+ contacts (Levi/Graham/Chris), HOT Warren Chan validating art-services. BUT learnings.md flags it as capital-intensive/project-based/low-margin — convergence matters because the *services* layer (customs/trucking/install), not storage, is where recurring revenue and reachable owners sit. Identifier should split the variant.
2. **Insurance cluster (HNW personal-lines #10 specifically)** — REINFORCEMENT + actionable. 9+ sources, ONE named warm-intro target (two retiring women, anti-PE, ~100% recurring) via August. Convergence matters because the cluster's whole-firm acquisition path is DEAD, but this specific small personal-lines target threads the needle — pursue the target, not the category.
3. **Premium Pest (#1)** — REINFORCEMENT. 5 sources, strongest quant ($29.7B/34K firms), HOT Matt + Camilla operational focus. Convergence confirms it's tradeable but flags elevated PE-owned-target/pricing risk — channel value is exit/comp + women-network (NPMA), direct-acquisition needs sub-platform targets.
4. **Heat-transfer/on-demand label mfg** — NET-NEW, never scored. 1 quant source but Kay-diligenced (30% margins, asset-light, sticky, US, B2B) — best buy-box fit of the net-new ideas. Worth a one-pager and scorecard run.
5. **Trade Credit/Customs/Cargo (#13)** — REINFORCEMENT w/ NEW river-guide asset: Kay's brother (marine logistics) + Jeremy Black bullishness. Convergence matters because it converts a tracked niche from cold to warm-access — flag brother as river-guide node.

**Net-new candidates for Identifier:** art-storage-SERVICES variant, heat-transfer label mfg (top fit), insurance FMO/IMO (capital-light, low-confidence). **Carpet/warranty-pipe/VA** carry soft/hard-exclude + regulatory caveats — surface for Kay, do not advance unflagged. **Avoid:** whole-firm insurance acquisition, pure art advisory, art-tech platforms (lifecycle DEAD).

---
## [niche-intel-identifier] — 2026-06-02 23:48 ET
**Source:** Independent validation of synthesizer Convergence Report + Lead Lifecycle Tracker. WebSearch run on each candidate. Status: complete. **ADVANCING 2 niches. Surfacing 4 not-advanced.**

### ADVANCED #1

```
Niche: Fine-Art Logistics SERVICES (crating / fine-art trucking / installation / customs brokerage) — the asset-light services layer, NOT storage
Thesis: Independently-owned fine-art logistics firms provide mission-critical, recurring/repeat services (climate-controlled trucking, custom crating, white-glove install, customs brokerage) to galleries, museums, estates, and UHNW collectors. The services layer is asset-light (vans + labor + bonded-customs licenses, not climate warehouses), referral-locked through galleries, and fragmented across family operators — exactly the HVA-adjacent, UHNW-client, regulatory-shovel (customs bond) shape G&B anchors on. PE has degraded service quality at the consolidated platforms (UOVO, Crozier, Cadogan Tate), opening whitespace for a high-touch independent.
Signal source: Warren Chan/Anacapa (HOT, art-services validation, ~June 9 mtg); Levi/Acumen, Graham, Chris Wise, Jeremy Black, Margot, Krupa — 6.5 historical sources. CONTEXT ONLY.
Independent validation: WebSearch confirms a deeply fragmented field — family-owned regional operators (Art Couriers LA/Miami; Art Pack 25yr; Atelier 4 four-market; Overseas Brokers full customs+crating+rigging stack) competing against a thin layer of PE/multi-location chains (UOVO, Cadogan Tate 7 US offices, Craters & Freighters 65 locations). Integrated service stacks are the norm; customs brokerage is embedded (regulatory chokepoint, no art tariffs currently). Learnings.md confirms the recurring/reachable value sits in SERVICES (~75% transport+service mix), NOT storage (capital-intensive, ~5-16% margin, balance-sheet business investors reject).
Dedup check: Checked against active niches — distinct from #8 (Storage for HVA) because this is the asset-LIGHT services layer (trucking/crating/install/customs), explicitly EXCLUDING the capital-intensive storage real estate that makes #8 marginal; distinct from #9 (Trade Credit/Customs Bonds/Cargo Insurance) because that is an insurance-brokerage niche (selling cargo/bond policies), whereas this is a physical-logistics-services operator that USES customs brokerage as one service line. Recommend tracker carry this as a sharpened net-new entry OR a re-scope of #8 from "storage" to "logistics services" — Kay decides; do NOT double-count storage.

QUICK SCREEN:
- Margins: Moderate — services layer 15-25% EBITDA (vs storage 5-16%); install/customs higher-margin than trucking
- Recurring Revenue: Moderate — repeat/referral-locked gallery+estate relationships, project-based individual jobs but high client stickiness; ~60% convertible to retainer/contract
- Industry Growth: Moderate — tied to art-market volume + $84T wealth transfer (80% of family offices asked to manage hard assets, Deloitte); climate-driven premiums and silver-tsunami collections support demand
- Growth TAM: Pass — fine-art logistics globally multi-$B; US fragmented services slice supports multiple $2-10M EBITDA operators

TARGET TAM:
- Total firms in market: ~150-300 US fine-art logistics operators (long fragmented tail)
- Independently owned (potential targets): majority — most are family/owner-run regionals
- Already PE-backed/acquired: ~5-8 platforms (UOVO, Crozier, Cadogan Tate, Atelier 4 partial)
- PE consolidation risk: Medium — platforms exist but service degradation = independent whitespace
- Named examples: Maquette (NY, 2 Wall St, owner-run); Art Pack (25yr, crating/storage/install); Atelier 4 (NYC/Miami/LA/Charlotte); SAT/Safe Art Transport (NY); Santa Fe transport listing (NM, live — out of geo)

MARKET TAM:
- Market size: Fine-art logistics multi-$B globally; US services slice est. $1-2B
- Growth rate: ~4-6% CAGR, demand decoupling from art-price growth via wealth-transfer
- Key demand drivers: $84T wealth transfer, family-office hard-asset mandates, climate-driven handling needs, customs/bonded-import volume, museum/gallery activity

Fit/Caveats for Kay: Strongest net-new of the cycle and warm-access (Warren Chan ~June 9; Levi/Graham/Chris contacts live). RIGHT-TO-WIN HIGH — Chanel luxury-service background + art-network depth. CAVEAT: trucking line is lower-margin/labor-heavy (Graham: labor is the value-killer buyers underestimate) — underwrite the services MIX, weight install/customs over pure transport. Must NOT drift into storage real estate. Multi-partner ownership (Acumen) is an investor deal-killer — screen for single-owner targets.
```

### ADVANCED #2

```
Niche: Insurance FMO/IMO Distribution-Aggregator (annuity & life broker-group marketing orgs)
Thesis: FMO/IMOs sit between carriers and independent agents, earning recurring OVERRIDE commissions on every policy their agent network writes — capital-light, no balance sheet, no underwriting risk. Demographic tailwind (annuity demand from retiring boomers) plus carrier preference to outsource distribution makes this a recurring, asset-light, shovel-seller B2B platform. Materially better buy-box fit than whole-firm retail brokerage acquisition (which the lifecycle tracker marks DEAD at 12-14x).
Signal source: Jeremy Black (HISTORICAL, "Jolene" marketing-org client — broker groups writing annuity/life; "scalable back-office, multiple agents servicing territories"). Single-source, low signal confidence. CONTEXT ONLY.
Independent validation: WebSearch confirms the model structurally — FMO earns an override from the carrier on top of the agent's commission; recurring, volume-based, capital-light. PE does acquire in this category (distribution roll-ups active). Distinct economics from retail brokerage: no book-portability problem, override stream travels with the agent network.
Dedup check: Checked against active niches — distinct from #7/#10/#13 (specialty/HNW/trade-credit RETAIL brokerage — those SELL policies to end-clients and carry the DEAD whole-firm-acquisition lifecycle flag) because an FMO/IMO is a wholesale DISTRIBUTION layer earning overrides on an agent network, not a retail book. Not a duplicate of #6 (Vertical SaaS) — this is a services/distribution operator, not software.
Independent validation:

QUICK SCREEN:
- Margins: Strong — capital-light override revenue, low opex; healthy EBITDA margins typical
- Recurring Revenue: High — override/renewal commissions recur with the agent network's in-force book
- Industry Growth: Moderate — annuity/life demand rising with retiring-boomer wave; carrier outsourcing of distribution
- Growth TAM: Pass — US life/annuity distribution is large; FMO/IMO layer multi-$B in override flow

TARGET TAM:
- Total firms in market: hundreds of FMO/IMO/BGA orgs nationally (highly fragmented)
- Independently owned (potential targets): majority small/mid owner-run
- Already PE-backed/acquired: growing — distribution roll-ups active (Integrity, AmeriLife, etc.)
- PE consolidation risk: Medium-High — Integrity/AmeriLife consolidating aggressively at the top; mid-tier still fragmented
- Named examples: thin — no specific independent targets surfaced this cycle (the "Jolene" org is a description, not a named live target). NEEDS target-discovery to validate pool.

MARKET TAM:
- Market size: US life/annuity distribution multi-$B; override layer significant slice
- Growth rate: ~5-7% CAGR (annuity sales at record levels)
- Key demand drivers: retiring-boomer annuity demand, carrier distribution outsourcing, agent-network economics

Fit/Caveats for Kay: STRONG structural buy-box fit (capital-light, recurring, fragmented, shovel-seller) but LOW signal confidence and THIN named-target pool — single historical source, no live target identified. Top-end consolidation (Integrity/AmeriLife) is real PE pressure; opportunity is mid/small tier. Advancing for a one-pager + target-discovery probe to TEST the independent-target pool before committing channel resources. Confirm B2B agent-network economics vs any B2C drift.
```

### SURFACED BUT NOT ADVANCED
- **Heat-transfer / on-demand label manufacturing** — NOT ADVANCED. Validation undercut the buy-box fit at the NICHE level: it is a printing/converting operation with real press/equipment capital (capital-intensive, the synthesizer's pressure-test concern confirmed), and the category is only moderately fragmented (top-5 ~55% revenue). The specific co Kay diligenced (30% margin, no inventory) is an outlier, not the niche norm — and "buy the one good company" is a target play, not a niche thesis. Learnings.md: capital-intensive = structurally incompatible with search fund. Kay can still pursue the SPECIFIC company as a one-off, but it does not warrant a niche-level pipeline. (No-gate rule: flagged, not killed — Kay decides if she wants the one-pager anyway.)
- **Carpet / commercial-multifamily flooring installation (NJ)** — NOT ADVANCED here (Kay-directed; runs the full screen per inbox). Construction-adjacent soft-exclude (trades + building products), low-margin install-labor, project-based. Surfaced for Kay's explicit screen request; flagging soft-exclude at scoring.
- **Insurance-fed warranty residential pipe installation (B2B2C)** — NOT ADVANCED. Construction/trades-adjacent + residential B2C end-customer; attractive lead-gen structure (insurer-fed) but fails core excludes. Surface for Kay (Matt sending approved-provider list).
- **VA-benefits consultancy** — NOT ADVANCED. Lifecycle near-DEAD: B2C end-customer + severe regulatory headwind (CA fee-ban end-2026, LA caps, "claims sharks" stigma). Web data materially weakens. Do not advance.
- **Whole-firm insurance acquisition / pure art advisory / art-tech platforms** — confirmed DEAD/KILLED per lifecycle tracker; not resurfaced.

**To one-pager + scorer:** (1) Fine-Art Logistics SERVICES, (2) Insurance FMO/IMO Distribution-Aggregator.

---
## [niche-intel-onepager: Fine-Art Logistics] — 2026-06-02 ET

**Status:** complete. One-pager built from template (NOT scratch) and uploaded.

**Pre-flight dedup:** No existing "Fine-Art Logistics" or "Storage" folder in WEEKLY REVIEW parent (1eq7Fjek...). Created NEW folder — this is the sharpened SERVICES-ONLY re-scope (strips capital-intensive storage), distinct from tracked #8 "Storage for HVA" and #9 "Trade Credit/Customs Bonds Insurance." No duplication.

**Drive:**
- New folder: `1cwIJl72r8nak7hReixXVOYtdj4gHsjPb` ("Fine-Art Logistics Services")
- Uploaded file: `1DHGw4k7n3YbUDjFGjXIQaUVnVpiMcw_7` (fine-art-logistics-onepager.pptx, 167KB)
- pptx: slide 0 = all 6 template shapes preserved (2 lines, 16r×2c table, logo, 2 text boxes); slide 1 = Sources (14 live hyperlinks across 4 source groups). Assessment/Status left "Pending Scoring" for Step 4 scorer.

**Key research findings feeding scoring:**
- **Margins:** Services layer ~15-25% EBITDA (install/customs highest, trucking lowest) vs storage 5-16%. Source: gather/synthesize (Levi/Acumen — storage 16% Queens) + identifier quick-screen.
- **Recurring %:** ~60% convertible to retainer/contract; referral-locked gallery/estate relationships, project-based individual jobs but high stickiness.
- **CAGR / growth:** ~4.1-4.7% market CAGR. Global fine-art logistics $3.5-4.06B (2025-26) -> $5.3-6.13B by 2034-35. Sources: BusinessResearchInsights (4.7%), OpenPR (4.1%), Mordor.
- **TAM:** US services slice est. ~$1-2B (of ~$3.5-4B global). ~150-300 US operators, mostly family/owner-run; ~5-8 PE platforms.
- **Exit comps (proven, active):** Crozier Fine Arts (Iron Mountain) — acquired Artex 2018, Martinspeed 2021; UOVO — acquired Museo Vault, regional roll-up; Cadogan Tate (TSG Consumer Partners, formerly H2 Equity) — acquired Wetzel & Sons, Art Logistics Ltd. Plus Atelier 4, Craters & Freighters (~65 loc).
- **Warm access:** Warren Chan/Anacapa (HOT, ~June 9, art-services validation); Levi/Acumen, Graham, Chris Wise contacts live. RIGHT-TO-WIN HIGH (luxury-service + art-network depth).
- **Caveats for scorer:** trucking line labor-heavy/low-margin (weight services MIX toward install/customs); must NOT drift into storage real estate; multi-partner ownership (Acumen) = investor deal-killer, screen single-owner; medium PE-consolidation risk but platform service degradation = independent whitespace.

---
## [niche-intel-onepager: Insurance FMO-IMO] — 2026-06-02 ET

**Status:** complete. One-pager built from template (cloned, NOT scratch) and uploaded.

**Pre-flight dedup:** Checked WEEKLY REVIEW parent (1eq7Fjek...). No existing FMO/IMO or distribution-aggregator folder. This is the upstream wholesale DISTRIBUTION layer (override commissions on agent production) — distinct from tracked retail-brokerage niches #7 Art & Collectibles, #10 HNW Personal Lines, #13 Surplus Lines (those SELL policies to end-clients and carry the DEAD whole-firm-acquisition lifecycle flag). No duplication. Created NEW folder.

**Drive:**
- New folder: `1se2WtUaF11jY3iDvgsgjQGmVuDDFJV8i` ("Insurance FMO-IMO Distribution-Aggregator")
- Uploaded file: `1MsgsYjjc-8uYAZCHuLDj-9E4h6sqhU2e` (insurance-fmo-imo-onepager.pptx, 168KB)
- pptx: slide 0 = all 6 template shapes preserved (2 lines, 16r×2c table, logo, 2 text boxes); slide 1 = Sources (23 live hyperlinks across 4 source groups). Assessment/Status left "Pending Scoring" for Step 4 scorer. No "Kay" anywhere — G&B only.

**4 INITIAL SCREEN data points feeding scoring:**
- **Margins:** STRONG — capital-light override revenue, no reserves/underwriting risk/balance sheet; low marginal opex (people/marketing/lead-gen). Healthy EBITDA margins typical for override-driven distributors. Exact % not publicly disclosed (private firms); structurally high-margin. Source: gather/synthesize + Ritter/AgentSync override mechanics.
- **Recurring %:** HIGH — override + renewal/trail commissions recur with the agent network's in-force block; override stream travels with the network (no client-book portability problem). Distinct advantage vs retail brokerage.
- **CAGR / growth:** ~5-7% distribution-layer growth, driven by record annuity wave. US retail annuity sales $464.1B in 2025 (+7% YoY, 4th consecutive record year); FIA $127.9B; RILA +20% to $79.6B. Source: LIMRA 2026.
- **TAM:** Multi-$B override layer on top of $464B annuity flow + life/Medicare. Hundreds of FMO/IMO/BGAs nationally (no fixed definition = long fragmented tail). Target pool: mid/small owner-run majority; ~3 dominant PE consolidators at top.

**Exit / PE pressure (real, names specific):**
- Integrity Marketing Group — Silver Lake $1.2B investment (2021), founder/employee-majority; serial acquirer (AIMCOR Jan 2026, Consolidated Marketing Group).
- AmeriLife — Genstar Capital + Thomas H. Lee Partners, $3B+ valuation.
- Simplicity Group — Lee Equity Partners majority (2020) + SkyKnight Capital + Dragoneer (2024); 15+ distribution businesses. Earlier backer Aquiline Capital.

**Caveats for scorer / pressure-test on independent pool:**
- THIN NAMED-TARGET POOL — single historical source (Jeremy Black "Jolene" description, NOT a named live target). No specific independent target surfaced this cycle. Advancing as one-pager + **target-discovery PROBE** to validate the independent mid/small pool BEFORE committing channel resources.
- PE consolidation MEDIUM-HIGH at top tier (Integrity/AmeriLife/Simplicity aggressively buying mid-tier, bidding up multiples + thinning pool) — opportunity is mid/small tier below the Big Three.
- Carrier DISINTERMEDIATION risk (direct-to-consumer / digital could compress overrides) — primary structural risk to monitor.
- Confirm B2B agent-network economics (override on agent production) vs any B2C drift — relationship is B2B with agents/carriers; end-policyholders are retail but not the FMO's commercial counterparty.
- Screen for SINGLE-OWNER succession targets (multi-partner ownership = investor deal-killer per art-storage precedent).

---
## [niche-intel-scorer] — 2026-06-02 23:58 ET

**Source:** INDUSTRY scorecard scoring of both advanced niches against `scorecard-structure.md` (TEMPLATE tab, 8 weighted categories, +/+-/- → 3/2/1, normalized /3). Status: complete. 2 scorecards uploaded, 2 one-pagers updated, folders deduped (1 scorecard + 1 one-pager each).

### NICHE 1 — Fine-Art Logistics Services
- **Overall: 2.39 / 3 (79.6%) — PROMISING**
- Category breakdown: Mission Criticality 3.0, Impact 3.0, Porter 2.5, Value Creation 2.5, Growth 2.25, Size & Frag 2.0, Industry Economics 2.0, Exogenous Risk 2.0.
- **INITIAL SCREEN: 4/4 PASS** — Margins PASS (services 15-25% EBITDA), Recurring PASS (~60% convertible, referral-locked), Growth PASS (~4-5% vs GDP ~3%), TAM PASS (US services ~$1-2B).
- **WEEKLY REVIEW columns:** Margins = Medium (15-25%); Recurring Revenue = Medium (~60% convertible); AI Defensibility = High (physical white-glove handling, low-tech, AI-resistant); Right to Win = STRONG (Chanel/luxury-service + art-network depth); Network Access = STRONG (Warren Chan/Anacapa warm path ~June 9, Levi/Graham/Chris Wise live).
- **Target pool:** ~150-300 US operators, majority independent/owner-run (~5-8 PE platforms). Sprint: long (50+ tail).
- **Verdict:** Strongest net-new of the cycle — warm-access + right-to-win edge; weight services MIX to install/customs (trucking labor-heavy), avoid storage real estate, screen single-owner targets.
- **Scorecard file ID:** `1fZxFGvKxtrcG4JyC7yltWnE2ZN7iV6Hs`
- **One-pager:** UPDATED with score (new ID `1KpO70vnxYlS_cwNsDgqGzmteDRY11ZIa`); old file deleted, folder deduped.

### NICHE 2 — Insurance FMO/IMO Distribution-Aggregator
- **Overall: 2.20 / 3 (73.5%) — MODERATE**
- Category breakdown: Industry Economics 2.67, Mission Criticality 2.33, Growth 2.25, Porter 2.17, Size & Frag 2.0, Exogenous Risk 2.0, Value Creation 2.0, Impact 2.0.
- **INITIAL SCREEN: 4/4 PASS** — Margins PASS (capital-light overrides, structurally high), Recurring PASS (override/renewal recurs with in-force block), Growth PASS (~5-7% on record annuity wave, $464B 2025), TAM PASS (multi-$B override layer).
- **WEEKLY REVIEW columns:** Margins = Very High (capital-light override, no balance sheet); Recurring Revenue = High (override/trail recurs with agent network); AI Defensibility = Medium (carrier disintermediation / digital-direct is the structural risk); Right to Win = MODERATE (weaker — no direct FMO/insurance-distribution background); Network Access = SOME/THIN (single historical source, no named live target).
- **Target pool:** Hundreds of FMO/IMO/BGA orgs nationally but THIN NAMED pool — needs target-discovery probe. Sprint: focused (20-50, pool unvalidated).
- **Verdict:** Structurally sound but thin named pool + high regulatory exposure + carrier-disintermediation risk; advance as target-discovery PROBE to validate independent mid/small tier below Integrity/AmeriLife/Simplicity before committing channel resources.
- **Scorecard file ID:** `1cdBW9emWbutPqtW6FWxiYA78RSyqap25`
- **One-pager:** UPDATED with score (new ID `1QfEL9glJSz87X9E8famSHiDOW9nWFqr-`); old file deleted, folder deduped.

**Drive failures:** none. All uploads/deletes succeeded first attempt.
**Handoff to tracker:** both niches scored; Fine-Art Logistics 2.39/3 (note re-scope decision vs tracked #8 Storage is Kay's call per identifier), FMO/IMO 2.20/3 (probe-gated). Orchestrator owns the brain/outputs report.

## [niche-intel-tracker] — 2026-06-02 22:41 ET
Tracker write COMPLETE. WEEKLY REVIEW tab (IDEATION archived per policy — both niches appended to WEEKLY REVIEW).
- **Pre-write count:** 16 niche rows (ranks 1-16, sheet rows 4-19).
- **Appended:**
  - **Rank 17** — Fine-Art Logistics Services (sheet row 20). Status "New - Pending Review", Score 2.39, QSBS "Likely Eligible", Target Pool "150-300", Channel blank, Start 6/2/2026. Notes intact (re-scope caveat vs #8 Storage preserved).
  - **Rank 18** — Insurance FMO/IMO Distribution-Aggregator (sheet row 21). Status "New - Pending Review", Score 2.20, QSBS "TBD", Target Pool "Hundreds (thin NAMED pool)", Channel blank, Start 6/2/2026. Notes intact (probe-gated caveat preserved).
- **Post-write count:** 18 niche rows. Delta +2 (matches expected).
- **Verification:** Re-read A19:K21 — both rows landed with full notes, no comma/pipe mis-parse (used --values-json). Score 2.20 renders as numeric "2.2" (value correct). Days in Review (K) left blank as instructed.
- **tracker_updated: true**

---
## [23:00] orchestrator — RUN COMPLETE
All 5 pipeline steps executed and verified. Integrity validator PASSED.

**2 niches advanced to WEEKLY REVIEW (ranks 17 & 18, status New - Pending Review):**
1. **Fine-Art Logistics Services — 2.39/3 (PROMISING)** — asset-light services layer only (crating / fine-art trucking / installation / customs brokerage), strips capital-intensive storage. 4/4 screen pass. Services-only re-scope of #8 — analyst call decides re-scope vs net-new. Warm access Warren Chan/Anacapa ~June 9. Folder `1cwIJl72r8nak7hReixXVOYtdj4gHsjPb`.
2. **Insurance FMO/IMO Distribution-Aggregator — 2.20/3 (MODERATE, probe-gated)** — wholesale distribution/override layer, 4/4 screen pass, thin named pool → target-discovery probe before channel commitment. Folder `1se2WtUaF11jY3iDvgsgjQGmVuDDFJV8i`.

**4 surfaced-not-advanced** (heat-transfer label mfg = one-off target not a niche; carpet/flooring + warranty-pipe install = construction/trades excludes; VA-benefits = near-dead). **3 DEAD/KILLED confirmed not resurfaced** (whole-firm insurance acquisition, pure art advisory standalone, art-tech platforms).

Artifacts: report `brain/outputs/2026-06-02-niche-intelligence-report.md`, sidecar `brain/trackers/niches/niche-intel-2026-06-02.json`, 2 one-pagers + 2 scorecards in Drive. Source gaps (OneNote MCP, ChatGPT export, Granola MCP headless) documented as recurring infra open loops.
