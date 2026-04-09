---
schema_version: 1.1.0
date: 2026-04-09
type: context
title: "Session Decisions — April 9, 2026"
sessions: 1
last_updated: 2026-04-09T22:00:00Z
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
- Kay's end-of-April goals not yet formalized
- Yahoo archive migration pending Gmail throttle resolution
- Pest Management Compliance Software on tracker as New — needs Kay's decision at next analyst call
- StartVirtual QA form for JJ still pending
