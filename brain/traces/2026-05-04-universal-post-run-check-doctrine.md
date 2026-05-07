---
schema_version: 1.1.0
date: 2026-05-04
type: trace
title: "Universal POST_RUN_CHECK doctrine — every launchd skill needs a validator, not just mutating ones"
trace_type: doctrine-establishment
tags: ["date/2026-05-04", "trace", "topic/launchd-hardening", "topic/conference-discovery", "topic/dashboard-reliability"]
---

# Universal POST_RUN_CHECK doctrine — every launchd skill needs a validator, not just mutating ones

## Trigger

May 3, 2026 the scheduled `conference-discovery` launchd job's archival subagent cleared the Conference Pipeline Google Sheet (~70 rows) before its stream timed out. The skill self-detected the destruction, saved a memory rule (`feedback_no_clear_rewrite_populated_sheets`), surfaced to Kay via the log, and exited 0. The wrapper saw exit 0 → `launchd-debugger` did not flag → the dashboard's C-Suite & Skills weekly-flow tile for the Sunday cell went green.

Kay caught it visually on May 4 evening when she noticed the Conference Pipeline tab looked empty. She asked: "why does the conference pipeline look empty?"

The CLAUDE.md hardening doctrine at the time (2026-04-25, bead ai-ops-1) explicitly distinguished mutating scheduled skills (need POST_RUN_CHECK validator) from read-only skills ("absence-of-output surfaces in pipeline-manager"). conference-discovery was classified as mutating but had not yet been added to the hardened-skill list. The 5 hardened skills at that time: target-discovery Phase 2, jj-operations-sunday, nightly-tracker-audit, weekly-tracker, relationship-manager.

## Decision

Kay broadened the doctrine: **"any launchd skill should be on there."** No more mutating-vs-read-only distinction for the purposes of POST_RUN_CHECK exemption. Every launchd-scheduled skill needs a validator.

Read-only skills get lighter validators (artifact-landed checks: "did `email-scan-results-{TODAY}.md` land >200 bytes with required sections?"), but no skill is exempted from the post-run check entirely.

## Reasoning

The mutating-vs-read-only distinction was load-bearing on a flawed assumption: "read-only skills can't cause damage, so silent zero is fine." The May 3 incident proved silent zero is not fine even when no damage occurs — the dashboard's "healthy" claim is itself a load-bearing signal that drives Kay's decisions, and a green tile that masks reality is a category of harm separate from data destruction.

Specifically: conference-discovery's failure was structurally a "graceful self-detect + stop" — but from launchd's perspective, indistinguishable from a successful run. Read-only skills that fail silently (e.g., email-intelligence not actually scanning Gmail because of an OAuth blip) produce the same failure shape. The dashboard goes green either way.

A POST_RUN_CHECK that asks "did this skill produce its expected artifact, freshly?" catches both classes. So the validator pattern is the right shape; the only thing that needed updating was the universal-application rule.

## Action taken

1. Wrote `scripts/validate_conference_discovery_integrity.py` (fails on missing pre-run snapshot or row delta > 15).
2. Wrote `.claude/skills/conference-discovery/headless-sunday-prompt.md` mandating pre-run snapshot at `brain/context/rollback-snapshots/conference-pipeline-pre-run-{TODAY}.json` BEFORE any Pipeline mutation; bans clear-then-rewrite; caps single-run archival at 15 rows.
3. Updated `~/Library/LaunchAgents/com.greenwich-barrow.conference-discovery.plist` with POST_RUN_CHECK env var; reloaded.
4. Updated `CLAUDE.md` "Wrapper hardening pattern" section with the universal doctrine; added 2026-05-04 dated entry; conference-discovery added to hardened list.
5. Hardened the 3 highest-leverage remaining gaps (snapshot refreshers feeding the dashboard) — attio-snapshot-refresh, jj-snapshot-refresh, apollo-credits-refresh — same evening.
6. Audit logged 5-6 still-unhardened launchd skills (email-intelligence, calibration-workflow, external-services-probe, weekly-archive-export, weekly-snapshot, health-monitor) for follow-up batch session.
7. Belt-and-suspenders: added `Bash(gog sheets clear:*)` to project-local settings.local.json deny list to block the wipe pattern at the harness layer pre-emptively.

## Implication for future agents

When implementing or scheduling ANY launchd job, build the validator with it — not as a follow-up. The validator is now part of the wrapper-hardening pattern, not an upgrade to it. Read-only skills get artifact-landed checks; mutating skills get content-sanity checks. Both must exist before the plist goes live.

Cross-ref: `feedback_dashboard_green_can_lie.md`, `feedback_no_clear_rewrite_populated_sheets.md`, `feedback_mutating_skill_hardening_pattern.md` (now extends to all skills, not just mutating).
