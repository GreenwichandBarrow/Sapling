#!/usr/bin/env python3
"""
Stop gate for loop agents - only activates when CLAUDE_LOOP_AGENT=1.
When not in a loop context, exits cleanly.
"""
import os
import sys

# Only activate when running inside a loop agent
if os.environ.get("CLAUDE_LOOP_AGENT") != "1":
    sys.exit(0)

# TODO: Implement actual stop gate logic for loop agents
# For now, allow stop
sys.exit(0)
