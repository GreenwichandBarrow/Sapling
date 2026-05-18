---
date: 2026-05-17
type: context
title: "Session Decisions — 2026-05-17"
tags: ["date/2026-05-17", "context", "topic/session-decisions", "topic/to-do-consolidation", "topic/dashboard", "topic/deal-aggregator", "status/done"]
---

# Session Decisions — 2026-05-17 (Sunday)

Source: synthesized from [[brain/context/continuation-2026-05-17-2|continuation #2]].
Two prior commits ([d8613e1], [5e01423]) already pushed to origin; HEAD == origin/main.

## Decisions

### To Do consolidation

- **APPROVE** — Single `To Do` tab with Status (Not Completed / On-going / Completed) + Horizon (Short Term / Long Term / Weekly Recurring Mon–Sat) dropdowns. No sweep job, no donut charts. Collapse thin boundaries; the underlying data is inherently weekly-batch so per-tab fragmentation added structure without signal.
- **APPROVE** — Weekly dashboard freshness is acceptable (not live/daily). Data arrives in weekly batches; "live" was a false premise, so daily-refresh expectations were chasing a problem that doesn't exist.
- **DECIDED** — Recurring row canonical shape = Status `On-going` + Horizon `Weekly Recurring {Day}` ONLY. Never duplicate recurrence/day text in Notes. (Codified: `feedback_recurring_row_canonical_shape.md`.)
- **DECIDED** — Email to-dos = one row per recipient. The binary checkbox maps 1:1 to a single recipient; bundling recipients breaks completion tracking. (Codified: `feedback_email_todos_one_per_recipient.md`.)

### Dashboard / infra diagnosis

- **REJECT** — Dedicated dashboard-maintenance agent. Agents don't fix unreliable plumbing; the fix is wiring the missing feeds + loud validators that fail on unexpected zeros. A maintenance agent would mask the root cause class instead of eliminating it.
- **REJECT** — Repoint dashboard to the weekly-tracker Google Sheet as system of record (task 9 superseded). The M&A Analytics page already implements a 9-snapshot weekly archive sourced from vault/Attio; the sheet has never been populated because weekly-tracker never ran. Rebuilding a sheet-source layer would duplicate working infrastructure.
- **APPROVE** — Dashboard is architecturally sound. Pipeline / broker-scan / M&A-model / 9-snapshot archive all work. One root-cause class explains every gap: (a) macOS-on-Linux assumptions on a systemd VPS, (b) proprietary-flow feeds never wired (DealsX, conferences), (c) operator-maintained YAML mistaken for live data. No architecture change.

### Deal-aggregator scoping

- **REJECT** — 2-week Gantt milestone sequencing. Over-structuring; capture the core workstream + daily cadence only, leave the ~13 backlog Gantt items unscheduled rather than forcing them onto a week grid. (Codified: `feedback_no_overstructured_project_schedules.md`.)
- **PASS** — Stale "Re: Touch Base" Gmail draft (5/12) left as-is per Kay. Routine; no downstream action.

## Actions Taken

- **CREATED / UPDATED** — To Do consolidation shipped live and verified: single `To Do` tab, Status/Horizon dropdowns, retired tabs renamed `_retired_*_2026-05-17` and hidden (not deleted — rollback window), habit split (8 habits incl. ACV drink / Probiotic protein shake), recurring rows deduped to 4 canonical (rows 68/69/70/210), `archive-todo` retired.
- **UPDATED** — JJ credentials macOS→Linux fix shipped: `scripts/refresh_jj_snapshot.py` cross-platform resolver, verified resolving to `/home/ubuntu/.config/gogcli/credentials.json`.
- **UPDATED** — Sunday tracker week distributed to day tabs; Sunday day tab split into individual email rows ([[entities/carlos-nieto|Carlos]], Hamptons Pest, Jay & Jason, Matt, Becky, Laura, [[entities/krupa-shah|Krupa]], Deborah) + "Claude: specialized agents" / "Claude: to-do per day". Laundry + Axial preserved checked.
- **CREATED** — 7 memory files (in [d8613e1]): `feedback_email_todos_one_per_recipient`, `feedback_no_overstructured_project_schedules`, `feedback_ongoing_todo_capture_ask_placement`, `feedback_recurring_row_canonical_shape`, `feedback_weekly_plan_layers_on_carryover`, `project_phase2_validator_precedes_jj_tabs`, `reference_gog_no_hide_tab_jj_archive`.
- **CREATED** — Continuation #2 written ([[brain/context/continuation-2026-05-17-2]]).
- **CREATED / DELETED-PENDING** — Committed full session as [d8613e1]; savestate [5e01423]. Both pushed to origin (HEAD == origin/main).

## Deferred

- **DEFER** — Deal-aggregator outreach + daily 5-email/LinkedIn cadence begins **Monday AM 2026-05-18** (scheduled, never Sunday).
- **DEFER** — Delete `_retired_*` To Do tabs **~2026-05-24** after a week of clean operation (consolidation rollback window).
- **DEFER** — Task 12: decide retire-vs-schedule the `weekly-tracker` skill (never run; superseded by M&A archive — likely retire). Resolve inside the next execution session, do NOT rebuild around the sheet.

## Open Loops

- **Tasks 6–13 dashboard/infra execution block** — next session via `/pickingback`. Sequence: T6 (re-run JJ snapshot, verify Operations-calls non-zero + timer enabled) → T7 (DealsX manual weekly feed, seed 5/11–5/15 = 436 sent / 11 replied / 5 positive / 12 bounced) → T8 (harden `validate_jj_snapshot_integrity.py` + peers to fail loud on unexpected zeros) → T11 (fix coaching-vs-intermediary misclassification: [[entities/harrison-wells|Harrison Wells]] 5/15 + Jackson Niketas 5/12 are coaching not deal-flow; inflates Owner conv 4 → true 2) → T13 KEYSTONE (sweep scripts/dashboard for macOS-isms → systemd/cross-platform; verify scheduled skills fire on systemd timers) → T9 reframed (verify M&A weekly-archive + Attio-snapshot refresh actually fire) → T12 (retire-vs-schedule weekly-tracker). No blocking open questions.
