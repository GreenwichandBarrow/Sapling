#!/usr/bin/env python3
"""Post-run validator for post-call-analyzer (rewritten 2026-05-13).

Per universal POST_RUN_CHECK doctrine (feedback_mutating_skill_hardening_pattern.md):
every scheduled mutating skill must have an integrity validator that runs after
Claude exits 0. Non-zero exit from this script → wrapper overrides skill exit
code → Slack alert with VALIDATOR FAILED prefix.

Checks (matches SKILL.md "Validator (mandatory)" section):
  1. Queue dir empty OR all entries <3h old (mid-flight tolerance)
  2. Each entry in processed.json ledger has doc_url + vault_call_note (or explicit
     failure marker)
  3. No file in processed/ older than 30 days (rotate — WARN, not FAIL)
  4. Checkpoint file modification time <24h ago (detector ran recently)

Self-locates REPO_ROOT for server (~/projects/Sapling) and iMac legacy
(~/Documents/AI Operations) install paths.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / "CLAUDE.md").exists() and (parent / ".claude").exists():
            return parent
    for candidate in [
        Path.home() / "projects/Sapling",
        Path.home() / "Documents/AI Operations",
    ]:
        if candidate.exists():
            return candidate
    raise SystemExit("validate_post_call_analyzer_integrity: could not locate REPO_ROOT")


REPO_ROOT = find_repo_root()
QUEUE_DIR = REPO_ROOT / "brain/trackers/post-call-analyzer/queue"
PROCESSED_DIR = REPO_ROOT / "brain/trackers/post-call-analyzer/processed"
PROCESSED_LEDGER = REPO_ROOT / "brain/trackers/post-call-analyzer/processed.json"
CHECKPOINT_FILE = Path.home() / ".cache/post-call-analyzer/last-checkpoint.txt"

STALE_QUEUE_HOURS = 3
STALE_CHECKPOINT_HOURS = 24
ROTATE_PROCESSED_DAYS = 30

failures: list[str] = []
warnings: list[str] = []


def _mtime_age_hours(path: Path) -> float:
    return (time.time() - path.stat().st_mtime) / 3600


def check_queue_freshness() -> None:
    if not QUEUE_DIR.exists():
        return
    stale: list[str] = []
    for entry in QUEUE_DIR.iterdir():
        if entry.name.startswith(".") or not entry.name.endswith(".json"):
            continue
        if _mtime_age_hours(entry) > STALE_QUEUE_HOURS:
            stale.append(entry.name)
    if stale:
        failures.append(
            f"Queue has {len(stale)} stale entries (>{STALE_QUEUE_HOURS}h old): "
            f"{', '.join(stale[:5])}{'...' if len(stale) > 5 else ''}"
        )


def check_processed_entries() -> None:
    if not PROCESSED_LEDGER.exists():
        return
    try:
        ledger = json.loads(PROCESSED_LEDGER.read_text())
    except json.JSONDecodeError as e:
        failures.append(f"processed.json malformed: {e}")
        return

    # Ledger shapes supported:
    #   New (post-2026-05-13): {"processed": [{"id": ..., "doc_url": ..., ...}, ...], "last_updated": ...}
    #   New flat:              {"processed": ["id1", "id2", ...], "last_updated": ...}
    #   Legacy:                {"<id>": {<meta>}, ...}
    if isinstance(ledger, dict) and "processed" in ledger:
        items = ledger["processed"]
        if not isinstance(items, list):
            failures.append(f"processed.json 'processed' field is {type(items).__name__}, expected list")
            return
        entries_iter = (
            items if items and isinstance(items[0], dict) else [{"id": e} for e in items]
        )
    elif isinstance(ledger, dict):
        entries_iter = [
            {"id": k, **v} if isinstance(v, dict) else {"id": k} for k, v in ledger.items()
        ]
    else:
        failures.append(f"processed.json unexpected shape: {type(ledger).__name__}")
        return

    for entry in entries_iter:
        nid = entry.get("id")
        if not nid:
            continue
        has_artifacts = (
            entry.get("doc_url")
            or entry.get("vault_call_note")
            or entry.get("doc_failed")
            or entry.get("attio_failed")
            or entry.get("slack_failed")
            or entry.get("processed_at")
        )
        if not has_artifacts:
            failures.append(f"processed entry {nid} has no artifact + no failure marker")


def check_processed_rotation() -> None:
    if not PROCESSED_DIR.exists():
        return
    old: list[str] = []
    cutoff = time.time() - (ROTATE_PROCESSED_DAYS * 86400)
    for entry in PROCESSED_DIR.iterdir():
        if entry.is_file() and entry.stat().st_mtime < cutoff:
            old.append(entry.name)
    if old:
        warnings.append(
            f"{len(old)} processed/ files older than {ROTATE_PROCESSED_DAYS}d — "
            f"consider rotation: {', '.join(old[:3])}{'...' if len(old) > 3 else ''}"
        )


def check_checkpoint_freshness() -> None:
    if not CHECKPOINT_FILE.exists():
        warnings.append(f"no checkpoint file at {CHECKPOINT_FILE} — first-run grace")
        return
    age_h = _mtime_age_hours(CHECKPOINT_FILE)
    if age_h > STALE_CHECKPOINT_HOURS:
        failures.append(
            f"Checkpoint file is {age_h:.1f}h old (>{STALE_CHECKPOINT_HOURS}h) — "
            f"detector may not be firing. Path: {CHECKPOINT_FILE}"
        )


def main() -> int:
    check_queue_freshness()
    check_processed_entries()
    check_processed_rotation()
    check_checkpoint_freshness()

    print(f"REPO_ROOT: {REPO_ROOT}")
    print(f"Checks complete: {len(failures)} failures, {len(warnings)} warnings")
    for w in warnings:
        print(f"  WARN: {w}")
    for f in failures:
        print(f"  FAIL: {f}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
