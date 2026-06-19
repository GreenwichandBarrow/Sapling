"""Stop handler: enforce forward-only pipeline source tagging doctrine.

Kay decided on 2026-06-19 that source tagging should be a forward operating
rule, not a broad historical CRM cleanup. Pipeline-manager owns source capture;
the dashboard must not invent attribution from incomplete Attio/Salesflare data.
"""

import json
import re
from pathlib import Path
from typing import Optional

from ..models import Decision, HandlerResult

CONTEXT = re.compile(
    r"\b(source tag|source tagging|source attribution|lead source|pipeline source|"
    r"M&A plumbing|dashboard plumbing|Attio|Salesflare|pipeline-source-map)\b",
    re.IGNORECASE,
)

BAD_PATTERNS = [
    (
        re.compile(r"\bAttio\s+(?:is|should be|will be)\s+the\s+(?:sole|single|only)\s+source\s+of\s+truth\b", re.IGNORECASE),
        "Attio is not the sole source of truth for pipeline source tagging; it is the operating database to reconcile after Kay/evidence review.",
    ),
    (
        re.compile(r"\bdashboard\s+(?:can|should|will|needs to)\s+(?:infer|guess|derive|backfill)\s+(?:lead\s+)?source", re.IGNORECASE),
        "The dashboard must not infer or guess source attribution. It may only display tagged source data or Unknown / needs review.",
    ),
    (
        re.compile(r"\b(?:backfill|clean up|cleanup|reconstruct)\s+(?:all|everything|the entire|full)\s+(?:historical|history|past|CRM|Attio|Salesflare)", re.IGNORECASE),
        "Do not turn source tagging into a broad historical CRM archaeology project. Backfill only NDA-forward or investor-relevant deals.",
    ),
    (
        re.compile(r"\b(?:every|all)\s+(?:old|historical|past)\s+(?:lead|deal|record|opportunity)", re.IGNORECASE),
        "Historical source tagging is intentionally limited to meaningful deals, not every old lead or record.",
    ),
]


def pipeline_source_tagging_guard(input_data: dict) -> Optional[HandlerResult]:
    if input_data.get("stop_hook_active"):
        return None

    transcript_path = input_data.get("transcript_path", "")
    if not transcript_path:
        return None

    text = _extract_last_assistant_text(transcript_path)
    if not text or not CONTEXT.search(text):
        return None

    stripped = re.sub(r"```[\s\S]*?```", "", text)
    stripped = re.sub(r"`[^`]*`", "", stripped)

    for pattern, explanation in BAD_PATTERNS:
        match = pattern.search(stripped)
        if not match:
            continue
        reason = (
            "Rule violation (pipeline-source-tagging-guard): "
            f"{explanation} Offending phrase: '{match.group(0)}'. "
            "Use the approved doctrine: source tagging is forward operating hygiene; "
            "new real opportunities get one fixed source category plus source detail; "
            "Good Morning asks only when a meaningful active deal is missing source; "
            "historical backfill is limited to NDA-forward / investor-relevant deals; "
            "dashboard output must show mapped source or Unknown / needs review."
        )
        return HandlerResult(decision=Decision.BLOCK, reason=reason)

    return None


def _extract_last_assistant_text(transcript_path: str) -> str:
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
