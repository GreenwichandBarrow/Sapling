#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_attio_snapshot_integrity.py"
spec = importlib.util.spec_from_file_location("validate_attio_snapshot_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def valid_snapshot() -> dict:
    return {
        "fetched_at": "2026-06-05T12:00:00Z",
        "list_id": "list_123",
        "stages": [
            {"title": "Identified", "is_terminal": False},
            {"title": "Closed / Not Proceeding", "is_terminal": True},
        ],
        "deals": [
            {"record_id": "rec_1", "company": "Example Co", "stage": "Identified"},
        ],
        "closed_count": 4,
    }


class AttioSnapshotValidatorTest(unittest.TestCase):
    def test_valid_snapshot_passes(self) -> None:
        failures = validator.validate_snapshot_data(valid_snapshot())

        self.assertEqual(failures, [])

    def test_deal_stage_must_match_stage_titles(self) -> None:
        data = valid_snapshot()
        data["deals"][0]["stage"] = "Unknown"

        failures = validator.validate_snapshot_data(data)

        self.assertTrue(any("is not in stage titles" in f for f in failures))

    def test_rejects_blank_stage_title_and_bad_closed_count(self) -> None:
        data = valid_snapshot()
        data["stages"][0]["title"] = ""
        data["closed_count"] = True

        failures = validator.validate_snapshot_data(data)

        self.assertTrue(any("title" in f for f in failures))
        self.assertTrue(any("closed_count" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
