---
schema_version: 1.1.0
date: 2026-05-16
type: trace
today: "[[notes/daily/2026-05-16]]"
task: Diagnose apparent gog/1Password auth outage blocking the morning workflow
output: "[[context/session-decisions-2026-05-16]]"
had_human_override: true
tags: [date/2026-05-16, trace, topic/gog-false-alarm, topic/op-1password-resolution, pattern/test-real-path-before-escalating]
---

# Decision Trace: gog "Outage" Was a Local-Shell Test Artifact

## Context
Morning signal-gathering hit `no TTY available for keyring file backend password prompt`. A briefing was issued declaring gog/Gmail/Calendar/Sheets down, op:// resolution broken, and all 7 scheduled-job secrets unreachable — escalated as a 🔴 credential incident. Kay pushed back twice ("you're already using Attio/Apollo/Slack", "you have it already"), which exposed the flaw.

## Decisions

### How to verify an auth outage before escalating
**AI proposed:** `op whoami` in the interactive shell → 0 accounts → conclude system-wide op failure, escalate.
**Chosen (after Kay pushback):** run the *actual* path scheduled jobs use — `. ~/.config/op-sa-token.env; source scripts/load-env.sh; load_env scripts/.env.launchd` — then test `op inject` + a value-suppressed `gog calendar`.
**Result:** all exit 0. SA token valid, scoped to GB Server. The "outage" existed only in the interactive shell, which does not source the systemd `EnvironmentFile`. One real, isolated bug: `export-weekly-archive-to-sheet.sh` was the lone wrapper bypassing the `run-skill.sh` resolution pattern.
**Reasoning:** the interactive shell and the scheduled-job environment are different credential contexts; testing one says nothing about the other.
**Pattern:** #pattern/test-real-path-before-escalating

## Alternatives Considered
- Trust `op whoami` and provision a new service account (would have been wasted — token already valid)
- Ask Kay to interactively `op signin` (declined by Kay; unnecessary)
- Continue blocking the morning workflow on a false premise (12 min lost before correction)

## Why This Trace Matters
A future agent seeing the keyring-prompt error will, by default, repeat the same false escalation. The interactive shell on this VPS never sources `~/.config/op-sa-token.env`; scheduled jobs do via systemd `EnvironmentFile=%h/.config/op-sa-token.env`. The 1Password SA architecture is sound — verify through the scheduled path, not a bare shell, before declaring an auth outage.

## Key Insight
Before declaring gog/op/1Password down: reproduce through the scheduled resolution path (`. ~/.config/op-sa-token.env` → `load-env.sh` → `load_env scripts/.env.launchd`), not an interactive `op whoami`. A failing bare shell is the expected state, not an incident.
