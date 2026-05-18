---
schema_version: 1.1.0
date: 2026-05-17
type: trace
title: "Don't add an agent to babysit unreliable plumbing — fix feeds + loud validators"
trace_type: architecture
tags: ["date/2026-05-17", "trace", "topic/dashboard", "topic/dashboard-infra-fix", "topic/agents-vs-plumbing", "topic/weekly-tracker"]
---

# Don't add an agent to babysit unreliable plumbing — fix feeds + loud validators

## Trigger

Full 7-page dashboard diagnostic found every gap traced to one root-cause class: macOS-on-Linux assumptions on a systemd VPS, proprietary feeds never wired (DealsX/conferences), and operator YAML mistaken for live data. The instinct on the table was a dedicated dashboard-maintenance agent to keep it healthy. A parallel proposal: repoint the dashboard to the weekly-tracker Google Sheet as system of record.

## Decision

**REJECT** a dedicated dashboard-maintenance agent. **REJECT** repointing to the weekly-tracker sheet. Instead: wire the missing feeds, harden validators to fail loud on unexpected zeros, and sweep the macOS-isms. No new agent, no sheet-source rebuild, no architecture change.

## Alternatives considered

1. **Dedicated maintenance agent** — rejected. An agent polling a broken pipeline masks the root cause and adds a layer that itself needs babysitting. Agents don't make unreliable plumbing reliable; they hide that it isn't.
2. **Repoint dashboard to the weekly-tracker Google Sheet** — rejected. The M&A Analytics page already implements a working 9-snapshot weekly vault/Attio archive. The sheet was never populated because `weekly-tracker` never ran. Rebuilding a sheet-source layer duplicates working infrastructure to feed a consumer that already has a working source. (This is why Task 12 leans retire-not-revive weekly-tracker.)
3. **Fix feeds + loud validators + macOS-ism sweep** — chosen. Eliminates the root-cause class instead of layering over it. Validators that fail (exit 1) on the false-zero signature trip launchd-debugger instead of serving a week of silently bad data.

## Reasoning

The JJ false-zero (every scheduled run 5/13→5/15 returned exit 0 with `OAuth refresh failed`, validator said "OK") is the canonical lesson: the failure wasn't missing supervision, it was a validator that didn't fail loud. Adding an agent on top would have inherited the same silent-success blindness. Per Harrison's wrapper-validator doctrine — verify the deliverable in a fresh process, don't trust the producer's exit code. Reliability comes from loud validators at the run boundary, not from an observer agent.

## Why this trace matters

When a dashboard/pipeline "looks unreliable," the tempting fix is a supervisory agent or a parallel system-of-record. Both add surface area and hide root cause. A future agent should first ask: *is a feed unwired, a validator silent, or a platform assumption wrong?* Fix that. Reserve agents for judgment, not for plumbing reliability.

## Key insight

Agents don't fix unreliable plumbing — loud validators do. Don't rebuild around dead infrastructure (weekly-tracker sheet); retire it and harden the working path.
