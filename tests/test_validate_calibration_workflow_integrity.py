#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "validate_calibration_workflow_integrity.py"
spec = importlib.util.spec_from_file_location("validate_calibration_workflow_integrity", MODULE_PATH)
validator = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(validator)


def valid_report() -> str:
    return """---
date: 2026-06-05
type: output
output_type: calibration
runtime: codex
status: no_action
---

# Codex Calibration Report - 2026-06-05

## Executive Summary

No changes needed.

## Trace Inventory

Reviewed scheduled skill traces and validator results.

## Findings

No risky drift found.

## Proposed Changes

None.

## Deferred or Blocked

None.

## Safety Notes

No email will be sent. No commit will be created by this calibration report. No Slack message will be posted.

## Validation

Validator completed.
""" + ("x" * 900)


class CalibrationWorkflowValidatorTest(unittest.TestCase):
    def test_valid_report_passes(self) -> None:
        failures, status = validator.validate_report_text(valid_report(), "2026-06-05")

        self.assertEqual(failures, [])
        self.assertEqual(status, "no_action")

    def test_missing_safety_notes_fail(self) -> None:
        report = valid_report().replace("No Slack message will be posted.", "")

        failures, _ = validator.validate_report_text(report, "2026-06-05")

        self.assertTrue(any("no slack" in f for f in failures))

    def test_interactive_waiting_phrasing_fails(self) -> None:
        report = valid_report() + "\nShould I apply all of these?\n"

        failures, _ = validator.validate_report_text(report, "2026-06-05")

        self.assertTrue(any("interactive/waiting" in f for f in failures))


if __name__ == "__main__":
    unittest.main()
