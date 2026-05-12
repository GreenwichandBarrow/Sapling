#!/usr/bin/env python3
"""One-shot fix script for TO DO 5.12.26 sheet (Kay's personal task tracker).

Two fixes:
  Fix 1: Update _donut_data 'Left' formulas to use IF(COUNTA(...)=0, 1, ...)
         so empty-day donuts (Sat/Sun) render a placeholder ring instead
         of a blank chart.
  Fix 2: Update workbook spreadsheetTheme ACCENT1 + ACCENT2 to sage-dark
         and pure white so pie slices inherit the right palette by default.
         Per-slice manual overrides (e.g. Kay's Mon green) are preserved
         because they live on the chart, not the theme.

Snapshots pre-state to brain/context/rollback-snapshots/.

Auth: gog refresh-token path (same as build_donut_charts.py).
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

# Per-day layout: (day_label, status_col, task_col)
DAY_DEFS = [
    ("Mon", "B", "C"),
    ("Tue", "D", "E"),
    ("Wed", "F", "G"),
    ("Thu", "H", "I"),
    ("Fri", "J", "K"),
    ("Sat", "L", "M"),
    ("Sun", "N", "O"),
]

# Sage-dark #7a8c4d
ACCENT1_RGB = {"red": 0x7A / 255, "green": 0x8C / 255, "blue": 0x4D / 255}
# Pure white
ACCENT2_RGB = {"red": 1.0, "green": 1.0, "blue": 1.0}


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
            sys.exit(f"{label}: API error {r.status_code}: {r.text[:600]}")
        sys.exit(f"{label}: API retries exhausted")

    def get_metadata(self, fields: str | None = None) -> dict:
        params = {}
        if fields:
            params["fields"] = fields
        return self._retry(
            lambda: self.s.get(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}",
                params=params, timeout=60,
            ),
            label="get_metadata",
        )

    def get_values(self, range_a1: str, *, render: str = "FORMULA") -> list[list]:
        data = self._retry(
            lambda: self.s.get(
                f"https://sheets.googleapis.com/v4/spreadsheets/{TRACKER_SHEET_ID}/values/{range_a1}",
                params={"valueRenderOption": render},
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


def main():
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")
    snapshot_path = SNAPSHOT_DIR / f"donut-color-fix-{timestamp}.json"

    token = get_access_token()
    api = API(token)

    # ----- Snapshot: pull current _donut_data formulas + theme colors -----

    print("[fix] reading current _donut_data formulas...", file=sys.stderr)
    pre_formulas = api.get_values(f"'{HELPER_TAB_TITLE}'!A1:C8", render="FORMULA")

    print("[fix] reading current spreadsheetTheme.themeColors...", file=sys.stderr)
    meta = api.get_metadata(fields="properties(spreadsheetTheme)")
    pre_theme = meta.get("properties", {}).get("spreadsheetTheme", {})
    pre_theme_colors = pre_theme.get("themeColors", [])

    snapshot = {
        "timestamp_utc": timestamp,
        "tracker_sheet_id": TRACKER_SHEET_ID,
        "helper_tab_title": HELPER_TAB_TITLE,
        "pre_donut_data_formulas": pre_formulas,
        "pre_spreadsheet_theme": pre_theme,
    }
    snapshot_path.write_text(json.dumps(snapshot, indent=2))
    print(f"[fix] snapshot saved: {snapshot_path}", file=sys.stderr)

    # ----- Fix 1: Update Left formulas in _donut_data -----

    new_rows = [["Day", "Done", "Left"]]
    for label, stat_col, task_col in DAY_DEFS:
        done = f"=COUNTIF('{LIVE_TAB_TITLE}'!{stat_col}23:{stat_col}37, TRUE)"
        # Wrap COUNTA - COUNTIF in IF: when COUNTA=0 (empty day) return 1 as placeholder.
        left = (
            f"=IF(COUNTA('{LIVE_TAB_TITLE}'!{task_col}23:{task_col}37)=0, 1, "
            f"COUNTA('{LIVE_TAB_TITLE}'!{task_col}23:{task_col}37) - "
            f"COUNTIF('{LIVE_TAB_TITLE}'!{stat_col}23:{stat_col}37, TRUE))"
        )
        new_rows.append([label, done, left])

    api.values_update(f"'{HELPER_TAB_TITLE}'!A1:C8", new_rows)
    print("[fix] updated _donut_data Left formulas (placeholder for empty days)", file=sys.stderr)

    # Re-read computed values for verification
    post_values = api.get_values(f"'{HELPER_TAB_TITLE}'!A1:C8", render="UNFORMATTED_VALUE")
    post_formulas = api.get_values(f"'{HELPER_TAB_TITLE}'!A1:C8", render="FORMULA")

    # ----- Fix 2: Update spreadsheetTheme ACCENT1 + ACCENT2 -----

    # Build a new theme colors array. ACCENT1 -> sage-dark, ACCENT2 -> white.
    # All other entries pass through unchanged.
    new_theme_colors = []
    have_accent1 = False
    have_accent2 = False
    for entry in pre_theme_colors:
        ctype = entry.get("colorType")
        if ctype == "ACCENT1":
            new_theme_colors.append({"colorType": "ACCENT1", "color": {"rgbColor": ACCENT1_RGB}})
            have_accent1 = True
        elif ctype == "ACCENT2":
            new_theme_colors.append({"colorType": "ACCENT2", "color": {"rgbColor": ACCENT2_RGB}})
            have_accent2 = True
        else:
            # Preserve other accent colors / text / background as-is.
            new_theme_colors.append(entry)
    if not have_accent1:
        new_theme_colors.append({"colorType": "ACCENT1", "color": {"rgbColor": ACCENT1_RGB}})
    if not have_accent2:
        new_theme_colors.append({"colorType": "ACCENT2", "color": {"rgbColor": ACCENT2_RGB}})

    # Sheets API requires primaryFontFamily to be set when updating themeColors
    # (discovered via 400 INVALID_ARGUMENT). Preserve existing font family.
    primary_font = pre_theme.get("primaryFontFamily") or "Arial"

    theme_payload = {
        "updateSpreadsheetProperties": {
            "properties": {
                "spreadsheetTheme": {
                    "primaryFontFamily": primary_font,
                    "themeColors": new_theme_colors,
                }
            },
            "fields": "spreadsheetTheme(primaryFontFamily,themeColors)",
        }
    }

    api.batch_update([theme_payload])
    print("[fix] updated spreadsheetTheme (ACCENT1=sage-dark, ACCENT2=white)", file=sys.stderr)

    # Re-read theme to confirm
    post_meta = api.get_metadata(fields="properties(spreadsheetTheme)")
    post_theme_colors = (
        post_meta.get("properties", {}).get("spreadsheetTheme", {}).get("themeColors", [])
    )
    accent1_after = next(
        (e for e in post_theme_colors if e.get("colorType") == "ACCENT1"), None
    )
    accent2_after = next(
        (e for e in post_theme_colors if e.get("colorType") == "ACCENT2"), None
    )

    output = {
        "status": "OK",
        "snapshot_path": str(snapshot_path),
        "fix1": {
            "post_formulas_rows": post_formulas,
            "post_values_rows": post_values,
        },
        "fix2": {
            "ACCENT1": accent1_after,
            "ACCENT2": accent2_after,
        },
    }
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
