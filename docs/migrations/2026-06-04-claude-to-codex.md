# Claude Code to Codex Migration - Phase 1

Date: 2026-06-04
Host: agent-vps-7731c88b
Project: `~/projects/Sapling`

## Program Phases

1. **Phase 1 - Faithful Migration:** preserve behavior while moving from Claude Code to Codex.
2. **Phase 2 - Codex-Native Improvement:** improve migrated skills, orchestration, permissions, validation, and cost/model routing after stability.
3. **Phase 3 - Claude Code Cleanup:** after a quiet period, archive or remove expired Claude Code artifacts and fallback paths.

## Decisions

- Scope: migrate scheduled jobs and interactive Sapling workflows.
- Doctrine: port `CLAUDE.md` directly to `AGENTS.md` first; refine later.
- Runner: create a neutral `scripts/run-agent-skill.sh` with `AGENT_RUNTIME=codex`.
- Skills: migrate all `.claude/skills` to `.agents/skills`; validate scheduled/core workflows first.
- Headless prompts: preserve separate headless prompt files.
- Auth: scheduled jobs use `CODEX_API_KEY` resolved through 1Password only.
- Permissions: broad during migration; tighten after validation.
- MCP: migrate config, but scheduled jobs do not depend on MCP until tested.
- Hooks: must-have safety hooks/stop hooks before cutover; nice-to-have hooks later.
- Cutover: test manually first; update live systemd services in a controlled final step.
- Dependencies: cut over material dependency clusters together.
- Email: never send email. Drafts only when verified draft-only.
- Slack: failures/blockers only during migration.
- Backups: pre-migration snapshot created before edits.
- Git: logical commits, no push unless explicitly requested.

## Backup Snapshot

- `/home/ubuntu/backups/claude-to-codex-20260604-161906`

## Deferred / Follow-Up

1. Refine `AGENTS.md` after direct port works.
2. Add nested `AGENTS.md` files later if useful.
3. Tighten scheduled-job permissions after validation.
4. Consolidate headless prompts into `SKILL.md` later if useful.
5. Deep-validate rare/archive skills after core jobs are green.
6. Make scheduled jobs depend on MCP only after MCP paths are tested.
7. Port nice-to-have hooks after safety hooks and scheduled jobs are stable.
8. Failed scheduled jobs, if any, remain on Claude temporarily and get blocker notes.
9. Delete/archive Claude files only after a quiet period.
10. Optimize per-job Codex model routing/cost after migration.
11. Revise migrated skills after cutover to take advantage of Codex-native capabilities.
12. Post-migration cleanup phase for obsolete Claude-era artifacts.

## Migration Matrix

Status values: `pending`, `ported`, `validated`, `cutover`, `blocked`.

| Workflow / Component | Source | Codex Target | Tier | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Doctrine | `CLAUDE.md` | `AGENTS.md` | 1 | ported | Direct port with runtime terminology adapted. |
| Skills | `.claude/skills` | `.agents/skills` | 1/2/3 | ported | Full copy; tiering still evidence-based. |
| Hooks | `.claude/hooks` + `.claude/settings.json` | `.codex/hooks` + `.codex/hooks.json` | 1 | ported | Must-have safety hooks copied; requires Codex hook validation/trust. |
| Codex env | `scripts/.env.launchd` | `scripts/.env.codex` | 1 | blocked | Placeholder `CODEX_API_KEY` op reference needs confirmed 1Password item/field. |
| Runner | `scripts/run-skill.sh` | `scripts/run-agent-skill.sh` | 1 | ported | New runner created; old runner preserved. |
| calibration-workflow | systemd + `run-skill.sh calibration-workflow` | `run-agent-skill.sh calibration-workflow` | 1 | pending | Active timer Thu 23:00. |
| conference-discovery | systemd + headless Sunday prompt | `run-agent-skill.sh conference-discovery sunday` | 1 | pending | Active timer Sun 21:00; validator exists. |
| deal-aggregator cluster | morning/afternoon/friday timers + headless prompts | `run-agent-skill.sh deal-aggregator` variants | 1 | pending | Material cluster; validators exist. |
| email-intelligence | weekday timer + headless prompt | `run-agent-skill.sh email-intelligence` | 1 | pending | Email-adjacent; must verify draft-only/no send before validation. |
| health-monitor | weekly timer | `run-agent-skill.sh health-monitor` | 1 | pending | Pilot candidate. |
| jj-operations | Sunday timer + headless prompt | `run-agent-skill.sh jj-operations:sunday-prep` | 1 | pending | Validator exists. |
| launchd-debugger | daily/on-failure prompts | `run-agent-skill.sh launchd-debugger` variants | 1 | pending | Name retained for workflow history; runner says Codex. |
| niche-intelligence | Tuesday timer + headless prompt | `run-agent-skill.sh niche-intelligence:tuesday` | 1 | pending | Validator exists; dependency on last30days noted in old runner. |
| nightly-tracker-audit | nightly timer + prompt | `run-agent-skill.sh nightly-tracker-audit:nightly` | 1 | pending | Validator exists. |
| post-call-analyzer | poll script + triggered prompt | `run-agent-skill.sh post-call-analyzer:on-trigger` | 1 | pending | Email-adjacent; verify no send. |
| relationship-manager | weekday timer + prompt | `run-agent-skill.sh relationship-manager:daily` | 1 | pending | Validator exists. |
| target-discovery | Sunday timer + prompt | `run-agent-skill.sh target-discovery phase2-sunday` | 1 | pending | Validator exists; JJ dependency. |
| Direct script refresh jobs | refresh/probe/export/snapshot scripts | unchanged initially | 1 | pending | Apollo, Attio, JJ snapshot, external probe, weekly export, and weekly snapshot appear agent-free. |
| post-call-analyzer poll | `scripts/post_call_analyzer_poll.sh` -> `scripts/run-skill.sh post-call-analyzer:on-trigger` | Codex poll trigger or updated script to call `run-agent-skill.sh` | 1 | pending | This direct script still triggers Claude runner internally; cut over with post-call analyzer cluster. |

## Safety Requirements

- Never send email.
- Email draft workflows require explicit draft-only verification before validation.
- `CODEX_API_KEY` must resolve through 1Password at runtime.
- `~/.config/sapling/disable-codex-scheduled` disables Codex scheduled jobs only.
- Safety hooks are copied for interactive use; scheduled jobs also enforce key safety checks inside the runner.

## Bootstrap Status

- Backup created: `/home/ubuntu/backups/claude-to-codex-20260604-161906`.
- `AGENTS.md` created from `CLAUDE.md` with obvious runtime terminology adapted.
- `.agents/skills` created from `.claude/skills`.
- `.codex/hooks` created from `.claude/hooks`.
- `.codex/hooks.json` created with a wrapper script at `.codex/hooks/run-hook.sh`.
- `scripts/.env.codex` created with a placeholder 1Password reference for `CODEX_API_KEY`.
- `scripts/run-agent-skill.sh` created as a neutral runner with `AGENT_RUNTIME=codex`.
- Runner smoke test blocks safely before `codex exec` when `CODEX_API_KEY` is unresolved.
- Runner uses the supported `codex exec --dangerously-bypass-approvals-and-sandbox` flag for Phase 1 broad permissions on this VPS Codex build.
- Runner email-send scan is scoped to the active skill and known email-adjacent trigger scripts to avoid false positives from unrelated legacy scripts.

## Current Blockers

1. Confirm/create the 1Password item referenced by `scripts/.env.codex`:
   - Vault: `GB Server`
   - Item: `OpenAI API Key`
   - Field: `credential`
   - Expected env reference: `op://GB Server/OpenAI API Key/credential`
2. Real Codex validation and systemd cutover cannot proceed until `CODEX_API_KEY` resolves.

## Safety Validation

- Email-send hook synthetic test: `gog gmail send ...` is denied.
- Secret-file hook synthetic test: `cat scripts/.env.launchd` is denied.
- Runner email safety scan blocks potential send paths before `codex exec`.
- Runner kill switch path: `~/.config/sapling/disable-codex-scheduled`.

## Rollback Policy

- Preserve `.claude`, `CLAUDE.md`, and `scripts/run-skill.sh` during Phase 1.
- Per workflow/cluster, rollback by restoring service files from the backup snapshot and running `systemctl --user daemon-reload`.
- Blocked workflows remain on Claude until resolved.

## Completion Criteria

- Codex-native doctrine, skills, prompts, MCP/config, runner, 1Password auth, must-have hooks/stop hooks or runner safety checks, validation matrix, cutover notes, blockers, and rollback docs are in place.
- Validated workflows/clusters are cut over to Codex.
- Failed workflows remain safely on Claude temporarily with blocker notes.
- Claude files are preserved, not deleted.
