# Phase 3 Readiness - Claude to Codex

Date: 2026-06-14
Status: ready for billing downgrade decision; deletion deferred

## Purpose

Phase 3 is the cleanup phase after the Claude Code to Codex migration. The
near-term business decision is whether Kay can lower Claude Code billing before
new Claude pricing takes effect on 2026-06-15.

This note separates that billing decision from irreversible cleanup. The system
can stop relying on Claude for scheduled operations while preserving Claude
context and migration history as an archive.

## Current Runtime Finding

No active Claude scheduled runtime was found.

Verified on 2026-06-14:

- Codex/systemd scheduled jobs are active.
- Codex app-server processes are running on the VPS.
- `claude-usage-refresh.timer` is loaded but disabled and inactive.
- No active user timers matching Claude/Anthropic were listed.
- Claude files remain in the repository as historical and compatibility
  artifacts, not as active scheduled operations.

## Billing Recommendation

Kay can lower the Claude Code plan from the operations perspective, assuming no
separate human-only Claude workflow requires the current plan.

Do not delete Claude repo artifacts today. Downgrading billing and deleting
historical migration context are separate decisions.

## Keep Indefinitely For Now

These items should remain available as archive/reference even after downgrade:

- `.claude/**`
- `CLAUDE.md`
- migration docs under `docs/migrations/`
- Claude-era command and skill definitions used for fidelity comparison
- prior launchd/systemd migration notes
- historical memory entries about Claude pricing, usage, and migration rationale

Reason: these files are useful for audit, rollback understanding, and checking
whether Codex skills preserved the full Claude-era operating intent.

## Do Not Remove Yet

Do not remove these until after the billing downgrade has been completed and the
Codex operating model has run cleanly for another review window:

- disabled Claude usage monitoring service/timer files
- `scripts/refresh-claude-usage.sh`
- `scripts/refresh_claude_usage.py`
- pre-Codex systemd backup files in `~/.config/systemd/user`
- compatibility aliases and duplicate case-sensitive operating-area paths
- legacy `jj-*` cold-call compatibility names
- rollback snapshots and generated runtime artifacts without a retention policy

## Safe Phase 3 Cleanup Candidates

After downgrade and final approval, the following can be cleaned up:

- remove or archive disabled Claude usage refresh units if Claude spend
  monitoring is no longer needed
- move pre-Codex systemd backup files to a dated archive or delete them after
  validation
- remove lowercase symlink/path aliases created only to repair stale Codex
  project bindings
- rename or retire legacy `jj-*` cold-call identifiers after downstream sheets,
  validators, and dashboard references no longer depend on them
- adopt a retention policy for generated runtime snapshots before deleting them

## Blocking Items Before Full Cleanup

These are not blockers to lowering Claude billing. They are blockers to deleting
legacy artifacts:

- next live Good Morning and Good Night should validate the restored robust
  command contracts
- dashboard plumbing and email orchestration are still being finalized in the
  dashboard thread
- deal aggregator source-effectiveness review is still being finalized in the
  dashboard thread
- generated runtime artifact policy is still open
- cold-call artifacts should not receive additional investment because cold
  calling is expected to phase out soon

## Operating Rule

During Phase 3, cleanup should be reversible unless Kay explicitly approves
deletion. Prefer archive, disable, or document before remove.

## Decision Log

- 2026-06-14: Claude scheduled runtime checked; no active Claude scheduled
  operations found.
- 2026-06-14: Claude usage timer confirmed disabled and inactive.
- 2026-06-14: Recommended lowering Claude Code billing while preserving Claude
  artifacts as archive.
