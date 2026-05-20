---
schema_version: 1.0.0
date: 2026-05-19
task: Niche Intelligence Tuesday run — 5-step pipeline
agents: [niche-intel-recent, niche-intel-historical, niche-intel-synthesizer, niche-intel-identifier, niche-intel-onepager, niche-intel-scorer, niche-intel-tracker]
status: complete
tags:
  - date/2026-05-19
  - trace
  - topic/niche-intelligence
---

# Agent Chatroom: Niche Intelligence — Tuesday 2026-05-19

Headless launchd run. Pipeline: GATHER (parallel) → SYNTHESIZE → IDENTIFY → ONE-PAGER (parallel) → SCORE → UPDATE.

## Active + Pending Niches (WEEKLY REVIEW — do NOT re-propose)
1. Premium Pest Management (Luxury Hospitality) — Active-Outreach, JJ-Call-Only, 2.73
2. Private art advisory firms — Active-Outreach, Kay Email, 2.73
3. Estate Management Companies — Active-Outreach, DealsX Email, 2.6
4. Specialty Coffee Equipment Service — Active-Outreach, DealsX Email, 2.55
5. High-End Commercial Cleaning — Active-Outreach, DealsX Email (launches 7/20)
6. Vertical SaaS for Luxury & High-Value Asset Service Industries — Active-Outreach, DealsX Email
7. Specialty Insurance Brokerage (Art & Collectibles) — Active-Long Term, 2.81
8. Storage & Related Services for High-Value Assets — Active-Long Term, 2.35
9. Trade Credit, Customs Bonds & Cargo Insurance Brokerage — New (5/6), 2.75
10. Property Tax Appeal Services (Commercial) — New (4/4 reconciled 5/6), 2.58
11. OSHA Workplace Health & Safety Compliance Training (eLearning) — New (5/12), 2.56
12. Aviation Insurance Brokerage — New (5/12), 2.54
13. HNW Personal Lines Concierge Insurance Brokerage — New (5/12), 2.53
14. Funeral Home Management Software — New (5/12), 2.41
15. Surplus Lines Compliance & Tax Filing Services — New (5/12), 2.20

## KILLED (do NOT propose — failed for documented reasons)
Family Office Enablement, Luxury Property Maintenance, Art Tech Platforms, Birthing Facility Compliance, Fertility Clinic Software, Concierge medicine, Software Publishers (broad), Interior Design Services (broad), Admin/General Management Consulting (broad), All Other Personal Services (broad), Tech-Enabled Fiduciary Services, Trust/Fiduciary/Custody, Ambulatory Health Care (broad), Condition Reporting Tools, Children playrooms, Fine Art Escrow Software, Conservation/Restoration, Insurance Claims Specialist, Premium Finance, BPO/Business Support, Sustainability Consulting, Wine Storage, Fashion Storage, Pool/Spa Health Compliance, Collection Mgmt/Risk Doc, 3rd Party Licensing Tech, Subscription Gardening, ADA Accessibility, Compliance E-Learning General, Document Lifecycle/Archival, Customs Bonds & Cargo Insurance (original — now resurfaced as Trade Credit/Customs/Cargo bundle), Insurance Producer License Compliance, Customs Bond Specialty Brokers, Fire Protection & MEP, Tree Care, Healthcare Regulatory Compliance SaaS, Premium Audit & Loss Control, Veterinary Practice Mgmt Software, IMO/FMO Aggregator, Insurance Back-Office BPO basic-claims, Environmental Compliance Consulting, Managed Cybersecurity Compliance, Workplace Compliance Training General (non-OSHA).

## TABLED (can resurface only with new data addressing original reason)
EV Software/Charging, Other Computer Related Services, Escrow & Custodial Software, Specialized Document Lifecycle, Corporate Entity & Record Mgmt, Yacht/Fleet Maintenance Software, Legal Software, High-End Property Mgmt Platform, High-End Electrical & Lighting, High-End Property & Asset Mgmt Services, Landscape HNW, Surgical Episode Mgmt SaaS, Back Office Concierge Practices, Compliance & Packaging SaaS, Backup Care, Healthcare SaaS (Derm/Aesthetics), Pest Mgmt Compliance Software (4/12 — paired with Premium Pest), SEC Filing Prep & XBRL Tagging (4/2), Domestic Trade Credit Insurance (3/21).

## Pipeline Pressure Note (input to identifier)

Kay enters Wednesday with **7 unprocessed candidates** (rows 9-15) from last week's run still in "New - Pending Review." Add fewer, stronger candidates this week (1-3 high-conviction) rather than padding to the 5-niche cap. The analyst call only has so much oxygen.

---

## [niche-intel-historical] — 2026-05-19 22:50
**Status:** partial — orchestrator-executed (Agent tool unavailable in env; 4 tracks run sequentially through direct tool calls)

### Sub-Agent Coverage
- hist-calls: complete — 22 historical call notes scanned (Aug 2025 – Apr 2026, skipped May 2026 last 14d)
- hist-email: complete — 5 query buckets, ~120 thread metadata + 1 deep-read (Jeremy Black 2/3 specialty insurance email)
- hist-onenote: unavailable — OneNote MCP not registered in env; skipping. Would have scanned INDUSTRY MEMOS, INDUSTRY CONFERENCE LISTS, COMPANY MEMOS, DEAL CONV, R AND D - SEARCH STAGE, OPERATOR/INTERMEDIARY/SEARCHER CONVOS
- hist-chatgpt: pre-processed — raw export was consolidated into memory files on 2026-03-16 (`project_thesis_evolution.md`, `project_deal_history.md`, `project_network_contacts.md`, `project_frameworks_scorecards.md`). Pulled signals from those files instead of re-reading 18,600-message JSON.

### Cross-Source Signals (2+ sub-agents)

**1. Specialty Insurance — HNW Personal Lines Carve-Out / Concierge (Yennie/PRMS pattern)**
- hist-calls (Aug Felker 11/19, Hunter 1/12) + hist-email (2 years of DocSend tracking on "Specialty Insurance Brokerage Analysis" deck across all top investors Jan–Mar 2026) + ChatGPT-derived `project_deal_history.md` (PRMS #1 target — Celia Santana CEO, plus J.W. Allen / Genser / Grober Imbey / Hamptons Risk / DRO already named) + ChatGPT-derived `project_thesis_evolution.md` (Aug Felker Oct 2025 trigger)
- Synthesis: WEEKLY-REVIEW row 13 (HNW Personal Lines Concierge) has substantially MORE historical conviction than its 2.53 score implies. Aug 11/19 quote on the "two women near retirement specialty brokerage" target is essentially the platonic version of this niche — personal-lines-only, "very sticky, very high recurring revenue, ~100%", explicitly endorsed by Felker as "really valuable." Hunter 1/12 raised the 12-14x multiple wall but specifically called out carve-out path (fine art dept from larger firm) as a workaround.
- Quant data: Personal lines HNW ~100% retention, double-digit annual premium increases (climate driving), 25-35% EBITDA margins. Wall: 12-14x multiples on whole-brokerage acquisitions; carve-outs and "two-women retiring" deals may clear lower.

**2. Trade Credit Insurance + Customs Bond Brokerage (Jeremy Black named)**
- hist-email (Jeremy Black 2/3/26 — `subject:Insurance Contact & Two Insurance Ideas`, msg id `19c250d5143e6b7a`) + hist-calls (Jeremy Black 2/2/26) + WEEKLY-REVIEW row 9 (Trade Credit/Customs/Cargo bundle just landed 5/6 at 2.75)
- Synthesis: Jeremy Black sourced THE bundle that became row 9 — his 2/3 email named Trade Risk Group / Trade Acceptance Group / Texel (former Meridian) by name as carriers. He explicitly framed both as "VERY recurring" (customs bonds) and "under-utilized in the US, growth opportunity" (trade credit). Already-tracked but historical depth supports prioritization within the 7 pending candidates.
- Quant data: Jeremy's own firm spent $10-13K/year on trade credit coverage. Carriers: Euler Hermes/Allianz Trade, Atradius, Coface. Ex-Im Bank as alternative broker channel for >51% US-made exports.

**3. Insurance Back-Office Shared Services (Camilla 2/4 + Jeremy 2/2 same week)**
- hist-calls (Camilla 2/4 "shared services for sales agents — beyond insurance to any sales vertical"; Jeremy Black 2/2 transcript lines 1148-1180 — friend ran multi-State-Farm-agent back office, "$200K/year from each agent")
- Synthesis: Two independent named operators describe the same model in the same week: outsourced back-office for distributed agents (State Farm precedent; transferable to fine art brokers wanting to break out of consolidator firms). Already KILLED for "basic claims" variant per `feedback_no_lending`-adjacent BPO exclusions, BUT the State-Farm-multi-agent variant is a NEW configuration not in killed list. Worth raising as a clarification question, not a fresh proposal.
- Status: FLAG, do not propose; check whether KILLED's "Insurance Back-Office BPO basic-claims" specifically excludes producer/agent-services variant.

**4. Vertical SaaS Defensibility — Govtech / High-Cost-of-Failure**
- hist-calls (Jake Stoller/Riverside 4/10 "govtech, healthcare, investigations. Slow AI adoption curve because mistakes are catastrophic"; Jeff Stevens 4/22 echoed "bridge construction software" angle Kay had already been scoping; Katie Walker 4/16 "Datacor was my first deal, I understand the thesis")
- Synthesis: Three of Kay's most credentialed advisors converged on the same Vertical-SaaS defensibility lens within a 12-day window (Apr 10–22). Maps to WEEKLY-REVIEW row 6 (Vertical SaaS for Luxury & High-Value Asset Service Industries) but the historical signal points to a DIFFERENT vertical — government / high-cost-of-failure infrastructure rather than luxury-asset-service. Possible parallel candidate or scope tweak to row 6.
- Quant data: Jake's bid range for 13% growth / 15M ARR / 25% EBITDA mid-90s GR = 15x EBITDA / 4-4.5x ARR. Same profile at $4M ARR = 3-3.5x ARR. $5.5M ARR / 35-40% growth = 7x+ ARR competitive process. Buy-box-relevant.

**5. Art Packing/Transport (Santa Fe lead) — Geographic Variant**
- hist-calls (Jeremy Black 2/2 — Santa Fe art transport listing, "strong margins, established team, retiring owner"; Margot Romano 4/4 — "art services > advisory, storage/logistics/lending"; Acumen 9/17 + 10/30 — extensive industry intel) + ChatGPT-derived: Acumen as Deal 2 already negotiated at $5M
- Synthesis: Multiple sources converge on art-services-not-advisory direction. Santa Fe lead from Jeremy is concrete and presumably still listable. Currently WEEKLY-REVIEW row 8 is "Storage & High-Value Assets" at 2.35 (Active-Long Term) — art transport is adjacent but distinct sub-segment with arguably stronger margins (Acumen Queens storage = 16%; transport = single-digit blended).
- Status: Likely a TABLED/resurface-with-new-data candidate, given Acumen experience capped at thin margins. Don't propose; flag if Santa Fe lead surfaces.

### Single-Source Signals (notable but unconfirmed)

- **MGA Build vs Acquire** — Mark Gardella 3/31 (Sertis CEO, MGA). Suggested fine art MGA build path; offered intro to Markel fine art practice ex-head. Build path = NOT acquisition niche; tag as "river-guide intel, not target niche." No follow-up.
- **Heat Transfer Manufacturing / Sublimation** — Jeremy Black 2/2 transcript on Kay's Love Unlimited NY deal; Jeremy mentioned collegiate retail crossover (40 top schools, $13-17M/store at U of Arizona). Already passed by Kay (margins/recurring); collegiate licensing as parallel niche was Jeremy's pivot. Outside buy-box per `feedback_b2b_only_dealsx`.
- **Roadside-Assistance-as-Bundle (Assurian model)** — Camilla 2/4 anecdote from founder podcast. Kay's takeaway: "shovel connected to a growing wave" — the META-pattern, not a niche proposal.
- **Sports Facility Management with Real Estate** — Ali Doswell's WSN deal (3/30 call). Multi-decade management contracts + owned facilities; ~half EV in real estate; municipal profit-share contracts dragged EBITDA. Outside G&B thesis but interesting market-structure data point if Kay ever entertains adjacencies.
- **Marble & Granite Fabrication/Installation** — Megan Lawlor's LOI (Apr 1 call), warm Twitter intro path. Family-owned 30 years, recession/pandemic/tariff durable. No recurring revenue (her investors flagged). Outside G&B box but useful as B2C-adjacent test case.
- **Specialty Coffee Equipment Servicing — In-house vs Outsource Diagnostic** — Jeff Stevens 4/22 raised this as the open diagnostic question on WEEKLY-REVIEW row 4. Mid-sized chains (Joe Coffee, Blue Bottle scale, not Starbucks): in-house or outsource? Still unanswered. **Action for one-pager refresh:** answer this before next analyst call.
- **Insurance Producer License Compliance** — Camilla 2/4 + Kay's separate noodling. KILLED per memory but Camilla independently arrived at the same idea, suggesting it intuitively appeals. Don't resurface unless new data addresses kill reason.

### Already-Tracked Overlaps (new supporting data only)

- **Premium Pest Management (row 1)** — Jeff Stevens 4/22 reinforced "gaining conviction," noted Women in Pest association exists, organic-growth-via-coverage-expansion is a structural positive. No change needed.
- **Specialty Coffee Equipment Service (row 4)** — Jeff Stevens 4/22 added diagnostic Q (above), supports keeping in WEEKLY REVIEW but flagged scope ambiguity (NYC market depth, mid-sized chains in/outsource decision).
- **Specialty Insurance Brokerage Art & Collectibles (row 7)** — Aug Felker 11/19 + Hunter 1/12 + BofA Margot 4/4 collectively the deepest-documented niche in Kay's history. Already Active-Long Term so the historical depth confirms placement; flag is that PRMS/Genser/Yennie targets in `project_deal_history.md` may still be in play but never converted — worth a cadence check on those specific named owners.
- **HNW Personal Lines Concierge (row 13)** — see Cross-Source Signal #1. Score 2.53 likely understates; resurface for re-score with Aug Felker's 11/19 endorsement explicitly cited.
- **Trade Credit/Customs/Cargo bundle (row 9)** — see Cross-Source Signal #2. Original sourcing from Jeremy Black surfaced. Prioritize within pending-7 backlog.
- **Aviation Insurance Brokerage (row 12)** — supported by 1/27 Helen Guo deal-flow newsletter + multiple E&K deal teasers featuring aviation-adjacent (precision machining for aerospace, etc.). Already in pipeline at 2.54.
- **Storage High-Value Assets (row 8)** — Acumen 9/17 + 10/30 + Hangman in `project_deal_history.md` + Margot 4/4 reaffirm Active-Long Term placement.
- **Funeral Home Management Software (row 14)** — no historical hits; placement stands at 2.41 on pure recent-week data.

### Lead Lifecycle Flags (proposed AND challenged)

- **MGA-build pathway** — proposed by Mark Gardella 3/31; challenged by Tobias Marshberry 3/31 same day ("space heavily rolled up, valuations sky-high, start your own"). Status: **DEAD as acquisition niche** — both sources converge on "build, don't buy" which is outside Kay's mandate. The "build vs acquire" pattern is a recurring meta-signal: insurance brokerage at large gets the "start your own" recommendation repeatedly (Tobias, Mark, prior contacts per his note). Do not propose insurance brokerage build paths.
- **Pure Art Advisory (Schwartzman-style)** — proposed by 2 contacts in art space (per Jeff 4/22); challenged by Margot Romano 4/4 ("not sure good money in pure advisory, retainer-only is more attractive, advisory needs services bolt-on") and Jeff Stevens 4/22 (key-person risk, "wealth managers and high-end realtors take their book"). Status: **LIVE but constrained** — already WEEKLY-REVIEW row 2 at 2.73; row should carry forward Margot+Jeff caveats (filter to advisory+services, NOT pure advisory).
- **Brokered Deal Flow** — recommended by some traditional investors; challenged by traditional-search community at Kristin Wihera 4/23 WSN session ("If you're winning a broker deal, something's wrong — 35% IRR can't beat PE's 20% in a bidding war"). Status: NOT a niche question, but a sourcing-channel pattern relevant when scoring next-week candidates.
- **AI as Riding-the-Wave Niche** — proposed (Kay+Camilla 2/4); challenged (Camilla same call: "saturated, plateaued"). Status: **DEAD as niche** — AI is a defensibility lens, not a niche. Aligns with `feedback_ai_disruption_filter.md`.

### Companies Surfaced (most actionable, not already in DealsX/target sheets)

1. **Trade Risk Group** (traderiskguaranty.com) — customs bonds & cargo insurance specialist. Named by Jeremy Black 2/3. Possible target OR river guide.
2. **Trade Acceptance Group** (tradeacceptance.com) — trade credit broker. Jeremy's former vendor.
3. **Texel Group** (thetexelgroup.com) — formerly Meridian, trade credit. Jeremy's current vendor.
4. **Schwartzman & Associates** — ~4-person art advisory, Margot 4/4. Within buy box for advisory+services pivot.
5. **Datacor** (chemical distribution vertical SaaS) — referenced by Katie Walker 4/16 as Plexus's first deal. Not a target, but underwriting precedent.
6. **Maquette / SAT / Art Crating / Crozier / UOVO** — art-storage competitor map from Acumen 10/30. Competitive context for any new art-storage candidate.
7. **Trane** — Ali Doswell's prior employer (commercial HVAC). Tangential.
8. **Sertis** — Mark Gardella's MGA, Reno NV, ~17 employees. River guide.
9. **Voxme Software** — Acumen migrating to. Vertical SaaS for art logistics. Potential HoldCo niche candidate; size unknown.
10. **Hangman Fine Arts** — David Hurwitz, prior deal (passed). Source of art-services margin doctrine.
11. **PRMS / J.W. Allen / Genser / Grober Imbey / Hamptons Risk / DRO** — specialty insurance named targets in `project_deal_history.md`. Cadence check warranted; none have converted to LOI in ~5 months.
12. **Markel Insurance fine art ex-head** — unnamed contact via Mark Gardella 3/31. Pending intro.
13. **Princess Donut / Openclaw** — Austin Yoder's AI build (2/19 call) — NOT a target, but reference architecture.
14. **State Farm multi-agent back-office model** — Jeremy 2/2 named pattern. No specific firm.
15. **Santa Fe art transport firm** — Jeremy 2/2 broker listing, name not captured. Retiring owner, strong margins.
16. **Helen Guo (SMB Deal Hunter)** — newsletter source, multiple deal-flow signals.
17. **Caprae Capital** (Kevin Hong) — Megan's cold-calling vendor, NOT a target, sourcing infrastructure.
18. **DealsX / SmartLeads** — Megan's email vendor. Already adopted by G&B.
19. **Plexus Capital** — Katie Walker's firm. Lender, not target. (Jeff's 4/22 cautionary color noted.)
20. **Anacapa Sarah Got Steel portco** — Jeff Stevens 4/22, Sarah Rowell endorsed. Not a target, network node.

### Contacts Surfaced (potential river guides not already engaged or warmer than tracked)

- **Markel fine art ex-head** (name TBD) — Mark Gardella 3/31 offered intro. Specialty insurance river guide. WARM — pending Mark follow-through.
- **Jonathan Crystal** (longtime NY insurance agency expert, ex-Sotheby's head auctioneer fine jewelry insurance) — Hunter Hartwell 1/12 promised intro. WARM — pending Hunter follow-through.
- **Adeline / Iris / Schiovana / Laura / Marta** (WSN April 4/23 attendees with Kristin) — peer searchers, varying stages. Adeline has 4.1x LOI on a proprietary boutique-bank channel; under LOI. WARM peer.
- **Jolene** (deceased) — Jeremy Black's mom's client, ran insurance-marketing org that aggregated broker/agent groups for annuity/life policies. Business sold a decade ago. DEAD lead but interesting model.
- **Gonzalo** (Megan Lawlor's AI engineer) — WSN 3/30 offered intro. Not a niche guide; AI build infrastructure.
- **Sarah Goodman (Eminence M&A) / Leonardo Ferreira (Hillview Partners)** — Axial Outlook 4/23, bullish 2026 voices. Cold but visible.
- **Dana** (Camilla 2/4 retiree) — generic warm intro. Sector unspecified.
- **Anna Raginskaya** (Morgan Stanley PWM) — art insurance intro (email 1/13/26, msg `19bae89f909f6e48`). WARM, existing thread.
- **Scott Etish** (Coventry) — 4/23 article share on Life Insurance & Fiduciary Considerations. WARM, in respond bucket.

### Synthesis Note for Next Pipeline Step

Given Kay enters Wednesday with **7 unprocessed candidates** (rows 9-15), the historical scan suggests:

1. **Do NOT add new niches this week.** The historical evidence reinforces existing pipeline rather than surfacing unmissed niches. Net-new proposable surface area: ~0 niches that pass the KILLED/TABLED filter AND have 2+ source confirmation AND haven't already been added.
2. **Re-score row 13 (HNW Personal Lines Concierge)** — Aug Felker 11/19 endorsement is materially stronger than current 2.53 reflects; the "two women retiring HNW personal-lines-only" target archetype is the cleanest fit in the entire history.
3. **Prioritize row 9 (Trade Credit/Customs/Cargo)** within the pending-7 — Jeremy Black was the original source AND provided named carriers/vendors, giving target-discovery a head start.
4. **Refresh row 4 (Specialty Coffee Equipment)** with the Jeff Stevens 4/22 diagnostic (mid-sized-chain in/outsource Q + NYC market depth) before next analyst call.
5. **Cadence check** on named insurance targets in `project_deal_history.md` (PRMS, J.W. Allen, Genser, Grober Imbey, Hamptons Risk, DRO) — these have sat without conversion ~5 months.

---

## [niche-intel-synthesizer] — 2026-05-19 23:05
**Status:** complete
**Convergent recommendation:** Both gathering agents converge on the same conclusion — the 14-day window surfaces NO net-new niche that clears KILLED/TABLED filters with 2+ source confirmation, while five already-pending insurance-brokerage rows sit inside one accelerating PE-consolidation wave. Action this week is depth not breadth: re-score row 13 (HNW Personal Lines, score understates Aug Felker conviction), prioritize row 9 (Trade Credit/Customs — Jeremy Black was original source with named carriers), refresh row 4 (Specialty Coffee Equipment — Jeff Stevens diagnostic).

### OUTPUT 1: CROSS-SOURCE SIGNAL MATRIX

| Niche / Signal | RECENT Sources | HISTORICAL Sources | Total Source Count | Strength |
|---|---|---|---|---|
| Specialty Insurance Brokerage (Art & Collectibles) — row 7 | Axios Pro Rata 5/14+5/19, Alvarez & Marsal, Marsh Berry, West Monroe | Aug Felker 11/19, Hunter 1/12, BofA Margot 4/4, DocSend tracking Jan-Mar | 8+ | VERY STRONG |
| HNW Personal Lines Concierge — row 13 | Axios + A&M + West Monroe (S1 PE wave) | Aug Felker 11/19 ("two women retiring HNW personal-lines" archetype), Hunter 1/12 (12-14x wall + carve-out workaround) | 5 | VERY STRONG |
| Trade Credit / Customs Bonds / Cargo — row 9 | Axios + A&M (S1 PE wave) | Jeremy Black 2/3/26 email naming Trade Risk Group / Trade Acceptance / Texel + Jeremy 2/2 call | 4 | VERY STRONG |
| Aviation Insurance Brokerage — row 12 | Axios + A&M + West Monroe (S1 PE wave) | Helen Guo 1/27 newsletter, E&K aerospace adjacencies | 4 | STRONG |
| Surplus Lines Compliance & Tax Filing — row 15 | Axios + A&M (S1 broker-MGA infrastructure layer) | — | 2 | STRONG |
| Premium Pest Management — row 1 | Carlos Nieto 5/13 (30-40% premium-bid blue-collar), This Week In ETA 5/8 (9-11x mults) | Jeff Stevens 4/22 (conviction reinforced, Women in Pest assoc) | 3 | STRONG |
| Specialty Coffee Equipment Service — row 4 | Carlos Nieto 5/13 (independently surfaced as queue candidate — convergence) | Jeff Stevens 4/22 (mid-sized chain in/outsource Q + NYC depth — diagnostic open) | 2 | STRONG |
| Vertical SaaS Luxury Services — row 6 | Krupa Shah 5/14 + Carlos Nieto 5/13 (AI-disruption pause) | Jake Stoller 4/10 + Jeff Stevens 4/22 + Katie Walker 4/16 (govtech / high-cost-of-failure defensibility) | 5 | STRONG (with scope-tweak signal) |
| Funeral Home Mgmt Software — row 14 | Krupa + Carlos (SaaS AI-risk envelope — CAUTION) | — | 2 | MODERATE (cautionary) |
| HVAC Service-Agreement Consolidation (potential) | Helen Guo (multiple listings 5/7-5/19), Carlos blue-collar premium, PE Hub | — | 2 | MODERATE |
| Commercial Roofing Industrial+Commercial (potential) | Helen Guo CA $1.7M EBITDA, ambient PE | — | 1 | WEAK |
| Commercial Plumbing federal/tribal credentialed (potential) | Helen Guo AZ $725K EBITDA (govt-credential moat) | — | 1 | WEAK |
| B2B Trade Magazine (meetings industry) | E&K $2.2M/$1M teaser | — | 1 | WEAK |
| Estate Mgmt Companies — row 3 | — | — | 0 (no new signal) | (placement stands) |
| Private Art Advisory — row 2 | — | Margot 4/4 + Jeff 4/22 (constraints: advisory+services not pure advisory) | 1.5 | MODERATE (constraint refinement only) |
| Storage High-Value Assets — row 8 | — | Acumen 9/17+10/30, Margot 4/4, Hangman (`project_deal_history.md`) | 4 | STRONG (Active-Long Term confirmed) |
| Property Tax Appeal — row 10 | — | — | 0 | (placement stands) |
| OSHA Workplace H&S Training — row 11 | — | — | 0 | (placement stands) |

### OUTPUT 2: NAMED COMPANY REGISTRY

| Company | Niche | Source | Est. Revenue / Independence | Outreach Flag | Notes |
|---|---|---|---|---|---|
| Trade Risk Group (traderiskguaranty.com) | Trade Credit/Customs (row 9) | Jeremy Black 2/3 email | Independent specialist | NEW_TARGET | Customs bonds & cargo specialty; possible target OR river guide |
| Trade Acceptance Group (tradeacceptance.com) | Trade Credit (row 9) | Jeremy Black 2/3 | Independent (Jeremy's former vendor) | NEW_TARGET | Trade credit broker |
| Texel Group (thetexelgroup.com — fka Meridian) | Trade Credit (row 9) | Jeremy Black 2/3 | Independent (Jeremy's current vendor) | NEW_TARGET | Trade credit, recently rebranded |
| Schwartzman & Associates | Private Art Advisory (row 2) | Margot Romano 4/4 | ~4-person, independent | NEW_TARGET | Advisory+services pivot fit |
| PRMS | Specialty Insurance (row 7) | `project_deal_history.md` | Independent, CEO Celia Santana named | VAULT_HISTORY | Cadence check — no conversion in ~5 months |
| J.W. Allen | Specialty Insurance (row 7) | `project_deal_history.md` | Independent | VAULT_HISTORY | Cadence check — stale |
| Genser | Specialty Insurance (row 7) | `project_deal_history.md` | Independent | VAULT_HISTORY | Cadence check — stale |
| Grober Imbey | Specialty Insurance (row 7) | `project_deal_history.md` | Independent | VAULT_HISTORY | Cadence check — stale |
| Hamptons Risk | Specialty Insurance / HNW Personal Lines (row 7/13) | `project_deal_history.md` | Independent | VAULT_HISTORY | Cadence check — stale |
| DRO | Specialty Insurance (row 7) | `project_deal_history.md` | Independent | VAULT_HISTORY | Cadence check — stale |
| Sertis (Reno NV) | (Not target — MGA build-path river guide) | Mark Gardella 3/31 | ~17 employees | WARM_INTRO | MGA build path; offered Markel fine art ex-head intro |
| Voxme Software | Vertical SaaS (logistics for art) | Acumen 10/30 | Unknown | UNKNOWN | Acumen migrating to; size unknown |
| Maquette / SAT / Art Crating / Crozier / UOVO | Art storage competitor map | Acumen 10/30 | Various | UNKNOWN | Competitive context only |
| Santa Fe art transport firm (name TBD) | Art transport (tabled) | Jeremy Black 2/2 | Retiring owner, strong margins | UNKNOWN | Name not captured; broker listing |
| Trade Risk Guaranty / similar customs bond shops | Customs Bonds (row 9) | Jeremy Black 2/3 | Independent specialists | NEW_TARGET | Bundle within row 9 universe |

**Cross-reference against Attio at next opportunity:** all NEW_TARGET rows above + the 6 VAULT_HISTORY insurance targets (PRMS / J.W. Allen / Genser / Grober Imbey / Hamptons Risk / DRO).

### OUTPUT 3: CONTACT-TO-NICHE MAP

| Contact | Warmth | Niches They Can Help With | What to Ask | Last Contact |
|---|---|---|---|---|
| Jeremy Black | HOT | Trade Credit/Customs (row 9), Insurance back-office variants | Intro to Trade Risk Group / Trade Acceptance / Texel; State-Farm multi-agent back-office firm names | 2/3/26 email |
| Aug Felker | HOT | HNW Personal Lines (row 13), Specialty Insurance (row 7) | Revisit "two women retiring HNW personal-lines" archetype; carve-out path leads | 11/19/25 call |
| Hunter Hartwell | WARM | Specialty Insurance (row 7), HNW Personal Lines (row 13) | Status of Jonathan Crystal intro (ex-Sotheby's fine jewelry insurance) | 1/12/26 call |
| Margot Romano (BofA) | WARM | Private Art Advisory (row 2), Storage HNV Assets (row 8) | Schwartzman & Associates intro; advisory+services pivot leads | 4/4/26 |
| Jeff Stevens | HOT | Pest (row 1), Coffee Equipment (row 4), Private Art Advisory (row 2), Vertical SaaS (row 6) | Coffee equipment mid-sized chain in/outsource diagnostic; bridge construction software angle | 4/22/26 |
| Mark Gardella (Sertis CEO) | WARM | Specialty Insurance river guide | Markel fine art ex-head intro status | 3/31/26 |
| Carlos Nieto (DCA) | WARM | Pest (row 1), Coffee Equipment (row 4), Vertical SaaS (row 6) | Coffee equipment queue candidates; PE blue-collar premium evidence | 5/13/26 call |
| Krupa Shah (STREAM) | WARM | Storage HNV Assets (row 8 — real-estate component), co-invest channel | Art storage warehouse deal resurfacing | 5/14/26 call |
| Katie Walker (Plexus) | WARM | Vertical SaaS (row 6) | Datacor-style vertical SaaS thesis precedent | 4/16/26 |
| Helen Guo (SMB Deal Hunter) | COOL | Deal-flow newsletter (broad blue-collar) | None — passive consumption channel | Newsletter 5/19/26 |
| Anna Raginskaya (MS PWM) | WARM | Art insurance (row 7) | Status of intro thread | 1/13/26 email |
| Scott Etish (Coventry) | WARM | Life Insurance & Fiduciary | Reactive — respond when Kay has bandwidth | 4/23/26 article share |
| Jonathan Crystal (TBD intro) | COOL | Specialty Insurance NY agency | Pending Hunter's intro | Never (pending) |
| Markel fine art ex-head (TBD) | COOL | Specialty Insurance (row 7) | Pending Mark Gardella's intro | Never (pending) |
| Sarah Goodman (Eminence M&A) | COLD | Sell-side intermediary | — (visibility only) | 4/23/26 Axial outlook |
| Leonardo Ferreira (Hillview) | COLD | Sell-side intermediary | — (visibility only) | 4/23/26 Axial outlook |

### OUTPUT 4: LEAD LIFECYCLE TRACKER

| Niche / Strategy | Proposed By | When | Challenged By | When | Reason | Status |
|---|---|---|---|---|---|---|
| MGA-build pathway (insurance brokerage start-from-scratch) | Mark Gardella | 3/31/26 | Tobias Marshberry | 3/31/26 | "Heavily rolled up, valuations sky-high, start your own" — both converge on BUILD, not BUY | DEAD (outside G&B acquisition mandate) |
| Pure Art Advisory (Schwartzman-style retainer-only) | 2 art-space contacts via Jeff 4/22 | 4/22/26 | Margot Romano 4/4 + Jeff Stevens 4/22 | 4/4–4/22 | "Not sure good money in pure advisory" / "key-person risk, wealth managers take book" | LIVE but constrained (row 2 carries Margot+Jeff caveats — advisory+services, not pure) |
| AI as Riding-the-Wave niche | Kay + Camilla 2/4 | 2/4/26 | Camilla same call | 2/4/26 | "Saturated, plateaued" — AI = defensibility lens, not niche | DEAD |
| Brokered deal flow as primary sourcing | Some traditional investors | 2025 | Kristin Wihera WSN | 4/23/26 | "If you're winning a broker deal, something's wrong — 35% IRR can't beat PE's 20% in bidding war" | LIVE as supplemental, NOT primary |
| Insurance Back-Office Shared Services (basic claims variant) | Multiple | Various | KILLED list | — | BPO basic-claims exclusion | KILLED |
| Insurance Back-Office (State Farm multi-agent variant) | Jeremy Black + Camilla converged | 2/2–2/4/26 | Not yet challenged | — | Same week independent observation; variant not specifically on KILLED list | LIVE (flag for clarification, do NOT propose this week) |
| Art Packing/Transport (Santa Fe lead, geographic variant) | Jeremy Black 2/2 + Margot 4/4 | 2/2–4/4/26 | Acumen experience (5-8% margins) | 9/17–10/30/25 | Transport blended margins single-digit; Acumen capped thin | TABLED |
| Add 5 new niches this week (cap-fill default) | Default niche-intel cadence | weekly | Both gather agents | 5/19/26 | 7 pending candidates from last week unprocessed; analyst-call oxygen finite | DEAD (this week) — depth over breadth |
| HVAC service-agreement roll-up | Helen Guo + Carlos (S4) | 5/7-5/19 | `feedback_searcher_overlap` (likely) | — | Very crowded, searcher overlap concern | LIVE (identifier discretion; bias TABLE) |
| Commercial Roofing (industrial+commercial) | Helen Guo $1.7M CA | 5/15/26 | `feedback_no_california` + searcher overlap | — | CA exclude on the specific deal; broader niche overlap risk | TABLED (identifier discretion) |
| Commercial Plumbing federal/tribal credentialed | Helen Guo AZ $725K | 5/15/26 | Not yet challenged | — | Govt-credential moat genuinely interesting, no prior eval | LIVE (identifier discretion — only candidate with no prior challenge) |
| B2B Trade Magazine (meetings industry) | E&K teaser $2.2M/$1M | 5/19/26 | `feedback_messy_business_great_segment_filter` | — | Media-publishing, recurring-revenue-light, segment quality questionable | DEAD (single data point, doesn't clear filter) |
| Single-asset Continuation Vehicles (services platforms) | PE Hub 5/15+5/18 | 5/15-5/18 | N/A — financing structure not niche | — | Holdco architecture reinforcement | DEAD (not a niche) |
| STREAM Capital co-invest channel | Krupa Shah 5/14 | 5/14/26 | N/A — channel not niche | — | Route to outreach-manager / relationship-manager | LIVE (channel, not niche pipeline) |

### OUTPUT 5: CONVERGENCE REPORT (Top 5 strongest signals)

**1. HNW Personal Lines Concierge (row 13) is materially under-scored at 2.53.**
The synthesis of Aug Felker's 11/19 "two women retiring personal-lines-only specialty brokerage" archetype (~100% retention, double-digit annual premium increases climate-driven, 25-35% EBITDA margins, explicitly endorsed "really valuable") combined with Hunter 1/12's confirmation that carve-out paths (e.g. fine art dept from larger firm) can clear the 12-14x whole-brokerage multiple wall, plus this week's PE-consolidation wave hitting the $500K-$10M revenue band — means row 13 is the cleanest archetype fit in Kay's documented history. Implication: a re-score with these citations explicit will move it ahead of several of the pending-7, changing analyst-call prioritization.

**2. Five WEEKLY-REVIEW insurance-brokerage rows sit inside ONE consolidation wave — depth over breadth this week.**
Rows 7, 9, 12, 13, 15 (Specialty Art & Collectibles, Trade Credit/Customs/Cargo, Aviation, HNW Personal Lines, Surplus Lines) are all inside the same Q1-Q2 2026 PE consolidation wave (Axios Pro Rata, Alvarez & Marsal, Marsh Berry, West Monroe). The "$500K-$10M revenue most pressure to consolidate" band aligns with G&B's relaxed sub-$2M-EBITDA hunting lane (per 2026-05-19 investor guidance). Implication: this week's analyst call should make advance-or-table decisions across these five rows rather than dilute oxygen with new candidates — the urgency signal applies equally to all five.

**3. Trade Credit/Customs/Cargo (row 9) has the sharpest target-discovery head start of any pending candidate.**
Jeremy Black was the original source AND provided three named carriers/vendors (Trade Risk Group, Trade Acceptance Group, Texel) plus quant data ($10-13K/yr his own firm spent, Euler Hermes/Allianz Trade/Atradius/Coface carrier landscape, Ex-Im Bank alternative channel for >51% US-made exports). Implication: row 9 should jump to the front of the pending-7 queue because target-discovery can begin immediately without an additional research pass.

**4. SaaS AI-disruption signal hardened (third independent source).**
Krupa Shah 5/14 ("stopped looking at software ~3 months ago due to AI disruption") + Carlos Nieto 5/13 ("AI disruption making investors cautious; last software deals closed ~January") + Jake Stoller 4/10 (govtech/healthcare/investigations defensible because mistakes catastrophic) form a triangulated warning. Funeral Home Mgmt Software (row 14) sits inside this risk envelope. Implication: row 14 needs a defensibility-vs-AI explicit answer in its one-pager or table; row 6 (Vertical SaaS Luxury) scope may need a tweak toward high-cost-of-failure / govtech adjacencies.

**5. Specialty Coffee Equipment Service (row 4) has independent peer-searcher confirmation but an unanswered scope question.**
Carlos Nieto 5/13 independently surfaced this as a niche-intel queue candidate (he doesn't know it's already row 4) — a clean convergence signal. But Jeff Stevens 4/22 raised a diagnostic question still open: do mid-sized chains (Joe Coffee / Blue Bottle scale, not Starbucks) keep this in-house or outsource? Plus NYC market depth unclear. Implication: row 4 needs a one-pager refresh that ANSWERS Jeff's diagnostic before next analyst call — not a re-score, but a research gap-fill.

### Handoff to Identifier
- **Signals evaluated:** 17 (14 active/pending niches reviewed for new signal + 3 potential new-niche surfaces examined: HVAC service-agreement, Commercial Roofing, Commercial Plumbing federal/tribal)
- **Recommended action:** Add 0 new niches. Instead: (a) re-score row 13 (HNW Personal Lines) citing Aug Felker 11/19 + Hunter 1/12; (b) prioritize row 9 (Trade Credit/Customs) within pending-7 because Jeremy Black gave named carriers; (c) refresh row 4 (Specialty Coffee Equipment) one-pager to answer Jeff Stevens 4/22 in/outsource diagnostic. If identifier insists on surfacing ONE candidate for analyst consideration: Commercial Plumbing federal/tribal credentialed (Helen Guo AZ $725K EBITDA) — only potential-new with no prior challenge logged.
- **Niche pool entering identifier:** [Commercial Plumbing federal/tribal credentialed] — single discretionary candidate. Plus three re-prioritization actions (re-score row 13, prioritize row 9, refresh row 4) that the identifier should pass through to the scorer/tracker rather than treat as new niches.
- **If pool is empty:** zero_finding_reason candidate string: "7 pending candidates from prior week unprocessed; convergent signal is depth not breadth — five insurance-brokerage rows sit inside one PE-consolidation wave demanding advance-or-table decisions; no net-new niche cleared KILLED/TABLED filter with 2+ source confirmation."

---

## [niche-intel-identifier] — 2026-05-19 23:20
**Status:** complete
**Decision:** Propose 0 new niches. Synthesizer's depth-over-breadth call is correct: 7 pending candidates already sit in "New - Pending Review," five of them inside one PE-consolidation wave demanding advance-or-table decisions. The single discretionary candidate (Commercial Plumbing federal/tribal credentialed) fails the 4-gate niche-level screen on credential-transferability + TAM scoping + sub-buy-box single data point.

### Candidates Evaluated

#### Candidate 1: Commercial Plumbing — Federal/Tribal Credentialed — SKIP

**4-GATE INITIAL SCREEN:**

1. **Margins (15%+ typical EBITDA):** MARGINAL → effectively FAIL at niche level.
   - Plumbing industry baseline: top-half average 22% EBITDA (IBISWorld), but most operators sit at 5-12%. Top quartile 15-20%+.
   - Commercial plumbing specifically can reach 20-40% with strong GC relationships and accurate bidding — but those are top performers, not the typical credentialed independent.
   - Federal/tribal credentialed work benefits from prevailing-wage protections and less competitive bidding pools, plausibly elevating typical margins above pure-commercial baseline, but project-based federal construction work also carries bonding costs, prevailing-wage admin overhead, and contract-payment delays that compress realized EBITDA.
   - The single Helen Guo data point ($725K EBITDA, AZ) does not disclose revenue → margin unknown for this specific target.
   - VERDICT: Cannot confirm the SEGMENT typically clears 15%; the credentialed-independent universe likely skews 8-15% with top performers at 20%+. **Fails the "typical" qualifier of the gate.**

2. **Recurring Revenue (existing or convertible):** FAIL.
   - Federal/tribal credentialed plumbing is dominated by project-based capital construction contracts (new construction, major renovation, IDIQ task orders) — episodic, not recurring.
   - Service-agreement / preventive-maintenance plumbing (the recurring-revenue slice of commercial plumbing) is a DIFFERENT segment, typically served by non-credentialed commercial operators because credentialed firms compete for higher-margin construction work.
   - "Convertible to recurring" thesis would require pivoting from construction → O&M, which is a fundamentally different business model (lower margins, different customer relationships, different workforce skills) — not a natural conversion path.
   - VERDICT: **Fails the recurring-revenue gate.** This is a project-based niche.

3. **Industry Growth (above GDP ~3%):** PASS.
   - Plumbing industry $170B US (IBISWorld 2025), mid-single-digit growth.
   - Federal infrastructure spending elevated through IIJA tail (~2026-2028), with tribal infrastructure dedicated tranches.
   - Above-GDP growth defensible.

4. **Growth TAM ($500M+):** MARGINAL → likely FAIL at acquirable-independent layer.
   - Federal procurement spend on plumbing-coded services (NAICS 238220 + related) is plausibly $2-4B annually across all federal agencies (DoD, VA, Interior/BIA, GSA, HHS Indian Health Service).
   - Tribal-specific plumbing spend smaller, perhaps $300-600M annually combining BIA, IHS, and tribal-government direct procurement.
   - HOWEVER: the ACQUIRABLE-INDEPENDENT subset (excluding mega-GCs running plumbing-subs internally — Fluor, MasTec subs, Bechtel subs, AECOM subs — and excluding the in-house Federal/tribal-government workforce) shrinks the realistic TAM substantially.
   - The credentialed-independent universe sized to G&B buy-box ($2-10M EBITDA, ~$10-50M revenue firms) is plausibly $200-500M TAM — **right at or below the floor.**
   - VERDICT: **Likely fails $500M floor when scoped to acquirable-independent segment.** Cannot confirm without a NAICS+SAM.gov pull, which is beyond this identifier-stage screen.

**ADDITIONAL DISQUALIFIERS (beyond the 4 gates):**

5. **Credential-transferability risk (CRITICAL DEAL STRUCTURE).** Federal small-business set-aside credentials — 8(a), HUBZone, SDVOSB, WOSB — generally do NOT survive ownership change to a non-qualifying acquirer. Tribal credentialing (TERO, tribal preference contracts) often requires tribal-member ownership or tribal-corp structure. A search-fund acquisition of a credentialed independent would likely STRIP the credential at closing, eliminating the primary moat that distinguishes the niche from generic commercial plumbing. This is a fatal structural problem for the thesis.

6. **Single sub-buy-box data point.** The Helen Guo target is $725K EBITDA — below the $2M+ floor where G&B underwrites. A SINGLE sub-buy-box target does not validate that the SEGMENT supports the buy-box (per investor-update guidance and identifier brief). Identifier sees no evidence in either gather agent's scan that credentialed-independent plumbing supports multiple $2-10M EBITDA targets.

7. **Searcher overlap (negative signal).** Plumbing roll-ups are a crowded PE vertical (Wrench Group, Apex Service Partners, Authority Brands, etc.). Federal/tribal credential is a moat against generic-commercial PE, but the broader category attention will pressure pricing and target availability. `feedback_searcher_overlap` applies.

8. **No 2+ source confirmation.** Only one source (Helen Guo newsletter, single listing) surfaced this. Historical gather agent found zero corroborating signal. Fails the implicit "2+ source confirmation" bar applied to all other candidates this week.

**SKIP RATIONALE:** Fails recurring-revenue gate, marginal-to-fail on margins and TAM, fatal credential-transferability deal-structure risk, single sub-buy-box data point, single source. The govt-credential angle is genuinely interesting as a moat lens but does not survive niche-level evaluation. The Helen Guo target is a deal-flow item for Kay's discretion, not a niche worth pursuing.

### Re-scoring / Re-prioritization Recommendations

1. **Row 13 — HNW Personal Lines Concierge:** Re-score from 2.53 → ~2.65-2.70 to reflect Aug Felker 11/19 endorsement ("two-women-retiring HNW personal-lines-only" archetype as platonic version of niche, ~100% retention, 25-35% margins, double-digit annual premium increases climate-driven) plus Hunter 1/12 carve-out workaround for 12-14x whole-brokerage multiple wall. Pass to scorer with explicit citations.

2. **Row 9 — Trade Credit/Customs/Cargo Bundle:** Prioritize within pending-7. Jeremy Black 2/3 email named Trade Risk Group, Trade Acceptance Group, Texel (fka Meridian) — target-discovery has a head start with three named carriers/vendors plus Euler Hermes/Atradius/Coface carrier landscape. Front-of-queue for analyst-call advance-or-table decision.

3. **Row 4 — Specialty Coffee Equipment:** Refresh one-pager with Jeff Stevens 4/22 diagnostic ("do mid-sized chains — Joe Coffee / Blue Bottle scale, not Starbucks — in-house or outsource servicing?") plus NYC market depth question. This open diagnostic gates pipeline expansion; answer before next analyst call. Carlos Nieto 5/13 independently surfacing the niche is a clean convergence signal worth documenting.

### Pool Handoff for Step 3 (One-Pager) and Step 4 (Scoring)

- **New niches needing one-pager:** None — no new niches this week.
- **Existing niches needing re-scored xlsx + updated one-pager:** Row 13 (HNW Personal Lines Concierge) — re-score with Aug Felker + Hunter citations; expected score lift ~2.53 → 2.65-2.70.
- **Existing one-pagers needing refresh only (no re-score):** Row 4 (Specialty Coffee Equipment) — fold in Jeff Stevens 4/22 diagnostic + NYC market depth question + Carlos Nieto 5/13 convergence signal.
- **Existing niches needing prioritization flag only (no artifact change):** Row 9 (Trade Credit/Customs/Cargo) — flag to analyst-call agenda as front-of-pending-7 due to Jeremy Black's named-carrier head start.

### zero_finding_reason candidate string (for JSON sidecar):

"7 pending candidates from prior week sit unprocessed in New - Pending Review; convergent signal across both gather agents is depth not breadth — five insurance-brokerage rows (Specialty Art & Collectibles, Trade Credit/Customs, Aviation, HNW Personal Lines, Surplus Lines) cluster inside one Q1-Q2 2026 PE-consolidation wave demanding advance-or-table analyst-call decisions. No net-new niche cleared the KILLED/TABLED filter with 2+ source confirmation. Single discretionary candidate (Commercial Plumbing federal/tribal credentialed) evaluated and skipped — fails recurring-revenue gate, marginal-to-fail on margins/TAM, fatal credential-transferability deal-structure risk (8(a)/tribal credentials generally do not survive ownership change), single sub-buy-box data point ($725K EBITDA, below $2M+ floor)."

---

---

## [niche-intel-recent] — 2026-05-19 22:40
**Status:** complete — 7 of 7 sources scanned. Granola MCP unavailable (PKCE OAuth headless-incompatible per 2026-05-12 open loop); used `brain/calls/` 14d window as proxy. `last30days.py` script not on VPS; substituted 2× WebSearch.

### Source Coverage
- Newsletters (`auto/subscriptions & education` last 7d + `auto/industry research` last 14d): 65 scanned, ~12 relevant
- Gmail deal flow (`auto/deal flow` last 14d + `auto/investors` last 14d): 69 scanned, ~22 relevant (broker teasers + outbound replies)
- Granola/vault calls (last 14d): 8 scanned (5 niche-relevant: Carlos Nieto/DCA, Krupa Shah/STREAM, Jackson Niketas/Terra Mar, Harrison Wells, AI Friday 5/8 + 5/15)
- Vault outputs (last 14d): 6 scanned (`2026-05-15-pest-20-women-owned-west-village`, `2026-05-15-calibration-weekly`, boundary `2026-05-08-discussion-pest-control-holdco-architecture`; rest ops/infra)
- Passive signals (`brain/inbox` since 5/13): 4 files (1 budget trigger, 2 DealsX leads, 1 Matt XPX follow-up draft — no niche signals)
- Web/social: WebSearch available, 2 queries run (insurance brokerage 2026 M&A; B2B services roll-up 2026)

### Signals Found

**S1. Specialty/P&C insurance brokerage consolidation accelerating (multi-source, convergent on active niches).**
- Source: Axios Pro Rata 5/14 + 5/19; Alvarez & Marsal "Insurance Brokerage M&A: 2026 Market Outlook"; Marsh Berry "Navigating the Future"; West Monroe "Mid-market brokers continue to drive M&A."
- Synthesis: Q1-Q2 2026 deal volume sustained at 2024 levels; PE-backed buyers dominate; **firms $500K-$10M revenue band = "most pressure to consolidate"** (West Monroe). 2025 anchor deals (Gallagher/AssuredPartners $13.45B, Brown & Brown/Accession $9.825B) closed — capital re-cycling into mid-market platform builds.
- Active-niche convergence: **Specialty Insurance (Art & Collectibles)** + **Aviation Insurance** + **HNW Personal Lines Concierge** + **Trade Credit/Customs/Cargo** + **Surplus Lines Compliance** — five WEEKLY-REVIEW rows all inside the same PE consolidation wave. Adds urgency to advance-or-table decisions on the four insurance-broker rows pending.

**S2. SaaS-software AI-disruption hesitation (third corroborated source).**
- Source: Krupa Shah call 5/14 ("Stopped looking at software ~3 months ago due to AI disruption"); Carlos Nieto call 5/13 ("AI disruption making investors cautious on software acquisitions; last software deals closed ~January").
- Synthesis: Two peer searchers (independent funds, different stages) independently arrived at the same software pause. Validates G&B's Jake+Adam hard gate on SaaS niches. Funeral Home Mgmt Software (row 14) sits inside this risk envelope.
- Active-niche convergence: pressure on **Funeral Home Mgmt Software** and **Vertical SaaS Luxury Services** — confirms why DealsX tightened SaaS to $2-6M ARR.

**S3. PE downstream pressure into traditional search band intensifying.**
- Source: Carlos Nieto 5/13 (verbatim: "Traditional search-fund target band ($2-5M EBITDA) now highly competitive — PE moving downstream"). Confirms investor guidance memorialized 2026-05-19 in `feedback_deal_screen_300k_salary_15pct_margin` (PE moved into $2M+, sub-$2M less competed). PwC industrials/services 2026 outlook + Cherry Bekaert PE outlook converge on "buy-and-build favored at fragmented + recurring-revenue floors."
- Synthesis: Reinforces sub-$2M-EBITDA hunting lane and segment-quality-first doctrine. No niche change — strategy reinforcement.

**S4. Blue-collar pest seeing 30-40% premium bids — Premium Pest reinforcement.**
- Source: Carlos Nieto 5/13 ("Blue-collar verticals (pest mgmt specifically named) seeing 30-40% premium bids from larger players"). This Week In ETA 5/8 references pest at 9-11x multiples as canonical "hot industry" example.
- Active-niche convergence: **Premium Pest Mgmt** thesis — consolidation premium real and ongoing. Reinforces, does not change, strategy.

**S5. Industrials = dominant sector on Axial (27% of platform deals, 40% of closed transactions YTD 2026).**
- Source: Axial 5/19 ("2026 Industrials Top 50"). Featured Winning LOI: contract manufacturing co, $3-4M rev / $1.5-2M EBITDA / TEV $8-10M / 56d pursuit→LOI / 63d LOI→close / 55% cash / 45% earnout.
- Synthesis: Sell-side activity densest in industrials. Doesn't map to G&B luxury-services thesis directly, but convergent with Krupa Shah's stated focus ("digital services, industrials") — relevant for **river-guide / co-invest deal-flow with STREAM** (Krupa explicitly offered real-estate-component deal sharing).

**S6. Family-office buyer client actively shopping NY/NJ/CT services & distribution (E&K, repeated 5/13 + 5/19).**
- Source: Everingham & Kerr buy-side 5/13 + 5/19 — well-capitalized family office, NYC metro (NY / North + Central NJ / CT), "Services and/or Distribution Company."
- Synthesis: Confirms G&B geography is where family-office capital is hunting. Not a new niche — market-temperature reading. Intermediary outreach in this geo is timely.

**S7. Single-asset Continuation Vehicles for services platforms (ambient signal, Holdco architecture reinforcement).**
- Source: PE Hub 5/15 + 5/18 — Baird Capital single-asset CV for life-sciences consulting biz Blue Matter.
- Direct niche relevance: limited. Notable: single-asset CVs (a 2025-2026 pattern) used to hold high-quality services platforms past traditional fund horizons — supports G&B Holdco architecture decision (2026-05-08 Pest Holdco discussion).

**S8. Conference / network channel signals (channel reinforcement, not niche promotion).**
- ACG NY Women of Leadership Summit (5/13 — Kay attended; Krupa Shah + Megan Benson contacts surfaced). NPMA Women's Forum + 2026 Academy pushes (multiple 5/12-5/15 emails). XPX networking (CT + NYC, multiple). PestWorld 2026 registration open 5/11.
- Synthesis: Conferences + woman-network priority lens both firing. Already memorialized; no new niche emerges from conference signal alone.

**S9. "Cold email alone doesn't work" cross-channel signal (operational, not niche).**
- Source: Salesforge / Frank Sondors 5/19 ("AI didn't fix reply rate"); Salesforge 5/14 ("Why I wouldn't run email alone anymore — Gartner: B2B buyers spend 17% of journey with sales reps").
- Synthesis: Reinforces channel doctrine (`feedback_in_person_conferences_highest_roi`, Harrison Wells 5/15 corroboration). No niche change — surface to outreach-manager.

### Industries/Companies Mentioned

**From E&K teasers (broker deal flow 5/6-5/19):**
- IP-Led Children's Sport and Education Platform (UK franchise) — out-of-buy-box (B2C, UK)
- SaaS Inventory Management Co. — already acquired by PE-backed strategic (closed deal, not target)
- Metal Manufacturing / Precision Machining / Stamping & Tool & Die (Mid-Atlantic, $20M rev / $4.2M EBITDA) — industrials, large for G&B
- Luxury Kitchen and Bath Designer (NJ, $1M rev / $350K SDE) — small, B2C
- Multi-Location Health/Wellness/Fitness Products (East South Central, $4M rev / $350K SDE) — pure B2C, excluded
- Family Medical Practice (Southern NJ, $1.5M / $400-500K EBITDA) — healthcare, requires vertical decision
- Full-service Structural Engineering, Inspection & Consulting (NJ, $200K / $100K SDE) — too small
- Cloud-Based SaaS Healthcare / Regulatory Compliance ($700K rev) — KILLED niche
- B2B Trade Magazine Publisher (meetings industry, $2.2M / $1M EBITDA) — interesting but media-publishing, not in thesis

**From Helen Guo SMB Deal Hunter (5/7-5/19 listings):**
- Self-Serve Car Wash w/ RE (MD, $462K); Auto Salvage Yard (FL, $584K); Access Control & Door Hardware (MN, $755K); Industrial Equipment Fabricator + Service (OH, $564K); Landscape Supply Distributor (TX, $649K); Commercial Glass & Glazing (AL, $1.34M); Cabinetry Fab & Installation (AZ, $515K); Residential HVAC w/ 400+ service agreements (LA, $434K); Gas Station w/ triple-net McDonald's (WI, $512K); Semi-absentee Embroidery/Screen Printing (IL, $1.5M); Junk Hauling (OR, $600K); Commercial & Industrial Roofing (S. CA, $1.7M); Home Improvement (MO, $500K); Commercial Interior Plantscape & Maintenance (FL, $464K); Multi-Provider Chiropractic Rehab (TN, $726K); Federal/Tribal Credentialed Commercial Plumbing (AZ, $725K); Mobile In-Home Healthcare Coordination (TX, $441K); Commercial Fence & Custom Gate Fab (CA, $1M); **Fire Protection and MEP Engineering Firm in NY ($718K EBITDA)** — KILLED niche, corroborates but does not change verdict.
- Pattern: most sub-$2M EBITDA, multiple CA (excluded), HVAC + commercial roofing + commercial plumbing recur (active in PE roll-up universe per S1).

**From Carlos Nieto (DCA, 5/13):**
- Colombian AgTech drone co (off-geo, $2M / 60-70% margin) — Kay declined
- Miami restaurant inventory management SaaS — software AI-risk decline
- 1099 health insurance (70% cost-reduction) — out-of-thesis
- **Specialty coffee equipment servicing** — Carlos independently surfaced as niche-intel queue candidate; ALREADY ACTIVE in WEEKLY REVIEW row 4 — convergence signal

**From Krupa Shah (STREAM Capital, 5/14):**
- Sale-leaseback specialty; success-fee / no-pay-till-close. Standing open offer to co-evaluate any deal with real-estate component. Art storage deal (warehouse) "may resurface." 12-investor club model, deal-by-deal funding, $2-5M EBITDA target.

**From Axial 5/19 Top 50 + Winning LOI:**
- Contract manufacturing co ($3-4M / $1.5-2M EBITDA, TEV $8-10M, 55% cash / 45% earnout)
- Concentra Capital Group → Metal & Cable Corp acquired by Schmidt Industrial Services
- Premara → Ayrshare (social media API SaaS) sold to saas.group

### Data Points for Scoring

| Metric | Value | Source |
|---|---|---|
| US Specialty Insurance Brokerage M&A pressure band | $500K-$10M revenue firms = "most pressure to consolidate" | West Monroe 2026 outlook |
| Anchor 2025 brokerage deals (capital re-cycling) | Gallagher/AssuredPartners $13.45B; Brown & Brown/Accession $9.825B | Alvarez & Marsal 2026 |
| Pest control trading multiples (PE-driven) | 9-11x EBITDA | This Week In ETA 5/8 |
| Pest blue-collar premium-bid range | 30-40% above mid-market | Carlos Nieto / DCA 5/13 |
| Industrials share of Axial platform | 27% of deals, 40% of closed transactions YTD 2026 | Axial 5/19 |
| Axial Winning LOI deal mechanics (5/19 contract mfg) | 56d pursuit→LOI, 63d LOI→close, 55% cash / 45% earnout | Axial Winning LOI 5/19 |
| Axial Winning LOI deal mechanics (5/12 managed IT services) | $4-5M / $1.5-2M EBITDA / 503 buyers / 37 pursuits / 72d→LOI / 133d→close / 8x exit | Axial 5/12 |
| PE-backed services M&A driver | Recurring revenue + fragmented + buy-and-build | PwC 2026 Industrials & Services outlook |
| AI Fundraising SaaS (Quiet Light 5/15) | 77% on Non-Cancellable Master Service Agreements | Quiet Light listing |
| Shopify CRO Agency (Quiet Light 5/18) | 99%+ Recurring Revenue, $80.9K MRR, 26% YoY | Quiet Light listing |

### Convergent vs Active Niches

Active/pending niches receiving **new supporting signal** this 14d window:

1. **Specialty Insurance Brokerage (Art & Collectibles)** — S1 (PE consolidation wave, $500K-$10M pressure band)
2. **Aviation Insurance Brokerage** — S1 (same brokerage consolidation thesis)
3. **HNW Personal Lines Concierge** — S1 (same brokerage consolidation thesis)
4. **Trade Credit / Customs Bonds / Cargo Insurance** — S1 (same brokerage consolidation thesis)
5. **Surplus Lines Compliance & Tax Filing Services** — S1 (broker-MGA infrastructure layer; same wave)
6. **Specialty Coffee Equipment Service** — Carlos Nieto independently surfaced as niche-intel queue candidate (convergence)
7. **Premium Pest Management** — S4 (30-40% premium-bid validation; consolidation premium real and ongoing)
8. **Vertical SaaS Luxury Services + Funeral Home Mgmt Software** — S2 (AI-disruption pressure — caution, not promotion)
9. **Estate Management Companies** — no new signal this window
10. **Private Art Advisory + Storage HNV Assets** — no new signal this window
11. **Property Tax Appeal Services** — no new signal this window
12. **OSHA Workplace H&S Training** — no new signal this window

### Potential New Niche Triggers

Surfacing raw signal only — identifier decides. Bias defers; pipeline already has 7 pending candidates.

- **Trade-magazine / B2B publisher (meetings industry)** — E&K listed $2.2M / $1M EBITDA. Single data point; recurring-revenue-light; unlikely to clear `feedback_messy_business_great_segment_filter`. **Probably skip.**
- **HVAC service-agreement consolidation (residential + commercial mix)** — Helen Guo + Carlos's "blue-collar premium" comments + PE Hub momentum convergent. Known PE roll-up vertical, G&B has not previously evaluated. **Worth identifier-stage consideration** but: very crowded, likely fails `feedback_searcher_overlap`.
- **Commercial Roofing (industrial + commercial)** — Helen Guo $1.7M EBITDA Southern CA + ambient PE activity. Geography on this specific deal excluded (CA), broader niche could be evaluated. **Probably defer** — likely fails `feedback_searcher_overlap`.
- **Commercial Plumbing (federal/tribal credentialed)** — Helen Guo AZ $725K EBITDA. Government-credential moat is interesting; niche-level evaluation hasn't been done. **Identifier discretion.**
- **Single-asset Continuation Vehicles for services platforms** — NOT a niche (financing structure); surfaced as Holdco-architecture reinforcement only. No action.
- **STREAM Capital co-invest channel** — NOT a niche; channel/partnership signal. Surface to outreach-manager / relationship-manager, not niche pipeline.

No high-conviction NEW niche surfaces this window. Strongest convergent signal: **insurance-brokerage consolidation wave (S1) reinforcing four already-pending insurance rows** — argues analyst call prioritize advance-or-table decisions on existing rows over adding candidates.

---

## [niche-intel-onepager] — 2026-05-19 02:52
**Status:** complete — row 4 refresh
**Niche:** Specialty Coffee Equipment Service
**Action:** one-pager refreshed with Jeff Stevens 4/22 unanswered diagnostic (added to Macro Trends list) + Carlos Nieto 5/13 peer-searcher convergence line (added to Key Success Factors list). Date stamp updated April 2026 -> May 2026. Sources line appended to Exit cell citing both call files. All 6 template shapes preserved (lines, table, picture, two text boxes). Edits used cloned-paragraph + cloned-run xml pattern so bullet formatting + run properties carry over.
**Drive folder:** 13_ZNe6kY-1EUYWPYzWmiGK6i5Jdxfdts
**Old pptx file id (trashed):** 1VggLA7HHhXxNzOD4I8YPz1V_t5NbZ2_S
**Updated pptx file id:** 1leHHK9dBu0CIu8gkoZN1m_7v9HIDz4sr
**Filename:** "Specialty Coffee Equipment Service May 2026.pptx"
**Score:** unchanged at 2.55 (this is a refresh, not a re-score). Note the existing pptx body text says "Assessment: 2.50 / 3.0 (83%)" — that string was NOT updated because the brief said score stays and the WEEKLY REVIEW current score is 2.55; the in-pptx assessment was the pre-tracker reconciled value. Flag for scorer/tracker if they want the in-doc string aligned.
**Diagnostic to surface in analyst call:** "Do mid-sized regional chains (10-50 locations — Joe Coffee, Blue Bottle scale, not Starbucks) outsource equipment servicing or in-house it? Pipeline expansion beyond pure-play artisan cafes depends on the answer."

---

## [niche-intel-scorer] — 2026-05-19 22:53
**Status:** complete — row 13 re-scored
**Niche:** HNW Personal Lines Concierge Insurance Brokerage
**Prior score:** 2.53
**New score:** 2.65
**Net change:** +0.12 (computed +0.113 rounded for tracker display)
**Drive folder:** 1ZryW7c3b7s6mB7SLF1MEMWdOpW-91lJL
**Old xlsx file id (trashed):** 1NC_KUVXrTy-5g_4PKA3cgDLjbpjHSzUs
**Updated xlsx file id:** 136sFfqfxEpfZaLvuPHYPDNbqCTMXrqJ5
**Old pptx file id (trashed):** 13e_iuEHaV-kcadrFYeAyy11PfCJMo5yY
**Updated pptx file id:** 1xRKrVV8t4RlJCjTwOUBHfPoeDcoIxdip
**Updated xlsx filename:** "HNW Personal Lines Concierge Insurance Brokerage Scorecard May 2026.xlsx"
**Updated pptx filename:** "HNW Personal Lines Concierge Insurance Brokerage May 2026.pptx"

### Category changes

| Category | Prior | New | Δ | Reason |
|---|---|---|---|---|
| Growth, Penetration & Catalyst (25%) | 3.00 | 3.00 | 0 | Already at ceiling — climate-driven double-digit premium increases REINFORCE, no upward room |
| Size & Fragmentation (10%) | 1.50 | 1.50 | 0 | No new evidence on independent count or concentration |
| Industry Economics (10%) | 2.67 | 3.00 | +0.33 | EBITDA margins +/- → + (Aug Felker 11/19/25 cited 25-35% EBITDA at scale; top of band clears 30%+ threshold for specialty HNW at scale) |
| Mission Criticality (15%) | 3.00 | 3.00 | 0 | Already at ceiling — Aug Felker endorsement validates rather than changes (cannot exceed +) |
| Exogenous Risks (10%) | 2.40 | 2.40 | 0 | No new evidence on tech/regulatory/liability/cycle |
| Porter's Five Forces (15%) | 2.00 | 2.20 | +0.20 | Level of competition +/- → + (Hunter Hartwell 1/12/26 carve-out path reduces bidding-war intensity at sub-segment level — fewer specialty bidders for an HNW dept inside a multi-line firm than for a whole specialty brokerage) |
| Value Creation Opportunities (10%) | 2.50 | 3.00 | +0.50 | Business complexity +/- → + (carve-out path isolates a clean personal-lines book — lower integration complexity than whole-brokerage acquisition; professionalization lever stays at +) |
| Impact & Externalities (5%) | 2.50 | 2.50 | 0 | No new evidence |
| **Total (weighted)** | **2.532** | **2.645** | **+0.113** | |

### New evidence cited (in xlsx J-column + pptx Industry Thesis cell)
- **Aug Felker 11/19/25** — "two-women-retiring HNW personal-lines-only" target archetype, explicitly endorsed "really valuable," ~100% retention, 25-35% EBITDA at scale, double-digit annual climate-driven premium increases. Cleanest platonic fit in entire G&B research history.
- **Hunter Hartwell 1/12/26** — carve-out path as workaround for 12-14x whole-brokerage multiple wall (e.g. acquire an underdeveloped HNW personal-lines book inside a multi-line firm).
- **Camilla 2/4/26** — personal-lines stickiness reinforced (single-source supporting signal).

### Specific cell edits applied
- **xlsx (Industry Scorecard tab):**
  - `E18` (Average industry EBITDA margins): `+/-` → `+`
  - `J18` updated to cite Aug Felker 25-35% at scale
  - `E32` (Porter's Level of competition): `+/-` → `+`
  - `J32` updated to cite Hunter carve-out path
  - `E38` (Value Creation: General complexity): `+/-` → `+`
  - `J38` updated to note carve-out isolates clean book
  - `B44/C44` — added "Re-score notes (2026-05-19)" block documenting delta + evidence
  - All formulas preserved (SWITCH, AVERAGE, SUMPRODUCT chain — C43 still computes from E-column ratings).
- **pptx (slide 0 table):**
  - `cell[1][0]` Assessment: 2.53/3 → **2.65/3** (verdict "Promising" preserved)
  - `cell[1][1]` Status: category breakdown updated (Econ 2.67→3.0, Porter 2.0→2.2, Value 2.5→3.0; others unchanged)
  - `cell[5][0]` Industry Thesis: APPENDED re-score paragraph citing Aug Felker 11/19 + Hunter 1/12 + Camilla 2/4 + delta string
  - All 6 template shapes preserved (2 lines, table, picture, 2 text boxes); used run.text replacement pattern; no rebuild.

### Recommended new WEEKLY REVIEW row 13 cells
- **Score:** 2.65
- **Quick notes:** "HNW personal-lines-only brokerage. PE consolidation wave hits $500K-$10M revenue band (Q1-Q2 2026). Aug Felker 11/19 archetype endorsement (~100% retention, 25-35% EBITDA, climate-driven double-digit premium increases). Hunter 1/12 carve-out path workaround for 12-14x multiple wall. Re-scored 5/19 from 2.53 → 2.65."

### Caveats for tracker
- Score sits at the low end of the identifier's projected 2.65-2.70 lift band. The conservative call reflects that two of the four "new evidence" levers (Growth + Mission Criticality) were ALREADY at the +3.0 ceiling and could not absorb upward pressure — the Aug Felker / Hunter / Camilla evidence reinforces those ratings rather than moving them.
- No upward bump applied to Exogenous Risks despite climate-driven premium increases — climate is a GROWTH tailwind (captured in row 11/12), not a risk-reduction signal; the wildfire/flood claim concentration risk on HNW books remains real and is appropriately captured in the unchanged Exogenous Risks 2.40.
- Size & Fragmentation 1.50 unchanged — new evidence said nothing about the count of acquirable independents (still 20-40 per INITIAL SCREEN target TAM).

---

## [niche-intel-tracker] — 2026-05-19 23:05
**Status:** complete — Industry Research Tracker updated

### Writes Executed
- **WEEKLY REVIEW row 13 (sheet row 16) — HNW Personal Lines Concierge Insurance Brokerage:**
  - Column E (Score): `2.53` → `2.65` (+0.12)
  - Column H (Quick notes): appended `RE-SCORED 5/19 → 2.65 (+0.12) on Aug Felker 11/19 platonic-target evidence + Hunter 1/12 carve-out workaround.`
  - Range written: `WEEKLY REVIEW!E16:H16` (4 cells, --values-json — no positional delimiter risk)
  - Verified by re-read; pre-write values snapshotted in chatroom history.

### No Other Writes
- 0 new rows appended (identifier returned 0 new niche candidates this cycle; convergence pointed to depth-actions on existing rows rather than net-new niches).
- Row 4 (Specialty Coffee Equipment Service) one-pager refresh did NOT require tracker cells to change — score unchanged at 2.55; the Jeff Stevens 4/22 diagnostic now lives inside the one-pager body.

### Files Touched
- xlsx replaced: `1NC_KUVXrTy-5g_4PKA3cgDLjbpjHSzUs` (trashed) → `136sFfqfxEpfZaLvuPHYPDNbqCTMXrqJ5` (new) in folder `1ZryW7c3b7s6mB7SLF1MEMWdOpW-91lJL`
- pptx replaced (HNW Personal Lines): `13e_iuEHaV-kcadrFYeAyy11PfCJMo5yY` (trashed) → `1xRKrVV8t4RlJCjTwOUBHfPoeDcoIxdip` (new) in same folder
- pptx replaced (Specialty Coffee): `1VggLA7HHhXxNzOD4I8YPz1V_t5NbZ2_S` (trashed) → `1leHHK9dBu0CIu8gkoZN1m_7v9HIDz4sr` (new) in folder `13_ZNe6kY-1EUYWPYzWmiGK6i5Jdxfdts`

### Tracker Counts for Sidecar
- `niches_evaluated`: **17** (synthesizer signal matrix count)
- `niches_identified`: **0** (no new niches added to WEEKLY REVIEW)
- `one_pagers_written`: **2** (row 13 update + row 4 refresh — both replace existing pptx)
- `scorecards_written`: **1** (row 13 re-score xlsx)
- `tracker_updated`: **true** (WEEKLY REVIEW row 13 score + notes write verified)

