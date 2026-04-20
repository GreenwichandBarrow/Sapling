"""One-pager guardrail handler.

Blocks Write/Edit operations that insert personal or team-centric content
into niche one-pager files. Artifacts (one-pagers, scorecards, tracker
entries) must be pure industry analysis — the litmus test from
feedback_artifacts_pure_industry_analysis.md is that the artifact must
read identically regardless of which searcher is evaluating the niche.

This handler plugs into the existing router framework:
- Matches Write/Edit/MultiEdit tool calls
- Only inspects writes to files in brain/outputs whose names contain
  "one-pager", "onepager", or "niche-onepager"
- Strips frontmatter and wiki-links before pattern detection to avoid
  false positives on auto-generated fields like people: [[entities/...]]
- Returns Decision.BLOCK with a detailed reason when violations are found
"""

from __future__ import annotations

import re
from typing import Optional

from ..models import Decision, HandlerResult

# File-path patterns that indicate a niche one-pager
_ONEPAGER_PATH_RX = re.compile(
    r"brain/outputs/.*(?:niche-onepager|one-pager|onepager)[^/]*\.md$",
    re.IGNORECASE,
)

# Banned pattern specs: (regex, label)
# Keep high-signal patterns only — edge cases like "Chanel" (could be a
# legitimate industry reference in a luxury-goods niche) are intentionally
# not listed. The memory file is the authoritative rule; this hook is the
# backstop for clear violations.
_BANNED_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bKay(?:'s|\u2019s)?\b", re.IGNORECASE), "Kay / Kay's"),
    (re.compile(r"\bKay Schneider\b", re.IGNORECASE), "Kay Schneider"),
    (re.compile(r"\b(?:our|the|my)\s+(?:analyst|CoS|Chief of Staff|VA)\b", re.IGNORECASE),
     "team-member reference (our/the/my analyst|CoS|Chief of Staff|VA)"),
    (re.compile(r"\bMilanese\s+(?:analyst|CoS|Chief of Staff)\b", re.IGNORECASE),
     "Milanese analyst/CoS reference"),
    (re.compile(r"\bWedgwood\b", re.IGNORECASE), "Wedgwood (Kay's personal aspirational archetype)"),
    (re.compile(r"\bAlain Wertheimer\b", re.IGNORECASE), "Alain Wertheimer (Kay's personal archetype from G&B Charter)"),
    (re.compile(r"\bJJ\b"), "JJ (team member name)"),
    (re.compile(r"\b(?:G&B|Greenwich & Barrow|Greenwich and Barrow)(?:'s|\u2019s)?\s+right[- ]to[- ]win\b", re.IGNORECASE),
     "acquirer-specific right-to-win framing (should be generic)"),
    (re.compile(r"\bKay['\u2019]s\s+(?:network|rolodex|contacts|family|analyst|hospitality)\b", re.IGNORECASE),
     "Kay's personal-network reference"),
]


def _strip_frontmatter(text: str) -> str:
    """Remove leading YAML frontmatter if present."""
    if not text.startswith("---"):
        return text
    parts = text.split("\n---", 2)
    if len(parts) >= 2:
        # parts[0] is "---", parts[1] is frontmatter content, rest is body
        # Rejoin everything after the second '---' as body
        rest = parts[1].split("---", 1)
        if len(rest) == 2:
            return rest[1]
    return text


def _strip_wikilinks(text: str) -> str:
    """Remove [[wiki-link]] tokens so tokens inside them (e.g. kay-schneider)
    do not trigger word-boundary matches on personal names."""
    return re.sub(r"\[\[[^\]]*\]\]", "", text)


def _extract_new_content(tool_name: str, tool_input: dict) -> str:
    """Return the new content a Write/Edit/MultiEdit is trying to introduce."""
    if tool_name == "Write":
        return tool_input.get("content", "") or ""
    if tool_name == "Edit":
        return tool_input.get("new_string", "") or ""
    if tool_name == "MultiEdit":
        edits = tool_input.get("edits", []) or []
        return "\n".join((e.get("new_string", "") or "") for e in edits)
    return ""


def _detect_violations(content: str) -> list[str]:
    """Return a list of labeled violations found in the content."""
    cleaned = _strip_wikilinks(_strip_frontmatter(content))
    violations: list[str] = []
    for rx, label in _BANNED_PATTERNS:
        match = rx.search(cleaned)
        if match:
            snippet = match.group(0)
            violations.append(f"{label} \u2014 matched: '{snippet}'")
    return violations


def enforce_onepager_purity(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Write|Edit|MultiEdit]: block personal/team content in one-pagers."""
    tool_name = input_data.get("tool_name", "")
    if tool_name not in ("Write", "Edit", "MultiEdit"):
        return None

    tool_input = input_data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "") or ""

    if not _ONEPAGER_PATH_RX.search(file_path):
        return None

    content = _extract_new_content(tool_name, tool_input)
    if not content.strip():
        return None

    violations = _detect_violations(content)
    if not violations:
        return None

    reason_lines = [
        "One-pager guardrail triggered \u2014 this write would insert personal "
        "or team-centric content into a niche one-pager. Niche one-pagers are "
        "pure industry analysis.",
        "",
        "Detected patterns:",
    ]
    for v in violations:
        reason_lines.append(f"  \u2022 {v}")
    reason_lines.extend([
        "",
        "Rule source: memory/feedback_artifacts_pure_industry_analysis.md",
        "Litmus: the artifact must read identically regardless of which "
        "searcher is evaluating the niche. If any sentence changes based on "
        "who the acquirer is, strip that content.",
        "",
        "Rewrite the section in generic-acquirer voice (e.g. 'factors any "
        "acquirer should evaluate' rather than 'Kay has X') and retry.",
    ])

    return HandlerResult(
        decision=Decision.BLOCK,
        reason="\n".join(reason_lines),
        exit_code=2,
    )
