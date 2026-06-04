"""Warn when a brain/outputs/*-templates.md snapshot is being used as a drafting source.

Why this exists:
- 2026-05-19 trace `stale-vault-snapshot-not-canonical-template` — vault
  snapshot at `brain/outputs/2026-05-04-broker-outreach-templates.md` went
  stale relative to the canonical Google Doc, and a draft sourced from
  the snapshot leaked stale language.
- Doctrine: ALWAYS pull the live canonical doc via
  `bash scripts/fetch-template-doc.sh` before drafting from a template snapshot.

This handler fires on Read of a template snapshot in brain/outputs/ and
emits a stderr warning (does NOT block — soft reminder).
"""

import re
from typing import Optional

from ..models import HandlerResult


CANONICAL_TEMPLATE_DOC_FETCH = "bash scripts/fetch-template-doc.sh"


def warn_template_snapshot_read(input_data: dict) -> Optional[HandlerResult]:
    """PreToolUse[Read]: warn that brain/outputs/*-templates.md is a stale snapshot."""
    tool_input = input_data.get("tool_input") or {}
    file_path = tool_input.get("file_path", "")

    if "brain/outputs/" not in file_path:
        return None
    if not re.search(r"templates?[^/]*\.md$", file_path, re.IGNORECASE):
        return None

    msg = (
        f"⚠️  canonical_template_guard\n"
        f"File: {file_path}\n"
        f"This is a vault SNAPSHOT of a canonical template doc that lives in Google Drive.\n"
        f"Snapshots go stale. If you are about to DRAFT an external message from this file,\n"
        f"pull the live canonical doc FIRST:\n"
        f"  {CANONICAL_TEMPLATE_DOC_FETCH}\n"
        f"See: feedback_pull_canonical_doc_live_not_snapshot, feedback_no_intermediary_drafts_outside_template.\n"
    )
    return HandlerResult(
        stderr_message=msg,
        exit_code=0,
    )
