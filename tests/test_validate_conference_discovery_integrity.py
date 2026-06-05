#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from datetime import date
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_conference_discovery_integrity.py"
spec = importlib.util.spec_from_file_location("validate_conference_discovery_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class ConferenceDiscoveryValidatorTest(unittest.TestCase):
    def test_status_progressions_allow_expected_pipeline_moves(self) -> None:
        self.assertEqual(
            validator.classify_status_mutation("NEW", "Need to Book"),
            "allowed",
        )
        self.assertEqual(
            validator.classify_status_mutation("Need to Register", "Registered"),
            "allowed",
        )
        self.assertEqual(
            validator.classify_status_mutation("Skip", "Skipped"),
            "allowed",
        )

    def test_status_overwrite_is_hard_failure(self) -> None:
        self.assertEqual(
            validator.classify_status_mutation("Need to Book", "Skip"),
            "hard",
        )
        self.assertEqual(
            validator.classify_status_mutation("Attending", ""),
            "hard",
        )

    def test_empty_status_autofill_is_allowed(self) -> None:
        self.assertEqual(
            validator.classify_status_mutation("", "NEW"),
            "allowed",
        )

    def test_archival_legitimacy_is_strict(self) -> None:
        today = date(2026, 6, 5)

        self.assertTrue(validator._is_legitimate_archival("Skip", "8/01/26", today))
        self.assertTrue(validator._is_legitimate_archival("Attended", "8/01/26", today))
        self.assertTrue(validator._is_legitimate_archival("Attending", "6/01/26", today))
        self.assertFalse(validator._is_legitimate_archival("Attending", "6/10/26", today))
        self.assertFalse(validator._is_legitimate_archival("Need to Book", "6/01/26", today))


if __name__ == "__main__":
    unittest.main()
