"""Skill frontmatter guard.

Warns when a Write/Edit/MultiEdit to a SKILL.md file would leave the file
without valid `archetype` + `context_budget` frontmatter.

Why this exists:
- The evolving-skills plugin pattern (adopted 2026-05-15) requires every
  skill to declare its archetype and context budget so the Chief-of-Staff
  orchestrator can plan context spend per skill.
- The four archetypes are simple (<=150 lines), router (<=200), orchestrator
  (<=200), reference (<=100). The budget block declares skill_md,
  max_references, learnings_md, and sub_agent_limit.
- Without this hook, a contributor (or Claude) can silently drop the frontmatter
  when editing a skill — the orchestrator then has no context budget to honor.

Strategy: warn, don't block. Frontmatter conventions change; we want a loud
nudge in stderr that surfaces in transcript, not a hard stop that breaks
legitimate refactors. The hook returns NONE (no block) and emits a
stderr_message so Claude sees it next turn.

Matches Write/Edit/MultiEdit on file paths ending in /SKILL.md.
"""

from __future__ import annotations

import re
from typing import Optional

import yaml

from ..models import Decision, HandlerResult


_SKILL_MD_RX = re.compile(r"(^|/)SKILL\.md$")

_VALID_ARCHETYPES = {"simple", "router", "orchestrator", "reference"}

# Required context_budget keys. skill_md is mandatory; the others are strong
# defaults but not all skills set every one. We warn only on missing skill_md.
_REQUIRED_BUDGET_KEYS = {"skill_md"}
_RECOMMENDED_BUDGET_KEYS = {"max_references", "learnings_md", "sub_agent_limit"}


def _extract_full_content(tool_name: str, tool_input: dict) -> Optional[str]:
    """Return the full proposed file content if we can reconstruct it.

    For Write: the new content IS the full file.
    For Edit/MultiEdit: we don't have the original — we can only inspect the
    new_string fragments. We treat those as enough signal to detect the case
    where the edit operates on the frontmatter block itself.
    """
    if tool_name == "Write":
        return tool_input.get("content", "") or ""
    if tool_name == "Edit":
        # An Edit could be modifying frontmatter or body. We can't tell without
        # reading disk. Return new_string so we can inspect it for partial
        # frontmatter — better than nothing.
        return tool_input.get("new_string", "") or ""
    if tool_name == "MultiEdit":
        edits = tool_input.get("edits", []) or []
        return "\n".join((e.get("new_string", "") or "") for e in edits)
    return None


def _parse_frontmatter(text: str) -> Optional[dict]:
    """Parse leading YAML frontmatter. Returns dict on success, None otherwise."""
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    if lines[0].strip() != "---":
        return None
    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None
    fm_str = "\n".join(lines[1:end_idx])
    try:
        data = yaml.safe_load(fm_str)
    except yaml.YAMLError:
        return {"__yaml_error__": True}
    if not isinstance(data, dict):
        return None
    return data


def _diagnose(fm: Optional[dict]) -> list[str]:
    """Return a list of warning messages for missing/malformed fields."""
    issues: list[str] = []

    if fm is None:
        issues.append("no YAML frontmatter detected (file should start with `---`)")
        return issues

    if fm.get("__yaml_error__"):
        issues.append("frontmatter YAML failed to parse — check for unquoted colons or bad indentation")
        return issues

    archetype = fm.get("archetype")
    if archetype is None:
        issues.append("missing `archetype:` field (expected one of: simple, router, orchestrator, reference)")
    elif archetype not in _VALID_ARCHETYPES:
        issues.append(
            f"archetype `{archetype}` is not a recognized value "
            f"(expected one of: simple, router, orchestrator, reference)"
        )

    cb = fm.get("context_budget")
    if cb is None:
        issues.append("missing `context_budget:` mapping (must declare at minimum `skill_md:`)")
    elif not isinstance(cb, dict):
        issues.append(f"`context_budget:` must be a mapping, got {type(cb).__name__}")
    else:
        missing_required = _REQUIRED_BUDGET_KEYS - set(cb.keys())
        if missing_required:
            issues.append(
                f"`context_budget:` missing required key(s): {sorted(missing_required)}"
            )
        # Type-check skill_md if present
        if "skill_md" in cb:
            sm = cb["skill_md"]
            if not isinstance(sm, int) or sm <= 0:
                issues.append(
                    f"`context_budget.skill_md` must be a positive integer, got `{sm!r}`"
                )
        missing_recommended = _RECOMMENDED_BUDGET_KEYS - set(cb.keys())
        if missing_recommended:
            issues.append(
                f"`context_budget:` missing recommended key(s) "
                f"(not blocked, but please add): {sorted(missing_recommended)}"
            )

    return issues


def check_skill_frontmatter(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Write|Edit|MultiEdit]: warn if SKILL.md write loses frontmatter."""
    tool_name = input_data.get("tool_name", "")
    if tool_name not in ("Write", "Edit", "MultiEdit"):
        return None

    tool_input = input_data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""
    if not _SKILL_MD_RX.search(file_path):
        return None

    content = _extract_full_content(tool_name, tool_input)
    if content is None:
        return None

    # For Write: content is the whole file — we can be authoritative.
    # For Edit/MultiEdit: content is a fragment — we can only warn if the
    # fragment LOOKS like it touches frontmatter (contains `---` or starts
    # with `name:`/`archetype:`/`context_budget:`). Otherwise body-only edits
    # are skipped.
    if tool_name in ("Edit", "MultiEdit"):
        fragment_touches_fm = (
            "---" in content
            or re.search(r"(?m)^\s*(archetype|context_budget|name|description)\s*:", content) is not None
        )
        if not fragment_touches_fm:
            return None

    fm = _parse_frontmatter(content)
    issues = _diagnose(fm)
    if not issues:
        return None

    lines = [
        f"[skill-frontmatter-guard] {tool_name} on {file_path} would leave "
        f"the SKILL.md frontmatter in a state the orchestrator can't read:",
    ]
    for issue in issues:
        lines.append(f"  - {issue}")
    lines.extend([
        "",
        "Required frontmatter shape:",
        "  ---",
        "  name: <skill-name>",
        "  description: <when to use; trigger phrases>",
        "  archetype: simple | router | orchestrator | reference",
        "  context_budget:",
        "    skill_md: 200",
        "    max_references: 12",
        "    learnings_md: 40",
        "    sub_agent_limit: 500",
        "  ---",
        "",
        "Archetype caps: simple<=150, router<=200, orchestrator<=200, reference<=100.",
        "Reference templates: .claude/skills/create-skill/SKILL.md, .claude/skills/evolve/SKILL.md",
        "",
        "Note: this is a WARNING, not a block. The write will proceed. Fix on next edit.",
    ])
    msg = "\n".join(lines)

    return HandlerResult(
        decision=Decision.NONE,
        stderr_message=msg,
        additional_context=msg,
    )
