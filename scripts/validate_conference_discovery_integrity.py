#!/usr/bin/env python3
"""
Wrapper-level integrity validator for conference-discovery scheduled runs.

Runs as POST_RUN_CHECK after launchd wrapper completes. Catches the silent-success
failure mode where Claude exits 0 but the Conference Pipeline tab has been wiped
or catastrophically thinned. Precipitating incident: 2026-05-03 Sunday-night run
exited 0 after the archival subagent cleared all ~70 rows on the Pipeline tab.

Pattern mirrors validate_phase2_integrity.py: a pre-run snapshot written by the
skill before any sheet writes is the source of truth for "what was here before."
The validator reads that snapshot, then reads the live sheet, and rejects if
post-run row count is shorter than (pre-run - allowed_archival_delta).

Allowed archival delta: legitimate auto-archival moves (Skip → Skipped tab,
Attended → Attended tab, past-date passive → Skipped tab) reduce Pipeline row
count. We tolerate up to MAX_ARCHIVAL_DELTA rows of net reduction. Any larger
drop is presumptive wipe/data-loss and fails the check.

Snapshot contract (skill writes BEFORE any Pipeline mutation):
  brain/context/rollback-snapshots/conference-pipeline-pre-run-YYYY-MM-DD.json
  {
    "tab": "Pipeline",
    "row_count": 71,        # data rows, excluding header
    "captured_at": "...",
    "rows": [...]            # full row payload for restore-from-snapshot if needed
  }

If the snapshot is missing entirely, the validator FAILS — the skill is required
to write it, missing snapshot means the skill skipped its safety step.

Exit codes:
  0  Pass — snapshot exists; live row count within allowed delta of snapshot
  2  Fail — snapshot missing, sheet read failed, or row count dropped too far

Usage:
  python3 validate_conference_discovery_integrity.py [--date YYYY-MM-DD]
"""

import json
import os
import subprocess
import sys
from datetime import date, datetime


SHEET_ID = "1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY"
TAB = "Pipeline"
DATA_RANGE = "A2:O500"  # Row 1 is header, data starts row 2
SNAPSHOT_DIR = "/Users/kaycschneider/Documents/AI Operations/brain/context/rollback-snapshots"

# Auto-archival per SKILL.md routes Skip → Skipped tab, Attended → Attended tab,
# past-date passive → Skipped tab. A typical run archives 0–8 rows. We allow up
# to 15 to give headroom for catch-up runs (e.g. multi-week skipped backlog),
# while still catching wipe-class incidents (May 3 wiped ~70 rows in one swoop).
MAX_ARCHIVAL_DELTA = 15


def snapshot_path(run_date: date) -> str:
    return os.path.join(
        SNAPSHOT_DIR,
        f"conference-pipeline-pre-run-{run_date.isoformat()}.json",
    )


def get_pipeline_data_rows(sheet_id: str, tab: str, rng: str) -> list[list[str]]:
    """Return data rows (excluding header) with at least one non-empty cell."""
    result = subprocess.run(
        ["gog", "sheets", "get", sheet_id, f"'{tab}'!{rng}", "--json"],
        capture_output=True,
        text=True,
        timeout=30,
    )
    if result.returncode != 0:
        raise RuntimeError(f"gog sheets get failed: {result.stderr.strip()}")
    data = json.loads(result.stdout)
    rows = data.get("values", [])
    # Strip rows that are entirely blank
    return [r for r in rows if any(c and c.strip() for c in r)]


def main() -> int:
    args = sys.argv[1:]
    if "--date" in args:
        idx = args.index("--date")
        run_date = datetime.fromisoformat(args[idx + 1]).date()
    else:
        run_date = date.today()

    failures: list[str] = []

    # Check 1: Pre-run snapshot exists
    snap_path = snapshot_path(run_date)
    snapshot_count: int | None = None
    if not os.path.exists(snap_path):
        failures.append(
            f"pre-run snapshot missing at {snap_path} — skill must write this "
            f"BEFORE any Pipeline mutation (see headless-prompt.md Step 0)"
        )
    else:
        try:
            with open(snap_path) as f:
                snap = json.load(f)
            snapshot_count = int(snap.get("row_count", -1))
            if snapshot_count < 0:
                failures.append(
                    f"snapshot at {snap_path} has invalid row_count: {snap.get('row_count')!r}"
                )
                snapshot_count = None
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            failures.append(f"could not parse snapshot at {snap_path}: {exc}")

    # Check 2: Live sheet readable
    live_count: int | None = None
    try:
        live_rows = get_pipeline_data_rows(SHEET_ID, TAB, DATA_RANGE)
        live_count = len(live_rows)
    except Exception as exc:
        failures.append(f"could not read live Pipeline tab: {exc}")

    # Check 3: Row-count delta within tolerance
    if snapshot_count is not None and live_count is not None:
        delta = snapshot_count - live_count  # positive = rows lost
        if delta > MAX_ARCHIVAL_DELTA:
            failures.append(
                f"Pipeline tab lost too many rows: snapshot had {snapshot_count} "
                f"data rows, live has {live_count} (delta {delta} > "
                f"MAX_ARCHIVAL_DELTA {MAX_ARCHIVAL_DELTA}). "
                f"Likely a wipe/clear-rewrite. Restore from snapshot via "
                f"File → Version history on the Google Sheet, or use "
                f"{snap_path} as the rollback source."
            )
        elif live_count == 0 and snapshot_count > 0:
            # Belt-and-suspenders — explicit zero-row catch even if delta math
            # somehow misses (e.g. snapshot_count == MAX_ARCHIVAL_DELTA exactly)
            failures.append(
                f"Pipeline tab has zero data rows but snapshot had "
                f"{snapshot_count}. Total wipe. Restore immediately."
            )

    if failures:
        print(
            f"CONFERENCE-DISCOVERY VALIDATOR FAILED for {run_date}:",
            file=sys.stderr,
        )
        for f in failures:
            print(f"  - {f}", file=sys.stderr)
        return 2

    print(f"CONFERENCE-DISCOVERY VALIDATOR PASSED for {run_date}")
    print(f"  snapshot: {snap_path}")
    print(f"  pre-run rows: {snapshot_count}")
    print(f"  live rows: {live_count}")
    print(f"  delta: {snapshot_count - live_count} (tolerance: {MAX_ARCHIVAL_DELTA})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
