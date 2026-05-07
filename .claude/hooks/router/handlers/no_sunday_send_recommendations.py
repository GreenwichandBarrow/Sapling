"""Stop handler: block messages that recommend sending emails on Sunday.

Kay's rule (memory/feedback_no_sunday_emails.md): "No Sunday business emails.
Draft on weekend, schedule for Monday AM." Rule covers my recommendations to
Kay, since I don't actually send emails myself — the violation is when I say
"go ahead and send" on a Sunday.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional

from ..models import Decision, HandlerResult

SEND_PHRASES = re.compile(
    r"\b("
    r"go ahead and send|ready to send|push to send|fire the send|hit send|click send|"
    r"send it|send now|send today|send this now|send the draft|send it out|"
    r"push it to send|push now|fire it off|push the draft"
    r")\b",
    re.IGNORECASE,
)


def no_sunday_send_recommendations(input_data: dict) -> Optional[HandlerResult]:
    if input_data.get("stop_hook_active"):
        return None

    # Sunday is weekday() == 6
    if datetime.now().weekday() != 6:
        return None

    transcript_path = input_data.get("transcript_path", "")
    if not transcript_path:
        return None

    text = _extract_last_assistant_text(transcript_path)
    if not text:
        return None

    # Strip code blocks — shell commands that happen to say "send" shouldn't block
    stripped = re.sub(r"```[\s\S]*?```", "", text)
    stripped = re.sub(r"`[^`]*`", "", stripped)

    match = SEND_PHRASES.search(stripped)
    if not match:
        return None

    reason = (
        f"Rule violation (no-sunday-send-recommendations): you recommended "
        f"'{match.group(0)}' on a Sunday. Per memory/feedback_no_sunday_emails, "
        "never recommend Kay send business emails on Sunday — drafts should be "
        "scheduled for Monday AM instead. Rewrite to propose scheduling the send "
        "for Monday morning rather than sending today."
    )
    return HandlerResult(decision=Decision.BLOCK, reason=reason)


def _extract_last_assistant_text(transcript_path: str) -> str:
    p = Path(transcript_path)
    if not p.exists():
        return ""
    try:
        lines = p.read_text().splitlines()
    except Exception:
        return ""
    for line in reversed(lines):
        line = line.strip()
        if not line:
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if entry.get("type") != "assistant":
            continue
        message = entry.get("message", {}) or {}
        content = message.get("content", []) or []
        parts = [
            block.get("text", "")
            for block in content
            if isinstance(block, dict) and block.get("type") == "text"
        ]
        if parts:
            return "\n".join(parts)
    return ""
