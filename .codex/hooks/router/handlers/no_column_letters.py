"""Stop handler: block responses that reference spreadsheet cells by column letter.

Kay's rule (memory/feedback_no_column_references_in_docs.md): never say "Col T",
"Column A", "col U", etc. Use the column header NAME + a row identifier to triangulate —
e.g. "JJ: 1st Call Date on row 4" or "the 1st Call Date field for Acme Pest".

This hook reads the last assistant message from the transcript, strips code fences
(legit sheet ranges in shell commands are allowed), and blocks if a column-letter
reference survives outside code.
"""

import json
import re
from pathlib import Path
from typing import Optional

from ..models import Decision, HandlerResult

# Matches: "Col T", "col T", "COL T", "Column A", "columns T", "Cols T", "Col.T".
# The prefix is case-insensitive but the bounded letter is still [A-Z] so lowercase
# "column a" doesn't trigger on sentence-case prose where 'a' is just an article.
# Requires the letter(s) to be bounded (not followed by more word chars), so
# "Col. Mustard" and "Column name" do NOT match.
PATTERN = re.compile(r"\b(?:[Cc]ol|COL)(?:umn|UMN)?s?\s*\.?\s*[A-Z]{1,2}\b")


def no_column_letters(input_data: dict) -> Optional[HandlerResult]:
    # Avoid re-block loop: if we've already blocked once, let Claude stop.
    if input_data.get("stop_hook_active"):
        return None

    transcript_path = input_data.get("transcript_path", "")
    if not transcript_path:
        return None

    text = _extract_last_assistant_text(transcript_path)
    if not text:
        return None

    # Strip fenced code blocks and inline backticks — legit sheet-range args in
    # shell commands are allowed (e.g. `gog sheets read "Tab!T2:W45"`).
    stripped = re.sub(r"```[\s\S]*?```", "", text)
    stripped = re.sub(r"`[^`]*`", "", stripped)

    match = PATTERN.search(stripped)
    if not match:
        return None

    snippet = match.group(0)
    # Pull ~60 chars of surrounding context for the reason.
    idx = stripped.find(snippet)
    start = max(0, idx - 40)
    end = min(len(stripped), idx + len(snippet) + 40)
    context = stripped[start:end].replace("\n", " ")

    reason = (
        f"Rule violation (no-column-letters): you wrote '{snippet}' "
        f"in context '…{context}…'. "
        "Never reference spreadsheet cells by column letter in conversation. "
        "Use the column header NAME plus a row identifier to triangulate — "
        "e.g. 'JJ: 1st Call Date on row 4' or 'the 1st Call Date field for Acme Pest'. "
        "Rewrite the response (or the affected passage) and try again. "
        "Code-block sheet ranges like `Tab!T2:W45` inside backticks are allowed; "
        "prose-style column-letter references are not. "
        "See memory/feedback_no_column_references_in_docs.md."
    )

    return HandlerResult(decision=Decision.BLOCK, reason=reason)


def _extract_last_assistant_text(transcript_path: str) -> str:
    """Read the JSONL transcript and return the text of the most recent
    assistant message (concatenated across any text blocks)."""
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
        parts = []
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                parts.append(block.get("text", ""))
            elif isinstance(block, str):
                parts.append(block)
        if parts:
            return "\n".join(parts)

    return ""
