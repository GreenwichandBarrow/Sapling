---
schema_version: 1.0.0
date: 2026-06-12
type: output
output_type: calibration
runtime: codex
status: proposed
title: "Codex Calibration - 2026-06-12"
tags: ["date/2026-06-12", "output", "output/calibration", "runtime/codex", "status/proposed"]
---

# Codex Calibration Report - 2026-06-12

## Executive Summary

This headless Codex calibration found 4 unreviewed traces: 2 from 2026-06-09 and 2 from 2026-06-10. The apparent backlog is small and mostly not a raw doctrine gap. Two learnings are already substantially covered by existing rules: Codex must draft only and never send email; deal-aggregator success is measured by useful deal volume, not merely green scheduled execution. Two learnings are genuine workflow refinements that should be promoted through supervised skill maintenance: Gmail drafts must not be used as a reusable-template store, and `/goodnight` must keep its new multi-thread inventory behavior stable as the Codex multi-thread operating model expands.

The latest prior Codex calibration was `brain/outputs/calibrations/2026-06-05-codex-calibration.md`. Its open items have partially improved: the investor-update learning was already promoted, and the external-services snapshot now marks Attio MCP as a manual OAuth skip rather than an unexpected MCP process error. Deal-aggregator productivity remains the main recurring health concern: the June 5 digest showed 0.33 surfaced deals/day against the 1-3/day target, and the June 11 dashboard status still reports volume below target with one blocked source.

No system edits were made. This run wrote only this report.

## Trace Inventory

Trace helper command: `python3 .claude/scripts/list-unreviewed-traces.py`

Result: `4 unreviewed traces, 4 decisions, 4 learnings`.

Classification:

- Already covered by existing memory/skill/doctrine: `2026-06-09-email-draft-template-boundary` is covered for the no-send boundary by `AGENTS.md`, `memory/feedback_kay_handles_all_replies.md`, `pipeline-manager`, `target-discovery`, and `deal-aggregator` safety language. `2026-06-10-deal-aggregator-phase-2-5-open` is covered directionally by `memory/feedback_deal_aggregator_volume_first.md`, `memory/feedback_all_channels_parallel.md`, and the deal-aggregator SKILL.md target language.
- Genuine new learning: `2026-06-09-goodnight-multi-thread-git-scope` and `2026-06-10-goodnight-multi-thread-inventory` define a durable closeout requirement for Codex multi-thread operation. The command already contains a Step 2A inventory, but this should be treated as canonical and monitored. The template-source-of-truth portion of `2026-06-09-email-draft-template-boundary` is also a genuine refinement because reusable email language belongs in Drive/template workflows, not Gmail drafts.
- Noisy mechanical receipt: none. All 4 traces encode non-obvious operating preferences, not mere task receipts.
- Risky or business-sensitive recommendation needing Kay: deal-aggregator source additions/retirements and any change to job frequency/model/scope. These affect sourcing strategy, costs, or pipeline behavior and should stay in review surfaces, not be mutated by headless calibration.

## Findings

1. **The send boundary is already well covered, but the Gmail-draft/template boundary needs propagation.** Existing doctrine says draft only, never send. The newer nuance is that generic reusable email copy should live in Google Drive master templates and relevant outreach/email skills, while Gmail drafts are only actual messages Kay may personally send.

2. **Goodnight has already been updated for multi-thread inventory.** `.claude/commands/goodnight.md` now requires inventorying active/recent Codex threads or falling back to repo evidence, classifying each thread as Included, No repo delta, or Excluded with reason. This satisfies the core of both goodnight traces. Remaining risk is validator/reporting drift: future closeouts need to prove the inventory happened and account for dirty files left after commit.

3. **Deal-aggregator is green enough operationally but still under target.** The June 5 digest showed 0.33 deals/day over available weekday artifacts, with no missing weekday scan artifacts. The June 11 status still reports `BELOW TARGET`, 0 deals found in the afternoon run, 4 broker-opportunistic items, and one blocked source (`Flippa`, browser fallback unavailable). The trace is correct: green timers and validators are not the success metric.

4. **Prior calibration follow-up improved.** `investor-update/learnings.md` now says the 2026-05-28 investor briefing format learning was promoted on 2026-06-05. The external-services snapshot now marks `mcp-processes` as `skip` with manual Attio OAuth reconnect context instead of a misleading unexpected error.

5. **Scheduled/core health is broadly passing, with productivity watch items.** Recent final logs show relationship-manager, post-call-analyzer, nightly-tracker-audit, target-discovery Phase 2, weekly snapshot, Apollo, Attio snapshot, GOG, GitHub, and OpenAI Codex auth all landing artifacts or reporting healthy. Productivity metrics remain uneven: the June 5 weekly tracker had 0 outreach sends, 7 drafts, 96 operations dials, 4 owner conversations, 0 NDAs, 0 financials, and 0 CIMs. JJ activity recovered to 177 dials for the 2026-06-05 to 2026-06-11 bucket.

6. **Trace status fields are inconsistent with calibration review status.** Two listed traces have `status: done`, but the inventory helper still lists them as unreviewed. That is acceptable if `status: done` means task completion, but the report should not assume those traces have been calibrated. A clearer separation between task status and calibration review status would reduce future ambiguity.

## Proposed Changes

1. **Promote the Gmail-draft/template boundary into email-facing skills.** Target: `email-intelligence`, `pipeline-manager`, `outreach-manager`, and any draft-audit helper. Proposed rule: Gmail drafts are execution artifacts only; reusable language/templates live in the Drive G&B master template folder and must be pulled through the relevant skill/template workflow. Priority: high, because it reduces stale draft noise and prevents template artifacts from surfacing as pending messages.

2. **Add a lightweight goodnight closeout validation check.** Target: `/goodnight` command or a companion validator. Proposed check: the session-decisions file must include a thread inventory/source note and any post-commit dirty files must be classified with a reason. Priority: high, because multi-thread work increases the chance of unowned repo artifacts or incomplete commits.

3. **Keep deal-aggregator Phase 2.5 focused on outcome metrics.** Target: Phase 2.5 review queue / deal-aggregator maintenance. Proposed emphasis: source yield, source coverage parity, blocked-source recovery, broker-opportunistic surfacing, and review UX. Do not close the work solely because systemd, email leg, and validators are green. Priority: high, but business-sensitive; source roster changes should stay in Kay review artifacts.

4. **Clarify trace metadata semantics.** Target: trace schema or inventory helper. Proposed change: use a calibration-specific field such as `review_status: pending|proposed|applied|skipped`, and do not infer review state from `status: done`. Priority: medium; this reduces false backlog confusion without changing business behavior.

5. **Continue the weekly health distinction between reliability and productivity.** Target: calibration-workflow report prompt. Proposed rule: scheduled health should separately report (a) artifact/validator reliability and (b) business-output sufficiency. Priority: medium; this prevents "green run" evidence from masking low funnel output.

## Deferred or Blocked

- **Deal-aggregator source roster actions remain Kay/business-sensitive.** The June 5 digest proposed adding Archveo Advisors and moving 4 sources to Dormant. This run did not write to sheets or mutate source status. Retry path: surface through the normal review bucket or a supervised tracker-manager/deal-aggregator maintenance pass.

- **Goodnight validator implementation is deferred.** It would touch command/workflow behavior and potentially hooks or validators. Retry path: implement in a supervised maintenance pass after deciding whether validation belongs in `/goodnight`, a standalone script, or the evening wrapper.

- **Email-template propagation is deferred.** It requires edits to email-facing skills and potentially Drive-template fetch logic. Retry path: promote through `evolve` or a supervised calibration edit, using `memory/feedback_kay_handles_all_replies.md` as the source case.

- **No current-week full tracker artifact for 2026-06-12 was available at report time.** The latest complete weekly tracker artifact read was `brain/trackers/weekly/2026-06-05-weekly-tracker.md`. Retry path: the next calibration should read the 2026-06-12 weekly tracker after the weekly snapshot job lands.

## Safety Notes

- No email was sent by this calibration run.
- No commit was created by this calibration run.
- No Slack success post was made by this calibration run.
- No edits were made to `.codex/hooks/`, `.agents/skills/`, `AGENTS.md`, `memory/`, business workflow scripts, or Google Sheets.
- No traces were marked `applied` during this run.
- Actions needing Kay or supervised workflow ownership are listed under `Deferred or Blocked`; the headless run did not ask interactive approval questions.

## Validation

- Required report path exists: `brain/outputs/calibrations/2026-06-12-codex-calibration.md`.
- Required headings are present.
- Report is longer than 800 bytes.
- Trace inventory helper ran and returned 4 unreviewed traces.
- Latest prior Codex calibration report was read and reconciled against current trace/helper output.
- Scheduled/core health evidence reviewed: external-services snapshot, deal-aggregator status and weekly digest, weekly tracker artifact, recent final logs for relationship-manager, post-call-analyzer, nightly-tracker-audit, target-discovery, weekly snapshot, Apollo snapshot, Attio snapshot, and JJ activity snapshot.
- Wrapper validator to run after write: `python3 scripts/validate_calibration_workflow_integrity.py --date 2026-06-12`.
