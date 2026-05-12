---
name: Task Tracker Migration — Excel → Google Sheets (2026-05-12)
description: One-day full cutover from Excel-based personal task tracker to Google Sheets. Same architecture, same skill verbs, same CLI surface — backend swap only. Triggered by need for browser-native access from any device + Hetzner VPS server access.
type: project
originSessionId: tracker-migration-2026-05-12
---
# Personal Task Tracker — Excel → Sheets Migration (2026-05-12)

## What changed

- **Backend:** openpyxl + iMac Drive `.xlsx` file → Google Sheets API (`requests` + gog refresh-token export)
- **Access:** Mac-only (iMac Drive sync) → any browser, any device, anywhere
- **Sheet:** `TO DO 5.12.26` — id `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`
- **URL:** https://docs.google.com/spreadsheets/d/1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk/edit
- **Location:** `STRATEGIC PLANNING` Drive folder (same parent as the old Excel)

## What stayed the same

- **5-tab architecture:** Live Week / To Do / To Do Long Term / Projects / Myself Renewed Healthcare (+ Deal Aggregator Expansion Gantt, + Completed To Do auto-created by archive-todo)
- **Skill verbs:** all 9 (`append`, `promote`, `schedule-to-day-slot`, `archive`, `archive-todo`, `projects-create-gantt`, `reformat`, `report`, `gantt-tick`) — same CLI args
- **Layout:** 7 habits, 15 priority slots per day, 8 notes rows per day, big-% display rows 17-21, Mon-Sun European week
- **Palette:** sage-light #e8efd8, sage-dark #7a8c4d, sage-extra-light #f3f7e8, entity tints unchanged
- **Auto vs surface-for-approval rules** in SKILL.md decision matrix
- **Trace policy:** `append` goes to `logs/scheduled/`, decision-content verbs go to `brain/traces/`

## What's different (intentional)

- **Native Sheets primitives** replace Unicode glyphs:
  - `☐ / ✅` → native checkboxes (Data Validation → Checkbox)
  - Implicit free-text Type/Project → native dropdowns (Data Validation → Dropdown)
  - Color-coded done state still uses CF rules, but the trigger is `=$A2=TRUE` (checkbox boolean), not `=$B6="✅"` (Unicode string match)
- **Rollback path:** snapshot affected ranges to `brain/context/rollback-snapshots/tasks-{verb}-{timestamp}.json` BEFORE write, last 5 retained per verb. Replaces .xlsx file-copy backups.
- **Authentication:** Mints a fresh Google access token at the start of each verb run via `gog auth tokens export` → POST to oauth2.googleapis.com/token. Same pattern used by `scripts/refresh_jj_snapshot.py`.
- **API quota backoff:** 5x exponential retry (1s..16s) on 429 / 5xx responses.
- **No `lsof` file-lock guardrail** — Drive handles concurrency natively. Excel-vs-script-write race condition no longer exists.
- **DEPRECATED scripts:** `build_tasks_excel.py`, `populate_tasks_from_motion.py`, `maintain_tasks_excel.py`. Kept in repo for reference, never re-run. Any future rebuild uses the one-shot `/tmp/tracker-migration/build_sheet.py` instead.

## Files touched

- `scripts/task_tracker.py` — full rewrite, Excel → Sheets API
- `.claude/skills/task-tracker-manager/SKILL.md` — file scope, hard guardrails, output expectations
- `memory/project_personal_task_tracker.md` — file location, build scripts, design decisions
- `scripts/build_tasks_sheet.py` — one-shot build + data-migrate script (committed, re-runnable for future rebuilds when Kay rotates to a new yearly tracker)

## Cutover sequence

1. Created new Sheet via API + moved to `STRATEGIC PLANNING` folder
2. Built 6 tabs (Live Week, To Do, To Do Long Term, Projects, Myself Renewed Healthcare, Deal Aggregator Expansion) with native checkboxes + dropdowns + CF
3. Downloaded source `TO DO 4.26.26.xlsx` via gog drive download
4. Migrated all data: To Do rows (status, task, type, project, due, notes), To Do Long Term rows, Projects index with HYPERLINK formulas, Healthcare milestones + ticks, Live Week habits + priorities + notes
5. Added today's Saltoun To Do row + promoted to Tuesday slot 1
6. Rewrote `scripts/task_tracker.py` for Sheets
7. Smoke-tested verbs against the new Sheet

## Triggers to revisit

- If Kay says "I'm back on the Mac and want offline Excel back" → reverse the migration; both backends share the same architecture.
- If Sheets API quota becomes a real problem (unlikely at this scale, ~5 writes/day max) → consider local cache layer.
- If Kay wants per-niche or per-entity tabs broken out → extend the Projects index pattern.

## Why we did this

Source: Kay can't access the Excel tracker from the Hetzner VPS server or from any browser/device that isn't the iMac. Sheets-native gives her one tab in Chrome alongside the Streamlit dashboard + Conference Pipeline + Industry Research Tracker — all browser-native, all the time.
