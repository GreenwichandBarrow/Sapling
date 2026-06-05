#!/usr/bin/env python3
from __future__ import annotations

import os
import subprocess
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = REPO_ROOT / "scripts" / "validate_relationship_manager_integrity.py"
SECTIONS = [
    "## Overdue Contacts",
    "## Auto-Resolved",
    "## Pending Intros",
    "## Warm Intro Opportunities",
    "## Vault → Attio Syncs",
    "## Attio Dedup Needed",
    "## System Status Alerts",
]


class RelationshipManagerValidatorTest(unittest.TestCase):
    def run_validator(self, vault_dir: Path) -> subprocess.CompletedProcess[str]:
        env = os.environ.copy()
        env["RELATIONSHIP_MANAGER_VAULT_DIR"] = str(vault_dir)
        return subprocess.run(
            ["python3", str(VALIDATOR), "--date", "2026-06-05"],
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )

    def write_artifact(self, vault_dir: Path, body: str) -> None:
        (vault_dir / "relationship-status-2026-06-05.md").write_text(
            "---\n"
            "date: 2026-06-05\n"
            "type: relationship-status\n"
            "---\n\n"
            + body
        )

    def test_requires_every_section_header(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp)
            self.write_artifact(vault, "## Overdue Contacts\n\nNone\n" + ("x" * 250))

            result = self.run_validator(vault)

            self.assertEqual(result.returncode, 2)
            self.assertIn("missing expected section", result.stderr)
            self.assertIn("## System Status Alerts", result.stderr)

    def test_full_artifact_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            vault = Path(tmp)
            body = "\n\n".join(f"{section}\n\nNone." for section in SECTIONS)
            self.write_artifact(vault, body + "\n" + ("x" * 250))

            result = self.run_validator(vault)

            self.assertEqual(result.returncode, 0, result.stderr + result.stdout)


if __name__ == "__main__":
    unittest.main()
