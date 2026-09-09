"""Exercise the live shell detector with isolated state and no network access."""
from __future__ import annotations

import json
from pathlib import Path
import subprocess
import tempfile
import unittest


SCRIPT = Path(__file__).resolve().parents[1] / "scripts/post_call_analyzer_poll.codex.sh"


class PostCallPollTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.home = self.root / "home"
        self.bin = self.home / ".local/bin"
        self.bin.mkdir(parents=True)
        self.tracker = self.root / "brain/trackers/post-call-analyzer"
        self.queue = self.tracker / "queue"
        self.queue.mkdir(parents=True)
        self.checkpoint = self.home / ".cache/post-call-analyzer/last-checkpoint.txt"
        self.checkpoint.parent.mkdir(parents=True)
        self.checkpoint.write_text("2026-09-08T17:00:46Z\n")
        self.before = self.checkpoint.read_text()
        self.payload = self.root / "notes.json"
        self.payload.write_text("[]")
        self.ledger = self.tracker / "processed.json"
        self.ledger.write_text('{"processed": []}')
        self.marker = self.root / "launches"
        self.stub("granola-api", 'cat "$TEST_PAYLOAD"; exit "${TEST_API_RC:-0}"')
        # Intercept detachment before any real worker can start.
        self.stub("setsid", 'printf "%s\\n" "$*" >> "$TEST_LAUNCHES"')
        self.stub("op", "exit 1")
        self.stub("curl", 'echo "unexpected notification" >&2; exit 99')
        self.env = {
            "HOME": str(self.home), "PATH": f"{self.bin}:/usr/bin:/bin",
            "CODEX_PROJECT_DIR": str(self.root),
            "TEST_PAYLOAD": str(self.payload), "TEST_LAUNCHES": str(self.marker),
        }

    def stub(self, name, body):
        path = self.bin / name
        path.write_text("#!/bin/bash\n" + body + "\n")
        path.chmod(0o755)

    def run_poll(self):
        result = subprocess.run(
            ["/bin/bash", str(SCRIPT)], env=self.env,
            capture_output=True, text=True, timeout=10,
        )
        # Detached mock is short-lived; wait for its observable marker when launched.
        if "headless run launched" in result.stdout:
            import time
            for _ in range(100):
                if self.marker.exists():
                    break
                time.sleep(0.01)
        return result

    def test_empty_poll_retries_existing_queue_without_overwriting(self):
        entry = self.queue / "not_retry.json"
        entry.write_text('{"id":"not_retry","queued_at":"original"}')
        before = entry.read_bytes()
        result = self.run_poll()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("queued 0 new notes", result.stdout)
        self.assertIn("1 unprocessed notes pending", result.stdout)
        self.assertIn("post-call-analyzer:on-trigger", self.marker.read_text())
        self.assertEqual(entry.read_bytes(), before)

    def test_empty_queue_does_not_launch(self):
        self.assertEqual(self.run_poll().returncode, 0)
        self.assertFalse(self.marker.exists())

    def test_processed_queue_residue_does_not_launch(self):
        for ledger_entry in ("not_done", {"id": "not_done"}):
            with self.subTest(ledger_entry=ledger_entry):
                self.ledger.write_text(json.dumps({"processed": [ledger_entry]}))
                (self.queue / "not_done.json").write_text('{"id":"not_done"}')
                self.assertEqual(self.run_poll().returncode, 0)
                self.assertFalse(self.marker.exists())

    def test_new_note_preserves_quotes_and_backslashes(self):
        title = 'Team """quoted""" \\ notes\nnext line'
        self.payload.write_text(json.dumps([{"id": "not_new", "title": title}]))
        result = self.run_poll()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(self.marker.exists())
        self.assertEqual(json.loads((self.queue / "not_new.json").read_text())["title"], title)

    def test_processed_api_notes_are_not_requeued(self):
        self.ledger.write_text('{"processed": [{"id":"not_done"}]}')
        self.payload.write_text('[{"id":"not_done"}]')
        self.assertEqual(self.run_poll().returncode, 0)
        self.assertEqual(list(self.queue.glob("*.json")), [])
        self.assertFalse(self.marker.exists())

    def test_api_failure_holds_checkpoint(self):
        self.env["TEST_API_RC"] = "1"
        self.assertEqual(self.run_poll().returncode, 0)
        self.assertEqual(self.checkpoint.read_text(), self.before)
        self.assertFalse(self.marker.exists())

    def test_malformed_json_holds_checkpoint(self):
        self.payload.write_text("not json")
        self.assertEqual(self.run_poll().returncode, 1)
        self.assertEqual(self.checkpoint.read_text(), self.before)
        self.assertFalse(self.marker.exists())

    def test_recovery_suppresses_error_notification_before_secret_lookup(self):
        self.payload.write_text("not json")
        self.env["SAPLING_NO_NOTIFICATIONS"] = "1"
        self.env["TEST_NOTIFICATION"] = str(self.root / "notification")
        self.env["TEST_SECRET_LOOKUP"] = str(self.root / "secret-lookup")
        self.stub("op", 'touch "$TEST_SECRET_LOOKUP"; printf "https://example.invalid"')
        self.stub("curl", 'touch "$TEST_NOTIFICATION"')
        self.assertEqual(self.run_poll().returncode, 1)
        self.assertFalse(Path(self.env["TEST_SECRET_LOOKUP"]).exists())
        self.assertFalse(Path(self.env["TEST_NOTIFICATION"]).exists())
        self.assertEqual(self.checkpoint.read_text(), self.before)


if __name__ == "__main__":
    unittest.main()
