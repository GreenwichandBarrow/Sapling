#!/usr/bin/env python3
"""Scan logs/scheduled/ for launchd job failures in the last 24 hours.

Wrapped by `scripts/run-skill.sh` indirectly via the launchd-debugger skill
(invoked daily 5am ET). Emits a JSON list of failed jobs to stdout — one
entry per failed run, ready for the headless prompt to fan out into per-job
debug subagents.

Detection logic
---------------

The shared wrapper (`scripts/run-skill.sh`) writes one log file per run at
`logs/scheduled/{skill}-{YYYY-MM-DD}-{HHMM}.log` and embeds these markers:

  * `Finished claude run: {date}, exit: {N} (attempts: {n})` — final wrapper
    exit code (skill exit OR validator-overridden exit).
  * `VALIDATOR FAILED — overriding skill exit code` — POST_RUN_CHECK
    validator rejected output even though Claude exited 0.
  * `PREFLIGHT FAILED (auth): ...` — Claude CLI 401 on preflight.

Some jobs (the bash-only refresh scripts under `apollo-credits-refresh.sh`,
`refresh-attio-snapshot.sh`, `refresh-jj-snapshot.sh`) do NOT use the shared
wrapper and emit no `Finished claude run` marker. We treat absence of an
explicit error pattern as success for those (they're tiny, idempotent, and
their own watchdog is the snapshot-staleness banner on the dashboard).

Failure conditions surfaced
---------------------------

A log entry becomes a failure record if ANY of:
  1. `exit:` line shows non-zero
  2. `VALIDATOR FAILED` marker present
  3. `PREFLIGHT FAILED` marker present
  4. `STOP marker` line written by a headless skill (e.g.
     `NIGHTLY-TRACKER-AUDIT STOP: ...`)

Per-skill dedup: only the most recent failed log per skill is returned
(older retries within the 24h window are noise — the agent should debug
the latest state, not historical attempts).

JSON output schema (per entry)
------------------------------

{
  "job": "nightly-tracker-audit",
  "last_log_path": "/abs/path/to/log",
  "last_log_mtime": "2026-05-01T03:30:14",
  "exit_code": 2,
  "validator_failed": true,
  "last_50_lines": "...",
  "error_signature": "VALIDATOR FAILED: WEEKLY REVIEW has 2 Tabled rows lingering"
}

Empty list `[]` = no failures in last 24h.

Exit codes
----------

  0  — script ran successfully (regardless of whether failures were found)
  2  — script itself errored (log dir missing, etc.)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LOG_DIR = REPO_ROOT / "logs" / "scheduled"
DEFAULT_WINDOW_HOURS = 24

# Filename pattern: {skill-name}-{YYYY-MM-DD}-{HHMM}.log
# Skill name may contain hyphens, so we anchor on the date suffix.
LOG_FILENAME_RE = re.compile(
    r"^(?P<skill>.+?)-(?P<date>\d{4}-\d{2}-\d{2})-(?P<time>\d{4})\.log$"
)

EXIT_LINE_RE = re.compile(r"Finished claude run:.*exit:\s*(?P<code>-?\d+)")
# Anchor on the wrapper's real override marker (em-dash, U+2014) — NOT the bare
# substring. The bare form false-matches skills' own SUCCESS-summary negation
# prose, e.g. nightly-tracker-audit's "No STOP marker, no `VALIDATOR FAILED`."
VALIDATOR_FAIL_RE = re.compile(r"VALIDATOR FAILED — overriding skill exit code")
PREFLIGHT_FAIL_RE = re.compile(r"PREFLIGHT FAILED")
STOP_MARKER_RE = re.compile(r"^[A-Z][A-Z0-9-]+\s+STOP:\s*(.+)$", re.MULTILINE)


def parse_log(path: Path) -> dict | None:
    """Return failure record dict if log indicates failure, else None."""
    try:
        text = path.read_text(errors="replace")
    except OSError:
        return None

    exit_match = EXIT_LINE_RE.search(text)
    exit_code: int | None = int(exit_match.group("code")) if exit_match else None

    validator_failed = bool(VALIDATOR_FAIL_RE.search(text))
    preflight_failed = bool(PREFLIGHT_FAIL_RE.search(text))
    stop_match = STOP_MARKER_RE.search(text)

    is_failure = (
        (exit_code is not None and exit_code != 0)
        or validator_failed
        or preflight_failed
        or stop_match is not None
    )
    if not is_failure:
        return None

    # Last 50 lines for diagnosis context.
    lines = text.splitlines()
    last_50 = "\n".join(lines[-50:])

    # Build a one-line error signature.
    if preflight_failed:
        signature = "PREFLIGHT AUTH FAIL — Claude CLI 401, re-auth required"
    elif validator_failed:
        # Find the validator line plus any preceding context.
        sig_lines = [ln for ln in lines[-30:] if "VALIDATOR" in ln or "FAIL" in ln]
        signature = sig_lines[-1].strip() if sig_lines else "VALIDATOR FAILED"
    elif stop_match:
        signature = stop_match.group(0).strip()
    elif exit_code is not None:
        # Grep last few non-empty lines for an error hint.
        non_empty = [ln for ln in lines[-15:] if ln.strip()]
        tail = " | ".join(non_empty[-3:]) if non_empty else ""
        signature = f"exit {exit_code}: {tail[:200]}"
    else:
        signature = "unknown failure mode"

    mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc).astimezone()

    return {
        "last_log_path": str(path),
        "last_log_mtime": mtime.isoformat(timespec="seconds"),
        "exit_code": exit_code if exit_code is not None else -1,
        "validator_failed": validator_failed,
        "preflight_failed": preflight_failed,
        "last_50_lines": last_50,
        "error_signature": signature,
    }


def scan(window_hours: int = DEFAULT_WINDOW_HOURS, log_file: Path | None = None) -> list[dict]:
    if not LOG_DIR.exists():
        print(f"ERROR: log dir missing: {LOG_DIR}", file=sys.stderr)
        sys.exit(2)

    # --log-file: parse a single specific log and return that result (or []).
    # Bypasses the per-skill dedup + time-window filter — useful for backfill,
    # validation, and the test harness verifying detection on a known failure.
    if log_file is not None:
        if not log_file.exists():
            print(f"ERROR: log file missing: {log_file}", file=sys.stderr)
            sys.exit(2)
        match = LOG_FILENAME_RE.match(log_file.name)
        if not match:
            print(f"ERROR: log file name does not match expected pattern: {log_file.name}", file=sys.stderr)
            sys.exit(2)
        record = parse_log(log_file)
        if record is None:
            return []
        record["job"] = match.group("skill")
        return [record]

    cutoff = datetime.now(tz=timezone.utc) - timedelta(hours=window_hours)
    cutoff_ts = cutoff.timestamp()

    # Bucket failures per skill, keep only the most-recent failure per skill.
    per_skill: dict[str, dict] = {}

    for log_path in LOG_DIR.glob("*.log"):
        try:
            stat = log_path.stat()
        except OSError:
            continue
        if stat.st_mtime < cutoff_ts:
            continue

        match = LOG_FILENAME_RE.match(log_path.name)
        if not match:
            # launchd-side stderr files (e.g. *-launchd.log) and anything
            # without the dated convention are skipped — they hold launchd
            # bootstrap output, not skill exit state.
            continue
        skill = match.group("skill")

        record = parse_log(log_path)
        if record is None:
            continue
        record["job"] = skill

        prior = per_skill.get(skill)
        if prior is None or record["last_log_mtime"] > prior["last_log_mtime"]:
            per_skill[skill] = record

    # Stable ordering: oldest failure first so the agent debugs in chronological order.
    return sorted(per_skill.values(), key=lambda r: r["last_log_mtime"])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scan logs/scheduled/ for launchd job failures.",
    )
    parser.add_argument(
        "--lookback-hours",
        type=int,
        default=None,
        help=f"Hours back from now to scan (default: {DEFAULT_WINDOW_HOURS}).",
    )
    parser.add_argument(
        "--lookback-days",
        type=int,
        default=None,
        help="Days back from now to scan. Overrides --lookback-hours if both set.",
    )
    parser.add_argument(
        "--log-file",
        type=Path,
        default=None,
        help="Parse a single specific log file. Bypasses dedup + time window. "
             "Useful for backfill, validation, and test harnesses.",
    )
    args = parser.parse_args()

    if args.lookback_days is not None:
        window_hours = args.lookback_days * 24
    elif args.lookback_hours is not None:
        window_hours = args.lookback_hours
    else:
        window_hours = DEFAULT_WINDOW_HOURS

    failures = scan(window_hours=window_hours, log_file=args.log_file)
    print(json.dumps(failures, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
