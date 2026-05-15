#!/usr/bin/env python3
"""PreToolUse event router: validation gates and context injection."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from router.framework import dispatch
from router.models import HandlerConfig
from router.handlers.vault import stats_protection, validate_vault_schema
from router.handlers.skills import inject_skill_context
from router.handlers.gmail import block_gmail_send
from router.handlers.weekly_tracker_validation import validate_weekly_tracker_before_slack
from router.handlers.onepager_guardrail import enforce_onepager_purity
from router.handlers.no_revenue_in_outreach import no_revenue_in_outreach
from router.handlers.secret_file_guard import block_secret_file_reads
from router.handlers.gog_sheets_delimiter_guard import block_gog_sheets_delimiter_writes
from router.handlers.skill_frontmatter_guard import check_skill_frontmatter

HANDLERS = [
    HandlerConfig(
        fn=block_secret_file_reads,
        matcher=r"^Bash$",
        name="secret-file-guard",
    ),
    HandlerConfig(
        fn=block_gog_sheets_delimiter_writes,
        matcher=r"^Bash$",
        name="gog-sheets-delimiter-guard",
    ),
    HandlerConfig(
        fn=no_revenue_in_outreach,
        matcher=r"^Bash$",
        name="no-revenue-in-outreach",
    ),
    HandlerConfig(
        fn=stats_protection,
        matcher=r"Write|Edit",
        name="stats-protection",
    ),
    HandlerConfig(
        fn=validate_vault_schema,
        matcher=r"^Write$",
        name="validate-vault-schema",
    ),
    HandlerConfig(
        fn=enforce_onepager_purity,
        matcher=r"Write|Edit|MultiEdit",
        name="onepager-guardrail",
    ),
    HandlerConfig(
        fn=check_skill_frontmatter,
        matcher=r"Write|Edit|MultiEdit",
        name="skill-frontmatter-guard",
    ),
    HandlerConfig(
        fn=inject_skill_context,
        matcher=r"^Skill$",
        name="inject-skill-context",
    ),
    HandlerConfig(
        fn=block_gmail_send,
        matcher=r"^Bash$",
        name="block-gmail-send",
    ),
    HandlerConfig(
        fn=validate_weekly_tracker_before_slack,
        matcher=r"^Bash$",
        name="weekly-tracker-validation",
    ),
]

if __name__ == "__main__":
    dispatch(HANDLERS, "PreToolUse")
