#!/usr/bin/env python3
"""
Wrapper-level integrity validator for cold-call operations Sunday prep run.

Runs as POST_RUN_CHECK after the scheduled wrapper completes. Independent of
skill-internal validation. Catches silent-success failures where the agent
exits 0 but Mon-Fri Call Log tabs are missing, empty, or have blank
`Owner Name` — the 4/19 failure mode.

For each cold-call niche (legacy env JJ_CALL_NICHES, default "Premium Pest Management"):
  1. Verify all 5 Mon-Fri Call Log tabs exist for the coming week
  2. Verify each tab has rows with `Owner Name` populated

Exit codes:
  0  Pass — all niches have 5 tabs with populated `Owner Name`
  2  Fail — any niche missing tabs OR tab has rows with blank `Owner Name`

Usage:
  python3 validate_jj_operations_integrity.py [--week-start YYYY-MM-DD]

If --week-start omitted, computes the upcoming Monday from today (or today if Mon).
"""

import json
import os
import subprocess
import sys
from datetime import date, datetime, timedelta


# Mirrors scripts/validate_phase2_integrity.py NICHE_SHEETS.
os.environ.setdefault("GOG_ACCOUNT", "kay.s@greenwichandbarrow.com")


NICHE_SHEETS = {
    "Art Insurance": "15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ",
    "Domestic TCI": "1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw",
    "IPLC": "1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ",
    "Art Storage": "1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g",
    "Art Advisory": "1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0",
    "Premium Pest Management": "1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I",
}


def upcoming_monday(today: date) -> date:
    """Return today if Monday, else next Monday."""
    days_until_monday = (0 - today.weekday()) % 7
    return today + timedelta(days=days_until_monday)


def tab_name(d: date) -> str:
    """Format: 'Call Log M.DD.YY' — month no leading zero, day with leading zero."""
    return f"Call Log {d.month}.{d.day:02d}.{d.strftime('%y')}"


def _run_with_retry(args: list[str], timeout: int = 90) -> subprocess.CompletedProcess:
    """Run a subprocess once, retry once on TimeoutExpired with same budget.

    gog's sheets metadata API occasionally exceeds 30s on cold cache (real
    failure mode observed Sunday 4/26 surfaced as "could not list tabs").
    90s budget + retry-once handles transient slowness without swallowing
    a genuinely stuck call — second timeout raises normally.
    """
    try:
        return subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        print(
            f"[validate_jj_operations] subprocess timed out after {timeout}s, retrying once: {' '.join(args)}",
            file=sys.stderr,
        )
        return subprocess.run(args, capture_output=True, text=True, timeout=timeout)


def list_sheet_tabs(sheet_id: str) -> list[str]:
    """Return list of tab titles via `gog sheets metadata`."""
    result = _run_with_retry(["gog", "sheets", "metadata", sheet_id], timeout=90)
    if result.returncode != 0:
        raise RuntimeError(f"gog sheets metadata failed: {result.stderr.strip()}")
    titles = []
    in_sheets = False
    for line in result.stdout.splitlines():
        if line.startswith("Sheets:"):
            in_sheets = True
            continue
        if not in_sheets:
            continue
        # Skip header line
        if line.strip().startswith("ID") and "TITLE" in line:
            continue
        if not line.strip():
            continue
        # Format: "{id}    {title}    {rows}    {cols}" — split by 2+ spaces
        parts = [p for p in line.split("  ") if p.strip()]
        if len(parts) >= 2:
            titles.append(parts[1].strip())
    return titles


def idx_to_letter(idx: int) -> str:
    """Convert a 0-based column index to an A1-style column letter."""
    result = ""
    while True:
        result = chr(65 + idx % 26) + result
        idx = idx // 26 - 1
        if idx < 0:
            return result


def get_values(sheet_id: str, rng: str) -> list[list[str]]:
    result = _run_with_retry(
        ["gog", "sheets", "get", sheet_id, rng, "--json"], timeout=90
    )
    if result.returncode != 0:
        return []
    try:
        data = json.loads(result.stdout)
    except json.JSONDecodeError:
        return []
    return data.get("values", []) or []


def header_map(sheet_id: str, tab: str) -> dict[str, int]:
    rows = get_values(sheet_id, f"'{tab}'!1:1")
    headers = rows[0] if rows else []
    return {str(value).strip(): idx for idx, value in enumerate(headers) if str(value).strip()}


def resolve_header(headers: dict[str, int], tab: str, candidates: list[str]) -> tuple[str, int]:
    for candidate in candidates:
        if candidate in headers:
            return candidate, headers[candidate]
    available = ", ".join(sorted(headers)) or "(none)"
    raise RuntimeError(
        f"required header not found in {tab!r}; tried {candidates}; available: {available}"
    )


def get_tab_rows_by_headers(
    sheet_id: str,
    tab: str,
    required: dict[str, list[str]],
    max_row: int = 200,
) -> tuple[dict[str, tuple[str, int]], list[list[str]]]:
    headers = header_map(sheet_id, tab)
    resolved = {key: resolve_header(headers, tab, names) for key, names in required.items()}
    rightmost = max(idx for _, idx in resolved.values())
    rng = f"'{tab}'!A2:{idx_to_letter(rightmost)}{max_row}"
    return resolved, get_values(sheet_id, rng)


def row_value(row: list[str], resolved: dict[str, tuple[str, int]], key: str) -> str:
    idx = resolved[key][1]
    return row[idx].strip() if len(row) > idx and row[idx] else ""


def validate_call_log_tabs(
    niche: str,
    tabs: list[str],
    expected_tabs: list[str],
    tab_rows,
) -> list[str]:
    failures: list[str] = []
    missing = [t for t in expected_tabs if t not in tabs]
    if missing:
        return [f"[{niche}] missing Call Log tabs: {missing}"]

    # Each existing tab must have at least one row with Owner Name populated.
    for tab in expected_tabs:
        try:
            resolved, rows = tab_rows(tab)
        except RuntimeError as exc:
            failures.append(f"[{niche}] tab '{tab}' header resolution failed: {exc}")
            continue

        owner_names = [row_value(row, resolved, "owner") for row in rows]
        non_blank = [v for v in owner_names if v.strip()]
        if not non_blank:
            failures.append(f"[{niche}] tab '{tab}' has zero rows with `Owner Name` — dial-blocking")
            continue

        # Identify if any row has Company populated but Owner Name blank.
        companies = [row_value(row, resolved, "company") for row in rows]
        blanks = []
        for i, company in enumerate(companies):
            if company.strip() and (i >= len(owner_names) or not owner_names[i].strip()):
                blanks.append(i + 2)  # row number (header at row 1)
        if blanks:
            failures.append(
                f"[{niche}] tab '{tab}' has {len(blanks)} rows with Company set but Owner Name blank "
                f"(rows {blanks[:5]}{'...' if len(blanks) > 5 else ''})"
            )
    return failures


def main() -> int:
    args = sys.argv[1:]
    if "--week-start" in args:
        idx = args.index("--week-start")
        monday = datetime.fromisoformat(args[idx + 1]).date()
    else:
        monday = upcoming_monday(date.today())

    expected_tabs = [tab_name(monday + timedelta(days=i)) for i in range(5)]
    raw_niches = os.environ.get("JJ_CALL_NICHES", "Premium Pest Management")
    niches = [n.strip() for n in raw_niches.split(",") if n.strip()]

    failures = []

    for niche in niches:
        sheet_id = NICHE_SHEETS.get(niche)
        if not sheet_id:
            failures.append(f"[{niche}] no sheet ID in NICHE_SHEETS map — add it")
            continue

        try:
            tabs = list_sheet_tabs(sheet_id)
        except Exception as e:
            failures.append(f"[{niche}] could not list tabs: {e}")
            continue

        failures.extend(
            validate_call_log_tabs(
                niche,
                tabs,
                expected_tabs,
                lambda tab: get_tab_rows_by_headers(
                    sheet_id,
                    tab,
                    {"company": ["Company"], "owner": ["Owner Name"]},
                ),
            )
        )

    if failures:
        print(f"COLD-CALL OPERATIONS VALIDATOR FAILED for week of {monday}:", file=sys.stderr)
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"COLD-CALL OPERATIONS VALIDATOR PASSED for week of {monday}")
    print(f"  Niches checked: {niches}")
    print(f"  Tabs verified: {expected_tabs}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
