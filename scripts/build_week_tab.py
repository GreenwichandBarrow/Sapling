#!/usr/bin/env python3
"""One-shot builder — create the permanent `Week` planning tab (LEFTMOST,
index 0, before `Sun`) for Kay's task tracker (2026-05-17 design correction).

The tracker has BOTH surfaces:
  * `Week`     — Sunday planning canvas, all 7 days visible, Sun→Sat. Where
                 build-week rebuilds/clears + stamps Recurring and Kay lays
                 out the full week.
  * 7 day tabs — Sun..Sat daily execution surface, fed by `distribute-week`.

Structure follows the `TO DO 6.7.26` Week reference layout:

  Row 1      merged A1:O1 title "WEEK OF Jun 7-13" — 16pt bold, sage-light fill
  Row 3      DAILY FOCUS / THEME
  Row 6      SUNDAY..SATURDAY 2-col-merged day headers
  Rows 8-22  15 visible planning slots/day: status checkbox col + task col per day
  Row 24     notes sub-headers (2-col-merged)

Native checkboxes (Data Validation BOOLEAN). Sage palette. Per-day donut is
intentionally SKIPPED for now (the per-day donuts already live on the 7 day
tabs; the Week tab is a planning canvas, kept simple — flagged in the report).

Modes:
  (default)        reset/format Week tab + wire formulas from day tabs
  --dry-run        report what would be created; NO writes
  --no-populate    compatibility flag; formulas are still wired
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import task_tracker as tt  # noqa: E402

SAGE_LIGHT = tt.hex_to_rgb(tt.SAGE_LIGHT_HEX)
SAGE_DARK = tt.hex_to_rgb(tt.SAGE_DARK_HEX)
SAGE_XL = tt.hex_to_rgb(tt.SAGE_EXTRA_LIGHT_HEX)
INK = tt.hex_to_rgb(tt.INK_HEX)
MUTED = tt.hex_to_rgb(tt.MUTED_HEX)
WHITE = {"red": 1, "green": 1, "blue": 1}


def _txt(value, *, bold=False, size=11, fg=None, bg=None, halign="LEFT"):
    fmt = {"horizontalAlignment": halign, "verticalAlignment": "MIDDLE",
           "textFormat": {"bold": bold, "fontSize": size,
                          "foregroundColor": fg or INK}}
    if bg is not None:
        fmt["backgroundColor"] = bg
    cell = {"userEnteredFormat": fmt}
    if value is not None:
        cell["userEnteredValue"] = {"stringValue": value}
    return cell


def week_label(wd):
    a, b = wd[0], wd[6]
    if a.month == b.month:
        return f"WEEK OF {a.strftime('%b')} {a.day}-{b.day}"
    return f"WEEK OF {a.strftime('%b')} {a.day}-{b.strftime('%b')} {b.day}"


def structure_requests(sid: int, wd) -> list[dict]:
    """All structural/formatting/value requests for the Week tab (Sun→Sat)."""
    R: list[dict] = []

    R.append({"updateSheetProperties": {
        "properties": {"sheetId": sid, "gridProperties": {
            "rowCount": tt.WK_GRID_ROWS,
            "columnCount": tt.WK_GRID_COLS,
            "frozenRowCount": 1,
        }},
        "fields": "gridProperties(rowCount,columnCount,frozenRowCount)",
    }})

    # Reset stale merges, values, formatting, and validation before rebuilding.
    # The Week tab is a formula mirror; old value-populated layouts must not survive.
    full_range = {"sheetId": sid, "startRowIndex": 0, "endRowIndex": tt.WK_GRID_ROWS,
                  "startColumnIndex": 0, "endColumnIndex": tt.WK_GRID_COLS}
    R.append({"unmergeCells": {"range": full_range}})
    R.append({"repeatCell": {
        "range": full_range,
        "cell": {},
        "fields": "userEnteredValue,userEnteredFormat,dataValidation",
    }})
    DI = list(range(7))  # 0=Sun..6=Sat

    # ---- column widths: col0 label 180; per day status 36 + content 200 ----
    R.append({"updateDimensionProperties": {
        "range": {"sheetId": sid, "dimension": "COLUMNS", "startIndex": 0, "endIndex": 1},
        "properties": {"pixelSize": 180}, "fields": "pixelSize"}})
    for i in DI:
        R.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": tt.wk_status_col(i), "endIndex": tt.wk_status_col(i) + 1},
            "properties": {"pixelSize": 36}, "fields": "pixelSize"}})
        R.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": tt.wk_content_col(i), "endIndex": tt.wk_content_col(i) + 1},
            "properties": {"pixelSize": 200}, "fields": "pixelSize"}})

    # ---- Row 1: merged A1:O1 title ----
    R.append({"mergeCells": {
        "range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1,
                  "startColumnIndex": 0, "endColumnIndex": tt.WK_GRID_COLS},
        "mergeType": "MERGE_ALL"}})
    R.append({"updateCells": {
        "rows": [{"values": [_txt(week_label(wd), bold=True, size=16,
                                  fg=INK, bg=SAGE_LIGHT, halign="CENTER")]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0}}})

    # ---- Row 3: daily focus/theme ----
    R.append({"updateCells": {
        "rows": [{"values": [_txt("DAILY FOCUS / THEME", bold=True, size=10, fg=SAGE_DARK)]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": tt.WK_FOCUS_ROW - 1,
                  "columnIndex": 0}}})
    for i in DI:
        c0 = tt.wk_status_col(i)
        R.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_FOCUS_ROW - 1,
                      "endRowIndex": tt.WK_FOCUS_ROW,
                      "startColumnIndex": c0, "endColumnIndex": c0 + 2},
            "mergeType": "MERGE_ALL"}})

    # ---- Day headers (2-col merged, white/sage-dark) ----
    for i in DI:
        c0 = tt.wk_status_col(i)
        full = {"Sun": "SUNDAY", "Mon": "MONDAY", "Tue": "TUESDAY",
                "Wed": "WEDNESDAY", "Thu": "THURSDAY", "Fri": "FRIDAY",
                "Sat": "SATURDAY"}[tt.WK_DAY_ORDER[i]]
        label = f"{full} · {wd[i].strftime('%b')} {wd[i].day}"
        R.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_DAYHDR_ROW - 1,
                      "endRowIndex": tt.WK_DAYHDR_ROW,
                      "startColumnIndex": c0, "endColumnIndex": c0 + 2},
            "mergeType": "MERGE_ALL"}})
        R.append({"updateCells": {
            "rows": [{"values": [_txt(label, bold=True, size=11,
                                      fg=WHITE, bg=SAGE_DARK, halign="CENTER")]}],
            "fields": "userEnteredValue,userEnteredFormat",
            "start": {"sheetId": sid, "rowIndex": tt.WK_DAYHDR_ROW - 1,
                      "columnIndex": c0}}})

    # ---- Priority slots: 15 rows/day ----
    for i in DI:
        sc = tt.wk_status_col(i)
        tc = tt.wk_content_col(i)
        R.append({"setDataValidation": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_SLOT_FIRST_ROW - 1,
                      "endRowIndex": tt.WK_SLOT_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": sc + 1},
            "rule": {"condition": {"type": "BOOLEAN"}, "strict": True}}})
        R.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_SLOT_FIRST_ROW - 1,
                      "endRowIndex": tt.WK_SLOT_LAST_ROW,
                      "startColumnIndex": tc, "endColumnIndex": tc + 1},
            "cell": {"userEnteredFormat": {
                "verticalAlignment": "MIDDLE", "wrapStrategy": "WRAP",
                "textFormat": {"fontSize": 10, "foregroundColor": INK}}},
            "fields": "userEnteredFormat(verticalAlignment,wrapStrategy,textFormat)"}})
        R.append({"repeatCell": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_SLOT_FIRST_ROW - 1,
                      "endRowIndex": tt.WK_SLOT_FIRST_ROW - 1 + tt.TOP_PRIORITY_SLOT_COUNT,
                      "startColumnIndex": sc, "endColumnIndex": tc + 1},
            "cell": {"userEnteredFormat": {"backgroundColor": SAGE_LIGHT}},
            "fields": "userEnteredFormat.backgroundColor"}})
        # Done-row CF: status TRUE → strikethrough + sage-extra-light over the
        # day's status+content columns.
        R.append({"addConditionalFormatRule": {
            "rule": {"ranges": [{"sheetId": sid,
                                 "startRowIndex": tt.WK_SLOT_FIRST_ROW - 1,
                                 "endRowIndex": tt.WK_SLOT_LAST_ROW,
                                 "startColumnIndex": sc, "endColumnIndex": tc + 1}],
                     "booleanRule": {
                         "condition": {"type": "CUSTOM_FORMULA", "values": [
                             {"userEnteredValue":
                              f"=${tt.col_letter(sc)}{tt.WK_SLOT_FIRST_ROW}=TRUE"}]},
                         "format": {"backgroundColor": SAGE_XL,
                                    "textFormat": {"strikethrough": True,
                                                   "foregroundColor": MUTED}}}},
             "index": 0}})

    # ---- Slot row heights ~30px ----
    R.append({"updateDimensionProperties": {
        "range": {"sheetId": sid, "dimension": "ROWS",
                  "startIndex": tt.WK_SLOT_FIRST_ROW - 1, "endIndex": tt.WK_SLOT_LAST_ROW},
        "properties": {"pixelSize": 30}, "fields": "pixelSize"}})

    # ---- Row 50: notes sub-headers (2-col merged) + 51-58 merged block ----
    for i in DI:
        c0 = tt.wk_status_col(i)
        R.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_NOTES_HDR_ROW - 1,
                      "endRowIndex": tt.WK_NOTES_HDR_ROW,
                      "startColumnIndex": c0, "endColumnIndex": c0 + 2},
            "mergeType": "MERGE_ALL"}})
        R.append({"updateCells": {
            "rows": [{"values": [_txt("notes · ideas · jot", size=9,
                                      fg=MUTED, halign="CENTER")]}],
            "fields": "userEnteredValue,userEnteredFormat",
            "start": {"sheetId": sid, "rowIndex": tt.WK_NOTES_HDR_ROW - 1,
                      "columnIndex": c0}}})
        R.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_NOTES_FIRST_ROW - 1,
                      "endRowIndex": tt.WK_NOTES_LAST_ROW,
                      "startColumnIndex": c0, "endColumnIndex": c0 + 2},
            "mergeType": "MERGE_ALL"}})

    return R


def populate_from_day_tabs(client, wd) -> dict:
    """Reverse-populate the Week grid FROM the current 7 day tabs so Kay sees
    this week's already-placed plan at a glance. Reads each day tab's slots
    (rows 17-41, A=status B=task) into the matching Week-grid day block's first 15 visible slots.
    Returns a summary dict."""
    summary = {"slots_written": 0, "per_day": {}}
    for i, day_name in enumerate(tt.WK_DAY_ORDER):
        block = client.get_values(f"'{day_name}'!A1:E{tt.DAY_SLOT_LAST_ROW}")
        sc = tt.wk_status_col(i)
        tc = tt.wk_content_col(i)
        col = tt.col_letter
        # Slots: day-tab priority rows → Week priority rows
        st_vals, tk_vals = [], []
        for r in range(tt.DAY_SLOT_FIRST_ROW - 1, tt.DAY_SLOT_FIRST_ROW - 1 + tt.WK_SLOT_COUNT):
            row = block[r] if r < len(block) else []
            st_vals.append([bool(row[0]) if len(row) > 0 and row[0] not in ("", None) else False])
            tk_vals.append([row[1] if len(row) > 1 and str(row[1]).strip() else ""])
        client.values_update(
            f"'{tt.TAB_WEEK}'!{col(sc)}{tt.WK_SLOT_FIRST_ROW}:{col(sc)}{tt.WK_SLOT_LAST_ROW}",
            st_vals)
        client.values_update(
            f"'{tt.TAB_WEEK}'!{col(tc)}{tt.WK_SLOT_FIRST_ROW}:{col(tc)}{tt.WK_SLOT_LAST_ROW}",
            tk_vals)
        nslots = sum(1 for tk in tk_vals if tk[0])
        summary["slots_written"] += nslots
        summary["per_day"][day_name] = nslots
    return summary


def main():
    ap = argparse.ArgumentParser(prog="build_week_tab")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--no-populate", action="store_true")
    ap.add_argument("--sheet-id", default=None,
                    help="target spreadsheet ID (default: resolver via task_tracker)")
    args = ap.parse_args()

    client = tt.SheetsClient(args.sheet_id) if args.sheet_id else tt.SheetsClient()
    meta = client.get_metadata()
    wd = tt.week_dates(date.today())
    existing = tt.find_tab(meta, tt.TAB_WEEK)

    report = {
        "mode": "dry-run" if args.dry_run else "build",
        "week_sun_to_sat": [d.isoformat() for d in wd],
        "week_label": week_label(wd),
        "week_tab_exists": existing is not None,
        "day_order": tt.WK_DAY_ORDER,
    }

    if args.dry_run:
        report["would"] = [
            f"CREATE '{tt.TAB_WEEK}' tab at index 0 (LEFTMOST, before 'Sun')"
            if existing is None else
            f"'{tt.TAB_WEEK}' already exists (sheetId={existing['sheetId']}) — would re-apply structure",
            "APPLY task-only Week structure re-ordered Sun→Sat (title, "
            "day headers, 25 slots/day, notes block, native "
            "checkboxes, sage palette, done-row CF)",
            "SKIP per-day donut (Week tab is a planning canvas; day tabs keep "
            "their donuts) — design simplification, flagged",
        ]
        report["would"].append(
            "WIRE Week grid formulas from the 7 day tabs current first 15 task slots "
            "(day rows 17-31 → Week rows 8-22)")
        print(json.dumps(report, indent=2))
        return

    # ---- snapshot (additive op; snapshot any pre-existing Week tab) ----
    snap_ranges = [f"'{n}'!A1:L50" for n in tt.WK_DAY_ORDER]
    if existing is not None:
        snap_ranges.append(f"'{tt.TAB_WEEK}'!A1:O60")
    snap = tt.snapshot_ranges(client, "build-week-tab", snap_ranges)
    report["snapshot"] = snap

    # ---- create Week tab leftmost (index 0) ----
    if existing is None:
        resp = client.batch_update([{"addSheet": {"properties": {
            "title": tt.TAB_WEEK,
            "index": 0,
            "gridProperties": {"rowCount": tt.WK_GRID_ROWS,
                               "columnCount": tt.WK_GRID_COLS,
                               "frozenRowCount": 1},
        }}}])
        wk_sid = resp["replies"][0]["addSheet"]["properties"]["sheetId"]
    else:
        wk_sid = existing["sheetId"]
        # Force leftmost.
        client.batch_update([{"updateSheetProperties": {
            "properties": {"sheetId": wk_sid, "index": 0},
            "fields": "index"}}])
    report["week_sheet_id"] = wk_sid

    # ---- structure / formatting ----
    client.batch_update(structure_requests(wk_sid, wd))

    # ---- wire formulas from the 7 day tabs ----
    meta = client.get_metadata()
    formula_writes = tt._build_week_formulas(meta)
    for rng, vals in formula_writes:
        client.values_update(rng, vals)
    report["formula_ranges"] = len(formula_writes)

    report["donut_note"] = ("Per-day donut intentionally skipped on the Week "
                            "tab — it is a planning canvas; the 7 day tabs "
                            "retain their existing donut charts.")
    report["status"] = "OK"
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
