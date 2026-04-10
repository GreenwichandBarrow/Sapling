---
schema_version: 1.1.0
date: 2026-04-09
type: context
title: "Session Decisions — April 9, 2026"
sessions: 2
last_updated: 2026-04-09T23:59:00Z
tags: ["date/2026-04-09", "context", "topic/session-decisions"]
---

# Session Decisions — April 9, 2026 (Thursday)

## Decisions

### Pipeline & Niches
- APPROVE: Fractional CFO → Tabled. Investor feedback from [[entities/guillermo-lavergne]]: too much AI disruption risk, team-dependent, no searcher fit.
- APPROVE: Art Storage previously tabled (confirmed, no change)
- APPROVE: Art Advisory list scrub executed — 81 firms → 64 (17 removed with <5 employees, moved to Passed tab)
- APPROVE: Pest Management Compliance Software added to WEEKLY REVIEW as Rank 5, Status: New (score 2.57). Vertical SaaS for pest control compliance, synergy with Premium Pest Management.
- APPROVE: Vertical Software for Luxury & High-Value Asset Service Industries as 3rd DealsX niche (replacing Fractional CFO). Umbrella niche covering jewelry, marina, art gallery, private club, equestrian, auction house, event rental, wine/spirits, estate management, fine art logistics, classic car restoration software.
- APPROVE: No firearms software — not a personal fit for Kay
- APPROVE: No aviation software — heard from another investor it's extremely competitive
- APPROVE: DealsX onboarding sheet finalized with 3 niches: (1) Specialty Insurance Brokerage - Fine Art & Specie, (2) Luxury Property & Estate Management Services, (3) Vertical Software for Luxury & High-Value Asset Service Industries
- APPROVE: Estate Management framing must be B2B (serving family offices, trust companies, wealth management firms), not B2C (serving individual wealthy homeowners)

### Overdue Contacts
- APPROVE: [[entities/alexandre-carel]] → Dormant in Attio. Won't circle back.
- APPROVE: [[entities/kristina-marcigliano]] & [[entities/michael-topol]] — conditional, circle back if insurance opportunity arises
- APPROVE: [[entities/carlos-nieto]] — reach out by May 7
- APPROVE: [[entities/kanayo]] — no action until after May 7

### System Fixes
- APPROVE: CLAUDE.md Source of Truth updated — Google Sheets tracker is authority for niche statuses, Google Drive is authority for living documents (call preps, briefs). Never reconstruct from session decisions or vault snapshots.
- APPROVE: pipeline-manager SKILL.md updated — must always read tracker sheet directly for niche statuses, not depend on artifacts or session decisions
- APPROVE: meeting-brief SKILL.md updated — read-side rule added: check Drive modifiedTime before reading vault copy
- APPROVE: CLAUDE.md jj-operations schedule corrected — prep is Sunday 11pm only, harvest has no launchd job
- APPROVE: SMERGERS and DealStream removed from intermediary-manager SKILL.md (tested Apr 8, not viable)

### Investor Call ([[entities/guillermo-lavergne]])
- APPROVE: [[entities/guillermo-lavergne]] call notes consolidated for Granola entry (cell phone call, not recorded)
- APPROVE: [[entities/guillermo-lavergne]]'s challenge — set an end-of-April goal and hit it
- APPROVE: Kay's potential April goals: 20 owner conversations, 1 interesting deal to show [[entities/guillermo-lavergne]]
- APPROVE: [[entities/guillermo-lavergne]] feedback: searchers moving away from software, criteria changed dramatically, Ashford increased investibility threshold
- APPROVE: Premium Pest Management one-pager updated with premium differentiation (commercial/hospitality thesis, HACCP, IPM, white-glove, why nationals don't compete)

### Other
- APPROVE: Gusto payroll issue resolved (item 17)
- APPROVE: Superhuman G&B token belongs in System Status, not standalone carried item
- APPROVE: New Gmail account created for Yahoo archive migration, forwarding updated, Superhuman connected
- APPROVE: [[entities/guillermo-lavergne]] call prep was already updated by Kay (not Claude) — system should check Drive for living docs, not present stale vault copies

## Actions Taken

### Tracker & Pipeline
- UPDATED: Fractional CFO moved from WEEKLY REVIEW to TABLED tab (reason: investor feedback — too much AI disruption risk, team-dependent, no searcher fit)
- UPDATED: Art Advisory target list scrubbed — 17 firms under 5 employees moved to Passed tab (81 → 64)
- CREATED: Pest Management Compliance Software added to WEEKLY REVIEW as Rank 5, New
- UPDATED: Specialty Insurance Brokerage renamed to "Specialty Insurance Brokerage - Fine Art & Specie" on DealsX sheet
- UPDATED: WEEKLY REVIEW renumbered (Insurance Brokerage rank 4, Pest Mgmt Compliance Software rank 5)

### DealsX Onboarding
- UPDATED: DealsX Industry Verticals sheet — Fractional CFO row replaced with Estate Management (B2B framing for family offices)
- CREATED: Vertical Software niche row added to DealsX sheet with full description, sub-verticals, keywords
- UPDATED: Insurance niche title corrected on DealsX sheet

### Attio
- UPDATED: [[entities/alexandre-carel]] nurture_cadence set to Dormant

### Skills & System
- UPDATED: CLAUDE.md — Source of Truth section expanded (Google Sheets for niche statuses, Google Drive for living documents)
- UPDATED: pipeline-manager SKILL.md — niche detection must read tracker sheet directly, briefing format lists each niche
- UPDATED: meeting-brief SKILL.md — read-side rule for Drive vs vault
- UPDATED: CLAUDE.md — jj-operations schedule corrected (Sunday 11pm prep only, no daily harvest launchd)
- UPDATED: intermediary-manager SKILL.md — SMERGERS and DealStream removed
- COMMITTED: All changes to git (2 commits)

### Deliverables
- CREATED: email-scan-results-2026-04-09.md
- CREATED: relationship-status-2026-04-09.md
- CREATED: Premium Pest Management 4.9.26.pptx (updated one-pager with premium differentiation)
- CREATED: Pest Management Compliance Software April 2026.pptx (one-pager)
- CREATED: Pest Management Compliance Software Scorecard April 2026.xlsx
- CREATED: 2026-04-09-niche-intelligence-report.md (Vertical Compliance SaaS run)

### Niche Intelligence
- RAN: Vertical Compliance SaaS thesis — 6 focus areas, 5 failed, 1 finalist (Pest Mgmt Compliance Software)
- RAN: Luxury vertical SaaS pattern search — 7 new sub-verticals identified (FBO, equestrian, auction house, private club, classic car, event rental, plus firearms rejected)

## Deferred

- DEFER: Estate Management one-pager defensibility update ([[entities/guillermo-lavergne]]'s challenge about law firms/accountants absorbing)
- DEFER: Yahoo archive import to new Gmail — Gmail throttling new account, try again tonight
- DEFER: Full niche-intelligence pipeline (one-pager + scorecard) for umbrella Vertical Software niche on tracker
- DEFER: Philip Hoffman warm intro path — still undecided
- DEFER: BK Growth Mid-Search Summit RSVP — May 18-19 Boston (Kay confirmed attendance via email)
- DEFER: ACG DealSource transfer to WOL Summit — no response from Casey Coleman
- DEFER: [[entities/sam-singh]]'s references (John Baker, Christine Koval) — not contacted, Kay moving forward with DealsX regardless
- DEFER: 4 platform registrations: Keystone, DealForce, FE International, DealFlow Agent
- DEFER: Superhuman G&B token still expired
- DEFER: DMARC tighten to reject ~Apr 20
- DEFER: Deal-eval remaining template items
- DEFER: Download Otter.ai for cell phone call recording
- DEFER: Andy Lock / DealsX contract review — Kay nudged today, Amanda looped in, pending

## Open Loops

- DealsX onboarding call tomorrow (4/10) at 10:30am with [[entities/sam-singh]] — sheet ready, contract pending
- [[entities/ashley-emerole]] coffee tomorrow 9:30am — no prep needed
- Umbrella vertical SaaS niche needs one-pager and scorecard before analyst call
- [[entities/guillermo-lavergne]] challenged estate management defensibility — one-pager needs update
- Yahoo archive migration pending Gmail throttle resolution
- Pest Management Compliance Software on tracker as New — needs Kay's decision at next analyst call
- StartVirtual QA form for JJ still pending

---

# Session 2 — April 9, 2026 (Thursday Evening)

## Decisions

### System & Skills
- APPROVE: Session handoff system built — "save state" / "picking back up" protocol with hooks
- APPROVE: Calendar check hook added to session start (verify dates, never guess)
- APPROVE: Deal eval skill tabled — focus all energy on sourcing engine
- APPROVE: Intermediary-manager renamed → deal-aggregator (prepped deals, not leads)
- APPROVE: Deal aggregator rewritten — primary deal source, no volume cap, 1-3 deals/day target, email inbound as Channel 2, DealsX excluded (separate dashboard)

### Pipeline & Niches
- APPROVE: April goals formalized — (1) 1 deal ready for Jeff & Guillermo, (2) sourcing engine fully loaded
- APPROVE: Vertical Software for Luxury & High-Value Asset Service Industries added to WEEKLY REVIEW as rank 6, Active-Outreach, DealsX Email
- APPROVE: 3 DealsX niches confirmed for onboarding call — Insurance, Estate Management, Vertical Software. Also mention Art Advisory + Art Storage as side explorations.
- APPROVE: Timothy Wong / MMPC outreach email sent (pest management follow-up to JJ's call)
- APPROVE: BK Growth / Pacific Lake hotel booked for May 18-19 Boston

### Niche Conviction (explored, not decided)
- NOTED: Premium pest management thesis challenged — fine dining restaurant uses Western Pest (Rollins subsidiary). Same pattern as commercial cleaning — luxury clients don't pay for premium pest.
- NOTED: Insurance doubts — Hunter Hartwell had deals but couldn't get investors to table at insurance multiples. [[entities/mike-horowitz]] advised avoid areas "done already" by search.
- NOTED: [[entities/guillermo-lavergne]] — investors being more conservative (macro), software bar raised. Andrew S. stressed by software multiples on current exit.
- NOTED: Luxury travel explored as niche — failed criticality test (discretionary). Concierge/membership clubs interesting but thin deal flow.
- NOTED: Luxury brand vendor angle explored — all killed by Kay (overseas, project-based, huge 3PLs, tiny businesses). Fashion industry in structural decline (Saks/Neiman bankruptcy).
- NOTED: Kay inspired by [[entities/amanda-neilson]] (Andrew Freiman's wife) — acquired Peace Care Experts through personal conviction + search fund criteria alignment. Kay wants that level of thesis clarity.
- NOTED: Kay requested thesis discovery questions — cross personal conviction with buy box filters. Prepare for next session.

### Investor Intel
- NOTED: Compounding Labs article — [[entities/andrew-freiman]] & [[entities/will-thorndike]]'s firm. Own capital only, decadal holds, serial acquisition holding companies. Anti-PE positioning.
- NOTED: Will Thorndike is in Kay's cap table 3 times.
- NOTED: VDC / Nashton Company (mosquito/pest control search fund exit) — same investor circle as Kay's investors. Pest management thesis validated by community, though 2011 vintage.

## Actions Taken

### Skills & System
- CREATED: Session handoff hooks — handoff.py (save state / picking back up detection), calendar_check in session.py
- UPDATED: settings wired — session_start.py and user_prompt_submit.py updated with new handlers
- RENAMED: intermediary-manager → deal-aggregator (skill dir, SKILL.md, CLAUDE.md, 6 skill files, skill-rules.json, start command, launchd plist)
- UPDATED: deal-aggregator SKILL.md fully rewritten — removed 20% channel framing, 25% cap, added email inbound channel, 1-3 deals/day target, volume tracking
- UPDATED: WEEKLY REVIEW tracker — Vertical Software added rank 6
- SENT: Timothy Wong / MMPC outreach email via Superhuman

### Deal Aggregator Test Run
- RAN: Full deal-aggregator test — BusinessExits (21 listings), Rejigg (10 listings), 4 niche platforms. Result: 0 thesis matches. General platforms don't surface luxury/premium deals. Niche platforms mostly login-gated.
- RESEARCHED: Broker platform email alert capabilities — 5 free registrations identified
- RESEARCHED: SMB Deal Hunter aggregator — scrapes BizBuySell/BizQuest, not proprietary flow
- RESEARCHED: IBBA, M&A Source, AM&AA broker associations for member deal lists

### Research
- RAN: Luxury travel niche screen — failed criticality test
- RAN: Search fund closed deal database — 70+ specific acquisitions across Pacific Lake, Broadtree, Kingsway, Chenmark, SFA, Acquiring Minds
- RAN: Kay's resume cross-reference against closed deals and transferable skills
- RESEARCHED: PeaceCare Experts (Amanda Neilson's acquisition) and Compounding Labs (Freiman/Thorndike)

## Deferred

- DEFER: 5 broker platform registrations — DealFlow Agent, DealForce, BizBuySell, BusinessBroker.net, BizQuest
- DEFER: Thesis discovery questions — prepare for next session (conviction + buy box intersection)
- DEFER: River guide builder — discussed, not started
- DEFER: Yahoo archive import — still throttled
- DEFER: Estate Management one-pager defensibility update
- DEFER: Umbrella Vertical Software one-pager + scorecard
- DEFER: M&A Source DEALMATCH membership evaluation
- DEFER: Axial buyer mandate platform evaluation
- DEFER: Superhuman G&B token still expired
- DEFER: DMARC tighten to reject ~Apr 20
- DEFER: Deal-eval remaining template items
- DEFER: Download Otter.ai for cell phone call recording
- DEFER: Andy Lock / DealsX contract review — pending
- DEFER: 4 platform registrations: Keystone, DealForce, FE International, DealFlow Agent
- DEFER: Philip Hoffman warm intro path — undecided
- DEFER: ACG DealSource transfer to WOL Summit — no response
- DEFER: [[entities/sam-singh]]'s references — not contacted
- DEFER: StartVirtual QA form for JJ

## Open Loops

- DealsX onboarding call Fri 4/10 10:30am with [[entities/sam-singh]]
- [[entities/ashley-emerole]] coffee Fri 4/10 9:30am
- Team TB Camilla/Kay Fri 4/10 12pm
- BK Growth 1st Thursday Zoom Fri 4/10 1pm
- Premium pest management thesis — Western Pest data point challenges premium angle
- Insurance thesis — Hunter Hartwell couldn't close with investors
- Kay's core conviction thesis — discovery questions to prepare
- Pest Management Compliance Software on tracker as New
- Kay's end-of-April goals need to be shared with investors
