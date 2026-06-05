#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_deal_aggregator_integrity.py"
spec = importlib.util.spec_from_file_location("validate_deal_aggregator_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


FRONTMATTER = """---
date: 2026-06-05
type: tracker
---

# Digest

## 1. Source Productivity
## 2. Volume Check
## 3. Proposed Additions
## 4. Proposed Retirements
## 5. Recommended Actions
"""


class DealAggregatorDigestValidatorTest(unittest.TestCase):
    def write_digest(self, body: str) -> str:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
        tmp.write(FRONTMATTER + "\n" + body + "\n" + ("x" * 240))
        tmp.close()
        return tmp.name

    def test_weekend_missing_artifacts_fail_validation(self) -> None:
        artifact = self.write_digest(
            "Missing scan artifacts in the window: 2026-05-30, 2026-05-31."
        )

        failures = validator.validate_artifact(
            artifact, validator.DIGEST_SECTIONS, date(2026, 6, 5)
        )

        self.assertTrue(any("weekend date 2026-05-30" in f for f in failures))
        self.assertTrue(any("weekend date 2026-05-31" in f for f in failures))

    def test_expected_non_run_weekends_pass_validation(self) -> None:
        artifact = self.write_digest(
            "Expected non-run days: 2026-05-30, 2026-05-31.\n"
            "Missing scheduled weekday scan artifacts: none."
        )

        failures = validator.validate_artifact(
            artifact, validator.DIGEST_SECTIONS, date(2026, 6, 5)
        )

        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
