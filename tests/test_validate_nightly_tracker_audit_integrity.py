#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_nightly_tracker_audit_integrity.py"
spec = importlib.util.spec_from_file_location("validate_nightly_tracker_audit_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class NightlyTrackerAuditValidatorTest(unittest.TestCase):
    def test_clean_rows_pass(self) -> None:
        rows = [
            ["1", "Pest Control", "Active"],
            ["2", "Art Storage", "Active"],
            ["", "", ""],
        ]

        failures, data_count = validator.analyze_weekly_review_rows(rows)

        self.assertEqual(failures, [])
        self.assertEqual(data_count, 2)

    def test_flags_tabled_and_killed_rows(self) -> None:
        rows = [
            ["1", "Pest Control", "Tabled"],
            ["2", "Art Storage", "Killed"],
        ]

        failures, _ = validator.analyze_weekly_review_rows(rows)

        self.assertTrue(any("Tabled/Killed rows" in f for f in failures))
        self.assertTrue(any("Pest Control" in f for f in failures))
        self.assertTrue(any("Art Storage" in f for f in failures))

    def test_flags_blank_gap_and_rank_drift(self) -> None:
        rows = [
            ["1", "Pest Control", "Active"],
            ["", "", ""],
            ["4", "Art Storage", "Active"],
        ]

        failures, _ = validator.analyze_weekly_review_rows(rows)

        self.assertTrue(any("Blank gaps" in f for f in failures))
        self.assertTrue(any("Rank column not sequential" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
