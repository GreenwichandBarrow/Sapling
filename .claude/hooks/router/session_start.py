#!/usr/bin/env python3
"""SessionStart event router: init, git sync, dedup cleanup, continuation."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from router.framework import dispatch
from router.models import HandlerConfig
from router.handlers.session import session_init, calendar_check, dedup_cleanup
from router.handlers.git import git_sync_startup
from router.handlers.continuation import load_continuation_state
from router.handlers.pipeline import pipeline_pulse

HANDLERS = [
    HandlerConfig(fn=session_init, name="session-init"),
    HandlerConfig(fn=calendar_check, name="calendar-check"),
    HandlerConfig(fn=git_sync_startup, name="git-sync-startup"),
    HandlerConfig(fn=dedup_cleanup, matcher="startup", name="dedup-cleanup"),
    HandlerConfig(fn=load_continuation_state, matcher="compact", name="load-continuation"),
    HandlerConfig(fn=pipeline_pulse, matcher="startup", name="pipeline-pulse"),
]

if __name__ == "__main__":
    dispatch(HANDLERS, "SessionStart")
