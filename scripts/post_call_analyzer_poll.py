#!/usr/bin/env python3
"""
post_call_analyzer_poll.py — Cheap poller for the post-call-analyzer skill.

Runs every 10 min via launchd. Detects new Granola transcripts in the local
cache and writes per-doc trigger files to the queue dir. Only fires the
expensive Claude run when the queue is non-empty.

Business-hours gate: Mon-Fri 8am-7pm America/New_York. Outside → exit 0.

Idempotency: writes to queue/{doc_id}.json are overwrite-safe. processed.json
gates duplicate downstream processing.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

WORKDIR = Path(os.environ["HOME"]) / "Documents" / "AI Operations"
GRANOLA_CACHE = (
    Path(os.environ["HOME"]) / "Library" / "Application Support" / "Granola" / "cache-v6.json"
)
TRACKER_DIR = WORKDIR / "brain" / "trackers" / "post-call-analyzer"
QUEUE_DIR = TRACKER_DIR / "queue"
PROCESSED_DIR = TRACKER_DIR / "processed"
PROCESSED_LEDGER = TRACKER_DIR / "processed.json"
LOG_DIR = WORKDIR / "logs" / "scheduled"
LOG_FILE = LOG_DIR / f"post-call-analyzer-poll-{datetime.now().strftime('%Y-%m-%d')}.log"

LOOKBACK_MIN = 60
MIN_CONTENT_LEN = 100
MIN_TRANSCRIPT_ENTRIES = 5
ET = ZoneInfo("America/New_York")


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%H:%M:%S")
    with LOG_FILE.open("a") as f:
        f.write(f"[{ts}] {msg}\n")


def in_business_hours() -> bool:
    now = datetime.now(ET)
    if now.weekday() >= 5:
        return False
    return 8 <= now.hour < 19


def load_processed() -> dict:
    if not PROCESSED_LEDGER.exists():
        return {}
    try:
        return json.loads(PROCESSED_LEDGER.read_text() or "{}")
    except json.JSONDecodeError as exc:
        log(f"WARN: processed.json corrupt ({exc}); treating as empty")
        return {}


def load_granola_cache() -> dict | None:
    if not GRANOLA_CACHE.exists():
        log(f"WARN: Granola cache not found at {GRANOLA_CACHE}")
        return None
    try:
        with GRANOLA_CACHE.open() as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as exc:
        log(f"WARN: Granola cache read failed ({exc}); will retry next poll")
        return None


def has_extractable_content(doc: dict, transcripts: dict) -> tuple[bool, str]:
    """Granola lazily populates notes_plain after server-side summarization.
    Check multiple sources before declaring the doc ready for processing."""
    notes_plain = (doc.get("notes_plain") or "").strip()
    if len(notes_plain) >= MIN_CONTENT_LEN:
        return True, "notes_plain"
    notes_markdown = (doc.get("notes_markdown") or "").strip()
    if len(notes_markdown) >= MIN_CONTENT_LEN:
        return True, "notes_markdown"
    transcript = transcripts.get(doc["id"]) if isinstance(transcripts, dict) else None
    if isinstance(transcript, list) and len(transcript) >= MIN_TRANSCRIPT_ENTRIES:
        return True, f"transcript({len(transcript)} entries)"
    return False, "no-content-yet"


def find_new_docs(cache: dict, processed: dict) -> list[dict]:
    state = cache.get("cache", {}).get("state", {})
    documents = state.get("documents", {})
    transcripts = state.get("transcripts", {})
    if not isinstance(documents, dict):
        log(f"WARN: documents is {type(documents).__name__}, expected dict")
        return []

    cutoff = datetime.now(timezone.utc) - timedelta(minutes=LOOKBACK_MIN)
    new_docs = []

    for doc_id, doc in documents.items():
        if not isinstance(doc, dict):
            continue
        if doc_id in processed:
            continue
        if doc.get("deleted_at"):
            continue
        if not doc.get("meeting_end_count", 0):
            continue

        updated_at_raw = doc.get("updated_at") or doc.get("created_at")
        if not updated_at_raw:
            continue
        try:
            updated_at = datetime.fromisoformat(updated_at_raw.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            continue
        if updated_at < cutoff:
            continue

        ready, content_source = has_extractable_content(doc, transcripts)
        if not ready:
            log(f"  skip {doc_id[:8]} — meeting ended but no content yet ({content_source})")
            continue

        notes_plain = (doc.get("notes_plain") or "").strip()
        new_docs.append({
            "id": doc_id,
            "title": doc.get("title") or "(untitled)",
            "created_at": doc.get("created_at"),
            "updated_at": doc.get("updated_at"),
            "content_source": content_source,
            "notes_plain_preview": notes_plain[:500] if notes_plain else "",
            "notes_plain_len": len(notes_plain),
            "people": doc.get("people") or [],
            "google_calendar_event": doc.get("google_calendar_event"),
            "type": doc.get("type"),
            "has_transcript": isinstance(transcripts.get(doc_id), list),
            "meeting_end_count": doc.get("meeting_end_count", 0),
        })

    return new_docs


def write_queue(docs: list[dict]) -> int:
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for doc in docs:
        out = QUEUE_DIR / f"{doc['id']}.json"
        out.write_text(json.dumps(doc, indent=2, default=str))
        written += 1
    return written


def trigger_claude_run() -> int:
    wrapper = WORKDIR / "scripts" / "run-skill.sh"
    if not wrapper.exists():
        log(f"ERROR: wrapper not found at {wrapper}")
        return 1
    log("Queue non-empty → invoking run-skill.sh post-call-analyzer on-trigger (background)")
    proc = subprocess.Popen(
        ["/bin/bash", str(wrapper), "post-call-analyzer", "on-trigger"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    return 0


def main() -> int:
    TRACKER_DIR.mkdir(parents=True, exist_ok=True)
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    if not in_business_hours():
        return 0

    # Architecture (2026-05-07): launchd's WatchPaths fires this script ONLY
    # when Granola writes to cache-v6.json. The write IS the trigger. No
    # polling, no calendar gate (which would falsely reject calls whose
    # Granola flush lags behind the call-end window). Idempotency via
    # processed.json + meeting_end_count filter inside find_new_docs().
    cache = load_granola_cache()
    if cache is None:
        return 0

    processed = load_processed()
    new_docs = find_new_docs(cache, processed)

    if not new_docs:
        return 0

    log(f"Found {len(new_docs)} new doc(s): {', '.join(d['id'][:8] for d in new_docs)}")
    written = write_queue(new_docs)
    log(f"Wrote {written} queue file(s)")

    return trigger_claude_run()


if __name__ == "__main__":
    sys.exit(main())
