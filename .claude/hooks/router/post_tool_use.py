#!/usr/bin/env python3
"""PostToolUse event router: secret redaction, schema migration, chatroom, calibration."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from router.framework import dispatch
from router.models import HandlerConfig
from router.handlers.redact_secrets import redact_bash_secrets
from router.handlers.schema_migration import schema_update_prompt
from router.handlers.chatroom import chatroom_state_sync
from router.handlers.calibration import calibration_stats_updater
from router.handlers.no_kay_in_deliverables import no_kay_in_deliverables

HANDLERS = [
    HandlerConfig(
        fn=no_kay_in_deliverables,
        matcher=r"Write|Edit",
        name="no-kay-in-deliverables",
    ),
    HandlerConfig(
        fn=redact_bash_secrets,
        matcher=r"^Bash$",
        name="redact-secrets",
    ),
    HandlerConfig(
        fn=schema_update_prompt,
        matcher=r"Write|Edit",
        name="schema-update-prompt",
    ),
    HandlerConfig(
        fn=chatroom_state_sync,
        matcher=r"Write|Edit",
        name="chatroom-state-sync",
    ),
    HandlerConfig(
        fn=calibration_stats_updater,
        matcher=r"^Write$",
        name="calibration-stats-updater",
    ),
]

if __name__ == "__main__":
    dispatch(HANDLERS, "PostToolUse")
