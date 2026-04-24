"""PostToolUse handler: block Write/Edit to deliverable paths when the content
contains "Kay" as a distinct token.

Kay's rule (memory/feedback_no_name_in_deliverables.md): never use "Kay" in
one-pagers, scorecards, call briefs, or similar deliverables. Use "G&B" or
"Greenwich & Barrow" instead. These documents are shared with analysts and
investors; personal-name references break the brand.

Deliverable file-path patterns covered:
- brain/outputs/* (markdown deliverables)
- brain/briefs/* (call-prep briefs)
- brain/library/client-facing/* (client-facing library)
- /tmp/*-onepager.md, /tmp/*-scorecard.md, /tmp/*-brief.md (staging files)

pptx/xlsx files are not scanned by this hook (would need unzipping); those
remain governed by the reference docs + sub-agent prompts.
"""

import re
from pathlib import Path
from typing import Optional

from ..models import Decision, HandlerResult

# Match "Kay" as a distinct token — word boundary on both sides so "Kayak" and
# "Kayla" don't trigger. Catches "Kay", "Kay's", "Kay,", "Kay." and friends.
KAY_TOKEN = re.compile(r"\bKay('?s)?\b")

DELIVERABLE_PATTERNS = [
    re.compile(r"/brain/outputs/"),
    re.compile(r"/brain/briefs/"),
    re.compile(r"/brain/library/client-facing/"),
    re.compile(r"/tmp/.*-(onepager|scorecard|brief|one-pager|one_pager)\.md$"),
]


def no_kay_in_deliverables(input_data: dict) -> Optional[HandlerResult]:
    tool_name = input_data.get("tool_name", "")
    if tool_name not in ("Write", "Edit"):
        return None

    tool_input = input_data.get("tool_input", {}) or {}
    file_path = tool_input.get("file_path", "")
    if not file_path:
        return None

    if not _is_deliverable(file_path):
        return None

    # Only scan text files
    if not file_path.endswith((".md", ".txt", ".markdown")):
        return None

    # Get the content that was written/edited
    content = _extract_content(tool_input)
    if not content:
        return None

    # Strip frontmatter (names in tags/people fields are OK — they're metadata)
    body = _strip_frontmatter(content)

    # Also exempt wiki-links like [[entities/kay-schneider]] — those are
    # structural references, not prose
    body_no_links = re.sub(r"\[\[[^\]]*\]\]", "", body)

    match = KAY_TOKEN.search(body_no_links)
    if not match:
        return None

    # Pull ~60 chars of surrounding context
    idx = body_no_links.find(match.group(0))
    start = max(0, idx - 40)
    end = min(len(body_no_links), idx + len(match.group(0)) + 40)
    context = body_no_links[start:end].replace("\n", " ").strip()

    reason = (
        f"Rule violation (no-kay-in-deliverables): '{match.group(0)}' appears in "
        f"'{file_path}' at '…{context}…'. Per memory/feedback_no_name_in_deliverables, "
        "deliverables (one-pagers, scorecards, call briefs, client-facing docs) "
        "must use 'G&B' or 'Greenwich & Barrow' instead of Kay's first name. "
        "These are shared with analysts and investors; personal-name references "
        "break the brand. Rewrite and resubmit. (Wiki-links, tags, and "
        "frontmatter-people fields are not flagged — only prose.)"
    )
    return HandlerResult(decision=Decision.BLOCK, reason=reason)


def _is_deliverable(file_path: str) -> bool:
    return any(p.search(file_path) for p in DELIVERABLE_PATTERNS)


def _extract_content(tool_input: dict) -> str:
    """For Write tool, return 'content'. For Edit, return the 'new_string' (the
    text being inserted, which is what we care about validating)."""
    if "content" in tool_input:
        return tool_input.get("content", "") or ""
    return tool_input.get("new_string", "") or ""


def _strip_frontmatter(content: str) -> str:
    """Remove a leading YAML frontmatter block so tags / people fields don't
    trigger on legitimate metadata mentions."""
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end > 0:
            return content[end + 5 :]
    return content
