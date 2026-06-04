"""Block writes of low-signal verb-log "traces" to brain/traces/.

Why this exists:
- 2026-05-21 Thursday meta-calibration found 13-14 mechanical CRUD receipts
  from task-tracker-manager in a single week, each emitted as a "decision
  trace" despite failing the decision-traces litmus test. They drowned out
  real signal in the calibration input.

Block conditions (ALL must hold):
- file_path matches brain/traces/*.md (NOT brain/traces/agents/ or processed/)
- file body (excluding frontmatter) is <= 15 non-empty lines
- frontmatter `tags` contains an entry beginning with `verb/`
- body has no `## Decisions` (or `# Decisions`, `### Decisions`) heading

When blocked, suggests redirecting to brain/context/verb-logs/.
"""

import re
from typing import Optional

from ..models import Decision, HandlerResult


def _extract_frontmatter_and_body(content: str) -> tuple[str, str]:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return "", content
    return match.group(1), match.group(2)


def _has_verb_tag(frontmatter: str) -> bool:
    if re.search(r"^\s*-\s*verb/", frontmatter, re.MULTILINE):
        return True
    if re.search(r"tags:\s*\[[^\]]*verb/", frontmatter):
        return True
    return False


def _has_decisions_section(body: str) -> bool:
    return bool(re.search(r"^#{1,3}\s+Decisions\b", body, re.MULTILINE | re.IGNORECASE))


def block_verb_log_traces(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Write|Edit]: block verb-log receipts disguised as traces."""
    tool_input = input_data.get("tool_input") or {}
    file_path = tool_input.get("file_path", "")

    if "brain/traces/" not in file_path:
        return None
    if "brain/traces/agents/" in file_path or "brain/traces/processed/" in file_path:
        return None
    if not file_path.endswith(".md"):
        return None

    content = tool_input.get("content") or tool_input.get("new_string") or ""
    if not content:
        return None

    frontmatter, body = _extract_frontmatter_and_body(content)
    body_lines = [ln for ln in body.split("\n") if ln.strip()]

    if len(body_lines) > 15:
        return None
    if not _has_verb_tag(frontmatter):
        return None
    if _has_decisions_section(body):
        return None

    msg = (
        f"BLOCKED: trace_litmus_guard\n"
        f"File: {file_path}\n"
        f"This looks like a verb-log receipt (≤15 non-empty body lines, verb/ tag, no Decisions section).\n"
        f"Per decision-traces SKILL.md anti-pattern #6, mechanical CRUD receipts are not decision\n"
        f"traces — they drown real signal in calibration analysis.\n"
        f"Options:\n"
        f"  1. Redirect to brain/context/verb-logs/{{slug}}.md if you need to log the action.\n"
        f"  2. Add a Decisions section with a real choice-between-alternatives.\n"
        f"  3. Skip the trace entirely (per decision-traces permission_to_skip).\n"
    )
    return HandlerResult(
        decision=Decision.BLOCK,
        reason="verb-log trace fails decision-traces litmus",
        stderr_message=msg,
        exit_code=2,
    )
