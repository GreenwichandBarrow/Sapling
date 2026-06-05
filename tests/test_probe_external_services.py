#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "probe_external_services.py"
spec = importlib.util.spec_from_file_location("probe_external_services", MODULE_PATH)
probe = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(probe)


class McpProcessProbeTest(unittest.TestCase):
    def test_all_manual_oauth_skips_do_not_report_error(self) -> None:
        with patch.object(probe, "_run", return_value=(0, "", "", 12)):
            result = probe.probe_mcp_processes()

        self.assertEqual(result["status"], "skip")
        self.assertIn("manual-skip=attio-mcp,superhuman", result["message"])
        self.assertIn("manual OAuth", result["skip_reason"])

    def test_running_active_process_with_other_manual_skip_is_ok(self) -> None:
        ps = "123 ? S 0:00 /usr/bin/attio-mcp\n"
        with patch.object(probe, "_run", return_value=(0, ps, "", 12)):
            result = probe.probe_mcp_processes()

        self.assertEqual(result["status"], "ok")
        self.assertIn("attio-mcp=1", result["message"])
        self.assertIn("manual-skip=superhuman", result["message"])

    def test_unexpected_missing_still_errors(self) -> None:
        with (
            patch.object(probe, "_run", return_value=(0, "", "", 12)),
            patch.object(probe, "probe_attio_mcp", return_value=probe._result("ok", 1, "healthy")),
            patch.object(probe, "probe_superhuman", return_value=probe._skip("manual")),
        ):
            result = probe.probe_mcp_processes()

        self.assertEqual(result["status"], "error")
        self.assertIn("unexpected-missing=attio-mcp", result["message"])


if __name__ == "__main__":
    unittest.main()
