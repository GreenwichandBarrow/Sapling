#!/usr/bin/env python3
"""Restore future/current Skip rows from Skipped back to Pipeline.

One-off repair for the 2026-06-08 conference-discovery archival rule bug.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests


SHEET_ID = "1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY"
ACCOUNT = "kay.s@greenwichandbarrow.com"
PIPELINE = "Pipeline"
SKIPPED = "Skipped"
TODAY = date(2026, 6, 8)

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
SNAPSHOT_DIR = REPO_ROOT / "brain" / "context" / "rollback-snapshots"
GOG_CREDS_PATH = Path.home() / ".config" / "gogcli" / "credentials.json"


def run_gog(args: list[str], *, timeout: int = 60) -> subprocess.CompletedProcess:
    command = "source scripts/op-env.sh >/dev/null 2>&1; exec \"$@\""
    return subprocess.run(
        ["bash", "-lc", command, "gog-wrapper", "gog", *args],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        timeout=timeout,
    )


def gog_json(args: list[str]) -> dict:
    proc = run_gog(args)
    if proc.returncode != 0:
        sys.exit(f"gog failed: {' '.join(args)}\n{proc.stderr[:1000]}")
    return json.loads(proc.stdout or "{}")


def access_token() -> str:
    if not GOG_CREDS_PATH.exists():
        sys.exit(f"gog credentials not found at {GOG_CREDS_PATH}")
    creds = json.loads(GOG_CREDS_PATH.read_text())
    with tempfile.NamedTemporaryFile("r", suffix=".json", delete=False) as tmp:
        tmp_path = Path(tmp.name)
    try:
        export = run_gog(["auth", "tokens", "export", ACCOUNT, "--out", str(tmp_path), "--overwrite"])
        if export.returncode != 0:
            sys.exit(f"gog token export failed: {export.stderr[:1000]}")
        token_file = json.loads(tmp_path.read_text())
        refresh_token = token_file.get("refresh_token")
    finally:
        tmp_path.unlink(missing_ok=True)
    if not refresh_token:
        sys.exit("no refresh_token from gog export")
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "refresh_token": refresh_token,
            "grant_type": "refresh_token",
        },
        timeout=20,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


def norm(value: str) -> str:
    return re.sub(r"\s+", " ", (value or "").strip()).lower()


def header_map(headers: list[str]) -> dict[str, int]:
    return {norm(header): i for i, header in enumerate(headers)}


def find_idx(headers: list[str], *names: str) -> int | None:
    hm = header_map(headers)
    for name in names:
        found = hm.get(norm(name))
        if found is not None:
            return found
    return None


def cell(row: list[str], i: int | None) -> str:
    if i is None or i >= len(row):
        return ""
    return str(row[i]).strip()


def values(tab: str) -> list[list[str]]:
    data = gog_json(["sheets", "get", SHEET_ID, f"{tab}!A1:Z500", "-a", ACCOUNT, "-j"])
    return data.get("values") or data.get("data", {}).get("values") or []


def metadata() -> dict:
    return gog_json(["sheets", "metadata", SHEET_ID, "-a", ACCOUNT, "-j"])


def parse_start_date(value: str) -> date | None:
    match = re.search(r"(\d{1,2})/(\d{1,2})(?:/(\d{2,4}))?", value or "")
    if not match:
        return None
    month = int(match.group(1))
    day = int(match.group(2))
    raw_year = match.group(3)
    year = TODAY.year if raw_year is None else int(raw_year)
    if year < 100:
        year += 2000
    try:
        return date(year, month, day)
    except ValueError:
        return None


def week_label(d: date) -> str:
    monday = d - timedelta(days=d.weekday())
    return f"{monday.month}/{monday.day}"


def is_header(row: list[str], pipeline_headers: list[str]) -> bool:
    week_i = find_idx(pipeline_headers, "Week Of")
    if week_i is None or not cell(row, week_i):
        return False
    return all(not cell(row, i) for i in range(len(pipeline_headers)) if i != week_i)


def sheet_id(meta: dict, title: str) -> int:
    for sheet in meta.get("sheets", []):
        props = sheet.get("properties", {})
        if props.get("title") == title:
            return int(props["sheetId"])
    sys.exit(f"sheet tab not found: {title}")


def snapshot(pipeline: list[list[str]], skipped: list[list[str]], candidates: list[dict]) -> Path:
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    path = SNAPSHOT_DIR / f"conference-future-skip-restore-{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    path.write_text(json.dumps({
        "captured_at": datetime.now().isoformat(),
        "today": TODAY.isoformat(),
        "pipeline": pipeline,
        "skipped": skipped,
        "candidates": candidates,
    }, indent=2))
    return path


def batch_update(token: str, requests_list: list[dict]) -> dict:
    if not requests_list:
        return {}
    session = requests.Session()
    session.headers.update({"Authorization": f"Bearer {token}"})
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}:batchUpdate"
    for attempt in range(5):
        resp = session.post(url, json={"requests": requests_list}, timeout=60)
        if resp.status_code == 200:
            return resp.json()
        if resp.status_code == 429 or resp.status_code >= 500:
            time.sleep(2 ** attempt)
            continue
        try:
            detail = json.dumps(resp.json(), indent=2)
        except Exception:
            detail = resp.text
        sys.exit(f"batchUpdate failed HTTP {resp.status_code}: {detail[:2000]}")
    sys.exit("batchUpdate failed after retries")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    pipeline = values(PIPELINE)
    skipped = values(SKIPPED)
    if not pipeline or not skipped:
        sys.exit("missing Pipeline or Skipped values")

    p_headers = pipeline[0]
    s_headers = skipped[0]
    p_by = header_map(p_headers)
    s_by = header_map(s_headers)

    s_date_i = find_idx(s_headers, "Date of Conference", "Date")
    s_decision_i = find_idx(s_headers, "Decision")
    s_event_i = find_idx(s_headers, "Event Name", "Conference", "Name")

    candidates = []
    for row_number, row in enumerate(skipped[1:], start=2):
        decision = cell(row, s_decision_i)
        start = parse_start_date(cell(row, s_date_i))
        if decision.lower() in {"skip", "skipped"} and start and start >= TODAY:
            candidates.append({
                "row_number": row_number,
                "start": start.isoformat(),
                "week": week_label(start),
                "event": cell(row, s_event_i),
                "row": row,
            })

    candidates.sort(key=lambda c: (c["week"], c["start"], c["event"]))
    print(f"restore_candidates={len(candidates)}")
    for c in candidates:
        print(f"RESTORE row={c['row_number']} week={c['week']} start={c['start']} event={c['event']}")
    if not candidates:
        return 0

    if len({c["week"] for c in candidates}) != 1:
        sys.exit("restore script expected one week section; inspect candidates manually")
    target_week = candidates[0]["week"]

    week_i = find_idx(p_headers, "Week Of")
    target_header_pos = None
    next_header_pos = len(pipeline)
    for pos, row in enumerate(pipeline[1:], start=2):
        if is_header(row, p_headers):
            if cell(row, week_i) == target_week:
                target_header_pos = pos
                continue
            if target_header_pos is not None and pos > target_header_pos:
                next_header_pos = pos
                break
    if target_header_pos is None:
        sys.exit(f"Pipeline week header not found: {target_week}")

    insert_row_number = next_header_pos
    ordered_rows = []
    for candidate in candidates:
        source = candidate["row"]
        row_obj: dict[str, str] = {}
        for header in p_headers:
            key = norm(header)
            if key == norm("Week Of"):
                row_obj[header] = ""
            elif key == norm("Date of Conference"):
                row_obj[header] = cell(source, find_idx(s_headers, "Date of Conference", "Date"))
            elif key in s_by:
                row_obj[header] = cell(source, s_by[key])
            else:
                row_obj[header] = ""
        ordered_rows.append([row_obj.get(header, "") for header in p_headers])

    snap = snapshot(pipeline, skipped, candidates)
    print(f"snapshot={snap}")
    print(f"insert_pipeline_row={insert_row_number}")
    if args.dry_run:
        return 0

    meta = metadata()
    pipeline_id = sheet_id(meta, PIPELINE)
    skipped_id = sheet_id(meta, SKIPPED)
    insert_index = insert_row_number - 1
    requests_list = [
        {
            "insertDimension": {
                "range": {
                    "sheetId": pipeline_id,
                    "dimension": "ROWS",
                    "startIndex": insert_index,
                    "endIndex": insert_index + len(ordered_rows),
                },
                "inheritFromBefore": True,
            }
        },
        {
            "updateCells": {
                "range": {
                    "sheetId": pipeline_id,
                    "startRowIndex": insert_index,
                    "endRowIndex": insert_index + len(ordered_rows),
                    "startColumnIndex": 0,
                    "endColumnIndex": len(p_headers),
                },
                "rows": [
                    {"values": [{"userEnteredValue": {"stringValue": value}} for value in row]}
                    for row in ordered_rows
                ],
                "fields": "userEnteredValue",
            }
        },
    ]
    for candidate in sorted(candidates, key=lambda c: c["row_number"], reverse=True):
        start = candidate["row_number"] - 1
        requests_list.append({
            "deleteDimension": {
                "range": {
                    "sheetId": skipped_id,
                    "dimension": "ROWS",
                    "startIndex": start,
                    "endIndex": start + 1,
                }
            }
        })

    token = access_token()
    batch_update(token, requests_list)
    print(f"restored={len(candidates)} deleted_from_skipped={len(candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
