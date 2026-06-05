#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_post_call_analyzer_integrity.py"
spec = importlib.util.spec_from_file_location("validate_post_call_analyzer_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class PostCallAnalyzerValidatorTest(unittest.TestCase):
    def test_processed_ledger_accepts_complete_entries(self) -> None:
        ledger = {
            "processed": [
                {
                    "id": "not_123",
                    "doc_url": "https://docs.google.com/document/d/example/edit",
                    "vault_call_note": "brain/calls/2026-06-05-example.md",
                },
                {"id": "not_456", "attio_failed": True},
            ],
            "last_updated": "2026-06-05T12:00:00Z",
        }

        failures = validator.validate_processed_ledger(ledger)

        self.assertEqual(failures, [])

    def test_processed_ledger_flags_entries_without_artifact_or_failure(self) -> None:
        ledger = {"processed": [{"id": "not_empty"}]}

        failures = validator.validate_processed_ledger(ledger)

        self.assertEqual(
            failures,
            ["processed entry not_empty has no artifact + no failure marker"],
        )

    def test_processed_ledger_rejects_bad_shape(self) -> None:
        failures = validator.validate_processed_ledger({"processed": "not-a-list"})

        self.assertEqual(
            failures,
            ["processed.json 'processed' field is str, expected list"],
        )


if __name__ == "__main__":
    unittest.main()
