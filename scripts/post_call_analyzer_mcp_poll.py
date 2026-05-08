#!/usr/bin/env python3
"""
post_call_analyzer_mcp_poll.py — Phase 4 server-side detector for the
post-call-analyzer skill.

Replaces the iMac-only `post_call_analyzer_poll.py` Granola-local-cache reader.
Runs on the Linux server every 5 min via systemd OnUnitActiveSec=5min.

Architecture:
  - Calls Granola MCP `mcp__granola__list_meetings` via `claude -p` as a thin
    MCP client subprocess (Granola MCP is OAuth-gated; Claude Code already
    knows how to handle the auth handshake when a server is registered with
    `claude mcp add granola https://mcp.granola.ai/mcp`).
  - Granola's MCP exposes start time only (its `date` field) — there is no
    `ended_at` field. We anchor on `started_at` and require the call to have
    started >=90min ago so a 1h call that ran 30min over still gets caught
    after it actually ends. Window: cutoff_old <= started_at <= now - 90min.
  - For qualifying meetings not already in processed.json, drops a queue file
    at brain/trackers/post-call-analyzer/queue/{meeting_id}.json.
  - If the queue is non-empty, fires the run-skill.sh wrapper which runs the
    headless Claude prompt to drain the queue.

Defensive against MCP downtime: any failure (claude binary missing, MCP not
configured, network timeout, malformed JSON) → log + exit 0 so the timer
keeps firing. The validator catches stale queue entries (>30 min) on the
next successful run.

Idempotency: keyed on Granola cloud meeting ID. processed.json is the canonical
ledger. The iMac sidecar (post_call_analyzer_poll.py) writes to the same ledger
during shadow mode; whichever detector wins the race writes the queue first
and the other no-ops on its next tick.

NO business-hours gate (server runs 24/7 — Kay's call cadence determines
load, not a clock).
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TRACKER_DIR = REPO_ROOT / "brain" / "trackers" / "post-call-analyzer"
QUEUE_DIR = TRACKER_DIR / "queue"
PROCESSED_LEDGER = TRACKER_DIR / "processed.json"
LOG_DIR = REPO_ROOT / "logs" / "scheduled"
LOG_FILE = LOG_DIR / f"post-call-analyzer-mcp-poll-{datetime.now().strftime('%Y-%m-%d')}.log"
WRAPPER = REPO_ROOT / "scripts" / "run-skill.sh"

LOOKBACK_HOURS = 24
MIN_AGE_MINUTES = 90  # meeting must have started >=1.5h ago to be considered ended (covers 30min + 1h calls + 30min runover)
CLAUDE_TIMEOUT_SEC = 180

# Use the same Claude binary path the wrapper uses, so behavior matches.
CLAUDE_BIN = Path(os.environ.get("CLAUDE_BIN", str(Path.home() / ".local" / "bin" / "claude")))

DETECT_PROMPT = """Use the mcp__granola__list_meetings tool to list meetings from the last 24 hours.

Output ONLY a JSON array. No markdown fences, no preamble, no commentary, no explanation. Each element must be an object with these fields exactly:

{
  "id": "<granola meeting id (string)>",
  "title": "<meeting title (string)>",
  "started_at": "<ISO 8601 UTC timestamp; pass through Granola's date field>",
  "attendees": [<array of strings — emails preferred, names if email unavailable>]
}

If the MCP call fails or returns no meetings, output exactly: []

Do not call any other MCP tool. Do not write files. Do not produce any text other than the JSON array.
"""


def log(msg: str) -> None:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%H:%M:%S")
    with LOG_FILE.open("a") as f:
        f.write(f"[{ts}] {msg}\n")


def load_processed() -> dict:
    if not PROCESSED_LEDGER.exists():
        return {}
    try:
        return json.loads(PROCESSED_LEDGER.read_text() or "{}")
    except json.JSONDecodeError as exc:
        log(f"WARN: processed.json corrupt ({exc}); treating as empty")
        return {}


def call_mcp_via_claude() -> list[dict] | None:
    """Invoke `claude -p` as MCP client. Returns parsed list or None on hard fail.

    None means 'no signal this tick' — caller treats it as no-op, not an error
    to surface. The validator handles stale state on the next successful run.
    """
    if not CLAUDE_BIN.exists():
        log(f"ERROR: claude binary missing at {CLAUDE_BIN} — install or set $CLAUDE_BIN")
        return None
    try:
        proc = subprocess.run(
            [str(CLAUDE_BIN), "-p", "--dangerously-skip-permissions"],
            input=DETECT_PROMPT,
            capture_output=True,
            text=True,
            timeout=CLAUDE_TIMEOUT_SEC,
        )
    except subprocess.TimeoutExpired:
        log(f"WARN: claude -p timed out after {CLAUDE_TIMEOUT_SEC}s; will retry next tick")
        return None
    except OSError as exc:
        log(f"WARN: claude -p invocation failed: {exc}")
        return None

    if proc.returncode != 0:
        log(f"WARN: claude -p exit {proc.returncode}; stderr tail: {proc.stderr[-300:]!r}")
        return None

    raw = proc.stdout.strip()
    if not raw:
        log("WARN: claude -p returned empty stdout")
        return None

    # Tolerate occasional code fences despite the 'no fences' instruction.
    if raw.startswith("```"):
        lines = [ln for ln in raw.splitlines() if not ln.strip().startswith("```")]
        raw = "\n".join(lines).strip()

    try:
        meetings = json.loads(raw)
    except json.JSONDecodeError:
        log(f"WARN: non-JSON response; head: {raw[:300]!r}")
        return None
    if not isinstance(meetings, list):
        log(f"WARN: expected JSON list, got {type(meetings).__name__}")
        return None
    return meetings


def parse_iso(ts_str: str | None) -> datetime | None:
    if not ts_str or not isinstance(ts_str, str):
        return None
    try:
        t = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
    except ValueError:
        return None
    if t.tzinfo is None:
        t = t.replace(tzinfo=timezone.utc)
    return t


def filter_new_meetings(meetings: list[dict], processed: dict) -> list[dict]:
    now = datetime.now(timezone.utc)
    cutoff_old = now - timedelta(hours=LOOKBACK_HOURS)
    cutoff_recent = now - timedelta(minutes=MIN_AGE_MINUTES)
    new_ones: list[dict] = []
    for m in meetings:
        if not isinstance(m, dict):
            continue
        mid = m.get("id")
        if not mid or not isinstance(mid, str):
            continue
        if mid in processed:
            continue
        # Already-queued (race with iMac sidecar) → skip; the in-flight wrapper
        # will pick it up.
        if (QUEUE_DIR / f"{mid}.json").exists():
            continue
        started = parse_iso(m.get("started_at"))
        if started is None:
            continue
        # Window: started in last 24h AND >=90min ago (call has likely ended)
        if started < cutoff_old or started > cutoff_recent:
            continue
        new_ones.append(m)
    return new_ones


def write_queue(meetings: list[dict]) -> int:
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for m in meetings:
        out = QUEUE_DIR / f"{m['id']}.json"
        # Carry the source flag so the headless prompt knows to read transcripts
        # via mcp__granola__get_meeting_transcript instead of the local cache.
        payload = dict(m)
        payload["detector"] = "mcp"
        payload["queued_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
        out.write_text(json.dumps(payload, indent=2, default=str))
        written += 1
    return written


def trigger_claude_run() -> int:
    if not WRAPPER.exists():
        log(f"ERROR: wrapper missing at {WRAPPER}")
        return 1
    log("Queue non-empty → invoking run-skill.sh post-call-analyzer on-trigger (background)")
    subprocess.Popen(
        ["/bin/bash", str(WRAPPER), "post-call-analyzer", "on-trigger"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    return 0


def main() -> int:
    TRACKER_DIR.mkdir(parents=True, exist_ok=True)
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)

    meetings = call_mcp_via_claude()
    if meetings is None:
        return 0  # defensive — already logged; never break the timer

    if not meetings:
        return 0  # no recent meetings — silent no-op

    processed = load_processed()
    new_ones = filter_new_meetings(meetings, processed)
    if not new_ones:
        return 0

    log(f"Found {len(new_ones)} new meeting(s): {', '.join(m['id'][:8] for m in new_ones)}")
    written = write_queue(new_ones)
    log(f"Wrote {written} queue file(s)")
    return trigger_claude_run()


if __name__ == "__main__":
    sys.exit(main())
