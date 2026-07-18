#!/usr/bin/env python3
"""Post-run validator for post-call-analyzer (rewritten 2026-05-13).

Per universal POST_RUN_CHECK doctrine (feedback_mutating_skill_hardening_pattern.md):
every scheduled mutating skill must have an integrity validator that runs after
the agent exits 0. Non-zero exit from this script → wrapper overrides skill exit
code → Slack alert with VALIDATOR FAILED prefix.

Checks (matches SKILL.md "Validator (mandatory)" section):
  1. Queue dir empty OR all entries <3h old (mid-flight tolerance)
  2. Each entry in processed.json ledger has doc_url + vault_call_note (or explicit
     failure marker)
  3. No file in processed/ older than 30 days (rotate -- WARN, not FAIL)
  4. Checkpoint file modification time <24h ago (detector ran recently)
  5. Pending staged task files are well-formed. Non-empty legacy backlog older
     than the next Good Morning cycle is WARN-only so a successful daily scan is
     not converted into a hard failure.

Self-locates REPO_ROOT for server (~/projects/Sapling) and Codex migration
worktrees.
"""

from __future__ import annotations

import json
import sys
import time
from pathlib import Path


def find_repo_root() -> Path:
    here = Path(__file__).resolve()
    for parent in [here.parent, *here.parents]:
        if (parent / "AGENTS.md").exists() and (parent / ".codex").exists():
            return parent
    for candidate in [
        Path.home() / "projects/Sapling",
    ]:
        if candidate.exists():
            return candidate
    raise SystemExit("validate_post_call_analyzer_integrity: could not locate REPO_ROOT")


REPO_ROOT = find_repo_root()
QUEUE_DIR = REPO_ROOT / "brain/trackers/post-call-analyzer/queue"
PROCESSED_DIR = REPO_ROOT / "brain/trackers/post-call-analyzer/processed"
PROCESSED_LEDGER = REPO_ROOT / "brain/trackers/post-call-analyzer/processed.json"
CHECKPOINT_FILE = Path.home() / ".cache/post-call-analyzer/last-checkpoint.txt"
PENDING_TASKS_DIR = REPO_ROOT / "brain/trackers/post-call-analyzer/pending-tasks"

STALE_QUEUE_HOURS = 3
STALE_CHECKPOINT_HOURS = 24
# A 6pm post-call run should wait for the next morning, but not survive into the
# following post-call cycle without Good Morning surfacing it.
STALE_PENDING_TASK_HOURS = 20
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


def validate_processed_ledger(ledger: object) -> list[str]:
    ledger_failures: list[str] = []

    # Ledger shapes supported:
    #   New (post-2026-05-13): {"processed": [{"id": ..., "doc_url": ..., ...}, ...], "last_updated": ...}
    #   New flat:              {"processed": ["id1", "id2", ...], "last_updated": ...}
    #   Legacy:                {"<id>": {<meta>}, ...}
    if isinstance(ledger, dict) and "processed" in ledger:
        items = ledger["processed"]
        if not isinstance(items, list):
            return [f"processed.json 'processed' field is {type(items).__name__}, expected list"]
        entries_iter = (
            items if items and isinstance(items[0], dict) else [{"id": e} for e in items]
        )
    elif isinstance(ledger, dict):
        entries_iter = [
            {"id": k, **v} if isinstance(v, dict) else {"id": k} for k, v in ledger.items()
        ]
    else:
        return [f"processed.json unexpected shape: {type(ledger).__name__}"]

    for entry in entries_iter:
        if not isinstance(entry, dict):
            ledger_failures.append(
                f"processed entry has unexpected shape: {type(entry).__name__}"
            )
            continue
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
        legacy_detector_only = (
            entry.get("detector")
            and entry.get("queued_at")
            and entry.get("created_at")
            and entry.get("updated_at")
        )
        if not has_artifacts:
            if legacy_detector_only:
                continue
            ledger_failures.append(f"processed entry {nid} has no artifact + no failure marker")
    return ledger_failures



def _extract_tasks(payload: object) -> tuple[list[object] | None, str | None]:
    if isinstance(payload, list):
        return payload, None
    if isinstance(payload, dict):
        for key in ("tasks", "items"):
            value = payload.get(key)
            if isinstance(value, list):
                return value, None
        return None, "object missing tasks/items array"
    return None, f"unexpected JSON shape: {type(payload).__name__}"


def check_pending_task_handoff() -> None:
    if not PENDING_TASKS_DIR.exists():
        return

    stale_nonempty: list[str] = []
    malformed: list[str] = []
    zero_task_old: list[str] = []

    for entry in PENDING_TASKS_DIR.iterdir():
        if not entry.is_file() or entry.name.startswith(".") or not entry.name.endswith(".json"):
            continue
        age_h = _mtime_age_hours(entry)
        try:
            payload = json.loads(entry.read_text())
        except json.JSONDecodeError as e:
            malformed.append(f"{entry.name}: malformed JSON: {e}")
            continue

        tasks, shape_error = _extract_tasks(payload)
        if shape_error:
            malformed.append(f"{entry.name}: {shape_error}")
            continue

        assert tasks is not None
        nonempty_tasks = []
        for idx, task in enumerate(tasks, start=1):
            if not isinstance(task, dict):
                malformed.append(f"{entry.name}: task {idx} has shape {type(task).__name__}")
                continue
            task_text = str(task.get("task_text") or "").strip()
            source = task.get("source_call_id") or task.get("source_doc_url") or task.get("source_transcript_url")
            staged = task.get("staged_at") or entry.stat().st_mtime
            if not task_text:
                malformed.append(f"{entry.name}: task {idx} missing task_text")
            if not source:
                malformed.append(f"{entry.name}: task {idx} missing source_call_id/source_doc_url")
            if not staged:
                malformed.append(f"{entry.name}: task {idx} missing staged_at and mtime fallback")
            if task_text:
                nonempty_tasks.append(task_text)

        if nonempty_tasks and age_h > STALE_PENDING_TASK_HOURS:
            stale_nonempty.append(f"{entry.name} ({len(nonempty_tasks)} tasks, {age_h:.1f}h old)")
        elif not nonempty_tasks and age_h > STALE_PENDING_TASK_HOURS:
            zero_task_old.append(f"{entry.name} ({age_h:.1f}h old)")

    if malformed:
        failures.append(
            "Malformed staged post-call task file(s): "
            f"{'; '.join(malformed[:5])}{'...' if len(malformed) > 5 else ''}"
        )
    if stale_nonempty:
        warnings.append(
            "HANDOFF-WARN: staged post-call tasks pending Good Morning review: "
            f"{'; '.join(stale_nonempty[:8])}{'...' if len(stale_nonempty) > 8 else ''}"
        )
    if zero_task_old:
        warnings.append(
            f"{len(zero_task_old)} zero-task pending file(s) older than {STALE_PENDING_TASK_HOURS}h; "
            f"archive or mark zero-action: {', '.join(zero_task_old[:3])}{'...' if len(zero_task_old) > 3 else ''}"
        )

def check_processed_entries() -> None:
    if not PROCESSED_LEDGER.exists():
        return
    try:
        ledger = json.loads(PROCESSED_LEDGER.read_text())
    except json.JSONDecodeError as e:
        failures.append(f"processed.json malformed: {e}")
        return

    failures.extend(validate_processed_ledger(ledger))


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
    check_pending_task_handoff()

    print(f"REPO_ROOT: {REPO_ROOT}")
    print(f"Checks complete: {len(failures)} failures, {len(warnings)} warnings")
    for w in warnings:
        print(f"  WARN: {w}")
    for f in failures:
        print(f"  FAIL: {f}")

    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
