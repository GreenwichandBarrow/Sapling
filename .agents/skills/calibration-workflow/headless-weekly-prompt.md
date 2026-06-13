# calibration-workflow - Headless Weekly Codex Run

You are running the `calibration-workflow` skill non-interactively under systemd. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals, and do not wait for Kay.

## Mandatory operating mode

This Codex Phase 1 version is report-first and proposal-only.

You may:
- Analyze unreviewed traces, recent calibration outputs, memory files, skills, hooks, and scheduled-workflow evidence.
- Produce a durable calibration report with prioritized recommendations.
- Apply only strictly mechanical metadata hygiene if it is already proven by existing calibration output and cannot change business behavior.

You must not:
- Send email. Never call any send command or API.
- Commit changes.
- Post success summaries to Slack.
- Edit `.codex/hooks/`, `.agents/skills/`, `AGENTS.md`, `memory/`, or business workflow scripts during the scheduled run unless the edit is a tiny validator/reporting fix required to complete this headless run. Put those improvements in the report as proposals instead.
- Mark traces as `applied` unless the report clearly explains why each trace was already covered by existing memory/skill/doctrine. Prefer `proposed` over mutation.

## Mandatory ordering

1. Read `.agents/skills/calibration-workflow/SKILL.md` for domain context, but override any instruction that requires human approval, Claude-only paths, direct commit, or Slack success posting.
2. Run the trace inventory helper:
   `python3 .codex/scripts/list-unreviewed-traces.py`
3. Read the latest calibration report in `brain/outputs/calibrations/` and reconcile whether apparent backlog is real or already handled.
4. Sample enough unreviewed traces to classify them into:
   - already covered by existing memory/skill/doctrine
   - genuine new learning
   - noisy mechanical receipt
   - risky or business-sensitive recommendation needing Kay
5. Review scheduled/core skill health before proposing changes. Prioritize improvements that reduce silent-success, duplicate-action, email-send, credential, or data-clobber risk.
6. Write the durable report at exactly:
   `brain/outputs/calibrations/{YYYY-MM-DD}-codex-calibration.md`

## Required report structure

The report must include YAML frontmatter:

```yaml
---
schema_version: 1.0.0
date: {YYYY-MM-DD}
type: output
output_type: calibration
runtime: codex
status: proposed
title: "Codex Calibration - {YYYY-MM-DD}"
tags: ["date/{YYYY-MM-DD}", "output", "output/calibration", "runtime/codex", "status/proposed"]
---
```

Then include these headings:

- `# Codex Calibration Report - {YYYY-MM-DD}`
- `## Executive Summary`
- `## Trace Inventory`
- `## Findings`
- `## Proposed Changes`
- `## Deferred or Blocked`
- `## Safety Notes`
- `## Validation`

If no genuine new calibration is needed, still write the report with `status: no_action` and explain why.

## What success looks like

- The dated report exists at `brain/outputs/calibrations/{YYYY-MM-DD}-codex-calibration.md`.
- The report is at least 800 bytes and has all required headings.
- The report contains explicit safety notes confirming no email was sent, no commit was created, and no Slack success post was made.
- Any action that needs Kay is listed under `Deferred or Blocked`, not asked interactively.

## Failure handling

If source data is unavailable:
- Write the report anyway with `status: blocked`.
- Explain the unavailable source and the retry path under `Deferred or Blocked`.
- Do not exit waiting for approval.

The wrapper-side validator `scripts/validate_calibration_workflow_integrity.py` is authoritative for the scheduled job.
