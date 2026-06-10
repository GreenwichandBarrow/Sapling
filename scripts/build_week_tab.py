#!/usr/bin/env python3
"""One-shot builder — create the permanent `Week` planning tab (LEFTMOST,
index 0, before `Sun`) for Kay's task tracker (2026-05-17 design correction).

The tracker has BOTH surfaces:
  * `Week`     — Sunday planning canvas, all 7 days visible, Sun→Sat. Where
                 build-week rebuilds/clears + stamps Recurring and Kay lays
                 out the full week.
  * 7 day tabs — Sun..Sat daily execution surface, fed by `distribute-week`.

Structure is modelled on the verbatim `archive_May 11-17` grid copy but
RE-ORDERED Sun→Sat (the archive grid was Mon-first):

  Row 1      merged A1:O1 title "WEEK OF May 17-23" — 16pt bold, sage-light fill
  Row 5      "HABIT TRACKER" — 10pt bold
  Row 6      Sun..Sat 2-col-merged sub-headers (9pt bold)
  Rows 7-13  7 habit rows: col0 label, status checkbox per day at odd col
  Row 15     SUNDAY..SATURDAY 2-col-merged headers (11pt bold, white/sage-dark)
  Rows 24-48 25 priority slots/day: status checkbox col + task col per day
  Row 50     notes sub-headers (2-col-merged)
  Rows 51-58 merged free-notes block per day

Native checkboxes (Data Validation BOOLEAN). Sage palette. Per-day donut is
intentionally SKIPPED for now (the per-day donuts already live on the 7 day
tabs; the Week tab is a planning canvas, kept simple — flagged in the report).

Modes:
  (default)        create Week tab + structure + reverse-populate from day tabs
  --dry-run        report what would be created; NO writes
  --no-populate    create + format only; skip the reverse-populate pass
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

    # ---- Row 5: HABIT TRACKER header ----
    R.append({"updateCells": {
        "rows": [{"values": [_txt("HABIT TRACKER", bold=True, size=10, fg=SAGE_DARK)]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": tt.WK_HABITS_HEADER_ROW - 1,
                  "columnIndex": 0}}})

    # ---- Row 6: Sun..Sat habit sub-headers (2-col merged) ----
    for i in DI:
        c0 = tt.wk_status_col(i)
        R.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_HABIT_DAYHDR_ROW - 1,
                      "endRowIndex": tt.WK_HABIT_DAYHDR_ROW,
                      "startColumnIndex": c0, "endColumnIndex": c0 + 2},
            "mergeType": "MERGE_ALL"}})
        R.append({"updateCells": {
            "rows": [{"values": [_txt(tt.WK_DAY_ORDER[i], bold=True, size=9,
                                      fg=SAGE_DARK, halign="CENTER")]}],
            "fields": "userEnteredValue,userEnteredFormat",
            "start": {"sheetId": sid, "rowIndex": tt.WK_HABIT_DAYHDR_ROW - 1,
                      "columnIndex": c0}}})

    # ---- Rows 7-13: 7 habit rows. col0 label, status checkbox per day ----
    for hi, label in enumerate(tt.HABITS_DEFAULT):
        r0 = tt.WK_HABIT_FIRST_ROW - 1 + hi
        R.append({"updateCells": {
            "rows": [{"values": [_txt(label, size=10, fg=INK)]}],
            "fields": "userEnteredValue,userEnteredFormat",
            "start": {"sheetId": sid, "rowIndex": r0, "columnIndex": 0}}})
    for i in DI:
        sc = tt.wk_status_col(i)
        R.append({"setDataValidation": {
            "range": {"sheetId": sid, "startRowIndex": tt.WK_HABIT_FIRST_ROW - 1,
                      "endRowIndex": tt.WK_HABIT_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": sc + 1},
            "rule": {"condition": {"type": "BOOLEAN"}, "strict": True}}})

    # ---- Row 15: SUNDAY..SATURDAY headers (2-col merged, white/sage-dark) ----
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

    # ---- Rows 24-48: 25 priority slots/day ----
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
    (rows 16-40, A=status B=task) + habits (rows 5-13, A=status) and writes
    into the matching Week-grid day block. Returns a summary dict."""
    summary = {"slots_written": 0, "habits_written": 0, "per_day": {}}
    for i, day_name in enumerate(tt.WK_DAY_ORDER):
        block = client.get_values(f"'{day_name}'!A1:E37")
        sc = tt.wk_status_col(i)
        tc = tt.wk_content_col(i)
        col = tt.col_letter
        # Slots: day-tab rows 13..27 → Week rows 23..37
        st_vals, tk_vals = [], []
        for r in range(tt.DAY_SLOT_FIRST_ROW - 1, tt.DAY_SLOT_LAST_ROW):
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
        # Habits: day-tab rows 4..10 col A → Week rows 7..13 status col
        hb_vals = []
        for r in range(tt.DAY_HABIT_FIRST_ROW - 1, tt.DAY_HABIT_LAST_ROW):
            row = block[r] if r < len(block) else []
            hb_vals.append([bool(row[0]) if len(row) > 0 and row[0] not in ("", None) else False])
        client.values_update(
            f"'{tt.TAB_WEEK}'!{col(sc)}{tt.WK_HABIT_FIRST_ROW}:{col(sc)}{tt.WK_HABIT_LAST_ROW}",
            hb_vals)
        summary["slots_written"] += nslots
        summary["habits_written"] += sum(1 for h in hb_vals if h[0])
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
            "APPLY archive-grid structure re-ordered Sun→Sat (title, habit "
            "tracker, day headers, 25 slots/day, notes block, native "
            "checkboxes, sage palette, done-row CF)",
            "SKIP per-day donut (Week tab is a planning canvas; day tabs keep "
            "their donuts) — design simplification, flagged",
        ]
        if not args.no_populate:
            report["would"].append(
                "REVERSE-POPULATE Week grid from the 7 day tabs' current slots "
                "+ habits (rows 16-40 / 5-13)")
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

    # ---- reverse-populate from the 7 day tabs ----
    if not args.no_populate:
        report["populate"] = populate_from_day_tabs(client, wd)

    report["donut_note"] = ("Per-day donut intentionally skipped on the Week "
                            "tab — it is a planning canvas; the 7 day tabs "
                            "retain their existing donut charts.")
    report["status"] = "OK"
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
