"""task-tracker-manager skill helper — verbs for Kay's personal task tracker.

Migrated 2026-05-12 from openpyxl/xlsx to Google Sheets API. Same CLI surface.

Subcommands:
    append                  Add a row to the To Do tab.
    promote                 Move a To Do row into a specific day TAB's priority slot.
    schedule-to-day-slot    Direct write to a day TAB slot (no To Do source row required).
    sync-done-status        Reconcile checked day-tab slots → matching To Do rows (text-match).
    build-week              Sunday rebuild ceremony (day-tab model) — combined archive
                            tab + clear/re-title 7 day tabs + stamp Recurring Template
                            (--skip-recurring to bypass; --dry-run to preview).
    archive                 DEPRECATED 2026-05-17 — alias of build-week.
    move-day-item           Move/copy a slot item between day tabs (manual carryover:
                            completed | incomplete | added | deleted).
    migrate                 2026-05-17 one-shot cutover (dry-run by default; never runs
                            the destructive teardown itself).
    archive-todo            Sweep checked rows from To Do tab into a running
                            "Completed To Do" tab (created on first run). Auto-runs
                            sync-done-status first (skip with --skip-sync).
    recurring-add           Append a row to the Recurring Template tab — stamped onto
                            every future Sunday rollover.
    recurring-remove        Clear a row from the Recurring Template tab.
    projects-create-gantt   Create a new Gantt project tab cloning the
                            Myself Renewed Healthcare structure; updates Projects index.
    reformat                Re-apply conditional formatting + dropdowns + checkboxes.
    report                  Markdown health summary (overdue, empty slots, carryover).
    gantt-tick              Fill a week-cell on a Gantt project tab.

Auth: gog refresh token from ~/.config/gogcli/credentials.json. API quota
retried with exponential backoff. Affected ranges snapshotted to
brain/context/rollback-snapshots/tasks-{verb}-{timestamp}.json before each write.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

# --------------------------------------------------------------- file paths

_SCRIPT_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SCRIPT_DIR.parent
SNAPSHOT_DIR = _REPO_ROOT / "brain" / "context" / "rollback-snapshots"
SNAPSHOT_KEEP = 5

GOG_CREDS_PATH = Path.home() / ".config" / "gogcli" / "credentials.json"
GOG_ACCOUNT = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")

# Sheet ID — read from env override, fallback to migration default.
TRACKER_SHEET_ID = os.environ.get(
    "TRACKER_SHEET_ID",
    "1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk",
)
TRACKER_SHEET_URL = f"https://docs.google.com/spreadsheets/d/{TRACKER_SHEET_ID}/edit"

# --------------------------------------------------------------- palette (hex)

SAGE_LIGHT_HEX = "e8efd8"
SAGE_DARK_HEX = "7a8c4d"
SAGE_EXTRA_LIGHT_HEX = "f3f7e8"
INK_HEX = "2e3d2a"
MUTED_HEX = "9a9a8a"
TYPE_HOME_HEX = "f4e8d8"
TYPE_WORK_HEX = SAGE_EXTRA_LIGHT_HEX

ENTITY_COLOR_HEX = {
    "G&B": "7a8c4d",
    "Kai Grey": "9b8e7c",
    "Panthera Grey": "7a7e89",
    "Myself Renewed": "f4ddd9",
    "Home": "d8c7a8",
}

# --------------------------------------------------------------- layout constants

# Tab names
TAB_TODO = "To Do"
TAB_TODO_LONG_TERM = "To Do Long Term"
TAB_PROJECTS = "Projects"
TAB_COMPLETED_TODO = "Completed To Do"
TAB_RECURRING_TEMPLATE = "Recurring Weekly To Dos"

# Recurring Template column layout (0-based)
RT_COL_DAY = 0
RT_COL_SLOT = 1
RT_COL_TASK = 2
RT_COL_TYPE = 3
RT_COL_PROJECT = 4
RT_COL_NOTES = 5
RT_HEADERS = ["Day", "Slot", "Task", "Type", "Project", "Notes"]
RT_MAX_ROWS = 60

# To Do columns (0-based) — header NAMES live in TODO_HEADERS. These constants are
# for code only, never appear in Kay-facing output.
TODO_COL_STATUS = 0
TODO_COL_TASK = 1
TODO_COL_TYPE = 2
TODO_COL_PROJECT = 3
TODO_COL_DUE = 4
TODO_COL_NOTES = 5
TODO_COL_HORIZON = 6
TODO_HEADERS = ["Status", "Task", "Type", "Project", "Due", "Notes", "Horizon"]
TODO_MAX_ROWS = 400

# 2026-05-17 consolidation: Status is a 3-state dropdown (was native checkbox);
# Horizon classifies the item + (for recurring) carries the target day.
# To Do Long Term + Recurring Weekly To Dos + Completed To Do tabs are retired —
# everything lives in the single `To Do` tab, filtered by Horizon.
STATUS_OPTIONS = ["Not Completed", "On-going", "Completed"]
HORIZON_OPTIONS = [
    "Short Term", "Long Term",
    "Weekly Recurring Mon", "Weekly Recurring Tue", "Weekly Recurring Wed",
    "Weekly Recurring Thu", "Weekly Recurring Fri", "Weekly Recurring Sat",
]
RECURRING_HORIZON_PREFIX = "Weekly Recurring"  # extensible: Quarterly/Yearly later

# To Do Long Term columns (0-based)
LT_COL_STATUS = 0
LT_COL_TASK = 1
LT_COL_TYPE = 2
LT_COL_PROJECT = 3
LT_COL_DUE = 4
LT_COL_NOTES = 5
LT_HEADERS = ["Status", "Item", "Type", "Project", "Due", "Notes"]
LT_STATUS_OPTIONS = ["Idea", "Active", "On hold", "Promoted", "Done"]
LT_MAX_ROWS = 200

# Projects columns (0-based)
PJ_COL_PROJECT = 0
PJ_COL_ENTITY = 1
PJ_COL_STATUS = 2
PJ_COL_START = 3
PJ_COL_TARGET = 4
PJ_COL_TAB = 5
PJ_COL_NOTES = 6
PJ_HEADERS = ["Project", "Entity", "Status", "Start", "Target", "Tab", "Notes"]
PJ_STATUS_OPTIONS = ["Plan Needed", "Active", "On hold", "Done"]
PJ_MAX_ROWS = 50

# Dropdown values
TYPE_OPTIONS = ["Work", "Home"]
PROJECT_OPTIONS = ["G&B", "Kai Grey", "Panthera Grey", "Myself Renewed", "Home"]

# --- DEPRECATED 2026-05-17: single "Live Week" 7-day-pair grid ---------------
# The single Live Week tab (7 day-blocks in one tab) is retired in favor of 7
# permanent single-column day tabs (Sun..Sat). These constants + the
# `find_live_week_tab()` / `current_week_label()` helpers below are kept ONLY for
# the one-shot migration's pre-teardown `sync-done-status` read against the OLD
# `May 11-17` grid (migrate path). No verb in the new model uses them. Remove
# after the 2026-05-17 cutover is confirmed.
LIVE_DAY_STAT = {i: 1 + i * 2 for i in range(7)}  # DEPRECATED
LIVE_DAY_TASK = {i: 2 + i * 2 for i in range(7)}  # DEPRECATED
LIVE_HABIT_FIRST_ROW = 7   # DEPRECATED rows 7..13 = 7 habits (old grid)
LIVE_HABIT_LAST_ROW = 13   # DEPRECATED
LIVE_SLOT_FIRST_ROW = 23   # DEPRECATED rows 23..37 = 15 priority slots (old grid)
LIVE_SLOT_LAST_ROW = 37    # DEPRECATED
LIVE_NOTES_FIRST_ROW = 40  # DEPRECATED
LIVE_NOTES_LAST_ROW = 47   # DEPRECATED
LIVE_BIG_PCT_ROW = 17      # DEPRECATED merged 17..21 anchored at row 17

DAY_BY_NAME = {
    "mon": 0, "monday": 0,
    "tue": 1, "tuesday": 1,
    "wed": 2, "wednesday": 2,
    "thu": 3, "thursday": 3,
    "fri": 4, "friday": 4,
    "sat": 5, "saturday": 5,
    "sun": 6, "sunday": 6,
}
DAY_LABELS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
WEEKDAY_NAMES_FULL = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# --- Day-tab model (2026-05-17 rebuild) --------------------------------------
# Seven permanent, writable, large-font day tabs, leftmost in the strip,
# ordered Sun → Sat. Each tab is structurally identical (only the title row
# differs). Kay plans the week Sunday, then lives only in the current day's tab.
DAY_TAB_NAMES = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
# Map a python weekday-anchored day index (Mon=0..Sun=6, as in DAY_BY_NAME) to
# the day-tab name. DAY_BY_NAME maps "sun"→6 etc; DAY_LABELS[idx] gives 3-letter.
DAY_IDX_TO_TAB = {DAY_BY_NAME[k.lower()]: DAY_LABELS[DAY_BY_NAME[k.lower()]]
                  for k in ("mon", "tue", "wed", "thu", "fri", "sat", "sun")}

# Per-day-tab layout (1-based rows for A1 references)
DAY_TITLE_ROW = 1            # merged A1:E1 "SUNDAY · May 17"
DAY_HABITS_HEADER_ROW = 3    # "HABITS"
DAY_HABIT_FIRST_ROW = 4      # rows 4..10 = 7 habit rows
DAY_HABIT_LAST_ROW = 12
DAY_COL_HEADER_ROW = 13      # ✓ | Task | Type | Project | Notes
DAY_SLOT_FIRST_ROW = 14      # rows 13..27 = 15 priority slots
DAY_SLOT_LAST_ROW = 28
DAY_NOTES_HEADER_ROW = 30    # "NOTES"
DAY_NOTES_FIRST_ROW = 31     # rows 30..37 = free-notes block
DAY_NOTES_LAST_ROW = 38
DAY_GRID_ROWS = 41           # generous; chart anchors col G row 1
DAY_GRID_COLS = 12           # A..E content + G chart anchor headroom

# Per-day-tab columns (0-based)
DAY_COL_STATUS = 0   # A — native checkbox
DAY_COL_TASK = 1     # B — Task, 17pt
DAY_COL_TYPE = 2     # C — Type dropdown
DAY_COL_PROJECT = 3  # D — Project dropdown
DAY_COL_NOTES = 4    # E — Notes free text
DAY_COL_LAST = DAY_COL_NOTES
DAY_HEADERS = ["✓", "Task", "Type", "Project", "Notes"]
DAY_SLOT_COUNT = DAY_SLOT_LAST_ROW - DAY_SLOT_FIRST_ROW + 1  # 15
DAY_HABIT_COUNT = DAY_HABIT_LAST_ROW - DAY_HABIT_FIRST_ROW + 1  # 7

TAB_DONUT_DATA = "_donut_data"

# --- Week planning tab (2026-05-17 design correction) ------------------------
# The tracker has BOTH surfaces:
#   * the `Week` planning tab — Sunday canvas, all 7 days visible, Sun→Sat,
#     where `build-week` rebuilds/clears + stamps Recurring, and Kay lays out
#     the full week before fanning out;
#   * the 7 day tabs (Sun..Sat) — daily execution surface, fed by the new
#     `distribute-week` verb.
# The Week tab is a grid (one block per day, side by side) modelled on the
# verbatim `archive_May 11-17` copy but re-ordered Sun→Sat.
TAB_WEEK = "Week"

# Week-tab grid layout (1-based rows for A1 references; mirrors archive grid).
WK_TITLE_ROW = 1               # merged A1:O1 "WEEK OF May 17-23"
WK_HABITS_HEADER_ROW = 5       # "HABIT TRACKER"
WK_HABIT_DAYHDR_ROW = 6        # Sun..Sat 2-col-merged sub-headers
WK_HABIT_FIRST_ROW = 7         # rows 7..13 = 7 habit rows (label col 0)
WK_HABIT_LAST_ROW = 15
WK_DAYHDR_ROW = 16             # SUNDAY..SATURDAY 2-col-merged headers
WK_SLOT_FIRST_ROW = 24         # rows 23..37 = 15 priority slots
WK_SLOT_LAST_ROW = 38
WK_NOTES_HDR_ROW = 40          # notes label row
WK_NOTES_FIRST_ROW = 41        # rows 40..47 = merged notes block per day
WK_NOTES_LAST_ROW = 48
WK_GRID_ROWS = 51
WK_GRID_COLS = 15              # col0 label + 7 day-pairs (status + content)
WK_SLOT_COUNT = WK_SLOT_LAST_ROW - WK_SLOT_FIRST_ROW + 1   # 15
WK_HABIT_COUNT = WK_HABIT_LAST_ROW - WK_HABIT_FIRST_ROW + 1  # 7

# Day order on the Week grid is Sun→Sat (design-corrected; archive grid was
# Mon-first). Column mapping: col 0 = habit/notes label, then for day i
# (0=Sun..6=Sat): status checkbox col = 1 + 2*i, content/task col = 2 + 2*i.
WK_DAY_ORDER = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]


def wk_status_col(day_idx: int) -> int:
    """0-based status (checkbox) column for Week-grid day `day_idx` (0=Sun)."""
    return 1 + 2 * day_idx


def wk_content_col(day_idx: int) -> int:
    """0-based content/task column for Week-grid day `day_idx` (0=Sun)."""
    return 2 + 2 * day_idx


HABITS_DEFAULT = [
    "Water & hygiene",
    "Meditation",
    "Exercises",
    "ACV drink",
    "Probiotic protein shake",
    "Class",
    "Bike to work",
    "10K steps",
    "Omega 3 & magnesium",
]


# --------------------------------------------------------------- auth + API

class SheetsClient:
    def __init__(self):
        self.token = _get_access_token()
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def _retry(self, fn):
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
            # 4xx other than rate-limit: print body for diagnosis
            try:
                err = r.json()
                print(f"task-tracker-manager: API error {r.status_code}: {json.dumps(err)[:400]}", file=sys.stderr)
            except Exception:
                print(f"task-tracker-manager: API error {r.status_code}: {r.text[:400]}", file=sys.stderr)
            r.raise_for_status()
        if last:
            raise last

    def get_metadata(self) -> dict:
        return self._retry(lambda: self.session.get(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}",
            params={"fields": "sheets(properties(sheetId,title,gridProperties,index)),namedRanges"},
            timeout=30,
        ))

    def get_values(self, range_a1: str) -> list[list]:
        data = self._retry(lambda: self.session.get(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
            params={"valueRenderOption": "UNFORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"},
            timeout=30,
        ))
        return data.get("values", [])

    def values_update(self, range_a1: str, values: list[list]) -> dict:
        return self._retry(lambda: self.session.put(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": values},
            timeout=30,
        ))

    def values_append(self, range_a1: str, values: list[list]) -> dict:
        return self._retry(lambda: self.session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}:append",
            params={"valueInputOption": "USER_ENTERED", "insertDataOption": "INSERT_ROWS"},
            json={"values": values},
            timeout=30,
        ))

    def values_clear(self, range_a1: str) -> dict:
        return self._retry(lambda: self.session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}:clear",
            timeout=30,
        ))

    def batch_update(self, requests_list: list[dict]) -> dict:
        if not requests_list:
            return {}
        return self._retry(lambda: self.session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}:batchUpdate",
            json={"requests": requests_list},
            timeout=60,
        ))


def _get_access_token() -> str:
    """Refresh gog's OAuth token to mint a fresh Google API access token."""
    if not GOG_CREDS_PATH.exists():
        sys.exit(f"task-tracker-manager: gog credentials not found at {GOG_CREDS_PATH}")
    creds = json.loads(GOG_CREDS_PATH.read_text())
    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        export = subprocess.run(
            ["gog", "auth", "tokens", "export", GOG_ACCOUNT, "--out", str(tmp_path), "--overwrite"],
            capture_output=True, text=True, timeout=15,
        )
        if export.returncode != 0:
            sys.exit(f"task-tracker-manager: gog token export failed: {export.stderr[:200]}")
        token_file = json.loads(tmp_path.read_text())
        refresh_token = token_file.get("refresh_token")
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass
    if not refresh_token:
        sys.exit("task-tracker-manager: no refresh_token from gog export")
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        },
        timeout=15,
    )
    if resp.status_code != 200:
        sys.exit(f"task-tracker-manager: token refresh failed: {resp.status_code}")
    return resp.json()["access_token"]


# --------------------------------------------------------------- shared utils

def col_letter(idx_0: int) -> str:
    s = ""
    n = idx_0
    while True:
        s = chr(65 + n % 26) + s
        n = n // 26 - 1
        if n < 0:
            break
    return s


def hex_to_rgb(hexstr: str) -> dict:
    h = hexstr.lstrip("#")
    return {
        "red": int(h[0:2], 16) / 255.0,
        "green": int(h[2:4], 16) / 255.0,
        "blue": int(h[4:6], 16) / 255.0,
    }


def current_week_label(today: date | None = None) -> str:
    """DEPRECATED 2026-05-17. Monday-anchored single-week label. Retained only
    for migration teardown bookkeeping / archive-tab naming. New model uses
    `week_dates()` (Sunday boundary) + per-day title rows."""
    if today is None:
        today = date.today()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    if monday.month == sunday.month:
        return f"{monday.strftime('%b')} {monday.day}-{sunday.day}"
    return f"{monday.strftime('%b')} {monday.day}-{sunday.strftime('%b')} {sunday.day}"


def find_live_week_tab(metadata: dict) -> dict | None:
    """DEPRECATED 2026-05-17. Finds the OLD single Live Week tab (month-prefixed
    title). Retained ONLY for the migration's pre-teardown sync against the
    `May 11-17` grid. No new-model verb calls this."""
    months = ("Jan ", "Feb ", "Mar ", "Apr ", "May ", "Jun ", "Jul ", "Aug ",
              "Sep ", "Oct ", "Nov ", "Dec ")
    for s in metadata.get("sheets", []):
        title = s["properties"]["title"]
        if title.startswith("archive_"):
            continue
        if any(title.startswith(m) for m in months):
            return s["properties"]
    return None


# --------------------------------------------------------------- day-tab helpers

def week_dates(today: date | None = None) -> list[date]:
    """Return the 7 dates of the Sunday-boundary week containing `today`,
    ordered Sun..Sat (index 0 = Sunday). Sunday boundary:
    sunday = today - timedelta(days=(today.weekday()+1) % 7)
    (Python weekday(): Mon=0..Sun=6; (wd+1)%7 gives days since Sunday)."""
    if today is None:
        today = date.today()
    sunday = today - timedelta(days=(today.weekday() + 1) % 7)
    return [sunday + timedelta(days=i) for i in range(7)]


def day_title_text(day_name: str, d: date) -> str:
    """Title-row string for a day tab, e.g. 'SUNDAY · May 17'."""
    full = {
        "Sun": "SUNDAY", "Mon": "MONDAY", "Tue": "TUESDAY", "Wed": "WEDNESDAY",
        "Thu": "THURSDAY", "Fri": "FRIDAY", "Sat": "SATURDAY",
    }[day_name]
    return f"{full} · {d.strftime('%b')} {d.day}"


def find_day_tab(metadata: dict, day_name: str) -> dict | None:
    """Return the sheet `properties` dict for the permanent day tab `day_name`
    (one of DAY_TAB_NAMES). None if absent (pre-migration)."""
    return find_tab(metadata, day_name)


def day_tab_range(day_name: str, col0: int, r1: int, r2: int | None = None) -> str:
    """Build an A1 range on a day tab. `col0` 0-based column, `r1`/`r2` 1-based
    rows. If r2 is None, a single-row span. Single column only (the day-tab
    model is single-column-per-field)."""
    cl = col_letter(col0)
    if r2 is None:
        return f"'{day_name}'!{cl}{r1}"
    return f"'{day_name}'!{cl}{r1}:{cl}{r2}"


def day_tab_block(day_name: str, c0: int, c1: int, r1: int, r2: int) -> str:
    """Multi-column A1 range on a day tab (c0..c1 0-based inclusive)."""
    return f"'{day_name}'!{col_letter(c0)}{r1}:{col_letter(c1)}{r2}"


def _iter_day_tabs(metadata: dict):
    """Yield (day_name, props_dict) for every permanent day tab present, in
    Sun..Sat order. Skips any day tab not yet created (pre-migration tolerance)."""
    for day_name in DAY_TAB_NAMES:
        props = find_day_tab(metadata, day_name)
        if props is not None:
            yield day_name, props


def _resolve_day_tab_name(arg_day: str) -> str:
    """Map a --day arg (Mon..Sun, full or 3-letter, any case) to a day-tab name
    in DAY_TAB_NAMES. Exits on unknown."""
    idx = DAY_BY_NAME.get(arg_day.lower())
    if idx is None:
        sys.exit(f"task-tracker-manager: unknown day {arg_day!r}. Use Sun..Sat / Mon..Sun.")
    return DAY_LABELS[idx]  # DAY_LABELS uses 3-letter Mon..Sun; all are in DAY_TAB_NAMES


def find_tab(metadata: dict, name: str) -> dict | None:
    for s in metadata.get("sheets", []):
        if s["properties"]["title"] == name:
            return s["properties"]
    return None


def snapshot_ranges(client: SheetsClient, verb: str, ranges: list[str]) -> str:
    """Snapshot the listed A1 ranges into a JSON file for rollback. Returns the path."""
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    path = SNAPSHOT_DIR / f"tasks-{verb}-{ts}.json"
    snapshot = {"verb": verb, "timestamp": ts, "sheet_id": TRACKER_SHEET_ID, "ranges": {}}
    for r in ranges:
        try:
            snapshot["ranges"][r] = client.get_values(r)
        except Exception as e:
            snapshot["ranges"][r] = {"_error": str(e)}
    path.write_text(json.dumps(snapshot, indent=2, default=str))
    # Prune to last N per verb
    existing = sorted(SNAPSHOT_DIR.glob(f"tasks-{verb}-*.json"))
    for old in existing[:-SNAPSHOT_KEEP]:
        try:
            old.unlink()
        except OSError:
            pass
    return str(path)


def trace(verb: str, slug: str, lines: list[str]) -> None:
    today_iso = date.today().isoformat()
    trace_dir = _REPO_ROOT / "brain" / "traces"
    trace_dir.mkdir(parents=True, exist_ok=True)
    trace_path = trace_dir / f"{today_iso}-task-tracker-{verb}-{slug}.md"
    body = "\n".join([
        "---",
        f"name: task-tracker {verb} — {slug}",
        f"date: {today_iso}",
        f"type: trace",
        f"tags:",
        f"  - date/{today_iso}",
        f"  - trace",
        f"  - skill/task-tracker-manager",
        f"  - verb/{verb}",
        "---",
        f"# task-tracker {verb} — {slug}",
        "",
        *lines,
    ])
    trace_path.write_text(body)


def log_append_receipt(verb: str, lines: list[str]) -> None:
    """For append: write rollback receipt to logs/scheduled/, NOT brain/traces/.
    Per SKILL.md hard guardrail 4 — append receipts are not decisions."""
    today_iso = date.today().isoformat()
    log_dir = _REPO_ROOT / "logs" / "scheduled"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"task-tracker-{today_iso}.log"
    with log_path.open("a") as f:
        ts = datetime.now().isoformat()
        f.write(f"\n[{ts}] {verb}\n")
        for line in lines:
            f.write(f"  {line}\n")


# --------------------------------------------------------------- verbs

def cmd_append(args) -> int:
    if args.type not in TYPE_OPTIONS:
        sys.exit(f"task-tracker-manager: --type must be one of {TYPE_OPTIONS}")
    client = SheetsClient()

    # Find first empty row in To Do tab (after header row 1).
    existing = client.get_values(f"'{TAB_TODO}'!{col_letter(TODO_COL_TASK)}2:{col_letter(TODO_COL_TASK)}{TODO_MAX_ROWS}")
    target_row = 2  # 1-based row to write
    for i, row in enumerate(existing):
        if not row or not (row[0] if row else "").strip():
            target_row = 2 + i
            break
    else:
        # No empty row found within existing data; next row is after the last
        target_row = 2 + len(existing)
    if target_row > TODO_MAX_ROWS:
        sys.exit(f"task-tracker-manager: To Do tab is full (>{TODO_MAX_ROWS}). Time to widen capacity.")

    # Snapshot the target row before writing
    snap = snapshot_ranges(client, "append",
        [f"'{TAB_TODO}'!A{target_row}:G{target_row}"])

    horizon = getattr(args, "horizon", None) or "Short Term"
    if horizon not in HORIZON_OPTIONS:
        sys.exit(f"task-tracker-manager: --horizon must be one of {HORIZON_OPTIONS}")
    row_values = [
        "Not Completed",   # Status (3-state dropdown; was checkbox False)
        args.task,         # Task
        args.type,         # Type
        args.project or "",
        args.due or "",
        args.notes or "",
        horizon,           # Horizon
    ]
    client.values_update(f"'{TAB_TODO}'!A{target_row}:G{target_row}", [row_values])

    log_append_receipt("append", [
        f"task: {args.task}",
        f"type: {args.type}",
        f"project: {args.project or '—'}",
        f"due: {args.due or '—'}",
        f"row: {target_row}",
        f"snapshot: {snap}",
    ])
    print(f'task-tracker-manager: appended row {target_row} ("{args.task}" / {args.type} / {args.project or "—"} / {args.due or "—"})')
    return 0


def cmd_promote(args) -> int:
    """Move a To Do row into a specific day TAB's priority slot (new day-tab model).

    Writes [[False, task]] into A/B of the target day tab's slot row. Refuses to
    overwrite an occupied slot. Leaves the To Do row in place, prepends a
    `→ promoted to {day} slot {N} on {date}` marker to its Notes so it stays
    visible but de-prioritized.
    """
    day_name = _resolve_day_tab_name(args.day)
    if not (1 <= args.slot <= DAY_SLOT_COUNT):
        sys.exit(f"task-tracker-manager: --slot must be 1..{DAY_SLOT_COUNT}")

    client = SheetsClient()
    meta = client.get_metadata()
    if find_day_tab(meta, day_name) is None:
        sys.exit(f"task-tracker-manager: day tab '{day_name}' not found — run build-week first")

    todo_row = args.todo_row
    todo_vals = client.get_values(f"'{TAB_TODO}'!B{todo_row}")
    task_text = todo_vals[0][0] if todo_vals and todo_vals[0] else None
    if not task_text:
        sys.exit(f"task-tracker-manager: To Do row {todo_row} is empty")

    slot_row = DAY_SLOT_FIRST_ROW + args.slot - 1
    task_cell = day_tab_range(day_name, DAY_COL_TASK, slot_row)
    existing_vals = client.get_values(task_cell)
    existing = (existing_vals[0][0] if existing_vals and existing_vals[0] else "")
    if existing:
        sys.exit(f'task-tracker-manager: refused promote — {day_name} slot {args.slot} '
                 f'already contains "{existing}"')

    # Snapshot the source To Do row + destination slot A:E
    dst_block = day_tab_block(day_name, DAY_COL_STATUS, DAY_COL_LAST, slot_row, slot_row)
    snap = snapshot_ranges(client, "promote", [
        f"'{TAB_TODO}'!A{todo_row}:F{todo_row}",
        dst_block,
    ])

    # Carry Type/Project from the To Do row into the day-tab slot.
    todo_full = client.get_values(f"'{TAB_TODO}'!A{todo_row}:F{todo_row}")
    tr = todo_full[0] if todo_full and todo_full[0] else []
    src_type = (tr[TODO_COL_TYPE] if len(tr) > TODO_COL_TYPE else "") or ""
    src_proj = (tr[TODO_COL_PROJECT] if len(tr) > TODO_COL_PROJECT else "") or ""

    # Write destination slot A:E = [unchecked, task, type, project, notes]
    client.values_update(
        dst_block,
        [[False, task_text, src_type, src_proj, ""]],
    )
    # Mark source To Do row Notes (col F) with a moved indicator.
    existing_notes = (tr[TODO_COL_NOTES] if len(tr) > TODO_COL_NOTES else "") or ""
    marker = f"→ promoted to {day_name} slot {args.slot} on {date.today().isoformat()}"
    new_notes = (f"{marker}; {existing_notes}"
                 if existing_notes and marker not in existing_notes
                 else (existing_notes or marker))
    client.values_update(f"'{TAB_TODO}'!F{todo_row}", [[new_notes]])

    trace("promote", f"{day_name.lower()}-{args.slot}", [
        f"- todo_row: {todo_row}",
        f"- task: {task_text}",
        f"- promoted_to: {day_name} tab slot {args.slot} (row {slot_row})",
        f"- snapshot: {snap}",
    ])
    print(f'task-tracker-manager: promoted To Do row {todo_row} → {day_name} slot {args.slot} ("{task_text}")')
    return 0


def cmd_schedule_to_day_slot(args) -> int:
    """Direct write to a day TAB's priority slot (no To Do source). New day-tab
    model. --slot optional (auto-pick first empty). Refuses occupied slots
    unless --force. Writes [False, task, type, project, notes] into A:E."""
    day_name = _resolve_day_tab_name(args.day)

    client = SheetsClient()
    meta = client.get_metadata()
    if find_day_tab(meta, day_name) is None:
        sys.exit(f"task-tracker-manager: day tab '{day_name}' not found — run build-week first")

    if args.slot is not None:
        if not (1 <= args.slot <= DAY_SLOT_COUNT):
            sys.exit(f"task-tracker-manager: --slot must be 1..{DAY_SLOT_COUNT}")
        slot = args.slot
    else:
        col_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
        slot = None
        for i in range(DAY_SLOT_COUNT):
            v = col_vals[i][0] if i < len(col_vals) and col_vals[i] else ""
            if not v:
                slot = i + 1
                break
        if slot is None:
            sys.exit(f"task-tracker-manager: refused schedule-to-day-slot — {day_name} has no empty slots")

    slot_row = DAY_SLOT_FIRST_ROW + slot - 1
    task_cell = day_tab_range(day_name, DAY_COL_TASK, slot_row)
    existing_vals = client.get_values(task_cell)
    existing = (existing_vals[0][0] if existing_vals and existing_vals[0] else "")
    if existing and not args.force:
        sys.exit(f'task-tracker-manager: refused schedule-to-day-slot — {day_name} slot {slot} '
                 f'already contains "{existing}" (use --force to overwrite)')

    dst_block = day_tab_block(day_name, DAY_COL_STATUS, DAY_COL_LAST, slot_row, slot_row)
    snap = snapshot_ranges(client, "schedule-to-day-slot", [dst_block])

    client.values_update(
        dst_block,
        [[False, args.task, getattr(args, "type", "") or "",
          getattr(args, "project", "") or "", getattr(args, "notes", "") or ""]],
    )

    trace("schedule-to-day-slot", f"{day_name.lower()}-{slot}", [
        f"- task: {args.task}",
        f"- placement: {day_name} tab slot {slot} (row {slot_row})",
        f"- overwrote: {existing!r}" if existing else "- overwrote: (slot was empty)",
        f"- snapshot: {snap}",
    ])
    print(f'task-tracker-manager: scheduled "{args.task}" → {day_name} slot {slot}')
    return 0


def _read_recurring_template(client: SheetsClient) -> list[dict]:
    """Recurring source (2026-05-17 consolidation): the separate Recurring tab is
    retired — recurring items now live in the single `To Do` tab, identified by a
    `Weekly Recurring {Day}` Horizon (col G). Returns the same dict shape the
    stamp helpers expect: day (3-letter), slot (always None → auto-pick, matching
    the old all-blank-slot convention), task, type, project, notes, row (1-based).
    Malformed Horizon days are warned + skipped so one bad row can't abort the
    Sunday rollover."""
    rows = client.get_values(
        f"'{TAB_TODO}'!A2:{col_letter(TODO_COL_HORIZON)}{TODO_MAX_ROWS}")
    out: list[dict] = []
    for i, row in enumerate(rows):
        task = (row[TODO_COL_TASK] if len(row) > TODO_COL_TASK else "").strip() if row else ""
        horizon = (row[TODO_COL_HORIZON] if len(row) > TODO_COL_HORIZON else "").strip() if row else ""
        if not task or not _todo_is_recurring(horizon):
            continue
        day3 = _recurring_day3(horizon)
        if day3 is None:
            print(f"task-tracker-manager: WARNING To Do row {2+i} has unparseable "
                  f"recurring Horizon {horizon!r} — skipped", file=sys.stderr)
            continue
        type_ = (row[TODO_COL_TYPE] if len(row) > TODO_COL_TYPE else "").strip() if row else ""
        if type_ and type_ not in TYPE_OPTIONS:
            type_ = ""
        project = (row[TODO_COL_PROJECT] if len(row) > TODO_COL_PROJECT else "").strip() if row else ""
        notes = (row[TODO_COL_NOTES] if len(row) > TODO_COL_NOTES else "").strip() if row else ""
        out.append({
            "row": 2 + i,
            "day": day3,
            "slot": None,  # auto-pick first empty (old recurring slot was always blank)
            "task": task,
            "type": type_ or "Work",
            "project": project,
            "notes": notes,
        })
    return out


def _stamp_recurring_week(client: SheetsClient, meta: dict,
                          dry_run: bool = False) -> dict:
    """Stamp every row of the Recurring Template onto the WEEK planning grid's
    day blocks (design-corrected target — recurring lands on the Week canvas,
    NOT the 7 day tabs; `distribute-week` later fans the finalized Week plan
    into the day tabs). Mirrors the day-tab collision-refuse semantics.

    Returns {stamped, refused, rows_read, tab_present}."""
    # Recurring source is the To Do tab (Horizon = 'Weekly Recurring {Day}'),
    # not a separate tab — see _read_recurring_template (2026-05-17 consolidation).
    week_tab = find_tab(meta, TAB_WEEK)
    summary = {"stamped": [], "refused": [], "rows_read": 0, "tab_present": True}
    if week_tab is None:
        print(f"task-tracker-manager: '{TAB_WEEK}' tab not present — cannot stamp recurring")
        return summary

    rows = _read_recurring_template(client)
    summary["rows_read"] = len(rows)
    if not rows:
        print("task-tracker-manager: no 'Weekly Recurring' To Do rows — nothing to stamp")
        return summary

    # In-memory view of each day-block's content column (post-clear state).
    # day_idx 0=Sun..6=Sat ; WK_DAY_ORDER aligns to that index.
    name_to_widx = {name: i for i, name in enumerate(WK_DAY_ORDER)}
    slot_grid: dict[int, list[str]] = {}
    for widx in range(7):
        tc = wk_content_col(widx)
        cl = col_letter(tc)
        vals = client.get_values(
            f"'{TAB_WEEK}'!{cl}{WK_SLOT_FIRST_ROW}:{cl}{WK_SLOT_LAST_ROW}")
        flat = [(v[0] if v else "") if isinstance(v, list) else "" for v in vals]
        while len(flat) < WK_SLOT_COUNT:
            flat.append("")
        slot_grid[widx] = flat

    writes: list[tuple[str, list[list]]] = []
    for r in rows:
        day_idx = DAY_BY_NAME[r["day"].lower()]
        tab_name = DAY_LABELS[day_idx]  # 3-letter == WK_DAY_ORDER member
        widx = name_to_widx.get(tab_name)
        if widx is None:
            summary["refused"].append({"row": r["row"], "day": r["day"],
                                       "slot": r["slot"], "task": r["task"],
                                       "reason": f"unknown day {tab_name!r}"})
            continue

        target_slot = r["slot"]
        if target_slot is not None:
            existing = slot_grid[widx][target_slot - 1]
            if existing and str(existing).strip():
                summary["refused"].append({
                    "row": r["row"], "day": r["day"], "slot": target_slot,
                    "task": r["task"], "reason": f'slot occupied by "{existing}"'})
                print(f'task-tracker-manager: WARNING recurring stamp REFUSED '
                      f'(template row {r["row"]}, Week {tab_name} slot {target_slot}): '
                      f'slot occupied by "{existing}" — skipping, Kay resolves manually')
                continue
            chosen_slot = target_slot
        else:
            chosen_slot = None
            for idx, v in enumerate(slot_grid[widx]):
                if not v or not str(v).strip():
                    chosen_slot = idx + 1
                    break
            if chosen_slot is None:
                summary["refused"].append({
                    "row": r["row"], "day": r["day"], "slot": None,
                    "task": r["task"], "reason": f"Week {tab_name} has no empty slots"})
                print(f'task-tracker-manager: WARNING recurring stamp REFUSED '
                      f'(template row {r["row"]}): Week {tab_name} has no empty slots — skipping')
                continue

        slot_row = WK_SLOT_FIRST_ROW + chosen_slot - 1
        sc = col_letter(wk_status_col(widx))
        tc = col_letter(wk_content_col(widx))
        # Status checkbox FALSE + task text. Type/Project/Notes are NOT carried
        # onto the Week grid (it is a compact planning canvas — task text only;
        # distribute-week reads task text and the day tabs carry full metadata
        # via promote/schedule-to-day-slot/recurring stamp on distribute).
        writes.append((f"'{TAB_WEEK}'!{sc}{slot_row}", [[False]]))
        writes.append((f"'{TAB_WEEK}'!{tc}{slot_row}", [[r["task"]]]))
        slot_grid[widx][chosen_slot - 1] = r["task"]
        summary["stamped"].append({
            "template_row": r["row"], "day": r["day"], "slot": chosen_slot,
            "task": r["task"], "auto_picked": r["slot"] is None})
        prefix = "task-tracker-manager: recurring stamp → Week"
        if dry_run:
            prefix += " (DRY RUN)"
        ap = " (auto-picked)" if r["slot"] is None else ""
        print(f'{prefix}: template row {r["row"]} → Week {tab_name} slot {chosen_slot}{ap}: "{r["task"]}"')

    if not dry_run and writes:
        for rng, vals in writes:
            client.values_update(rng, vals)
    return summary


def _day_clear_requests(sid: int) -> list[dict]:
    """Build repeatCell requests that reset ONE day tab to a clean week:
    habit checkboxes FALSE, slot status checkboxes FALSE, slot Task/Type/Project/
    Notes empty, free-notes block empty. Title row + headers + dropdowns + CF +
    checkbox data-validation are PRESERVED (only userEnteredValue is touched)."""
    reqs: list[dict] = []
    # Habit status checkboxes (col A, rows 4..10) → FALSE
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_HABIT_FIRST_ROW - 1, "endRowIndex": DAY_HABIT_LAST_ROW,
                  "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_STATUS + 1},
        "cell": {"userEnteredValue": {"boolValue": False}},
        "fields": "userEnteredValue"}})
    # Slot status checkboxes (col A, rows 13..27) → FALSE
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_SLOT_FIRST_ROW - 1, "endRowIndex": DAY_SLOT_LAST_ROW,
                  "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_STATUS + 1},
        "cell": {"userEnteredValue": {"boolValue": False}},
        "fields": "userEnteredValue"}})
    # Slot Task/Type/Project/Notes (cols B..E, rows 13..27) → empty
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_SLOT_FIRST_ROW - 1, "endRowIndex": DAY_SLOT_LAST_ROW,
                  "startColumnIndex": DAY_COL_TASK, "endColumnIndex": DAY_COL_LAST + 1},
        "cell": {"userEnteredValue": {"stringValue": ""}},
        "fields": "userEnteredValue"}})
    # Free-notes block (cols A..E, rows 30..37) → empty
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_NOTES_FIRST_ROW - 1, "endRowIndex": DAY_NOTES_LAST_ROW,
                  "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_LAST + 1},
        "cell": {"userEnteredValue": {"stringValue": ""}},
        "fields": "userEnteredValue"}})
    return reqs


def _week_clear_requests(sid: int) -> list[dict]:
    """Build repeatCell requests that reset the Week planning tab to a clean week:
    for each of the 7 day-columns — habit checkboxes FALSE, slot status checkboxes FALSE,
    slot task text empty, per-day notes block empty. Title row + headers + labels +
    dropdowns + CF + checkbox data-validation are PRESERVED (only userEnteredValue is touched)."""
    reqs: list[dict] = []
    for i in range(7):
        sc = wk_status_col(i)
        cc = wk_content_col(i)
        # Habit status checkboxes (rows 7..15, day's status col) → FALSE
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_HABIT_FIRST_ROW - 1, "endRowIndex": WK_HABIT_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": sc + 1},
            "cell": {"userEnteredValue": {"boolValue": False}},
            "fields": "userEnteredValue"}})
        # Priority slot status checkboxes (rows 24..38, day's status col) → FALSE
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_SLOT_FIRST_ROW - 1, "endRowIndex": WK_SLOT_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": sc + 1},
            "cell": {"userEnteredValue": {"boolValue": False}},
            "fields": "userEnteredValue"}})
        # Priority slot task content (rows 24..38, day's content col) → empty
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_SLOT_FIRST_ROW - 1, "endRowIndex": WK_SLOT_LAST_ROW,
                      "startColumnIndex": cc, "endColumnIndex": cc + 1},
            "cell": {"userEnteredValue": {"stringValue": ""}},
            "fields": "userEnteredValue"}})
        # Per-day notes block (rows 41..48, day's status + content cols) → empty
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_NOTES_FIRST_ROW - 1, "endRowIndex": WK_NOTES_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": cc + 1},
            "cell": {"userEnteredValue": {"stringValue": ""}},
            "fields": "userEnteredValue"}})
    return reqs


def cmd_build_week(args) -> int:
    """Sunday weekly rebuild ceremony — targets the WEEK PLANNING TAB.

    Design-corrected model (2026-05-17): the tracker has BOTH surfaces. This
    verb rebuilds the **Week planning tab** (the Sunday canvas) — it does NOT
    touch the 7 day tabs. After Kay finalizes the week on the Week tab,
    `distribute-week` fans it out into the day tabs.

    1. Snapshot the Week tab + `To Do` to one rollback JSON.
    2. Write ONE combined `archive_{Sun-date}` tab capturing the prior week's
       Week tab verbatim (values only — the Week tab is NOT destroyed; it is
       cleared + re-titled in place, formatting preserved).
    3. Clear all 7 day-blocks' slots/habits/notes/checkboxes on the Week tab
       via repeatCell (preserves title/headers/labels/dropdowns/CF/validation).
    4. Re-title the Week tab title row to this week's Sun..Sat label + re-stamp
       the per-day header row dates.
    5. Stamp the Recurring Template ONTO THE WEEK TAB (unless --skip-recurring).
    6. Trace.

    Flags: --dry-run (report only, NO writes), --skip-recurring.

    NOTE: carryover is NOT auto-copied — `report` surfaces incompletes and Kay
    approves each move during the Sunday walkthrough, on the Week tab.
    """
    client = SheetsClient()
    meta = client.get_metadata()

    week_tab = find_tab(meta, TAB_WEEK)
    wd = week_dates(date.today())  # Sun..Sat dates for THIS week
    sun_date = wd[0]
    if sun_date.month == wd[6].month:
        week_label = f"WEEK OF {sun_date.strftime('%b')} {sun_date.day}-{wd[6].day}"
    else:
        week_label = (f"WEEK OF {sun_date.strftime('%b')} {sun_date.day}-"
                      f"{wd[6].strftime('%b')} {wd[6].day}")
    archive_name = f"archive_{sun_date.strftime('%b')} {sun_date.day}"

    # ---------- dry-run: report only ----------
    if getattr(args, "dry_run", False):
        print("task-tracker-manager: build-week (DRY RUN) — targets the Week planning tab")
        print(f"  Week (Sunday boundary): {wd[0].isoformat()} .. {wd[6].isoformat()}")
        print(f"  Week tab present: {week_tab is not None}"
              + ("" if week_tab is not None else " — run scripts/build_week_tab.py first"))
        print(f"  Would write combined archive tab: {archive_name!r} (far-right)")
        print(f"  Would clear ALL 7 day-blocks on the Week tab + re-title row 1 → {week_label!r}")
        print("  Would re-stamp per-day header dates (row 15):")
        for i in range(7):
            print(f"    {WK_DAY_ORDER[i]} → {day_title_text(WK_DAY_ORDER[i], wd[i])!r}")
        if getattr(args, "skip_recurring", False):
            print("  --skip-recurring set → would NOT stamp recurring rows")
        else:
            rows = _read_recurring_template(client)
            if not rows:
                print("  No 'Weekly Recurring' To Do rows — nothing to stamp")
            else:
                print(f"  {len(rows)} 'Weekly Recurring' To Do row(s); "
                      f"would stamp onto the CLEARED Week grid:")
                synth: dict[str, set[int]] = {n: set() for n in WK_DAY_ORDER}
                for r in rows:
                    tab_name = DAY_LABELS[DAY_BY_NAME[r["day"].lower()]]
                    if tab_name not in synth:
                        print(f'    REFUSED template row {r["row"]}: unknown day {tab_name!r}')
                        continue
                    if r["slot"] is not None:
                        if r["slot"] in synth[tab_name]:
                            print(f'    REFUSED template row {r["row"]} (Week {tab_name} slot {r["slot"]}): '
                                  f'another template row already pinned there')
                            continue
                        synth[tab_name].add(r["slot"]); slot = r["slot"]; ap = ""
                    else:
                        slot = next((s for s in range(1, WK_SLOT_COUNT + 1)
                                     if s not in synth[tab_name]), None)
                        if slot is None:
                            print(f'    REFUSED template row {r["row"]}: Week {tab_name} has no empty slots')
                            continue
                        synth[tab_name].add(slot); ap = " (auto-picked)"
                    print(f'    WOULD STAMP: template row {r["row"]} → Week {tab_name} slot {slot}{ap}: "{r["task"]}"')
        print("task-tracker-manager: build-week DRY RUN complete — no writes")
        return 0

    if week_tab is None:
        sys.exit("task-tracker-manager: Week tab not present — run "
                 "scripts/build_week_tab.py before build-week")
    wk_sid = week_tab["sheetId"]

    # ---------- 1. Snapshot ----------
    # (_donut_data removed 2026-05-17 — donut layer retired.)
    snap_ranges = [f"'{TAB_WEEK}'!A1:{col_letter(WK_GRID_COLS - 1)}{WK_GRID_ROWS}",
                   f"'{TAB_TODO}'!A1:{col_letter(TODO_COL_HORIZON)}{TODO_MAX_ROWS}"]
    snap = snapshot_ranges(client, "build-week", snap_ranges)

    # ---------- 2. Combined archive tab (prior Week tab verbatim, values-only) -
    existing_titles = {s["properties"]["title"] for s in meta.get("sheets", [])}
    final_archive = archive_name
    suffix = 1
    while final_archive in existing_titles:
        suffix += 1
        final_archive = f"{archive_name}_v{suffix}"
    client.batch_update([{
        "addSheet": {"properties": {
            "title": final_archive,
            "index": len(meta.get("sheets", [])),  # far right
            "gridProperties": {"rowCount": WK_GRID_ROWS + 4,
                               "columnCount": WK_GRID_COLS},
        }}
    }])
    prior = client.get_values(
        f"'{TAB_WEEK}'!A1:{col_letter(WK_GRID_COLS - 1)}{WK_GRID_ROWS}")
    archive_block: list[list] = [
        [f"ARCHIVE — Week tab, week of {sun_date.strftime('%b')} {sun_date.day} "
         f"(captured {date.today().isoformat()})"]
    ]
    for row in (prior or []):
        archive_block.append(list(row) if row else [])
    client.values_update(
        f"'{final_archive}'!A1:{col_letter(WK_GRID_COLS - 1)}{len(archive_block)}",
        archive_block)

    # ---------- 3. Clear + 4. Re-title (one batch) ----------
    mutate: list[dict] = _week_clear_requests(wk_sid)
    # Row-1 title (col 0, merged anchor)
    mutate.append({"updateCells": {
        "rows": [{"values": [{"userEnteredValue": {"stringValue": week_label}}]}],
        "fields": "userEnteredValue",
        "start": {"sheetId": wk_sid, "rowIndex": WK_TITLE_ROW - 1, "columnIndex": 0}}})
    # Per-day header dates (row 15, merged anchors at status cols)
    for i in range(7):
        sc = wk_status_col(i)
        mutate.append({"updateCells": {
            "rows": [{"values": [{"userEnteredValue": {
                "stringValue": day_title_text(WK_DAY_ORDER[i], wd[i])}}]}],
            "fields": "userEnteredValue",
            "start": {"sheetId": wk_sid, "rowIndex": WK_DAYHDR_ROW - 1,
                      "columnIndex": sc}}})
    client.batch_update(mutate)

    # ---------- 5. Recurring stamp (onto the Week tab) ----------
    recurring_summary: dict = {"stamped": [], "refused": [], "rows_read": 0, "tab_present": False}
    if getattr(args, "skip_recurring", False):
        print("task-tracker-manager: --skip-recurring set — Recurring Template NOT stamped")
    else:
        meta_after = client.get_metadata()
        recurring_summary = _stamp_recurring_week(client, meta_after, dry_run=False)

    # ---------- 6. Trace ----------
    trace_lines = [
        f"- week (Sunday boundary): {wd[0].isoformat()} .. {wd[6].isoformat()}",
        f"- target: Week planning tab (day tabs untouched — distribute-week fans out later)",
        f"- combined archive tab written: {final_archive} (far-right, values-only)",
        f"- Week tab cleared + re-titled: {week_label!r}",
        f"- snapshot: {snap}",
    ]
    if recurring_summary["tab_present"]:
        trace_lines.append(f"- recurring stamped onto Week: {len(recurring_summary['stamped'])} row(s)")
        if recurring_summary["refused"]:
            trace_lines.append(f"- recurring REFUSED: {len(recurring_summary['refused'])}")
            for ref in recurring_summary["refused"]:
                trace_lines.append(f"  - template row {ref['row']} {ref['day']} slot {ref['slot']}: {ref['reason']}")
    trace("build-week", sun_date.isoformat(), trace_lines)
    print(f'task-tracker-manager: build-week complete — archived prior Week → "{final_archive}", '
          f'cleared + re-titled the Week tab to {week_label!r}. '
          f'Day tabs untouched — run distribute-week after Kay finalizes the plan.')
    if recurring_summary["tab_present"]:
        print(f'task-tracker-manager: stamped {len(recurring_summary["stamped"])} recurring row(s) onto Week'
              + (f"; {len(recurring_summary['refused'])} refused" if recurring_summary["refused"] else ""))
    return 0


def cmd_distribute_week(args) -> int:
    """Fan the finalized Week planning tab OUT into the 7 day tabs.

    Design-corrected model (2026-05-17): after `build-week` rebuilds the Week
    tab and Kay lays out the full week there, this verb reads each Week-grid
    day-block's 15 priority slots (status + task) and habit checkboxes and
    writes them into the corresponding day tab's slots (rows 13-27) + habits
    (rows 4-10). Collision-aware: refuses to overwrite a non-empty day-tab slot
    that the Week plan does NOT also fill at the same slot index, unless
    --force (so re-running after a manual day-tab edit is safe by default).

    Flags: --dry-run (report only), --force (overwrite occupied day-tab slots),
    --day {Sun..Sat} (limit to one day; default all 7).
    """
    client = SheetsClient()
    meta = client.get_metadata()
    week_tab = find_tab(meta, TAB_WEEK)
    if week_tab is None:
        sys.exit("task-tracker-manager: Week tab not present — run build-week first")

    only_day = None
    if getattr(args, "day", None):
        only_day = _resolve_day_tab_name(args.day)

    wd = week_dates(date.today())
    targets = []  # (widx, day_name)
    for widx, name in enumerate(WK_DAY_ORDER):
        if only_day and name != only_day:
            continue
        if find_day_tab(meta, name) is None:
            print(f"task-tracker-manager: WARNING day tab {name!r} not present — skipping")
            continue
        targets.append((widx, name))

    # Read Week-grid plan per target day.
    plan: dict[str, dict] = {}
    for widx, name in targets:
        sc = col_letter(wk_status_col(widx))
        tc = col_letter(wk_content_col(widx))
        st = client.get_values(f"'{TAB_WEEK}'!{sc}{WK_SLOT_FIRST_ROW}:{sc}{WK_SLOT_LAST_ROW}")
        tk = client.get_values(f"'{TAB_WEEK}'!{tc}{WK_SLOT_FIRST_ROW}:{tc}{WK_SLOT_LAST_ROW}")
        hb = client.get_values(f"'{TAB_WEEK}'!{sc}{WK_HABIT_FIRST_ROW}:{sc}{WK_HABIT_LAST_ROW}")
        slots = []
        for i in range(WK_SLOT_COUNT):
            s = st[i][0] if i < len(st) and st[i] else ""
            t = tk[i][0] if i < len(tk) and tk[i] else ""
            slots.append((_is_truthy(s), str(t).strip() if t else ""))
        habits = []
        for i in range(WK_HABIT_COUNT):
            h = hb[i][0] if i < len(hb) and hb[i] else ""
            habits.append(_is_truthy(h))
        plan[name] = {"slots": slots, "habits": habits}

    # Inspect destination day-tab slots for collisions.
    collisions: list[str] = []
    dest_now: dict[str, list[str]] = {}
    for _widx, name in targets:
        cur = client.get_values(
            day_tab_range(name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
        flat = [(cur[i][0] if i < len(cur) and cur[i] else "") for i in range(DAY_SLOT_COUNT)]
        flat = [str(x).strip() if x else "" for x in flat]
        dest_now[name] = flat
        for i in range(DAY_SLOT_COUNT):
            planned = plan[name]["slots"][i][1] if i < len(plan[name]["slots"]) else ""
            existing = flat[i]
            if existing and planned and existing != planned:
                collisions.append(f"{name} slot {i+1}: day tab has \"{existing}\" "
                                  f"≠ Week plan \"{planned}\"")
            elif existing and not planned:
                collisions.append(f"{name} slot {i+1}: day tab has \"{existing}\" "
                                  f"but Week plan is empty there")

    if getattr(args, "dry_run", False):
        print("task-tracker-manager: distribute-week (DRY RUN)")
        print(f"  Week (Sunday boundary): {wd[0].isoformat()} .. {wd[6].isoformat()}")
        print(f"  Targets: {[n for _w, n in targets] or '(none)'}")
        for _widx, name in targets:
            filled = sum(1 for _s, t in plan[name]["slots"] if t)
            print(f"    {name}: would write {filled} slot(s) + "
                  f"{sum(plan[name]['habits'])} habit check(s)")
        if collisions:
            print(f"  COLLISIONS ({len(collisions)}) — would "
                  f"{'OVERWRITE (--force)' if getattr(args,'force',False) else 'REFUSE without --force'}:")
            for c in collisions:
                print(f"    - {c}")
        else:
            print("  No collisions.")
        print("task-tracker-manager: distribute-week DRY RUN complete — no writes")
        return 0

    if collisions and not getattr(args, "force", False):
        print(f"task-tracker-manager: refused distribute-week — {len(collisions)} "
              f"collision(s) between the Week plan and existing day-tab content. "
              f"Re-run with --force to overwrite, or resolve on the day tabs first:",
              file=sys.stderr)
        for c in collisions:
            print(f"  - {c}", file=sys.stderr)
        return 1

    # Snapshot every target day tab's full block + the Week tab.
    snap_ranges = [day_tab_block(n, DAY_COL_STATUS, DAY_COL_LAST, 1, DAY_GRID_ROWS)
                   for _w, n in targets]
    snap_ranges.append(f"'{TAB_WEEK}'!A1:{col_letter(WK_GRID_COLS - 1)}{WK_GRID_ROWS}")
    snap = snapshot_ranges(client, "distribute-week", snap_ranges)

    written = {}
    for _widx, name in targets:
        slots = plan[name]["slots"]
        habits = plan[name]["habits"]
        # Slot block A:E rows 13..27 — write [status, task, "", "", ""].
        # Type/Project/Notes are NOT carried (the Week canvas holds task text
        # only; Kay enriches on the day tab, or recurring metadata was set on
        # the Recurring Template and is re-applied if she re-promotes). Existing
        # day-tab Type/Project for a row that keeps the same task is preserved
        # only when the slot already matched; otherwise reset to blank.
        rows_vals = []
        for i in range(DAY_SLOT_COUNT):
            done, task = slots[i] if i < len(slots) else (False, "")
            rows_vals.append([done, task, "", "", ""])
        client.values_update(
            day_tab_block(name, DAY_COL_STATUS, DAY_COL_LAST,
                          DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW),
            rows_vals)
        # Habit checkboxes rows 4..10 col A.
        client.values_update(
            day_tab_range(name, DAY_COL_STATUS, DAY_HABIT_FIRST_ROW, DAY_HABIT_LAST_ROW),
            [[h] for h in habits])
        written[name] = sum(1 for _d, t in slots if t)

    trace("distribute-week", wd[0].isoformat(), [
        f"- week (Sunday boundary): {wd[0].isoformat()} .. {wd[6].isoformat()}",
        f"- fanned Week plan → day tabs: {written}",
        f"- forced over collisions: {getattr(args, 'force', False)}",
        f"- collisions at run: {collisions or 'none'}",
        f"- snapshot: {snap}",
    ])
    total = sum(written.values())
    print(f"task-tracker-manager: distribute-week complete — fanned {total} slot(s) "
          f"from the Week tab into {len(written)} day tab(s): {written}")
    return 0


def cmd_archive(args) -> int:
    """DEPRECATED ALIAS 2026-05-17 → build-week. The single Live Week grid is
    retired; the Sunday ceremony is now `build-week` over 7 permanent day tabs.
    This alias delegates and prints a deprecation notice."""
    print("task-tracker-manager: NOTICE `archive` is deprecated — delegating to "
          "`build-week` (day-tab model, 2026-05-17 rebuild). Update callers to "
          "use `build-week` directly.", file=sys.stderr)
    return cmd_build_week(args)


def cmd_sync_done_status(args, _client: "SheetsClient | None" = None,
                         _meta: dict | None = None) -> int:
    """Reconcile checked weekly slots → matching To Do rows by exact task-text match.

    For each non-empty DAY-TAB priority slot whose native checkbox is TRUE, find the
    matching To Do row (case-sensitive, whitespace-stripped) and set its Status to
    "Completed" (3-state dropdown, post-2026-05-17). The CF rule (=$A2="Completed")
    paints strikethrough + sage-light fill. Ambiguous matches (>1 To Do row, same
    task) are flagged + skipped — Kay resolves manually.

    Recurring-Horizon To Do rows are excluded from matching: checking a stamped
    recurring instance on a day tab must NOT complete the permanent template row.
    Day tabs / Week tab keep native checkboxes (Kay's surfaces, unchanged) — only
    the To Do backend uses the Status enum.
    """
    client = _client or SheetsClient()
    meta = _meta or client.get_metadata()
    day_tabs = list(_iter_day_tabs(meta))
    if not day_tabs:
        sys.exit("task-tracker-manager: no day tabs present — run scripts/build_day_tabs.py first")

    # 1. Walk the 7 day tabs' 15 slots each — read A (status) + B (task) columns.
    #    MUST run BEFORE the Sunday clear (build-week) so completed items flow to
    #    To Do before slots are wiped.
    weekly_checked: list[dict] = []  # one entry per (day, slot) where checkbox=TRUE and task non-empty
    weekly_slots_scanned = 0
    for day_name, _props in day_tabs:
        status_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_STATUS, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
        task_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
        for slot_i in range(DAY_SLOT_COUNT):
            status = status_vals[slot_i][0] if slot_i < len(status_vals) and status_vals[slot_i] else ""
            task = task_vals[slot_i][0] if slot_i < len(task_vals) and task_vals[slot_i] else ""
            task_text = (task or "").strip() if isinstance(task, str) else ""
            if not task_text:
                continue
            weekly_slots_scanned += 1
            if _is_truthy(status):
                weekly_checked.append({
                    "day": day_name,
                    "slot": slot_i + 1,
                    "task_text": task_text,
                })

    # 2. Walk To Do tab — build {task_text(stripped): [row_indices]} dict.
    #    Recurring-Horizon rows are EXCLUDED: a daily check of a stamped recurring
    #    instance must never mark the permanent recurring template row 'Completed'.
    todo_rows = client.get_values(
        f"'{TAB_TODO}'!A2:{col_letter(TODO_COL_HORIZON)}{TODO_MAX_ROWS}")
    todo_by_task: dict[str, list[dict]] = {}
    for i, row in enumerate(todo_rows):
        task = row[TODO_COL_TASK] if len(row) > TODO_COL_TASK else ""
        if not isinstance(task, str):
            continue
        key = task.strip()
        if not key:
            continue
        horizon = row[TODO_COL_HORIZON] if len(row) > TODO_COL_HORIZON else ""
        if _todo_is_recurring(horizon):
            continue
        status = row[TODO_COL_STATUS] if len(row) > TODO_COL_STATUS else ""
        todo_by_task.setdefault(key, []).append({
            "row": 2 + i,  # 1-based
            "status": status,
            "is_truthy": _todo_is_done(status),
        })

    # 3. Match + classify.
    to_sync: list[dict] = []  # rows to flip TRUE
    ambiguities: list[dict] = []
    schedule_only_skipped = 0
    already_true = 0
    for w in weekly_checked:
        matches = todo_by_task.get(w["task_text"])
        if not matches:
            schedule_only_skipped += 1
            continue
        if len(matches) > 1:
            ambiguities.append({
                "task_text": w["task_text"],
                "rows": [m["row"] for m in matches],
                "day": w["day"],
                "slot": w["slot"],
            })
            continue
        m = matches[0]
        if m["is_truthy"]:
            already_true += 1
            continue
        to_sync.append({
            "row": m["row"],
            "task_text": w["task_text"],
            "day": w["day"],
            "slot": w["slot"],
        })

    # Dedup to_sync — if two weekly slots checked same task (rare), one write is enough.
    seen_rows: set[int] = set()
    deduped: list[dict] = []
    for s in to_sync:
        if s["row"] in seen_rows:
            continue
        seen_rows.add(s["row"])
        deduped.append(s)
    to_sync = deduped

    # 4. Snapshot To Do Status column BEFORE any write — always, even no-op (audit trail).
    # If snapshot write fails the helper raises and the verb aborts.
    snap = snapshot_ranges(client, "sync-done-status", [
        f"'{TAB_TODO}'!A2:A{TODO_MAX_ROWS}",
    ])

    # 5. Apply writes (or skip in dry-run).
    rows_synced = 0
    if to_sync and not args.dry_run:
        # Status is a 3-state dropdown string post-2026-05-17. Write the literal
        # "Completed"; the ONE_OF_LIST validation accepts it and the CF rule
        # (=$A2="Completed") paints strikethrough + sage-light fill.
        todo_tab = find_tab(meta, TAB_TODO)
        if todo_tab is None:
            sys.exit(f"task-tracker-manager: '{TAB_TODO}' tab not found")
        todo_sid = todo_tab["sheetId"]
        batch: list[dict] = []
        for s in to_sync:
            batch.append({
                "updateCells": {
                    "rows": [{"values": [{"userEnteredValue": {"stringValue": "Completed"}}]}],
                    "fields": "userEnteredValue",
                    "start": {"sheetId": todo_sid, "rowIndex": s["row"] - 1, "columnIndex": TODO_COL_STATUS},
                }
            })
        client.batch_update(batch)
        rows_synced = len(to_sync)

    # 6. Print summary.
    prefix = "task-tracker-manager: sync-done-status"
    if args.dry_run:
        prefix += " (DRY RUN)"
    print(f"{prefix} complete")
    print(f"  Weekly slots scanned: {weekly_slots_scanned}")
    print(f"  Slots checked TRUE: {len(weekly_checked)}")
    if args.dry_run:
        would = len(to_sync)
        print(f"  To Do rows WOULD sync: {would}")
    else:
        print(f"  To Do rows synced: {rows_synced}")
    print(f"  Already-TRUE no-ops: {already_true}")
    print(f"  Ambiguities flagged: {len(ambiguities)}")
    print(f"  Schedule-only items skipped: {schedule_only_skipped}")
    print(f"  Snapshot: {snap}")
    for amb in ambiguities:
        print(f'  AMBIGUITY: "{amb["task_text"]}" matches To Do rows {amb["rows"]} '
              f'(checked from {amb["day"]} slot {amb["slot"]})')

    # 7. Trace only if real change occurred (>0 rows synced) AND not dry-run.
    if rows_synced > 0 and not args.dry_run:
        lines = [
            f"- rows synced: {rows_synced}",
            f"- weekly slots scanned: {weekly_slots_scanned}",
            f"- weekly slots TRUE: {len(weekly_checked)}",
            f"- schedule-only skipped: {schedule_only_skipped}",
            f"- already-TRUE no-ops: {already_true}",
            f"- ambiguities: {len(ambiguities)}",
            "",
            "**Synced:**",
        ]
        for s in to_sync:
            lines.append(f"- row {s['row']}: \"{s['task_text']}\" (from {s['day']} slot {s['slot']})")
        if ambiguities:
            lines.append("")
            lines.append("**Ambiguities (NOT written, resolve manually):**")
            for amb in ambiguities:
                lines.append(f"- \"{amb['task_text']}\" → rows {amb['rows']}")
        lines.append("")
        lines.append(f"- snapshot: {snap}")
        lines.append(f"- rollback: replay snapshot ranges from {snap}")
        trace("sync-done-status", f"synced-{rows_synced}", lines)

    return 0


def cmd_archive_todo(args) -> int:
    """RETIRED 2026-05-17 (schema consolidation). The sweep-to-Completed-tab
    model is gone: Status is now a 3-state dropdown in the single `To Do` tab and
    completed rows stay in place (strikethrough via CF, hidden via filter views).
    Kept as a no-op so any lingering caller / scheduled invocation does not error."""
    print("task-tracker-manager: archive-todo is RETIRED (2026-05-17 consolidation) "
          "— no sweep. Completed items stay in To Do; use Status='Completed' + a "
          "filter view. No action taken.", file=sys.stderr)
    return 0



def _is_truthy(v) -> bool:
    """Native-checkbox truthiness. Used for DAY-TAB and WEEK-TAB slots/habits
    (those remain native checkboxes — Kay's working surfaces, unchanged)."""
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().upper() in ("TRUE", "✅", "YES", "DONE")
    return bool(v)


def _todo_is_done(v) -> bool:
    """To Do tab 'done' test. Post-2026-05-17 the To Do Status column is a
    3-state dropdown string, not a checkbox. Done == 'Completed'. Old boolean
    TRUE is still treated as done so this is safe to run pre/post migration."""
    if isinstance(v, bool):
        return v
    return str(v or "").strip().lower() == "completed"


def _todo_is_recurring(horizon: str) -> bool:
    """A To Do row is a recurring template if its Horizon starts with a
    recurring prefix (currently only 'Weekly Recurring {Day}')."""
    return str(horizon or "").strip().startswith(RECURRING_HORIZON_PREFIX)


def _recurring_day3(horizon: str) -> str | None:
    """Extract the 3-letter target day from a 'Weekly Recurring {Day}' horizon."""
    h = str(horizon or "").strip()
    if not h.startswith(RECURRING_HORIZON_PREFIX):
        return None
    suffix = h[len(RECURRING_HORIZON_PREFIX):].strip()
    idx = DAY_BY_NAME.get(suffix.lower())
    return DAY_LABELS[idx] if idx is not None else None


def cmd_recurring_add(args) -> int:
    """Add a weekly-recurring item. Post-2026-05-17 the separate Recurring tab is
    retired — this appends a row to the single `To Do` tab with
    Horizon="Weekly Recurring {Day}" + Status="On-going". `build-week` reads these
    every Sunday. Decision-content (changes future weeks), so traces.
    `--slot` is accepted but ignored (recurring always auto-picks, as before)."""
    day_idx = DAY_BY_NAME.get(args.day.lower())
    if day_idx is None:
        sys.exit(f"task-tracker-manager: unknown day {args.day!r}. Use Mon..Sat.")
    day3 = DAY_LABELS[day_idx]
    horizon = f"{RECURRING_HORIZON_PREFIX} {day3}"
    if horizon not in HORIZON_OPTIONS:
        sys.exit(f"task-tracker-manager: weekly recurring supports Mon..Sat only "
                 f"(got {day3}). {horizon!r} not in {HORIZON_OPTIONS}")
    if args.type not in TYPE_OPTIONS:
        sys.exit(f"task-tracker-manager: --type must be one of {TYPE_OPTIONS}")
    if not args.task.strip():
        sys.exit("task-tracker-manager: --task must be non-empty")

    client = SheetsClient()

    existing = client.get_values(
        f"'{TAB_TODO}'!{col_letter(TODO_COL_TASK)}2:{col_letter(TODO_COL_TASK)}{TODO_MAX_ROWS}")
    target_row = 2
    for i, row in enumerate(existing):
        if not row or not (row[0] if row else "").strip():
            target_row = 2 + i
            break
    else:
        target_row = 2 + len(existing)
    if target_row > TODO_MAX_ROWS:
        sys.exit(f"task-tracker-manager: To Do tab is full (>{TODO_MAX_ROWS}).")

    snap = snapshot_ranges(client, "recurring-add",
        [f"'{TAB_TODO}'!A{target_row}:G{target_row}"])
    client.values_update(f"'{TAB_TODO}'!A{target_row}:G{target_row}", [[
        "On-going", args.task, args.type, args.project or "", "",
        args.notes or "", horizon,
    ]])

    trace("recurring-add", f"{day3.lower()}-row{target_row}", [
        f"- horizon: {horizon}",
        f"- task: {args.task}",
        f"- type: {args.type}",
        f"- project: {args.project or '—'}",
        f"- To Do row: {target_row}",
        f"- snapshot: {snap}",
        f"- effect: stamped onto {day3} every future Sunday build-week",
    ])
    print(f'task-tracker-manager: added recurring To Do row {target_row} '
          f'("{args.task}", {horizon}, {args.type})')
    return 0


def cmd_recurring_remove(args) -> int:
    """Remove a weekly-recurring item by clearing its `To Do` row (preserves row
    numbering for snapshot rollback). Refuses non-recurring rows as a guard.
    Traces (compounds across every future week)."""
    client = SheetsClient()
    if not (2 <= args.row <= TODO_MAX_ROWS):
        sys.exit(f"task-tracker-manager: --row must be 2..{TODO_MAX_ROWS} (1 is the header)")

    pre = client.get_values(f"'{TAB_TODO}'!A{args.row}:G{args.row}")
    pre_row = pre[0] if pre and pre[0] else []
    if not pre_row or not any((c or "").strip() if isinstance(c, str) else c for c in pre_row):
        sys.exit(f"task-tracker-manager: To Do row {args.row} is already empty")
    pad = list(pre_row) + [""] * (7 - len(pre_row))
    horizon = str(pad[TODO_COL_HORIZON] or "")
    if not _todo_is_recurring(horizon):
        sys.exit(f"task-tracker-manager: refused — To Do row {args.row} Horizon "
                 f"{horizon!r} is not recurring. Use a normal edit, not recurring-remove.")

    snap = snapshot_ranges(client, "recurring-remove",
        [f"'{TAB_TODO}'!A{args.row}:G{args.row}"])
    client.values_clear(f"'{TAB_TODO}'!A{args.row}:G{args.row}")

    trace("recurring-remove", f"row{args.row}", [
        f"- removed To Do row: {args.row}",
        f"- horizon: {horizon}",
        f"- task: {pad[TODO_COL_TASK]}",
        f"- type: {pad[TODO_COL_TYPE]}",
        f"- project: {pad[TODO_COL_PROJECT] or '—'}",
        f"- snapshot: {snap}",
        f"- effect: no longer stamped on future Sunday build-week ceremonies",
    ])
    print(f'task-tracker-manager: removed recurring To Do row {args.row} '
          f'("{pad[TODO_COL_TASK]}", {horizon})')
    return 0


def cmd_projects_create_gantt(args) -> int:
    if len(args.project) > 100 or any(ch in args.project for ch in ":\\/?*[]"):
        sys.exit(f"task-tracker-manager: invalid tab name {args.project!r} (no :\\/?*[])")
    client = SheetsClient()
    meta = client.get_metadata()
    if find_tab(meta, args.project):
        sys.exit(f"task-tracker-manager: tab {args.project!r} already exists — pick a different name or delete first")
    if find_tab(meta, TAB_PROJECTS) is None:
        sys.exit(f"task-tracker-manager: '{TAB_PROJECTS}' index tab missing")
    if args.weeks < 4 or args.weeks > 30:
        sys.exit("task-tracker-manager: --weeks must be 4..30")

    # Add new Gantt tab
    resp = client.batch_update([{
        "addSheet": {
            "properties": {
                "title": args.project,
                "gridProperties": {"rowCount": 30, "columnCount": 6 + args.weeks, "frozenRowCount": 5},
            }
        }
    }])
    gantt_sid = resp["replies"][0]["addSheet"]["properties"]["sheetId"]

    # Build structure + write headers
    snap = snapshot_ranges(client, "projects-create-gantt",
                           [f"'{TAB_PROJECTS}'!A2:G{PJ_MAX_ROWS}"])

    # Use the same Gantt builder logic from the migration script: write inline here.
    GANTT_FIRST_WEEK_COL = 5
    last_col = GANTT_FIRST_WEEK_COL + args.weeks
    R: list[dict] = []
    V: list[dict] = []
    # Title row
    R.append({"mergeCells": {
        "range": {"sheetId": gantt_sid, "startRowIndex": 1, "endRowIndex": 2,
                  "startColumnIndex": 0, "endColumnIndex": last_col},
        "mergeType": "MERGE_ALL",
    }})
    V.append({"updateCells": {
        "rows": [{"values": [{
            "userEnteredValue": {"stringValue": args.project.upper()},
            "userEnteredFormat": {
                "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE",
                "backgroundColor": hex_to_rgb(SAGE_LIGHT_HEX),
                "textFormat": {"bold": True, "fontSize": 16,
                               "foregroundColor": hex_to_rgb(SAGE_DARK_HEX)},
            },
        }]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": gantt_sid, "rowIndex": 1, "columnIndex": 0},
    }})
    # Subtitle
    R.append({"mergeCells": {
        "range": {"sheetId": gantt_sid, "startRowIndex": 2, "endRowIndex": 3,
                  "startColumnIndex": 0, "endColumnIndex": last_col},
        "mergeType": "MERGE_ALL",
    }})
    V.append({"updateCells": {
        "rows": [{"values": [{
            "userEnteredValue": {"stringValue": f"Entity: {args.entity}  ·  Tick the week boxes you're actively working on each milestone — the row builds into a Gantt bar"},
            "userEnteredFormat": {
                "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE",
                "textFormat": {"italic": True, "fontSize": 9,
                               "foregroundColor": hex_to_rgb(MUTED_HEX)},
            },
        }]}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": gantt_sid, "rowIndex": 2, "columnIndex": 0},
    }})

    # Header row 5
    headers_fixed = ["Status", "Milestone", "Start", "Target", "Notes"]
    header_cells = []
    for header in headers_fixed:
        header_cells.append({
            "userEnteredValue": {"stringValue": header},
            "userEnteredFormat": {
                "horizontalAlignment": "LEFT", "verticalAlignment": "MIDDLE",
                "backgroundColor": hex_to_rgb(SAGE_DARK_HEX),
                "textFormat": {"bold": True, "fontSize": 10,
                               "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
            },
        })
    # Week column headers
    y, m, d = (int(x) for x in args.start.split("-"))
    start_dt = date(y, m, d)
    monday = start_dt - timedelta(days=start_dt.weekday())
    for w in range(args.weeks):
        wk = monday + timedelta(days=7 * w)
        header_cells.append({
            "userEnteredValue": {"stringValue": f"{wk.month}/{wk.day}"},
            "userEnteredFormat": {
                "horizontalAlignment": "CENTER", "verticalAlignment": "MIDDLE",
                "backgroundColor": hex_to_rgb(SAGE_DARK_HEX),
                "textFormat": {"bold": True, "fontSize": 9,
                               "foregroundColor": {"red": 1, "green": 1, "blue": 1}},
            },
        })
    V.append({"updateCells": {
        "rows": [{"values": header_cells}],
        "fields": "userEnteredValue,userEnteredFormat",
        "start": {"sheetId": gantt_sid, "rowIndex": 4, "columnIndex": 0},
    }})

    # Status + week-cell checkboxes for milestone rows 6..15 (0-based 5..14)
    R.append({"setDataValidation": {
        "range": {"sheetId": gantt_sid, "startRowIndex": 5, "endRowIndex": 15,
                  "startColumnIndex": 0, "endColumnIndex": 1},
        "rule": {"condition": {"type": "BOOLEAN"}, "strict": True},
    }})
    R.append({"setDataValidation": {
        "range": {"sheetId": gantt_sid, "startRowIndex": 5, "endRowIndex": 15,
                  "startColumnIndex": GANTT_FIRST_WEEK_COL, "endColumnIndex": last_col},
        "rule": {"condition": {"type": "BOOLEAN"}, "strict": True},
    }})

    # Conditional formatting
    entity_hex = ENTITY_COLOR_HEX.get(args.entity, SAGE_DARK_HEX)
    first_week_letter = col_letter(GANTT_FIRST_WEEK_COL)
    R.append({"addConditionalFormatRule": {
        "rule": {
            "ranges": [{"sheetId": gantt_sid, "startRowIndex": 5, "endRowIndex": 15,
                        "startColumnIndex": GANTT_FIRST_WEEK_COL, "endColumnIndex": last_col}],
            "booleanRule": {
                "condition": {"type": "CUSTOM_FORMULA",
                              "values": [{"userEnteredValue": f"={first_week_letter}6=TRUE"}]},
                "format": {"backgroundColor": hex_to_rgb(entity_hex)},
            },
        },
        "index": 0,
    }})
    R.append({"addConditionalFormatRule": {
        "rule": {
            "ranges": [{"sheetId": gantt_sid, "startRowIndex": 5, "endRowIndex": 15,
                        "startColumnIndex": 0, "endColumnIndex": 5}],
            "booleanRule": {
                "condition": {"type": "CUSTOM_FORMULA",
                              "values": [{"userEnteredValue": "=$A6=TRUE"}]},
                "format": {
                    "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                    "textFormat": {"strikethrough": True,
                                   "foregroundColor": hex_to_rgb(MUTED_HEX)},
                },
            },
        },
        "index": 0,
    }})

    # Column widths
    widths = {0: 50, 1: 360, 2: 100, 3: 100, 4: 260}
    for c, w in widths.items():
        R.append({"updateDimensionProperties": {
            "range": {"sheetId": gantt_sid, "dimension": "COLUMNS", "startIndex": c, "endIndex": c + 1},
            "properties": {"pixelSize": w}, "fields": "pixelSize",
        }})
    for w in range(args.weeks):
        col = GANTT_FIRST_WEEK_COL + w
        R.append({"updateDimensionProperties": {
            "range": {"sheetId": gantt_sid, "dimension": "COLUMNS", "startIndex": col, "endIndex": col + 1},
            "properties": {"pixelSize": 44}, "fields": "pixelSize",
        }})

    client.batch_update(R + V)

    # Update Projects index
    pj_rows = client.get_values(f"'{TAB_PROJECTS}'!A2:G{PJ_MAX_ROWS}")
    existing_row = None
    for i, row in enumerate(pj_rows):
        if row and row[0] == args.project:
            existing_row = 2 + i
            break

    hyperlink = f'=HYPERLINK("#gid={gantt_sid}","Open")'
    notes = args.notes or ""
    if existing_row is None:
        # Append new row
        target_row = 2 + len([r for r in pj_rows if r and r[0]])
        client.values_update(
            f"'{TAB_PROJECTS}'!A{target_row}:G{target_row}",
            [[args.project, args.entity, args.status, args.start, args.target, hyperlink, notes]],
        )
        index_msg = f"appended at row {target_row}"
    else:
        # Update tab cell + status
        client.values_update(f"'{TAB_PROJECTS}'!F{existing_row}", [[hyperlink]])
        if args.status:
            client.values_update(f"'{TAB_PROJECTS}'!C{existing_row}", [[args.status]])
        index_msg = f"updated row {existing_row} (existing entry)"

    trace("projects-create-gantt", args.project.lower().replace(" ", "-"), [
        f"- project: {args.project}",
        f"- entity: {args.entity} (color #{entity_hex})",
        f"- gantt tab: created with {args.weeks} weekly columns from {args.start}",
        f"- projects index: {index_msg}",
        f"- snapshot: {snap}",
    ])
    print(f'task-tracker-manager: created Gantt tab "{args.project}" ({args.weeks} weeks from {args.start}); Projects index {index_msg}')
    return 0


def cmd_reformat(args) -> int:
    """Re-apply conditional formatting on the canonical tabs. Idempotent.

    Strips existing rules and rebuilds. Safe to run more than once.
    """
    client = SheetsClient()
    meta = client.get_metadata()
    day_tabs = list(_iter_day_tabs(meta))
    if not day_tabs:
        sys.exit("task-tracker-manager: no day tabs present — run scripts/build_day_tabs.py first")
    todo_sid = find_tab(meta, TAB_TODO)["sheetId"] if find_tab(meta, TAB_TODO) else None
    pj_sid = find_tab(meta, TAB_PROJECTS)["sheetId"] if find_tab(meta, TAB_PROJECTS) else None

    snap = snapshot_ranges(client, "reformat", [
        day_tab_block(n, DAY_COL_STATUS, DAY_COL_LAST, 1, DAY_GRID_ROWS)
        for n, _ in day_tabs
    ])

    R: list[dict] = []

    # NOTE: addConditionalFormatRule is additive — duplicate rules may stack.
    # Idempotency is "safe to re-run", not "dedupes". Manual cleanup in UI if
    # rules accumulate (documented in SKILL.md).

    # Per day tab: slot rule =$A13=TRUE over A13:E27, habit rule =$A4=TRUE over A4:E10.
    for day_name, props in day_tabs:
        sid = props["sheetId"]
        # Slot rule: status TRUE → strikethrough + sage-extra-light across A:E.
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": sid,
                            "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                            "endRowIndex": DAY_SLOT_LAST_ROW,
                            "startColumnIndex": DAY_COL_STATUS,
                            "endColumnIndex": DAY_COL_LAST + 1}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue":
                                              f"=$A{DAY_SLOT_FIRST_ROW}=TRUE"}]},
                    "format": {
                        "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                        "textFormat": {"strikethrough": True,
                                       "foregroundColor": hex_to_rgb(MUTED_HEX)},
                    },
                },
            },
            "index": 0,
        }})
        # Habit rule: status TRUE → sage-extra-light fill across A:E.
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": sid,
                            "startRowIndex": DAY_HABIT_FIRST_ROW - 1,
                            "endRowIndex": DAY_HABIT_LAST_ROW,
                            "startColumnIndex": DAY_COL_STATUS,
                            "endColumnIndex": DAY_COL_LAST + 1}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue":
                                              f"=$A{DAY_HABIT_FIRST_ROW}=TRUE"}]},
                    "format": {"backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX)},
                },
            },
            "index": 0,
        }})

    # To Do tab CF — Status is now a 3-state dropdown string (2026-05-17).
    # Completed → strikethrough + sage-light. On-going → subtle sage fill (no
    # strikethrough) so in-progress items read differently from done + not-started.
    if todo_sid is not None:
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": todo_sid,
                            "startRowIndex": 1, "endRowIndex": TODO_MAX_ROWS,
                            "startColumnIndex": 0, "endColumnIndex": len(TODO_HEADERS)}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": '=$A2="Completed"'}]},
                    "format": {
                        "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                        "textFormat": {"strikethrough": True,
                                       "foregroundColor": hex_to_rgb(MUTED_HEX)},
                    },
                },
            },
            "index": 0,
        }})
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": todo_sid,
                            "startRowIndex": 1, "endRowIndex": TODO_MAX_ROWS,
                            "startColumnIndex": 0, "endColumnIndex": len(TODO_HEADERS)}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": '=$A2="On-going"'}]},
                    "format": {"backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX)},
                },
            },
            "index": 0,
        }})

    if R:
        client.batch_update(R)
    trace("reformat", "rules-reapplied", [
        f"- applied {len(R)} conditional-format rules",
        f"- snapshot: {snap}",
    ])
    print(f"task-tracker-manager: reformatted ({len(R)} conditional-format rule(s) applied)")
    return 0


def cmd_report(args) -> int:
    client = SheetsClient()
    meta = client.get_metadata()
    today = date.today()
    today_iso = today.isoformat()

    overdue = []
    unscheduled = []
    long_term = []
    todo_rows = client.get_values(
        f"'{TAB_TODO}'!A2:{col_letter(TODO_COL_HORIZON)}{TODO_MAX_ROWS}")
    for i, row in enumerate(todo_rows):
        r = 2 + i  # 1-based
        status = row[TODO_COL_STATUS] if len(row) > TODO_COL_STATUS else ""
        task = row[TODO_COL_TASK] if len(row) > TODO_COL_TASK else ""
        horizon = (row[TODO_COL_HORIZON] if len(row) > TODO_COL_HORIZON else "").strip()
        if not task:
            continue
        # Recurring templates are not tasks — never overdue/unscheduled.
        if _todo_is_recurring(horizon):
            continue
        if _todo_is_done(status):
            continue
        if horizon == "Long Term":
            long_term.append(f"  - row {r}: {task}")
            continue
        due = row[TODO_COL_DUE] if len(row) > TODO_COL_DUE else ""
        if due:
            due_str = str(due)[:10]
            if due_str < today_iso:
                overdue.append(f"  - row {r}: {task} (due {due_str})")
        else:
            unscheduled.append(f"  - row {r}: {task}")

    # Per-day carryover + capacity across the 7 permanent day tabs.
    # Carryover = slots where Task non-empty AND status FALSE, grouped by day.
    day_tabs = list(_iter_day_tabs(meta))
    carryover_lines: list[str] = []
    empty_slots_lines: list[str] = []
    carryover_total = 0
    tomorrow_tab = DAY_LABELS[(today.weekday() + 1) % 7]
    for day_name, _props in day_tabs:
        status_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_STATUS, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
        task_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
        empty = 0
        day_incomplete: list[str] = []
        for si in range(DAY_SLOT_COUNT):
            st = status_vals[si][0] if si < len(status_vals) and status_vals[si] else ""
            tk = task_vals[si][0] if si < len(task_vals) and task_vals[si] else ""
            tk_text = (tk or "").strip() if isinstance(tk, str) else ""
            if not tk_text:
                empty += 1
                continue
            if not _is_truthy(st):
                day_incomplete.append(f"slot {si + 1}: {tk_text}")
        if day_incomplete:
            carryover_lines.append(f"  - {day_name} ({len(day_incomplete)} incomplete):")
            for it in day_incomplete:
                carryover_lines.append(f"    - {it}")
            carryover_total += len(day_incomplete)
        marker = "  ← tomorrow" if day_name == tomorrow_tab else ""
        empty_slots_lines.append(
            f"  - {day_name}: {empty}/{DAY_SLOT_COUNT} empty{marker}")

    # Stale projects: read Projects + check Gantt tab for any ticks in last 14 days — heuristic
    # is week-cell TRUE in any column whose header date is within 14 days of today.
    stale_projects = []
    pj_rows = client.get_values(f"'{TAB_PROJECTS}'!A2:G{PJ_MAX_ROWS}")
    for row in pj_rows:
        if len(row) < 3 or not row[0]:
            continue
        if (row[2] if len(row) > 2 else "") == "Done":
            continue
        # Skip — full stale-detection needs reading each Gantt tab; defer to friday review
        # Just surface the project name if Status != Done
        # (Will be filled in by future enhancement)

    lines = [f"## Tracker health ({today_iso})", ""]
    lines.append(f"**Overdue ({len(overdue)}):**")
    lines.extend(overdue if overdue else ["  - none"])
    lines.append("")
    lines.append(f"**Unscheduled / no due date ({len(unscheduled)}):**")
    lines.extend(unscheduled[:10] if unscheduled else ["  - none"])
    if len(unscheduled) > 10:
        lines.append(f"  - … and {len(unscheduled) - 10} more")
    lines.append("")
    lines.append(f"**Long Term ({len(long_term)}):**")
    lines.extend(long_term[:10] if long_term else ["  - none"])
    if len(long_term) > 10:
        lines.append(f"  - … and {len(long_term) - 10} more")
    lines.append("")
    lines.append(f"**Carryover — incomplete day-tab slots ({carryover_total}):**")
    lines.extend(carryover_lines if carryover_lines else ["  - none"])
    lines.append("  _(manual carryover — Kay approves each move; no auto-carry)_")
    lines.append("")
    lines.append("**Priority slot capacity (per day tab):**")
    lines.extend(empty_slots_lines if empty_slots_lines
                 else ["  - (no day tabs found — run scripts/build_day_tabs.py)"])
    lines.append("")
    lines.append(f"**Sheet:** {TRACKER_SHEET_URL}")

    print("\n".join(lines))
    return 0


def cmd_move_day_item(args) -> int:
    """Move/copy a priority-slot item between day tabs (manual carryover).

    --from {day} --slot N --to {day} [--slot M] --state {completed|incomplete|added|deleted}

    - completed  : copy src→dst, dst status TRUE
    - incomplete : copy src→dst, dst status FALSE
    - added      : write dst only (src ignored — new item, --task required)
    - deleted    : clear src only (no dst write)
    Copies Task/Type/Project/Notes. Collision-refuse on dst (occupied slot,
    unless --force). Always snapshots src+dst, always traces.
    """
    state = args.state
    if state not in ("completed", "incomplete", "added", "deleted"):
        sys.exit("task-tracker-manager: --state must be completed|incomplete|added|deleted")

    client = SheetsClient()
    meta = client.get_metadata()

    src_name = _resolve_day_tab_name(args.from_day) if args.from_day else None
    dst_name = _resolve_day_tab_name(args.to_day) if args.to_day else None

    snap_targets: list[str] = []
    src_block = dst_block = None
    src_row = dst_row = None

    if state != "added":
        if not src_name or args.slot is None:
            sys.exit("task-tracker-manager: --from + --slot required for "
                     "completed/incomplete/deleted")
        if find_day_tab(meta, src_name) is None:
            sys.exit(f"task-tracker-manager: source day tab '{src_name}' not found")
        if not (1 <= args.slot <= DAY_SLOT_COUNT):
            sys.exit(f"task-tracker-manager: --slot must be 1..{DAY_SLOT_COUNT}")
        src_row = DAY_SLOT_FIRST_ROW + args.slot - 1
        src_block = day_tab_block(src_name, DAY_COL_STATUS, DAY_COL_LAST, src_row, src_row)
        snap_targets.append(src_block)

    if state != "deleted":
        if not dst_name:
            sys.exit("task-tracker-manager: --to required for "
                     "completed/incomplete/added")
        if find_day_tab(meta, dst_name) is None:
            sys.exit(f"task-tracker-manager: dest day tab '{dst_name}' not found")
        dst_slot = args.to_slot if args.to_slot is not None else (
            args.slot if state != "added" else None)
        if dst_slot is None:
            # auto-pick first empty slot on dst
            col_vals = client.get_values(
                day_tab_range(dst_name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW))
            dst_slot = next((i + 1 for i in range(DAY_SLOT_COUNT)
                             if not (col_vals[i][0] if i < len(col_vals) and col_vals[i] else "")),
                            None)
            if dst_slot is None:
                sys.exit(f"task-tracker-manager: refused move-day-item — {dst_name} has no empty slots")
        if not (1 <= dst_slot <= DAY_SLOT_COUNT):
            sys.exit(f"task-tracker-manager: dest --slot must be 1..{DAY_SLOT_COUNT}")
        dst_row = DAY_SLOT_FIRST_ROW + dst_slot - 1
        dst_block = day_tab_block(dst_name, DAY_COL_STATUS, DAY_COL_LAST, dst_row, dst_row)
        snap_targets.append(dst_block)

    # Resolve payload (Task/Type/Project/Notes)
    if state == "added":
        if not args.task:
            sys.exit("task-tracker-manager: --task required for --state added")
        payload = [args.task, getattr(args, "type", "") or "",
                   getattr(args, "project", "") or "", getattr(args, "notes", "") or ""]
    else:
        src_vals = client.get_values(src_block)
        sr = src_vals[0] if src_vals and src_vals[0] else []
        task = (sr[DAY_COL_TASK] if len(sr) > DAY_COL_TASK else "") or ""
        if not str(task).strip():
            sys.exit(f"task-tracker-manager: source {src_name} slot {args.slot} is empty")
        payload = [task,
                   (sr[DAY_COL_TYPE] if len(sr) > DAY_COL_TYPE else "") or "",
                   (sr[DAY_COL_PROJECT] if len(sr) > DAY_COL_PROJECT else "") or "",
                   (sr[DAY_COL_NOTES] if len(sr) > DAY_COL_NOTES else "") or ""]

    # Collision-refuse on dst
    if dst_block is not None:
        dst_existing = client.get_values(
            day_tab_range(dst_name, DAY_COL_TASK, dst_row))
        de = (dst_existing[0][0] if dst_existing and dst_existing[0] else "")
        if de and not args.force:
            sys.exit(f'task-tracker-manager: refused move-day-item — {dst_name} slot '
                     f'{dst_row - DAY_SLOT_FIRST_ROW + 1} already contains "{de}" '
                     f'(use --force to overwrite)')

    snap = snapshot_ranges(client, "move-day-item", snap_targets)

    # Apply writes
    if dst_block is not None:
        status_bool = (state == "completed")
        client.values_update(dst_block, [[status_bool] + payload])
    if state == "deleted" or (state in ("completed", "incomplete") and src_block is not None):
        # For completed/incomplete this is a MOVE — clear source after copy.
        client.batch_update([{
            "repeatCell": {
                "range": {"sheetId": find_day_tab(meta, src_name)["sheetId"],
                          "startRowIndex": src_row - 1, "endRowIndex": src_row,
                          "startColumnIndex": DAY_COL_STATUS,
                          "endColumnIndex": DAY_COL_LAST + 1},
                "cell": {"userEnteredValue": {"stringValue": ""}},
                "fields": "userEnteredValue",
            }
        }, {
            "updateCells": {
                "rows": [{"values": [{"userEnteredValue": {"boolValue": False}}]}],
                "fields": "userEnteredValue",
                "start": {"sheetId": find_day_tab(meta, src_name)["sheetId"],
                          "rowIndex": src_row - 1, "columnIndex": DAY_COL_STATUS},
            }
        }])

    desc = {
        "completed": f"moved {src_name} slot {args.slot} → {dst_name} (done)",
        "incomplete": f"moved {src_name} slot {args.slot} → {dst_name} (carry)",
        "added": f"added new item → {dst_name}",
        "deleted": f"deleted {src_name} slot {args.slot}",
    }[state]
    trace("move-day-item", f"{state}-{(src_name or dst_name).lower()}", [
        f"- state: {state}",
        f"- {desc}",
        f"- task: {payload[0]}",
        f"- snapshot: {snap}",
    ])
    print(f'task-tracker-manager: move-day-item ({state}) — {desc}: "{payload[0]}"')
    return 0


def cmd_gantt_tick(args) -> int:
    client = SheetsClient()
    meta = client.get_metadata()
    if find_tab(meta, args.project) is None:
        sys.exit(f"task-tracker-manager: project tab {args.project!r} not found")
    cell_ref = f"{args.week_col}{args.milestone_row}"
    snap = snapshot_ranges(client, "gantt-tick", [f"'{args.project}'!{cell_ref}"])
    client.values_update(f"'{args.project}'!{cell_ref}", [[True]])
    print(f'task-tracker-manager: ticked {args.project} {cell_ref}')
    return 0


def cmd_migrate(args) -> int:
    """One-shot 2026-05-17 cutover from the single Live Week grid to 7 day tabs.

    SAFETY: this verb NEVER performs the destructive teardown (delete/hide of the
    old `Today` / `May 11-17` tabs) by itself. The destructive steps are run by a
    human supervisor following the printed ordered command list. Without
    --execute-nondestructive this is pure dry-run reporting.

    Non-destructive steps it WILL run with --execute-nondestructive:
      (a) snapshot the full pre-migration state to one rollback JSON
      (b) run sync-done-status against the OLD `May 11-17` grid (pre-teardown)
          via the deprecated single-grid code path, then archive-todo
    It will then PRINT the remaining ordered steps for the human to run.
    """
    client = SheetsClient()
    meta = client.get_metadata()
    old_grid = find_live_week_tab(meta)
    today_tab = find_tab(meta, "Today")
    donut = find_tab(meta, TAB_DONUT_DATA)
    day_tabs_present = [n for n, _ in _iter_day_tabs(meta)]

    print("task-tracker-manager: migrate (cutover 2026-05-17)")
    print(f"  Old Live Week grid: "
          f"{old_grid['title']!r} (sheetId={old_grid['sheetId']})" if old_grid
          else "  Old Live Week grid: NOT FOUND")
    print(f"  Retired 'Today' tab present: {today_tab is not None} "
          f"(sheetId={today_tab['sheetId'] if today_tab else 'n/a'})")
    print(f"  _donut_data present: {donut is not None}")
    print(f"  Day tabs already present: {day_tabs_present or '(none)'}")

    if not getattr(args, "execute_nondestructive", False):
        print("  [DRY RUN] no writes. Pass --execute-nondestructive to run "
              "snapshot + pre-teardown sync (still NO destructive teardown).")
    else:
        # (a) full pre-migration snapshot
        snap_ranges = []
        if old_grid:
            snap_ranges.append(f"'{old_grid['title']}'!A1:O50")
        if today_tab:
            snap_ranges.append("'Today'!A1:H48")
        if donut:
            snap_ranges.append(f"'{TAB_DONUT_DATA}'!A1:C10")
        for t in (TAB_TODO, TAB_RECURRING_TEMPLATE, TAB_PROJECTS,
                  TAB_TODO_LONG_TERM, TAB_COMPLETED_TODO):
            if find_tab(meta, t):
                snap_ranges.append(f"'{t}'!A1:H{TODO_MAX_ROWS}")
        for s in meta.get("sheets", []):
            title = s["properties"]["title"]
            if title in ("Deal Aggregator Expansion", "Myself Renewed Healthcare"):
                snap_ranges.append(f"'{title}'!A1:Z40")
        snap = snapshot_ranges(client, "migrate", snap_ranges)
        print(f"  [DONE] pre-migration snapshot: {snap}")
        # (b) pre-teardown sync against OLD grid + archive-todo
        if old_grid:
            print("  [RUN] sync-done-status against OLD grid (deprecated path)…")
            rc = _legacy_sync_old_grid(client, meta, old_grid["title"])
            print(f"  [DONE] legacy sync rc={rc}; now run archive-todo manually "
                  "(see ordered list).")
        else:
            print("  [SKIP] no old grid — sync not applicable.")

    print()
    print("  ORDERED MANUAL STEPS (human supervisor, destructive — NOT run here):")
    print("   1. (done above if --execute-nondestructive) snapshot + legacy sync")
    print("   2. python3 scripts/task_tracker.py archive-todo   # sweep ✅ → Completed To Do")
    print("   3. python3 scripts/build_day_tabs.py               # create 7 day tabs (idempotent)")
    print("   4. python3 scripts/build_day_tabs.py --donuts-only # _donut_data rebuild + 7 charts")
    print("   5. (in Sheet UI / Sheets API) duplicate `May 11-17` → `archive_May 11-17` far-right")
    print("   6. (in Sheet UI / Sheets API) delete or hide retired `Today` (sheetId 433823170)")
    print("      and the old `May 11-17` Live Week tab AFTER the archive exists")
    print("   7. python3 scripts/task_tracker.py report          # confirm 7 day tabs, carryover surfaced")
    print("   8. Kay walks carryover in /goodmorning; approved moves via move-day-item / promote")
    print("  task-tracker-manager: migrate report complete")
    return 0


def _legacy_sync_old_grid(client, meta, week_title) -> int:
    """Run the OLD single-grid sync-done-status against `week_title` (pre-teardown
    only). Uses the deprecated LIVE_* day-pair constants intentionally — this is
    the one place the old grid is still read, exactly as the plan's migration
    step 2 requires."""
    weekly_checked = []
    for day_idx in range(7):
        sc = col_letter(LIVE_DAY_STAT[day_idx])
        tc = col_letter(LIVE_DAY_TASK[day_idx])
        status_vals = client.get_values(
            f"'{week_title}'!{sc}{LIVE_SLOT_FIRST_ROW}:{sc}{LIVE_SLOT_LAST_ROW}")
        task_vals = client.get_values(
            f"'{week_title}'!{tc}{LIVE_SLOT_FIRST_ROW}:{tc}{LIVE_SLOT_LAST_ROW}")
        for si in range(15):
            st = status_vals[si][0] if si < len(status_vals) and status_vals[si] else ""
            tk = task_vals[si][0] if si < len(task_vals) and task_vals[si] else ""
            txt = (tk or "").strip() if isinstance(tk, str) else ""
            if txt and _is_truthy(st):
                weekly_checked.append(txt)
    todo_rows = client.get_values(f"'{TAB_TODO}'!A2:F{TODO_MAX_ROWS}")
    by_task: dict[str, list[int]] = {}
    truthy: dict[int, bool] = {}
    for i, row in enumerate(todo_rows):
        t = row[1] if len(row) > 1 else ""
        if not isinstance(t, str) or not t.strip():
            continue
        by_task.setdefault(t.strip(), []).append(2 + i)
        truthy[2 + i] = _is_truthy(row[0] if row else "")
    flips = []
    for txt in set(weekly_checked):
        m = by_task.get(txt)
        if m and len(m) == 1 and not truthy[m[0]]:
            flips.append(m[0])
    if not flips:
        print("  [legacy-sync] 0 To Do rows to flip")
        return 0
    snap = snapshot_ranges(client, "migrate-legacy-sync",
                           [f"'{TAB_TODO}'!A2:A{TODO_MAX_ROWS}"])
    todo_sid = find_tab(meta, TAB_TODO)["sheetId"]
    client.batch_update([{
        "updateCells": {
            "rows": [{"values": [{"userEnteredValue": {"boolValue": True}}]}],
            "fields": "userEnteredValue",
            "start": {"sheetId": todo_sid, "rowIndex": r - 1, "columnIndex": TODO_COL_STATUS},
        }} for r in flips])
    print(f"  [legacy-sync] flipped {len(flips)} To Do row(s); snapshot {snap}")
    return 0


# --------------------------------------------------------------- argparse

def main():
    p = argparse.ArgumentParser(prog="task_tracker")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("append")
    a.add_argument("--task", required=True)
    a.add_argument("--type", required=True, choices=TYPE_OPTIONS)
    a.add_argument("--project", default="")
    a.add_argument("--due", default="")
    a.add_argument("--notes", default="")
    a.add_argument("--horizon", default="Short Term", choices=HORIZON_OPTIONS,
                   help="item classification (default Short Term)")
    a.set_defaults(func=cmd_append)

    pr = sub.add_parser("promote",
                        help="Move a To Do row into a day TAB's priority slot (day-tab model).")
    pr.add_argument("--todo-row", type=int, required=True)
    pr.add_argument("--day", required=True, help="Sun..Sat / Mon..Sun")
    pr.add_argument("--slot", type=int, required=True, help="1..15")
    pr.set_defaults(func=cmd_promote)

    bw = sub.add_parser("build-week",
                        help="Sunday rebuild ceremony — archive + clear + re-title "
                             "the WEEK PLANNING TAB + stamp Recurring onto it. "
                             "Day tabs untouched (use distribute-week after).")
    bw.add_argument("--skip-recurring", action="store_true",
                    help="bypass the Recurring Template stamp step (rare)")
    bw.add_argument("--dry-run", action="store_true",
                    help="report what would happen without writing — no archive, no clear, no stamp")
    bw.set_defaults(func=cmd_build_week)

    dw = sub.add_parser("distribute-week",
                        help="Fan the finalized Week planning tab OUT into the 7 "
                             "day tabs (collision-aware; snapshot+trace).")
    dw.add_argument("--dry-run", action="store_true",
                    help="report what would be written + collisions; no writes")
    dw.add_argument("--force", action="store_true",
                    help="overwrite occupied day-tab slots that the Week plan changes")
    dw.add_argument("--day", default=None,
                    help="limit to one day tab (Sun..Sat / Mon..Sun); default all 7")
    dw.set_defaults(func=cmd_distribute_week)

    # DEPRECATED alias: archive → build-week (prints deprecation notice).
    ar = sub.add_parser("archive",
                        help="DEPRECATED 2026-05-17 — alias of build-week.")
    ar.add_argument("--skip-recurring", action="store_true")
    ar.add_argument("--dry-run", action="store_true")
    ar.set_defaults(func=cmd_archive)

    mdi = sub.add_parser("move-day-item",
                         help="Move/copy a slot item between day tabs (manual carryover).")
    mdi.add_argument("--from", dest="from_day", default=None,
                     help="source day tab (Sun..Sat); required unless --state added")
    mdi.add_argument("--slot", type=int, default=None,
                     help="source slot 1..15 (also dest slot if --to-slot omitted)")
    mdi.add_argument("--to", dest="to_day", default=None,
                     help="dest day tab (Sun..Sat); required unless --state deleted")
    mdi.add_argument("--to-slot", type=int, default=None,
                     help="dest slot 1..15; omit to auto-pick first empty")
    mdi.add_argument("--state", required=True,
                     choices=["completed", "incomplete", "added", "deleted"])
    mdi.add_argument("--task", default=None, help="required for --state added")
    mdi.add_argument("--type", default="")
    mdi.add_argument("--project", default="")
    mdi.add_argument("--notes", default="")
    mdi.add_argument("--force", action="store_true",
                     help="overwrite an occupied dest slot")
    mdi.set_defaults(func=cmd_move_day_item)

    mg = sub.add_parser("migrate",
                        help="2026-05-17 one-shot cutover (dry-run by default; "
                             "never runs destructive teardown).")
    mg.add_argument("--execute-nondestructive", action="store_true",
                    help="run snapshot + pre-teardown legacy sync (still NO teardown)")
    mg.set_defaults(func=cmd_migrate)

    ra = sub.add_parser("recurring-add",
                        help="Append a row to the Recurring Template tab (stamped onto every new week by `build-week`).")
    ra.add_argument("--day", required=True, help="Mon..Sun")
    ra.add_argument("--task", required=True)
    ra.add_argument("--type", required=True, choices=TYPE_OPTIONS)
    ra.add_argument("--project", default="")
    ra.add_argument("--slot", type=int, default=None,
                    help="1..15; omit for auto-pick first empty slot on that day")
    ra.add_argument("--notes", default="")
    ra.set_defaults(func=cmd_recurring_add)

    rr = sub.add_parser("recurring-remove",
                        help="Clear a row from the Recurring Template tab (snapshot rollback retained).")
    rr.add_argument("--row", type=int, required=True,
                    help="row number to remove (2 is the first data row)")
    rr.set_defaults(func=cmd_recurring_remove)

    at = sub.add_parser("archive-todo")
    at.add_argument("--skip-sync", action="store_true",
                    help="skip the auto sync-done-status pre-step (rare)")
    at.set_defaults(func=cmd_archive_todo)

    sds_sync = sub.add_parser(
        "sync-done-status",
        help="Reconcile checked weekly slots → matching To Do rows by exact task-text match.",
    )
    sds_sync.add_argument("--dry-run", action="store_true",
                          help="report what would change without writing")
    sds_sync.set_defaults(func=cmd_sync_done_status)

    sds = sub.add_parser("schedule-to-day-slot",
                          help="Direct write to a day TAB's priority slot (day-tab model).")
    sds.add_argument("--task", required=True)
    sds.add_argument("--day", required=True, help="Sun..Sat / Mon..Sun")
    sds.add_argument("--slot", type=int, default=None,
                     help="1..15; if omitted, auto-pick first empty slot")
    sds.add_argument("--type", default="", help="Work / Home (optional)")
    sds.add_argument("--project", default="", help="optional")
    sds.add_argument("--notes", default="", help="optional")
    sds.add_argument("--force", action="store_true",
                     help="overwrite even if occupied")
    sds.set_defaults(func=cmd_schedule_to_day_slot)

    pcg = sub.add_parser("projects-create-gantt")
    pcg.add_argument("--project", required=True)
    pcg.add_argument("--entity", required=True,
                     help="Home | G&B | Myself Renewed | Kai Grey | Panthera Grey")
    pcg.add_argument("--status", default="Active",
                     help="Status column on Projects index (default: Active)")
    pcg.add_argument("--start", required=True, help="ISO date YYYY-MM-DD")
    pcg.add_argument("--target", required=True, help="ISO date YYYY-MM-DD")
    pcg.add_argument("--weeks", type=int, default=16,
                     help="number of weekly columns (4..30; default 16)")
    pcg.add_argument("--notes", default="")
    pcg.set_defaults(func=cmd_projects_create_gantt)

    rf = sub.add_parser("reformat")
    rf.set_defaults(func=cmd_reformat)

    rp = sub.add_parser("report")
    rp.set_defaults(func=cmd_report)

    gt = sub.add_parser("gantt-tick")
    gt.add_argument("--project", required=True)
    gt.add_argument("--milestone-row", type=int, required=True)
    gt.add_argument("--week-col", required=True)
    gt.set_defaults(func=cmd_gantt_tick)

    args = p.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
