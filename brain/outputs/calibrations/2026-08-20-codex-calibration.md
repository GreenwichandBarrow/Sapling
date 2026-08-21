---
schema_version: 1.0.0
date: 2026-08-20
type: output
output_type: calibration
runtime: codex
status: proposed
title: "Codex Calibration - 2026-08-20"
tags: ["date/2026-08-20", "output", "output/calibration", "runtime/codex", "status/proposed"]
---

# Codex Calibration Report - 2026-08-20

## Executive Summary

This headless Codex calibration found 78 unreviewed traces with 78 decisions and 12 learnings. The apparent backlog is real as an inventory count, but the calibration signal is still concentrated in a small subset: 59 task-tracker operational receipts, 1 weekly-tracker coordination receipt, and 18 substantive preference or workflow traces.

The latest prior report, `brain/outputs/calibrations/2026-08-13-codex-calibration.md`, already proposed the main structural changes: a trace receipt lane, scheduled-log redaction or summarization, Deal Aggregator critical-volume escalation, supervised email-intelligence closure, supervised skill-learning promotion, skill freshness verification, and a helper for "new since prior report." The new evidence this week does not require a new behavioral doctrine. It raises the priority of two existing proposals: receipt-lane separation and recovered-validator visibility.

Current scheduled/core health looks operationally live, not silently broken. `launchd-debugger` reported zero failures on 2026-08-20; `email-intelligence`, `deal-aggregator`, `relationship-manager`, `post-call-analyzer` polling, and `niche-intelligence` wrote or reported expected artifacts. The system risk is that successful jobs can still hide poor business throughput, recovered validator failures, and oversized logs.

No files outside this dated report were changed. No trace statuses were mutated. All behavior-changing improvements remain proposals for supervised maintenance.

## Trace Inventory

Trace helper command run: `python3 .codex/scripts/list-unreviewed-traces.py`.

Result: `78 unreviewed traces, 78 decisions, 12 learnings`.

Reconciled prior calibration: `brain/outputs/calibrations/2026-08-13-codex-calibration.md`.

Classification:

- Already covered by existing memory, skill doctrine, or prior calibration: email draft/send boundaries, live Drive template source-of-truth, Good Night multi-thread inventory, deal-aggregator Phase 2.5 tuning, Daily Ops / Task Manager thread boundaries, tracker-manager niche conventions, Good Morning brief restructuring, XPX intermediary voice, task carry-forward cleanup, meeting-brief approval-gated generation, and prior tracker-manager niche-output treatment.
- Genuine new learning: no new human-preference learning beyond prior proposals. New evidence supports two existing system-health proposals: separate mechanical trace receipts from calibration candidates, and record recovered validator failures so final success does not erase repair work.
- Noisy mechanical receipt: 59 task-tracker traces, including the new `brain/traces/2026-08-20-task-tracker-sync-done-status-synced-5.md`. It records 5 rows synced, 65 weekly slots scanned, 18 schedule-only skips, 0 ambiguities, plus a rollback snapshot. That is useful audit evidence, not a Kay-preference calibration item.
- Risky or business-sensitive recommendation needing Kay or supervised maintenance: trace status backfill, receipt-lane semantics, scheduled-log redaction, Deal Aggregator source/channel remediation, Good Morning operating-surface changes, skill freshness updates, and any edits to `.codex/hooks/`, `.agents/skills/`, `AGENTS.md`, `memory/`, validators, business workflow scripts, or scheduled workflow scripts.

Representative traces sampled this run:

- `brain/traces/2026-08-20-task-tracker-sync-done-status-synced-5.md`
- `brain/traces/2026-06-09-email-draft-template-boundary.md`
- `brain/traces/2026-07-13-meeting-brief-approval-gate.md`
- `brain/traces/2026-08-07-weekly-tracker.md`

## Findings

1. **The backlog remains inflated by receipts.** Of 78 pending traces, 59 are task-tracker receipts and 1 is a weekly-tracker coordination receipt. The raw pending count therefore overstates the unresolved calibration work by roughly 3x.

2. **Only one new unreviewed trace appeared since the 2026-08-13 run.** The new trace is the 2026-08-20 task-tracker sync receipt. It has no `## Learnings` section and does not change future agent behavior beyond the existing receipt-lane proposal.

3. **The prior substantive proposals are still live.** The most important open proposals remain receipt-lane handling, scheduled-log summarization, Deal Aggregator critical-volume escalation, recovered-failure reporting, skill-learning promotion, and freshness verification. None were applied during this report-first run.

4. **Scheduled health is green at the wrapper level.** `brain/trackers/health/launchd-debugger-2026-08-20.json` reports 0 failures detected, 0 fixes attempted, 0 Slack surfaces, and 19 runtime seconds.

5. **Recovered validator failures are getting hidden by final success.** The 2026-08-20 relationship-manager log shows an initial validator failure for a section header mismatch, a local correction, and then a passing final summary. The final artifact is valid, but calibration should count this as a recovered failure because it indicates validator/reporting fragility.

6. **Deal Aggregator remains live but below target.** The 2026-08-20 run wrote `brain/context/deal-aggregator-scan-2026-08-20.md`, passed validation, scanned 18 sources, found 0 deals, found 1 near miss, and reported a live email leg. The 2026-08-14 weekly digest shows a 7-day average of 0.0/day against a 1-3/day target, with source coverage diagnosed as the bottleneck.

7. **Weekly activity still shows zero throughput.** `brain/trackers/weekly/2026-08-14-weekly-tracker.md` shows 0 outreach sends, 0 drafts, 0 operations dials, 0 owner conversations, 0 NDAs, and 0 financials received. This is not necessarily a scheduler outage, but it deserves a pipeline operating response if it persists.

8. **Scheduled logs remain too verbose.** Recent logs include large skill-body dumps and high-volume command output. That makes health scans noisy, increases token pressure, and obscures the difference between a real failure and expected words like "ERROR" inside reference material.

## Proposed Changes

1. **High: implement the trace receipt lane.** Add explicit metadata for operational receipts, especially task-tracker row-write and sync receipts, and update `.codex/scripts/list-unreviewed-traces.py` to report calibration candidates separately from receipts. Backfill only after the convention is documented.

2. **High: surface recovered validator failures.** Add a lightweight "recovered validation issue" field to scheduled-run health artifacts or calibration evidence when a log contains a validator failure followed by a successful repair. Final pass/fail should remain green, but recovered failures should feed weekly calibration and Good Morning only when repeated.

3. **High: reduce scheduled-log payload size.** Suppress or summarize skill-body dumps, raw Gmail/thread payloads, raw HTML/base64 bodies, and high-volume command output in scheduled logs. Keep final artifact paths, validator lines, and concise summaries.

4. **High: keep Deal Aggregator critical-volume escalation open.** A live run with 0 surfaced deals and 0.0/day weekly average should not read as healthy just because validators pass. Treat repeated below-target volume as a Track B sourcing problem until source coverage is repaired or intentionally paused.

5. **Medium: add a zero-throughput persistence check to Good Morning or weekly calibration.** When outreach sends, drafts, operations dials, owner conversations, NDAs, and financials are all zero for two consecutive weekly trackers, surface the operating question as pipeline health rather than leaving it as passive metrics.

6. **Medium: process skill-local learnings under supervision.** Prioritize local `pipeline-manager`, `goodnight-closeout`, and `investor-update` learnings. Leave plugin/template learnings alone unless a local override is explicitly needed.

7. **Low: add a "new since prior calibration" helper.** The dated reports repeatedly reconcile current helper output against the prior report. A script field for new trace count, new receipt count, and new substantive count would reduce manual work and error risk.

## Deferred or Blocked

- Edits to `.codex/hooks/`, `.agents/skills/`, `AGENTS.md`, `memory/`, validators, scheduled scripts, and business workflow scripts are deferred because this scheduled run is report-first and proposal-only.
- Trace status mutation is deferred. No traces were marked `applied`, `proposed`, `skipped`, or `receipt`.
- Receipt-lane implementation is deferred because it changes trace semantics and helper output.
- Recovered-validator reporting is deferred because it changes scheduler health semantics and should be implemented carefully.
- Scheduled-log redaction is deferred because it changes runner behavior and needs care around debug usefulness.
- Deal Aggregator source/channel remediation is deferred because it touches sourcing strategy and possibly DealsX operating plumbing.
- Zero-throughput escalation is deferred because it changes the Good Morning decision surface and should be reviewed against Kay's current operating priorities.
- Skill freshness queue updates are deferred because changing verification dates without actual verification would create false freshness.
- Google Drive SOP reconciliation was not performed because no deliverable, schedule, or notification behavior was changed in this report-only run.

## Safety Notes

- No email was sent by this calibration run.
- No email draft was created by this calibration run.
- No commit was created by this calibration run.
- No Slack success post was made by this calibration run.
- No Google Sheet write was performed by this calibration run.
- No Google Drive document was edited by this calibration run.
- No Attio, Apollo, Gmail, Calendar, Drive, Sheets, Granola, or Slack write API was called by this calibration run.
- No traces were moved, archived, or status-mutated by this calibration run.
- No edits were made to `.codex/hooks/`, `.agents/skills/`, `AGENTS.md`, `memory/`, schemas, validators, business workflow scripts, or scheduled workflow scripts.
- Existing uncommitted files in the worktree were left untouched except for this new calibration report.

## Validation

- Required report path written: `brain/outputs/calibrations/2026-08-20-codex-calibration.md`.
- Required scheduled date used throughout: `2026-08-20`.
- Required frontmatter included with `runtime: codex` and `status: proposed`.
- Required headings included: Executive Summary, Trace Inventory, Findings, Proposed Changes, Deferred or Blocked, Safety Notes, and Validation.
- Report length exceeds 800 bytes.
- Calibration skill instructions read completely: `.agents/skills/calibration-workflow/SKILL.md`.
- Trace inventory helper ran: `python3 .codex/scripts/list-unreviewed-traces.py`.
- Latest prior calibration report read and reconciled: `brain/outputs/calibrations/2026-08-13-codex-calibration.md`.
- Output schema example checked before writing this vault output: `schemas/vault/output.yaml`.
- Scheduled/core health evidence reviewed: launchd-debugger 2026-08-20 JSON, relationship-manager 2026-08-20 final log, email-intelligence 2026-08-20 final log and artifact, deal-aggregator 2026-08-20 final log and scan artifact, post-call-analyzer 2026-08-20 poll log, niche-intelligence 2026-08-20 final log, weekly tracker 2026-08-14, and deal-aggregator weekly digest 2026-08-14.
- Wrapper validator to run after write: `python3 scripts/validate_calibration_workflow_integrity.py --date 2026-08-20`.
