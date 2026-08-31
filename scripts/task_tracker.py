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

Auth: gog refresh token from ~/.config/gogcli/credentials.json, with
GOG_KEYRING_PASSWORD resolved through scripts/op-env.sh before gog calls. API
quota retried with exponential backoff. Affected ranges snapshotted to
brain/context/rollback-snapshots/tasks-{verb}-{timestamp}.json before each write.
"""

from __future__ import annotations

import argparse
from types import SimpleNamespace
import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path

import requests

# --------------------------------------------------------------- file paths

_SCRIPT_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SCRIPT_DIR.parent
SNAPSHOT_DIR = _REPO_ROOT / "brain" / "context" / "rollback-snapshots"
SNAPSHOT_KEEP = 5

GOG_CREDS_PATH = Path.home() / ".config" / "gogcli" / "credentials.json"
GOG_ACCOUNT = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")
STRATEGIC_PLANNING_FOLDER_ID = "12IpnsQ5V_M1fiTm0NZM9wKhlerauILMd"
TO_DO_ARCHIVE_FOLDER_NAME = "To Do Archive"
WEEKLY_TEMPLATE_SHEET_ID = "1EaznKNTweSVRxbXpoEA2CyXLD8P96mWVU0K38-5pMxc"


def _run_gog(args: list[str], *, timeout: int = 30) -> subprocess.CompletedProcess:
    """Run gog with 1Password-backed environment loaded when needed."""
    command = "source scripts/op-env.sh >/dev/null 2>&1 || true; exec \"$@\""
    return subprocess.run(
        ["bash", "-lc", command, "gog-wrapper", "gog", *args],
        cwd=_REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
    )

# Sheet ID resolution — env override > resolver pointer > Drive search > migration fallback.
# Resolver lives in scripts/tracker_sheet_resolver.py (2026-05-26 refactor: weekly-files architecture).
def _resolve_tracker_sheet_id() -> str:
    env_id = os.environ.get("TRACKER_SHEET_ID")
    if env_id:
        return env_id
    try:
        sys.path.insert(0, str(Path(__file__).parent))
        from tracker_sheet_resolver import resolve_current_sheet_id
        return resolve_current_sheet_id()
    except Exception as e:
        print(f"task-tracker-manager: resolver fallback failed ({e}); "
              f"using migration default", file=sys.stderr)
        return "1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk"

TRACKER_SHEET_ID = _resolve_tracker_sheet_id()
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
TEMPLATE_PROJECT_PLACEHOLDER_TABS = {"PROJECT 1"}
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
TODO_COL_DAY = 7
TODO_HEADERS = ["Status", "Task", "Type", "Project", "Due", "Notes", "Horizon", "Day of the Week"]
DAY_OF_WEEK_OPTIONS = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
TODO_MAX_ROWS = 400

# 2026-05-17 consolidation: Status is a dropdown (was native checkbox);
# Horizon classifies the item + (for recurring) carries the target day.
# To Do Long Term + Recurring Weekly To Dos + Completed To Do tabs are retired —
# everything lives in the single `To Do` tab, filtered by Horizon.
STATUS_OPTIONS = ["Not Completed", "On-going", "Completed", "Dropped"]
STATUS_NOT_COMPLETED = "Not Completed"
STATUS_ONGOING = "On-going"
STATUS_COMPLETED = "Completed"
STATUS_DROPPED = "Dropped"
HORIZON_OPTIONS = [
    "Short Term", "Long Term",
    "Weekly Recurring Sun", "Weekly Recurring Mon", "Weekly Recurring Tue",
    "Weekly Recurring Wed", "Weekly Recurring Thu", "Weekly Recurring Fri",
    "Weekly Recurring Sat",
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
DAY_HABITS_HEADER_ROW = 4    # "HABITS" + "SUPPLEMENTAL"
DAY_HABIT_FIRST_ROW = 5      # rows 5..14 = 10 habit rows
DAY_HABIT_LAST_ROW = 14
DAY_FOCUS_LABEL_ROW = 16      # DAILY FOCUS label
DAY_FOCUS_VALUE_ROW = 17      # daily focus value
DAY_COL_HEADER_ROW = 20      # ✓ | Task | Type | Project | Notes
DAY_SLOT_FIRST_ROW = 21      # rows 21..70 = 50 priority slots
DAY_SLOT_LAST_ROW = 70
DAY_NOTES_HEADER_ROW = 71    # "NOTES"
DAY_NOTES_FIRST_ROW = 72     # rows 72..79 = free-notes block
DAY_NOTES_LAST_ROW = 79
DAY_GRID_ROWS = 82           # matches focus-section layout observed 2026-08-09
DAY_GRID_COLS = 12           # A..F content + G chart anchor headroom

# Per-day-tab columns (0-based)
DAY_COL_STATUS = 0   # A — native checkbox
DAY_COL_TASK = 1     # B — Task, 17pt
DAY_COL_TYPE = 2     # C — Type dropdown
DAY_COL_PROJECT = 3  # D — Project dropdown
DAY_COL_NOTES = 4    # E — Notes free text
DAY_COL_LAST = DAY_COL_NOTES
DAY_HEADERS = ["✓", "Task", "Type", "Project", "Notes"]
DAY_SLOT_COUNT = DAY_SLOT_LAST_ROW - DAY_SLOT_FIRST_ROW + 1  # 50
TOP_PRIORITY_SLOT_COUNT = 3  # fixed green-shaded priority band per day
DAY_HABIT_COUNT = DAY_HABIT_LAST_ROW - DAY_HABIT_FIRST_ROW + 1  # 10

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

# Week-tab grid layout (1-based rows for A1 references). Habits intentionally
# live only on the day tabs; Week is a task-planning mirror.
WK_TITLE_ROW = 1               # merged A1:O1 "WEEK OF May 17-23"
WK_SHOW_HABITS = False
WK_HABITS_HEADER_ROW = 0       # retired on Week tab
WK_HABIT_DAYHDR_ROW = 0        # retired on Week tab
WK_HABIT_FIRST_ROW = 0         # retired on Week tab
WK_HABIT_LAST_ROW = 0          # retired on Week tab
WK_FOCUS_ROW = 3               # DAILY FOCUS / THEME
WK_DAYHDR_ROW = 6              # SUNDAY..SATURDAY 2-col-merged headers
WK_SLOT_FIRST_ROW = 8          # rows 8..22 = 15 visible planning slots
WK_SLOT_LAST_ROW = 32
WK_NOTES_HDR_ROW = 34          # notes label row
WK_NOTES_FIRST_ROW = 35        # rows 35..37 = optional notes space
WK_NOTES_LAST_ROW = 37
WK_GRID_ROWS = 38
WK_GRID_COLS = 15              # col0 label + 7 day-pairs (status + content)
WK_SLOT_COUNT = WK_SLOT_LAST_ROW - WK_SLOT_FIRST_ROW + 1   # 25
WK_HABIT_COUNT = 0

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


# --------------------------------------------------------------- auth + API

class SheetsClient:
    """Per-sheet API client. Constructor accepts `sheet_id` so Phase 3 cmd_build_week
    can hold two clients simultaneously (prior file + new file) for cross-file carryover.

    Defaults to module-level TRACKER_SHEET_ID (resolver-driven). For long-running
    processes that need a fresh resolve, use `SheetsClient.current()`.
    """
    def __init__(self, sheet_id: str | None = None):
        self.sheet_id = sheet_id or TRACKER_SHEET_ID
        self.token = _get_access_token()
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    @classmethod
    def current(cls) -> "SheetsClient":
        """Fresh-resolve the current sheet ID via the resolver (bypasses module-load cache)."""
        try:
            sys.path.insert(0, str(Path(__file__).parent))
            from tracker_sheet_resolver import resolve_current_sheet_id
            return cls(resolve_current_sheet_id())
        except Exception:
            return cls(TRACKER_SHEET_ID)

    def _retry(self, fn):
        last = None
        last_response = None
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
                last_response = r
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
        if last_response is not None:
            raise RuntimeError(
                f"API retry exhausted with status {last_response.status_code}: "
                f"{last_response.text[:400]}"
            )
        raise RuntimeError("API retry exhausted without a response")

    def get_metadata(self) -> dict:
        return self._retry(lambda: self.session.get(
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}",
            params={"fields": "sheets(properties(sheetId,title,gridProperties,index)),namedRanges"},
            timeout=30,
        ))

    def get_values(self, range_a1: str) -> list[list]:
        data = self._retry(lambda: self.session.get(
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}/values/{range_a1}",
            params={"valueRenderOption": "UNFORMATTED_VALUE", "dateTimeRenderOption": "FORMATTED_STRING"},
            timeout=30,
        ))
        return data.get("values", [])

    def values_update(self, range_a1: str, values: list[list]) -> dict:
        return self._retry(lambda: self.session.put(
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}/values/{range_a1}",
            params={"valueInputOption": "USER_ENTERED"},
            json={"values": values},
            timeout=30,
        ))

    def values_append(self, range_a1: str, values: list[list]) -> dict:
        return self._retry(lambda: self.session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}/values/{range_a1}:append",
            params={"valueInputOption": "USER_ENTERED", "insertDataOption": "INSERT_ROWS"},
            json={"values": values},
            timeout=30,
        ))

    def values_clear(self, range_a1: str) -> dict:
        return self._retry(lambda: self.session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}/values/{range_a1}:clear",
            timeout=30,
        ))

    def batch_update(self, requests_list: list[dict]) -> dict:
        if not requests_list:
            return {}
        return self._retry(lambda: self.session.post(
            f"https://sheets.googleapis.com/v4/spreadsheets/{self.sheet_id}:batchUpdate",
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
        export = _run_gog(
            ["auth", "tokens", "export", GOG_ACCOUNT, "--out", str(tmp_path), "--overwrite"],
            timeout=15,
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
    snapshot = {"verb": verb, "timestamp": ts, "sheet_id": client.sheet_id, "ranges": {}}
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


# Verbs whose "trace" is a mechanical receipt of an instruction Kay already
# gave, not a decision between alternatives. Per decision-traces SKILL.md
# anti-pattern #6 these belong in brain/context/verb-logs/, never brain/traces/
# — they pollute calibration input. The 2026-06-04 calibration found 12 of 38
# traces in the prior batch were exactly these receipts (32% noise).
_RECEIPT_VERBS = {
    "compact-todo",
    "schedule-to-day-slot",
    "build-week",
    "build-week-v2",
    "carry-forward-day",
    "distribute-week",
    "reformat",
    "schedule-from-todo-days",
}


def trace(verb: str, slug: str, lines: list[str]) -> None:
    if verb in _RECEIPT_VERBS:
        # Mechanical receipt — route to verb-logs, preserve the rollback record
        # without polluting brain/traces/ (calibration input).
        log_verb_receipt(verb, slug, lines)
        return
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


def log_verb_receipt(verb: str, slug: str, lines: list[str]) -> None:
    """Mechanical verb receipt → brain/context/verb-logs/, NOT brain/traces/.
    Per decision-traces SKILL.md anti-pattern #6 — these are receipts of an
    instruction already given, not decisions, and they pollute calibration."""
    today_iso = date.today().isoformat()
    log_dir = _REPO_ROOT / "brain" / "context" / "verb-logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_path = log_dir / f"{today_iso}-task-tracker.log"
    with log_path.open("a") as f:
        ts = datetime.now().isoformat()
        f.write(f"\n[{ts}] {verb} — {slug}\n")
        for line in lines:
            f.write(f"  {line}\n")


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
        [f"'{TAB_TODO}'!A{target_row}:{col_letter(len(TODO_HEADERS) - 1)}{target_row}"])

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
        "",                # Day of the Week
    ]
    client.values_update(f"'{TAB_TODO}'!A{target_row}:{col_letter(len(TODO_HEADERS) - 1)}{target_row}", [row_values])

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


def _compact_todo(client: "SheetsClient", *, buffer: int = 40, dry_run: bool = False) -> dict:
    """Strip gap rows from the To Do tab and pack real rows to the top.

    A *real* row = Task (col B) non-empty. Everything else is a gap: leftover
    `FALSE` checkbox cells from the pre-2026-05-17 checkbox architecture, blank
    rows, stray empty-checkbox rows. These accumulate because `append` only fills
    the first empty row (never removes), and `build-week`'s Drive-copy carries the
    whole cluttered tab forward every Sunday.

    Rewrites header + real rows contiguously from row 2, physically deletes the
    surplus rows (keeping a small validated `buffer` for future appends), and
    re-applies Status/Type/Project/Horizon dropdown validation across the
    retained range so an old checkbox-validation row can't reintroduce a raw
    `FALSE`. The done-row CF (relative `$A2="Completed"`) is range-based and
    survives compaction untouched.

    Returns {"real", "removed", "kept_through", "deleted_rows"}.
    Caller owns snapshot + trace. Touches ONLY the To Do tab.
    """
    meta = client.get_metadata()
    todo = find_tab(meta, TAB_TODO)
    if todo is None:
        raise RuntimeError(f"'{TAB_TODO}' tab not found")
    todo_sid = todo["sheetId"]
    total_rows = todo.get("gridProperties", {}).get("rowCount", TODO_MAX_ROWS)
    ncol = len(TODO_HEADERS)
    last_col = col_letter(ncol - 1)

    all_vals = client.get_values(f"'{TAB_TODO}'!A1:{last_col}{total_rows}")
    header = all_vals[0] if all_vals else list(TODO_HEADERS)
    body = all_vals[1:] if len(all_vals) > 1 else []

    def _norm(r):
        r = list(r) + [""] * (ncol - len(r))
        return ["" if c is None else c for c in r[:ncol]]

    def _task(r):
        return (r[TODO_COL_TASK].strip() if len(r) > TODO_COL_TASK and r[TODO_COL_TASK] else "")

    real = [_norm(r) for r in body if _task(r)]
    n_real = len(real)
    n_removed = len(body) - n_real
    kept_through = 1 + n_real + max(0, buffer)  # 1-based last row to retain

    summary = {"real": n_real, "removed": n_removed,
               "kept_through": kept_through, "deleted_rows": 0, "dry_run": dry_run}
    if dry_run or n_removed == 0:
        return summary

    # 1) Write header + compacted real rows.
    client.values_update(f"'{TAB_TODO}'!A1:{last_col}{1 + n_real}", [_norm(header)] + real)

    # 2) Clear residual values below the compacted block (defensive, pre-delete).
    if (2 + n_real) <= total_rows:
        client.values_clear(f"'{TAB_TODO}'!A{2 + n_real}:{last_col}{total_rows}")

    reqs: list[dict] = []
    # 3) Physically delete surplus rows beyond the retained buffer (0-based, end-exclusive).
    if kept_through < total_rows:
        reqs.append({"deleteDimension": {
            "range": {"sheetId": todo_sid, "dimension": "ROWS",
                      "startIndex": kept_through, "endIndex": total_rows}}})
        summary["deleted_rows"] = total_rows - kept_through

    # 4) Re-apply dropdown validation across rows 2..kept_through so an old
    #    checkbox-validation gap row can't leak a raw FALSE back in.
    def _dv(col0, options):
        return {"setDataValidation": {
            "range": {"sheetId": todo_sid, "startRowIndex": 1, "endRowIndex": kept_through,
                      "startColumnIndex": col0, "endColumnIndex": col0 + 1},
            "rule": {"condition": {"type": "ONE_OF_LIST",
                                   "values": [{"userEnteredValue": o} for o in options]},
                     "showCustomUi": True, "strict": False}}}
    reqs += [
        _dv(TODO_COL_STATUS, STATUS_OPTIONS),
        _dv(TODO_COL_TYPE, TYPE_OPTIONS),
        _dv(TODO_COL_PROJECT, PROJECT_OPTIONS),
        _dv(TODO_COL_HORIZON, HORIZON_OPTIONS),
        _dv(TODO_COL_DAY, DAY_OF_WEEK_OPTIONS),
    ]
    client.batch_update(reqs)
    return summary


def cmd_compact_todo(args) -> int:
    """Remove empty/leftover gap rows from the To Do tab; pack real rows to top."""
    client = SheetsClient()
    buffer = getattr(args, "buffer", 40)
    dry_run = getattr(args, "dry_run", False)

    snap = None
    if not dry_run:
        meta = client.get_metadata()
        todo = find_tab(meta, TAB_TODO)
        total_rows = (todo.get("gridProperties", {}).get("rowCount", TODO_MAX_ROWS)
                      if todo else TODO_MAX_ROWS)
        snap = snapshot_ranges(client, "compact-todo",
            [f"'{TAB_TODO}'!A1:{col_letter(len(TODO_HEADERS) - 1)}{total_rows}"])

    try:
        s = _compact_todo(client, buffer=buffer, dry_run=dry_run)
    except RuntimeError as e:
        sys.exit(f"task-tracker-manager: {e}")

    if dry_run:
        print(f"task-tracker-manager: [dry-run] To Do has {s['real']} real rows; "
              f"{s['removed']} gap rows would be removed (keep through row {s['kept_through']}, "
              f"incl ~{buffer}-row append buffer)")
        return 0
    if s["removed"] == 0:
        print(f"task-tracker-manager: To Do already compact — {s['real']} rows, 0 gaps")
        return 0

    trace("compact-todo", "todo-gap-removal", [
        f"real rows kept: {s['real']}",
        f"gap rows removed: {s['removed']}",
        f"rows physically deleted: {s['deleted_rows']}",
        f"retained through row {s['kept_through']} (incl ~{buffer}-row append buffer)",
        f"snapshot: {snap}",
    ])
    print(f"task-tracker-manager: compacted To Do — kept {s['real']} real rows, "
          f"removed {s['removed']} gap rows ({s['deleted_rows']} rows deleted). snapshot: {snap}")
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
        f"'{TAB_TODO}'!A2:{col_letter(len(TODO_HEADERS) - 1)}{TODO_MAX_ROWS}")
    out: list[dict] = []
    for i, row in enumerate(rows):
        status = (row[TODO_COL_STATUS] if len(row) > TODO_COL_STATUS else "").strip() if row else ""
        task = (row[TODO_COL_TASK] if len(row) > TODO_COL_TASK else "").strip() if row else ""
        horizon = (row[TODO_COL_HORIZON] if len(row) > TODO_COL_HORIZON else "").strip() if row else ""
        if status != STATUS_ONGOING or not task or not _todo_is_recurring(horizon):
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
    # Habit status checkboxes (primary A, supplemental C, secondary supplemental E) → FALSE.
    for col, last_row in ((0, DAY_HABIT_LAST_ROW), (2, DAY_HABIT_LAST_ROW), (4, DAY_HABIT_FIRST_ROW + 4)):
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": DAY_HABIT_FIRST_ROW - 1, "endRowIndex": last_row,
                      "startColumnIndex": col, "endColumnIndex": col + 1},
            "cell": {"userEnteredValue": {"boolValue": False}},
            "fields": "userEnteredValue"}})
    # Slot status checkboxes (col A, rows 17..41) → FALSE
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_SLOT_FIRST_ROW - 1, "endRowIndex": DAY_SLOT_LAST_ROW,
                  "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_STATUS + 1},
        "cell": {"userEnteredValue": {"boolValue": False}},
        "fields": "userEnteredValue"}})
    # Slot Task/Type/Project/Notes (cols B..E, rows 17..41) → empty
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_SLOT_FIRST_ROW - 1, "endRowIndex": DAY_SLOT_LAST_ROW,
                  "startColumnIndex": DAY_COL_TASK, "endColumnIndex": DAY_COL_LAST + 1},
        "cell": {"userEnteredValue": {"stringValue": ""}},
        "fields": "userEnteredValue"}})
    # Top 3 priority slots retain fixed sage shading after the weekly clear.
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                  "endRowIndex": DAY_SLOT_FIRST_ROW - 1 + TOP_PRIORITY_SLOT_COUNT,
                  "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_LAST + 1},
        "cell": {"userEnteredFormat": {"backgroundColor": hex_to_rgb(SAGE_LIGHT_HEX)}},
        "fields": "userEnteredFormat.backgroundColor"}})

    # Free-notes block (cols A..E, rows 43..50) → empty
    reqs.append({"repeatCell": {
        "range": {"sheetId": sid,
                  "startRowIndex": DAY_NOTES_FIRST_ROW - 1, "endRowIndex": DAY_NOTES_LAST_ROW,
                  "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_LAST + 1},
        "cell": {"userEnteredValue": {"stringValue": ""}},
        "fields": "userEnteredValue"}})
    return reqs


def _week_clear_requests(sid: int) -> list[dict]:
    """Build repeatCell requests that reset the Week planning tab to a clean week:
    for each of the 7 day-columns — slot status checkboxes FALSE,
    slot task text empty, per-day notes block empty. Title row + headers + labels +
    dropdowns + CF + checkbox data-validation are PRESERVED (only userEnteredValue is touched)."""
    reqs: list[dict] = []
    for i in range(7):
        sc = wk_status_col(i)
        cc = wk_content_col(i)
        # Priority slot status checkboxes (Week task rows) → FALSE
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_SLOT_FIRST_ROW - 1, "endRowIndex": WK_SLOT_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": sc + 1},
            "cell": {"userEnteredValue": {"boolValue": False}},
            "fields": "userEnteredValue"}})
        # Priority slot task content (Week task rows) → empty
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_SLOT_FIRST_ROW - 1, "endRowIndex": WK_SLOT_LAST_ROW,
                      "startColumnIndex": cc, "endColumnIndex": cc + 1},
            "cell": {"userEnteredValue": {"stringValue": ""}},
            "fields": "userEnteredValue"}})
        # Per-day notes block (rows 51..58, day's status + content cols) → empty
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": WK_NOTES_FIRST_ROW - 1, "endRowIndex": WK_NOTES_LAST_ROW,
                      "startColumnIndex": sc, "endColumnIndex": cc + 1},
            "cell": {"userEnteredValue": {"stringValue": ""}},
            "fields": "userEnteredValue"}})
    return reqs


def _pull_carryover_to_week(client: "SheetsClient", dry_run: bool = False) -> dict:
    """Pull incomplete items from each day tab onto the new Week tab (step 6a — added 2026-05-26).

    An item on a day tab is "incomplete" if `Task` (col B) is non-empty AND `Status` (col A)
    checkbox is NOT TRUE. For each incomplete item, write the Task text into the next empty
    slot on the Week tab's day-block for that same day. Skips completed slots (Status TRUE)
    and empty slots. Collision-refuses against already-stamped recurring items (auto-picks
    the next empty slot below).

    Doctrine source: `memory/feedback_no_time_blocking_item_list_scheduling` + the 2026-05-26
    Kay directive: "when it plans the next week - it should pull incomplete tasks from the
    daily tabs and flow them into the week tab of the new week for my review."

    Returns: {"pulled": [{day, src_slot, dst_slot, task}], "refused": [...], "rows_read": int}
    """
    summary = {"pulled": [], "refused": [], "rows_read": 0}
    day_order = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

    for i, day_tab in enumerate(day_order):
        # Read day tab's priority slots (cols A=status, B=task, rows 17..41)
        rng = f"'{day_tab}'!A{DAY_SLOT_FIRST_ROW}:B{DAY_SLOT_LAST_ROW}"
        try:
            vals = client.get_values(rng) or []
        except Exception:
            vals = []
        summary["rows_read"] += len(vals)

        incompletes: list[tuple[int, str]] = []  # (src_slot_num, task)
        for slot_idx, row in enumerate(vals):
            slot_num = slot_idx + 1  # 1-indexed
            status = row[0] if len(row) > 0 else ""
            task = row[1] if len(row) > 1 else ""
            # Status TRUE → completed → skip
            status_is_true = (status is True) or (str(status).strip().upper() == "TRUE")
            task_str = str(task).strip() if task is not None else ""
            if task_str and not status_is_true:
                incompletes.append((slot_num, task_str))

        if not incompletes:
            continue

        # Read Week tab's day-block content col to identify already-occupied slots
        # AND collect the set of already-placed task texts (for dedup vs recurring stamps).
        wk_cc = wk_content_col(i)
        wk_col = col_letter(wk_cc)
        wk_rng = f"'{TAB_WEEK}'!{wk_col}{WK_SLOT_FIRST_ROW}:{wk_col}{WK_SLOT_LAST_ROW}"
        try:
            wk_vals = client.get_values(wk_rng) or []
        except Exception:
            wk_vals = []
        empty_slots: list[tuple[int, int]] = []
        placed_normalized: set[str] = set()
        for s in range(WK_SLOT_COUNT):
            wk_cell = ""
            if s < len(wk_vals) and len(wk_vals[s]) > 0:
                wk_cell = str(wk_vals[s][0]).strip()
            if not wk_cell:
                empty_slots.append((s + 1, WK_SLOT_FIRST_ROW + s))
            else:
                placed_normalized.add(wk_cell.lower())

        # Place each incomplete in the next empty Week-tab slot for this day.
        # Dedup: skip carryover items whose normalized text already exists on the Week tab
        # for this day (e.g., recurring items already stamped — avoid duplicates per
        # 2026-05-26 calibration).
        writes: list[tuple[str, str]] = []
        for src_slot, task in incompletes:
            if task.lower() in placed_normalized:
                summary["refused"].append({
                    "day": day_tab, "src_slot": src_slot, "task": task,
                    "reason": "already present on Week tab for this day (recurring stamp or duplicate)"
                })
                continue
            if not empty_slots:
                summary["refused"].append({
                    "day": day_tab, "src_slot": src_slot, "task": task,
                    "reason": "no empty slot on Week tab for this day (25 slots full)"
                })
                continue
            dst_slot, wk_row = empty_slots.pop(0)
            cell = f"'{TAB_WEEK}'!{wk_col}{wk_row}"
            writes.append((cell, task))
            placed_normalized.add(task.lower())
            summary["pulled"].append({
                "day": day_tab, "src_slot": src_slot,
                "dst_slot": dst_slot, "task": task
            })

        if not dry_run:
            for cell, task in writes:
                client.values_update(cell, [[task]])

    return summary


# =================================================================================
# Phase 3 (2026-05-26) — Weekly-files architecture: cross-file rollover helpers
# =================================================================================

def _drive_copy_file(src_file_id: str, new_title: str, parent_folder_id: str | None = None) -> str:
    """Drive-copy a sheet to a new file. Returns new file ID. Raises on failure."""
    cmd = ["drive", "copy", src_file_id, new_title, "--json"]
    if parent_folder_id:
        cmd += ["--parent", parent_folder_id]
    result = _run_gog(cmd, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(f"gog drive copy failed: {result.stderr.strip() or result.stdout.strip()}")
    try:
        data = json.loads(result.stdout) if result.stdout.strip() else {}
    except json.JSONDecodeError:
        raise RuntimeError(f"gog drive copy returned non-JSON: {result.stdout[:300]}")
    new_id = data.get("id") or (data.get("file") or {}).get("id")
    if not new_id:
        raise RuntimeError(f"gog drive copy returned no file ID: {json.dumps(data)[:300]}")
    return new_id


def _drive_move_file(file_id: str, parent_folder_id: str) -> None:
    """Move a file under a parent folder. Idempotent."""
    result = _run_gog(["drive", "move", file_id, "--parent", parent_folder_id], timeout=30)
    if result.returncode != 0:
        # Non-fatal — log warning
        print(f"task-tracker-manager: WARN drive move failed ({result.stderr.strip()})", file=sys.stderr)


def _drive_search_files(query: str) -> list[dict]:
    result = _run_gog(["drive", "search", query, "--raw-query", "--json"], timeout=30)
    if result.returncode != 0:
        return []
    try:
        data = json.loads(result.stdout) if result.stdout.strip() else []
    except json.JSONDecodeError:
        return []
    if isinstance(data, list):
        return data
    return data.get("files", []) or data.get("results", []) or []


def _find_existing_tracker_files(title: str) -> list[dict]:
    safe_title = title.replace("'", "\\'")
    query = (
        f"name = '{safe_title}' "
        "and mimeType = 'application/vnd.google-apps.spreadsheet' "
        "and trashed = false"
    )
    files = _drive_search_files(query)
    files.sort(key=lambda f: f.get("modifiedTime", ""), reverse=True)
    return files


def _find_to_do_archive_folder_id() -> str | None:
    """Find the To Do Archive folder by name. Returns ID or None."""
    files = _drive_search_files(
        f"name = '{TO_DO_ARCHIVE_FOLDER_NAME}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    )
    if not files:
        return None
    return files[0].get("id")


def _stamp_recurring_day_tabs(client: SheetsClient, meta: dict, dry_run: bool = False) -> dict:
    """Stamp every 'Weekly Recurring' To Do row onto the day tab matching its Horizon.

    Phase 3 replacement for _stamp_recurring_week. Target = day tabs (not Week tab),
    because in the weekly-files architecture the Week tab is formula-driven (live mirror
    of day tabs); recurring items are written to day tabs and the Week tab auto-reflects.

    Returns {stamped, refused, rows_read}.
    """
    summary = {"stamped": [], "refused": [], "rows_read": 0}
    rows = _read_recurring_template(client)
    summary["rows_read"] = len(rows)
    if not rows:
        return summary

    # In-memory view of each day tab's task column to detect occupied slots.
    day_grid: dict[str, list[str]] = {}
    for day_tab in DAY_TAB_NAMES:
        try:
            vals = client.get_values(f"'{day_tab}'!B{DAY_SLOT_FIRST_ROW}:B{DAY_SLOT_LAST_ROW}")
        except Exception:
            vals = []
        flat = [(v[0] if v else "") if isinstance(v, list) else "" for v in vals]
        while len(flat) < DAY_SLOT_LAST_ROW - DAY_SLOT_FIRST_ROW + 1:
            flat.append("")
        day_grid[day_tab] = flat

    writes: list[tuple[str, list[list]]] = []
    for r in rows:
        day_idx = DAY_BY_NAME[r["day"].lower()]
        tab_name = DAY_LABELS[day_idx]
        if tab_name not in day_grid:
            summary["refused"].append({"row": r["row"], "day": r["day"], "slot": r["slot"],
                                       "task": r["task"], "reason": f"unknown day tab {tab_name!r}"})
            continue

        target_slot = r["slot"]
        if target_slot is not None:
            existing = day_grid[tab_name][target_slot - 1]
            if existing and str(existing).strip():
                summary["refused"].append({
                    "row": r["row"], "day": r["day"], "slot": target_slot,
                    "task": r["task"], "reason": f'slot occupied by "{existing}"'})
                continue
            chosen_slot = target_slot
        else:
            chosen_slot = None
            for idx, v in enumerate(day_grid[tab_name]):
                if not v or not str(v).strip():
                    chosen_slot = idx + 1
                    break
            if chosen_slot is None:
                summary["refused"].append({"row": r["row"], "day": r["day"], "slot": None,
                                           "task": r["task"], "reason": f"{tab_name} day tab has no empty slots"})
                continue

        slot_row = DAY_SLOT_FIRST_ROW + chosen_slot - 1
        cell = f"'{tab_name}'!B{slot_row}"
        writes.append((cell, [[r["task"]]]))
        day_grid[tab_name][chosen_slot - 1] = r["task"]  # update in-memory so later carryover sees it
        summary["stamped"].append({"row": r["row"], "day": tab_name, "slot": chosen_slot, "task": r["task"]})

    if not dry_run:
        for cell, vals in writes:
            client.values_update(cell, vals)

    return summary


def _carryover_cross_file(prior_client: SheetsClient, new_client: SheetsClient, dry_run: bool = False) -> dict:
    """Read incomplete items from PRIOR file's day tabs, write to NEW file's same day tabs.

    Phase 3 replacement for _pull_carryover_to_week. Cross-file read + write.
    Dedup vs recurring stamps already placed on the new file's day tabs.

    Returns {pulled, refused, rows_read}.
    """
    summary = {"pulled": [], "refused": [], "rows_read": 0}

    for day_tab in DAY_TAB_NAMES:
        # Read PRIOR file's day tab slots
        rng = f"'{day_tab}'!A{DAY_SLOT_FIRST_ROW}:B{DAY_SLOT_LAST_ROW}"
        try:
            prior_vals = prior_client.get_values(rng) or []
        except Exception:
            prior_vals = []
        summary["rows_read"] += len(prior_vals)

        incompletes: list[tuple[int, str]] = []
        for slot_idx, row in enumerate(prior_vals):
            slot_num = slot_idx + 1
            status = row[0] if len(row) > 0 else ""
            task = row[1] if len(row) > 1 else ""
            status_true = (status is True) or (str(status).strip().upper() == "TRUE")
            task_str = str(task).strip() if task is not None else ""
            if task_str and not status_true:
                incompletes.append((slot_num, task_str))

        if not incompletes:
            continue

        # Read NEW file's day tab to find empty slots + already-placed recurring tasks for dedup
        try:
            new_vals = new_client.get_values(rng) or []
        except Exception:
            new_vals = []
        empty_slots: list[tuple[int, int]] = []
        placed_normalized: set[str] = set()
        slot_count = DAY_SLOT_LAST_ROW - DAY_SLOT_FIRST_ROW + 1
        for s in range(slot_count):
            wk_cell = ""
            if s < len(new_vals) and len(new_vals[s]) > 1:
                wk_cell = str(new_vals[s][1]).strip()
            if not wk_cell:
                empty_slots.append((s + 1, DAY_SLOT_FIRST_ROW + s))
            else:
                placed_normalized.add(wk_cell.lower())

        writes: list[tuple[str, list[list]]] = []
        for src_slot, task in incompletes:
            if task.lower() in placed_normalized:
                summary["refused"].append({
                    "day": day_tab, "src_slot": src_slot, "task": task,
                    "reason": "already present on new file's day tab (recurring stamp or duplicate)"
                })
                continue
            if not empty_slots:
                summary["refused"].append({
                    "day": day_tab, "src_slot": src_slot, "task": task,
                    "reason": "no empty slot on new file's day tab"
                })
                continue
            dst_slot, dst_row = empty_slots.pop(0)
            cell = f"'{day_tab}'!B{dst_row}"
            writes.append((cell, [[task]]))
            placed_normalized.add(task.lower())
            summary["pulled"].append({
                "day": day_tab, "src_slot": src_slot,
                "dst_slot": dst_slot, "task": task
            })

        if not dry_run:
            for cell, vals in writes:
                new_client.values_update(cell, vals)

    return summary


def _sync_combined_day_tasks_to_todo(day_client: SheetsClient, todo_client: SheetsClient | None = None,
                                     todo_meta: dict | None = None,
                                     dry_run: bool = False) -> dict:
    """Fold combined day-tab task text back into the To Do backend."""
    todo_client = todo_client or day_client
    meta = todo_meta or todo_client.get_metadata()
    if find_tab(meta, TAB_TODO) is None:
        return {"combined": [], "skipped": [{"reason": "To Do tab missing"}]}

    day_tasks: list[dict] = []
    for day_tab in DAY_TAB_NAMES:
        vals = day_client.get_values(f"'{day_tab}'!A{DAY_SLOT_FIRST_ROW}:E{DAY_SLOT_LAST_ROW}") or []
        for slot_i, row in enumerate(vals, start=1):
            status = row[DAY_COL_STATUS] if len(row) > DAY_COL_STATUS else ""
            task = row[DAY_COL_TASK] if len(row) > DAY_COL_TASK else ""
            task_text = str(task or "").strip()
            if not task_text or ":" not in task_text:
                continue
            prefix = task_text.split(":", 1)[0].strip()
            if len(prefix) >= 8:
                done = status is True or str(status).strip().upper() == "TRUE"
                day_tasks.append({"day": day_tab, "slot": slot_i, "task": task_text, "prefix": prefix, "done": done})

    todo_rows = todo_client.get_values(f"'{TAB_TODO}'!A2:{col_letter(len(TODO_HEADERS) - 1)}{TODO_MAX_ROWS}") or []
    combined: list[dict] = []
    skipped: list[dict] = []
    used_candidate_rows: set[int] = set()
    for d in day_tasks:
        prefix = d["prefix"]
        candidates = []
        for idx, row in enumerate(todo_rows, start=2):
            if idx in used_candidate_rows:
                continue
            task = row[TODO_COL_TASK] if len(row) > TODO_COL_TASK else ""
            task_text = str(task or "").strip()
            row_status = row[TODO_COL_STATUS] if len(row) > TODO_COL_STATUS else ""
            if str(row_status).strip() == "Completed" and not d["done"]:
                continue
            if task_text and task_text != d["task"] and task_text.lower().startswith((prefix + " ").lower()):
                candidates.append({"row": idx, "values": row, "task": task_text})
        if len(candidates) < 3:
            continue
        if any(len(c["task"]) > max(len(prefix) + 80, 120) for c in candidates):
            skipped.append({"day": d["day"], "slot": d["slot"], "task": d["task"],
                            "reason": "candidate task too long", "rows": [c["row"] for c in candidates]})
            continue

        keep = candidates[0]
        keep_vals = list(keep["values"]) + [""] * (len(TODO_HEADERS) - len(keep["values"]))
        keep_vals[TODO_COL_STATUS] = "Completed" if d["done"] else "Not Completed"
        keep_vals[TODO_COL_TASK] = d["task"]
        if not keep_vals[TODO_COL_NOTES]:
            keep_vals[TODO_COL_NOTES] = f"Combined from To Do rows {', '.join(str(c['row']) for c in candidates)} based on {d['day']} slot {d['slot']}."
        if not keep_vals[TODO_COL_HORIZON]:
            keep_vals[TODO_COL_HORIZON] = "Short Term"
        clear_rows = [c["row"] for c in candidates[1:]]

        if not dry_run:
            todo_client.values_update(f"'{TAB_TODO}'!A{keep['row']}:{col_letter(len(TODO_HEADERS) - 1)}{keep['row']}", [keep_vals[:len(TODO_HEADERS)]])
            for row_num in clear_rows:
                todo_client.values_update(f"'{TAB_TODO}'!A{row_num}:{col_letter(len(TODO_HEADERS) - 1)}{row_num}", [[""] * len(TODO_HEADERS)])
        combined.append({"day": d["day"], "slot": d["slot"], "task": d["task"],
                         "kept_row": keep["row"], "cleared_rows": clear_rows,
                         "source_tasks": [c["task"] for c in candidates]})
        used_candidate_rows.update(c["row"] for c in candidates)

    return {"combined": combined, "skipped": skipped}

def _build_week_formulas(meta: dict) -> list[tuple[str, list[list]]]:
    """Generate the formula writes that wire the Week tab to be a live mirror of day tabs.

    For each day i in 0..6, for each slot s in 1..25:
      Week!<status_col><WK_SLOT_FIRST_ROW + s - 1> = "='<DayTab>'!A<DAY_SLOT_FIRST_ROW + s - 1>"
      Week!<content_col><WK_SLOT_FIRST_ROW + s - 1> = "='<DayTab>'!B<DAY_SLOT_FIRST_ROW + s - 1>"
    Returns list of (a1_range, values) tuples — caller batches the writes.
    """
    writes: list[tuple[str, list[list]]] = []
    week_tab = find_tab(meta, TAB_WEEK)
    if week_tab is None:
        return writes  # Week tab missing — skip silently; build_week_tab.py needs to run first

    slot_count = WK_SLOT_COUNT
    for i in range(7):
        day_tab = WK_DAY_ORDER[i]
        sc = col_letter(wk_status_col(i))
        cc = col_letter(wk_content_col(i))

        # Priority slot status formulas (=DayTab!A14, =DayTab!A15, …)
        status_formulas = [[f"='{day_tab}'!A{DAY_SLOT_FIRST_ROW + s}"] for s in range(slot_count)]
        writes.append((f"'{TAB_WEEK}'!{sc}{WK_SLOT_FIRST_ROW}:{sc}{WK_SLOT_LAST_ROW}", status_formulas))

        # Priority slot task formulas (=DayTab!B14, =DayTab!B15, …)
        task_formulas = [[f"='{day_tab}'!B{DAY_SLOT_FIRST_ROW + s}"] for s in range(slot_count)]
        writes.append((f"'{TAB_WEEK}'!{cc}{WK_SLOT_FIRST_ROW}:{cc}{WK_SLOT_LAST_ROW}", task_formulas))

    return writes



def _copy_sheet_to_spreadsheet(source_client: SheetsClient, source_sheet_id: int, dest_spreadsheet_id: str) -> dict:
    """Copy one sheet/tab from source spreadsheet to a destination spreadsheet."""
    return source_client._retry(lambda: source_client.session.post(
        f"https://sheets.googleapis.com/v4/spreadsheets/{source_client.sheet_id}/sheets/{source_sheet_id}:copyTo",
        json={"destinationSpreadsheetId": dest_spreadsheet_id},
        timeout=60,
    ))


def _rename_and_move_sheet(client: SheetsClient, sheet_id: int, title: str, index: int | None = None) -> None:
    props = {"sheetId": sheet_id, "title": title}
    fields = "title"
    if index is not None:
        props["index"] = index
        fields = "title,index"
    client.batch_update([{"updateSheetProperties": {"properties": props, "fields": fields}}])


def _delete_sheet(client: SheetsClient, sheet_id: int) -> None:
    client.batch_update([{"deleteSheet": {"sheetId": sheet_id}}])


def _unique_sheet_title(existing: set[str], preferred: str, max_len: int = 99) -> str:
    base = preferred[:max_len].rstrip()
    if base not in existing:
        existing.add(base)
        return base
    i = 2
    while True:
        suffix = f" {i}"
        candidate = f"{base[:max_len-len(suffix)]}{suffix}".rstrip()
        if candidate not in existing:
            existing.add(candidate)
            return candidate
        i += 1


def _copy_tab_between_spreadsheets(source_client: SheetsClient, dest_client: SheetsClient,
                                   source_props: dict, new_title: str,
                                   index: int | None = None) -> str:
    copied = _copy_sheet_to_spreadsheet(source_client, source_props["sheetId"], dest_client.sheet_id)
    new_sheet_id = copied.get("sheetId")
    if new_sheet_id is None:
        raise RuntimeError(f"copyTo returned no sheetId for {source_props.get('title')!r}: {copied}")
    _rename_and_move_sheet(dest_client, new_sheet_id, new_title, index=index)
    return new_title


def _normalize_todo_row(row: list) -> list:
    row = list(row or []) + [""] * len(TODO_HEADERS)
    row = row[:len(TODO_HEADERS)]
    if row[TODO_COL_TASK] and not row[TODO_COL_STATUS]:
        row[TODO_COL_STATUS] = "Not Completed"
    if row[TODO_COL_TASK] and not row[TODO_COL_HORIZON]:
        row[TODO_COL_HORIZON] = "Short Term"
    return row


def _read_real_todo_rows(client: SheetsClient) -> list[list]:
    rows = client.get_values(f"'{TAB_TODO}'!A2:{col_letter(len(TODO_HEADERS) - 1)}{TODO_MAX_ROWS}") or []
    out = []
    for row in rows:
        norm = _normalize_todo_row(row)
        if str(norm[TODO_COL_TASK] or "").strip():
            out.append(norm)
    return out


def _write_todo_rows_sorted(client: SheetsClient, rows: list[list], *, clear_to: int = TODO_MAX_ROWS) -> dict:
    ongoing = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "On-going"]
    not_completed = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "Not Completed"]
    other_active = [r for r in rows if str(r[TODO_COL_STATUS]).strip() not in {"On-going", "Not Completed", "Completed", "Dropped"}]
    done = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "Completed"]
    dropped = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "Dropped"]
    packed = ongoing + not_completed + other_active + done + dropped
    last_col = col_letter(len(TODO_HEADERS) - 1)
    client.values_update(f"'{TAB_TODO}'!A1:{last_col}1", [TODO_HEADERS])
    if packed:
        client.values_update(f"'{TAB_TODO}'!A2:{last_col}{len(packed)+1}", packed)

    # Sheets rejects clear ranges past the current grid. Template/prior files can
    # have fewer than TODO_MAX_ROWS rows, so cap the cleanup to the live grid.
    grid_rows = clear_to
    try:
        meta = client.get_metadata()
        todo_props = find_tab(meta, TAB_TODO)
        if todo_props:
            grid_rows = min(clear_to, todo_props.get("gridProperties", {}).get("rowCount", clear_to))
    except Exception:
        grid_rows = clear_to
    clear_start = len(packed) + 2
    if clear_start <= grid_rows:
        client.values_clear(f"'{TAB_TODO}'!A{clear_start}:{last_col}{grid_rows}")
    return {"ongoing": len(ongoing), "not_completed": len(not_completed), "other_active": len(other_active), "completed": len(done), "dropped": len(dropped), "active": len(ongoing) + len(not_completed) + len(other_active), "total": len(packed)}


def _append_missing_day_tasks_to_todo(prior_client: SheetsClient, dry_run: bool = False) -> dict:
    """Ensure every prior daily-tab task slot has a To Do backend row.

    This is intentionally conservative: exact task-text matching only. Checked day slots
    become Completed when appended; unchecked day slots become Not Completed. Existing
    To Do rows are not reshaped here; combined edits are handled separately.
    """
    todo_rows = _read_real_todo_rows(prior_client)
    existing = {str(r[TODO_COL_TASK]).strip().lower() for r in todo_rows if str(r[TODO_COL_TASK]).strip()}
    additions: list[list] = []
    for day_tab in DAY_TAB_NAMES:
        vals = prior_client.get_values(f"'{day_tab}'!A{DAY_SLOT_FIRST_ROW}:E{DAY_SLOT_LAST_ROW}") or []
        for slot_i, row in enumerate(vals, start=1):
            task = str(row[DAY_COL_TASK] if len(row) > DAY_COL_TASK else "" or "").strip()
            if not task or task.lower() in existing:
                continue
            status_val = row[DAY_COL_STATUS] if len(row) > DAY_COL_STATUS else ""
            is_done = (status_val is True) or (str(status_val).strip().upper() == "TRUE")
            type_val = row[DAY_COL_TYPE] if len(row) > DAY_COL_TYPE else ""
            project_val = row[DAY_COL_PROJECT] if len(row) > DAY_COL_PROJECT else ""
            notes_val = row[DAY_COL_NOTES] if len(row) > DAY_COL_NOTES else ""
            additions.append([
                "Completed" if is_done else "Not Completed",
                task,
                type_val if type_val in TYPE_OPTIONS else "",
                project_val,
                "",
                notes_val,
                "Short Term",
            ])
            existing.add(task.lower())
    if additions and not dry_run:
        _write_todo_rows_sorted(prior_client, todo_rows + additions)
    return {"added": len(additions), "tasks": [r[TODO_COL_TASK] for r in additions]}


def _copy_project_surfaces(prior_client: SheetsClient, new_client: SheetsClient,
                           prior_meta: dict, new_meta: dict) -> dict:
    """Copy project tracking data/tabs from prior workbook into the new template workbook.

    Template placeholder project tabs are structural examples only. They are deleted
    from the newly copied template before real project tabs are copied from the prior
    week, so placeholders like PROJECT 1 never become live weekly tabs.
    """
    template_owned = {TAB_WEEK, TAB_TODO, *DAY_TAB_NAMES}
    copied: list[str] = []
    updated: list[str] = []
    deleted_placeholders: list[str] = []

    # Remove placeholder project tabs that exist only because the blank template
    # carries a frame/example. Real project tabs come only from the prior week.
    for title in TEMPLATE_PROJECT_PLACEHOLDER_TABS:
        props = find_tab(new_meta, title)
        if props:
            _delete_sheet(new_client, props["sheetId"])
            deleted_placeholders.append(title)
    if deleted_placeholders:
        new_meta = new_client.get_metadata()

    prior_projects = find_tab(prior_meta, TAB_PROJECTS)
    new_projects = find_tab(new_meta, TAB_PROJECTS)
    if prior_projects and new_projects:
        vals = prior_client.get_values(f"'{TAB_PROJECTS}'!A1:Z200") or []
        new_client.values_clear(f"'{TAB_PROJECTS}'!A1:Z200")
        if vals:
            new_client.values_update(f"'{TAB_PROJECTS}'!A1:{col_letter(max(len(r) for r in vals)-1)}{len(vals)}", vals)
        updated.append(TAB_PROJECTS)

    new_meta = new_client.get_metadata()
    existing = {s["properties"]["title"] for s in new_meta.get("sheets", [])}
    insert_at = len(new_meta.get("sheets", []))
    for s in prior_meta.get("sheets", []):
        title = s["properties"]["title"]
        if title in template_owned or title == TAB_PROJECTS or title.startswith("archive_"):
            continue
        # Skip retired/system tabs; copy user-facing project/Gantt tabs only.
        if title.startswith("_retired_") or title == TAB_RECURRING_TEMPLATE or title == TAB_COMPLETED_TODO or title == TAB_TODO_LONG_TERM:
            continue
        dest_title = _unique_sheet_title(existing, title)
        _copy_tab_between_spreadsheets(prior_client, new_client, s["properties"], dest_title, index=insert_at)
        copied.append(dest_title)
        insert_at += 1
    return {"projects_updated": updated, "project_tabs_copied": copied, "deleted_template_placeholders": deleted_placeholders}


def _archive_prior_day_tabs(prior_client: SheetsClient, new_client: SheetsClient,
                            prior_meta: dict, prior_sunday: date) -> dict:
    new_meta = new_client.get_metadata()
    existing = {s["properties"]["title"] for s in new_meta.get("sheets", [])}
    insert_at = len(new_meta.get("sheets", []))
    copied: list[str] = []
    for day in DAY_TAB_NAMES:
        props = find_tab(prior_meta, day)
        if not props:
            continue
        title = _unique_sheet_title(existing, f"archive_{prior_sunday.month}.{prior_sunday.day}_{day}")
        _copy_tab_between_spreadsheets(prior_client, new_client, props, title, index=insert_at)
        copied.append(title)
        insert_at += 1
    return {"archive_tabs_copied": copied}


def _clear_live_day_task_slots(client: SheetsClient, meta: dict) -> None:
    reqs: list[dict] = []
    for d in DAY_TAB_NAMES:
        props = find_tab(meta, d)
        if not props:
            continue
        sid = props["sheetId"]
        # Clear only task slots; template habit checkboxes stay blank/unchecked as designed.
        reqs.append({"repeatCell": {
            "range": {"sheetId": sid,
                      "startRowIndex": DAY_SLOT_FIRST_ROW - 1, "endRowIndex": DAY_SLOT_LAST_ROW,
                      "startColumnIndex": DAY_COL_STATUS, "endColumnIndex": DAY_COL_LAST + 1},
            "cell": {"userEnteredValue": {"stringValue": ""}},
            "fields": "userEnteredValue"}})
    if reqs:
        client.batch_update(reqs)


def _retitle_week_and_day_headers(client: SheetsClient, meta: dict, wd: list[date], week_label: str) -> None:
    week_tab_props = find_tab(meta, TAB_WEEK)
    if week_tab_props:
        wk_sid = week_tab_props["sheetId"]
        reqs = [{"updateCells": {
            "rows": [{"values": [{"userEnteredValue": {"stringValue": week_label}}]}],
            "fields": "userEnteredValue",
            "start": {"sheetId": wk_sid, "rowIndex": WK_TITLE_ROW - 1, "columnIndex": 0}}}]
        for i in range(7):
            reqs.append({"updateCells": {
                "rows": [{"values": [{"userEnteredValue": {
                    "stringValue": day_title_text(WK_DAY_ORDER[i], wd[i])}}]}],
                "fields": "userEnteredValue",
                "start": {"sheetId": wk_sid, "rowIndex": WK_DAYHDR_ROW - 1,
                          "columnIndex": wk_status_col(i)}}})
        client.batch_update(reqs)
    for i, day_tab in enumerate(DAY_TAB_NAMES):
        if find_tab(meta, day_tab):
            client.values_update(f"'{day_tab}'!A1", [[day_title_text(day_tab, wd[i])]])


def cmd_build_week_v2(args, prior_client: SheetsClient, prior_info: dict) -> int:
    """Template-first weekly rollover.

    Create the new weekly tracker from the blank structural template, reconcile the
    prior file's day tabs into its To Do backend, import the reconciled backend and
    project surfaces, archive prior daily tabs at the far right, seed the Week tab
    with recurring/explicit-day items only, and leave live day tabs empty until Kay
    approves the Week plan.
    """
    from datetime import date as _date
    sys.path.insert(0, str(Path(__file__).parent))
    from tracker_sheet_resolver import write_pointer

    wd = week_dates(_date.today())
    sun_date = wd[0]
    prior_week_raw = prior_info.get("week_of") or (sun_date - timedelta(days=7)).isoformat()
    try:
        prior_sunday = date.fromisoformat(str(prior_week_raw)[:10])
    except Exception:
        prior_sunday = sun_date - timedelta(days=7)
    title_prefix = getattr(args, "title_prefix", "") or ""
    new_title = f"{title_prefix}TO DO {sun_date.month}.{sun_date.day}.{sun_date.year % 100}"
    if sun_date.month == wd[6].month:
        week_label = f"WEEK OF {sun_date.strftime('%b')} {sun_date.day}-{wd[6].day}"
    else:
        week_label = f"WEEK OF {sun_date.strftime('%b')} {sun_date.day}-{wd[6].strftime('%b')} {wd[6].day}"

    existing_files = [] if getattr(args, "force_new_file", False) else _find_existing_tracker_files(new_title)
    if getattr(args, "dry_run", False):
        preview = {
            "prior_sheet": prior_info,
            "template_sheet_id": WEEKLY_TEMPLATE_SHEET_ID,
            "would_create": new_title,
            "week_label": week_label,
            "new_file_folder": "STRATEGIC PLANNING",
            "existing_target_files": [{
                "id": f.get("id"), "name": f.get("name"),
                "modifiedTime": f.get("modifiedTime"), "webViewLink": f.get("webViewLink"),
            } for f in existing_files],
        }
        try:
            todo_rows = _read_real_todo_rows(prior_client)
            preview["prior_todo_real_rows"] = len(todo_rows)
            preview["prior_todo_completed_rows"] = sum(1 for r in todo_rows if str(r[TODO_COL_STATUS]).strip() == "Completed")
            preview["missing_day_tasks_to_add"] = _append_missing_day_tasks_to_todo(prior_client, dry_run=True)["added"]
            preview["recurring_rows_to_week"] = len([
                r for r in todo_rows
                if len(r) > TODO_COL_HORIZON
                and str(r[TODO_COL_STATUS] or "") == STATUS_ONGOING
                and _todo_is_recurring(str(r[TODO_COL_HORIZON] or ""))
            ])
        except Exception as e:
            preview["inspection_error"] = str(e)
        print(json.dumps(preview, indent=2, default=str))
        return 0

    if existing_files:
        print(
            f"task-tracker-manager: refused build-week — {len(existing_files)} existing "
            f"file(s) named {new_title!r} already exist. Delete/rename the bad file or use "
            f"--title-prefix for a sandbox test.",
            file=sys.stderr,
        )
        for f in existing_files[:5]:
            print(f"  - {f.get('id')} modified={f.get('modifiedTime')} url={f.get('webViewLink','')}", file=sys.stderr)
        return 1

    # 1. Reconcile prior file before importing content.
    try:
        cmd_sync_done_status(SimpleNamespace(dry_run=False), _client=prior_client, _meta=prior_client.get_metadata())
    except Exception as e:
        print(f"task-tracker-manager: WARN pre-copy sync-done-status skipped — {e}", file=sys.stderr)
    missing_summary = {"added": 0, "tasks": []}
    try:
        missing_summary = _append_missing_day_tasks_to_todo(prior_client, dry_run=False)
        if missing_summary["added"]:
            print(f"task-tracker-manager: added {missing_summary['added']} missing day-tab task(s) into prior To Do")
    except Exception as e:
        print(f"task-tracker-manager: WARN missing day-task reconciliation skipped — {e}", file=sys.stderr)
    combined_summary = {"combined": [], "skipped": []}
    try:
        combined_summary = _sync_combined_day_tasks_to_todo(prior_client, prior_client, prior_client.get_metadata(), dry_run=False)
        if combined_summary["combined"]:
            print(f"task-tracker-manager: folded {len(combined_summary['combined'])} combined day-task edit(s) into prior To Do")
    except Exception as e:
        print(f"task-tracker-manager: WARN combined day-task reconciliation skipped — {e}", file=sys.stderr)

    # Sort/pack prior To Do so the imported backend starts clean.
    todo_rows = _read_real_todo_rows(prior_client)
    prior_pack = _write_todo_rows_sorted(prior_client, todo_rows)

    # 2. Snapshot prior file after reconciliation.
    snap_ranges = [f"'{TAB_WEEK}'!A1:O51"] + [f"'{d}'!A1:F54" for d in DAY_TAB_NAMES] + [f"'{TAB_TODO}'!A1:{col_letter(len(TODO_HEADERS) - 1)}400"]
    snap = snapshot_ranges(prior_client, "build-week-v2", snap_ranges)
    print(f"task-tracker-manager: snapshot reconciled prior file → {snap}")

    # 3. Copy blank template into Strategic Planning as the new weekly file.
    print(f"task-tracker-manager: gog drive copy template → {new_title}")
    try:
        new_sheet_id = _drive_copy_file(WEEKLY_TEMPLATE_SHEET_ID, new_title, STRATEGIC_PLANNING_FOLDER_ID)
    except RuntimeError as e:
        print(f"task-tracker-manager: template drive copy FAILED — {e}", file=sys.stderr)
        return 1
    print(f"task-tracker-manager: new template-based file created — id={new_sheet_id}")

    new_client = SheetsClient(new_sheet_id)
    prior_meta = prior_client.get_metadata()
    new_meta = new_client.get_metadata()

    # 4. Import reconciled To Do backend, active rows first and completed rows at bottom.
    todo_import = _write_todo_rows_sorted(new_client, todo_rows)
    print(f"task-tracker-manager: imported To Do — {todo_import['ongoing']} on-going, {todo_import['not_completed']} not completed, {todo_import['completed']} completed")

    # 5. Copy project tracking surfaces.
    project_summary = _copy_project_surfaces(prior_client, new_client, prior_meta, new_meta)
    print(f"task-tracker-manager: copied project surfaces — Projects data: {bool(project_summary['projects_updated'])}; "
          f"extra tabs: {len(project_summary['project_tabs_copied'])}; "
          f"template placeholders removed: {project_summary.get('deleted_template_placeholders', [])}")

    # 6. Copy prior daily tabs as far-right archive tabs.
    archive_summary = _archive_prior_day_tabs(prior_client, new_client, prior_meta, prior_sunday)
    print(f"task-tracker-manager: archived prior daily tabs into new file — {len(archive_summary['archive_tabs_copied'])} tab(s)")

    # 7. Rebuild/retitle Week and live day headers from template, clear live day task slots.
    new_meta = new_client.get_metadata()
    week_tab_props = find_tab(new_meta, TAB_WEEK)
    if week_tab_props:
        try:
            import build_week_tab
            new_client.batch_update(build_week_tab.structure_requests(week_tab_props["sheetId"], wd))
            print("task-tracker-manager: rebuilt Week tab structure from approved layout")
        except Exception as e:
            print(f"task-tracker-manager: WARN Week tab structure rebuild skipped — {e}", file=sys.stderr)
    new_meta = new_client.get_metadata()
    _clear_live_day_task_slots(new_client, new_meta)
    _retitle_week_and_day_headers(new_client, new_meta, wd, week_label)

    # 8. Populate Week baseline only. Do not touch live day tabs with tasks.
    recurring_summary = {"stamped": [], "refused": [], "rows_read": 0, "tab_present": False}
    if not getattr(args, "skip_recurring", False):
        recurring_summary = _stamp_recurring_week(new_client, new_client.get_metadata(), dry_run=False)
        print(f"task-tracker-manager: stamped {len(recurring_summary['stamped'])} recurring row(s) onto Week"
              + (f"; {len(recurring_summary['refused'])} refused" if recurring_summary["refused"] else ""))

    # 9. Archive prior file only after new file exists and content is imported.
    folder_id = _find_to_do_archive_folder_id()
    prior_archived = False
    if getattr(args, "no_folder_move", False):
        print("task-tracker-manager: --no-folder-move set — prior file stays in source folder")
    elif folder_id:
        _drive_move_file(prior_info["sheet_id"], folder_id)
        prior_archived = True
        print(f"task-tracker-manager: archived prior file → {TO_DO_ARCHIVE_FOLDER_NAME} ({folder_id})")
    else:
        print(f"task-tracker-manager: WARN '{TO_DO_ARCHIVE_FOLDER_NAME}' folder not found; prior file not moved", file=sys.stderr)

    # 10. Pointer update is last.
    if getattr(args, "no_pointer_update", False):
        print("task-tracker-manager: --no-pointer-update set — pointer unchanged")
    else:
        try:
            write_pointer(new_sheet_id, new_title, sun_date)
            print(f"task-tracker-manager: pointer updated → {new_title} ({new_sheet_id})")
        except Exception as e:
            print(f"task-tracker-manager: WARN pointer write failed ({e}); resolver fallback should recover", file=sys.stderr)

    trace_lines = [
        f"- prior file: {prior_info.get('title')} ({prior_info.get('sheet_id')})",
        f"- template source: {WEEKLY_TEMPLATE_SHEET_ID}",
        f"- new file: {new_title} ({new_sheet_id})",
        f"- week label: {week_label}",
        f"- missing day-tab tasks added to prior To Do: {missing_summary['added']}",
        f"- combined day-task edits folded before import: {len(combined_summary['combined'])}",
        f"- prior To Do packed before import: {prior_pack}",
        f"- imported To Do: {todo_import}",
        f"- project tabs copied: {project_summary['project_tabs_copied']}",
        f"- template project placeholders removed: {project_summary.get('deleted_template_placeholders', [])}",
        f"- archive daily tabs copied: {archive_summary['archive_tabs_copied']}",
        f"- recurring stamped onto Week: {len(recurring_summary['stamped'])}",
        f"- prior file archived: {prior_archived} ({folder_id or 'missing archive folder'})",
        f"- snapshot: {snap}",
    ]
    if recurring_summary["refused"]:
        for ref in recurring_summary["refused"]:
            trace_lines.append(f"  - recurring REFUSED: {ref.get('day')} slot {ref.get('slot')}: {ref.get('reason')}")
    trace("build-week-v2", sun_date.isoformat(), trace_lines)
    print(f"task-tracker-manager: build-week (template-first) complete — new file {new_title} live; Week ready for Kay review")
    return 0

def cmd_build_week(args) -> int:
    """Sunday weekly rebuild ceremony.

    PHASE 3 (2026-05-26) — weekly-files architecture: default behavior is now
    cross-file rollover (cmd_build_week_v2). The legacy in-place rebuild stays
    callable via --legacy for emergency recovery; per the no-auto-retire doctrine
    (`memory/feedback_explicit_review_before_retiring_verbs.md`) it is not removed.

    NEW DEFAULT (--legacy NOT set):
      1. Resolve prior file (current week's sheet) via tracker_sheet_resolver
      2. gog drive copy prior → new file `TO DO {next-Sun-date}.YY`
      3. Move new file into 'To Do Archive' folder
      4. Clear all 7 day tabs on new file
      5. Stamp recurring onto new file's day tabs
      6. Cross-file carryover (read prior day tabs → write new day tabs)
      7. Wire Week tab cells as in-file formulas (=Tue!B14 etc.)
      8. Re-title Week tab + per-day header dates
      9. Update pointer atomically (LAST step)
      10. Trace
      See cmd_build_week_v2 for full implementation.

    LEGACY (--legacy): in-place rebuild on the resolved current sheet. Archive
    prior Week tab as `archive_{Sun-date}` far-right tab, clear all 7 day-blocks
    on Week tab, re-title, stamp recurring onto Week tab, pull carryover from
    same-file day tabs onto Week tab. Day tabs untouched. distribute-week then
    fans out. This is the pre-2026-05-26 behavior preserved for recovery.
    """
    # --- New default: cross-file rollover ---
    if not getattr(args, "legacy", False):
        sys.path.insert(0, str(Path(__file__).parent))
        try:
            from tracker_sheet_resolver import resolve_current_sheet
        except ImportError as e:
            print(f"task-tracker-manager: resolver import failed ({e}); falling back to --legacy mode", file=sys.stderr)
        else:
            prior_info = resolve_current_sheet(force_refresh=getattr(args, "refresh_pointer", False))
            prior_client = SheetsClient(prior_info["sheet_id"])
            return cmd_build_week_v2(args, prior_client, prior_info)

    # --- Legacy fallthrough: in-place rebuild ---
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
        print("  Would re-stamp per-day header dates (row 17):")
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
        # Carryover preview
        if getattr(args, "skip_carryover", False):
            print("  --skip-carryover set → would NOT pull incomplete items from day tabs")
        else:
            print("  Carryover preview — incomplete day-tab items that WOULD be pulled onto the new Week tab:")
            preview = _pull_carryover_to_week(client, dry_run=True)
            if preview["pulled"]:
                for p in preview["pulled"]:
                    print(f"    WOULD PULL: {p['day']} src slot {p['src_slot']} → Week dst slot {p['dst_slot']}: \"{p['task']}\"")
                if preview["refused"]:
                    print(f"  {len(preview['refused'])} REFUSED (no empty slot on Week tab):")
                    for ref in preview["refused"]:
                        print(f"    REFUSED: {ref['day']} src slot {ref['src_slot']} \"{ref['task']}\": {ref['reason']}")
            else:
                print("    (no incomplete items — all prior-week day-tab slots are either completed or empty)")
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
    # Per-day header dates (row 17, merged anchors at status cols)
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

    # ---------- 6a. Carryover pull from prior week's day tabs (added 2026-05-26 per Kay) ----------
    carryover_summary: dict = {"pulled": [], "refused": [], "rows_read": 0}
    if getattr(args, "skip_carryover", False):
        print("task-tracker-manager: --skip-carryover set — incomplete day-tab items NOT pulled to Week tab")
    else:
        carryover_summary = _pull_carryover_to_week(client, dry_run=False)
        if carryover_summary["pulled"]:
            print(f"task-tracker-manager: pulled {len(carryover_summary['pulled'])} incomplete item(s) "
                  f"from prior week's day tabs onto Week tab"
                  + (f"; {len(carryover_summary['refused'])} refused (no empty slot)"
                     if carryover_summary["refused"] else ""))
            for p in carryover_summary["pulled"][:10]:  # cap chatter
                print(f"  carryover: {p['day']} src slot {p['src_slot']} → Week dst slot {p['dst_slot']}: \"{p['task']}\"")
            if len(carryover_summary["pulled"]) > 10:
                print(f"  … and {len(carryover_summary['pulled']) - 10} more (see trace)")
        else:
            print("task-tracker-manager: no incomplete items to carry over (all prior-week day-tab slots were either completed or empty)")

    # ---------- 6. Trace ----------
    trace_lines = [
        f"- week (Sunday boundary): {wd[0].isoformat()} .. {wd[6].isoformat()}",
        f"- target: Week planning tab (day tabs read for carryover, not written — distribute-week fans out later)",
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
    if carryover_summary["pulled"] or carryover_summary["refused"]:
        trace_lines.append(f"- carryover pulled from day tabs → Week: {len(carryover_summary['pulled'])} item(s)")
        for p in carryover_summary["pulled"]:
            trace_lines.append(f"  - carryover-pull: {p['day']} src slot {p['src_slot']} → Week dst slot {p['dst_slot']}: \"{p['task']}\"")
        if carryover_summary["refused"]:
            trace_lines.append(f"- carryover REFUSED: {len(carryover_summary['refused'])}")
            for ref in carryover_summary["refused"]:
                trace_lines.append(f"  - {ref['day']} src slot {ref['src_slot']} \"{ref['task']}\": {ref['reason']}")
    trace("build-week", sun_date.isoformat(), trace_lines)
    print(f'task-tracker-manager: build-week complete — archived prior Week → "{final_archive}", '
          f'cleared + re-titled the Week tab to {week_label!r}. '
          f'Day tabs untouched — review the Week tab, then run distribute-week to fan it out.')
    if recurring_summary["tab_present"]:
        print(f'task-tracker-manager: stamped {len(recurring_summary["stamped"])} recurring row(s) onto Week'
              + (f"; {len(recurring_summary['refused'])} refused" if recurring_summary["refused"] else ""))
    return 0



def cmd_schedule_from_todo_days(args) -> int:
    """Populate the Week planning tab from To Do rows with Day of the Week set.

    Kay's Sunday scheduling bridge: she reviews the To Do backend, assigns a day
    in column H, this command writes those non-completed rows into the matching
    Week day block. Daily tabs remain untouched until Kay approves the Week plan
    and asks to fan it out.
    """
    client = SheetsClient()
    meta = client.get_metadata()
    snap_ranges = [f"'{TAB_TODO}'!A1:{col_letter(len(TODO_HEADERS) - 1)}{TODO_MAX_ROWS}",
                   f"'{TAB_WEEK}'!A1:{col_letter(WK_GRID_COLS - 1)}{WK_GRID_ROWS}"] + [
        day_tab_block(d, DAY_COL_STATUS, DAY_COL_LAST, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW)
        for d in DAY_TAB_NAMES if find_tab(meta, d)
    ]
    snap = snapshot_ranges(client, "schedule-from-todo-days", snap_ranges)

    rows = _read_real_todo_rows(client)
    ongoing = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "On-going"]
    not_completed = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "Not Completed"]
    other_active = [r for r in rows if str(r[TODO_COL_STATUS]).strip() not in {"On-going", "Not Completed", "Completed", "Dropped"}]
    done = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "Completed"]
    dropped = [r for r in rows if str(r[TODO_COL_STATUS]).strip() == "Dropped"]
    pack_summary = {
        "ongoing": len(ongoing),
        "not_completed": len(not_completed),
        "other_active": len(other_active),
        "completed": len(done),
        "dropped": len(dropped),
        "active": len(ongoing) + len(not_completed) + len(other_active),
        "total": len(rows),
    }
    if not getattr(args, "dry_run", False):
        pack_summary = _write_todo_rows_sorted(client, rows)
        rows = _read_real_todo_rows(client)

    week_start, week_end = week_dates(date.today())[0], week_dates(date.today())[-1]
    day_assigned: dict[str, list[str]] = {d: [] for d in DAY_TAB_NAMES}
    recurring_baseline: dict[str, list[str]] = {d: [] for d in DAY_TAB_NAMES}
    skipped: list[dict] = []
    for r in rows:
        status = str(r[TODO_COL_STATUS] or "").strip()
        task = str(r[TODO_COL_TASK] or "").strip()
        if not task or status in {"Completed", "Dropped"}:
            continue
        horizon = str(r[TODO_COL_HORIZON] or "").strip()
        if _todo_is_recurring(horizon):
            day3 = _recurring_day3(horizon)
            if day3:
                day_tab = _resolve_day_tab_name(day3)
                if task not in recurring_baseline[day_tab]:
                    recurring_baseline[day_tab].append(task)
        day_value = str(r[TODO_COL_DAY] if len(r) > TODO_COL_DAY else "" or "").strip()
        if day_value:
            due_value = str(r[TODO_COL_DUE] if len(r) > TODO_COL_DUE else "" or "").strip()
            if due_value:
                try:
                    due_date = datetime.strptime(due_value, "%Y-%m-%d").date()
                except ValueError:
                    skipped.append({"task": task, "day": day_value, "reason": f"unparseable due date {due_value!r}"})
                    continue
                if due_date > week_end:
                    skipped.append({"task": task, "day": day_value, "reason": f"future due date {due_value} outside current week"})
                    continue
            try:
                day_tab = _resolve_day_tab_name(day_value)
            except SystemExit:
                skipped.append({"task": task, "day": day_value, "reason": "unrecognized day"})
                continue
            if task not in day_assigned[day_tab]:
                day_assigned[day_tab].append(task)

    planned: dict[str, list[str]] = {d: [] for d in DAY_TAB_NAMES}
    for day_tab in DAY_TAB_NAMES:
        planned[day_tab].extend(day_assigned[day_tab])
        for task in recurring_baseline[day_tab]:
            if task not in planned[day_tab]:
                planned[day_tab].append(task)

    collisions = {d: len(v) for d, v in planned.items() if len(v) > WK_SLOT_COUNT}
    if collisions:
        print(f"task-tracker-manager: refused schedule-from-todo-days — too many tasks for Week slots: {collisions}", file=sys.stderr)
        return 1

    summary = {d: len(v) for d, v in planned.items() if v}
    if getattr(args, "dry_run", False):
        print(json.dumps({
            "target": "Week",
            "pack_summary": pack_summary,
            "would_write": summary,
            "week_slot_capacity": WK_SLOT_COUNT,
            "skipped": skipped,
            "snapshot": snap,
        }, indent=2))
        return 0

    # Clear Week task slots only, then write recurring baseline + H-assigned tasks.
    week_tab = find_tab(client.get_metadata(), TAB_WEEK)
    if week_tab is None:
        print("task-tracker-manager: Week tab not found", file=sys.stderr)
        return 1
    try:
        import build_week_tab
        client.batch_update(build_week_tab.structure_requests(week_tab["sheetId"], week_dates(date.today())))
    except Exception as e:
        print(f"task-tracker-manager: WARN Week structure rebuild skipped — {e}", file=sys.stderr)
    writes: list[tuple[str, list[list]]] = []
    for widx, day in enumerate(WK_DAY_ORDER):
        sc = col_letter(wk_status_col(widx))
        tc = col_letter(wk_content_col(widx))
        values_status = []
        values_task = []
        for i in range(WK_SLOT_COUNT):
            task = planned[day][i] if i < len(planned[day]) else ""
            values_status.append([False])
            values_task.append([task])
        writes.append((f"'{TAB_WEEK}'!{sc}{WK_SLOT_FIRST_ROW}:{sc}{WK_SLOT_LAST_ROW}", values_status))
        writes.append((f"'{TAB_WEEK}'!{tc}{WK_SLOT_FIRST_ROW}:{tc}{WK_SLOT_LAST_ROW}", values_task))
    for rng, vals in writes:
        client.values_update(rng, vals)

    # Daily tabs should remain empty until Kay approves Week and asks to distribute.
    blank = [[False, "", "", "", ""] for _ in range(DAY_SLOT_COUNT)]
    for day_tab in DAY_TAB_NAMES:
        if find_tab(meta, day_tab):
            client.values_update(day_tab_block(day_tab, DAY_COL_STATUS, DAY_COL_LAST, DAY_SLOT_FIRST_ROW, DAY_SLOT_LAST_ROW), blank)

    trace("schedule-from-todo-days", date.today().isoformat(), [
        f"- target: Week planning tab",
        f"- packed To Do: {pack_summary}",
        f"- wrote Week from To Do Day of the Week: {summary}",
        f"- daily tabs cleared/not populated pending Kay approval",
        f"- skipped: {skipped}",
        f"- snapshot: {snap}",
    ])
    print(f"task-tracker-manager: scheduled To Do day assignments into Week — {summary}; daily tabs left empty. snapshot: {snap}")
    if skipped:
        print(f"task-tracker-manager: skipped {len(skipped)} row(s): {skipped[:10]}")
    return 0


def cmd_distribute_week(args) -> int:
    """Fan the finalized Week planning tab OUT into the 7 day tabs.

    Design-corrected model (2026-05-17): after `build-week` rebuilds the Week
    tab and Kay lays out the full week there, this verb reads each Week-grid
    day-block's 25 priority slots (status + task) and writes them into the
    corresponding day tab's slots (rows 17-41). Collision-aware: refuses to overwrite a non-empty day-tab slot
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
        slots = []
        for i in range(WK_SLOT_COUNT):
            s = st[i][0] if i < len(st) and st[i] else ""
            t = tk[i][0] if i < len(tk) and tk[i] else ""
            slots.append((_is_truthy(s), str(t).strip() if t else ""))
        plan[name] = {"slots": slots}

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
            print(f"    {name}: would write {filled} slot(s)")
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
        # Slot block A:E rows 17..41 — write [status, task, "", "", ""].
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

    # 1. Walk the 7 day tabs' 25 slots each — read A (status) + B (task) columns.
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
        f"'{TAB_TODO}'!A2:{col_letter(len(TODO_HEADERS) - 1)}{TODO_MAX_ROWS}")
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
        sys.exit(f"task-tracker-manager: weekly recurring supports Sun..Sat "
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
        [f"'{TAB_TODO}'!A{target_row}:{col_letter(len(TODO_HEADERS) - 1)}{target_row}"])
    client.values_update(f"'{TAB_TODO}'!A{target_row}:{col_letter(len(TODO_HEADERS) - 1)}{target_row}", [[
        "On-going", args.task, args.type, args.project or "", "",
        args.notes or "", horizon, "",
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

    pre = client.get_values(f"'{TAB_TODO}'!A{args.row}:{col_letter(len(TODO_HEADERS) - 1)}{args.row}")
    pre_row = pre[0] if pre and pre[0] else []
    if not pre_row or not any((c or "").strip() if isinstance(c, str) else c for c in pre_row):
        sys.exit(f"task-tracker-manager: To Do row {args.row} is already empty")
    pad = list(pre_row) + [""] * (len(TODO_HEADERS) - len(pre_row))
    horizon = str(pad[TODO_COL_HORIZON] or "")
    if not _todo_is_recurring(horizon):
        sys.exit(f"task-tracker-manager: refused — To Do row {args.row} Horizon "
                 f"{horizon!r} is not recurring. Use a normal edit, not recurring-remove.")

    snap = snapshot_ranges(client, "recurring-remove",
        [f"'{TAB_TODO}'!A{args.row}:{col_letter(len(TODO_HEADERS) - 1)}{args.row}"])
    client.values_clear(f"'{TAB_TODO}'!A{args.row}:{col_letter(len(TODO_HEADERS) - 1)}{args.row}")

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
    week_sid = find_tab(meta, TAB_WEEK)["sheetId"] if find_tab(meta, TAB_WEEK) else None

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
        task_last_row = _day_task_last_row(client, day_name)
        R.extend(_day_task_format_requests(sid, DAY_SLOT_FIRST_ROW, task_last_row))
        # Top 3 priority slots: fixed sage shading across A:E.
        R.append({"repeatCell": {
            "range": {"sheetId": sid,
                        "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                        "endRowIndex": DAY_SLOT_FIRST_ROW - 1 + TOP_PRIORITY_SLOT_COUNT,
                        "startColumnIndex": DAY_COL_STATUS,
                        "endColumnIndex": DAY_COL_LAST + 1},
            "cell": {"userEnteredFormat": {"backgroundColor": hex_to_rgb(SAGE_LIGHT_HEX)}},
            "fields": "userEnteredFormat.backgroundColor",
        }})

        # Slot rule: status TRUE → strikethrough + sage-extra-light across A:E.
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": sid,
                            "startRowIndex": DAY_SLOT_FIRST_ROW - 1,
                            "endRowIndex": task_last_row,
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
        # Habit rules: each checkbox shades only its own checkbox+label pair.
        for col_letter, start_col, end_col in (("A", 0, 2), ("C", 2, 4), ("E", 4, 6)):
            R.append({"addConditionalFormatRule": {
                "rule": {
                    "ranges": [{"sheetId": sid,
                                "startRowIndex": DAY_HABIT_FIRST_ROW - 1,
                                "endRowIndex": DAY_HABIT_LAST_ROW,
                                "startColumnIndex": start_col,
                                "endColumnIndex": end_col}],
                    "booleanRule": {
                        "condition": {"type": "CUSTOM_FORMULA",
                                      "values": [{"userEnteredValue":
                                                  f"=${col_letter}{DAY_HABIT_FIRST_ROW}=TRUE"}]},
                        "format": {"backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX)},
                    },
                },
                "index": 0,
            }})

    # Week tab: mirror the same fixed top-3 priority shading for each day block.
    if week_sid is not None:
        for i in range(7):
            sc = wk_status_col(i)
            tc = wk_content_col(i)
            R.append({"repeatCell": {
                "range": {"sheetId": week_sid,
                            "startRowIndex": WK_SLOT_FIRST_ROW - 1,
                            "endRowIndex": WK_SLOT_FIRST_ROW - 1 + TOP_PRIORITY_SLOT_COUNT,
                            "startColumnIndex": sc,
                            "endColumnIndex": tc + 1},
                "cell": {"userEnteredFormat": {"backgroundColor": hex_to_rgb(SAGE_LIGHT_HEX)}},
                "fields": "userEnteredFormat.backgroundColor",
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

    # ---- Pack-to-top auto-compact (added 2026-05-26 per feedback_task_tracker_pack_to_top) ----
    # Read each day tab + each Week-tab day-block, filter to non-empty (status, task) pairs,
    # write back packed (items at top, empties below). Closes gaps from manual deletes.
    compact_summary = {"day_tab_packed": 0, "week_block_packed": 0}

    def _flat(vals, n=DAY_SLOT_COUNT, default=""):
        out = []
        for v in (vals or []):
            cell = v[0] if (isinstance(v, list) and len(v) > 0) else default
            out.append(cell)
        while len(out) < n: out.append(default)
        return out[:n]

    # Day tabs
    for day_tab in DAY_TAB_NAMES:
        try:
            statuses = _flat(client.get_values(f"'{day_tab}'!A{DAY_SLOT_FIRST_ROW}:A{DAY_SLOT_LAST_ROW}"), default=False)
            tasks    = _flat(client.get_values(f"'{day_tab}'!B{DAY_SLOT_FIRST_ROW}:B{DAY_SLOT_LAST_ROW}"), default="")
        except Exception:
            continue
        packed = [(s, t) for s, t in zip(statuses, tasks) if str(t or "").strip()]
        original_non_empty = sum(1 for t in tasks if str(t or "").strip())
        # Detect if compact is needed: are non-empty items already at top with no gaps?
        needs_compact = False
        for i, t in enumerate(tasks):
            if not str(t or "").strip() and any(str(tt or "").strip() for tt in tasks[i+1:]):
                needs_compact = True; break
        if needs_compact:
            n = len(packed)
            new_status = [[s] for s, _ in packed] + [[False]] * (DAY_SLOT_COUNT - n)
            new_task   = [[t] for _, t in packed] + [[""]] * (DAY_SLOT_COUNT - n)
            client.values_update(f"'{day_tab}'!A{DAY_SLOT_FIRST_ROW}:A{DAY_SLOT_LAST_ROW}", new_status)
            client.values_update(f"'{day_tab}'!B{DAY_SLOT_FIRST_ROW}:B{DAY_SLOT_LAST_ROW}", new_task)
            compact_summary["day_tab_packed"] += 1
            print(f"task-tracker-manager: packed {day_tab} day tab ({n} items at top)")

    # Week tab is a formula mirror of day tabs; never compact it directly.
    # Day-tab packing flows through formulas instead.

    trace("reformat", "rules-reapplied", [
        f"- applied {len(R)} conditional-format rules",
        f"- snapshot: {snap}",
        f"- pack-to-top: {compact_summary['day_tab_packed']} day tab(s) compacted",
        f"- pack-to-top: {compact_summary['week_block_packed']} Week-tab day-block(s) compacted",
    ])
    print(f"task-tracker-manager: reformatted ({len(R)} CF rules + "
          f"{compact_summary['day_tab_packed']} day tabs + "
          f"{compact_summary['week_block_packed']} Week blocks compacted)")
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
        f"'{TAB_TODO}'!A2:{col_letter(len(TODO_HEADERS) - 1)}{TODO_MAX_ROWS}")
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
    # Carryover = any task row above the visible NOTES header where Task is
    # non-empty AND status is FALSE. This intentionally includes overflow rows
    # inserted by carry-forward-day, not just the canonical 25-slot block.
    day_tabs = list(_iter_day_tabs(meta))
    carryover_lines: list[str] = []
    empty_slots_lines: list[str] = []
    carryover_total = 0
    tomorrow_tab = DAY_LABELS[(today.weekday() + 1) % 7]
    for day_name, _props in day_tabs:
        last_task_row = max(DAY_SLOT_LAST_ROW, _day_task_last_row(client, day_name))
        status_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_STATUS, DAY_SLOT_FIRST_ROW, last_task_row))
        task_vals = client.get_values(
            day_tab_range(day_name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, last_task_row))
        empty = 0
        day_incomplete: list[str] = []
        row_count = last_task_row - DAY_SLOT_FIRST_ROW + 1
        for si in range(row_count):
            st = status_vals[si][0] if si < len(status_vals) and status_vals[si] else ""
            tk = task_vals[si][0] if si < len(task_vals) and task_vals[si] else ""
            tk_text = (tk or "").strip() if isinstance(tk, str) else ""
            canonical_slot = si < DAY_SLOT_COUNT
            if canonical_slot and not tk_text:
                empty += 1
                continue
            if not tk_text:
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


def _default_closeout_date() -> date:
    """Return the human operating date for Good Night carry-forward.

    Good Night often runs after midnight. Before 4am ET, treat the closeout as
    the prior calendar day so Sunday night does not become Monday -> Tuesday.
    """
    now = datetime.now(ZoneInfo("America/New_York"))
    if now.hour < 4:
        return (now - timedelta(days=1)).date()
    return now.date()


def _day_task_last_row(client: SheetsClient, day_name: str, *, scan_last: int = 80) -> int:
    """Return the last task row before the NOTES block on a day tab.

    Manual edits can push tasks below the canonical 25-slot range. Carry-forward
    must treat those overflow rows as task rows too, stopping at the visible
    NOTES header.
    """
    vals = client.get_values(f"'{day_name}'!A{DAY_SLOT_FIRST_ROW}:A{scan_last}") or []
    for offset, row in enumerate(vals):
        cell = str((row[0] if row else "") or "").strip().upper()
        if cell == "NOTES":
            return max(DAY_SLOT_LAST_ROW, DAY_SLOT_FIRST_ROW + offset - 1)
    return DAY_SLOT_LAST_ROW


def _day_task_row_count(last_row: int) -> int:
    return max(0, last_row - DAY_SLOT_FIRST_ROW + 1)


def _day_task_values_block(day_name: str, last_row: int) -> str:
    return day_tab_block(day_name, DAY_COL_STATUS, DAY_COL_LAST, DAY_SLOT_FIRST_ROW, last_row)


def _day_task_format_requests(sheet_id: int, start_row: int, end_row: int) -> list[dict]:
    """Canonical formatting/validation for day-tab task rows.

    Rows are 1-based and inclusive. Used for overflow rows inserted above NOTES
    so they behave like normal day-tab task slots instead of raw copied grid rows.
    """
    if end_row < start_row:
        return []
    return [
        {"setDataValidation": {
            "range": {"sheetId": sheet_id, "startRowIndex": start_row - 1,
                      "endRowIndex": end_row, "startColumnIndex": DAY_COL_STATUS,
                      "endColumnIndex": DAY_COL_STATUS + 1},
            "rule": {"condition": {"type": "BOOLEAN"}, "strict": True}}},
        {"repeatCell": {
            "range": {"sheetId": sheet_id, "startRowIndex": start_row - 1,
                      "endRowIndex": end_row, "startColumnIndex": DAY_COL_TASK,
                      "endColumnIndex": DAY_COL_TASK + 1},
            "cell": {"userEnteredFormat": {
                "verticalAlignment": "MIDDLE",
                "textFormat": {"fontSize": 17, "foregroundColor": hex_to_rgb(INK_HEX)}}},
            "fields": "userEnteredFormat(verticalAlignment,textFormat)"}},
        {"setDataValidation": {
            "range": {"sheetId": sheet_id, "startRowIndex": start_row - 1,
                      "endRowIndex": end_row, "startColumnIndex": DAY_COL_TYPE,
                      "endColumnIndex": DAY_COL_TYPE + 1},
            "rule": {"condition": {"type": "ONE_OF_LIST",
                                   "values": [{"userEnteredValue": o} for o in TYPE_OPTIONS]},
                     "showCustomUi": True, "strict": False}}},
        {"setDataValidation": {
            "range": {"sheetId": sheet_id, "startRowIndex": start_row - 1,
                      "endRowIndex": end_row, "startColumnIndex": DAY_COL_PROJECT,
                      "endColumnIndex": DAY_COL_PROJECT + 1},
            "rule": {"condition": {"type": "ONE_OF_LIST",
                                   "values": [{"userEnteredValue": o} for o in PROJECT_OPTIONS]},
                     "showCustomUi": True, "strict": False}}},
        {"updateDimensionProperties": {
            "range": {"sheetId": sheet_id, "dimension": "ROWS",
                      "startIndex": start_row - 1, "endIndex": end_row},
            "properties": {"pixelSize": 34}, "fields": "pixelSize"}},
    ]


def _pack_day_tab_checked_rows(client: SheetsClient, day_name: str) -> dict:
    """Pack a day tab's task rows with checked items first, then active items.

    This keeps yesterday readable after carry-forward clears incomplete rows out
    of the middle of the day. Formatting/validation live on the sheet rows, so
    only values are rewritten. Overflow task rows above NOTES are included.
    """
    task_last_row = _day_task_last_row(client, day_name)
    task_row_count = _day_task_row_count(task_last_row)
    vals = client.get_values(_day_task_values_block(day_name, task_last_row))
    completed: list[list] = []
    active: list[list] = []
    for i in range(task_row_count):
        row = list(vals[i]) if i < len(vals) else []
        padded = row + [""] * ((DAY_COL_LAST + 1) - len(row))
        task_text = str(padded[DAY_COL_TASK] or "").strip()
        if not task_text or task_text.lower() == "task":
            continue
        payload = [
            bool(_is_truthy(padded[DAY_COL_STATUS])),
            task_text,
            padded[DAY_COL_TYPE],
            padded[DAY_COL_PROJECT],
            padded[DAY_COL_NOTES],
        ]
        if payload[DAY_COL_STATUS]:
            completed.append(payload)
        else:
            active.append(payload)

    packed = completed + active
    blank = [False, "", "", "", ""]
    values = packed + [blank[:] for _ in range(task_row_count - len(packed))]
    client.values_update(_day_task_values_block(day_name, task_last_row), values)
    return {
        "completed": len(completed),
        "active": len(active),
        "blank": task_row_count - len(packed),
        "rows": f"{DAY_SLOT_FIRST_ROW}:{task_last_row}",
    }


def cmd_carry_forward_day(args) -> int:
    """Move all incomplete items from one day tab to the next day's empty slots.

    Default is closeout-date -> following day. Completed and empty slots stay
    where they are. This is the Good Night carry-forward path: it does not
    require Kay to approve each individual move.
    """
    if getattr(args, "date", None):
        try:
            today = date.fromisoformat(args.date)
        except ValueError:
            sys.exit("task-tracker-manager: --date must be YYYY-MM-DD")
    else:
        today = _default_closeout_date()
    src_name = _resolve_day_tab_name(args.from_day) if args.from_day else DAY_LABELS[today.weekday()]
    dst_name = _resolve_day_tab_name(args.to_day) if args.to_day else DAY_LABELS[(today.weekday() + 1) % 7]

    if src_name == dst_name:
        sys.exit("task-tracker-manager: refused carry-forward-day — source and destination are the same day")

    client = SheetsClient()
    meta = client.get_metadata()
    if find_day_tab(meta, src_name) is None:
        sys.exit(f"task-tracker-manager: source day tab '{src_name}' not found")
    if find_day_tab(meta, dst_name) is None:
        sys.exit(f"task-tracker-manager: destination day tab '{dst_name}' not found")

    src_last_row = _day_task_last_row(client, src_name)
    dst_last_row = _day_task_last_row(client, dst_name)
    src_row_count = _day_task_row_count(src_last_row)
    dst_row_count = _day_task_row_count(dst_last_row)

    src_vals = client.get_values(_day_task_values_block(src_name, src_last_row))
    dst_tasks = client.get_values(day_tab_range(dst_name, DAY_COL_TASK, DAY_SLOT_FIRST_ROW, dst_last_row))

    dst_existing_tasks = {
        str(row[0]).strip().casefold()
        for row in dst_tasks
        if row and str(row[0] or "").strip()
    }
    dst_empty_slots = [
        i + 1 for i in range(dst_row_count)
        if not (dst_tasks[i][0] if i < len(dst_tasks) and dst_tasks[i] else "")
    ]
    moves: list[dict] = []
    overflow_needed = 0
    for i in range(src_row_count):
        row = src_vals[i] if i < len(src_vals) else []
        status = row[DAY_COL_STATUS] if len(row) > DAY_COL_STATUS else ""
        task = row[DAY_COL_TASK] if len(row) > DAY_COL_TASK else ""
        task_text = str(task or "").strip()
        if not task_text or task_text.lower() == "task" or _is_truthy(status):
            continue
        task_key = task_text.casefold()
        if task_key in dst_existing_tasks:
            moves.append({
                "src_slot": i + 1,
                "src_row": DAY_SLOT_FIRST_ROW + i,
                "dst_slot": None,
                "dst_row": None,
                "task": task_text,
                "payload": [
                    False,
                    task_text,
                    row[DAY_COL_TYPE] if len(row) > DAY_COL_TYPE else "",
                    row[DAY_COL_PROJECT] if len(row) > DAY_COL_PROJECT else "",
                    row[DAY_COL_NOTES] if len(row) > DAY_COL_NOTES else "",
                ],
                "overflow_inserted": False,
                "already_in_destination": True,
            })
            continue
        if not dst_empty_slots:
            overflow_needed += 1
            dst_slot = dst_row_count + overflow_needed
        else:
            dst_slot = dst_empty_slots.pop(0)
        dst_existing_tasks.add(task_key)
        moves.append({
            "src_slot": i + 1,
            "src_row": DAY_SLOT_FIRST_ROW + i,
            "dst_slot": dst_slot,
            "dst_row": DAY_SLOT_FIRST_ROW + dst_slot - 1,
            "task": task_text,
            "payload": [
                False,
                task_text,
                row[DAY_COL_TYPE] if len(row) > DAY_COL_TYPE else "",
                row[DAY_COL_PROJECT] if len(row) > DAY_COL_PROJECT else "",
                row[DAY_COL_NOTES] if len(row) > DAY_COL_NOTES else "",
            ],
            "overflow_inserted": dst_slot > dst_row_count,
            "already_in_destination": False,
        })

    refused: list[dict] = []
    planned = moves

    if args.dry_run:
        print(f"task-tracker-manager: carry-forward-day (DRY RUN) {src_name} → {dst_name}")
        print(f"  Would move: {len(planned)}")
        print(f"  Refused: {len(refused)}")
        if overflow_needed:
            print(f"  Would insert {overflow_needed} overflow task row(s) above {dst_name} NOTES")
        for m in planned:
            if m.get("already_in_destination"):
                print(f"  - {src_name} slot {m['src_slot']} already exists on {dst_name}; would clear source: {m['task']}")
            else:
                print(f"  - {src_name} slot {m['src_slot']} → {dst_name} slot {m['dst_slot']}: {m['task']}")
        for m in refused:
            print(f"  - REFUSED {src_name} slot {m['src_slot']}: {m['task']} ({m['refused']})")
        return 0 if not refused else 1

    if refused:
        print(
            f"task-tracker-manager: refused carry-forward-day — {len(refused)} item(s) "
            f"could not fit in {dst_name}",
            file=sys.stderr,
        )
        for m in refused:
            print(f"  - {src_name} slot {m['src_slot']}: {m['task']} ({m['refused']})", file=sys.stderr)
        return 1

    snap = snapshot_ranges(client, "carry-forward-day", [
        _day_task_values_block(src_name, src_last_row),
        day_tab_block(dst_name, DAY_COL_STATUS, DAY_COL_LAST, DAY_SLOT_FIRST_ROW, dst_last_row + overflow_needed),
    ])

    if overflow_needed:
        dst_tab = find_day_tab(meta, dst_name)
        insert_at_row = dst_last_row + 1
        insert_start_index = insert_at_row - 1
        grid_rows = int(dst_tab.get("gridProperties", {}).get("rowCount", 0) or 0)
        requests = []
        if insert_start_index > grid_rows:
            requests.append({
                "updateSheetProperties": {
                    "properties": {
                        "sheetId": dst_tab["sheetId"],
                        "gridProperties": {"rowCount": insert_start_index},
                    },
                    "fields": "gridProperties.rowCount",
                }
            })
        requests.append({
            "insertDimension": {
                "range": {
                    "sheetId": dst_tab["sheetId"],
                    "dimension": "ROWS",
                    "startIndex": insert_start_index,
                    "endIndex": insert_start_index + overflow_needed,
                },
                "inheritFromBefore": True,
            }
        })
        requests.extend(_day_task_format_requests(dst_tab["sheetId"], insert_at_row, insert_at_row + overflow_needed - 1))
        client.batch_update(requests)

    if not planned:
        pack_summary = _pack_day_tab_checked_rows(client, src_name)
        trace("carry-forward-day", f"{src_name.lower()}-to-{dst_name.lower()}", [
            "- moved: 0",
            f"- source: {src_name}",
            f"- destination: {dst_name}",
            f"- source packed: {pack_summary}",
            f"- snapshot: {snap}",
        ])
        print(
            f"task-tracker-manager: carry-forward-day complete — no incomplete {src_name} "
            f"items to move; packed {src_name} checked rows to top"
        )
        return 0

    for m in planned:
        if m.get("already_in_destination"):
            continue
        client.values_update(
            day_tab_block(dst_name, DAY_COL_STATUS, DAY_COL_LAST, m["dst_row"], m["dst_row"]),
            [m["payload"]],
        )

    src_tab = find_day_tab(meta, src_name)
    clear_reqs = []
    for m in planned:
        clear_reqs.append({
            "repeatCell": {
                "range": {
                    "sheetId": src_tab["sheetId"],
                    "startRowIndex": m["src_row"] - 1,
                    "endRowIndex": m["src_row"],
                    "startColumnIndex": DAY_COL_STATUS,
                    "endColumnIndex": DAY_COL_LAST + 1,
                },
                "cell": {"userEnteredValue": {"stringValue": ""}},
                "fields": "userEnteredValue",
            }
        })
        clear_reqs.append({
            "updateCells": {
                "rows": [{"values": [{"userEnteredValue": {"boolValue": False}}]}],
                "fields": "userEnteredValue",
                "start": {
                    "sheetId": src_tab["sheetId"],
                    "rowIndex": m["src_row"] - 1,
                    "columnIndex": DAY_COL_STATUS,
                },
            }
        })
    client.batch_update(clear_reqs)
    pack_summary = _pack_day_tab_checked_rows(client, src_name)

    trace("carry-forward-day", f"{src_name.lower()}-to-{dst_name.lower()}", [
        f"- moved: {len(planned)}",
        f"- source: {src_name}",
        f"- destination: {dst_name}",
        f"- source packed: {pack_summary}",
        f"- snapshot: {snap}",
        "",
        *[
            (
                f"- {src_name} slot {m['src_slot']} already existed on {dst_name}; cleared source: {m['task']}"
                if m.get("already_in_destination")
                else f"- {src_name} slot {m['src_slot']} → {dst_name} slot {m['dst_slot']}: {m['task']}"
            )
            for m in planned
        ],
    ])
    print(
        f"task-tracker-manager: carry-forward-day complete — moved {len(planned)} "
        f"item(s) {src_name} → {dst_name}; packed {src_name} checked rows to top"
    )
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
    pr.add_argument("--slot", type=int, required=True, help="1..25")
    pr.set_defaults(func=cmd_promote)

    bw = sub.add_parser("build-week",
                        help="Sunday rebuild ceremony — archive + clear + re-title "
                             "the WEEK PLANNING TAB + stamp Recurring onto it. "
                             "Day tabs untouched (use distribute-week after).")
    bw.add_argument("--skip-recurring", action="store_true",
                    help="bypass the Recurring Template stamp step (rare)")
    bw.add_argument("--skip-carryover", action="store_true",
                    help="bypass the incomplete-day-tab carryover pull (added 2026-05-26)")
    bw.add_argument("--dry-run", action="store_true",
                    help="report what would happen without writing — no copy, no archive, no clear, no stamp, no carryover")
    bw.add_argument("--legacy", action="store_true",
                    help="use pre-2026-05-26 in-place rebuild (archive tab inside same sheet, no new file). Recovery only.")
    bw.add_argument("--title-prefix", default="",
                    help="prefix the new file's title (sandbox testing — e.g., '[SANDBOX] ')")
    bw.add_argument("--no-pointer-update", action="store_true",
                    help="skip pointer update — leaves resolver pointing at prior file (sandbox testing)")
    bw.add_argument("--no-folder-move", action="store_true",
                    help="skip moving the prior file into To Do Archive (sandbox testing)")
    bw.add_argument("--force-new-file", action="store_true",
                    help="allow creating a duplicate target weekly file. Testing only; routine runs should refuse duplicates.")
    bw.add_argument("--refresh-pointer", action="store_true",
                    help="force Drive search before resolving the prior file. Recovery only; routine runs trust the pointer.")
    bw.set_defaults(func=cmd_build_week)

    sfd = sub.add_parser("schedule-from-todo-days",
                         help="Populate the Week tab from To Do column H Day of the Week assignments.")
    sfd.add_argument("--dry-run", action="store_true",
                     help="report what would be written without changing the Week tab")
    sfd.set_defaults(func=cmd_schedule_from_todo_days)

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
                     help="source slot 1..25 (also dest slot if --to-slot omitted)")
    mdi.add_argument("--to", dest="to_day", default=None,
                     help="dest day tab (Sun..Sat); required unless --state deleted")
    mdi.add_argument("--to-slot", type=int, default=None,
                     help="dest slot 1..25; omit to auto-pick first empty")
    mdi.add_argument("--state", required=True,
                     choices=["completed", "incomplete", "added", "deleted"])
    mdi.add_argument("--task", default=None, help="required for --state added")
    mdi.add_argument("--type", default="")
    mdi.add_argument("--project", default="")
    mdi.add_argument("--notes", default="")
    mdi.add_argument("--force", action="store_true",
                     help="overwrite an occupied dest slot")
    mdi.set_defaults(func=cmd_move_day_item)

    cf = sub.add_parser("carry-forward-day",
                        help="Move all incomplete items from one day tab to the next day's empty slots.")
    cf.add_argument("--from", dest="from_day", default=None,
                    help="source day tab (default: today)")
    cf.add_argument("--to", dest="to_day", default=None,
                    help="destination day tab (default: tomorrow)")
    cf.add_argument("--date", default=None,
                    help="closeout date YYYY-MM-DD; default uses NY operating date, treating before 4am as prior day")
    cf.add_argument("--dry-run", action="store_true",
                    help="show planned carry-forward moves without writing")
    cf.set_defaults(func=cmd_carry_forward_day)

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
                    help="1..25; omit for auto-pick first empty slot on that day")
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
                     help="1..25; if omitted, auto-pick first empty slot")
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

    ct = sub.add_parser("compact-todo",
                        help="Remove empty/leftover gap rows from the To Do tab and "
                             "pack real rows to the top (snapshot+trace; runs inside build-week).")
    ct.add_argument("--dry-run", action="store_true",
                    help="report real/gap counts without writing")
    ct.add_argument("--buffer", type=int, default=40,
                    help="blank validated rows to retain below content for future appends (default 40)")
    ct.set_defaults(func=cmd_compact_todo)

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
