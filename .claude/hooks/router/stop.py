#!/usr/bin/env python3
"""Stop event router: orchestrator gate + git auto-commit."""

import os
import sys

# Ensure the router package is importable
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from router.framework import dispatch
from router.models import HandlerConfig
from router.handlers.orchestrator import orchestrator_stop_gate
from router.handlers.git import git_auto_commit_stop

HANDLERS = [
    HandlerConfig(fn=orchestrator_stop_gate, name="orchestrator-stop-gate"),
    HandlerConfig(fn=git_auto_commit_stop, name="git-auto-commit-stop"),
]

if __name__ == "__main__":
    dispatch(HANDLERS, "Stop")
