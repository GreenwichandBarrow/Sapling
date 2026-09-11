---
schema_version: 1.0.0
date: 2026-09-10
type: output
output_type: calibration
runtime: codex
status: proposed
title: "Codex Calibration - 2026-09-10"
tags: ["date/2026-09-10", "output", "output/calibration", "runtime/codex", "status/proposed"]
---

# Codex Calibration Report - 2026-09-10

## Executive Summary

Proposal-only calibration completed for the scheduled date 2026-09-10. The inventory contains 83 pending traces, 83 helper-counted decisions and 13 learning sections, compared with 81/81/12 in [[outputs/calibrations/2026-09-04-codex-calibration]]. No trace status or business behavior was changed.

Priority judgment: strengthen nightly tracker preservation checks and weekly metric provenance before interpreting validator success or recorded zeros as operating health. Both recommendations have concrete local evidence. Receipt cleanup remains useful, but must preserve substantive recurring-task decisions. A task-layout repair is already present in source; do not reopen it as an unimplemented build.

## Trace Inventory

Required helper ran after reading the calibration skill: `python3 .codex/scripts/list-unreviewed-traces.py`. Result: **83 unreviewed traces, 83 decisions, 13 learnings**. The latest report read was [[outputs/calibrations/2026-09-04-codex-calibration]]. Delta: +2 traces, +2 helper-counted decisions, +1 learning section. The two dated additions consistent with that delta are the completion-sync receipt and nightly audit below. The prior report has no full inventory manifest, so this is not a proven identity-level set difference.

The helper forces at least one decision per file and counts section headings rather than individual choices. The nightly trace has two decision subsections and two learning bullets under one heading each. Totals therefore describe inventory, not 83 independently verified preference decisions. Of 83 pending filenames, 63 belong to the task-tracker family; this does not establish that all 63 are noise.

| Sample | Classification | Evidence and disposition |
|---|---|---|
| [[traces/2026-06-09-email-draft-template-boundary]] | Already covered; high safety importance | `memory/feedback_kay_handles_all_replies.md` reserves sends to Kay and keeps reusable templates in Drive. No new rule needed. |
| [[traces/2026-07-13-meeting-brief-approval-gate]] | Already covered; high workflow importance | `.agents/skills/meeting-brief-manager/SKILL.md` explicitly requires approved/on-demand generation. |
| [[traces/2026-09-04-task-tracker-sync-done-status-synced-3]] | Noisy mechanical receipt | Three synced rows plus rollback evidence; no new choice or rationale. Preserve execution evidence. |
| [[traces/2026-09-01-task-tracker-move-day-item-incomplete-thu]] | Noisy mechanical receipt in this sample | Records a carry operation and snapshot. Do not generalize to all carry/recurring decisions. |
| [[traces/2026-09-05-nightly-tracker-audit]] | Mixed technical learning and risky recommendation | Trailing-cell normalization is a technical observation; post-write verification is existing doctrine. The claim that rewriting an already-clean sheet is safer must not become an automatic rule. |

Genuine new calibration evidence: the nightly validator preservation gap and weekly metric coverage mismatch below. These are engineering findings, not new preferences attributed to Kay. Business-sensitive recommendations include mutation strategy, throughput interpretation, recurring-task authorization and bulk entity reconciliation. All remain proposals. The backlog is real inventory, but neither wholly new nor wholly actionable.

## Findings

### 1. High: nightly validation cannot prove preservation or completed migrations

The new nightly trace reports rewriting 42 already-clean rows. `.agents/skills/nightly-tracker-audit/SKILL.md` Step 4 instructs clearing and rewriting. Its headless prompt says a persistent Drive/write failure may print a STOP marker and exit normally because the wrapper validator will catch remaining violations.

`scripts/validate_nightly_tracker_audit_integrity.py` reads fixed range `A4:K100` and fixed Rank/Niche/Status positions. It checks lingering Tabled/Killed statuses, internal gaps and sequential ranks. It does not compare pre/post row identities or preserved values, check destination tabs, verify Drive placement or prove the complete used table was inspected. This also conflicts with the skill instruction to resolve live headers.

A local pure-function probe supplied two valid synthetic rows, then one surviving row. Both returned no failures, with counts two and one. This demonstrates a missing preservation baseline; it does not establish real data loss. A failed Drive move after source-row removal could escape these checks (inference from source). A successful validator cannot establish stronger guarantees than it tests.

### 2. High: weekly zeros do not establish business inactivity

Reviewed [[trackers/weekly/2026-08-14-weekly-tracker]], [[trackers/weekly/2026-08-21-weekly-tracker]], [[trackers/weekly/2026-08-28-weekly-tracker]] and [[trackers/weekly/2026-09-04-weekly-tracker]]. They record zero sends/drafts/dials; the latest also records one owner conversation and one intermediary introduction. The health reviewer found zero of seven session-decisions files in each weekly window.

`dashboard/data_sources.py` function `_count_verb_tags_in_window` counts SENT/DRAFTED bullets in those files and silently skips missing files. Send/draft zeros mean no recorded tags in available input, not verified absence of outreach. This corrects the stronger throughput interpretation in the prior calibration. Dials and other measures have separate sources requiring separate coverage checks.

The same file computes `load_new_contacts` as `len(snapshot.deals) + snapshot.closed_count`; weekly reports label the resulting 159 records as new contacts/Attio total. That calculation does not measure new People. `dashboard/snapshot.py` defaults active niches to empty unless an activity row named `Active Niches` exists; no matching producer label was found in `dashboard/data_sources.py`. An empty fallback causing the reported “none” is an inference requiring an integration check. `jj_active` represents lifetime dialing, not current niche status. Current statuses require the live Industry Research Tracker.

### 3. Current scheduled controls work with coverage limitations

Read-only health review examined current final logs and artifacts:

- `logs/scheduled/deal-aggregator-2026-09-10-0700.log.final` reports validator success, 16 sources, one opportunistic candidate and zero PASS matches. [[context/deal-aggregator-scan-2026-09-10]] already labels coverage incomplete, with no public-marketplace listings parsed and an old DealsX snapshot. Prior taxonomy work is partially reflected; do not call it wholly absent or equate zero observed PASS with no market opportunities.
- [[context/email-scan-results-2026-09-10]] records an already-processed bookkeeper period and skips duplicate invocation. It also records incomplete draft coverage: two drafts returned, one detail available.
- [[context/relationship-status-2026-09-10]] records the missing prior-day closeout and uses live Gmail/Attio/vault fallback. Its 500-record People pull does not prove exhaustive coverage.
- Both scheduled-date post-call-analyzer final logs report drained queues, ledger/archive agreement and passed validation; evening handoff/aging warnings remain. These are earlier runs, not calibration actions.
- `logs/scheduled/nightly-tracker-audit-2026-09-09-2330.log.final` reports 45 valid rows, no moves and validator success. The scheduled-date launchd-debugger JSON reports zero detected failures. Neither proves all business invariants were tested.

Latest local health report remains [[trackers/health/2026-09-04-health]], reporting RED and 1,890 People versus 404 entity files. These counts are historical. No scheduled-date health report was found; timer due state was not checked, so no missed-run claim is made. No new credential incident or email-send breach was established. The wrapper already has credential setup, email preflight and validator-failure propagation; do not propose these as absent.

### 4. Receipt rules conflict; some current learning is already implemented

`.agents/skills/decision-traces/SKILL.md` excludes mechanical receipts, while task-tracker-manager still requires successful completion-sync traces and several other verb traces. Its `learnings.md` now explicitly records receipt-emitter cleanup. Hiding filenames alone would mask this producer conflict.

The learning file also records a daily layout shift that blocked maintenance and a subsequent repair. `scripts/task_tracker.py` now detects a unique supported task header and NOTES boundary in `_require_day_task_layout`. This supports “repair present”; no live maintenance or comprehensive regression verification was run here. A separate approval-wording change was rejected by automatic approval review according to that learning. It remains deferred.

Pipeline-manager and goodnight-closeout retain learning entries. Investor-update records a prior promotion rather than active new learning; private-family-office is a template stub. Do not promote every nonempty learning file. The freshness queue remains old; no dates were advanced without actual service verification.

### 5. Medium: legacy calibration bookkeeping can conflict with proposal-only output

`.codex/hooks/calibration-stats-updater.py` dispatches on a `Write` event for calibration markdown, then archives applied traces, updates statistics, bumps VERSION and stages files without checking report status/runtime. No registration was found in searched `.codex` JSON/TOML files; live activation is not established. If activated, its contract conflicts with this reporting mode. It was not invoked by this run. The inventory helper also treats proposed traces as pending, so changing statuses alone would not resolve repeated analysis.

## Proposed Changes

1. **High: strengthen nightly preservation and failure reporting.** Targets: `scripts/validate_nightly_tracker_audit_integrity.py`, nightly-tracker-audit skill/headless prompt and associated wrapper failure handling. Resolve headers/full used range; require pre-write snapshots; compare row identities and preserved values across source/destinations; verify expected Drive moves; propagate operation failures even when ranks are clean. Validate dropped rows, changed notes, incomplete moves, reordered headers and rows beyond the old range. Separately assess normalized no-change handling before replacing the current rewrite contract. Firing case: new nightly trace and local preservation probe. No real data-loss claim.

2. **High: repair weekly metric provenance before performance escalation.** Targets: `dashboard/data_sources.py`, `dashboard/snapshot.py`, `scripts/snapshot_weekly_to_vault.py` and associated validation. Preserve source coverage/missing-input information, label recorded activity accurately, correct pipeline-total labels, verify the active-niche producer and distinguish historical dialing. Test missing versus complete inputs; preserve unknown rather than factual zero. Firing case: four snapshots and inspected computations. This refines the existing operating-health proposal.

3. **Medium: reconcile receipt production and inventory semantics.** Targets: task-tracker-manager trace instructions, `scripts/task_tracker.py` emitter and `.codex/scripts/list-unreviewed-traces.py`. Preserve rollback/verb evidence in execution logs; emit decision traces for actual choices with rationale. Report substantive candidates and receipts separately and retain an identity manifest for future deltas. Preserve recurring schedule decisions that change future behavior. Firing case: sampled receipts and explicit instruction conflict. No blanket archival.

4. **Medium: protect proposal-only calibration bookkeeping.** Target: `.codex/hooks/calibration-stats-updater.py`, after confirming registration. Proposal/no-action/blocked reports must not archive traces, stage files or bump versions. Verify absence of side effects for each reporting status. Firing case: inspected status-blind branch; live activation is unverified.

Existing entity-reconciliation and deal-source-coverage proposals remain in the prior report; they are not newly discovered requirements.

## Deferred or Blocked

- All behavior changes and edits to protected skills, hooks, memory, doctrine, dashboard/business scripts and validators remain deferred to separately authorized maintenance. No interactive approval request is pending.
- Trace backfills/archival require per-item reviewable classification. No trace was marked applied, proposed or skipped.
- Actual outreach totals, current niche statuses, target alignment and current entity drift need live source verification. This report uses local evidence only.
- Live Drive SOP reconciliation and vendor/API freshness certification were not performed. Before changing deliverables, schedules or notifications, read the current SOP through the established 1Password-backed gog path and reconcile its contract. No such behavior changed here.
- Task-tracker approval-wording cleanup remains separate because its learning records an automatic approval-review rejection for weakening a safeguard. This run neither retried nor bypassed that change.
- Required local report sources were available. Missing closeouts/current health output limit business conclusions; retry those assessments against restored or source-complete evidence. They do not require this headless report to wait for human input.

## Safety Notes

- No email was sent. No email draft was created.
- No commit was created. No staging, push, VERSION bump or statistics update was performed.
- No Slack success post was made. No Slack message was sent by calibration.
- No Google Sheet, Drive, Gmail, Attio or other external write API was called.
- No credentials were loaded, rotated or printed.
- No edits were made to `.codex/hooks/`, `.agents/skills/`, `AGENTS.md`, `memory/`, schemas, validators or business workflow scripts.
- No traces were mutated or archived. No mechanical metadata hygiene was necessary.
- Existing unrelated worktree files were left untouched. The only intended repository output is this report. The health subagent reported no writes.

## Validation

- Exact report path: `brain/outputs/calibrations/2026-09-10-codex-calibration.md`. Required scheduled date, frontmatter and headings are present; report exceeds 800 bytes.
- The explicit calibration schema 1.0.0 takes precedence over the general output schema example, read before writing. Vault evidence uses wiki-links and required tags are present.
- Skill read, helper execution, latest-report reconciliation, representative sampling and scheduled/core health review completed in that order.
- Nightly validator pure-function probe used synthetic local data only. Two-row and one-row inputs both passed, demonstrating the limited guarantee above.
- An initial shell write was blocked by a command-parsing guard before execution. A structured file patch was used for the report; no secret-file access was requested or performed.
- Authoritative on-disk validation command: `python3 scripts/validate_calibration_workflow_integrity.py --date 2026-09-10`.
- Final worktree and HEAD checks accompany validation to confirm report-only scope. No live service verification or workflow repair is claimed.
