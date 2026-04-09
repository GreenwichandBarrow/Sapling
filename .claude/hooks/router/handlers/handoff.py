"""Mid-day session handoff: save state + resume detection.

Handles the "save state" / "picking back up" protocol for multi-session days.
Distinct from continuation.py which handles auto-compaction recovery.
"""

import glob as glob_mod
import os
import re
from datetime import datetime
from pathlib import Path

from ..config import CONTINUATION_DIR, CONTINUATION_PREFIX
from ..models import HandlerResult


def _today_continuations() -> list[Path]:
    """Find all continuation files from today, sorted by sequence number."""
    today = datetime.now().strftime("%Y-%m-%d")
    pattern = str(CONTINUATION_DIR / f"{CONTINUATION_PREFIX}{today}-*.md")
    files = sorted(glob_mod.glob(pattern))
    return [Path(f) for f in files]


def _latest_continuation() -> Path | None:
    """Get the most recent continuation file from today."""
    files = _today_continuations()
    return files[-1] if files else None


def detect_save_state(input_data: dict) -> HandlerResult:
    """UserPromptSubmit: detect 'save state' and inject instructions."""
    prompt = input_data.get("prompt", "").strip().lower()

    # Match "save state", "saving state", etc.
    if not re.search(r'\bsav(e|ing)\s+state\b', prompt):
        return None

    today = datetime.now().strftime("%Y-%m-%d")
    existing = _today_continuations()
    seq = len(existing) + 1
    filename = f"{CONTINUATION_PREFIX}{today}-{seq}.md"
    filepath = CONTINUATION_DIR / filename

    return HandlerResult(
        additional_context=f"""SAVE STATE REQUESTED

Kay is ending this mid-day session. Write a continuation note NOW.

**File:** `{filepath}`
**Format:**
```yaml
---
date: {today}
type: context
title: "Continuation — {today} #{seq}"
saved_at: [current ISO timestamp]
session_number: {seq}
tags: ["date/{today}", "context", "topic/continuation"]
---
```

**Body — write these sections (200-300 words max total):**

## Active Threads
What we were working on and current state of each thread.

## Decisions Made This Session
Key decisions, approvals, rejections since last save point.

## Next Steps
What should happen next when Kay picks back up.

## Open Questions
Anything unresolved that needs Kay's input.

**After writing:**
1. Commit the continuation file to git
2. Confirm to Kay: "State saved. Pick back up anytime."
3. Do NOT write a session-decisions file (that's for good evening only)

IMPORTANT: Keep it tight. This is a handoff note, not a diary.""",
        suppress_further=True,
    )


def detect_picking_back_up(input_data: dict) -> HandlerResult:
    """UserPromptSubmit: detect 'picking back up' and inject continuation context."""
    prompt = input_data.get("prompt", "").strip().lower()

    # Match "picking back up", "pick back up", "picking up where we left off"
    if not re.search(r'\bpick(ing)?\s+(back\s+)?up\b', prompt):
        return None

    latest = _latest_continuation()
    if not latest:
        return HandlerResult(
            additional_context="""KAY IS RESUMING — but no continuation file found from today.

Read the most recent session-decisions file from brain/context/ and today's calendar (already injected by session start hook) to get oriented. Give Kay a quick summary of where things stand.""",
            suppress_further=True,
        )

    try:
        content = latest.read_text()
    except Exception:
        return HandlerResult(
            additional_context=f"KAY IS RESUMING — continuation file exists at {latest} but couldn't be read. Read it manually.",
            suppress_further=True,
        )

    return HandlerResult(
        additional_context=f"""KAY IS RESUMING MID-DAY SESSION

Continuation note loaded from: {latest}

{content}

---

INSTRUCTIONS:
1. Calendar is already injected by session start hook — reference it for timing
2. Give Kay a quick 3-5 line summary: "Here's where we are..." covering active threads and next steps
3. Do NOT re-run the morning briefing (email-intel, pipeline-manager, etc.)
4. Do NOT write a new continuation file
5. Just pick up where you left off""",
        suppress_further=True,
    )


def load_today_continuation(input_data: dict) -> HandlerResult:
    """SessionStart: if continuation files exist from today, inject the latest.

    This tells Claude it's a mid-day restart, not a fresh morning start.
    Suppresses the pipeline-pulse trigger so 'good morning' still works explicitly.
    """
    latest = _latest_continuation()
    if not latest:
        return None

    return HandlerResult(
        additional_context=f"""MID-DAY SESSION DETECTED

A continuation file exists from earlier today: {latest.name}
This means Kay has already had her morning briefing. Do NOT re-run the morning workflow automatically.

If Kay says "picking back up" — load the continuation file and resume.
If Kay says "good morning" — she wants the full briefing anyway (unusual but respect it).
If Kay says something else — just help with whatever she needs, continuity context is available if needed.""",
    )
