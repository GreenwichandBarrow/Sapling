#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_apollo_credits_integrity.py"
spec = importlib.util.spec_from_file_location("validate_apollo_credits_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def valid_snapshot() -> dict:
    return {
        "fetched_at": "2026-06-05T15:00:45-0400",
        "minute_remaining": 999,
        "raw_response": {
            "enrich_status": 200,
            "rate_limit_headers": {
                "x-rate-limit-minute": "1000",
                "x-minute-usage": "1",
            },
        },
    }


class ApolloCreditsValidatorTest(unittest.TestCase):
    def test_valid_snapshot_passes(self) -> None:
        failures = validator.validate_snapshot_data(valid_snapshot())

        self.assertEqual(failures, [])

    def test_rejected_enrich_call_fails(self) -> None:
        data = valid_snapshot()
        data["raw_response"]["enrich_status"] = 401

        failures = validator.validate_snapshot_data(data)

        self.assertTrue(any("expected 200" in f for f in failures))

    def test_missing_rate_limit_headers_fail(self) -> None:
        data = valid_snapshot()
        del data["raw_response"]["rate_limit_headers"]["x-minute-usage"]

        failures = validator.validate_snapshot_data(data)

        self.assertEqual(
            failures,
            ["rate_limit_headers missing required keys: ['x-minute-usage']"],
        )

    def test_raw_response_must_be_object(self) -> None:
        data = valid_snapshot()
        data["raw_response"] = "bad"

        failures = validator.validate_snapshot_data(data)

        self.assertEqual(failures, ["`raw_response` is str, expected dict"])


if __name__ == "__main__":
    unittest.main()
