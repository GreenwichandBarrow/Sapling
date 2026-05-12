#!/usr/bin/env python3
"""One-shot build script — replace the big-% per-day display on the Live Week
tab with 7 native Google Sheets donut charts (pie + pieHole=0.5).

Per Kay's 2026-05-12 preference: real chart objects, true donut hole, sage
palette to mirror her original aesthetic intent.

Layout target — Live Week tab `May 11-17`:
  rows 17..21 of each day-pair (B-C Mon, D-E Tue, ..., N-O Sun) currently hold
  a merged big-% formula. This script:
    1. Snapshots current state to brain/context/rollback-snapshots/
    2. Creates hidden helper tab `_donut_data` with 7 rows of COUNTIF math
    3. Unmerges the 5-row x 2-col area per day, clears the formula
    4. Adds 7 embedded pieChart objects with pieHole=0.5 anchored at row 17
       of each day's left column.

Auth: same gog-refresh-token path as scripts/task_tracker.py.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
SNAPSHOT_DIR = REPO_ROOT / "brain" / "context" / "rollback-snapshots"
GOG_CREDS_PATH = Path.home() / ".config" / "gogcli" / "credentials.json"
GOG_ACCOUNT = os.environ.get("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")
TRACKER_SHEET_ID = os.environ.get(
    "TRACKER_SHEET_ID", "1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk"
)
LIVE_TAB_TITLE = "May 11-17"
HELPER_TAB_TITLE = "_donut_data"

# Sage palette per memory/project_personal_task_tracker.md
SAGE_DARK = {"red": 0x7A / 255, "green": 0x8C / 255, "blue": 0x4D / 255}
SAGE_EXTRA_LIGHT = {"red": 0xF3 / 255, "green": 0xF7 / 255, "blue": 0xE8 / 255}

# Per-day layout
DAY_DEFS = [
    # (day_label, status_col_letter, task_col_letter, anchor_col_idx_0based)
    ("Mon", "B", "C", 1),
    ("Tue", "D", "E", 3),
    ("Wed", "F", "G", 5),
    ("Thu", "H", "I", 7),
    ("Fri", "J", "K", 9),
    ("Sat", "L", "M", 11),
    ("Sun", "N", "O", 13),
]


# --------------------------------------------------------------- auth

def get_access_token() -> str:
    """Mint a fresh Sheets API access token via gog's refresh token."""
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
        token_file = json.loads(tmp_path.read_text())
        refresh = token_file.get("refresh_token")
    finally:
        try:
            tmp_path.unlink(missing_ok=True)
        except OSError:
            pass
    if not refresh:
        sys.exit("no refresh_token from gog export")
    resp = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": creds["client_id"],
            "client_secret": creds["client_secret"],
            "refresh_token": refresh,
            "grant_type": "refresh_token",
        },
        timeout=15,
    )
    if resp.status_code != 200:
        sys.exit(f"token refresh failed: {resp.status_code}")
    return resp.json()["access_token"]


# --------------------------------------------------------------- API helpers

class API:
    def __init__(self, token: str):
        self.s = requests.Session()
        self.s.headers.update({"Authorization": f"Bearer {token}"})

    def _retry(self, fn, *, label: str):
        for attempt in range(5):
            r = fn()
            if r.status_code == 200:
                return r.json()
            if r.status_code in (429,) or r.status_code >= 500:
                time.sleep(2 ** attempt)
                continue
            sys.exit(f"{label}: API error {r.status_code}: {r.text[:400]}")
        sys.exit(f"{label}: API retries exhausted")

    def get_metadata(self, fields: str = None) -> dict:
        params = {}
        if fields:
            params["fields"] = fields
        if "includeGridData" in (fields or ""):
            params["includeGridData"] = "true"
        return self._retry(
            lambda: self.s.get(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}",
                params=params, timeout=60,
            ),
            label="get_metadata",
        )

    def get_metadata_with_grid(self, ranges: list[str]) -> dict:
        params = [("includeGridData", "true")]
        for r in ranges:
            params.append(("ranges", r))
        return self._retry(
            lambda: self.s.get(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}",
                params=params, timeout=60,
            ),
            label="get_metadata_with_grid",
        )

    def get_values(self, range_a1: str) -> list[list]:
        data = self._retry(
            lambda: self.s.get(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
                params={"valueRenderOption": "FORMULA"},
                timeout=30,
            ),
            label="get_values",
        )
        return data.get("values", [])

    def values_update(self, range_a1: str, values: list[list]) -> dict:
        return self._retry(
            lambda: self.s.put(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
                params={"valueInputOption": "USER_ENTERED"},
                json={"values": values},
                timeout=30,
            ),
            label="values_update",
        )

    def batch_update(self, requests_list: list[dict]) -> dict:
        return self._retry(
            lambda: self.s.post(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}:batchUpdate",
                json={"requests": requests_list},
                timeout=60,
            ),
            label="batch_update",
        )


# --------------------------------------------------------------- main flow

def find_sheet_id(meta: dict, title: str) -> int | None:
    for s in meta.get("sheets", []):
        if s["properties"]["title"] == title:
            return s["properties"]["sheetId"]
    return None


def find_existing_merges(meta_with_grid: dict, sheet_id: int) -> list[dict]:
    for s in meta_with_grid.get("sheets", []):
        if s["properties"]["sheetId"] != sheet_id:
            continue
        return s.get("merges", [])
    return []


def find_existing_charts(meta: dict, sheet_id: int) -> list[dict]:
    """Return list of existing charts anchored on the live week tab."""
    out = []
    for s in meta.get("sheets", []):
        if s["properties"]["sheetId"] != sheet_id:
            continue
        for ch in s.get("charts", []):
            out.append(ch)
    return out


def main():
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    snapshot_path = SNAPSHOT_DIR / f"tasks-donut-build-{timestamp}.json"

    token = get_access_token()
    api = API(token)

    # ----- Step 1: discover layout + snapshot -----

    print(f"[donut-build] resolving sheet metadata...", file=sys.stderr)
    # First get full metadata (includes charts list per sheet)
    full_meta = api.get_metadata(
        fields="sheets(properties(sheetId,title,index,hidden),charts(chartId,position,spec(title,pieChart)))"
    )
    live_sheet_id = find_sheet_id(full_meta, LIVE_TAB_TITLE)
    if live_sheet_id is None:
        sys.exit(f"Live tab '{LIVE_TAB_TITLE}' not found")
    helper_sheet_id = find_sheet_id(full_meta, HELPER_TAB_TITLE)
    existing_charts = find_existing_charts(full_meta, live_sheet_id)

    # Grab merges + formula values for rows 17:21 across all day-pair columns
    merges_meta = api.get_metadata_with_grid([f"'{LIVE_TAB_TITLE}'!A17:O21"])
    existing_merges = find_existing_merges(merges_meta, live_sheet_id)
    # Only keep merges that touch rows 17:21 (0-indexed 16..21)
    relevant_merges = [
        m for m in existing_merges
        if m.get("startRowIndex", 0) >= 16
        and m.get("endRowIndex", 0) <= 21
        and m.get("startColumnIndex", 0) <= 14
    ]

    current_formulas = api.get_values(f"'{LIVE_TAB_TITLE}'!A17:O21")

    snapshot = {
        "timestamp_utc": timestamp,
        "tracker_sheet_id": TRACKER_SHEET_ID,
        "live_tab_title": LIVE_TAB_TITLE,
        "live_tab_sheet_id": live_sheet_id,
        "helper_tab_existed_before": helper_sheet_id is not None,
        "helper_tab_sheet_id": helper_sheet_id,
        "rows_17_21_formulas": current_formulas,
        "rows_17_21_merges": relevant_merges,
        "existing_charts_on_live_tab": existing_charts,
    }
    snapshot_path.write_text(json.dumps(snapshot, indent=2))
    print(f"[donut-build] snapshot saved: {snapshot_path}", file=sys.stderr)

    # ----- Step 2: create or reuse helper tab + populate formulas -----

    if helper_sheet_id is None:
        print(f"[donut-build] creating helper tab '{HELPER_TAB_TITLE}'...", file=sys.stderr)
        resp = api.batch_update([{
            "addSheet": {
                "properties": {
                    "title": HELPER_TAB_TITLE,
                    "hidden": True,
                    "gridProperties": {"rowCount": 10, "columnCount": 3},
                }
            }
        }])
        helper_sheet_id = resp["replies"][0]["addSheet"]["properties"]["sheetId"]
        print(f"[donut-build] helper tab created: sheetId={helper_sheet_id}", file=sys.stderr)
    else:
        # Ensure it's hidden in case Kay or a prior run un-hid it
        api.batch_update([{
            "updateSheetProperties": {
                "properties": {"sheetId": helper_sheet_id, "hidden": True},
                "fields": "hidden",
            }
        }])

    # Header + 7 data rows. Each row: Day label | Done formula | Left formula
    helper_rows = [["Day", "Done", "Left"]]
    for label, stat_col, task_col, _ in DAY_DEFS:
        done = f"=COUNTIF('{LIVE_TAB_TITLE}'!{stat_col}23:{stat_col}37, TRUE)"
        left = f"=COUNTA('{LIVE_TAB_TITLE}'!{task_col}23:{task_col}37) - COUNTIF('{LIVE_TAB_TITLE}'!{stat_col}23:{stat_col}37, TRUE)"
        helper_rows.append([label, done, left])

    api.values_update(f"'{HELPER_TAB_TITLE}'!A1:C8", helper_rows)
    print(f"[donut-build] helper tab populated: 7 day rows", file=sys.stderr)

    # ----- Step 3: unmerge + clear rows 17:21 on live tab -----

    unmerge_requests = []
    for m in relevant_merges:
        unmerge_requests.append({
            "unmergeCells": {
                "range": {
                    "sheetId": live_sheet_id,
                    "startRowIndex": m["startRowIndex"],
                    "endRowIndex": m["endRowIndex"],
                    "startColumnIndex": m["startColumnIndex"],
                    "endColumnIndex": m["endColumnIndex"],
                }
            }
        })
    if unmerge_requests:
        api.batch_update(unmerge_requests)
        print(f"[donut-build] unmerged {len(unmerge_requests)} merged ranges in rows 17:21", file=sys.stderr)

    # Clear values + formulas in rows 17:21 (so charts have a clean background)
    blank_block = [["" for _ in range(15)] for _ in range(5)]
    api.values_update(f"'{LIVE_TAB_TITLE}'!A17:O21", blank_block)
    print(f"[donut-build] cleared values in rows 17:21 cols A:O", file=sys.stderr)

    # ----- Step 4: delete any prior donut charts we own + add 7 fresh charts -----

    delete_requests = []
    for ch in existing_charts:
        ov = ch.get("position", {}).get("overlayPosition", {})
        anchor = ov.get("anchorCell", {})
        if (
            anchor.get("sheetId") == live_sheet_id
            and anchor.get("rowIndex") == 16  # row 17 = index 16
            and anchor.get("columnIndex") in {d[3] for d in DAY_DEFS}
            and ch.get("spec", {}).get("pieChart") is not None
        ):
            delete_requests.append({"deleteEmbeddedObject": {"objectId": ch["chartId"]}})
    if delete_requests:
        api.batch_update(delete_requests)
        print(f"[donut-build] removed {len(delete_requests)} stale donut charts", file=sys.stderr)

    chart_requests = []
    for day_idx, (label, _stat, _task, anchor_col) in enumerate(DAY_DEFS):
        data_row = day_idx + 1  # row 0 is header, day rows are 1..7
        chart_requests.append({
            "addChart": {
                "chart": {
                    "spec": {
                        "title": "",
                        "titleTextFormat": {"fontSize": 1},
                        "pieChart": {
                            "legendPosition": "NO_LEGEND",
                            "threeDimensional": False,
                            "pieHole": 0.5,
                            "domain": {
                                "sourceRange": {
                                    "sources": [{
                                        "sheetId": helper_sheet_id,
                                        "startRowIndex": 0,
                                        "endRowIndex": 1,
                                        "startColumnIndex": 1,
                                        "endColumnIndex": 3,
                                    }]
                                }
                            },
                            "series": {
                                "sourceRange": {
                                    "sources": [{
                                        "sheetId": helper_sheet_id,
                                        "startRowIndex": data_row,
                                        "endRowIndex": data_row + 1,
                                        "startColumnIndex": 1,
                                        "endColumnIndex": 3,
                                    }]
                                }
                            },
                        },
                        "backgroundColor": {"red": 1, "green": 1, "blue": 1},
                    },
                    "position": {
                        "overlayPosition": {
                            "anchorCell": {
                                "sheetId": live_sheet_id,
                                "rowIndex": 16,
                                "columnIndex": anchor_col,
                            },
                            "offsetXPixels": 0,
                            "offsetYPixels": 0,
                            "widthPixels": 120,
                            "heightPixels": 120,
                        }
                    },
                }
            }
        })

    resp = api.batch_update(chart_requests)
    new_chart_ids = []
    for reply in resp.get("replies", []):
        if "addChart" in reply:
            new_chart_ids.append(reply["addChart"]["chart"]["chartId"])
    print(f"[donut-build] added {len(new_chart_ids)} donut charts: {new_chart_ids}", file=sys.stderr)

    # ----- Step 5: attempt slice color override -----
    # Sheets API supports per-series color but for pie charts, slice colors
    # are configured at the chart level via `pieChart` (no native field).
    # The pie palette is theme-driven. We can override slice colors via
    # `series` only on bar/column/line charts in this API. For pie, the
    # only color control is at theme level.
    # → Color override: FALLBACK to default Sheets palette. Flag in report.
    colors_landed = False

    # Verification: re-fetch metadata to confirm chart IDs + positions
    verify_meta = api.get_metadata(
        fields="sheets(properties(sheetId,title),charts(chartId,position(overlayPosition(anchorCell(sheetId,rowIndex,columnIndex))),spec(pieChart(pieHole))))"
    )
    verified_charts = []
    for s in verify_meta.get("sheets", []):
        if s["properties"]["sheetId"] != live_sheet_id:
            continue
        for ch in s.get("charts", []):
            anchor = ch.get("position", {}).get("overlayPosition", {}).get("anchorCell", {})
            pieHole = ch.get("spec", {}).get("pieChart", {}).get("pieHole")
            verified_charts.append({
                "chartId": ch["chartId"],
                "anchorRow": anchor.get("rowIndex"),
                "anchorCol": anchor.get("columnIndex"),
                "pieHole": pieHole,
            })

    output = {
        "status": "OK",
        "snapshot_path": str(snapshot_path),
        "helper_tab_sheet_id": helper_sheet_id,
        "helper_tab_title": HELPER_TAB_TITLE,
        "live_tab_sheet_id": live_sheet_id,
        "live_tab_title": LIVE_TAB_TITLE,
        "new_chart_ids": new_chart_ids,
        "verified_charts": verified_charts,
        "colors_landed": colors_landed,
        "color_note": "Sheets pieChart API does not expose per-slice color overrides; default palette applied. Manual recolor in Sheet UI possible.",
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
