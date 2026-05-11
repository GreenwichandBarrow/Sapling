---
schema_version: 1.1.0
date: 2026-05-10
type: trace
title: "Fix shared-concern bugs at the wrapper layer, not per-instance"
had_human_override: false
importance: medium
target: "scripts/run-skill.sh, process, future-validator-additions"
tags: ["date/2026-05-10", "trace", "topic/launchd-debugger", "topic/systemd-validators", "topic/run-skill", "pattern/shared-wrapper-shared-fix"]
---

# Trace: Fix shared-concern bugs at the wrapper layer, not per-instance

## Context

Decision-3 of the 2026-05-10 morning briefing was the `nightly-tracker-audit` POST_RUN_CHECK validator failing nightly with:

```
NIGHTLY-TRACKER-AUDIT VALIDATOR FAILED: could not read sheet:
gog sheets get failed: missing --account (or set GOG_ACCOUNT, ...)
```

The skill body itself ran clean (sheet was correctly sorted), but the validator's `subprocess.run(["gog", "sheets", "get", ...])` call had no `--account` flag and `GOG_ACCOUNT` wasn't set in the launchd-context env. Root cause was unambiguous; the question was where to fix it.

## Decisions

### Fix layer

**AI proposed:** Three options — (1) patch `validate_nightly_tracker_audit_integrity.py` line 33 to add `"--account", "kay.s@..."` to the subprocess args, (2) patch all 4 validators that have the same pattern (discovered via grep), (3) export `GOG_ACCOUNT` once in `scripts/run-skill.sh` (the wrapper that all systemd services invoke).

**Chosen:** Option 3 — wrapper-level export. Single line added at `scripts/run-skill.sh` line ~41, just after `load_env`:

```bash
export GOG_ACCOUNT="${GOG_ACCOUNT:-kay.s@greenwichandbarrow.com}"
```

**Reasoning:** A grep across `scripts/validate_*_integrity.py` revealed the same pattern in 4 separate validators (`nightly-tracker-audit`, `conference-discovery`, `jj-operations`, `weekly-tracker`). Three of those hadn't surfaced as failures yet only because their schedules hadn't fired since the universal POST_RUN_CHECK doctrine rolled out (2026-05-04). Patching each script independently would have been 4 edits, 4 diff reviews, and 4 future maintenance touchpoints. Wrapper-level export is one edit that:
- covers all 4 currently-broken validators
- covers any future validator that calls `gog` without `--account`
- documents the requirement once at the env-setup stage of the wrapper, where any reader of `run-skill.sh` immediately sees it
- preserves the existing `${VAR:-default}` pattern so a plist or `.env.launchd` override still wins if Kay ever needs a different account

The override-friendly form (`${GOG_ACCOUNT:-...}`) was important — hardcoding the email would have broken multi-account scenarios (none today, but cheap insurance).

**Pattern:** #pattern/shared-wrapper-shared-fix

## Learnings

When investigating a single failure, grep across siblings before deciding where to fix. The "fix the broken thing" instinct points at the per-instance patch; the "fix it once" instinct points at the shared wrapper. Both are correct. The grep across siblings tells you which.

Concretely, the heuristic that worked here: when the broken thing is **invoked through a shared wrapper script**, the shared wrapper is almost always the right fix layer for environment/setup concerns. Per-instance fixes are appropriate when the fix is **logically specific to one consumer** (e.g., one validator's data parsing).

A second-layer issue surfaced after the wrapper fix: `GOG_KEYRING_PASSWORD` was also missing from launchd-context env (lived in `~/.bashrc`, interactive only). That fix went into `scripts/.env.launchd` as an op:// reference, NOT into `run-skill.sh` as a default — because the keyring password IS a secret and per-account rotation matters; wrapper-defaulting it would create a hidden source-of-truth that conflicts with the 1Password vault. The right layer for **a default value of a config setting** (account email) is different from the right layer for **a secret credential** (op:// reference resolved at runtime).

## Why This Trace Matters

A future agent encountering a similar "validator X fails on env Y" symptom might default to patching validator X. That works, but doesn't compound — the next validator with the same env hole will fail tomorrow and need its own patch. The wrapper-level alternative is invisible from the per-validator view and only reveals itself via cross-script grep.

The trace generalizes beyond this specific bug: any time a fix CAN apply at a shared wrapper/middleware/orchestrator layer AND the concern is genuinely shared (env setup, auth bootstrap, common headers, etc.), prefer that layer. Save per-instance patches for genuinely-instance-specific concerns.

## Key Insight

**Grep before patching.** When fixing a single failure, search siblings to see if the same pattern exists elsewhere. If yes, fix at the shared layer; if no, the per-instance patch is correct. The 30-second grep saves hours of compounding maintenance.
