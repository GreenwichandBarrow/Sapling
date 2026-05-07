#!/usr/bin/env python3
"""Phase 2 Sunday-night post-run integrity validator.

Driver that calls `.claude/hooks/enrichment_integrity_check.py` once per
active JJ-Call-Only niche. Wrapped by `scripts/run-skill.sh` as the
POST_RUN_CHECK for `com.greenwich-barrow.target-discovery-sunday.plist`.

Why this exists: a single Phase 2 run may process multiple JJ-Call-Only
niches. Each niche has its own target sheet and its own Mon-Fri Call Log
tabs. The integrity check must run per-niche so a silent failure on
one niche doesn't get masked by a pass on another.

Behavior:
  - Reads NICHE_SHEETS map (mirrors scripts/refresh_jj_snapshot.py).
  - For each niche listed in JJ_CALL_NICHES env var (comma-separated;
    defaults to "Premium Pest Management"), run the integrity check
    against today's pool artifact.
  - Pool artifact path: brain/context/jj-week-pool-{YYYY-MM-DD}.md
  - Returns exit 0 only if ALL invoked niches pass.

Exit codes:
  0 — all niches passed integrity check
  1 — at least one niche failed (drift or missing Col K)
  2 — error invoking subprocess or pool artifact missing entirely
"""

from __future__ import annotations

import os
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
HOOK_PATH = REPO_ROOT / ".claude" / "hooks" / "enrichment_integrity_check.py"
POOL_DIR = REPO_ROOT / "brain" / "context"

# Mirrors scripts/refresh_jj_snapshot.py NICHE_SHEETS. Update both when a
# new JJ-Call-Only niche activates a target sheet.
NICHE_SHEETS = {
    "Art Insurance": "15M76-gpcklwc47HDXIwyFC9Tj8K4wDOor4i0uxCYyHQ",
    "Domestic TCI": "1lEAx-3pEshsSc0Rix4KunJ38mzHahjAmV6nQA_cuwLw",
    "IPLC": "1Cdw6yb8-yBQtx5mTB8Hu4rENkJfpmt3t7HZdGqtdylQ",
    "Art Storage": "1PDprJ_gApm7T_kzpNWlWk7qItQ11M95ssL9_UD5sE9g",
    "Art Advisory": "1c6Db21D2qDpiT7LnEQ4l0AROlA-gucDQD1ZGOlrZ-K0",
    "Premium Pest Management": "1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I",
}


def _today_pool_path() -> Path:
    return POOL_DIR / f"jj-week-pool-{date.today().isoformat()}.md"


def _niches_to_check() -> list[str]:
    raw = os.environ.get("JJ_CALL_NICHES", "Premium Pest Management")
    return [n.strip() for n in raw.split(",") if n.strip()]


def _run_check(niche: str, sheet_id: str, pool_path: Path) -> tuple[int, str]:
    if not pool_path.exists():
        return (
            2,
            f"[{niche}] pool artifact missing at {pool_path}; "
            "Phase 2 Step 1 produced nothing",
        )
    try:
        result = subprocess.run(
            ["python3", str(HOOK_PATH), sheet_id, str(pool_path)],
            capture_output=True,
            text=True,
            timeout=300,
        )
    except subprocess.TimeoutExpired:
        return (2, f"[{niche}] integrity check timed out after 300s")
    except FileNotFoundError as exc:
        return (2, f"[{niche}] could not invoke hook: {exc}")

    output = (result.stdout + result.stderr).strip()
    if result.returncode == 0:
        return (0, f"[{niche}] PASS\n{output}")
    return (
        result.returncode,
        f"[{niche}] FAIL (exit {result.returncode})\n{output}",
    )


def main() -> int:
    niches = _niches_to_check()
    pool_path = _today_pool_path()

    if not niches:
        print("ERROR: no niches configured in JJ_CALL_NICHES", file=sys.stderr)
        return 2

    overall_exit = 0
    summaries: list[str] = []
    for niche in niches:
        sheet_id = NICHE_SHEETS.get(niche)
        if not sheet_id:
            summaries.append(f"[{niche}] ERROR: not in NICHE_SHEETS map")
            overall_exit = max(overall_exit, 2)
            continue
        code, summary = _run_check(niche, sheet_id, pool_path)
        summaries.append(summary)
        if code != 0:
            overall_exit = max(overall_exit, code)

    print("=== Phase 2 integrity validation ===")
    for summary in summaries:
        print(summary)
        print()

    if overall_exit == 0:
        print("OVERALL: PASS — all niches integrity-checked")
    else:
        print(f"OVERALL: FAIL (exit {overall_exit})", file=sys.stderr)
    return overall_exit


if __name__ == "__main__":
    sys.exit(main())
