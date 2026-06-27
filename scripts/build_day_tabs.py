#!/usr/bin/env python3
"""One-shot builder — create/repair the 7 permanent day tabs (Sun..Sat,
leftmost in the strip) for Kay's task tracker (2026-05-17 day-tab rebuild).

Reuses the gog-refresh-token auth path + exponential-backoff API client +
sage palette.

Per day tab (structurally identical, only the title row differs):

  Row 1     merged A1:E1 title "SUNDAY · May 17" — 20pt bold, sage-dark fill
  Row 4     "HABITS" header
  Rows 5-13 9 habit rows: A=native checkbox, B:E merged label, 14pt
  Row 15    column headers ✓ | Task | Type | Project | Notes — 12pt bold
  Rows 17-41 25 priority slots: A=native checkbox, B=Task 17pt,
            C=Type dropdown, D=Project dropdown, E=Notes; row height ~34px
  Row 42    "NOTES" header
  Rows 43-50 free-notes block, A:E merged per row

Idempotent: re-running repairs layout/formatting without destroying slot
content (only formatting + structural cells are (re)written; existing
slot/habit/notes user values are NOT cleared — that is build-week's job).

Modes:
  (default)        build/repair all 7 day tabs
  --dry-run        report what would be created/changed; NO writes
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_DIR = REPO_ROOT / "brain" / "context" / "rollback-snapshots"
GOG_CREDS_PATH = Path.home() / ".config" / "gogcli" / "credentials.json"
GOG_ACCOUNT = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")
def _resolve_tracker_sheet_id() -> str:
    """Env override > resolver > migration fallback. Mirrors task_tracker.py pattern."""
    env_id = os.environ.get("TRACKER_SHEET_ID")
    if env_id:
        return env_id
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from tracker_sheet_resolver import resolve_current_sheet_id
        return resolve_current_sheet_id()
    except Exception as e:
        print(f"build_day_tabs: resolver fallback failed ({e}); using migration default", file=sys.stderr)
        return "1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk"

TRACKER_SHEET_ID = _resolve_tracker_sheet_id()

# ---- layout (mirrors task_tracker.py DAY_* constants — kept in sync) --------
DAY_TAB_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
DAY_FULL = {"Sun": "SUNDAY", "Mon": "MONDAY", "Tue": "TUESDAY", "Wed": "WEDNESDAY",
            "Thu": "THURSDAY", "Fri": "FRIDAY", "Sat": "SATURDAY"}
DAY_TITLE_ROW = 1
DAY_HABITS_HEADER_ROW = 4
DAY_HABIT_FIRST_ROW = 5
DAY_HABIT_LAST_ROW = 14
DAY_COL_HEADER_ROW = 16
DAY_SLOT_FIRST_ROW = 17
DAY_SLOT_LAST_ROW = 66
DAY_NOTES_HEADER_ROW = 67
DAY_NOTES_FIRST_ROW = 68
DAY_NOTES_LAST_ROW = 75
DAY_GRID_ROWS = 78
DAY_GRID_COLS = 12
TOP_PRIORITY_SLOT_COUNT = 3

HABITS_DEFAULT = [
    "Sleep 8h",
    "Water + hygiene",
    "Headspace",
    "Mobility sequence",
    "Journal",
    "14h fast: 7:30p-9:30a",
    "ACV turmeric tonic",
    "Protein/probiotic shake",
    "Coffee cutoff 11a",
    "Lunch yogurt parfait",
]
HABITS_SUPPLEMENTAL_DEFAULT = [
    "Matcha cutoff 2p",
    "10K steps",
    "Exercise",
    "Multivitamin",
    "Omega-3",
    "Curcumin",
    "Urolithin A",
    "Magnesium",
    "Eating cutoff 7:30p",
    "Screen cutoff 9:30p",
]
HABITS_SUPPLEMENTAL_SECONDARY_DEFAULT = [
    "Sauna",
    "Glutamine",
    "Ketones",
    "Red light",
]
HABIT_GOAL_TEXT = "Protein 120g + Fiber 25g"
TYPE_OPTIONS = ["Work", "Home"]
PROJECT_OPTIONS = ["G&B", "Kai Grey", "Panthera Grey", "Myself Renewed", "Home"]

# Sage palette (mirrors task_tracker.py / project_personal_task_tracker.md)
SAGE_LIGHT = {"red": 0xE8 / 255, "green": 0xEF / 255, "blue": 0xD8 / 255}
SAGE_DARK = {"red": 0x7A / 255, "green": 0x8C / 255, "blue": 0x4D / 255}
SAGE_EXTRA_LIGHT = {"red": 0xF3 / 255, "green": 0xF7 / 255, "blue": 0xE8 / 255}
INK = {"red": 0x2E / 255, "green": 0x3D / 255, "blue": 0x2A / 255}
MUTED = {"red": 0x9A / 255, "green": 0x9A / 255, "blue": 0x8A / 255}
WHITE = {"red": 1, "green": 1, "blue": 1}


# --------------------------------------------------------------- auth

def get_access_token() -> str:
    if not GOG_CREDS_PATH.exists():
        sys.exit(f"gog credentials not found at {GOG_CREDS_PATH}")
    creds = json.loads(GOG_CREDS_PATH.read_text())
    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        export = subprocess.run(
            ["gog", "auth", "tokens", "export", GOG_ACCOUNT,
             "--out", str(tmp_path), "--overwrite"],
            capture_output=True, text=True, timeout=15,
        )
        if export.returncode != 0:
            sys.exit(f"gog token export failed: {export.stderr[:200]}")
        refresh = json.loads(tmp_path.read_text()).get("refresh_token")
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass
    if not refresh:
        sys.exit("no refresh_token from gog export")
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={"client_id": creds["client_id"], "client_secret": creds["client_secret"],
              "refresh_token": refresh, "grant_type": "refresh_token"},
        timeout=15,
    )
    if resp.status_code != 200:
        sys.exit(f"token refresh failed: {resp.status_code}")
    return resp.json()["access_token"]


# --------------------------------------------------------------- API client

class API:
    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.headers.update({"Authorization": f"Bearer {token}"})

    def _retry(self, fn, *, label: str):
        last = None
        for attempt in range(5):
            try:
                r = fn()
            except requests.RequestException as e:
                last = e
                time.sleep(2 ** attempt)
                continue
            if r.status_code == 200:
                return r.json()
            if r.status_code in (429,) or r.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            sys.exit(f"{label}: API error {r.status_code}: {r.text[:400]}")
        if last:
            sys.exit(f"{label}: API retries exhausted ({last})")
        sys.exit(f"{label}: API retries exhausted")

    def get_metadata(self, fields: str | None = None) -> dict:
        params = {"fields": fields} if fields else {}
        return self._retry(lambda: self.s.get(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}",
            params=params, timeout=60), label="get_metadata")

    def get_values(self, range_a1: str) -> list[list]:
        data = self._retry(lambda: self.s.get(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
            params={"valueRenderOption": "FORMULA"}, timeout=30), label="get_values")
        return data.get("values", [])

    def values_update(self, range_a1: str, values: list[list]) -> dict:
        return self._retry(lambda: self.s.put(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": values}, timeout=30), label="values_update")

    def batch_update(self, reqs: list[dict]) -> dict:
        if not reqs:
            return {}
        return self._retry(lambda: self.s.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}:batchUpdate",
            json={"requests": reqs}, timeout=90), label="batch_update")


# --------------------------------------------------------------- helpers

def find_sheet(meta: dict, title: str) -> dict | None:
    for s in meta.get("sheets", []):
        if s["properties"]["title"] == title:
            return s["properties"]
    return None


def week_dates(today: date) -> list[date]:
    """Sun..Sat dates for the Sunday-boundary week containing `today`."""
    sunday = today - timedelta(days=(today.weekday() + 1) % 7)
    return [sunday + timedelta(days=i) for i in range(7)]


def day_title_text(day_name: str, d: date) -> str:
    return f"{DAY_FULL[day_name]} · {d.strftime('%b')} {d.day}"


def _txt(value: str, *, bold=False, size=11, fg=INK, bg=None,
         italic=False, halign="LEFT"):
    fmt = {"horizontalAlignment": halign, "verticalAlignment": "MIDDLE",
           "textFormat": {"bold": bold, "italic": italic, "fontSize": size,
                          "foregroundColor": fg}}
    if bg is not None:
        fmt["backgroundColor"] = bg
    return {"userEnteredValue": {"stringValue": value}, "userEnteredFormat": fmt}


# --------------------------------------------------------------- layout build

def day_tab_structure_requests(sid: int, day_name: str, d: date) -> list[dict]:
    """All structural/formatting requests for ONE day tab. Does NOT write user
    slot/habit/notes content — only the title, headers, habit labels,
    checkboxes, dropdowns, merges, column widths, row heights, CF."""
    R: list[dict] = []
    V: list[dict] = []

    R.append({"updateSheetProperties": {
        "properties": {"sheetId": sid, "gridProperties": {"rowCount": DAY_GRID_ROWS, "columnCount": DAY_GRID_COLS}},
        "fields": "gridProperties.rowCount,gridProperties.columnCount"}})
    # Clear stale note-block merges from the old 25-slot layout before applying
    # the expanded 50-slot frame. Values are left intact by this structural pass.
    R.append({"unmergeCells": {
        "range": {"sheetId": sid, "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_NOTES_LAST_ROW, "startColumnIndex": 0,
                  "endColumnIndex": 6}}})

    # ---- Title row 1: merge A1:F1, 20pt bold, sage-dark fill ----
    R.append({"mergeCells": {
        "range": {"sheetId": sid, "startRowIndex": 0, "endRowIndex": 1,
                  "startColumnIndex": 0, "endColumnIndex": 6},
        "mergeType": "MERGE_ALL"}})
    V.append({"updateCells": {
        "rows": [{"values": [_txt(day_title_text(day_name, d), bold=True, size=20,
                                  fg=WHITE, bg=SAGE_DARK)]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": 0, "columnIndex": 0}}})

    # ---- Row 2: daily focus/theme label ----
    V.append({"updateCells": {
        "rows": [{"values": [_txt("DAILY FOCUS / THEME", bold=True, size=10, fg=SAGE_DARK)]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": 1, "columnIndex": 0}}})

    # ---- HABITS header row 4 ----
    V.append({"updateCells": {
        "rows": [{"values": [
            _txt("HABITS", bold=True, size=12, fg=SAGE_DARK), {}, {}, {},
            _txt("SUPPLEMENTAL", bold=True, size=12, fg=SAGE_DARK),
        ]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": DAY_HABITS_HEADER_ROW - 1,
                  "columnIndex": 0}}})

    # ---- Habit rows 5..14: A/B primary, C/D supplemental, E/F secondary supplemental/goal ----
    for c0, end_row in ((0, DAY_HABIT_LAST_ROW), (2, DAY_HABIT_LAST_ROW), (4, DAY_HABIT_FIRST_ROW + 4)):
        R.append({"setDataValidation": {
            "range": {"sheetId": sid, "startRowIndex": DAY_HABIT_FIRST_ROW - 1,
                      "endRowIndex": end_row, "startColumnIndex": c0,
                      "endColumnIndex": c0 + 1},
            "rule": {"condition": {"type": "BOOLEAN"}, "strict": True}}})
    for i, label in enumerate(HABITS_DEFAULT):
        r0 = DAY_HABIT_FIRST_ROW - 1 + i
        row_values = [
            {"userEnteredValue": {"boolValue": False}},
            _txt(label, size=14),
            {"userEnteredValue": {"boolValue": False}},
            _txt(HABITS_SUPPLEMENTAL_DEFAULT[i], size=14),
        ]
        if i < len(HABITS_SUPPLEMENTAL_SECONDARY_DEFAULT):
            row_values += [
                {"userEnteredValue": {"boolValue": False}},
                _txt(HABITS_SUPPLEMENTAL_SECONDARY_DEFAULT[i], size=14),
            ]
        elif label.startswith("14h fast"):
            row_values += [_txt("GOAL", bold=True, size=10, fg=SAGE_DARK), {}]
        elif label.startswith("ACV turmeric"):
            row_values += [{}, _txt(HABIT_GOAL_TEXT, size=14)]
        V.append({"updateCells": {
            "rows": [{"values": row_values}],
            "fields": "userEnteredValue,userEnteredFormat",
            "start": {"sheetId": sid, "rowIndex": r0, "columnIndex": 0}}})

    # ---- Column headers row 16 ----
    headers = ["✓", "Task", "Type", "Project", "Notes"]
    V.append({"updateCells": {
        "rows": [{"values": [_txt(h, bold=True, size=12, fg=WHITE, bg=SAGE_DARK,
                                  halign=("CENTER" if h == "✓" else "LEFT"))
                             for h in headers]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": DAY_COL_HEADER_ROW - 1,
                  "columnIndex": 0}}})

    # ---- Priority slots 16..40 ----
    # A: native checkbox
    R.append({"setDataValidation": {
        "range": {"sheetId": sid, "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_SLOT_LAST_ROW, "startColumnIndex": 0,
                  "endColumnIndex": 1},
        "rule": {"condition": {"type": "BOOLEAN"}, "strict": True}}})
    # B: Task — 17pt (apply cell format across the column block)
    R.append({"repeatCell": {
        "range": {"sheetId": sid, "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_SLOT_LAST_ROW, "startColumnIndex": 1,
                  "endColumnIndex": 2},
        "cell": {"userEnteredFormat": {
            "verticalAlignment": "MIDDLE",
            "textFormat": {"fontSize": 17, "foregroundColor": INK}}},
        "fields": "userEnteredFormat(verticalAlignment,textFormat)"}})
    # Top 3 priority slots: fixed sage shading across A:E
    R.append({"repeatCell": {
        "range": {"sheetId": sid, "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_SLOT_FIRST_ROW - 1 + TOP_PRIORITY_SLOT_COUNT,
                  "startColumnIndex": 0, "endColumnIndex": 5},
        "cell": {"userEnteredFormat": {"backgroundColor": SAGE_LIGHT}},
        "fields": "userEnteredFormat.backgroundColor"}})

    # C: Type dropdown
    R.append({"setDataValidation": {
        "range": {"sheetId": sid, "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_SLOT_LAST_ROW, "startColumnIndex": 2,
                  "endColumnIndex": 3},
        "rule": {"condition": {"type": "ONE_OF_LIST",
                               "values": [{"userEnteredValue": o} for o in TYPE_OPTIONS]},
                 "showCustomUi": True, "strict": False}}})
    # D: Project dropdown
    R.append({"setDataValidation": {
        "range": {"sheetId": sid, "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_SLOT_LAST_ROW, "startColumnIndex": 3,
                  "endColumnIndex": 4},
        "rule": {"condition": {"type": "ONE_OF_LIST",
                               "values": [{"userEnteredValue": o} for o in PROJECT_OPTIONS]},
                 "showCustomUi": True, "strict": False}}})
    # Slot row heights ~34px
    R.append({"updateDimensionProperties": {
        "range": {"sheetId": sid, "dimension": "ROWS",
                  "startIndex": DAY_SLOT_FIRST_ROW - 1, "endIndex": DAY_SLOT_LAST_ROW},
        "properties": {"pixelSize": 34}, "fields": "pixelSize"}})

    # ---- NOTES header row 43 + free-notes block 44..51 merged A:F per row ----
    V.append({"updateCells": {
        "rows": [{"values": [_txt("NOTES", bold=True, size=12, fg=SAGE_DARK)]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": sid, "rowIndex": DAY_NOTES_HEADER_ROW - 1,
                  "columnIndex": 0}}})
    for r0 in range(DAY_NOTES_FIRST_ROW - 1, DAY_NOTES_LAST_ROW):
        R.append({"mergeCells": {
            "range": {"sheetId": sid, "startRowIndex": r0, "endRowIndex": r0 + 1,
                      "startColumnIndex": 0, "endColumnIndex": 6},
            "mergeType": "MERGE_ALL"}})

    # ---- Column widths ----
    for c, w in {0: 44, 1: 270, 2: 44, 3: 190, 4: 44, 5: 200}.items():
        R.append({"updateDimensionProperties": {
            "range": {"sheetId": sid, "dimension": "COLUMNS",
                      "startIndex": c, "endIndex": c + 1},
            "properties": {"pixelSize": w}, "fields": "pixelSize"}})

    # ---- Conditional formatting ----
    # Slot rule: =$A16=TRUE → strikethrough + sage-extra-light over A16:E40
    R.append({"addConditionalFormatRule": {
        "rule": {
            "ranges": [{"sheetId": sid,
                        "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                        "endRowIndex": DAY_SLOT_LAST_ROW,
                        "startColumnIndex": 0, "endColumnIndex": 5}],
            "booleanRule": {
                "condition": {"type": "CUSTOM_FORMULA",
                              "values": [{"userEnteredValue": f"=$A{DAY_SLOT_FIRST_ROW}=TRUE"}]},
                "format": {"backgroundColor": SAGE_EXTRA_LIGHT,
                           "textFormat": {"strikethrough": True, "foregroundColor": MUTED}}}},
        "index": 0}})
    # Habit rules: each checkbox shades only its own checkbox+label pair.
    for col_letter, start_col, end_col in (("A", 0, 2), ("C", 2, 4), ("E", 4, 6)):
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": sid,
                            "startRowIndex": DAY_HABIT_FIRST_ROW - 1,
                            "endRowIndex": DAY_HABIT_LAST_ROW,
                            "startColumnIndex": start_col, "endColumnIndex": end_col}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": f"=${col_letter}{DAY_HABIT_FIRST_ROW}=TRUE"}]},
                    "format": {"backgroundColor": SAGE_EXTRA_LIGHT}}},
            "index": 0}})

    return R + V


# --------------------------------------------------------------- main

def main():
    global TRACKER_SHEET_ID
    ap = argparse.ArgumentParser(prog="build_day_tabs")
    ap.add_argument("--dry-run", action="store_true",
                    help="report what would be created/changed; NO writes")
    ap.add_argument("--sheet-id", default=None,
                    help="target spreadsheet ID (default: resolver → current week's TO DO file)")
    args = ap.parse_args()

    if args.sheet_id:
        TRACKER_SHEET_ID = args.sheet_id

    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")

    token = get_access_token()
    api = API(token)
    meta = api.get_metadata(
        fields="sheets(properties(sheetId,title,index,hidden,gridProperties))")
    sheets = meta.get("sheets", [])
    n_sheets = len(sheets)

    wd = week_dates(date.today())
    titles = {DAY_TAB_NAMES[i]: day_title_text(DAY_TAB_NAMES[i], wd[i]) for i in range(7)}

    present = {n: find_sheet(meta, n) for n in DAY_TAB_NAMES}
    missing = [n for n in DAY_TAB_NAMES if present[n] is None]

    report = {
        "timestamp_utc": ts,
        "mode": "dry-run" if args.dry_run else "build",
        "week_sun_to_sat": [d.isoformat() for d in wd],
        "day_tabs_present": [n for n in DAY_TAB_NAMES if present[n] is not None],
        "day_tabs_missing": missing,
        "titles": titles,
    }

    if args.dry_run:
        report["would"] = []
        for n in DAY_TAB_NAMES:
            if present[n] is None:
                report["would"].append(f"CREATE day tab {n!r} (leftmost) + full layout")
            else:
                report["would"].append(f"REPAIR layout/formatting on existing {n!r}")
        report["would"].append("snapshot pre-state to brain/context/rollback-snapshots/")
        print(json.dumps(report, indent=2))
        return

    # ---- snapshot pre-state ----
    snap = {"timestamp_utc": ts, "tracker_sheet_id": TRACKER_SHEET_ID,
            "present_day_tabs": {}}
    for n in DAY_TAB_NAMES:
        if present[n] is not None:
            try:
                snap["present_day_tabs"][n] = api.get_values(f"'{n}'!A1:E{DAY_GRID_ROWS}")
            except SystemExit:
                snap["present_day_tabs"][n] = "_snapshot_error_"
    snap_path = SNAPSHOT_DIR / f"tasks-build-day-tabs-{ts}.json"
    snap_path.write_text(json.dumps(snap, indent=2, default=str))
    report["snapshot_path"] = str(snap_path)

    # ---- create missing day tabs (leftmost, Sun..Sat order) ----
    add_reqs = []
    for idx, n in enumerate(DAY_TAB_NAMES):
        if present[n] is None:
            add_reqs.append({"addSheet": {"properties": {
                "title": n,
                "index": idx,  # Sun..Sat leftmost; idx preserves order
                "gridProperties": {"rowCount": DAY_GRID_ROWS,
                                   "columnCount": DAY_GRID_COLS,
                                   "frozenRowCount": 1},
            }}})
    if add_reqs:
        resp = api.batch_update(add_reqs)
        for rep in resp.get("replies", []):
            if "addSheet" in rep:
                pr = rep["addSheet"]["properties"]
                present[pr["title"]] = pr
        # Re-fetch metadata so indices are accurate before reorder.
        meta = api.get_metadata(
            fields="sheets(properties(sheetId,title,index))")
    # Force the 7 day tabs to the leftmost positions in Sun..Sat order.
    reorder = []
    for idx, n in enumerate(DAY_TAB_NAMES):
        sid = find_sheet(meta, n)["sheetId"] if find_sheet(meta, n) else present[n]["sheetId"]
        reorder.append({"updateSheetProperties": {
            "properties": {"sheetId": sid, "index": idx},
            "fields": "index"}})
    api.batch_update(reorder)

    # ---- per-tab structure/formatting ----
    for i, n in enumerate(DAY_TAB_NAMES):
        sid = find_sheet(api.get_metadata(
            fields="sheets(properties(sheetId,title))"), n)["sheetId"]
        api.batch_update(day_tab_structure_requests(sid, n, wd[i]))

    report["status"] = "OK"
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
