"""Gmail handler: block email sending via gog CLI.

Prevents gog Gmail send-like commands from executing. Drafts can be created,
but send, draft-send, forward, and autoreply paths are blocked. Completed
drafts must be sent from the Gmail UI.
"""

import re

from ..models import Decision, HandlerResult


_GMAIL_SEND_RE = re.compile(
    r"gog\s+(send|gmail\s+(send|forward|autoreply|drafts?\s+send))",
    re.IGNORECASE,
)


def block_gmail_send(input_data: dict) -> HandlerResult:
    """PreToolUse[Bash]: block gog Gmail send-like commands."""
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    if _GMAIL_SEND_RE.search(command):
        return HandlerResult(
            decision=Decision.BLOCK,
            reason="Sending email is not permitted. Create a draft instead and send from Gmail UI.",
        )

    return None
