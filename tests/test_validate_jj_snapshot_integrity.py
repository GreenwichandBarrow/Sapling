#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_jj_snapshot_integrity.py"
spec = importlib.util.spec_from_file_location("validate_jj_snapshot_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def valid_snapshot() -> dict:
    return {
        "fetched_at": "2026-06-05T12:00:00Z",
        "niches_scanned": ["Premium Pest Management"],
        "per_niche_lifetime": {"Premium Pest Management": 123},
        "dials_today": 0,
        "dials_lifetime": 123,
        "by_day": {"2026-06-05": 0},
        "weekly_buckets": [{"week": "2026-06-01", "dials": 10}],
    }


class JJSnapshotValidatorTest(unittest.TestCase):
    def test_valid_snapshot_passes(self) -> None:
        failures = validator.validate_snapshot_data(valid_snapshot())

        self.assertEqual(failures, [])

    def test_flags_false_zero_lifetime(self) -> None:
        data = valid_snapshot()
        data["dials_lifetime"] = 0

        failures = validator.validate_snapshot_data(data)

        self.assertTrue(any("FALSE ZERO" in f for f in failures))

    def test_requires_niches_and_weekly_buckets(self) -> None:
        data = valid_snapshot()
        data["niches_scanned"] = []
        data["weekly_buckets"] = []

        failures = validator.validate_snapshot_data(data)

        self.assertTrue(any("niches_scanned" in f for f in failures))
        self.assertTrue(any("weekly_buckets" in f for f in failures))

    def test_rejects_bool_lifetime(self) -> None:
        data = valid_snapshot()
        data["dials_lifetime"] = True

        failures = validator.validate_snapshot_data(data)

        self.assertTrue(any("expected a positive int" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
