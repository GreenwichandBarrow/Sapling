"""Chatroom handler: state sync after writes.

Delegates to existing chatroom-state-sync.py script since it has
complex state management with atomic file writes.
"""

import json
import os
import subprocess

from ..config import CHATROOM_PREFIX
from ..models import HandlerResult


def chatroom_state_sync(input_data: dict) -> HandlerResult:
    """PostToolUse[Write|Edit]: sync chatroom state after writes."""
    tool_input = input_data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if CHATROOM_PREFIX not in file_path or not file_path.endswith(".md"):
        return None

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    script_path = os.path.join(project_dir, ".claude", "hooks", "chatroom-state-sync.py")

    if not os.path.exists(script_path):
        return None

    try:
        result = subprocess.run(
            ["python3", script_path],
            input=json.dumps(input_data),
            capture_output=True,
            text=True,
            timeout=5,
            cwd=project_dir,
        )

        out = HandlerResult()

        if result.stdout.strip():
            try:
                parsed = json.loads(result.stdout.strip())
                if parsed.get("message"):
                    out.additional_context = parsed["message"]
            except json.JSONDecodeError:
                out.additional_context = result.stdout.strip()

        if result.stderr.strip():
            out.stderr_message = result.stderr.strip()

        return out if (out.additional_context or out.stderr_message) else None

    except subprocess.TimeoutExpired:
        return HandlerResult(stderr_message="[chatroom] chatroom-state-sync.py timed out")
    except Exception as e:
        return HandlerResult(stderr_message=f"[chatroom] chatroom-state-sync.py error: {e}")
