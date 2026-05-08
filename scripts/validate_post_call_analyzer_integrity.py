#!/usr/bin/env python3
"""
validate_post_call_analyzer_integrity.py — POST_RUN_CHECK for post-call-analyzer.

Runs after the Claude headless prompt exits 0. Verifies the run actually drained
the queue and produced corresponding artifacts. Non-zero exit → wrapper
overrides skill exit code and fires Slack alert per
`feedback_mutating_skill_hardening_pattern.md`.

Self-locating REPO_ROOT — works on both iMac (~/Documents/AI Operations) and
Linux server (~/projects/Sapling). Phase 4 update 2026-05-08.

Checks:
1. Queue dir empty OR all entries <30 min old (still mid-flight from a fresh poll)
2. Each newly-processed doc_id has either a vault call note or an explicit
   failure marker in its processed/{id}.json
3. Thought-analysis artifacts (research-prompts + socrates-questions) named
   in archive entries actually exist on disk in brain/inbox/
4. processed/{id}.json files older than 30 days are flagged for rotation (warn, not fail)
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRACKER_DIR = REPO_ROOT / "brain" / "trackers" / "post-call-analyzer"
QUEUE_DIR = TRACKER_DIR / "queue"
PROCESSED_DIR = TRACKER_DIR / "processed"
TASK_QUEUE_DIR = TRACKER_DIR / "task_queue"
LEDGER = TRACKER_DIR / "processed.json"
INBOX_DIR = REPO_ROOT / "brain" / "inbox"

STALE_QUEUE_MIN = 30
ROTATION_DAYS = 30


def fail(msg: str) -> int:
    print(f"FAIL: {msg}", file=sys.stderr)
    return 2


def warn(msg: str) -> None:
    print(f"WARN: {msg}")


def main() -> int:
    if not TRACKER_DIR.exists():
        return fail(f"tracker dir missing: {TRACKER_DIR}")

    queue_files = [p for p in QUEUE_DIR.glob("*.json") if p.name != ".gitkeep"]
    now = datetime.now(timezone.utc)

    stale_queue = []
    for q in queue_files:
        mtime = datetime.fromtimestamp(q.stat().st_mtime, timezone.utc)
        if now - mtime > timedelta(minutes=STALE_QUEUE_MIN):
            stale_queue.append(q.name)

    if stale_queue:
        return fail(
            f"queue has {len(stale_queue)} stale entries (>{STALE_QUEUE_MIN} min old): "
            f"{', '.join(stale_queue[:5])}"
        )

    if LEDGER.exists():
        try:
            ledger = json.loads(LEDGER.read_text() or "{}")
        except json.JSONDecodeError as exc:
            return fail(f"processed.json invalid JSON: {exc}")
    else:
        ledger = {}

    today = datetime.now().strftime("%Y-%m-%d")
    today_processed = [
        (doc_id, meta)
        for doc_id, meta in ledger.items()
        if isinstance(meta, dict) and meta.get("processed_at", "").startswith(today)
    ]

    missing_artifacts: list[str] = []
    missing_thought_artifacts: list[str] = []

    for doc_id, meta in today_processed:
        archive = PROCESSED_DIR / f"{doc_id}.json"
        if not archive.exists():
            missing_artifacts.append(doc_id)
            continue
        try:
            data = json.loads(archive.read_text())
        except json.JSONDecodeError:
            missing_artifacts.append(f"{doc_id} (invalid archive)")
            continue
        if data.get("processing_failed"):
            continue

        # Check 2 — vault call note exists
        vault_path = data.get("vault_call_note")
        if vault_path and not (REPO_ROOT / vault_path).exists():
            missing_artifacts.append(f"{doc_id} (vault note {vault_path} missing)")

        # Check 3 (Phase 4) — thought-analysis artifacts named in archive exist
        for prompt_path in data.get("research_prompts_created", []) or []:
            if not (REPO_ROOT / prompt_path).exists():
                missing_thought_artifacts.append(f"{doc_id}: {prompt_path}")
        for sq_path in data.get("socrates_questions_created", []) or []:
            if not (REPO_ROOT / sq_path).exists():
                missing_thought_artifacts.append(f"{doc_id}: {sq_path}")

    if missing_artifacts:
        return fail(
            f"{len(missing_artifacts)} processed entries missing vault notes: "
            f"{', '.join(missing_artifacts[:5])}"
        )

    if missing_thought_artifacts:
        return fail(
            f"{len(missing_thought_artifacts)} thought-analysis artifacts named in archives "
            f"but missing on disk: {', '.join(missing_thought_artifacts[:5])}"
        )

    rotation_cutoff = now - timedelta(days=ROTATION_DAYS)
    rotation_candidates = [
        p.name
        for p in PROCESSED_DIR.glob("*.json")
        if p.name != ".gitkeep"
        and datetime.fromtimestamp(p.stat().st_mtime, timezone.utc) < rotation_cutoff
    ]
    if rotation_candidates:
        warn(f"{len(rotation_candidates)} processed entries past {ROTATION_DAYS}d rotation")

    # Surface task-queue depth for visibility (not a fail condition during
    # shadow mode — drain is Phase 4.5).
    task_queue_count = 0
    if TASK_QUEUE_DIR.exists():
        task_queue_count = len([p for p in TASK_QUEUE_DIR.glob("*.json") if p.name != ".gitkeep"])

    print(
        f"OK: queue={len(queue_files)} fresh, processed_today={len(today_processed)}, "
        f"ledger_total={len(ledger)}, task_queue_pending={task_queue_count}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
