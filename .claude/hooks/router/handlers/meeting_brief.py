"""Meeting brief stop gate: confirms brief was saved to both Google Drive and vault."""

import os
import re
from datetime import datetime
from pathlib import Path

from ..models import Decision, HandlerResult


def meeting_brief_stop_check(input_data: dict) -> HandlerResult:
    """Stop hook: if a meeting-brief skill was invoked this session,
    remind the agent to confirm deliverables are in both locations."""

    transcript = input_data.get("transcript_summary", "")
    tool_history = input_data.get("tool_use_history", "")

    # Only trigger if the meeting-brief skill was actually invoked (not just mentioned)
    # Check tool_use_history for Skill tool calls with meeting-brief
    tool_text = str(tool_history)

    skill_invocation_signals = [
        '"skill": "meeting-brief"',
        "'skill': 'meeting-brief'",
        "skill: meeting-brief",
    ]

    # Also check if a brief file was actually written this session
    write_signals = [
        "brain/briefs/" in tool_text and ("Write" in tool_text or "write" in tool_text),
    ]

    session_involved_brief = (
        any(signal in tool_text for signal in skill_invocation_signals)
        or any(write_signals)
    )

    if not session_involved_brief:
        return None

    # Check if both deliverables exist for today
    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    today = datetime.now().strftime("%Y-%m-%d")
    briefs_dir = Path(project_dir) / "brain" / "briefs"

    vault_briefs_today = list(briefs_dir.glob(f"{today}-*.md")) if briefs_dir.exists() else []

    if not vault_briefs_today:
        return HandlerResult(
            decision=Decision.BLOCK,
            reason=(
                "Meeting brief workflow detected but no vault brief found for today.\n"
                "Before stopping, confirm:\n"
                "  1. Brief saved to brain/briefs/{date}-{slug}.md\n"
                "  2. Brief saved as Google Doc in RESEARCH/BRIEFS folder\n"
                "  3. Google Doc link shared with user"
            ),
        )

    # Vault file exists — just add a gentle reminder about Google Drive
    return HandlerResult(
        additional_context=(
            "MEETING BRIEF CHECK: Vault brief found. "
            "Confirm Google Doc was also saved to RESEARCH/BRIEFS folder "
            "and link was shared with user."
        ),
    )
