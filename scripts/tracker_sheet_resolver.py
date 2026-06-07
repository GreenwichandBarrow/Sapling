#!/usr/bin/env python3
"""tracker_sheet_resolver.py — discover the current week's TO DO sheet ID.

Hybrid pointer + Drive-search resolver. Pointer at
~/.config/sapling/current-tracker-sheet.json holds {sheet_id, title, week_of,
updated_at}. The legacy Claude pointer path remains a read fallback only.
Updated atomically by the build-week verb.

Resolution order:
  1. TRACKER_SHEET_ID env var (backward-compat override)
  2. In-process cache (per-Python-process)
  3. Pointer file (if fresh — week_of >= most-recent-Sunday-on-or-before-today)
  4. Drive search fallback (writes back to pointer atomically)

Usage:
  python3 tracker_sheet_resolver.py             # prints sheet ID
  python3 tracker_sheet_resolver.py --print-id  # same
  python3 tracker_sheet_resolver.py --print-json
  python3 tracker_sheet_resolver.py --refresh   # force Drive search
  python3 tracker_sheet_resolver.py --prior     # print prior week's sheet ID
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Optional

# ---- constants ----

_SCRIPT_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SCRIPT_DIR.parent
POINTER_PATH = Path.home() / ".config" / "sapling" / "current-tracker-sheet.json"
LEGACY_POINTER_PATH = Path.home() / ".claude" / "config" / "current-tracker-sheet.json"
TRACKER_FOLDER_NAME = "To Do Archive"  # Kay created 2026-05-26
LEGACY_PARENT_FOLDER_ID = "12IpnsQ5V_M1fiTm0NZM9wKhlerauILMd"  # STRATEGIC PLANNING (pre-migration)
SHEET_NAME_PATTERN = re.compile(r"^TO DO (\d{1,2})\.(\d{1,2})\.(\d{2,4})$")
ENV_OVERRIDE = "TRACKER_SHEET_ID"

# In-process cache to avoid hitting disk + Drive on every call within one process
_PROCESS_CACHE: dict = {"value": None}


# ---- pointer I/O ----

def _read_pointer() -> Optional[dict]:
    for path in (POINTER_PATH, LEGACY_POINTER_PATH):
        try:
            if not path.exists():
                continue
            with open(path) as f:
                pointer = json.load(f)
            pointer.setdefault("_pointer_path", str(path))
            return pointer
        except (json.JSONDecodeError, OSError):
            continue
    return None


def write_pointer(sheet_id: str, title: str, week_of: date) -> None:
    """Atomic write — tmp + rename."""
    POINTER_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "sheet_id": sheet_id,
        "title": title,
        "week_of": week_of.isoformat(),
        "updated_at": datetime.now(timezone.utc).isoformat(),
    }
    tmp = POINTER_PATH.with_suffix(".json.tmp")
    with open(tmp, "w") as f:
        json.dump(payload, f, indent=2)
    tmp.replace(POINTER_PATH)
    _PROCESS_CACHE["value"] = payload


# ---- staleness check ----

def _most_recent_sunday(today: Optional[date] = None) -> date:
    """The Sunday on or before today (Sun..Sat week boundary)."""
    if today is None:
        today = date.today()
    # weekday(): Mon=0..Sun=6. Days since most recent Sunday:
    days_since_sun = (today.weekday() + 1) % 7
    return today - timedelta(days=days_since_sun)


def _is_pointer_fresh(pointer: dict, today: Optional[date] = None) -> bool:
    """Pointer is fresh if week_of >= most-recent-Sunday-on-or-before-today."""
    try:
        ptr_week = date.fromisoformat(pointer["week_of"])
    except (KeyError, ValueError, TypeError):
        return False
    return ptr_week >= _most_recent_sunday(today)


# ---- Drive search fallback ----

def _gog_drive_search(query: str) -> list:
    """Run gog drive search via subprocess. Returns list of file dicts (id, name, createdTime)."""
    try:
        command = "source scripts/op-env.sh >/dev/null 2>&1 || true; exec \"$@\""
        result = subprocess.run(
            [
                "bash", "-lc", command, "gog-wrapper",
                "gog", "drive", "search", query, "--raw-query", "--json",
            ],
            cwd=_REPO_ROOT,
            capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            return []
        data = json.loads(result.stdout) if result.stdout.strip() else []
        if isinstance(data, dict):
            return data.get("files", []) or data.get("results", []) or []
        return data if isinstance(data, list) else []
    except (subprocess.TimeoutExpired, json.JSONDecodeError):
        return []


def _find_archive_folder_id() -> Optional[str]:
    """Find the 'To Do Archive' folder by name. Returns ID or None."""
    q = (f"name = '{TRACKER_FOLDER_NAME}' "
         f"and mimeType = 'application/vnd.google-apps.folder' "
         f"and trashed = false")
    files = _gog_drive_search(q)
    if not files:
        return None
    return files[0].get("id")


def _parse_sheet_date(title: str) -> Optional[date]:
    """Parse 'TO DO M.D.YY' → date(). Returns None if no match."""
    m = SHEET_NAME_PATTERN.match(title.strip())
    if not m:
        return None
    month, day, year = int(m.group(1)), int(m.group(2)), int(m.group(3))
    if year < 100:
        year += 2000
    try:
        return date(year, month, day)
    except ValueError:
        return None


def _search_to_do_files() -> list:
    """Search Drive for `TO DO M.D.YY` spreadsheets — archive folder first, then legacy parent."""
    candidates: list = []
    archive_id = _find_archive_folder_id()
    if archive_id:
        q = (f"'{archive_id}' in parents "
             f"and name contains 'TO DO' "
             f"and mimeType = 'application/vnd.google-apps.spreadsheet' "
             f"and trashed = false")
        candidates = _gog_drive_search(q)
    if not candidates:
        q = (f"'{LEGACY_PARENT_FOLDER_ID}' in parents "
             f"and name contains 'TO DO' "
             f"and mimeType = 'application/vnd.google-apps.spreadsheet' "
             f"and trashed = false")
        candidates = _gog_drive_search(q)
    return candidates


def _drive_search_for_current() -> Optional[dict]:
    """Most-recent `TO DO M.D.YY` file. Returns {sheet_id, title, week_of} or None."""
    candidates = _search_to_do_files()
    parsed = []
    for f in candidates:
        title = f.get("name", "")
        sid = f.get("id", "")
        created = f.get("createdTime", "")
        wk = _parse_sheet_date(title)
        if wk and sid:
            parsed.append((wk, sid, title, created))
    if not parsed:
        return None
    parsed.sort(key=lambda x: (x[0], x[3]), reverse=True)
    wk, sid, title, _ = parsed[0]
    return {"sheet_id": sid, "title": title, "week_of": wk.isoformat()}


# ---- public API ----

def resolve_current_sheet(force_refresh: bool = False) -> dict:
    """Return {sheet_id, title, week_of} for the current week's tracker sheet."""
    if not force_refresh:
        env_id = os.environ.get(ENV_OVERRIDE)
        if env_id:
            return {
                "sheet_id": env_id,
                "title": "(env override)",
                "week_of": _most_recent_sunday().isoformat(),
            }
        cached = _PROCESS_CACHE.get("value")
        if cached:
            return cached

    pointer = _read_pointer()
    if pointer and not force_refresh and _is_pointer_fresh(pointer):
        _PROCESS_CACHE["value"] = pointer
        return pointer

    found = _drive_search_for_current()
    if not found:
        if pointer:
            print(
                f"[tracker_sheet_resolver] WARN: Drive search returned nothing; "
                f"using stale pointer week_of={pointer.get('week_of')}",
                file=sys.stderr,
            )
            _PROCESS_CACHE["value"] = pointer
            return pointer
        raise RuntimeError(
            "No tracker sheet found. Pointer absent and Drive search returned 0 matches. "
            f"Looked in '{TRACKER_FOLDER_NAME}' folder + STRATEGIC PLANNING parent."
        )

    try:
        write_pointer(found["sheet_id"], found["title"], date.fromisoformat(found["week_of"]))
    except OSError as e:
        print(f"[tracker_sheet_resolver] WARN: pointer write failed ({e}); using in-memory result", file=sys.stderr)
    _PROCESS_CACHE["value"] = found
    return found


def resolve_current_sheet_id(force_refresh: bool = False) -> str:
    return resolve_current_sheet(force_refresh)["sheet_id"]


def find_prior_sheet_id(current_sheet_id: str) -> Optional[str]:
    """Second-most-recent `TO DO M.D.YY` sheet — for cross-file carryover at rollover."""
    candidates = _search_to_do_files()
    parsed = []
    for f in candidates:
        title = f.get("name", "")
        sid = f.get("id", "")
        created = f.get("createdTime", "")
        wk = _parse_sheet_date(title)
        if wk and sid and sid != current_sheet_id:
            parsed.append((wk, sid, title, created))
    if not parsed:
        return None
    parsed.sort(key=lambda x: (x[0], x[3]), reverse=True)
    return parsed[0][1]


# ---- CLI ----

def _cli() -> int:
    import argparse
    p = argparse.ArgumentParser(description="Resolve the current week's TO DO tracker sheet ID")
    p.add_argument("--print-id", action="store_true", help="Print just the sheet ID (default)")
    p.add_argument("--print-json", action="store_true", help="Print full {sheet_id, title, week_of} JSON")
    p.add_argument("--refresh", action="store_true", help="Force Drive search (bypass pointer cache)")
    p.add_argument("--prior", action="store_true", help="Print prior week's sheet ID (cross-file carryover)")
    args = p.parse_args()

    if args.prior:
        current = resolve_current_sheet_id(force_refresh=args.refresh)
        prior = find_prior_sheet_id(current)
        if prior:
            print(prior)
            return 0
        print("[tracker_sheet_resolver] No prior sheet found", file=sys.stderr)
        return 1

    info = resolve_current_sheet(force_refresh=args.refresh)
    if args.print_json:
        print(json.dumps(info, indent=2))
    else:
        print(info["sheet_id"])
    return 0


if __name__ == "__main__":
    sys.exit(_cli())
