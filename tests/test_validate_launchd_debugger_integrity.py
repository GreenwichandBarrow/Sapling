#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_launchd_debugger_integrity.py"
spec = importlib.util.spec_from_file_location("validate_launchd_debugger_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def clean_artifact() -> dict:
    return {
        "date": "2026-06-05",
        "scan_started_at": "2026-06-05T06:00:00Z",
        "scan_finished_at": "2026-06-05T06:02:00Z",
        "failures_detected": 1,
        "fixes_attempted": 1,
        "fixes_succeeded": 1,
        "surfaces_to_slack": 0,
        "runtime_seconds": 120,
        "results": [{"job": "email-intelligence", "cause": "stale", "action": "FIX"}],
    }


class LaunchdDebuggerValidatorTest(unittest.TestCase):
    def test_clean_artifact_passes(self) -> None:
        failures, stats = validator.validate_artifact_data(clean_artifact(), "2026-06-05")

        self.assertEqual(failures, [])
        self.assertEqual(stats["declared"], 1)

    def test_requires_result_shape_and_valid_action(self) -> None:
        data = clean_artifact()
        data["results"] = [{"job": "email-intelligence", "action": "IGNORE"}]

        failures, _ = validator.validate_artifact_data(data, "2026-06-05")

        self.assertTrue(any("missing fields" in f for f in failures))
        self.assertTrue(any("not in" in f for f in failures))

    def test_flags_orphan_failure_accounting(self) -> None:
        data = clean_artifact()
        data["fixes_succeeded"] = 0

        failures, _ = validator.validate_artifact_data(data, "2026-06-05")

        self.assertTrue(any("orphan failures" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
