#!/usr/bin/env python3
"""Enrichment integrity stop hook.

Validates the target-discovery Phase 2 contract before jj-operations
declares its Sunday-night prep "done":

  1. The pool selected in Step 1 (and updated through backfills) is the
     exact set of rows that appear on the Mon–Fri Call Log tabs.
  2. Every row on every Mon–Fri Call Log tab has Col K (Owner Name)
     populated.

Rationale: on 2026-04-20 JJ opened his Monday tab to find 36 of 40 rows
with blank owner names because Phase 2 enrichment targeted rows that
were NOT the same rows jj-operations prep wrote to the tabs. This hook
blocks that failure mode.

Usage:
  python3 enrichment_integrity_check.py <sheet_id> <pool_artifact_path>

Exit codes:
  0 — PASS (all invariants hold)
  1 — FAIL (one or more invariants broken; details printed to stderr)
  2 — ERROR (could not fetch data; sheet read failed, etc.)

Invokers:
  - target-discovery Phase 2 Step 5 end (Sunday night)
  - jj-operations prep mode, as the final check before declaring done
  - Morning briefing (warn-only) on Monday when log indicates failure
"""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import date, timedelta
from pathlib import Path


def _fetch_range(sheet_id: str, range_: str) -> list[list[str]]:
    """Call gog sheets get and return the raw values matrix."""
    result = subprocess.run(
        ["gog", "sheets", "get", sheet_id, range_, "--json"],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gog sheets get failed ({range_}): {result.stderr}")
    payload = json.loads(result.stdout)
    return payload.get("values", []) or []


def _mon_fri_tab_names(anchor: date | None = None) -> list[str]:
    """Return the 5 Call Log tab names for the Mon–Fri of `anchor`'s week."""
    anchor = anchor or date.today()
    monday = anchor - timedelta(days=anchor.weekday())
    tabs: list[str] = []
    for i in range(5):
        d = monday + timedelta(days=i)
        tabs.append(f"Call Log {d.month}.{d.day:02d}.{str(d.year)[-2:]}")
    return tabs


def _load_pool_artifact(path: Path) -> set[int]:
    """Parse row numbers from the Sunday-night pool artifact.

    The artifact is a markdown file; row numbers are expected on lines
    matching `- row: 123` or `row_number: 123`. We accept either form to
    keep the producer flexible.
    """
    if not path.exists():
        raise FileNotFoundError(f"pool artifact missing: {path}")
    rows: set[int] = set()
    for line in path.read_text().splitlines():
        stripped = line.strip()
        # Match "- row: 123", "row: 123", "row_number: 123", "- 123"
        for prefix in ("- row:", "row:", "row_number:", "-"):
            if stripped.startswith(prefix):
                tail = stripped.removeprefix(prefix).strip()
                if tail.isdigit():
                    rows.add(int(tail))
                    break
    return rows


def _run_check(sheet_id: str, pool_path: Path) -> tuple[bool, list[str]]:
    """Run the two invariants. Returns (passed, failure_messages)."""
    failures: list[str] = []

    # Invariant 1: pool artifact rows align with Call Log tab contents
    pool_rows = _load_pool_artifact(pool_path)
    if not pool_rows:
        failures.append(
            f"pool artifact at {pool_path} contains zero row numbers; "
            "Step 1 produced no selection"
        )

    # Read company-name column (B) from Full Target List for row->company map
    full_list_b = _fetch_range(sheet_id, "Full Target List!B2:B2000")
    row_to_company: dict[int, str] = {}
    for idx, row in enumerate(full_list_b, start=2):  # row 2 = first data row
        if row and row[0].strip():
            row_to_company[idx] = row[0].strip()
    pool_companies = {row_to_company[r] for r in pool_rows if r in row_to_company}

    # Walk each Mon–Fri Call Log tab
    tab_names = _mon_fri_tab_names()
    seen_companies: set[str] = set()
    for tab in tab_names:
        try:
            tab_rows = _fetch_range(sheet_id, f"{tab}!B2:K50")
        except RuntimeError as exc:
            failures.append(f"could not read {tab!r}: {exc}")
            continue

        for row_idx, row in enumerate(tab_rows, start=2):
            company = row[0].strip() if row and len(row) > 0 else ""
            if not company:
                continue  # blank row, skip

            # Invariant 2: Col K (Owner Name) populated
            owner = row[9].strip() if len(row) > 9 else ""
            if not owner:
                failures.append(
                    f"{tab} row {row_idx}: company {company!r} has blank "
                    "Col K (Owner Name) — enrichment never landed"
                )

            # Invariant 1: company on the tab should be in pool
            if pool_companies and company not in pool_companies:
                failures.append(
                    f"{tab} row {row_idx}: company {company!r} is on the tab "
                    "but was not in the Step 1 pool artifact — drift detected"
                )
            seen_companies.add(company)

    # Reverse check: every pool company should appear on some tab
    missing_from_tabs = pool_companies - seen_companies
    for company in sorted(missing_from_tabs):
        failures.append(
            f"pool company {company!r} was selected in Step 1 but does not "
            "appear on any Mon–Fri Call Log tab"
        )

    return (len(failures) == 0, failures)


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "usage: enrichment_integrity_check.py <sheet_id> <pool_artifact_path>",
            file=sys.stderr,
        )
        return 2

    sheet_id = sys.argv[1]
    pool_path = Path(sys.argv[2]).expanduser()

    try:
        passed, failures = _run_check(sheet_id, pool_path)
    except (FileNotFoundError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if passed:
        print("PASS: enrichment integrity OK — pool ↔ tabs aligned, all Col K populated")
        return 0

    print("FAIL: enrichment integrity check detected drift", file=sys.stderr)
    for msg in failures:
        print(f"  - {msg}", file=sys.stderr)
    print(
        f"\n{len(failures)} issue(s). Escalate to Monday briefing as "
        "'ENRICHMENT INTEGRITY FAILURE' per target-discovery SKILL.md.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
