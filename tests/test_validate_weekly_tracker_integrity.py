#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_weekly_tracker_integrity.py"
spec = importlib.util.spec_from_file_location("validate_weekly_tracker_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


FRONTMATTER = """---
schema_version: "2.0.0"
date: 2026-05-29
type: tracker
tags:
  - topic/weekly-tracker
---

# Weekly Activity Tracker
"""


class WeeklyTrackerValidatorTest(unittest.TestCase):
    def write_snapshot(self, body: str) -> str:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
        tmp.write(FRONTMATTER + "\n" + body + "\n" + ("x" * 1200))
        tmp.close()
        return tmp.name

    def test_requires_required_sections(self) -> None:
        snapshot = self.write_snapshot("## Key Metrics (vs Goal)\n\nOnly one section.")

        failures = validator.validate_vault_snapshot(snapshot, date(2026, 5, 29))

        self.assertTrue(any("missing required section" in f for f in failures))
        self.assertTrue(any("## Signal Quality" in f for f in failures))

    def test_complete_snapshot_passes(self) -> None:
        body = "\n\n".join(
            [
                "## Key Metrics (vs Goal)\n\n| Metric | This Week |",
                "## System Throughput\n\n| Metric | This Week |",
                "## Signal Quality\n\n| Metric | This Week |",
                "## Pipeline Health\n\n| Metric | This Week |",
                "## Channel Performance\n\n| Channel | Sent |",
                "## Flags\n\nNone.",
            ]
        )
        snapshot = self.write_snapshot(body)

        failures = validator.validate_vault_snapshot(snapshot, date(2026, 5, 29))

        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
