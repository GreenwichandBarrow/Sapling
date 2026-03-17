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

    # Heuristic: check if this session involved meeting brief work
    # Look for signals in the conversation context
    session_text = str(input_data)

    brief_signals = [
        "meeting-brief",
        "meeting brief",
        "Meeting Brief:",
        "brain/briefs/",
        "RESEARCH/BRIEFS",
        "1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ",
    ]

    session_involved_brief = any(signal in session_text for signal in brief_signals)

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
