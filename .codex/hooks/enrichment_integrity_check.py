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
  python3 enrichment_integrity_check.py [--pool-only] <sheet_id> <pool_artifact_path>

  --pool-only: validate only that every pool row has Col K (Owner Name)
  populated in the Full Target List. Skips the Call Log tab walk. Use for
  target-discovery's 3pm fire, BEFORE jj-operations creates the tabs at
  6pm. Full mode (default) additionally walks the Mon-Fri tabs and is for
  invokers that run after the tabs exist.

Exit codes:
  0 — PASS (all invariants hold)
  1 — FAIL (one or more invariants broken; details printed to stderr)
  2 — ERROR (could not fetch data; sheet read failed, etc.)

Invokers:
  - target-discovery Phase 2 Step 5 end / 3pm POST_RUN_CHECK (Sunday) — --pool-only
  - jj-operations prep mode, as the final check before declaring done — full
  - Morning briefing (warn-only) on Monday when log indicates failure — full
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
    """Return the 5 Call Log tab names for the relevant Mon–Fri week.

    Anchoring rule:
      - Mon–Fri: this week's Mon-Fri (the week the anchor falls in).
      - Saturday: the just-completed Mon-Fri (anchor.weekday() == 5).
      - Sunday: the UPCOMING Mon-Fri (anchor.weekday() == 6). Phase 2's
        Sunday-night prep run targets the week that starts tomorrow,
        not the prior week. Prior to the 2026-05-04 fix this branch
        was projecting backward, producing 27 date-anchor drift
        failures in the 2026-05-03 launchd run.
    """
    anchor = anchor or date.today()
    if anchor.weekday() == 6:  # Sunday — project forward to tomorrow's Monday
        monday = anchor + timedelta(days=1)
    else:  # Mon-Sat — anchor on this week's Monday
        monday = anchor - timedelta(days=anchor.weekday())
    tabs: list[str] = []
    for i in range(5):
        d = monday + timedelta(days=i)
        tabs.append(f"Call Log {d.month}.{d.day:02d}.{str(d.year)[-2:]}")
    return tabs


def _self_test() -> None:
    """Exercise _mon_fri_tab_names across all weekdays. Asserts on regression.

    Covers the 2026-05-03 Sunday drift bug: Sunday 5/3 must project to
    the UPCOMING Mon-Fri (5/4-5/8), not the PRIOR week (4/27-5/1).
    """
    # Sunday 2026-05-03 → upcoming Mon-Fri 5/4 to 5/8 (the bug case)
    sun = date(2026, 5, 3)
    expected_sun = [
        "Call Log 5.04.26",
        "Call Log 5.05.26",
        "Call Log 5.06.26",
        "Call Log 5.07.26",
        "Call Log 5.08.26",
    ]
    assert _mon_fri_tab_names(sun) == expected_sun, (
        f"Sunday anchor regression: got {_mon_fri_tab_names(sun)}"
    )

    # Monday 2026-05-04 → this week's Mon-Fri 5/4 to 5/8
    mon = date(2026, 5, 4)
    assert _mon_fri_tab_names(mon) == expected_sun, (
        f"Monday anchor regression: got {_mon_fri_tab_names(mon)}"
    )

    # Wednesday 2026-05-06 → still this week's Mon-Fri 5/4 to 5/8
    wed = date(2026, 5, 6)
    assert _mon_fri_tab_names(wed) == expected_sun, (
        f"Wednesday anchor regression: got {_mon_fri_tab_names(wed)}"
    )

    # Saturday 2026-05-09 → the just-completed Mon-Fri 5/4 to 5/8
    sat = date(2026, 5, 9)
    assert _mon_fri_tab_names(sat) == expected_sun, (
        f"Saturday anchor regression: got {_mon_fri_tab_names(sat)}"
    )

    # Year-rollover: Sunday 2026-12-27 → Mon 12/28 to Fri 1/1/2027
    sun_dec = date(2026, 12, 27)
    expected_dec = [
        "Call Log 12.28.26",
        "Call Log 12.29.26",
        "Call Log 12.30.26",
        "Call Log 12.31.26",
        "Call Log 1.01.27",
    ]
    assert _mon_fri_tab_names(sun_dec) == expected_dec, (
        f"Year-rollover regression: got {_mon_fri_tab_names(sun_dec)}"
    )

    print("PASS: _mon_fri_tab_names self-test (5 cases)")


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


def _run_pool_only_check(sheet_id: str, pool_path: Path) -> tuple[bool, list[str]]:
    """Validate pool enrichment WITHOUT walking the Call Log tabs.

    Scope: this is what target-discovery Phase 2 actually produces at its
    Sunday 3pm fire — owner names written to the Full Target List Col K for
    every row in the Step 1 pool. It does NOT create the Mon–Fri Call Log
    tabs; jj-operations does that at 6pm, and its own validator
    (validate_jj_operations_integrity.py) checks tab existence + tab Col K.

    Running the full tab-walk check at 3pm produced ~192 false failures
    every Sunday because the tabs don't exist yet (2026-05-31 incident).
    Pool-only mode is the correct contract for the 3pm validator.

    Invariant: every pool row maps to a Full Target List row whose Col K
    (Owner Name) is populated.
    """
    failures: list[str] = []

    pool_rows = _load_pool_artifact(pool_path)
    if not pool_rows:
        failures.append(
            f"pool artifact at {pool_path} contains zero row numbers; "
            "Step 1 produced no selection"
        )
        return (False, failures)

    # Read company (B) + owner (K) from Full Target List in one fetch.
    full_list = _fetch_range(sheet_id, "Full Target List!B2:K2000")
    # idx 0 == sheet row 2
    for r in sorted(pool_rows):
        data_idx = r - 2
        if data_idx < 0 or data_idx >= len(full_list):
            failures.append(
                f"pool row {r} is outside Full Target List data range "
                "(B2:K2000) — stale or bad row number in pool artifact"
            )
            continue
        row = full_list[data_idx]
        company = row[0].strip() if len(row) > 0 else ""
        owner = row[9].strip() if len(row) > 9 else ""
        label = company or f"row {r}"
        if not company:
            failures.append(
                f"pool row {r}: blank company in Full Target List Col B — "
                "row number does not point at a real target"
            )
        if not owner:
            failures.append(
                f"pool row {r} ({label}): blank Col K (Owner Name) in Full "
                "Target List — enrichment never landed"
            )

    return (len(failures) == 0, failures)


def main() -> int:
    # Self-test mode: exercises _mon_fri_tab_names anchoring without needing
    # sheet/pool args. Used to verify the 2026-05-03 Sunday drift fix.
    if len(sys.argv) == 2 and sys.argv[1] == "--self-test":
        _self_test()
        return 0

    # --pool-only: validate pool enrichment without walking Call Log tabs.
    # Used by target-discovery's 3pm POST_RUN_CHECK, before jj-operations
    # creates the tabs at 6pm. Flag may appear in any position.
    args = sys.argv[1:]
    pool_only = "--pool-only" in args
    positional = [a for a in args if a != "--pool-only"]

    if len(positional) != 2:
        print(
            "usage: enrichment_integrity_check.py [--pool-only] "
            "<sheet_id> <pool_artifact_path>",
            file=sys.stderr,
        )
        return 2

    sheet_id = positional[0]
    pool_path = Path(positional[1]).expanduser()

    try:
        if pool_only:
            passed, failures = _run_pool_only_check(sheet_id, pool_path)
        else:
            passed, failures = _run_check(sheet_id, pool_path)
    except (FileNotFoundError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if passed:
        if pool_only:
            print(
                "PASS: pool enrichment OK — every pool row has Col K (Owner "
                "Name) populated in Full Target List"
            )
        else:
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
