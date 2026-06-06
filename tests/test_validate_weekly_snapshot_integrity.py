#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_weekly_snapshot_integrity.py"
spec = importlib.util.spec_from_file_location("validate_weekly_snapshot_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


FRONTMATTER = """---
schema_version: "2.0.0"
date: 2026-06-05
type: tracker
tags:
  - topic/weekly-tracker
  - source/dashboard-snapshot
---

# Weekly Dashboard Snapshot
"""


VALID_BODY = """
## Key Metrics

| Metric | This Week | Prior Week | Delta |
|--------|-----------|------------|-------|
| Outreach sends (SENT verb-tag bullets) | 12 | 10 | +2 |

## Channel Performance

| Channel | Sent | Reply | Positive | -> NDA | Reply rate |
|---------|------|-------|----------|-------|-----------|
| Email | 10 | 2 | 1 | 0 | 20% |

## Per-Niche Breakdown

| Niche | Sent |
| --- | ---: |
| Operators | 4 |

## Data Sources

**Source:** `dashboard.snapshot.snapshot_weekly()` - single source of truth for metric definitions.

- Attio snapshot fresh: True
- Operations snapshot fetched: 2026-06-05T22:01:09Z
- Pipeline total deal count: 151
- Prior week tracker present: True

## Narrative (optional manual additions)

No manual additions.
"""


class WeeklySnapshotValidatorTest(unittest.TestCase):
    def write_snapshot(self, frontmatter: str, body: str) -> str:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
        tmp.write(frontmatter + "\n" + body + "\n" + ("x" * 1200))
        tmp.close()
        return tmp.name

    def test_complete_dashboard_snapshot_passes(self) -> None:
        snapshot = self.write_snapshot(FRONTMATTER, VALID_BODY)

        failures = validator.validate_snapshot(snapshot, date(2026, 6, 5))

        self.assertEqual(failures, [])

    def test_requires_dashboard_source_tag(self) -> None:
        frontmatter = FRONTMATTER.replace("  - source/dashboard-snapshot\n", "")
        snapshot = self.write_snapshot(frontmatter, VALID_BODY)

        failures = validator.validate_snapshot(snapshot, date(2026, 6, 5))

        self.assertTrue(any("source/dashboard-snapshot" in failure for failure in failures))

    def test_requires_direct_snapshot_sections(self) -> None:
        snapshot = self.write_snapshot(
            FRONTMATTER,
            "## Key Metrics\n\n| Metric | This Week | Prior Week | Delta |",
        )

        failures = validator.validate_snapshot(snapshot, date(2026, 6, 5))

        self.assertTrue(any("missing required section" in failure for failure in failures))
        self.assertTrue(any("## Channel Performance" in failure for failure in failures))


if __name__ == "__main__":
    unittest.main()
