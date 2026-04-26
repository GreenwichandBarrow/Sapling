---
schema_version: 1.1.0
date: 2026-04-25
type: context
title: "Session Decisions — 2026-04-25 (Dashboard Session 6 — M&A Analytics)"
tags: [date/2026-04-25, context, topic/dashboard, topic/command-center, topic/ma-analytics, topic/session-6, topic/session-decisions]
---

# Session Decisions — 2026-04-25 (Dashboard Session 6)

Command Center build Session 6 — M&A Analytics page (non-DealsX zones).
Continuation: [[brain/context/continuation-2026-04-25-session6-ma-analytics]].
Page replaces the manual Weekly Activity Tracker Google Sheet.

## Decisions

- **APPROVE: ship Zones 1 + 3 + 4 + 5 live, Zones 2 + 2.5 as Live-May-7 placeholders.** Matches the continuation file's "3 full + 1 partial + 2 deferred placeholders" plan exactly. DealsX integration unlocks Zones 2 / 2.5 / DealsX rows in Zone 3 on May 7.
  - Why: honors `feedback_build_new_before_sunset_old` — page goes live with real data Kay can see today, deferred zones tag clearly so the placeholders aren't mistaken for missing data.
- **APPROVE: derive Zone 1 KPIs from existing Attio snapshot + brain/calls/, no new artifacts.** All 5 deal-flow tiles work off `load_pipeline(scope="full")` for stage advances + `closed_recent` for closures + brain/calls/ filename dates for owner conversations. No new scheduled job, no new MCP fetch.
  - Why: minimal-deps approach. A snapshot-refresh job is appropriate later when all 6 pages ship and we batch the automation story (per Session 3 open loop).
- **APPROVE: Zone 4 trends ship with graceful "pending" state for 3 of 4 panels.** Owner-conversations sparkline derives from brain/calls/ filename dates and renders real bars. NDAs / Reply rate / JJ dials render dimmed with a "Pending data history" delta line — no fake numbers.
  - Why: Mockup defines 4 panels; honest empty-state preserves the visual structure without inventing numbers. Panels backfill when (a) snapshot adds NDAs, (b) DealsX gives reply rate, (c) JJ master sheet gets wired.
- **APPROVE: Zone 3 channel rows for Kay-email + JJ-calls render with `—` not zero.** No reliable Streamlit-side reader exists for either. `—` signals "data not wired yet"; zero would falsely imply "we sent zero emails this week."
  - Why: `feedback_no_unverified_metrics` — never present numbers we can't defend.
- **APPROVE: hardcode 4 active niches in `_ACTIVE_NICHES` (Insurance Brokerage, Fine Art Storage, Equipment Servicing, Managed IT Services).** Industry Research Tracker is a Google Sheet that hasn't been wired into Streamlit yet. Hardcoded list is one source of truth update when a niche flips status; documented via inline comment.
  - Why: ship-and-iterate rather than block on Sheets API setup.
- **APPROVE: filter bar visual-only (Daily/This Week/This Quarter/LTD + 2 dropdowns).** Same convention as Deal Aggregator + Deal Pipeline. Interactivity is a future cross-page session, not Session 6 scope.

## Actions Taken

- **CREATED** `dashboard/pages/ma_analytics.py` — full page module: subtitle with snapshot-fresh phrase, visual-only filter bar, Zone 1 (5 KPI tiles), Zone 2 + 2.5 placeholders (yellow "Live May 7" pill), Zone 3 channel table (4 live rows + 2 deferred rows with "live May 7" pill in rate column), Zone 4 trend grid (4 panels with `pending` opacity for 3), Zone 5 activity rows.
- **UPDATED** `dashboard/data_sources.py` — added 6 dataclasses (`KPITile`, `ChannelRow`, `TrendPanel`, `ActivityRow`, `CallSummary`, `MAAnalytics`) + `load_ma_analytics()` orchestrator + 8 helpers covering call-vault parsing, stage-advance counts, weekly bucketing, bar scaling, CIM detection. ~570 lines added.
- **UPDATED** `dashboard/theme.py` — added ~270 lines of CSS for `.gb-kpi-tile` (5 colored variants) + `.gb-ch-table` + `.gb-trend-grid` + `.gb-act-row`. Flipped `NAV_ITEMS` `ma-analytics` flag from `False` → `True`.
- **UPDATED** `dashboard/command_center.py` — registered `ma_analytics.render` in `_PAGE_RENDERERS` under url path `ma-analytics`.

## Verification

- AppTest #1 (full app shell): 0 exceptions on landing.
- AppTest #2 (`ma_analytics.render` via `from_function` harness): 0 exceptions; 12 of 12 spot-checks present in rendered HTML (zone headers, Live-May-7 pill, Insurance Brokerage chip, all 3 new CSS classes).
- Streamlit live on `localhost:8501`. All 6 routes return HTTP 200: `/`, `/deal-aggregator`, `/deal-pipeline`, `/ma-analytics`, `/c-suite-skills`, `/infrastructure`.
- Live data sample (today, 7-day window 4/19→4/25): Zone 1 shows Owner conversations=3 (↑ 1 vs 2 last week), NDAs=0, Financials=0, LOIs=0, Closures=0. Zone 3 Intermediary intro=1, Conference=2. Zone 5 chips for XPX panel + WSN group + Guillermo biweekly.

## Open Loops

- **Browser visual check not performed by Claude.** AppTest passed and all routes return 200, but Kay should eyeball the page to confirm tile colors + trend opacity + channel-table deferred-row styling match the mockup. If anything drifts, iterate before May 7.
- **Active niches list is hardcoded.** Switching to a Google Sheets read is a follow-up — same time as wiring the JJ master sheet for Zone 3 / Zone 4 JJ-dials panel.
- **CIM detection regex is loose.** `_count_cims_in_window` matches "CIM received/signed/attached" patterns in email-scan-results bodies but could under- or over-count when scanners use new phrasing. Audit on first DealsX-live week (counts will be more verifiable then).
- **Conferences hint list (`xpx`, `acg`, `panel`, `wsn`, etc.) maintained inline.** When Kay attends a new conference type, the slug-hint constant needs an addition or the call won't be classified. Calibration candidate: derive from a `topic/conference-*` tag instead of slug-hint matching.

## Deferred (Post-May-7)

- **Wire DealsX integration into Zones 2 / 2.5 / DealsX rows in Zone 3.** Live-May-7 placeholders flip to live readers.
- **Audit DealsX AI taxonomy vs JJ call-log outcomes.** Per Session 4 PM open loop — align both or build mapping table.
- **Confirm DealsX LinkedIn DM metric semantics** before tuning Zone 3's DealsX-LinkedIn row.

---

**Dashboard dev server:** `dashboard/.venv/bin/streamlit run dashboard/command_center.py` — port 8501. Kill with `lsof -ti:8501 | xargs kill` before next session.

**Build sequence status:** Sessions 1, 2, 3, 4, 4.5, 5 (partial), 6 shipped. **All 6 nav items now serve content.** Post-May-7 scope = DealsX zone wiring; Session 5 part 2 (Infrastructure auth probes / Credits / Calibration) remains.

---

# Session 6 — Extended (Saturday afternoon → evening)

Long extended session after the morning Session 6 ship. Kay drove it
remotely from her phone via Remote Control mid-way through. ~6 hours,
12 commits. Full mockup-fidelity sweep + production-readiness +
strategic graduation (Decisions-only briefing migration).

## Decisions

- **APPROVE: Mockup-fidelity polish sweep** — Kay's "the mockups were amazing, we just needed them live" reframed scope. Six fixes in one bundle: font cascade override (Streamlit ships Source Sans Variable that beats Avenir Next), sidebar nav spacing tightening, landing hero tile (56px / weight-200 headline + accent gradient + 4 stage breakdown cells), Active Deal Pipeline stat-pills + filter pill rows, C-Suite & Skills filter pill row, Infrastructure subtitle voice. Plus: air restoration (rolled back the gap:0 rule that was squishing zones), kanban empty-state padding, Active Deal Pipeline column min-height bump, topbar alignment, summary-strip color coding across 3 pages, sidebar active-state blue via .streamlit/config.toml primaryColor (Emotion CSS-in-JS overrode external CSS).
- **APPROVE: Infrastructure Zones 2/3/4 ship as YAML-driven catalogs** rather than wait for live API readers. External Connectivity (13 services), Credits & Spend (6 tiles), Calibration & Learning (4 entries this week). Mirrors the tech_stack.yaml pattern; live readers swap in later as a delta against this baseline.
- **APPROVE: Attio snapshot scheduled refresh — hourly Mon-Fri 8am-8pm ET** (65 fires/week). Built `scripts/refresh_attio_snapshot.py` reading Active Deals - Owners list, deduping by record_id, fetching parent record fields. Wraps via `scripts/refresh-attio-snapshot.sh`, plist registered. Tested end-to-end: 18 active deals + 132 closed (was 131; one new closure since yesterday).
- **APPROVE: JJ snapshot scheduled refresh — Mon-Fri 9am/2:30pm/6pm ET** (15 fires/week). Built `scripts/refresh_jj_snapshot.py` scanning each niche sheet's working tab + every "Call Log M.DD.YY" tab via Sheets API metadata. Used gog refresh_token export + OAuth refresh to access Sheets API directly (gog doesn't expose tab metadata). Result: 133 lifetime dials surfaced (vs 2 with working-tab-only scan); 80 dials this week. Premium Pest had 8 hidden Call Log tabs.
- **APPROVE: Closed-strip post-NDA split via meaningful_conversation/notes engagement signal.** Without true Attio stage history, used the next-best signal: deals with `meaningful_conversation` OR notes attached count as post-NDA failures (had real engagement). Audit across all 132 closed entries: 2 post-NDA, 130 pre-NDA outreach attrition. Closed strip on Active Deal Pipeline + landing hero now show post-NDA only.
- **APPROVE: Weekly-tracker history backfills NDAs trend panel.** 6 weekly tracker snapshots in vault (`brain/trackers/weekly/*-weekly-tracker.md`) parsed into `WeeklyTrackerSnapshot` dataclasses. NDAs panel went from "Pending data history" to live with 2 historical peaks visible (Mar 20 + Mar 27). Reply rate stays pending (no source pre-DealsX).
- **APPROVE: Filter pills interactive on 3 of 4 pages via st.segmented_control.** Deal Aggregator (Today / This week / All), Active Deal Pipeline (All / Recent <14d / Stalled), C-Suite & Skills (All / Scheduled / On-demand / Gaps only). M&A Analytics intentionally NOT wired — its 5 zones use different time scopes; needs `load_ma_analytics(window_days=...)` refactor first (~30 min separate task).
- **APPROVE: Production-readiness bundle (A1+A2+A3).** Stale-snapshot banner with weekend-aware thresholds (won't fire on legitimate weekend gaps); health-monitor coverage of both new refresh jobs + expanded launchd jobs list to match CLAUDE.md; dashboard README covering architecture / data flow / scheduled jobs / how to add a new page / gotchas / testing pattern / session history.
- **APPROVE: Migrate morning briefing 4-bucket → Decisions-only.** Per the original migration plan in CLAUDE.md and `feedback_build_new_before_sunset_old`, this was held until the dashboard was operational. Gating condition met today. Single Decisions list ≤5 items, ordered by 🔴/🟡/🟢 urgency, RECOMMEND framing, header line points at dashboard for context. Tomorrow morning is first test.
- **APPROVE: CIM count regex fix — reject negation contexts.** Audited `_count_cims_in_window` against every email-scan-results file in vault. Truth: 0 CIMs to date. Prior regex matched "CIM received" inside "No CIM received" giving false positive of 1. Added `_CIM_NEGATION` guard. Validated with 8 unit tests.

## Actions Taken

12 commits this session (in order):

1. **8db81ca** Session 6: M&A Analytics page (non-DealsX zones) — full page render
2. **(auto)** Background hook: dashboard_landing.py landing hero rewrite as `aec1db9 update dashboard`
3. **7b36318** Mockup-fidelity polish sweep: font, sidebar, hero, filter pills
4. **22df502** Match Infrastructure summary strip to mockup
5. **3446ea5** C-Suite & Skills summary: always show scheduling gap pill, color numbers
6. **e5f71f6** Restore inter-zone air, fix kanban empty-state squish
7. **53b5203** Deal Aggregator summary: color number pills per mockup
8. **fe0f4c2** Align main content top with sidebar brand top
9. **4788885** Sidebar nav: blue active text, mockup spacing + weight
10. **0173485** Force blue text on active sidebar nav via descendant *
11. **a8ed23b** Infrastructure: ship Zones 2/3/4 + Streamlit theme config
12. **0822b05** Attio pipeline snapshot: hourly auto-refresh via launchd
13. **ce20ab1** JJ activity wired into M&A Analytics + scheduled refresh
14. **ed6ffbd** JJ snapshot: enumerate Call Log tabs via Sheets API
15. **(auto)** dashboard + scripts edits as `320427e update context, dashboard, scripts` (post-NDA split)
16. **bc53104** M&A Analytics Zone 4 NDAs panel: backfill from weekly-tracker history
17. **ec6eccf** Fix CIM count false positive: reject negation contexts
18. **242cb29** Filter pills now interactive on 3 pages via st.segmented_control
19. **d3976f5** Dashboard production-readiness: stale banner, health coverage, README
20. **e5b16fe** Morning briefing: migrate 4-bucket → Decisions-only post-dashboard

(Background auto-commit hook grabbed 2 of these as "update X" commits during the session — content is in HEAD.)

**CREATED:**
- `dashboard/.streamlit/config.toml` (theme provider config)
- `dashboard/data/external_services.yaml` + `credits.yaml` + `calibration.yaml`
- `dashboard/README.md` (architecture + gotchas + session history)
- `scripts/refresh_attio_snapshot.py` + `refresh-attio-snapshot.sh`
- `scripts/refresh_jj_snapshot.py` + `refresh-jj-snapshot.sh`
- `~/Library/LaunchAgents/com.greenwich-barrow.attio-snapshot-refresh.plist`
- `~/Library/LaunchAgents/com.greenwich-barrow.jj-snapshot-refresh.plist`
- `brain/context/jj-activity-snapshot.json` (refreshes 3x/day Mon-Fri)
- `brain/context/attio-pipeline-snapshot.json` (rewritten with post-NDA split + hourly refresh)

**UPDATED:**
- `dashboard/data_sources.py` (~700 lines added: MAAnalytics + JJActivity + WeeklyTrackerSnapshot + ExternalService + CreditTile + CalibrationLog dataclasses + 11 new loaders + staleness check helpers)
- `dashboard/theme.py` (~600 lines added: KPI tiles, channel table, trend grid, activity rows, hero tile, sidebar overrides, font cascade override, stale banner, service rows, credit tiles, calibration entries)
- `dashboard/command_center.py` (router + staleness banner)
- `dashboard/pages/dashboard_landing.py` (hero tile rewrite)
- `dashboard/pages/deal_aggregator.py` + `deal_pipeline.py` + `c_suite_skills.py` + `infrastructure.py` (filter interactivity + summary color coding + zone wire-ups)
- `dashboard/pages/ma_analytics.py` (new, then evolved with JJ wire-up + history backfill)
- `CLAUDE.md` (Scheduled Skills table + Morning Workflow Step 9 migration)
- `.claude/commands/goodmorning.md` (Step 7 migration)
- `.claude/skills/health-monitor/SKILL.md` (job coverage + data freshness rows)
- `memory/feedback_briefing_three_buckets.md` (rewritten for Decisions-only)
- `memory/MEMORY.md` (index entry update)

## Verification

- All 6 dashboard routes return HTTP 200: `/`, `/deal-aggregator`, `/deal-pipeline`, `/ma-analytics`, `/c-suite-skills`, `/infrastructure`
- AppTest 0 exceptions on every page modified this session
- Both refresh scripts tested end-to-end with logs written
- launchd shows both jobs registered: `com.greenwich-barrow.{attio,jj}-snapshot-refresh`
- Stale-snapshot banner correctly silent on Saturday (weekend-aware threshold)
- Real data flowing: Attio snapshot 18 active deals + 132 closed; JJ snapshot 133 lifetime + 80 this week; weekly tracker NDAs 2 historical peaks; CIM count 0 (truth)

## Open Loops

- **First Decisions-only briefing tomorrow morning** — Sunday's briefing (or Monday's if no Sunday) is the first real test of the new format. Watch for: feels-too-sparse, missing-context, urgency-emoji-noise. Adjust based on Kay's reaction.
- **M&A Analytics filter wire-up deferred** — needs `load_ma_analytics(window_days=...)` refactor (~30 min). Visual filter bar still renders but doesn't drive data.
- **Dropdowns + search interactivity across pages** — visual stubs only. ~30-45 min/page.
- **Active niches still hardcoded** in `_ACTIVE_NICHES` (Insurance Brokerage / Fine Art Storage / Equipment Servicing / Managed IT Services). Would auto-update Zone 5 + JJ-snapshot scope if pulled from Industry Research Tracker sheet (~45 min).
- **Hardcoded API key in `scripts/attio_create_people.py:14`** — security tech debt. Should read from env. ~5 min next session.
- **Premium Pest in JJ snapshot** — currently scanned (131 dials surfaced) but flagged "not active per session decisions". Decide: reactivate as active niche OR remove from JJ scan list. ~5 min decision + edit.

## Deferred

- **JJ Saturday refresh** — Mon-Fri only currently. Weekends could run too if Kay wants weekend dial visibility, but JJ doesn't work weekends so probably fine as-is.
- **DealsX integration (May 7)** — wires Zones 2 + 2.5 in M&A Analytics + DealsX rows in Zone 3.
- **Infrastructure live API readers** — auth probes, billing API for Apollo/Anthropic, calibration-workflow output reader. YAML stubs ship now; live wiring later.

## Strategic Note

The dashboard is now Kay's daily operational surface. Tomorrow morning's
briefing tests whether the migration sticks. If the Decisions-only format
feels right, the dashboard project's purpose is fulfilled — collapsed Kay's
morning routine from "scroll through 4 buckets + system status" to "decide
on ≤5 items, dashboard for context."

If it feels too sparse, recovery is easy: revert `feedback_briefing_three_buckets.md`
+ CLAUDE.md Step 9 + goodmorning.md Step 7 to the 4-bucket format. The dashboard
remains regardless — it's value-additive, not load-bearing on the briefing format.

---

# Saturday Evening — Launchd Hardening Tech-Debt Block (~1.5hr)

3-hour budget, finished in ~1.5hr. Bead `ai-ops-1` partial-complete.
Plan: [[outputs/2026-04-25-saturday-launchd-hardening-plan]]. Root cause:
[[outputs/2026-04-20-target-discovery-phase2-root-cause]].

This block was the originally-calendared 9am-4pm Saturday session that
got displaced by the unplanned Dashboard Session 6 marathon. Surfaced
mid-evening when Kay asked "did the multi-hour tech debt session
happen today?" Took two follow-ups (look at earlier this week, then
"what was scheduled for 11am") before I checked the calendar. The
calendar event title was literally `Tech-debt block: launchd hardening`
with `topic/tech-debt` tag on the plan file in `brain/outputs/`.

## Decisions

- **APPROVE: Cut 6-9hr plan to 3hr, ship critical-path L1+L2+L3, defer L4.** Trace: [[traces/2026-04-25-tech-debt-three-hour-scope-cut]]. Critical path = target-discovery Phase 2 because Sunday 10pm fire is the canonical re-test of the 4/19 silent-failure bug. Other 4 mutating skills don't have a fire pending tomorrow.
- **APPROVE: Wrapper-side prompt swap, not SKILL.md mode handler, for headless Phase 2 instructions.** Trace: [[traces/2026-04-25-headless-prompt-as-wrapper-swap]]. SKILL.md stays conversational; `headless-phase2-prompt.md` is the imperative runbook. Wrapper detects `skill:args` pair and pipes file content as user prompt instead of bare `/skill-name`.
- **APPROVE: Driver script (`validate_phase2_integrity.py`) over inline bash case-statement validators.** Per-niche fan-out is cleaner in Python; multi-niche support out of the box; same pattern future skills can copy.
- **APPROVE: Pre-grant authorization for autonomous execution through commits + plist reload + launchctl reload.** Per `feedback_decision_fatigue_minimization`. Mitigated by per-layer commits (rollback unit = layer), plist backup before edit, smoke tests before launchctl reload.
- **APPROVE: Calendar query order memory.** [[memory/feedback_what_was_planned_query_order]]. Calendar → beads → `brain/outputs/` → session-decisions, never trust session-decisions alone for "what was planned/scheduled" questions.
- **APPROVE: Mutating-skill hardening pattern memory.** [[memory/feedback_mutating_skill_hardening_pattern]]. Every scheduled mutating skill needs headless prompt + POST_RUN_CHECK validator + SKILL.md MANDATORY section. Read-only skills exempt.

## Actions Taken

**CREATED:**
- `scripts/validate_phase2_integrity.py` — driver fans out across active JJ-Call-Only niches (`JJ_CALL_NICHES` env), calls `enrichment_integrity_check.py` per sheet, aggregates exit codes
- `.claude/skills/target-discovery/headless-phase2-prompt.md` — non-interactive runbook for Sunday Phase 2 fire (forbids YES/NO/DISCUSS, mandates pool-artifact-first ordering)
- `brain/traces/2026-04-25-tech-debt-three-hour-scope-cut.md`
- `brain/traces/2026-04-25-headless-prompt-as-wrapper-swap.md`
- `~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/feedback_what_was_planned_query_order.md`
- `~/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/feedback_mutating_skill_hardening_pattern.md`

**UPDATED:**
- `scripts/run-skill.sh` — POST_RUN_CHECK env-var support, $TODAY substitution, EXIT_CODE override on validator failure, distinct "VALIDATOR FAILED" Slack message, headless-prompt detection via `skill:args` case statement
- `.claude/skills/target-discovery/SKILL.md` — Stop Hook section flipped to "(MANDATORY)" with copyable bash invocation; defense-in-depth note about wrapper redundancy
- `~/Library/LaunchAgents/com.greenwich-barrow.target-discovery-sunday.plist` — `phase2-sunday` arg in ProgramArguments, POST_RUN_CHECK + JJ_CALL_NICHES env vars (original backed up to `.bak-2026-04-25`), reloaded via `launchctl unload && load`
- `CLAUDE.md` — Scheduled Skills table corrected (target-discovery Phase 2 is Sunday 10pm not 11pm; jj-operations is Sunday 6pm not 11pm — doc rot fixed); new "Wrapper hardening pattern" section under Infrastructure
- `MEMORY.md` — index entries for both new feedback memories

**Commits (3, on `imac-mid-day-save-2026-04-22`):**
- `8d42724` Launchd hardening L1+L2: post-run validator + headless Phase 2 prompt
- `9fb9369` Launchd hardening L3: SKILL.md mandates validator as Phase 2 last step
- (CLAUDE.md commit) — schedule corrections + wrapper hardening pattern doc

## Verification

- Driver smoke test today (no Phase 2 ran today): exit 2, "pool artifact missing at brain/context/jj-week-pool-2026-04-25.md; Phase 2 Step 1 produced nothing" — exact failure mode that silently passed on 4/19
- Wrapper override logic isolated test: `EXIT_CODE=0` → validator returns 2 → `EXIT_CODE` overridden to 2, `VALIDATOR_FAILED=1` set
- `plutil -lint` plist OK
- `launchctl list | grep target-discovery` shows job registered post-reload

## Open Loops

- **Sunday 10pm Phase 2 canonical first-fire test** — tomorrow night is the real validation. Watch tomorrow morning for: (a) pool artifact at `brain/context/jj-week-pool-2026-04-26.md`, (b) no `VALIDATOR FAILED` Slack alert in #operations between 10pm Sun and 6am Mon, (c) JJ's Monday 10am tab populated with Col K owner names. If validator fires, the alert message will name `target-discovery` + the missing/broken niche.
- **Layer 4 — extend wrapper hardening to 4 other mutating skills.** `jj-operations-sunday`, `nightly-tracker-audit`, `weekly-tracker`, `relationship-manager`. Each is ~30-45min in a follow-up block. Pattern documented in CLAUDE.md + `feedback_mutating_skill_hardening_pattern.md`.
- **`jj-operations-sunday` timing quirk:** plist fires Sunday 6pm but the SKILL.md stop hook expects today's pool artifact (which Phase 2 doesn't write until Sunday 10pm). Either (a) the design assumes prep reads LAST week's pool — needs SKILL.md clarification, or (b) the plist time is wrong — needs flip to Monday early-AM. Out of scope for this block; investigate before adding L4 validator.
- **Calendar-block-displaced-by-dashboard pattern.** Captured in `feedback_what_was_planned_query_order.md` for the retrieval miss, but the deeper failure was Claude letting unplanned dashboard work consume a calendared block. Calibration candidate: stop hook on session start that reads today's calendar and refuses to deviate from a 3+ hour block without explicit Kay override.

## Deferred

- **Live end-to-end Phase 2 fire test before Sunday.** Would consume Apollo credits + write to real Pest Control sheet. Sunday 10pm launchd is the canonical first run; manual pre-test isn't worth the cost.
- **Layer 4 SKILL.md updates** for the other 4 mutating skills.
- **CLAUDE.md Scheduled Skills full audit** — only fixed the two times that touched today's work; other rows may also be doc-rotted vs plist Hour values.

## Calibration Candidates

- **Calendar-aware session start.** Add to `goodmorning` (or a separate session-start hook): read today's calendar, surface any 3+ hr blocks before any other agenda item. Forces a "are we honoring the block?" gate before unplanned work absorbs the day. Same hook on Saturday/Sunday since this happened on a Saturday.
- **Beads CLI install.** `bd: command not found` when I tried to check `ai-ops-1` status. Beads is in CLAUDE.md as the canonical task system; install + sync should be a setup-checklist item.
- **brain/outputs/ in default search scope.** Today's miss was searching `brain/context/` + `memory/` but not `brain/outputs/` — the plan file was tagged `topic/tech-debt` and would have surfaced. Add `brain/outputs/` to any "look up what was planned" workflow.


