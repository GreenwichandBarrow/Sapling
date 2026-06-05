#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_jj_operations_integrity.py"
spec = importlib.util.spec_from_file_location("validate_jj_operations_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class JJOperationsValidatorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.expected_tabs = [
            "Call Log 6.08.26",
            "Call Log 6.09.26",
            "Call Log 6.10.26",
            "Call Log 6.11.26",
            "Call Log 6.12.26",
        ]

    def test_complete_tabs_with_owner_names_pass(self) -> None:
        values = {
            (tab, "K"): ["Owner One", "Owner Two"] for tab in self.expected_tabs
        }
        values.update({(tab, "B"): ["Company One", "Company Two"] for tab in self.expected_tabs})

        failures = validator.validate_call_log_tabs(
            "Premium Pest Management",
            self.expected_tabs,
            self.expected_tabs,
            lambda tab, col: values[(tab, col)],
        )

        self.assertEqual(failures, [])

    def test_missing_tab_fails_before_column_checks(self) -> None:
        failures = validator.validate_call_log_tabs(
            "Premium Pest Management",
            self.expected_tabs[:-1],
            self.expected_tabs,
            lambda tab, col: [],
        )

        self.assertEqual(
            failures,
            ["[Premium Pest Management] missing Call Log tabs: ['Call Log 6.12.26']"],
        )

    def test_company_without_owner_name_fails(self) -> None:
        values = {}
        for tab in self.expected_tabs:
            values[(tab, "K")] = ["Owner One", ""]
            values[(tab, "B")] = ["Company One", "Company Two"]

        failures = validator.validate_call_log_tabs(
            "Premium Pest Management",
            self.expected_tabs,
            self.expected_tabs,
            lambda tab, col: values[(tab, col)],
        )

        self.assertTrue(any("Owner Name blank" in f for f in failures))
        self.assertTrue(any("rows [3]" in f for f in failures))

    def test_zero_owner_names_fails(self) -> None:
        values = {
            (tab, "K"): ["", ""] for tab in self.expected_tabs
        }
        values.update({(tab, "B"): ["Company One", "Company Two"] for tab in self.expected_tabs})

        failures = validator.validate_call_log_tabs(
            "Premium Pest Management",
            self.expected_tabs,
            self.expected_tabs,
            lambda tab, col: values[(tab, col)],
        )

        self.assertEqual(len(failures), len(self.expected_tabs))
        self.assertTrue(all("zero rows with Col K" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
