#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_niche_intelligence_integrity.py"
spec = importlib.util.spec_from_file_location("validate_niche_intelligence_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def valid_sidecar() -> dict:
    return {
        "run_date": "2026-06-02",
        "run_mode": "tuesday",
        "niches_evaluated": 3,
        "niches_identified": 1,
        "one_pagers_written": 1,
        "scorecards_written": 1,
        "tracker_updated": True,
        "runtime_seconds": 123.4,
    }


class NicheIntelligenceValidatorTest(unittest.TestCase):
    def test_valid_sidecar_passes(self) -> None:
        failures = validator.validate_sidecar_data(valid_sidecar(), date(2026, 6, 2))

        self.assertEqual(failures, [])

    def test_zero_finding_requires_reason(self) -> None:
        data = valid_sidecar()
        data["niches_identified"] = 0

        failures = validator.validate_sidecar_data(data, date(2026, 6, 2))

        self.assertTrue(any("zero_finding_reason" in f for f in failures))

    def test_report_requires_frontmatter_contract(self) -> None:
        content = """---
date: 2026-06-01
type: note
---

# Niche Intelligence
""" + ("x" * 700)

        failures = validator.validate_report_content(
            content,
            date(2026, 6, 2),
            len(content.encode("utf-8")),
            "report.md",
        )

        self.assertTrue(any("date does not match" in f for f in failures))
        self.assertTrue(any("type: output" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
