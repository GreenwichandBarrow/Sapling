"""Calibration handler: update stats after calibration output."""

import json
import os
import subprocess

from ..config import CALIBRATION_OUTPUT_PREFIX
from ..models import HandlerResult


def calibration_stats_updater(input_data: dict) -> HandlerResult:
    """PostToolUse[Write]: update stats.yaml after calibration output.

    Delegates to existing calibration-stats-updater.py script since
    it has complex logic (archiving traces, bumping version, git staging).
    """
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    if tool_name != "Write":
        return None

    file_path = tool_input.get("file_path", "")

    if CALIBRATION_OUTPUT_PREFIX not in file_path or not file_path.endswith(".md"):
        return None

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    script_path = os.path.join(project_dir, ".claude", "hooks", "calibration-stats-updater.py")

    if not os.path.exists(script_path):
        return None

    try:
        result = subprocess.run(
            ["python3", script_path],
            input=json.dumps(input_data),
            capture_output=True,
            text=True,
            timeout=10,
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
        return HandlerResult(stderr_message="[calibration] calibration-stats-updater.py timed out")
    except Exception as e:
        return HandlerResult(stderr_message=f"[calibration] calibration-stats-updater.py error: {e}")
