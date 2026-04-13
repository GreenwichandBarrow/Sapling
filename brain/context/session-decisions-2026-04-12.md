---
schema_version: "1.0.0"
date: 2026-04-12
type: session-decisions
session: full-day (Sunday)
tags:
  - date/2026-04-12
  - session-decisions
  - topic/system-health
  - topic/vertical-saas
  - topic/specialty-healthcare
  - topic/saas-filter
  - topic/weekend-briefing
---

# Session Decisions — April 12, 2026 (Sunday)

## Decisions

### Weekend + Workflow Architecture
- APPROVE: Weekend briefing variant — lighter than weekday. Email-intelligence + relationship-manager + session-decisions carryover + Monday prep. No JJ/outreach/pipeline-shift noise.
- APPROVE: Conference-discovery moves from Monday to Sunday (fits Kay's Sunday planning rhythm).
- APPROVE: Meeting-brief-manager nightly automation RETIRED. Morning briefing (pipeline-manager) now prompts "Brief needed?" per external meeting. Kay opts in → meeting-brief skill runs for that one.
- APPROVE: Friday meeting-brief prompt covers Mon+Tue (not just Sat). Sunday covers Mon (standard one-day-ahead).

### System Health + Calibration Fixes
- APPROVE: scripts/run-skill.sh retry logic (3 attempts, 30s backoff, on transient patterns incl. 401/authentication_error)
- APPROVE: email-intelligence plist deployed (Mon-Fri 7am ET)
- APPROVE: health-monitor skill upgraded — escalates 2+ consecutive fails to RED, audits launchctl vs CLAUDE.md plist coverage
- APPROVE: CLAUDE.md evening workflow step 3 hardened — MUST produce artifact (traces or explicit skip log)
- APPROVE: KEYCHAIN_PASSWORD added to .env.launchd (prevents niche-intelligence Tue 4/14 401)
- APPROVE: Pipeline-manager deferral aging — 5+ days surface with "Kill/Do now/Re-defer" forcing Q, 10+ days RED if no trigger

### Thesis + Niche Architecture
- APPROVE: DealsX Industry bucket model — broad industry on DealsX side, narrow niches on tracker with `DealsX Industry` column linking them.
- APPROVE: New WEEKLY REVIEW column L = "DealsX Industry" (safe append, no mid-sheet insertion).
- APPROVE: New WEEKLY REVIEW column M = "SaaS Filter" (hyperlinked to Reference tab).
- APPROVE: Reference tab on tracker — defines Jake Stoller 7 dimensions + Adam Datacor structure pattern + G&B scorecard-vs-filter distinction.
- APPROVE: SaaS Filter (Jake + Adam) is pass/fail gate BEFORE scorecard for SaaS niches. Non-SaaS niches blank (existing G&B scorecard only). Failing niches do NOT proceed to one-pager/scorecard.
- APPROVE: B2B and B2B2C acceptable for niches; pure B2C rejected (payer test — if payer is a business, passes regardless of end-user).

### Specialty Healthcare PM/EHR Bucket (DealsX Industry #4 formalized)
- APPROVE: 5 narrow tracker niches added as "New" / Under Review:
  - Rank 7: Behavioral Health PM — score 2.48/3.0
  - Rank 8: PT Clinic Software — score 2.44/3.0
  - Rank 9: Home Health Agency Software — score 2.51/3.0 (highest)
  - Rank 10: Fertility / IVF Clinic Software — score 2.25/3.0, FAILED Growth TAM screen (~$200-400M vs $500M floor) — FLAGGED in Red Flags column
  - Rank 11: Senior Living & Home Care Operating Software — score 2.24/3.0
- All 5 pass SaaS Filter (Jake + Adam). All 5 have one-pagers + scorecards in Drive.
- APPROVE: Home Health Agency SW is strongest on Jake framework (7/7), validated by Adam's ECP precedent in same category.
- APPROVE: Adam's right-to-win = adjacent tech expertise (Google) + sector pattern recognition (healthcare tech investing). Broader definition than industry-operator experience. Applies to Kay too.
- NOTED: Kay's right-to-win = luxury operations (Chanel) + women's health nonprofit credibility + finance/PE pattern recognition. Adam is stronger; Kay acknowledged.

### Specialty Healthcare Niche Refinements
- REJECT: Broad OB/GYN PM — Athena/Epic/eClinicalWorks territory, not a search fund niche.
- APPROVE: Fertility / IVF Clinic Software as replacement — specialty workflow moat, strongest right-to-win fit despite TAM gate failure. Kept on tracker "Under Review" for Wednesday analyst decision (not auto-killed per agent recommendation).

### Children Services Software (new DealsX Industry bucket, in progress)
- APPROVE: Lead niche — Childcare Center / Daycare Management Software (state licensing compliance, female-dominated workforce, B2B2C)
- REJECT: IEP / Special Education Management Software (Kay gut, despite strong filter fit)
- REJECT: Youth Sports / After-school Program Software (B2C)
- DEFER: Early Intervention Services Software (birth-to-3) — keep as candidate
- DEFER: Pediatric Behavioral Health / ABA PM — technically B2B2C but Kay's gut says B2C; awaiting her decision

### Learning / Thesis Insights (from BK Growth call transcript pull)
- NOTED: Adam's ECP trajectory per his own transcript quote: 4 years 30-45% ARR growth, 5th year 70% CARR growth, rule of 40 throughout/rule of 70-80 terminal, mid-teens EBITDA margin, low 90s gross retention, ~15x ARR exit multiple to Level Equity. No dollar figures disclosed.
- NOTED: Claude fabricated earlier $3M→$40M EBITDA trajectory (not in transcript). Corrected on record.
- NOTED: QSBS applies to vertical SaaS search fund exits. Post-OBBBA: $15M baseline or 10x basis, 100% federal exclusion after 5-year hold. Stacking via trusts can multiply exclusion meaningfully.
- NOTED: Growth round playbook — secondary + primary in same transaction. Searcher sells existing shares (liquidity) and reinvests portion as primary (conviction signal + new QSBS clock). Common veteran move.

## Actions Taken

### System Health
- CREATED: scripts/run-skill.sh v2 with retry loop + preflight auth check + optional keychain unlock
- CREATED: ~/Library/LaunchAgents/com.greenwich-barrow.email-intelligence.plist + loaded
- RETIRED: ~/Library/LaunchAgents/com.greenwich-barrow.meeting-brief-manager.plist → renamed .retired-2026-04-12
- UPDATED: .claude/skills/health-monitor/SKILL.md — consecutive-fail escalation + plist coverage audit
- UPDATED: .claude/skills/pipeline-manager/SKILL.md — Brief needed? section + deferral aging rules + briefing output format
- UPDATED: CLAUDE.md evening workflow step 3 enforcement clause
- CONFIGURED: $KEYCHAIN_PASSWORD in scripts/.env.launchd (verified unlock works)
- AUTHENTICATED: Granola MCP re-auth complete

### Deliverables Created (Specialty Healthcare PM/EHR batch)
- CREATED: 5 one-pager .pptx files in brain/library/internal/one-pagers/ — all uploaded to Drive under WEEKLY REVIEW parent
  - Behavioral Health Practice Management April 2026.pptx → folder 1rQIugA3Uhnyj6obcBF1HBBySeydcmoOY
  - PT Clinic Software April 2026.pptx → folder 11yzd1Pd4Oh01P3thGiRxesqOsOprI4oQ
  - Home Health Agency Software April 2026.pptx → folder 1W-8_0tl0ezeK7bo-4Z-tCnY9csMoUyl5
  - Fertility IVF Clinic Software April 2026.pptx → folder 1BZhPO6RU06l51AQNRnooZGYqDIS-DYJz
  - Senior Living and Home Care Operating Software April 2026.pptx → folder 1g2Ow1Gx8zri3u6ahNPPszbRoXHFzlkhZ
- CREATED: 5 scorecard .xlsx files uploaded to same Drive folders; Assessment cells updated in all 5 one-pagers
- CREATED: Reference tab on Industry Research Tracker (sheetId 1686348582)

### Tracker Updates
- CREATED: Col L "DealsX Industry" on WEEKLY REVIEW — populated for all 5 new niches with "Specialty Healthcare PM/EHR"
- CREATED: Col M "SaaS Filter" (hyperlinked to Reference tab) — all 5 new niches marked Pass
- CREATED: 5 new rows (ranks 7-11) on WEEKLY REVIEW with full data

### Decision Traces
- CREATED: brain/traces/2026-04-10-vertical-saas-thesis-conviction.md (backfilled)
- CREATED: brain/traces/2026-04-11-specialty-healthcare-niche-selection.md (backfilled)
- CREATED: brain/traces/2026-04-12-saas-filter-vs-scorecard.md (this session)
- CREATED: brain/traces/2026-04-12-dealsx-industry-bucket-model.md (this session)
- CREATED: brain/traces/2026-04-12-adam-right-to-win-reframe.md (this session)

### Memory Updates
- CREATED: feedback_repeated_fails_surface.md
- CREATED: feedback_no_opposite_questions.md
- CREATED: feedback_meeting_brief_on_demand.md
- CREATED: feedback_b2b_b2b2c_ok_no_b2c.md
- CREATED: feedback_jake_adam_filter_hard_gate.md
- Updated: MEMORY.md index

### Gmail / Superhuman
- DONE by Kay: Emptied Gmail Trash + Spam directly (confirmed Superhuman deletes were landing in Trash correctly; root cause of "reappearing" mail was split-inbox visibility issue)

## Deferred

- DEFER: Yahoo archive cleanup — retry setup B (Yahoo → right Gmail) after Gmail throttle clears (~3-7 days from Apr 9 error). Then bulk-delete 16K from wrong Gmail. Kay overwhelmed by the lift — parked for later.
- DEFER: EH&S sub-niches — only Apparel Manufacturing Compliance mentioned. Remaining discussion + one-pagers/scorecards queued for next working session.
- DEFER: Children Services Software bucket full rollout — Childcare Center Management is lead niche; need to one-pager/scorecard/track it. Early Intervention + Pediatric BH/ABA still need Kay decisions before proceeding.
- DEFER: Pediatric BH/ABA decision — keep (B2B2C by payer test) or drop (Kay's gut says B2C feel).
- DEFER: Conference pipeline / conference-discovery skill run (Kay's queue after niche batches done).
- DEFER: Additional DealsX Industry buckets beyond Specialty Healthcare, EH&S, Children Services.
- DEFER: PT Clinic one-pager research depth re-review (flagged as thinnest of the 5).
- DEFER: Move conference-discovery plist from Monday to Sunday schedule (decision made, execution queued).
- DEFER: Backfill SaaS Filter column for existing non-SaaS niches (leave blank).
- Carrying forward all prior deferrals: Mark Gardella reply, Philip Hoffman warm intro, Andrew Freiman email (Monday send), broker platform registrations, Otter.ai download, DMARC reject, etc.

## Open Loops

- Wednesday analyst call: 5 Specialty Healthcare niches need Kay decisions (Active-Outreach / Under Review / Table). Fertility IVF specifically needs the TAM-fail decision (push anyway vs table).
- Childcare Center Management: needs full one-pager + scorecard + tracker entry + Under Review status.
- Anthony's monthly P&L: budget-manager armed, waiting for "Management Report" email trigger.
- Yahoo archive: resolution parked, will resurface on aging-deferrals list in briefings.
- EH&S bucket: only Apparel Manufacturing identified as a narrow niche; 3-4 more needed.
- Goal by April EOM reminder: 1 deal to review with Guillermo & Jeff; Process sourcing fully operational.
