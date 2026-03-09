"""Orchestrator stop gate: prevents stopping while background tasks run."""

import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from ..config import CHATROOM_PREFIX
from ..models import Decision, HandlerResult

STATE_DIR = Path(os.path.expanduser("~/.claude/hook-state"))
MAX_ATTEMPTS = 3


def orchestrator_stop_gate(input_data: dict) -> HandlerResult:
    """Stop hook: block orchestrator from stopping with active tasks."""
    session_id = input_data.get("session_id", "unknown")

    if input_data.get("stop_hook_active"):
        return None

    state = _load_state(session_id)

    if not state.get("task_ids"):
        return None

    attempt = state.get("stop_attempt", 0)

    if attempt >= MAX_ATTEMPTS:
        _cleanup_state(session_id)
        return None

    chatroom = _find_active_chatroom()

    if chatroom:
        content = chatroom.read_text()

        if re.search(r'→\s*CLOSE', content):
            _cleanup_state(session_id)
            return None

        incomplete = _check_incomplete_coordination(content, state)

        if incomplete:
            attempt += 1
            state["stop_attempt"] = attempt
            _save_state(session_id, state)

            return HandlerResult(
                decision=Decision.BLOCK,
                reason=_construct_block_message(incomplete, attempt, chatroom),
            )

    _cleanup_state(session_id)
    return None


def _find_active_chatroom() -> Optional[Path]:
    """Find the most recent active chatroom file."""
    cwd = Path.cwd()
    agents_dir = cwd / CHATROOM_PREFIX

    if not agents_dir.exists():
        script_dir = Path(__file__).parent.parent.parent.parent
        agents_dir = script_dir / CHATROOM_PREFIX

    if not agents_dir.exists():
        return None

    today = datetime.now().strftime("%Y-%m-%d")

    for pattern in [f"{today}*.md", "*.md"]:
        for f in sorted(agents_dir.glob(pattern), reverse=True):
            try:
                content = f.read_text()
                if "status: active" in content:
                    return f
            except Exception:
                continue

    return None


def _check_incomplete_coordination(content: str, state: dict) -> Optional[dict]:
    """Check if coordination is incomplete."""
    issues = []

    waiting = re.findall(r'→\s*WAITING\s+@(\w+)', content)
    if waiting:
        issues.append(f"Agents still waiting: {', '.join(set(waiting))}")

    blocked = re.findall(r'→\s*BLOCKED:\s*(.+)', content)
    if blocked:
        issues.append(f"Unresolved blockers: {len(blocked)}")

    expected_agents = state.get("expected_agents", [])
    if expected_agents:
        ready_agents = set(re.findall(r'\[.*?\]\s*(\w+).*?→\s*READY', content, re.DOTALL))
        missing = set(expected_agents) - ready_agents
        if missing:
            issues.append(f"Agents not READY: {', '.join(missing)}")

    orchestrator_waiting = re.findall(r'→\s*WAITING\s+@orchestrator', content, re.IGNORECASE)
    orchestrator_responses = re.findall(r'\[.*?\]\s*orchestrator\n', content)
    if len(orchestrator_waiting) > len(orchestrator_responses):
        issues.append("Unaddressed requests to orchestrator")

    return {"issues": issues} if issues else None


def _construct_block_message(incomplete: dict, attempt: int, chatroom: Path) -> str:
    """Construct block message for orchestrator."""
    lines = [
        f"Coordination incomplete (attempt {attempt}/{MAX_ATTEMPTS})",
        "",
        "Issues:"
    ]

    for issue in incomplete.get("issues", []):
        lines.append(f"  - {issue}")

    lines.extend([
        "",
        "Before stopping, you should:",
        "  1. Check background tasks with TaskOutput(task_id, block=false)",
        "  2. Read chatroom for any WAITING @orchestrator signals",
        "  3. Handle any crashed agents (post BLOCKED on their behalf)",
        "  4. Post → CLOSE when coordination is complete",
        "",
        f"Chatroom: {chatroom}"
    ])

    return "\n".join(lines)


def _load_state(session_id: str) -> dict:
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_file = STATE_DIR / f"orchestrator-{session_id}.json"
    try:
        with open(state_file) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def _save_state(session_id: str, state: dict):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    state_file = STATE_DIR / f"orchestrator-{session_id}.json"
    with open(state_file, "w") as f:
        json.dump(state, f)


def _cleanup_state(session_id: str):
    state_file = STATE_DIR / f"orchestrator-{session_id}.json"
    try:
        state_file.unlink()
    except FileNotFoundError:
        pass
