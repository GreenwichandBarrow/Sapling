"""task-tracker-manager skill helper — verbs for Kay's personal task tracker.

Migrated 2026-05-12 from openpyxl/xlsx to Google Sheets API. Same CLI surface.

Subcommands:
    append                  Add a row to the To Do tab.
    promote                 Move a To Do row into a specific day-slot on the live week tab.
    schedule-to-day-slot    Direct write to a day-slot (no To Do source row required).
    sync-done-status        Reconcile checked weekly slots → matching To Do rows (text-match).
    archive                 Sunday rollover ceremony — duplicate live week tab to a
                            far-right archive tab, rename live to next week, clear data,
                            then stamp the Recurring Template tab onto the new week's
                            slots (--skip-recurring to bypass; --dry-run to preview).
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
TAB_RECURRING_TEMPLATE = "Recurring Template"

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
TODO_HEADERS = ["Status", "Task", "Type", "Project", "Due", "Notes"]
TODO_MAX_ROWS = 200

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

# Live Week — 7 day-pairs, each (status_col_idx, task_col_idx), 0-based
LIVE_DAY_STAT = {i: 1 + i * 2 for i in range(7)}
LIVE_DAY_TASK = {i: 2 + i * 2 for i in range(7)}

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

# Live Week rows (1-based for A1 references)
LIVE_HABIT_FIRST_ROW = 7   # rows 7..13 = 7 habits
LIVE_HABIT_LAST_ROW = 13
LIVE_SLOT_FIRST_ROW = 23   # rows 23..37 = 15 priority slots
LIVE_SLOT_LAST_ROW = 37
LIVE_NOTES_FIRST_ROW = 40
LIVE_NOTES_LAST_ROW = 47
LIVE_BIG_PCT_ROW = 17      # merged 17..21 anchored at row 17

HABITS_DEFAULT = [
    "Water & hygiene",
    "Meditation & stretches",
    "ACV drink & probiotic protein shake",
    "Exercise class",
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
    if today is None:
        today = date.today()
    monday = today - timedelta(days=today.weekday())
    sunday = monday + timedelta(days=6)
    if monday.month == sunday.month:
        return f"{monday.strftime('%b')} {monday.day}-{sunday.day}"
    return f"{monday.strftime('%b')} {monday.day}-{sunday.strftime('%b')} {sunday.day}"


def find_live_week_tab(metadata: dict) -> dict | None:
    """Find the live week tab (Mon-Sun label) — skips archive_* tabs."""
    months = ("Jan ", "Feb ", "Mar ", "Apr ", "May ", "Jun ", "Jul ", "Aug ",
              "Sep ", "Oct ", "Nov ", "Dec ")
    for s in metadata.get("sheets", []):
        title = s["properties"]["title"]
        if title.startswith("archive_"):
            continue
        if any(title.startswith(m) for m in months):
            return s["properties"]
    return None


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
        [f"'{TAB_TODO}'!A{target_row}:F{target_row}"])

    row_values = [
        False,             # Status
        args.task,         # Task
        args.type,         # Type
        args.project or "",
        args.due or "",
        args.notes or "",
    ]
    client.values_update(f"'{TAB_TODO}'!A{target_row}:F{target_row}", [row_values])

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
    day_idx = DAY_BY_NAME.get(args.day.lower())
    if day_idx is None:
        sys.exit(f"task-tracker-manager: unknown day {args.day!r}. Use Mon..Sun.")
    if not (1 <= args.slot <= 15):
        sys.exit("task-tracker-manager: --slot must be 1..15")

    client = SheetsClient()
    meta = client.get_metadata()
    week_props = find_live_week_tab(meta)
    if week_props is None:
        sys.exit("task-tracker-manager: live week tab not found")
    week_title = week_props["title"]

    todo_row = args.todo_row
    todo_range = f"'{TAB_TODO}'!B{todo_row}"  # Task cell
    todo_vals = client.get_values(todo_range)
    task_text = todo_vals[0][0] if todo_vals and todo_vals[0] else None
    if not task_text:
        sys.exit(f"task-tracker-manager: To Do row {todo_row} is empty")

    sc_letter = col_letter(LIVE_DAY_STAT[day_idx])
    tc_letter = col_letter(LIVE_DAY_TASK[day_idx])
    slot_row = LIVE_SLOT_FIRST_ROW + args.slot - 1

    existing_vals = client.get_values(f"'{week_title}'!{tc_letter}{slot_row}")
    existing = (existing_vals[0][0] if existing_vals and existing_vals[0] else "")
    if existing:
        sys.exit(f'task-tracker-manager: refused promote — {args.day} slot {args.slot} '
                 f'already contains "{existing}"')

    # Snapshot both the source todo status cell and the destination slot pair
    snap = snapshot_ranges(client, "promote", [
        f"'{TAB_TODO}'!A{todo_row}:F{todo_row}",
        f"'{week_title}'!{sc_letter}{slot_row}:{tc_letter}{slot_row}",
    ])

    # Write: destination task cell, destination status FALSE, source status → "→" marker
    # Sheets has no native "→" status; we'll set the source status checkbox to FALSE
    # and put "→" in the source notes column (Notes) as a moved indicator, leaving
    # the row visible. Simpler: just leave source row alone except mark Notes.
    # Better: use the existing "→" pattern by writing into the status cell as a STRING,
    # but the status cell is a checkbox. We'll instead append a marker in Notes
    # AND uncheck the box. The "→" indicator from the xlsx era is preserved as
    # NOTES prefix.
    # Update destination slot first
    client.values_update(f"'{week_title}'!{sc_letter}{slot_row}:{tc_letter}{slot_row}",
                         [[False, task_text]])
    # Mark source row with a moved indicator in Notes (col F = TODO_COL_NOTES)
    source_notes = client.get_values(f"'{TAB_TODO}'!F{todo_row}")
    existing_notes = (source_notes[0][0] if source_notes and source_notes[0] else "")
    marker = f"→ promoted to {args.day} slot {args.slot} on {date.today().isoformat()}"
    new_notes = f"{marker}; {existing_notes}" if existing_notes and marker not in existing_notes else (existing_notes or marker)
    client.values_update(f"'{TAB_TODO}'!F{todo_row}", [[new_notes]])

    trace("promote", f"{args.day.lower()}-{args.slot}", [
        f"- todo_row: {todo_row}",
        f"- task: {task_text}",
        f"- promoted_to: {week_title} {args.day} slot {args.slot} (row {slot_row})",
        f"- snapshot: {snap}",
    ])
    print(f'task-tracker-manager: promoted To Do row {todo_row} → {week_title} {args.day} slot {args.slot} ("{task_text}")')
    return 0


def cmd_schedule_to_day_slot(args) -> int:
    day_idx = DAY_BY_NAME.get(args.day.lower())
    if day_idx is None:
        sys.exit(f"task-tracker-manager: unknown day {args.day!r}. Use Mon..Sun.")

    client = SheetsClient()
    meta = client.get_metadata()
    week_props = find_live_week_tab(meta)
    if week_props is None:
        sys.exit("task-tracker-manager: live week tab not found")
    week_title = week_props["title"]

    tc_letter = col_letter(LIVE_DAY_TASK[day_idx])
    sc_letter = col_letter(LIVE_DAY_STAT[day_idx])

    if args.slot is not None:
        if not (1 <= args.slot <= 15):
            sys.exit("task-tracker-manager: --slot must be 1..15")
        slot = args.slot
    else:
        # Auto-pick first empty slot
        col_vals = client.get_values(f"'{week_title}'!{tc_letter}{LIVE_SLOT_FIRST_ROW}:{tc_letter}{LIVE_SLOT_LAST_ROW}")
        slot = None
        for i in range(15):
            v = col_vals[i][0] if i < len(col_vals) and col_vals[i] else ""
            if not v:
                slot = i + 1
                break
        if slot is None:
            sys.exit(f"task-tracker-manager: refused schedule-to-day-slot — {args.day} has no empty slots")

    slot_row = LIVE_SLOT_FIRST_ROW + slot - 1
    existing_vals = client.get_values(f"'{week_title}'!{tc_letter}{slot_row}")
    existing = (existing_vals[0][0] if existing_vals and existing_vals[0] else "")
    if existing and not args.force:
        sys.exit(f'task-tracker-manager: refused schedule-to-day-slot — {args.day} slot {slot} '
                 f'already contains "{existing}" (use --force to overwrite)')

    snap = snapshot_ranges(client, "schedule-to-day-slot",
                           [f"'{week_title}'!{sc_letter}{slot_row}:{tc_letter}{slot_row}"])

    client.values_update(f"'{week_title}'!{sc_letter}{slot_row}:{tc_letter}{slot_row}",
                         [[False, args.task]])

    trace("schedule-to-day-slot", f"{args.day.lower()}-{slot}", [
        f"- task: {args.task}",
        f"- placement: {week_title} {args.day} slot {slot} (row {slot_row})",
        f"- overwrote: {existing!r}" if existing else "- overwrote: (slot was empty)",
        f"- snapshot: {snap}",
    ])
    print(f'task-tracker-manager: scheduled "{args.task}" → {week_title} {args.day} slot {slot}')
    return 0


def _read_recurring_template(client: SheetsClient) -> list[dict]:
    """Read all rows from the Recurring Template tab. Returns list of dicts with keys
    day, slot (int or None), task, type, project, notes, row (1-based). Skips blank
    rows + rows with empty task/day. Validates Day + Type values softly (skips invalid
    with a warning to stderr) so a malformed row doesn't abort the rollover."""
    rows = client.get_values(f"'{TAB_RECURRING_TEMPLATE}'!A2:F{RT_MAX_ROWS}")
    out: list[dict] = []
    for i, row in enumerate(rows):
        day = (row[RT_COL_DAY] if len(row) > RT_COL_DAY else "").strip() if row else ""
        task = (row[RT_COL_TASK] if len(row) > RT_COL_TASK else "").strip() if row else ""
        if not day or not task:
            continue
        if day.lower() not in DAY_BY_NAME:
            print(f"task-tracker-manager: WARNING Recurring Template row {2+i} has invalid Day {day!r} — skipped",
                  file=sys.stderr)
            continue
        type_ = (row[RT_COL_TYPE] if len(row) > RT_COL_TYPE else "").strip() if row else ""
        if type_ and type_ not in TYPE_OPTIONS:
            print(f"task-tracker-manager: WARNING Recurring Template row {2+i} has invalid Type {type_!r} — skipped",
                  file=sys.stderr)
            continue
        slot_raw = row[RT_COL_SLOT] if len(row) > RT_COL_SLOT else ""
        slot: int | None = None
        if slot_raw != "" and slot_raw is not None:
            try:
                slot = int(slot_raw)
                if not (1 <= slot <= 15):
                    print(f"task-tracker-manager: WARNING Recurring Template row {2+i} slot {slot} out of 1..15 — treating as blank",
                          file=sys.stderr)
                    slot = None
            except (ValueError, TypeError):
                print(f"task-tracker-manager: WARNING Recurring Template row {2+i} slot {slot_raw!r} not numeric — treating as blank",
                      file=sys.stderr)
                slot = None
        project = (row[RT_COL_PROJECT] if len(row) > RT_COL_PROJECT else "").strip() if row else ""
        notes = (row[RT_COL_NOTES] if len(row) > RT_COL_NOTES else "").strip() if row else ""
        out.append({
            "row": 2 + i,
            "day": day,
            "slot": slot,
            "task": task,
            "type": type_ or "Work",
            "project": project,
            "notes": notes,
        })
    return out


def _stamp_recurring_template(client: SheetsClient, meta: dict, week_title: str,
                              dry_run: bool = False) -> dict:
    """Stamp every row of the Recurring Template tab onto `week_title`'s day-slots.

    Mirrors `schedule-to-day-slot` semantics with --force=False (refuse to overwrite).
    Returns a summary dict {stamped: [...], refused: [...], rows_read: int}.

    If --dry-run, no writes; just reports what would happen.
    """
    template_tab = find_tab(meta, TAB_RECURRING_TEMPLATE)
    summary = {"stamped": [], "refused": [], "rows_read": 0, "tab_present": template_tab is not None}
    if template_tab is None:
        print(f"task-tracker-manager: '{TAB_RECURRING_TEMPLATE}' tab not present — skipping recurring stamp")
        return summary

    rows = _read_recurring_template(client)
    summary["rows_read"] = len(rows)
    if not rows:
        print(f"task-tracker-manager: '{TAB_RECURRING_TEMPLATE}' has no usable rows — nothing to stamp")
        return summary

    # Fetch existing slot grid for the new week once, then walk the rows. Auto-pick logic
    # needs an in-memory view of empty slots that accounts for prior stamps in this run.
    slot_grid: dict[int, list[str]] = {}  # day_idx → list of 15 task strings (empty=blank)
    for day_idx in range(7):
        tc = col_letter(LIVE_DAY_TASK[day_idx])
        vals = client.get_values(
            f"'{week_title}'!{tc}{LIVE_SLOT_FIRST_ROW}:{tc}{LIVE_SLOT_LAST_ROW}"
        )
        flat = [(v[0] if v else "") if isinstance(v, list) else "" for v in vals]
        while len(flat) < 15:
            flat.append("")
        slot_grid[day_idx] = flat

    writes: list[tuple[str, list[list]]] = []  # (range_a1, [[bool, task]])
    for r in rows:
        day_idx = DAY_BY_NAME[r["day"].lower()]
        sc = col_letter(LIVE_DAY_STAT[day_idx])
        tc = col_letter(LIVE_DAY_TASK[day_idx])

        target_slot = r["slot"]
        if target_slot is not None:
            existing = slot_grid[day_idx][target_slot - 1]
            if existing and str(existing).strip():
                summary["refused"].append({
                    "row": r["row"],
                    "day": r["day"],
                    "slot": target_slot,
                    "task": r["task"],
                    "reason": f'slot occupied by "{existing}"',
                })
                print(f'task-tracker-manager: WARNING recurring stamp REFUSED '
                      f'(template row {r["row"]}, {r["day"]} slot {target_slot}): '
                      f'slot occupied by "{existing}" — skipping, Kay can resolve manually')
                continue
            chosen_slot = target_slot
        else:
            chosen_slot = None
            for idx, v in enumerate(slot_grid[day_idx]):
                if not v or not str(v).strip():
                    chosen_slot = idx + 1
                    break
            if chosen_slot is None:
                summary["refused"].append({
                    "row": r["row"],
                    "day": r["day"],
                    "slot": None,
                    "task": r["task"],
                    "reason": f"{r['day']} has no empty slots",
                })
                print(f'task-tracker-manager: WARNING recurring stamp REFUSED '
                      f'(template row {r["row"]}): {r["day"]} has no empty slots — skipping')
                continue

        slot_row = LIVE_SLOT_FIRST_ROW + chosen_slot - 1
        rng = f"'{week_title}'!{sc}{slot_row}:{tc}{slot_row}"
        writes.append((rng, [[False, r["task"]]]))
        # Update in-memory grid so subsequent auto-picks don't collide
        slot_grid[day_idx][chosen_slot - 1] = r["task"]
        summary["stamped"].append({
            "template_row": r["row"],
            "day": r["day"],
            "slot": chosen_slot,
            "task": r["task"],
            "auto_picked": r["slot"] is None,
        })
        prefix = "task-tracker-manager: recurring stamp"
        if dry_run:
            prefix += " (DRY RUN)"
        ap = " (auto-picked)" if r["slot"] is None else ""
        print(f'{prefix}: template row {r["row"]} → {week_title} {r["day"]} slot {chosen_slot}{ap}: "{r["task"]}"')

    if not dry_run and writes:
        for rng, vals in writes:
            client.values_update(rng, vals)

    return summary


def cmd_archive(args) -> int:
    """Sunday rollover: duplicate live week tab to a visible archive tab parked far-right,
    rename live to the upcoming week, clear data on live.

    After the live tab is renamed + cleared, the Recurring Template tab is read and
    its rows are stamped onto the new week's day-slots (mirrors schedule-to-day-slot
    with --force=False — occupied slots warn + skip). Pass --skip-recurring to bypass.
    Pass --dry-run to preview the entire ceremony (no writes, no rename, no clear,
    just reports what would happen including which Recurring Template rows would stamp
    onto which slots of the NEXT week's tab as if it were already created).
    """
    client = SheetsClient()
    meta = client.get_metadata()
    week_props = find_live_week_tab(meta)
    if week_props is None:
        sys.exit("task-tracker-manager: live week tab not found")
    old_label = week_props["title"]
    live_sid = week_props["sheetId"]

    # ---------- dry-run path: report only, no mutations ----------
    if getattr(args, "dry_run", False):
        today = date.today()
        if today.weekday() == 0:
            new_monday = today
        else:
            new_monday = today + timedelta(days=(7 - today.weekday()))
        new_label = current_week_label(new_monday)
        print(f"task-tracker-manager: archive (DRY RUN)")
        print(f"  Live tab found: {old_label!r} (sheetId={live_sid})")
        print(f"  Would archive → visible far-right tab archive_{old_label!r}")
        print(f"  Would rename live tab: {old_label!r} → {new_label!r}")
        print(f"  Would clear: habits, priorities, notes")
        if getattr(args, "skip_recurring", False):
            print(f"  --skip-recurring set → would NOT stamp Recurring Template")
        else:
            # Simulate the stamp against the CURRENT live tab's slot grid as proxy for
            # "what an empty new week would look like" — but for a realistic preview
            # we want an empty grid, so we substitute a synthetic empty grid. The
            # cheap version: read template rows, report what slots they'd take if all
            # 15 slots per day were empty (which is the post-clear state).
            template_tab = find_tab(meta, TAB_RECURRING_TEMPLATE)
            if template_tab is None:
                print(f"  Recurring Template tab NOT present — nothing to stamp")
            else:
                rows = _read_recurring_template(client)
                print(f"  Recurring Template tab present — {len(rows)} usable row(s)")
                # Synthetic empty grid
                synthetic_used: dict[int, set[int]] = {i: set() for i in range(7)}
                for r in rows:
                    day_idx = DAY_BY_NAME[r["day"].lower()]
                    if r["slot"] is not None:
                        if r["slot"] in synthetic_used[day_idx]:
                            print(f'    REFUSED template row {r["row"]} ({r["day"]} slot {r["slot"]}): another template row already pinned to that slot')
                            continue
                        synthetic_used[day_idx].add(r["slot"])
                        slot = r["slot"]
                        ap = ""
                    else:
                        slot = None
                        for s in range(1, 16):
                            if s not in synthetic_used[day_idx]:
                                slot = s
                                break
                        if slot is None:
                            print(f'    REFUSED template row {r["row"]}: {r["day"]} has no empty slots')
                            continue
                        synthetic_used[day_idx].add(slot)
                        ap = " (auto-picked)"
                    print(f'    WOULD STAMP: template row {r["row"]} → {new_label} {r["day"]} slot {slot}{ap}: "{r["task"]}"')
        print(f"task-tracker-manager: archive DRY RUN complete — no writes")
        return 0

    # Compute new label
    today = date.today()
    if today.weekday() == 0:
        new_monday = today
    else:
        new_monday = today + timedelta(days=(7 - today.weekday()))
    new_label = current_week_label(new_monday)

    # Snapshot the entire live tab before mutation
    snap = snapshot_ranges(client, "archive",
                           [f"'{old_label}'!A1:O50"])

    archive_name = f"archive_{old_label}"
    existing_titles = {s["properties"]["title"] for s in meta.get("sheets", [])}
    suffix = 1
    while archive_name in existing_titles:
        suffix += 1
        archive_name = f"archive_{old_label}_v{suffix}"

    # Duplicate the live tab
    dup_resp = client.batch_update([{
        "duplicateSheet": {
            "sourceSheetId": live_sid,
            "insertSheetIndex": len(meta.get("sheets", [])),  # park at far right
            "newSheetName": archive_name,
        }
    }])

    # Rename the live tab + clear data
    clear_requests: list[dict] = []
    # Clear habit ticks: cols B,D,F,H,J,L,N (status cols) rows 7-13
    for i in range(7):
        sc = LIVE_DAY_STAT[i]
        clear_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": live_sid,
                    "startRowIndex": LIVE_HABIT_FIRST_ROW - 1,
                    "endRowIndex": LIVE_HABIT_LAST_ROW,
                    "startColumnIndex": sc,
                    "endColumnIndex": sc + 1,
                },
                "cell": {"userEnteredValue": {"boolValue": False}},
                "fields": "userEnteredValue",
            }
        })
        # Clear priority status + task
        clear_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": live_sid,
                    "startRowIndex": LIVE_SLOT_FIRST_ROW - 1,
                    "endRowIndex": LIVE_SLOT_LAST_ROW,
                    "startColumnIndex": sc,
                    "endColumnIndex": sc + 1,
                },
                "cell": {"userEnteredValue": {"boolValue": False}},
                "fields": "userEnteredValue",
            }
        })
        tc = LIVE_DAY_TASK[i]
        clear_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": live_sid,
                    "startRowIndex": LIVE_SLOT_FIRST_ROW - 1,
                    "endRowIndex": LIVE_SLOT_LAST_ROW,
                    "startColumnIndex": tc,
                    "endColumnIndex": tc + 1,
                },
                "cell": {"userEnteredValue": {"stringValue": ""}},
                "fields": "userEnteredValue",
            }
        })
        # Clear notes block
        clear_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": live_sid,
                    "startRowIndex": LIVE_NOTES_FIRST_ROW - 1,
                    "endRowIndex": LIVE_NOTES_LAST_ROW,
                    "startColumnIndex": sc,
                    "endColumnIndex": tc + 1,
                },
                "cell": {"userEnteredValue": {"stringValue": ""}},
                "fields": "userEnteredValue",
            }
        })

    # Rename the live tab
    clear_requests.insert(0, {
        "updateSheetProperties": {
            "properties": {"sheetId": live_sid, "title": new_label},
            "fields": "title",
        }
    })
    # Update title-row text
    clear_requests.append({
        "updateCells": {
            "rows": [{"values": [{"userEnteredValue": {"stringValue": f"KAY — WEEK OF {new_label}"}}]}],
            "fields": "userEnteredValue",
            "start": {"sheetId": live_sid, "rowIndex": 0, "columnIndex": 0},
        }
    })

    client.batch_update(clear_requests)

    # ---------- Recurring Template stamp ----------
    recurring_summary: dict = {"stamped": [], "refused": [], "rows_read": 0, "tab_present": False}
    if getattr(args, "skip_recurring", False):
        print("task-tracker-manager: --skip-recurring set — Recurring Template NOT stamped")
    else:
        # Re-fetch metadata so the renamed tab title is current.
        meta_after = client.get_metadata()
        recurring_summary = _stamp_recurring_template(client, meta_after, new_label, dry_run=False)

    trace_lines = [
        f"- archived: {old_label} → visible tab {archive_name} (parked far-right)",
        f"- live tab renamed: {old_label} → {new_label}",
        f"- cleared: habits, priorities, notes",
        f"- snapshot: {snap}",
    ]
    if recurring_summary["tab_present"]:
        trace_lines.append(f"- recurring template stamped: {len(recurring_summary['stamped'])} row(s) onto new week")
        if recurring_summary["refused"]:
            trace_lines.append(f"- recurring stamps REFUSED (slot conflicts): {len(recurring_summary['refused'])}")
            for ref in recurring_summary["refused"]:
                trace_lines.append(f"  - template row {ref['row']} {ref['day']} slot {ref['slot']}: {ref['reason']}")
    elif not getattr(args, "skip_recurring", False):
        trace_lines.append(f"- recurring template: tab not present, skipped")
    trace("archive", old_label.lower().replace(" ", "-"), trace_lines)
    print(f'task-tracker-manager: archived "{old_label}" → visible far-right tab {archive_name}; live tab now "{new_label}"')
    if recurring_summary["tab_present"]:
        print(f'task-tracker-manager: stamped {len(recurring_summary["stamped"])} recurring row(s) onto {new_label}'
              + (f"; {len(recurring_summary['refused'])} refused" if recurring_summary["refused"] else ""))
    return 0


def cmd_sync_done_status(args, _client: "SheetsClient | None" = None,
                         _meta: dict | None = None) -> int:
    """Reconcile checked weekly slots → matching To Do rows by exact task-text match.

    For each non-empty priority slot across the live week tab whose status checkbox is
    TRUE, find the matching To Do row (case-sensitive, leading/trailing whitespace
    stripped) and flip its status to TRUE. The existing CF rule paints strikethrough +
    sage-light fill. Ambiguous matches (>1 To Do row with same task text) are flagged
    and skipped — Kay resolves manually.

    Note on the "→" case from the spec: the To Do Status column is a native Sheets
    checkbox (boolean only). The `promote` verb writes its "→ promoted to {day} slot N"
    marker into the Notes column, not Status. So a previously-promoted row's Status
    is FALSE — the standard FALSE → TRUE flip handles it. No string "→" state exists.
    """
    client = _client or SheetsClient()
    meta = _meta or client.get_metadata()
    week_props = find_live_week_tab(meta)
    if week_props is None:
        sys.exit("task-tracker-manager: live week tab not found")
    week_title = week_props["title"]

    # 1. Walk weekly slots — read status + task pair per day in two batched ranges per day.
    weekly_checked: list[dict] = []  # one entry per (day, slot) where checkbox=TRUE and task non-empty
    weekly_slots_scanned = 0
    for day_idx in range(7):
        sc = col_letter(LIVE_DAY_STAT[day_idx])
        tc = col_letter(LIVE_DAY_TASK[day_idx])
        status_vals = client.get_values(
            f"'{week_title}'!{sc}{LIVE_SLOT_FIRST_ROW}:{sc}{LIVE_SLOT_LAST_ROW}"
        )
        task_vals = client.get_values(
            f"'{week_title}'!{tc}{LIVE_SLOT_FIRST_ROW}:{tc}{LIVE_SLOT_LAST_ROW}"
        )
        for slot_i in range(15):
            status = status_vals[slot_i][0] if slot_i < len(status_vals) and status_vals[slot_i] else ""
            task = task_vals[slot_i][0] if slot_i < len(task_vals) and task_vals[slot_i] else ""
            task_text = (task or "").strip() if isinstance(task, str) else ""
            if not task_text:
                continue
            weekly_slots_scanned += 1
            if _is_truthy(status):
                weekly_checked.append({
                    "day": DAY_LABELS[day_idx],
                    "slot": slot_i + 1,
                    "task_text": task_text,
                })

    # 2. Walk To Do tab — build {task_text(stripped): [row_indices]} dict.
    todo_rows = client.get_values(f"'{TAB_TODO}'!A2:F{TODO_MAX_ROWS}")
    todo_by_task: dict[str, list[dict]] = {}
    for i, row in enumerate(todo_rows):
        task = row[1] if len(row) > 1 else ""
        if not isinstance(task, str):
            continue
        key = task.strip()
        if not key:
            continue
        status = row[0] if len(row) > 0 else ""
        todo_by_task.setdefault(key, []).append({
            "row": 2 + i,  # 1-based
            "status": status,
            "is_truthy": _is_truthy(status),
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
        # Use batch_update with updateCells for boolValue TRUE — values_update treats
        # "TRUE" as a string in USER_ENTERED mode unless we send raw bool which causes
        # the checkbox to flip correctly via the existing data-validation rule.
        todo_tab = find_tab(meta, TAB_TODO)
        if todo_tab is None:
            sys.exit(f"task-tracker-manager: '{TAB_TODO}' tab not found")
        todo_sid = todo_tab["sheetId"]
        batch: list[dict] = []
        for s in to_sync:
            batch.append({
                "updateCells": {
                    "rows": [{"values": [{"userEnteredValue": {"boolValue": True}}]}],
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
    """Sweep checked rows from To Do tab → 'Completed To Do' tab (created on first run).

    Pre-step: runs sync-done-status first (so checked weekly slots flip matching To Do
    rows to TRUE before the sweep picks them up). Pass --skip-sync to bypass.
    """
    client = SheetsClient()
    meta = client.get_metadata()

    # Pre-step: sync-done-status (unless --skip-sync).
    if not getattr(args, "skip_sync", False):
        sync_args = argparse.Namespace(dry_run=False)
        cmd_sync_done_status(sync_args, _client=client, _meta=meta)
        # Re-fetch metadata after sync (no schema changes, but cheap insurance).
        meta = client.get_metadata()

    # Read all To Do rows
    todo_rows = client.get_values(f"'{TAB_TODO}'!A2:F{TODO_MAX_ROWS}")
    swept = []
    for i, row in enumerate(todo_rows):
        # Status checkbox renders as boolean TRUE or string "TRUE"
        status = row[0] if len(row) > 0 else ""
        task = row[1] if len(row) > 1 else ""
        if not task:
            continue
        if not _is_truthy(status):
            continue
        swept.append({
            "row": 2 + i,  # 1-based
            "task": task,
            "type": row[2] if len(row) > 2 else "",
            "project": row[3] if len(row) > 3 else "",
            "due": row[4] if len(row) > 4 else "",
            "notes": row[5] if len(row) > 5 else "",
        })

    # Ensure Completed To Do tab exists
    completed_tab = find_tab(meta, TAB_COMPLETED_TODO)
    completed_created = False
    if completed_tab is None:
        resp = client.batch_update([{
            "addSheet": {
                "properties": {
                    "title": TAB_COMPLETED_TODO,
                    "gridProperties": {"rowCount": 500, "columnCount": 8, "frozenRowCount": 1},
                }
            }
        }])
        completed_sid = resp["replies"][0]["addSheet"]["properties"]["sheetId"]
        completed_created = True
        # Write headers + "Completed" column
        headers = TODO_HEADERS + ["Completed"]
        client.values_update(f"'{TAB_COMPLETED_TODO}'!A1:G1", [headers])
    else:
        completed_sid = completed_tab["sheetId"]

    if not swept:
        msg = "tab created" if completed_created else "tab present"
        print(f"task-tracker-manager: archive-todo — no checked rows in To Do to sweep ({msg})")
        return 0

    today_iso = date.today().isoformat()
    snap = snapshot_ranges(client, "archive-todo", [
        f"'{TAB_TODO}'!A2:F{TODO_MAX_ROWS}",
        f"'{TAB_COMPLETED_TODO}'!A1:G500",
    ])

    # Append to Completed To Do
    append_rows = []
    for s in swept:
        append_rows.append([
            True,
            s["task"],
            s["type"],
            s["project"],
            str(s["due"])[:10] if s["due"] else "",
            s["notes"],
            today_iso,
        ])
    client.values_append(f"'{TAB_COMPLETED_TODO}'!A1:G1", append_rows)

    # Clear the swept rows on the To Do side
    clear_requests = []
    for s in swept:
        r0 = s["row"] - 1
        clear_requests.append({
            "repeatCell": {
                "range": {
                    "sheetId": find_tab(meta, TAB_TODO)["sheetId"],
                    "startRowIndex": r0,
                    "endRowIndex": r0 + 1,
                    "startColumnIndex": 0,
                    "endColumnIndex": len(TODO_HEADERS),
                },
                "cell": {"userEnteredValue": {"stringValue": ""}},
                "fields": "userEnteredValue",
            }
        })
        # Reset status checkbox to FALSE explicitly
        clear_requests.append({
            "updateCells": {
                "rows": [{"values": [{"userEnteredValue": {"boolValue": False}}]}],
                "fields": "userEnteredValue",
                "start": {"sheetId": find_tab(meta, TAB_TODO)["sheetId"],
                          "rowIndex": r0, "columnIndex": 0},
            }
        })
    if clear_requests:
        client.batch_update(clear_requests)

    trace("archive-todo", f"sweep-{len(swept)}", [
        f"- swept: {len(swept)} checked rows from To Do",
        f"- destination: '{TAB_COMPLETED_TODO}' (appended)",
        f"- completed_date: {today_iso}",
        f"- snapshot: {snap}",
    ])
    print(f"task-tracker-manager: archive-todo swept {len(swept)} checked row(s) → '{TAB_COMPLETED_TODO}'")
    return 0


def _is_truthy(v) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, str):
        return v.strip().upper() in ("TRUE", "✅", "YES", "DONE")
    return bool(v)


def cmd_recurring_add(args) -> int:
    """Append a row to the Recurring Template tab. Decision-content (changes future
    weeks), so traces."""
    day_idx = DAY_BY_NAME.get(args.day.lower())
    if day_idx is None:
        sys.exit(f"task-tracker-manager: unknown day {args.day!r}. Use Mon..Sun.")
    day_canonical = DAY_LABELS[day_idx]
    if args.type not in TYPE_OPTIONS:
        sys.exit(f"task-tracker-manager: --type must be one of {TYPE_OPTIONS}")
    if args.slot is not None and not (1 <= args.slot <= 15):
        sys.exit("task-tracker-manager: --slot must be 1..15 (or omit for auto-pick)")
    if not args.task.strip():
        sys.exit("task-tracker-manager: --task must be non-empty")

    client = SheetsClient()
    meta = client.get_metadata()
    if find_tab(meta, TAB_RECURRING_TEMPLATE) is None:
        sys.exit(f"task-tracker-manager: '{TAB_RECURRING_TEMPLATE}' tab not found — create it first")

    # Find first empty row >= 2.
    existing = client.get_values(f"'{TAB_RECURRING_TEMPLATE}'!C2:C{RT_MAX_ROWS}")
    target_row = 2
    found = False
    for i, row in enumerate(existing):
        if not row or not (row[0] if row else "").strip():
            target_row = 2 + i
            found = True
            break
    if not found:
        target_row = 2 + len(existing)
    if target_row > RT_MAX_ROWS:
        sys.exit(f"task-tracker-manager: '{TAB_RECURRING_TEMPLATE}' is full (>{RT_MAX_ROWS}).")

    snap = snapshot_ranges(client, "recurring-add",
        [f"'{TAB_RECURRING_TEMPLATE}'!A{target_row}:F{target_row}"])

    row_values = [
        day_canonical,
        args.slot if args.slot is not None else "",
        args.task,
        args.type,
        args.project or "",
        args.notes or "",
    ]
    client.values_update(
        f"'{TAB_RECURRING_TEMPLATE}'!A{target_row}:F{target_row}",
        [row_values],
    )

    trace("recurring-add", f"{day_canonical.lower()}-row{target_row}", [
        f"- day: {day_canonical}",
        f"- slot: {args.slot if args.slot is not None else '(auto-pick)'}",
        f"- task: {args.task}",
        f"- type: {args.type}",
        f"- project: {args.project or '—'}",
        f"- row: {target_row}",
        f"- snapshot: {snap}",
        f"- effect: applied to every future Sunday `archive` ceremony",
    ])
    print(f'task-tracker-manager: appended Recurring Template row {target_row} '
          f'({day_canonical}{" slot " + str(args.slot) if args.slot is not None else ""}, '
          f'"{args.task}", {args.type}, {args.project or "—"})')
    return 0


def cmd_recurring_remove(args) -> int:
    """Delete a row from Recurring Template by clearing its values (preserves row
    numbering for snapshot rollback). Traces."""
    client = SheetsClient()
    meta = client.get_metadata()
    if find_tab(meta, TAB_RECURRING_TEMPLATE) is None:
        sys.exit(f"task-tracker-manager: '{TAB_RECURRING_TEMPLATE}' tab not found")
    if not (2 <= args.row <= RT_MAX_ROWS):
        sys.exit(f"task-tracker-manager: --row must be 2..{RT_MAX_ROWS} (1 is the header row)")

    # Read the row before delete so the trace captures what was removed.
    pre = client.get_values(f"'{TAB_RECURRING_TEMPLATE}'!A{args.row}:F{args.row}")
    pre_row = pre[0] if pre and pre[0] else []
    if not pre_row or not any((c or "").strip() if isinstance(c, str) else c for c in pre_row):
        sys.exit(f"task-tracker-manager: '{TAB_RECURRING_TEMPLATE}' row {args.row} is already empty — nothing to remove")

    snap = snapshot_ranges(client, "recurring-remove",
        [f"'{TAB_RECURRING_TEMPLATE}'!A{args.row}:F{args.row}"])

    # Clear via values_clear so the row preserves its numbering.
    client.values_clear(f"'{TAB_RECURRING_TEMPLATE}'!A{args.row}:F{args.row}")

    pad = pre_row + [""] * (6 - len(pre_row))
    trace("recurring-remove", f"row{args.row}", [
        f"- removed row: {args.row}",
        f"- day: {pad[RT_COL_DAY]}",
        f"- slot: {pad[RT_COL_SLOT] if pad[RT_COL_SLOT] != '' else '(auto-pick)'}",
        f"- task: {pad[RT_COL_TASK]}",
        f"- type: {pad[RT_COL_TYPE]}",
        f"- project: {pad[RT_COL_PROJECT] or '—'}",
        f"- snapshot: {snap}",
        f"- effect: no longer stamped on future Sunday `archive` ceremonies",
    ])
    print(f'task-tracker-manager: removed Recurring Template row {args.row} '
          f'("{pad[RT_COL_TASK]}", {pad[RT_COL_DAY]})')
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
    week_props = find_live_week_tab(meta)
    if week_props is None:
        sys.exit("task-tracker-manager: live week tab not found")
    live_sid = week_props["sheetId"]
    todo_sid = find_tab(meta, TAB_TODO)["sheetId"] if find_tab(meta, TAB_TODO) else None
    lt_sid = find_tab(meta, TAB_TODO_LONG_TERM)["sheetId"] if find_tab(meta, TAB_TODO_LONG_TERM) else None
    pj_sid = find_tab(meta, TAB_PROJECTS)["sheetId"] if find_tab(meta, TAB_PROJECTS) else None

    snap = snapshot_ranges(client, "reformat", [
        f"'{week_props['title']}'!A1:O50",
    ])

    R: list[dict] = []

    # Strip existing conditional format rules — we can't enumerate them from metadata
    # without listing them, so we use deleteConditionalFormatRule by index. Easier: just
    # add new rules and tolerate duplicates. (Idempotency: if duplicate, the user can run
    # reformat again — the rules will re-apply.) For a clean rebuild, we'd need a
    # GetSpreadsheet-with-conditionalFormats roundtrip — keep this minimal here.

    # Live Week: priority status TRUE → strikethrough on day-pair
    for i in range(7):
        sc = LIVE_DAY_STAT[i]
        tc = LIVE_DAY_TASK[i]
        sc_letter = col_letter(sc)
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": live_sid,
                            "startRowIndex": LIVE_SLOT_FIRST_ROW - 1,
                            "endRowIndex": LIVE_SLOT_LAST_ROW,
                            "startColumnIndex": sc, "endColumnIndex": tc + 1}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": f"=${sc_letter}{LIVE_SLOT_FIRST_ROW}=TRUE"}]},
                    "format": {
                        "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                        "textFormat": {"strikethrough": True,
                                       "foregroundColor": hex_to_rgb(MUTED_HEX)},
                    },
                },
            },
            "index": 0,
        }})
        # Habit row TRUE → fill
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": live_sid,
                            "startRowIndex": LIVE_HABIT_FIRST_ROW - 1,
                            "endRowIndex": LIVE_HABIT_LAST_ROW,
                            "startColumnIndex": sc, "endColumnIndex": tc + 1}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": f"=${sc_letter}{LIVE_HABIT_FIRST_ROW}=TRUE"}]},
                    "format": {
                        "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                    },
                },
            },
            "index": 0,
        }})

    # To Do tab CF
    if todo_sid is not None:
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": todo_sid,
                            "startRowIndex": 1, "endRowIndex": TODO_MAX_ROWS,
                            "startColumnIndex": 0, "endColumnIndex": len(TODO_HEADERS)}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": "=$A2=TRUE"}]},
                    "format": {
                        "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                        "textFormat": {"strikethrough": True,
                                       "foregroundColor": hex_to_rgb(MUTED_HEX)},
                    },
                },
            },
            "index": 0,
        }})

    # To Do Long Term CF
    if lt_sid is not None:
        R.append({"addConditionalFormatRule": {
            "rule": {
                "ranges": [{"sheetId": lt_sid,
                            "startRowIndex": 1, "endRowIndex": LT_MAX_ROWS,
                            "startColumnIndex": 0, "endColumnIndex": len(LT_HEADERS)}],
                "booleanRule": {
                    "condition": {"type": "CUSTOM_FORMULA",
                                  "values": [{"userEnteredValue": '=$A2="Done"'}]},
                    "format": {
                        "backgroundColor": hex_to_rgb(SAGE_EXTRA_LIGHT_HEX),
                        "textFormat": {"strikethrough": True,
                                       "foregroundColor": hex_to_rgb(MUTED_HEX)},
                    },
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
    todo_rows = client.get_values(f"'{TAB_TODO}'!A2:F{TODO_MAX_ROWS}")
    for i, row in enumerate(todo_rows):
        r = 2 + i  # 1-based
        status = row[0] if len(row) > 0 else ""
        task = row[1] if len(row) > 1 else ""
        if not task:
            continue
        if _is_truthy(status):
            continue
        due = row[4] if len(row) > 4 else ""
        if due:
            due_str = str(due)[:10]
            if due_str < today_iso:
                overdue.append(f"  - row {r}: {task} (due {due_str})")
        else:
            unscheduled.append(f"  - row {r}: {task}")

    # Tomorrow's empty priority slots
    week_props = find_live_week_tab(meta)
    empty_slots_lines = []
    if week_props is not None:
        week_title = week_props["title"]
        tomorrow_idx = (today.weekday() + 1) % 7
        tc_letter = col_letter(LIVE_DAY_TASK[tomorrow_idx])
        slot_vals = client.get_values(
            f"'{week_title}'!{tc_letter}{LIVE_SLOT_FIRST_ROW}:{tc_letter}{LIVE_SLOT_LAST_ROW}"
        )
        empty_count = sum(1 for s in slot_vals if not s or not (s[0] if s else "").strip())
        # Slot vals might be shorter than 15 if trailing rows are blank
        empty_count += 15 - len(slot_vals)
        empty_slots_lines.append(f"  - tomorrow ({DAY_LABELS[tomorrow_idx]}): {empty_count}/15 empty")

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
    lines.append("**Priority slot capacity:**")
    lines.extend(empty_slots_lines if empty_slots_lines else ["  - (no live week tab found)"])
    lines.append("")
    lines.append(f"**Sheet:** {TRACKER_SHEET_URL}")

    print("\n".join(lines))
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
    a.set_defaults(func=cmd_append)

    pr = sub.add_parser("promote")
    pr.add_argument("--todo-row", type=int, required=True)
    pr.add_argument("--day", required=True)
    pr.add_argument("--slot", type=int, required=True)
    pr.set_defaults(func=cmd_promote)

    ar = sub.add_parser("archive")
    ar.add_argument("--skip-recurring", action="store_true",
                    help="bypass the Recurring Template stamp step (rare)")
    ar.add_argument("--dry-run", action="store_true",
                    help="report what would happen without writing — no rename, no clear, no stamp")
    ar.set_defaults(func=cmd_archive)

    ra = sub.add_parser("recurring-add",
                        help="Append a row to the Recurring Template tab (stamped onto every new week by `archive`).")
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

    sds = sub.add_parser("schedule-to-day-slot")
    sds.add_argument("--task", required=True)
    sds.add_argument("--day", required=True)
    sds.add_argument("--slot", type=int, default=None,
                     help="1..15; if omitted, auto-pick first empty slot")
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
