# Claude to Codex Migration Fidelity Audit

Date: 2026-06-13
Status: in progress

## Why This Audit Exists

Kay flagged that the initial Codex migration did not preserve the full Claude-era `/goodnight` behavior. The first migration audit verified that skills, hooks, timers, and scheduled jobs existed and could run, but it did not fully verify semantic fidelity: whether the full breadth, intent, and operating contracts of the Claude system survived.

This audit upgrades the standard from "present and runnable" to "faithful unless intentionally improved."

## Current Findings

### 1. Good Night was under-migrated

Finding: `.claude/commands/goodnight.md` was a robust daily closeout contract, but Codex initially treated Good Night mostly as `task-tracker-manager carry-forward-day`.

Impact:
- unpushed commits accumulated
- dirty-tree state remained visible but unowned
- multi-thread inventory was not reliably enforced
- zero-trace / memory / calibration reporting could be skipped silently

Corrective action completed:
- Created `.agents/skills/goodnight-closeout/SKILL.md`
- Added `.agents/skills/goodnight-closeout/learnings.md`
- Updated task tracker routing so `task-tracker-manager` owns carry-forward only
- Updated chat recovery and migration docs to route Good Night through `goodnight-closeout`

Remaining action:
- Test the next real Good Night against the preserved Claude checklist.
- Decide whether push should be automatic for reviewed closeout commits on the migration branch or remain explicit until Phase 3.

### 2. Skill folders are present, but semantic diffs need review

Inventory result:
- Claude skill directories: 47
- Codex skill directories: 48
- Missing Codex skill directories: 0
- Codex-only skill directories: `goodnight-closeout`

This means the skill-copy layer exists, but many files intentionally or unintentionally differ. The following high-priority workflows have low-similarity diffs and need semantic review:

| Skill | Risk Surface | Initial Signal |
|---|---|---|
| `conference-discovery` | scheduled Sunday job, Google Sheet mutation, Slack notification | `SKILL.md` and headless prompt differ substantially |
| `deal-aggregator` | high-frequency scheduled deal sourcing | morning/afternoon/friday prompts differ substantially |
| `email-intelligence` | weekday source of morning items | headless prompt differs substantially; email safety must be preserved |
| `jj-operations` / cold-call operations | Sunday cold-call prep; legacy naming transition | skill and headless prompt differ substantially |
| `niche-intelligence` | Tuesday analyst-prep workflow | tracker references and headless prompt differ substantially |
| `post-call-analyzer` | transcript/call analysis and action-item routing | skill and trigger prompt differ substantially |
| `relationship-manager` | weekday relationship cadence | headless prompt differs materially |
| `target-discovery` | Sunday target enrichment and cold-call pool creation | skill, prompt, and Drive references differ materially |
| `health-monitor` | system health and monitoring | skill differs materially |
| `launchd-debugger` | failure diagnosis | skill differs materially |
| `investor-update` | external-facing investor materials | templates/learnings differ materially |

Review standard:
- Confirm which differences are intentional Codex improvements.
- Confirm no Claude-only assumptions, lost validations, missing stop hooks, or weakened output contracts.
- Confirm Kay-specific corrections from Phase 2.5 are present.

### 3. Slash commands were not treated as first-class migration units

Preserved Claude commands:

`calibrate`, `cfo`, `cio`, `cmo`, `commit`, `cpo`, `dashboard`, `gc`, `goodmorning`, `goodnight`, `ideate`, `migrate`, `onboard`, `pickingback`, `push`, `refine`, `savestate`, `socrates`, `start`, `task`, `triage`

Exact Codex-native coverage found:

| Claude Command | Codex Equivalent Status |
|---|---|
| `goodnight` | now covered by `goodnight-closeout` |
| `onboard` | covered by `onboard` skill |
| `socrates` | covered by `socrates` skill |
| `triage` | covered by `triage` skill |
| `start` | intentionally improved by `today`; direct Gmail/MCP scanning and Superhuman outreach from Claude command are not revived |
| `calibrate` | faithful plus improved via `calibration-workflow`; now uses AGENTS-era references and 1Password-first credential handling |
| `migrate` | faithful via `migration-workflow`; preserves detect/preview/apply/validate flow |
| `goodmorning` | repaired by new `goodmorning` skill; pending first live run validation |
| `savestate` | repaired by new `session-checkpoint` skill |
| `pickingback` | repaired by new `session-checkpoint` skill |
| `commit` / `push` | repaired by new `commit-steward` skill; push remains explicit during migration |
| `dashboard` | repaired by new `dashboard-command` skill |
| `cfo`, `cio`, `cmo`, `coo`, `cpo`, `gc` agent commands | repaired by new `c-suite-advisors` skill |
| `ideate`, `refine`, `task` | repaired by new `plan-refinery-command` and `task-command` skills |

This is a primary audit gap. Slash commands need the same treatment as skills because several encoded important operating behavior.

### 4. Hooks exist, but legacy references need classification

Hooks were copied to `.codex/hooks`, and `.codex/hooks.json` exists.

Potentially intentional compatibility:
- `CLAUDE_PROJECT_DIR` exported as an alias inside `.codex/hooks/run-hook.sh`
- `.claude` included in safe staging during the monitoring window
- legacy `CLAUDE.md` reference files retained

Needs review:
- `.codex/hooks/calibration-stats-updater.py` still writes `.claude/stats.yaml`
- `onboard` and `calibration-workflow` still refer to `.claude/stats.yaml` and `.claude/creatures`
- `agent-chatroom` still references `~/.claude/hook-state`
- some hook comments still address "Claude" rather than "Codex"

Classification required:
- keep temporarily for backward compatibility
- rename to neutral/Sapling path
- remove during Phase 3 cleanup

### 5. Scheduled jobs are cut over, but names and references need cleanup

Active systemd timers show Codex-side scheduled jobs running, including:
- `email-intelligence`
- `relationship-manager`
- `deal-aggregator`
- `post-call-analyzer-poll`
- `target-discovery-sunday`
- `cold-call-operations-sunday`
- `conference-discovery`
- `niche-intelligence`
- `nightly-tracker-audit`
- `calibration-workflow`
- `health-monitor`

Notable legacy surfaces:
- `jj-operations-sunday` and `jj-snapshot-refresh` are disabled, replaced by cold-call naming.
- `claude-usage-refresh.timer` is disabled, but service/timer files still exist.
- Docs and some generated templates still mention Claude/launchd/JJ for historical reasons.

Corrective action completed during Phase B:
- Removed active Superhuman wording from `docs/scheduled-skills.md`; email intelligence is Gmail/Granola-based and draft-only.
- Updated active `email-intelligence`, `relationship-manager`, and `outreach-manager` language so current workflows refer to cold-call operations rather than JJ as the operating model.
- Preserved legacy technical identifiers (`jj-operations`, `JJ_CALL_NICHES`, `JJ:*` sheet headers) only where scripts, validators, or existing Google Sheets still depend on them.
- Updated `outreach-manager` to resolve `Outreach Channel` by header name instead of column letters.
- Updated skill-router descriptions so Codex routes cold-call work by current terminology while retaining the legacy skill id until Phase 3 cleanup.

Remaining Phase B classification:
- Review the remaining scheduled/core skill prompts one by one for semantic fidelity, especially `post-call-analyzer`, `target-discovery`, `niche-intelligence`, `conference-discovery`, and `deal-aggregator`.
- Decide whether Phase 3 should rename legacy cold-call artifacts (`jj-operations`, `jj-activity-snapshot.json`, `validate_jj_*`) or keep them as compatibility aliases until downstream dashboards are renamed.

## Audit Plan

### Phase A - Command Fidelity

For each `.claude/commands/*.md`:
1. Summarize the original contract.
2. Identify the Codex equivalent.
3. Mark one of:
   - faithful
   - intentionally improved
   - partially migrated
   - missing
   - obsolete by decision
4. Patch missing/partial commands into repo-backed Codex skills or documented chat workflows.

Priority order:
1. `goodmorning`
2. `savestate`
3. `pickingback`
4. `commit`
5. `dashboard`
6. C-suite agent commands
7. `calibrate`, `start`, `task`, `ideate`, `refine`, `migrate`

Phase A repair status:
- Added `goodmorning` to preserve morning orchestration, day overlays, Sunday tracker safety, cold-call transition, and decisions-only briefing.
- Added `session-checkpoint` to preserve `/savestate` and `/pickingback`.
- Added `commit-steward` to preserve session wrap-up, atomic commit, dirty-tree classification, and explicit push handling.
- Added `dashboard-command` to preserve dashboard link, health check, and one-restart recovery behavior.
- Added `c-suite-advisors` to preserve CFO/CIO/CMO/COO/CPO/GC role contracts without runtime `.claude/agents` calls.
- Added `task-command` to preserve `/task` execution/tracking/decision-trace behavior.
- Added `plan-refinery-command` to preserve `/ideate` and `/refine` routing while using the existing `plan-refinery` skill.

Remaining Phase A review:
- First live-run validation still needed for `goodmorning` and `goodnight-closeout`, because those are high-value daily bookends.
- Continue watching whether old `/start` users should be redirected to `goodmorning` instead of `today` for daily operating briefings.

### Phase B - Scheduled/Core Skill Fidelity

For each scheduled/core skill:
1. Compare Claude vs Codex `SKILL.md`.
2. Compare headless prompts.
3. Confirm every stop hook / validation / artifact contract survived.
4. Confirm every Phase 2.5 improvement is present.
5. Confirm email-sending prohibition and 1Password credential routing.
6. Record whether differences are faithful, intentional improvement, or gap.

Priority order:
1. email-intelligence
2. deal-aggregator
3. conference-discovery
4. post-call-analyzer
5. target-discovery
6. cold-call operations / jj-operations
7. niche-intelligence
8. relationship-manager
9. health-monitor / launchd-debugger
10. weekly/nightly tracker workflows

### Phase C - Hook and Runtime Fidelity

1. Compare `.claude/hooks` against `.codex/hooks`.
2. Validate every must-have safety hook still fires in Codex.
3. Classify legacy path references.
4. Move durable state from `.claude/*` to neutral `.config/sapling` or `.codex/*` paths where appropriate.
5. Record Phase 3 cleanup actions.

### Phase D - Final Confidence Gate

Before Phase 3 cleanup:
- all command contracts classified
- all scheduled/core skills reviewed
- all active scheduled jobs have Codex replacements
- no required workflow depends on active Claude Code usage
- residual Claude artifacts are either preserved archives or explicitly marked for removal

## Current Recommendation

Pause broad Phase 3 cleanup until this fidelity audit is complete. Continue to keep Claude scheduled launches off where Codex replacements are validated, but do not delete preserved Claude command/skill artifacts until we finish semantic comparison.
