#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_email_intelligence_integrity.py"
spec = importlib.util.spec_from_file_location("validate_email_intelligence_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


FRONTMATTER = """---
schema_version: 1.1.0
date: 2026-06-05
type: context
status: done
source: email-intelligence
tags: [date/2026-06-05, output/email-scan-results, source/email-intelligence, status/done, topic/email-intelligence]
---

# Email Scan Results - 2026-06-05
"""


class EmailIntelligenceValidatorTest(unittest.TestCase):
    def write_artifact(self, body: str) -> str:
        tmp = tempfile.NamedTemporaryFile("w", suffix=".md", delete=False)
        tmp.write(FRONTMATTER + "\n" + body + "\n" + ("x" * 1200))
        tmp.close()
        return tmp.name

    def test_requires_all_expected_sections(self) -> None:
        artifact = self.write_artifact(
            "\n\n".join(
                [
                    "## 1. Actionable Items Created\n\nNone.",
                    "## 2. Deal Flow Classified\n\nNone.",
                    "## 3. Draft Status\n\nNone.",
                ]
            )
        )

        failures = validator.validate_artifact(artifact, date(2026, 6, 5))

        self.assertTrue(any("missing expected section" in f for f in failures))
        self.assertTrue(any("Auto-Drafts" in f for f in failures))

    def test_complete_artifact_passes(self) -> None:
        body = "\n\n".join(
            [
                "## 1. Actionable Items Created\n\nNone.",
                "## 2. Deal Flow Classified\n\nNone.",
                "## 3. Draft Status\n\nNone.",
                "## 4. Introductions Detected\n\nNone.",
                "## 5. Niche Signals\n\nNone.",
                "## 6. In-Person Meetings Today\n\nNone.",
                "## 7. Broker BLAST Listings (per-deal extraction)\n\nNone.",
                "## 8. Auto-Drafts Created\n\nNone.",
            ]
        )
        artifact = self.write_artifact(body)

        failures = validator.validate_artifact(artifact, date(2026, 6, 5))

        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
