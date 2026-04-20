---
schema_version: 1.0.0
date: 2026-04-24
type: output
title: "Saturday 4/25 Tech-Debt Block — Launchd Hardening Plan"
output_type: plan
status: draft
tags: [date/2026-04-24, output, output/plan, topic/launchd-hardening, topic/tech-debt, status/draft]
source: task
---

# Saturday 4/25 — Launchd Hardening Plan

## Scope

Fix the silent-failure bug that caused JJ's blank call-list fire on Monday 4/20. Same bug affects all 5 nightly mutating skills. See root-cause: [[outputs/2026-04-20-target-discovery-phase2-root-cause]]. Bead: `ai-ops-1`.

## Time block

**Saturday 2026-04-25, 9:00 AM ET onward.** Estimated 6–9 hours, single uninterrupted session.

## Why Friday 2pm

- JJ's shift ends at 2pm ET — no concurrent sheet writes from his side
- 1-day buffer before Sunday 10pm Phase 2 run — fix lands in time for first real production validation
- Gives buffer to roll back if any layer breaks something

## Four layers, in order

### Layer 1 — Post-run check in `run-skill.sh` (2 hr)

**Problem:** `scripts/run-skill.sh` trusts Claude's exit code as the sole signal. Skill exits 0 even when zero artifacts written.

**Fix:**
1. Add `POST_RUN_CHECK` env var + config map: each skill names its validator script
2. `run-skill.sh` runs the validator after Claude exits 0
3. If validator fails, override `EXIT_CODE` so Slack alert fires
4. For skills without a validator, fall back to current exit-code-only behavior

**Target-discovery validator:** `.claude/hooks/enrichment_integrity_check.py` (already built 4/20 morning, just wire it)

**Acceptance criterion:** manually run target-discovery with a broken Phase 2 path → wrapper returns non-zero → Slack alert fires

### Layer 2 — Headless prompt for Phase 2 (2–3 hr)

**Problem:** target-discovery agent asked "YES/NO/DISCUSS" inside a non-interactive shell → exited 0 without doing work.

**Fix:**
1. Create `.claude/skills/target-discovery/headless-phase2-prompt.md` — explicit non-interactive instruction set (no questions, no clarification loops, just execute the pipeline)
2. Modify launchd plist to pass `mode=phase2-sunday` arg
3. `run-skill.sh` selects the headless prompt when mode is passed

**Acceptance criterion:** fire launchd job manually → Phase 2 runs to completion → pool artifact exists → enriched rows land on FTL

### Layer 3 — Wire stop hook as mandatory last step (30 min)

**Problem:** `.claude/hooks/enrichment_integrity_check.py` is referenced in SKILL.md but not actually called by any caller.

**Fix:**
1. Update `target-discovery/SKILL.md` Step 5 to require hook invocation as final action (not just "enforced by hook")
2. Update headless prompt to match
3. Validator wired by Layer 1 is the enforcement mechanism

**Acceptance criterion:** SKILL.md + headless prompt + wrapper all three agree on the check

### Layer 4 — Extend pattern to the other 4 nightly skills (3–4 hr)

**Problem:** Same `run-skill.sh` wrapper + interactive-prompt pattern affects 4 other mutating skills.

**Skills to harden:**
- `jj-operations-sunday` (Sunday 6pm — creates Mon–Fri tabs)
- `nightly-tracker-audit` (nightly — processes Tabled/Killed, re-sorts WEEKLY REVIEW)
- `weekly-tracker` (Friday — populates sheet + vault snapshot)
- `relationship-manager` (daily morning — Attio nurture)

**Fix per skill:**
1. Author a headless prompt
2. Author a validator (what must exist/be true for run to be considered successful)
3. Wire validator into `run-skill.sh` config map

**Acceptance criterion:** each of 4 skills has `mode=headless-*` plus validator. Manually trigger all 4 in sequence → all report correct pass/fail.

## Success definition

- All 5 nightly jobs either (a) complete their work and report green, or (b) fail loudly with Slack alert
- No more silent zero-work "success" exits
- Sunday 4/26 Phase 2 runs cleanly; Monday 4/27 JJ tab is 100% Tier-1

## Rollback plan

Each layer is independent. If Layer 2 breaks, Layer 1's post-run check catches it and alerts. If Layer 1 breaks, existing behavior is preserved (exit code only). Layer 3 is documentation-only. Layer 4 builds on Layer 1–2.

Keep snapshots of `run-skill.sh` + plists before editing. Commit each layer separately.

## Separately — later decision (not this Friday)

[[outputs/ai-ops-2]] bead: evaluate GitHub Actions migration for the same 5 jobs. After this Friday's fixes ship, Kay can decide whether local-launchd or cloud is the long-term home. Migrating first would move the bugs, not fix them — so Friday's work is prerequisite.

## Linked artifacts

- Root cause: [[outputs/2026-04-20-target-discovery-phase2-root-cause]]
- Bead `ai-ops-1` (this plan)
- Bead `ai-ops-2` (follow-on GitHub Actions evaluation)
- Stop hook: `.claude/hooks/enrichment_integrity_check.py`
- Incident context: [[context/session-decisions-2026-04-20]] (to be written at goodnight)

## Tags

- topic/launchd-hardening
- topic/tech-debt
- topic/post-mortem
- status/draft
