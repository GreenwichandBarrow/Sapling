#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "scan_launchd_failures.py"
spec = importlib.util.spec_from_file_location("scan_launchd_failures", MODULE_PATH)
scanner = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(scanner)


class LaunchdFailureScannerTest(unittest.TestCase):
    def write_log(self, directory: Path, name: str, text: str) -> Path:
        path = directory / name
        path.write_text(text)
        return path

    def test_codex_exec_failure_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_log(
                Path(tmp),
                "email-intelligence-2026-06-05-0500.log",
                "Codex command: codex exec < prompt\nFAILED: codex exec exited 1\n",
            )

            record = scanner.parse_log(path)

        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual(record["exit_code"], 1)
        self.assertEqual(record["error_signature"], "FAILED: codex exec exited 1")

    def test_codex_post_run_failure_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_log(
                Path(tmp),
                "weekly-tracker-2026-06-05-0500.log",
                "Post-run check: python3 scripts/validate.py\nFAILED: post-run check exited 3\n",
            )

            record = scanner.parse_log(path)

        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual(record["exit_code"], 3)
        self.assertEqual(record["error_signature"], "FAILED: post-run check exited 3")

    def test_codex_success_is_not_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_log(
                Path(tmp),
                "relationship-manager-2026-06-05-0500.log",
                "Codex command: codex exec < prompt\nCompleted: Fri Jun  5 05:00:00 UTC 2026\n",
            )

            record = scanner.parse_log(path)

        self.assertIsNone(record)

    def test_legacy_claude_failure_remains_supported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_log(
                Path(tmp),
                "launchd-debugger-2026-06-05-0500.log",
                "Finished claude run: Fri Jun 5 05:00:00 UTC 2026, exit: 2 (attempts: 1)\n",
            )

            record = scanner.parse_log(path)

        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual(record["exit_code"], 2)
        self.assertIn("exit 2", record["error_signature"])

    def test_latest_success_resolves_older_failure_for_same_job(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            log_dir = Path(tmp)
            older = self.write_log(
                log_dir,
                "email-intelligence-2026-06-05-0400.log",
                "FAILED: codex exec exited 1\n",
            )
            newer = self.write_log(
                log_dir,
                "email-intelligence-2026-06-05-0500.log",
                "Completed: Fri Jun  5 05:00:00 UTC 2026\n",
            )
            older_time = 1_780_000_000
            newer_time = older_time + 60
            older.touch()
            newer.touch()
            import os

            os.utime(older, (older_time, older_time))
            os.utime(newer, (newer_time, newer_time))

            previous_log_dir = scanner.LOG_DIR
            scanner.LOG_DIR = log_dir
            try:
                failures = scanner.scan(window_hours=24 * 365)
            finally:
                scanner.LOG_DIR = previous_log_dir

        self.assertEqual(failures, [])

    def test_stop_marker_without_runner_failure_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = self.write_log(
                Path(tmp),
                "nightly-tracker-audit-2026-06-05-0500.log",
                "NIGHTLY-TRACKER-AUDIT STOP: missing REQUIRED sections\nCompleted: later\n",
            )

            record = scanner.parse_log(path)

        self.assertIsNotNone(record)
        assert record is not None
        self.assertEqual(record["exit_code"], -1)
        self.assertEqual(
            record["error_signature"],
            "NIGHTLY-TRACKER-AUDIT STOP: missing REQUIRED sections",
        )


if __name__ == "__main__":
    unittest.main()
