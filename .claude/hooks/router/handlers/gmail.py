"""Gmail handler: block email sending via gog CLI.

Prevents any gog gmail send or gog gmail drafts send command from executing.
Drafts can be created but must be sent from the Gmail UI.
"""

import re

from ..models import Decision, HandlerResult


def block_gmail_send(input_data: dict) -> HandlerResult:
    """PreToolUse[Bash]: block gog gmail send commands."""
    tool_input = input_data.get("tool_input", {})
    command = tool_input.get("command", "")

    if re.search(r'gog\s+(send|gmail\s+send|gmail\s+drafts\s+send)', command, re.IGNORECASE):
        return HandlerResult(
            decision=Decision.BLOCK,
            reason="Sending email is not permitted. Create a draft instead and send from Gmail UI.",
        )

    return None
