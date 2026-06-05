# Phase 1 Migration Inventory

Date: 2026-06-04
Host: `agent-vps-7731c88b`
Project: `~/projects/Sapling`

This inventory records the live surfaces found during the Claude Code to Codex Phase 1 migration. It is intentionally descriptive: conversion work should update this file as validation and cutover status changes.

## Summary

- Skills: 46 migrated skill files exist in `.agents/skills`, matching the 46 legacy `.claude/skills` files.
- Hooks: legacy `.claude/hooks` were copied into `.codex/hooks`, with `.codex/hooks.json` routing through `.codex/hooks/run-hook.sh`.
- Live scheduled jobs: 21 user systemd timers were found.
- Live Codex cutover: `health-monitor.service`, `nightly-tracker-audit.service`, `launchd-debugger.service`, `email-intelligence.service`, `post-call-analyzer-poll.service`, and the `deal-aggregator` service cluster now use Codex runner paths.
- Live legacy agent runner: 6 direct `run-skill.sh` services still remain on Claude because they are blocked, date-sensitive, or mutating workflows that were not safe to blindly pilot overnight.
- Direct script jobs: 6 recurring jobs appear agent-free and should remain unchanged in Phase 1 unless they internally trigger agent work.
- Cron: one user crontab entry exists for temp cleanup only.
- MCP: no active repo-level `.mcp.json` was found. The only live-looking MCP state was `~/.claude/mcp-needs-auth-cache.json`; scheduled Codex jobs must not depend on MCP until tested.

## Skills

`.agents/skills` contains a direct migration of all legacy skill directories:

- agent-chatroom
- budget-manager
- calibration-workflow
- cass
- conference-discovery
- conference-engagement
- create-agent-skills
- create-skill
- deal-aggregator
- deal-evaluation
- decision-traces
- email-intelligence
- evolve
- generate-prd
- generate-stories
- generate-visuals
- github
- gmail-filter-add
- gogcli
- health-monitor
- investor-update
- jj-operations
- launchd-debugger
- list-builder
- meeting-brief-manager
- meeting-brief
- migration-workflow
- niche-intelligence
- nightly-tracker-audit
- obsidian-vault-ops
- onboard
- outreach-manager
- pipeline-manager
- plan-refinery
- post-call-analyzer
- post-loi
- relationship-manager
- river-guide-builder
- socrates
- target-discovery
- task-tracker-manager
- today
- tracker-manager
- triage
- warm-intro-finder
- weekly-tracker

Phase 1 status: migrated, not yet Codex-improved. Phase 2 should review these for Codex-native execution improvements.

## Hooks

Codex hook files found:

- `.codex/hooks.json`
- `.codex/hooks/run-hook.sh`
- `.codex/hooks/router/pre_tool_use.py`
- `.codex/hooks/router/post_tool_use.py`
- `.codex/hooks/router/session_start.py`
- `.codex/hooks/router/stop.py`
- `.codex/hooks/router/pre_compact.py`
- `.codex/hooks/router/user_prompt_submit.py`
- `.codex/hooks/router/handlers/*`
- copied support hooks such as `git-auto-commit-stop.sh`, `git-smart-stage.sh`, `git-sync-startup.sh`, `session-init.sh`, `validate-edits.py`, `calibration-stats-updater.py`, `chatroom-state-sync.py`, and `enrichment_integrity_check.py`.

Phase 1 status: must-have safety hook logic is copied and synthetic checks pass for email-send denial and secret-file denial. Scheduled jobs also enforce safety in `scripts/run-agent-skill.sh` so they are not dependent on interactive hook execution.

## Live Systemd Timers

| Timer | Next/Pattern | Service | Current Runtime | Phase 1 Status |
| --- | --- | --- | --- | --- |
| `calibration-workflow.timer` | Thu 23:00 | `calibration-workflow.service` | Claude runner | blocked |
| `nightly-tracker-audit.timer` | daily 23:30 | `nightly-tracker-audit.service` | Codex runner | cutover |
| `health-monitor.timer` | Fri 00:30 | `health-monitor.service` | Codex runner | cutover |
| `launchd-debugger.timer` | daily 05:00 | `launchd-debugger.service` | Codex runner | cutover |
| `relationship-manager.timer` | weekdays 06:50 | `relationship-manager.service` | Claude runner | pending validation |
| `email-intelligence.timer` | weekdays 07:00 | `email-intelligence.service` | Codex runner | cutover |
| `deal-aggregator.timer` | weekdays 07:30 | `deal-aggregator.service` | Codex runner | cutover |
| `deal-aggregator-friday.timer` | Fri 07:30 | `deal-aggregator-friday.service` | Codex runner | cutover |
| `apollo-credits-refresh.timer` | weekdays hourly 08:00-20:00 | `apollo-credits-refresh.service` | direct script | unchanged |
| `attio-snapshot-refresh.timer` | weekdays hourly 08:00-20:00 | `attio-snapshot-refresh.service` | direct script | unchanged |
| `external-services-probe.timer` | weekdays half-hourly 08:00-20:30 | `external-services-probe.service` | direct script | unchanged |
| `jj-snapshot-refresh.timer` | weekdays 09:00, 14:30, 18:00 | `jj-snapshot-refresh.service` | direct script | unchanged |
| `post-call-analyzer-poll.timer` | daily 13:00 and 18:00 ET | `post-call-analyzer-poll.service` | Codex poller -> Codex runner on trigger | cutover; zero-queue poller pilot only |
| `deal-aggregator-afternoon.timer` | weekdays 14:00 | `deal-aggregator-afternoon.service` | Codex runner | cutover |
| `weekly-snapshot.timer` | Fri 22:00 | `weekly-snapshot.service` | direct script | unchanged |
| `weekly-archive-export.timer` | Sat 09:00 | `weekly-archive-export.service` | direct script | unchanged |
| `target-discovery-sunday.timer` | Sun 15:00 | `target-discovery-sunday.service` | Claude runner | pending validation; validator race noted |
| `jj-operations-sunday.timer` | Sun 18:00 | `jj-operations-sunday.service` | Claude runner | pending validation |
| `conference-discovery.timer` | Sun 21:00 | `conference-discovery.service` | Claude runner | pending validation |
| `niche-intelligence.timer` | Tue 22:30 | `niche-intelligence.service` | Claude runner | pending validation |

`launchpadlib-cache-clean.timer` is also present, but it is unrelated to Sapling agent migration.

## Live Agent-Backed Services Still On Claude

These live services still point at `scripts/run-skill.sh`:

- `calibration-workflow.service`
- `conference-discovery.service`
- `jj-operations-sunday.service`
- `niche-intelligence.service`
- `relationship-manager.service`
- `target-discovery-sunday.service`

Conversion rule: validate each workflow manually, then apply `scripts/prepare-codex-systemd-cutover.sh --apply --group <group>`. Do not edit timers during Phase 1 unless required.

## Agent Clusters

- `health-monitor`: validated and cut over.
- `deal-aggregator`: morning, afternoon, and Friday digest validated and cut over as one cluster.
- `post-call-analyzer`: poller cut over after zero-queue Codex pilot; analyzer trigger has prompt/validator coverage but still needs an observed queued-note Codex run.
- `target-discovery` / `jj-operations`: related via JJ niche context and should be treated carefully as a Sunday cluster.
- `email-intelligence`: validated no-send/draft-only behavior for the 2026-06-05 pilot and cut over.
- `relationship-manager`: may mutate CRM/contact state; validate with artifact checks before live cutover.
- `calibration-workflow`: blocked until headless prompt and durable-output validator exist.

## Cron

User crontab:

```cron
0 4 * * * /home/ubuntu/.local/bin/tmp-cleanup >/dev/null 2>&1
```

This is not an agent workflow and does not need Codex migration.

## Remaining Claude References

Expected retained references during Phase 1:

- `.claude/`
- `CLAUDE.md`
- `scripts/run-skill.sh`
- live services listed above that are not yet validated
- documentation naming the migration source system

Removal or archival belongs to Phase 3, after a quiet period.
