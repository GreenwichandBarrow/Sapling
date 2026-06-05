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
13. Neutralize legacy migration-specific naming in future migrations where practical.

## Migration Matrix

Status values: `pending`, `ported`, `validated`, `cutover`, `blocked`.

| Workflow / Component | Source | Codex Target | Tier | Status | Notes |
| --- | --- | --- | --- | --- | --- |
| Doctrine | `CLAUDE.md` | `AGENTS.md` | 1 | ported | Direct port with runtime terminology adapted. |
| Skills | `.claude/skills` | `.agents/skills` | 1/2/3 | ported | Full copy; tiering still evidence-based. |
| Hooks | `.claude/hooks` + `.claude/settings.json` | `.codex/hooks` + `.codex/hooks.json` | 1 | ported | Must-have safety hooks copied; requires Codex hook validation/trust. |
| Codex env | `scripts/.env.launchd` | `scripts/.env.codex` | 1 | validated | 1Password reference resolves; read-only Codex smoke test completed successfully. |
| Runner | `scripts/run-skill.sh` | `scripts/run-agent-skill.sh` | 1 | ported | New runner created; old runner preserved. |
| calibration-workflow | systemd + `run-skill.sh calibration-workflow` | `run-agent-skill.sh calibration-workflow` | 1 | cutover | Codex pilot wrote `brain/outputs/calibrations/2026-06-05-codex-calibration.md`, validator passed, and live service now uses `run-agent-skill.sh`. |
| conference-discovery | systemd + headless Sunday prompt | `run-agent-skill.sh conference-discovery sunday` | 1 | cutover | Prior run validator passed for 2026-05-31 after validator timeout hardening; live service now uses `run-agent-skill.sh`. Observe Sunday 2026-06-07 Codex run. |
| deal-aggregator cluster | morning/afternoon/friday timers + headless prompts | `run-agent-skill.sh deal-aggregator` variants | 1 | cutover | Morning Codex pilot wrote the daily artifact, posted 1 new deal, passed validator, and all three live services now use `run-agent-skill.sh`. |
| email-intelligence | weekday timer + headless prompt | `run-agent-skill.sh email-intelligence` | 1 | cutover | Codex pilot completed with no send path used, wrote `brain/context/email-scan-results-2026-06-05.md`, passed `validate_email_intelligence_integrity.py`, and live systemd service now uses `run-agent-skill.sh`. |
| health-monitor | weekly timer | `run-agent-skill.sh health-monitor` | 1 | cutover | Codex pilot completed, wrote `brain/trackers/health/2026-06-04-health.md`, validated artifact, posted Slack per RED/YELLOW rule, and live systemd service now uses `run-agent-skill.sh`. |
| jj-operations | Sunday timer + headless prompt | `run-agent-skill.sh jj-operations:sunday-prep` | 1 | cutover | Validator passed against week of 2026-06-01; live service now uses `run-agent-skill.sh`. Observe Sunday 2026-06-07 Codex run. |
| launchd-debugger | daily/on-failure prompts | `run-agent-skill.sh launchd-debugger` variants | 1 | cutover | Daily Codex pilot completed after scanner hardening; live systemd service now uses `run-agent-skill.sh`. |
| niche-intelligence | Tuesday timer + headless prompt | `run-agent-skill.sh niche-intelligence:tuesday` | 1 | cutover | Prior run validator passed for 2026-06-02; live service now uses `run-agent-skill.sh` with explicit date validation. `last30days` GitHub skill dependency is copied into `~/.codex/skills/last30days`. |
| nightly-tracker-audit | nightly timer + prompt | `run-agent-skill.sh nightly-tracker-audit:nightly` | 1 | cutover | Codex validation completed after runner inherited `op-env.sh`; live systemd service now uses `run-agent-skill.sh`. |
| post-call-analyzer | poll script + triggered prompt | `run-agent-skill.sh post-call-analyzer:on-trigger` | 1 | cutover | Codex poller pilot completed with 0 queued notes; live poll service now uses `post_call_analyzer_poll.codex.sh`. Analyzer trigger has Codex prompt/validator coverage but did not run on a fresh queued note during the pilot. |
| relationship-manager | weekday timer + prompt | `run-agent-skill.sh relationship-manager:daily` | 1 | cutover | Claude run passed on 2026-06-05; Codex runner now has same-day idempotency skip for valid artifacts; live service uses `run-agent-skill.sh relationship-manager:daily`. |
| target-discovery | Sunday timer + prompt | `run-agent-skill.sh target-discovery phase2-sunday` | 1 | cutover | Validator moved to `.codex/hooks`, uses pool-only check with explicit `--date`, and passed against 2026-05-31 pool; live service now uses `run-agent-skill.sh`. |
| Direct script refresh jobs | refresh/probe/export/snapshot scripts | unchanged initially | 1 | pending | Apollo, Attio, JJ snapshot, external probe, weekly export, and weekly snapshot appear agent-free. |
| post-call-analyzer poll | `scripts/post_call_analyzer_poll.sh` -> `scripts/run-skill.sh post-call-analyzer:on-trigger` | `scripts/post_call_analyzer_poll.codex.sh` -> `run-agent-skill.sh post-call-analyzer:on-trigger` | 1 | cutover | Live poll service now uses the Codex poller; zero-queue pilot passed. Fresh queued-note analyzer run still needs observation. |
| Readiness checker | n/a | `scripts/check-codex-migration-readiness.sh` | 1 | ported | Non-live gate for syntax, hooks, Codex CLI, 1Password key resolution, and synthetic safety checks. |
| Systemd cutover templates | live user units | `docs/migrations/systemd-codex-templates/README.md` | 1 | ported | Non-live service mapping and controlled cutover procedure; no timers modified yet. |
| post-call analyzer Codex poller | `scripts/post_call_analyzer_poll.sh` | `scripts/post_call_analyzer_poll.codex.sh` | 1 | ported | Parallel variant launches `run-agent-skill.sh`; live service unchanged until validation. |
| Systemd cutover tool | live user units | `scripts/prepare-codex-systemd-cutover.sh` | 1 | ported | Supports dry-run generation and guarded `--apply` by workflow group; refuses apply if readiness fails. |
| Scheduled prompt/validator coverage | old runner + systemd `POST_RUN_CHECK` | runner defaults + readiness checks | 1 | ported | Known scheduled headless prompts and validators are checked before cutover; runner has defaults for manual validation safety. |
| Email no-send audit | migrated skill docs/scripts | `scripts/audit-email-no-send.sh` | 1 | ported | Blocks executable-looking Gmail send commands while allowing draft-only policy text. |
| Phase 1 inventory | live VPS skills/hooks/timers/cron/MCP/config | `docs/migrations/2026-06-04-phase1-inventory.md` | 1 | ported | Comprehensive inventory created before further cutovers. |
| Failure scanner | `scripts/scan_launchd_failures.py` | Codex-aware scheduler failure scan | 1 | validated | Anchored real wrapper markers, detects Codex runner failures, and ignores resolved older failures after newer success logs. |

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
- `scripts/check-codex-migration-readiness.sh` created as a non-secret readiness gate.
- `docs/migrations/systemd-codex-templates/README.md` created with non-live cutover mapping.
- `scripts/post_call_analyzer_poll.codex.sh` created as a non-live Codex trigger variant.
- `scripts/prepare-codex-systemd-cutover.sh` created to generate dry-run service variants and later apply validated workflow groups only.
- Runner smoke test blocks safely before `codex exec` when `CODEX_API_KEY` is unresolved.
- Runner uses the supported `codex exec --dangerously-bypass-approvals-and-sandbox` flag for Phase 1 broad permissions on this VPS Codex build.
- Runner email-send scan is scoped to the active skill and known email-adjacent trigger scripts to avoid false positives from unrelated legacy scripts.
- Runner now defaults known scheduled workflow validators for manual Codex runs even when systemd has not injected `POST_RUN_CHECK`.
- Readiness checker verifies known scheduled headless prompt files and validator files exist.
- `gogcli` migrated reference docs no longer include email-send examples; draft-only examples remain.
- `scripts/audit-email-no-send.sh` added as a durable no-send scan for migrated skills/scripts.
- `docs/migrations/2026-06-04-phase1-inventory.md` added with the live VPS skills, hooks, timers, cron, MCP/config, and remaining Claude-runner surfaces.

## Current Blockers

1. `calibration-workflow` needs a dedicated headless prompt and durable-output validator before Codex cutover; leave it on Claude temporarily.
2. `post-call-analyzer-poll.service` must not be cut over until the Codex poller variant and analyzer workflow are tested as one cluster.
3. `target-discovery-sunday` has a recurring validator race noted by the Codex health-monitor pilot; resolve or add a deterministic validation path before Codex cutover.

## Safety Validation

- Email-send hook synthetic test: `gog gmail send ...` is denied.
- Secret-file hook synthetic test: `cat scripts/.env.launchd` is denied.
- Runner email safety scan blocks potential send paths before `codex exec`.
- Runner kill switch path: `~/.config/sapling/disable-codex-scheduled`.
- `scripts/check-codex-migration-readiness.sh` currently reports `CODEX_API_KEY` unresolved; this is expected until the 1Password item exists.
- `scripts/prepare-codex-systemd-cutover.sh --apply` refuses live service edits while readiness fails.
- Systemd dry-run generated Codex service variants under `docs/migrations/systemd-codex-templates/generated/` without modifying live units.
- `prepare-codex-systemd-cutover.sh --apply --group health-monitor` was tested while readiness failed and correctly refused to edit `~/.config/systemd/user/health-monitor.service`.
- Email no-send audit passes after removing executable send examples from migrated `gogcli` references.
- `scripts/check-codex-migration-readiness.sh` passed after `CODEX_API_KEY` was moved to `op://GB Server/OpenAI API Key/password`.
- Read-only `codex exec` smoke test completed successfully and returned project name `Sapling OS`.
- Migrated `.agents/skills/create-skill/SKILL.md` frontmatter was fixed so Codex no longer logs an invalid YAML startup warning.
- `health-monitor` Codex production pilot completed successfully at 2026-06-04 22:40 EDT.
- `health-monitor` artifact validation passed for `brain/trackers/health/2026-06-04-health.md` and `brain/traces/agents/2026-06-04-health-monitor.md`.
- `health-monitor.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh health-monitor`; rollback is the `.pre-codex-*` backup in `~/.config/systemd/user` or the pre-migration backup snapshot.
- Comprehensive inventory confirms 46 migrated skills, copied Codex hooks, 21 user systemd timers, one unrelated user cron cleanup job, no active repo-level MCP config, and three live Codex-cutover services (`health-monitor`, `nightly-tracker-audit`, and `launchd-debugger`).
- `nightly-tracker-audit` Codex production validation completed successfully at 2026-06-04 23:40 EDT after `scripts/run-agent-skill.sh` was fixed to source `scripts/op-env.sh` for wrapper-level validators.
- `nightly-tracker-audit.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh nightly-tracker-audit:nightly`; timer was unchanged.

## Rollback Policy

- Preserve `.claude`, `CLAUDE.md`, and `scripts/run-skill.sh` during Phase 1.
- Per workflow/cluster, rollback by restoring service files from the backup snapshot and running `systemctl --user daemon-reload`.
- Blocked workflows remain on Claude until resolved.

## Completion Criteria

- Codex-native doctrine, skills, prompts, MCP/config, runner, 1Password auth, must-have hooks/stop hooks or runner safety checks, validation matrix, cutover notes, blockers, and rollback docs are in place.
- Validated workflows/clusters are cut over to Codex.
- Failed workflows remain safely on Claude temporarily with blocker notes.
- Claude files are preserved, not deleted.

## Overnight Phase 1 Notes - 2026-06-05

- `launchd-debugger` Codex pilot initially exposed a false-positive scanner bug: legacy documentation text inside Codex JSON logs could match loose `PREFLIGHT FAILED` detection, and an older failed retry could remain visible after a newer success. `scripts/scan_launchd_failures.py` now anchors real wrapper markers, detects Codex runner failure lines, and treats only the newest log per job as current state.
- `launchd-debugger` clean Codex pilot completed at 2026-06-05 02:59 EDT with 0 failures, no Slack post, and validator pass.
- `launchd-debugger.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh launchd-debugger:daily`; timer was unchanged.
- `deal-aggregator` Codex morning pilot completed at 2026-06-05 03:15 EDT, wrote `brain/context/deal-aggregator-scan-2026-06-05.md`, posted 1 new Website Closers match to Slack, added its fingerprint, and passed `validate_deal_aggregator_integrity.py`.
- `deal-aggregator.service`, `deal-aggregator-afternoon.service`, and `deal-aggregator-friday.service` live systemd `ExecStart` values now point to `scripts/run-agent-skill.sh`; timers were unchanged.
- `email-intelligence` Codex pilot completed at 2026-06-05 03:49 EDT, wrote `brain/context/email-scan-results-2026-06-05.md`, scanned Gmail drafts without sending, found no CIM/NDA/active-deal fast-path triggers, found no auto-draft trigger, and passed `validate_email_intelligence_integrity.py`.
- `email-intelligence.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh email-intelligence`; timer was unchanged.
- `scripts/run-agent-skill.sh` email-send preflight now ignores explicit prohibition/policy prose such as `NEVER call gog gmail send`, while still blocking executable-looking send paths.
- `post_call_analyzer_poll.codex.sh` pilot completed at 2026-06-05 03:52 EDT with 0 queued Granola notes and no analyzer side effects.
- `post-call-analyzer-poll.service` live systemd `ExecStart` now points to `scripts/post_call_analyzer_poll.codex.sh`; timer was unchanged. Analyzer execution remains protected by `run-agent-skill.sh post-call-analyzer:on-trigger` and `validate_post_call_analyzer_integrity.py`, but a fresh queued-note Codex analyzer run did not occur during this pilot.


## Overnight Phase 1 Handoff - 2026-06-05 03:55 EDT

### Live on Codex runner paths

- `health-monitor.service`
- `nightly-tracker-audit.service`
- `launchd-debugger.service`
- `email-intelligence.service`
- `deal-aggregator.service`
- `deal-aggregator-afternoon.service`
- `deal-aggregator-friday.service`
- `post-call-analyzer-poll.service` (poller on Codex variant; analyzer fires through `run-agent-skill.sh post-call-analyzer:on-trigger` only when queued notes exist)

### Intentionally left on Claude for safety

- None among agent scheduled services after the calibration-workflow Codex cutover on 2026-06-05. Legacy Claude files remain preserved for rollback until Phase 3.

### Deferred to Phase 2 / Phase 3

- Phase 2: revise migrated skills for Codex-native execution improvements after faithful migration is stable.
- Phase 2: observe a fresh queued-note Codex post-call-analyzer run, not just a zero-queue poller run.
- Phase 3: remove or archive Claude Code runtime files only after the Codex scheduled system has passed enough live cycles.


## Morning Phase 1 Closeout - 2026-06-05

- Morning scheduled artifacts were reviewed and committed, including `brain/trackers/weekly/2026-06-05-deal-aggregator-digest.md` and refreshed snapshot JSON files.
- `relationship-manager` ran successfully on Claude at 2026-06-05 06:50 EDT and passed `validate_relationship_manager_integrity.py` for `brain/context/relationship-status-2026-06-05.md`.
- `scripts/run-agent-skill.sh` now has a same-day idempotency gate for `relationship-manager:daily`: if the current date artifact exists and validates, Codex skips rather than duplicating Attio/vault writes. A supervised rerun can set `RELATIONSHIP_MANAGER_ALLOW_RERUN=1`.
- `relationship-manager.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh relationship-manager:daily`; the next scheduled live Codex run is Monday 2026-06-08 06:50 EDT.


## Sunday Cluster Cutover - 2026-06-05

- `scripts/validate_phase2_integrity.py` now calls `.codex/hooks/enrichment_integrity_check.py`, runs the `--pool-only` enrichment check, and accepts `--date YYYY-MM-DD` for deterministic scheduled validation.
- `scripts/run-agent-skill.sh` now passes `--date "$TODAY"` to the target-discovery Phase 2 post-run validator.
- Regression validation passed against the prior Sunday pool: `python3 scripts/validate_phase2_integrity.py --date 2026-05-31` returned PASS for Premium Pest Management.
- JJ tab validation passed for the prior completed week: `python3 scripts/validate_jj_operations_integrity.py --week-start 2026-06-01` verified all five Call Log tabs and populated owner names.
- `target-discovery-sunday.service` and `jj-operations-sunday.service` live systemd `ExecStart` values now point to Codex runner paths. Timers were unchanged. Next live Codex observation window is Sunday 2026-06-07.


## Conference Discovery Cutover - 2026-06-05

- `scripts/validate_conference_discovery_integrity.py` now gives the live Pipeline sheet read a 90-second timeout and retries once, matching observed `gog` cold-cache behavior.
- Regression validation passed against `conference-pipeline-pre-run-2026-05-31.json`: row-count delta, header positions, cell mutations, and authorized statuses all passed.
- `conference-discovery.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh conference-discovery sunday`. Timer was unchanged. Next live Codex observation window is Sunday 2026-06-07 21:00 EDT.


## Niche Intelligence Cutover - 2026-06-05

- Regression validation passed against the 2026-06-02 niche-intelligence artifacts: markdown report and JSON sidecar both satisfy `validate_niche_intelligence_integrity.py`.
- `scripts/run-agent-skill.sh` now passes `--date "$TODAY"` to the niche-intelligence post-run validator.
- `niche-intelligence.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh niche-intelligence:tuesday`. Timer was unchanged. Next live Codex observation window is Tuesday 2026-06-09 22:30 EDT.
- The `last30days` GitHub skill dependency (`https://github.com/mvanhorn/last30days-skill`, commit `850c7e0`) was copied from `~/.claude/skills/last30days` to `~/.codex/skills/last30days`. Readiness now verifies the Codex copy exists.


## External Skill Dependency Migration - 2026-06-05

- `last30days` was not a repo-local Sapling skill; it was an external GitHub-backed skill installed at `~/.claude/skills/last30days` from `https://github.com/mvanhorn/last30days-skill`.
- It has now been copied to `~/.codex/skills/last30days` at commit `850c7e0`, preserving the GitHub remote.
- `scripts/check-codex-migration-readiness.sh` now fails if the Codex-side `last30days` skill or `scripts/last30days.py` entrypoint is missing.
- Phase 2 cleanup: update niche-intelligence internals to prefer the Codex path directly where they currently mention the legacy Claude path.


## External GitHub Skill Audit - 2026-06-05

- Audited personal skill directories under `~/.claude/skills` and `~/.codex/skills` for Git remotes. Only `last30days` had a GitHub remote on the VPS.
- Audited repo-local `.claude/skills` and `.agents/skills` for nested `.git` directories; none were found. Repo-local GitHub-provenance skills such as `evolve` and `create-skill` were already copied as part of the Sapling `.claude/skills` -> `.agents/skills` migration.
- Updated the active Codex niche-intelligence sub-agent reference to call `~/.codex/skills/last30days/skills/last30days/scripts/last30days.py` instead of a non-existent `~/.agents/skills/last30days` path.


## Calibration Workflow Codex Port - 2026-06-05

- Added `.agents/skills/calibration-workflow/headless-weekly-prompt.md` for non-interactive Codex runs. The Phase 1 scheduled mode writes a durable report and does not wait for approval.
- Added `scripts/validate_calibration_workflow_integrity.py` to require the dated Codex calibration report, required headings, Codex runtime frontmatter, and explicit safety notes.
- Added calibration-workflow prompt/validator coverage to `scripts/run-agent-skill.sh` and `scripts/check-codex-migration-readiness.sh`.
- Phase 1 policy for this workflow: report-first/proposal-only. Direct skill, hook, memory, and script improvements move to Phase 2 unless they are required for the headless run itself.
- Codex pilot completed at 2026-06-05 11:53 EDT and passed `scripts/validate_calibration_workflow_integrity.py --date 2026-06-05`.
- `calibration-workflow.service` live systemd `ExecStart` now points to `scripts/run-agent-skill.sh calibration-workflow`; timer was unchanged.

## Phase 2 Hardening Checkpoint - 2026-06-05

- Added focused unit coverage for every `scripts/validate_*_integrity.py` validator; the Phase 2 regression bundle now covers scheduled artifact shape, REST snapshot contracts, no-send email safety, conference status mutation safety, JJ call-log integrity, calibration report autonomy, and post-call analyzer ledger shape.
- Updated active scheduled-skill documentation and validator wording to reference `scripts/run-agent-skill.sh` / `codex exec` where live Codex services now use those paths. Historical Claude failure-mode notes and preserved rollback files remain untouched until Phase 3.
- Ported `scripts/health-monitor-red-bridge.sh` to VPS Codex semantics (`~/projects/Sapling` default and `scripts/run-agent-skill.sh` child runner), and added the health-monitor RED bridge block to `scripts/run-agent-skill.sh`. Live observation is still needed on the next health-monitor cycle.
