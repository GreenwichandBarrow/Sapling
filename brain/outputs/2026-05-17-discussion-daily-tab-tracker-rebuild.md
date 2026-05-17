---
schema_version: 1.2.0
date: 2026-05-17
type: discussion-brief
status: draft
skill_origin: socrates
kay_approved: null
kay_approval_date: null
tags:
  - date/2026-05-17
  - output
  - output/discussion-brief
  - status/draft
  - topic/task-tracker-rebuild
  - topic/daily-focus
---

# Discussion — Daily-tab task tracker rebuild

**Direction chosen:** Replace the single Live Week 7-day grid as the daily working surface with seven real, writable, large-font day tabs (Sunday through Saturday) built from the Sunday weekly plan. She lives only in the current day's tab during the week; items move tab-to-tab as completed / incomplete / added / deleted. No mirror, no back-sync. The following Sunday's `goodmorning` planning ceremony reads across the prior week's daily tabs to see what didn't get done and proposes the new week from that.

## Problem framing
The real problem was never "a Today tab with bigger font." The week-at-a-glance grid is itself the source of overwhelm during the week: small text, seven days competing for attention, no single calm place to focus. Sunday the week view is the right tool (planning wide). The rest of the week it scatters her. The need is a hard mode switch: plan wide on Sunday, then collapse into one calm day to live inside and actively work.

## Goal hierarchy
- **Surface ask:** fix the Today tab (font size, mirror behavior).
- **Underlying goal:** separate week-planning mode from daily-execution mode so day-to-day only today is visible, large and focused, and the week grid stops generating anxiety.

## Decision detail (converged)
- **Week boundary:** Sunday to Saturday, inclusive of Sunday.
- **Sunday:** run `goodmorning`; the weekly-planning ceremony finalizes the week including Sunday itself. The system then builds out all seven day tabs (Sun through Sat) as real editable tabs with real native checkboxes, large font.
- **During the week:** work only in the current day's tab. Real checkboxes toggled directly. It is the single surface Sunday through Saturday.
- **Carry behavior:** items move between day tabs on request, completed / incomplete / added / deleted. No automatic day-to-week write-back.
- **No week-grid mirror.** The old Live Week grid is no longer the live working surface; week-level state is a Sunday planning artifact only.
- **Next Sunday:** the planning ceremony reads across the prior week's daily tabs to identify incompletes and proposes the upcoming week from that. The daily tabs ARE the record of what happened.

## Alternatives considered
1. **Do nothing** — keep week grid, enlarge font. Rejected: doesn't fix overwhelm, still a 7-day grid.
2. **Enlarged read-only mirror** (auto-mirror, built 2026-05-17) — Rejected: a formula mirror can't be checked off without destroying itself; the working surface must be writable.
3. **Day as its own living, writable surface** — CHOSEN.
4. **Daily focus leaves the spreadsheet entirely** — Deferred: viable but splits the system across two tools; not needed if writable day tabs work.

## Assumptions surfaced
- "Must be a tab in the same Google Sheet" — treated as load-bearing (donut charts, archive ceremony, recurring template, To Do backlog all live there). Confirmed acceptable; rebuild stays in-Sheet.
- "Two-way sync is needed" — load-bearing assumption REMOVED. No back-sync is the lower-overwhelm design and was confirmed.

## Open questions / deferred to plan
- Fate of the existing Live Week tab plus the auto-mirror Today tab built 2026-05-17 (retire? repurpose as Sunday planning artifact?).
- Donut completion charts plus `_donut_data` helper: re-home per-day or drop.
- Recurring Template tab: how it stamps into the new per-day-tab model.
- To Do backlog plus Completed To Do: relationship to day tabs (source of carry-ins, destination of completed?).
- The "move item between day tabs" verb (completed/incomplete/added/deleted) — new verb spec.
- Sunday `archive` ceremony plus Sunday `goodmorning` overlay rewrite: currently read the single Live Week tab; must instead read across seven daily tabs. Largest behavior change.
- Conditional formatting and native-checkbox parity across seven tabs.
- Migration: today (2026-05-17) is Sunday and the live sheet holds the real current plan; sequence the rebuild without destroying this week's data (hard guardrail: snapshot, never wipe populated data).

## Handoff
Ready for plan mode with this brief as input. Execution owner: `task-tracker-manager` skill. Architectural change touching the archive ceremony, Sunday goodmorning overlay, donut charts, recurring template, and To Do backlog. Goal: plan tight, execute, then run `goodmorning` and test the new model the same Sunday.
