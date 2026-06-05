#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_phase2_integrity.py"
spec = importlib.util.spec_from_file_location("validate_phase2_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


class Phase2IntegrityValidatorTest(unittest.TestCase):
    def test_formats_success_result(self) -> None:
        code, summary = validator.format_hook_result(
            "Premium Pest Management",
            0,
            "pool ok\n",
            "",
        )

        self.assertEqual(code, 0)
        self.assertIn("[Premium Pest Management] PASS", summary)
        self.assertIn("pool ok", summary)

    def test_formats_failure_result_with_stderr(self) -> None:
        code, summary = validator.format_hook_result(
            "Premium Pest Management",
            1,
            "",
            "missing enrichment",
        )

        self.assertEqual(code, 1)
        self.assertIn("FAIL (exit 1)", summary)
        self.assertIn("missing enrichment", summary)

    def test_missing_pool_artifact_returns_error_without_hook(self) -> None:
        missing = Path(tempfile.gettempdir()) / "missing-jj-week-pool-for-test.md"
        if missing.exists():
            missing.unlink()

        code, summary = validator._run_check("Premium Pest Management", "sheet_id", missing)

        self.assertEqual(code, 2)
        self.assertIn("pool artifact missing", summary)


if __name__ == "__main__":
    unittest.main()
