#!/usr/bin/env python3
"""One-shot migration: consolidate the personal task tracker into a single
`To Do` tab with Status (3-state dropdown) + Horizon (dropdown) columns.

Retires `To Do Long Term`, `Recurring Weekly To Dos`, `Completed To Do`,
`_donut_data` (renamed `_retired_{name}_{date}` + hidden — NOT deleted; deletion
is a separate follow-up after a week of verified clean operation).

Dry-run by default. Pass --apply to write. Always snapshots first.

Design: see /home/ubuntu/.claude/plans/iridescent-rolling-manatee.md
"""
from __future__ import annotations

import argparse
import sys
from datetime import date

import scripts.task_tracker as tt

RETIRE_DATE = "2026-05-17"

STATUS_OPTIONS = ["Not Completed", "On-going", "Completed"]
HORIZON_OPTIONS = [
    "Short Term", "Long Term",
    "Weekly Recurring Mon", "Weekly Recurring Tue", "Weekly Recurring Wed",
    "Weekly Recurring Thu", "Weekly Recurring Fri", "Weekly Recurring Sat",
]

# To Do new column layout (0-based): A..F unchanged, G = Horizon
TODO_COL_HORIZON = 6
NEW_TODO_HEADERS = ["Status", "Task", "Type", "Project", "Due", "Notes", "Horizon"]

RETIRE_TABS = [
    tt.TAB_TODO_LONG_TERM,
    tt.TAB_RECURRING_TEMPLATE,
    tt.TAB_COMPLETED_TODO,
    tt.TAB_DONUT_DATA,
]


def _day3(day_raw: str) -> str | None:
    """Normalize a Recurring 'Day' value to 3-letter (Mon..Sun)."""
    if not day_raw:
        return None
    idx = tt.DAY_BY_NAME.get(str(day_raw).strip().lower())
    if idx is None:
        return None
    return tt.DAY_LABELS[idx]  # DAY_LABELS = [Mon,Tue,Wed,Thu,Fri,Sat,Sun]


def _lt_status_map(old: str) -> str:
    """Map old To Do Long Term text status -> new 3-state Status."""
    o = str(old or "").strip().lower()
    if o == "done":
        return "Completed"
    if o in ("active", "on hold"):
        return "On-going"
    return "Not Completed"  # idea / promoted / blank


def _last_content_row(values: list[list]) -> int:
    """1-based row number of the last row with any non-empty cell. values is A1-origin."""
    last = 0
    for i, row in enumerate(values):
        if any(str(c).strip() for c in row):
            last = i + 1
    return last


def main() -> int:
    ap = argparse.ArgumentParser("migrate_todo_consolidation")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry-run)")
    args = ap.parse_args()
    dry = not args.apply
    tag = "DRY RUN" if dry else "APPLY"

    c = tt.SheetsClient()
    meta = c.get_metadata()

    todo = tt.find_tab(meta, tt.TAB_TODO)
    if not todo:
        sys.exit("migrate: 'To Do' tab not found")
    todo_sid = todo["sheetId"]
    grid_rows = todo.get("gridProperties", {}).get("rowCount", 1000)

    # ---- 1. Snapshot everything we touch -----------------------------------
    snap_ranges = [
        f"'{tt.TAB_TODO}'!A1:G{grid_rows}",
        f"'{tt.TAB_TODO_LONG_TERM}'!A1:F300",
        f"'{tt.TAB_RECURRING_TEMPLATE}'!A1:F100",
        f"'{tt.TAB_COMPLETED_TODO}'!A1:G300",
        f"'{tt.TAB_DONUT_DATA}'!A1:C20",
    ]
    if dry:
        print(f"[{tag}] would snapshot: {snap_ranges}")
    else:
        sp = tt.snapshot_ranges(c, "migrate-consolidation", snap_ranges)
        print(f"SNAPSHOT: {sp}")

    # ---- 2. Read current To Do --------------------------------------------
    todo_vals = c.get_values(f"'{tt.TAB_TODO}'!A1:F{grid_rows}")
    existing_last = _last_content_row(todo_vals)  # includes header row 1
    print(f"To Do: {existing_last} rows with content (incl header).")

    # Convert existing data rows (2..existing_last): Status + Horizon
    status_writes = []   # (row, value)
    horizon_writes = []  # (row, value)
    converted = 0
    for r in range(2, existing_last + 1):
        row = todo_vals[r - 1] if r - 1 < len(todo_vals) else []
        task = (row[tt.TODO_COL_TASK].strip()
                if len(row) > tt.TODO_COL_TASK and row[tt.TODO_COL_TASK] else "")
        if not task:
            continue
        old_status = row[tt.TODO_COL_STATUS] if len(row) > tt.TODO_COL_STATUS else ""
        new_status = "Completed" if tt._is_truthy(old_status) else "Not Completed"
        status_writes.append((r, new_status))
        horizon_writes.append((r, "Short Term"))
        converted += 1
    print(f"  -> convert {converted} existing rows (Status enum + Horizon=Short Term)")

    # ---- 3. Gather folded rows from the 3 retiring tabs --------------------
    folded: list[list] = []  # each = [Status,Task,Type,Project,Due,Notes,Horizon]

    # 3a. To Do Long Term
    lt_vals = c.get_values(f"'{tt.TAB_TODO_LONG_TERM}'!A1:F300")
    lt_last = _last_content_row(lt_vals)
    lt_n = 0
    for r in range(2, lt_last + 1):
        row = lt_vals[r - 1] if r - 1 < len(lt_vals) else []
        task = (row[tt.LT_COL_TASK].strip()
                if len(row) > tt.LT_COL_TASK and row[tt.LT_COL_TASK] else "")
        if not task:
            continue
        old = row[tt.LT_COL_STATUS] if len(row) > tt.LT_COL_STATUS else ""
        notes = row[tt.LT_COL_NOTES] if len(row) > tt.LT_COL_NOTES else ""
        if old:
            notes = (f"(was LT: {old}) {notes}").strip()
        folded.append([
            _lt_status_map(old), task,
            row[tt.LT_COL_TYPE] if len(row) > tt.LT_COL_TYPE else "",
            row[tt.LT_COL_PROJECT] if len(row) > tt.LT_COL_PROJECT else "",
            row[tt.LT_COL_DUE] if len(row) > tt.LT_COL_DUE else "",
            notes, "Long Term",
        ])
        lt_n += 1

    # 3b. Recurring Weekly To Dos
    rt_vals = c.get_values(f"'{tt.TAB_RECURRING_TEMPLATE}'!A1:F100")
    rt_last = _last_content_row(rt_vals)
    rt_n = 0
    rt_skipped = []
    for r in range(2, rt_last + 1):
        row = rt_vals[r - 1] if r - 1 < len(rt_vals) else []
        task = (row[tt.RT_COL_TASK].strip()
                if len(row) > tt.RT_COL_TASK and row[tt.RT_COL_TASK] else "")
        if not task:
            continue
        d3 = _day3(row[tt.RT_COL_DAY] if len(row) > tt.RT_COL_DAY else "")
        if d3 is None:
            rt_skipped.append(task)
            continue
        folded.append([
            "On-going", task,
            row[tt.RT_COL_TYPE] if len(row) > tt.RT_COL_TYPE else "",
            row[tt.RT_COL_PROJECT] if len(row) > tt.RT_COL_PROJECT else "",
            "",  # Due — n/a for recurring
            row[tt.RT_COL_NOTES] if len(row) > tt.RT_COL_NOTES else "",
            f"Weekly Recurring {d3}",
        ])
        rt_n += 1

    # 3c. Completed To Do (historical)
    ct_vals = c.get_values(f"'{tt.TAB_COMPLETED_TODO}'!A1:G300")
    ct_last = _last_content_row(ct_vals)
    ct_n = 0
    for r in range(2, ct_last + 1):
        row = ct_vals[r - 1] if r - 1 < len(ct_vals) else []
        task = row[1].strip() if len(row) > 1 and row[1] else ""
        if not task:
            continue
        notes = row[5] if len(row) > 5 else ""
        comp_date = row[6] if len(row) > 6 else ""
        if comp_date:
            notes = (f"(completed {comp_date}) {notes}").strip()
        folded.append([
            "Completed", task,
            row[2] if len(row) > 2 else "",
            row[3] if len(row) > 3 else "",
            row[4] if len(row) > 4 else "",
            notes, "Short Term",
        ])
        ct_n += 1

    print(f"  -> fold {lt_n} Long Term + {rt_n} Recurring + {ct_n} Completed = "
          f"{len(folded)} new rows")
    if rt_skipped:
        print(f"  !! Recurring rows skipped (bad/blank Day): {rt_skipped}")

    first_fold_row = existing_last + 1
    last_fold_row = existing_last + len(folded)
    dropdown_last = max(last_fold_row + 50, 400)  # generous validation range

    print(f"\n[{tag}] PLAN:")
    print(f"  - To Do!G1 = 'Horizon'")
    print(f"  - Status dropdown A2:A{dropdown_last}  {STATUS_OPTIONS}")
    print(f"  - Horizon dropdown G2:G{dropdown_last} ({len(HORIZON_OPTIONS)} opts)")
    print(f"  - convert rows 2..{existing_last}; append folded rows "
          f"{first_fold_row}..{last_fold_row}")
    print(f"  - retire+hide tabs: {RETIRE_TABS} -> _retired_*_{RETIRE_DATE}")

    if dry:
        print("\nDRY RUN — no writes. Re-run with --apply.")
        return 0

    # ---- 4. Ensure grid is tall enough ------------------------------------
    if dropdown_last > grid_rows:
        c.batch_update([{
            "updateSheetProperties": {
                "properties": {"sheetId": todo_sid,
                               "gridProperties": {"rowCount": dropdown_last + 10}},
                "fields": "gridProperties.rowCount",
            }
        }])

    # ---- 5. Header + dropdowns -------------------------------------------
    c.values_update(f"'{tt.TAB_TODO}'!G1", [["Horizon"]])
    c.batch_update([
        {"setDataValidation": {
            "range": {"sheetId": todo_sid, "startRowIndex": 1,
                      "endRowIndex": dropdown_last, "startColumnIndex": 0,
                      "endColumnIndex": 1},
            "rule": {"condition": {"type": "ONE_OF_LIST",
                                   "values": [{"userEnteredValue": v} for v in STATUS_OPTIONS]},
                     "showCustomUi": True, "strict": False},
        }},
        {"setDataValidation": {
            "range": {"sheetId": todo_sid, "startRowIndex": 1,
                      "endRowIndex": dropdown_last, "startColumnIndex": TODO_COL_HORIZON,
                      "endColumnIndex": TODO_COL_HORIZON + 1},
            "rule": {"condition": {"type": "ONE_OF_LIST",
                                   "values": [{"userEnteredValue": v} for v in HORIZON_OPTIONS]},
                     "showCustomUi": True, "strict": False},
        }},
    ])

    # ---- 6. Convert existing rows (Status col A, Horizon col G) -----------
    if status_writes:
        a_col = [["" ] for _ in range(2, existing_last + 1)]
        g_col = [["" ] for _ in range(2, existing_last + 1)]
        sd = {r: v for r, v in status_writes}
        hd = {r: v for r, v in horizon_writes}
        for i, r in enumerate(range(2, existing_last + 1)):
            if r in sd:
                a_col[i] = [sd[r]]
                g_col[i] = [hd[r]]
        c.values_update(f"'{tt.TAB_TODO}'!A2:A{existing_last}", a_col)
        c.values_update(f"'{tt.TAB_TODO}'!G2:G{existing_last}", g_col)

    # ---- 7. Append folded rows -------------------------------------------
    if folded:
        c.values_update(
            f"'{tt.TAB_TODO}'!A{first_fold_row}:G{last_fold_row}", folded)

    # ---- 8. Retire + hide the 4 tabs -------------------------------------
    rename_reqs = []
    for name in RETIRE_TABS:
        p = tt.find_tab(meta, name)
        if not p:
            print(f"  (skip retire — '{name}' not present)")
            continue
        rename_reqs.append({
            "updateSheetProperties": {
                "properties": {"sheetId": p["sheetId"],
                               "title": f"_retired_{name}_{RETIRE_DATE}",
                               "hidden": True},
                "fields": "title,hidden",
            }
        })
    if rename_reqs:
        c.batch_update(rename_reqs)

    print(f"\nMIGRATION APPLIED. To Do now {last_fold_row} rows. "
          f"Retired {len(rename_reqs)} tabs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
