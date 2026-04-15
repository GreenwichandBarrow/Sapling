---
date: 2026-04-15
type: context
title: "Session Decisions — 2026-04-15 (major build day)"
tags: ["date/2026-04-15", "context", "topic/session-decisions", "session/full-day"]
---

## Decisions

### C-Suite agent architecture
- APPROVE: 6-agent structure — CFO, CIO, CMO, CPO, GC as slash commands; COO is the default conversation (no slash)
- APPROVE: Tiebreaker philosophy — Month 1 escalate both rationales to Kay, flip to COO synthesis after 4 weeks of calibration
- APPROVE: Stateless memory — agents re-read MEMORY.md + brain/ every invocation, no persistent per-agent memory
- APPROVE: CIO stays named Chief Investment Officer (not Head of Investments)
- APPROVE: Frame-learning flag — agents emit `frame_learning: true` when hitting knowledge gaps, auto-captured to traces
- APPROVE: Scaffold all 6 agent files + 5 slash commands today; skill refactors deferred to Week 1 (Apr 20+)
- DEFER: CTO/CISO role — revisit Week 4 (week of May 11)
- REJECT: CPO internal-only — flipped to exposed `/cpo` after Kay pushed back

### DealsX + Sam Singh
- DecisionS from 1pm call: verticals confirmed (Enterprise SaaS, Specialty Healthcare SaaS, Vertical SaaS Luxury, Female-Led SaaS); launch date 5/6/2026; Kay reviews copy week 1, spot-checks list week 2, launches week 3
- APPROVE: Revised SaaS revenue band 2-6M ARR (was 3-10M) — "happy to go down the fairway"
- APPROVE: Slack workspace communication with DealsX team (Sam adding Kay + team)
- DEFERRED: Payoneer payment retry pending Kay's bank AWS outage resolution

### Industry Research Tracker
- APPROVE: New DEALSX tab on tracker mirroring Sam's 6 buckets (Kay reformatted to match WEEKLY REVIEW structure)
- APPROVE: Col L (DealsX Industry) mapping for Ranks 3-11, 13 to Sam's 6 buckets
- APPROVE: Status → Active-Outreach + Start Date → 5/6/2026 for Ranks 6-11, 13 (all DealsX-routed)
- APPROVE: Childcare (Rank 11) re-tagged from "Specialty Healthcare PM/EHR" to "Female-Led Vertical SaaS B2B"
- APPROVE: Art Advisory (Rank 2) → Active-Long Term (Kay executed herself) — "not worth focus right now"
- REJECT: Removing WEEKLY REVIEW rows for DealsX-owned niches — Col D already serves as the owner filter
- PASS: Adding Sam's ~45 sub-niches as new WEEKLY REVIEW rows — wait for Sam's list-build to surface real companies, back into niches empirically

### Conference pipeline (major unlock)
- APPROVE: Strategy pivot from big industry conferences → grass-roots intermediary networking (broker breakfasts, ACG, XPX, AM&AA, accounting/law firm breakfasts, coffee chats with deal-makers)
- APPROVE: Geography = PA, CT, LI, NYC, NJ only (excluding Boston, DC, Midwest, CA)
- APPROVE: Schedule = Mon anytime incl. evenings, Tues/Wed ≤2pm, Thu ≤5pm, Fri ≤3pm (Fri added back with afternoon end)
- APPROVE: 1 event/week minimum, more if discovery yields
- APPROVE: conference-discovery and river-guide-builder share one event pipeline
- APPROVE: Conference Pipeline sheet (existing) holds all events; no new sheet

### Pipeline-manager gap
- REJECT (surfaced bug): Pipeline-manager failed to create Attio Active Deals list entry for Timothy Wong (MMPC) after Kay's 4/9 cold email. Attio auto-creates People but not list entries.
- APPROVE: Manual fix — MMPC added to Active Deals at Contacted stage
- APPROVE: Skill fix — outbound email scan extended to 14d window + auto-creates missing list entries with `source: manual-outbound-email`
- APPROVE: New stop hook #11 — post-scan coverage validation for outbound emails to external recipients

## Actions Taken

### Agent scaffolding
- CREATED: 6 agent files — `.claude/agents/{cfo, cio, cmo, cpo, coo, gc}.md` with full system prompts, hard rules, memory slices, output contracts
- CREATED: 5 slash commands — `.claude/commands/{cfo, cio, cmo, cpo, gc}.md` with `disable-model-invocation: true` and frame-learning trace capture
- CREATED: `/Users/kaycschneider/.claude/plans/logical-mapping-finch.md` — full implementation plan, approved

### Tracker updates
- CREATED: DEALSX tab on Industry Research Tracker (Kay then reformatted to match WEEKLY REVIEW structure)
- UPDATED: Col L (DealsX Industry) for Ranks 3-11, 13 to Sam's bucket names
- UPDATED: Col C (Status) → Active-Outreach for Ranks 6-11, 13
- UPDATED: Col J (Start Date) → 5/6/2026 for Ranks 6-11, 13
- UPDATED: Childcare Col L from Specialty Healthcare PM/EHR → Female-Led Vertical SaaS B2B

### Attio
- UPDATED: Ashley Emerole (Saunders Street) — Monthly → Quarterly cadence, next_action "Met 2026-04-15; next touch Q3 (Jul 2026)"
- CREATED: MMPC added to Active Deals at Contacted stage (entry c56a6320-6f14-409a-914e-3a63e638f566)

### Vault
- CREATED: `brain/calls/2026-04-15-sam-singh-dealsx.md` (DealsX onboarding call note)
- CREATED: `brain/context/c-suite-architecture-proposal-2026-04-16.md` referenced (existing, pulled as source of truth)
- CREATED: `brain/context/pober-acquisitions-platform-reference-2026-04-15.md` + 12 screenshots in `brain/reference/pober-acquisitions-screenshots-2026-04-15/`
- CREATED: 5 frame-learning traces in `brain/traces/`:
  - `2026-04-15-saas-revenue-band-revised.md`
  - `2026-04-15-channel-mix-by-route.md`
  - `2026-04-15-kay-focus-off-list-scrubbing.md`
  - `2026-04-15-pipeline-manager-outbound-scan-gap.md`
  - `2026-04-15-conference-unlock-broker-breakfasts.md`

### Skills updated
- UPDATED: `conference-discovery` — event format priority (intermediary networking), scheduling windows, geography constraints, DEALSX tab reference, shared pipeline with river-guide-builder, event criteria filter
- UPDATED: `niche-intelligence` — SKIP logic (Active-Outreach + DealsX Email + one-pager + scorecard = no action); Col D/Col C label correction
- UPDATED: `pipeline-manager` — outbound email scan extended to 14d + auto-create list entry for recipients with Person but no list entry; new Stop Hook #11 (outbound-email coverage reconciliation)

### Memory (MEMORY.md + 8 new feedback entries)
- CREATED: feedback_conference_intermediary_format, feedback_conference_geography, feedback_conference_schedule_windows, feedback_kay_off_list_scrubbing, feedback_saas_revenue_band_2_to_6_arr, feedback_tracker_dealsx_column_alignment, feedback_channel_mix_by_route, feedback_attio_autocreate_person_not_list, feedback_conference_shared_with_river_guide
- UPDATED: MEMORY.md index with 9 new entries

### Conference Pipeline (from background research subagent)
- POPULATED: Conference Pipeline sheet rows A43:Q56 with 14 verified events Apr 22 – Jun 30 (5 in next 14 days, 5 May-June, 4 flagged for verification). XPX-heavy given highest-fit scoring.

## Deferred

- C-suite skill refactors (target-discovery → /cio, deal-evaluation → /cfo & /gc, outreach-manager → /cmo) — scheduled Week 1 starting Apr 20
- MEMORY.md role-tagging (add `role/cfo`, `role/cio`, etc. frontmatter to per-agent memory slices) — Week 1
- CLAUDE.md "C-Suite Agents" section addition — Week 3 (May 4-10)
- Calibration-workflow role-scoped trace scanning — Week 3
- CPO internal-only activation decision — already flipped to exposed, skill refactor for /cpo Week 3
- Command Center dashboard (pin #2) — separate session; design locked in pober reference doc
- Intent-to-sell score + pre-draft replies (pin #3) — separate session
- Inbox-clearing lens — carried to tomorrow-pins-2026-04-16
- Payoneer payment retry — blocked on Kay's bank AWS outage
- Slack-inbound scan integration (Timothy Wong replied on Slack, invisible to Gmail scans) — future pin, not in Week 1 scope
- River-guide-builder update to reflect shared pipeline with conference-discovery — defer to when it's next touched

## Open Loops

- DealsX Week 1 (Apr 15-22): copy draft arrives from Sam for Kay review
- Timothy Wong (MMPC) Slack conversation — Kay to progress, status advance beyond Contacted as warranted
- Conference Pipeline: Kay reviews 14 new events, decides which 2-3 to register for next 14 days
- Ashley Emerole — Quarterly cadence set; next touch Q3 (Jul 2026), no action until then
- C-suite architecture Week 1 kickoff (Apr 20) — CIO + CFO skill refactor
- Friends' skepticism on vertical SaaS buying (4/14 carryover) — Kay's conviction state unclear
- Budget-Dashboard + bookkeeper monthly P&L — not Kay's job, await bookkeeper cadence (no nudging per feedback_no_anthony_nudges)

## Litmus Check — Decision Traces

Scanned for APPROVE/REJECT items with non-obvious reasoning that would change future agent behavior.

**Trace-worthy (already written today):**
1. `2026-04-15-saas-revenue-band-revised.md` — 2-6M ARR (was 3-10M)
2. `2026-04-15-channel-mix-by-route.md` — DealsX/Kay/JJ channel rules, phone-ack gating
3. `2026-04-15-kay-focus-off-list-scrubbing.md` — Kay's time-allocation decision
4. `2026-04-15-pipeline-manager-outbound-scan-gap.md` — auto-create list entry gap
5. `2026-04-15-conference-unlock-broker-breakfasts.md` — intermediary networking pivot

**Reviewed but not traced** (routine / not non-obvious):
- CIO name (standard choice, not a judgment call between alternatives that changes behavior)
- CPO slash exposure (reasonable symmetry fix, not a deep frame change)
- Sam's 6 buckets mapping (data reconciliation, not a judgment call)
- Tracker reformat (Kay's formatting preference, captured in memory)

All 5 frame-learning traces tagged for role-based loading (cfo, cio, cmo, cpo, gc, coo).

## Pins for Tomorrow

Carried forward to tomorrow-pins-2026-04-16:
1. Review 14 conference events on Conference Pipeline sheet — register for 2-3 near-term
2. DealsX Week 1 copy review when it arrives
3. Tim Young/Wong (MMPC) Slack follow-through
4. Inbox-clearing lens (original 4/16 pin)
5. Command Center dashboard design (pin #2, overkill version filtered per today's Pober reference)
6. Payoneer retry once bank back online
7. C-suite Week 1 prep (CIO + CFO skill refactor starts Apr 20)
