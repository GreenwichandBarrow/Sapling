---
date: 2026-04-27
type: context
title: "Continuation — 2026-04-27 #1"
saved_at: 2026-04-27T16:18:59Z
session_number: 1
tags: ["date/2026-04-27", "context", "topic/continuation"]
---

## Active Threads

### Excel To Do tracker — rebuild blocked by AutoSave clobber
**State:** UNFINISHED. The working file `/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.xlsx` was supposed to be expanded from 5 priority rows → 15 priority rows per day on the "This Week" tab, with the notes/ideas/journal area slimmed from 24 rows → 8 rows. The build script was updated, build + populate ran successfully, and 7 priorities were restored. But Excel had the file open with **AutoSave ON** during the rebuild and auto-saved its stale 5-row state back over disk afterward. Kay quit Excel and reopened — saw the OLD layout. Disk verification confirmed: file is back to 5-row layout with notes label "notes · ideas · journal" on row 29.

**What's done:**
- `scripts/build_tasks_excel.py` updated for 15 priority rows (rows 23-37), 8-row notes block (rows 40-47), notes label changed to just "notes" on row 39, env-var output path (`TASKS_XLSX_OUT`).
- Donut chart helper formulas + pct row formula updated to span `:37`.
- Conditional formatting + status dropdown ranges extended.
- Clean template built and verified at `/Users/kaycschneider/My Drive/MANAGER DOCUMENTS/G&B MASTER TEMPLATES/TO DO TEMPLATE.xlsx`. **Template is good — Kay confirmed.**
- Project memory `project_personal_task_tracker.md` updated with template path + new 15-row structure.

**What's pending:**
- Excel must be fully quit (Cmd+Q, not just window close) before re-running the rebuild on the working file.
- Re-run build + populate against `/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.xlsx`.
- Restore the 6 captured priorities (see below) — specifically preserve the ✅ done status on the Boston flight item.
- Tell Kay to disable AutoSave on this file going forward, OR always quit Excel before any rebuild.

**Captured priorities to restore (verified 2026-04-27 @ 12:17 PM):**
- `C23` Renew CitiBike (☐) — Mon
- `E23` Get 5/12 evening coverage (☐) — Tue
- `K23` Look into GLP1 (☐) — Fri
- `C25` Book flight to Boston (confirm LF off) — **B25 = ✅ PRESERVE DONE STATE**
- `C26` Email Matt Luczyk & Charles Gerber (☐) — Mon
- `C27` Pay G&B Taxes (☐) — Mon

**Note:** `C24 'Set up email alerts on FE International & Benchmark'` was previously typed but is GONE in the current file. Kay either cleared it manually or AutoSave dropped it. **Do NOT restore unless Kay explicitly asks.**

**Restoration script (paste-ready for next session):**
```bash
cd "/Users/kaycschneider/Documents/AI Operations" && \
  python3 scripts/build_tasks_excel.py && \
  python3 scripts/populate_tasks_from_motion.py && \
  python3 -c "
from openpyxl import load_workbook
PATH = '/Users/kaycschneider/My Drive/STRATEGIC PLANNING/TO DO 4.26.26.xlsx'
wb = load_workbook(PATH)
ws = wb['This Week']
restorations = [
    ('C23', 'Renew CitiBike', 'B23', '☐'),
    ('E23', 'Get 5/12 evening coverage', 'D23', '☐'),
    ('K23', 'Look into GLP1', 'J23', '☐'),
    ('C25', 'Book flight to Boston (confirm LF off)', 'B25', '✅'),
    ('C26', 'Email Matt Luczyk & Charles Gerber', 'B26', '☐'),
    ('C27', 'Pay G&B Taxes', 'B27', '☐'),
]
for tcell, ttext, scell, status in restorations:
    ws[tcell] = ttext
    ws[scell] = status
wb.save(PATH)
print(f'Restored {len(restorations)} priorities')
"
```

**Root cause:** Excel had the file open with AutoSave ON during my earlier rebuild. AutoSave wrote its in-memory 5-row state back over disk after my writes succeeded. Lesson learned the hard way — for any future rebuild against a Drive-synced Excel file, **first verify Excel is fully quit (Cmd+Q)** then run.

## Decisions Made This Session

- APPROVE: Expand This Week tab from 5 priority rows → 15 per day, slim notes area from 24 → 8 rows, label shortened from "notes · ideas · journal" → "notes". (Kay's request.)
- APPROVE: Save clean template version to `/Users/kaycschneider/My Drive/MANAGER DOCUMENTS/G&B MASTER TEMPLATES/TO DO TEMPLATE.xlsx`. Confirmed by Kay: "template looks good".
- DRAFTED: Build script `OUT` path made configurable via `TASKS_XLSX_OUT` env var so the same script can build the working file or the template without code edits.

## Next Steps

1. **(Kay)** Confirm Excel is fully quit (Cmd+Q, not just window close). AutoSave is the culprit — it must not be running.
2. **(Claude, next session)** Re-run the restoration script above against the working file. Expected: 15 priority rows on This Week, 6 priorities restored with Boston flight marked ✅.
3. **(Kay)** Reopen `TO DO 4.26.26.xlsx`. Verify 15 rows visible per day. If she wants AutoSave disabled to prevent recurrence, File → toggle AutoSave OFF for this file.
4. **(Claude, optional)** If recurrence concerns Kay, modify `build_tasks_excel.py` to write to a temp path and atomically rename → makes the rebuild Excel-AutoSave-resistant.

## Open Questions

- Does Kay want `C24 'Set up email alerts on FE International & Benchmark'` restored as a 7th priority? Currently dropped in the file — she may have cleared it deliberately, or AutoSave dropped it. Default: leave dropped unless she asks.
- Disable AutoSave on this file permanently, or just remember to quit Excel before any future rebuild?
