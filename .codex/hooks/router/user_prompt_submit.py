#!/usr/bin/env python3
"""UserPromptSubmit event router: handoff, skills, and memory."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from router.framework import dispatch
from router.models import HandlerConfig
from router.handlers.handoff import detect_save_state, detect_picking_back_up
from router.handlers.skills import skill_router
from router.handlers.memory import memory_recall

HANDLERS = [
    # Handoff handlers run first — they suppress_further when matched
    HandlerConfig(fn=detect_save_state, name="save-state"),
    HandlerConfig(fn=detect_picking_back_up, name="picking-back-up"),
    HandlerConfig(fn=skill_router, name="skill-router"),
    HandlerConfig(fn=memory_recall, name="memory-recall"),
]

if __name__ == "__main__":
    dispatch(HANDLERS, "UserPromptSubmit")
