---
name: Universal launchd-skill hardening pattern (POST_RUN_CHECK + headless prompt)
description: Every scheduled launchd skill — mutating OR read-only — ships with a POST_RUN_CHECK validator + a headless prompt + a SKILL.md mandatory-validator section. Read-only skills get LIGHTER artifact-landed validators, NOT exempt.
type: feedback
originSessionId: d5485724-ca82-4a50-bf98-38302fa9db3d
---
When authoring or modifying any scheduled `launchd` job, apply the wrapper hardening pattern. **Universal as of 2026-05-04** (broadened from mutating-only) — the dashboard-green-can-lie incident proved exit-code-zero is not a sufficient health signal for any scheduled skill.

## Required components (every launchd skill)

1. **Headless prompt** at `.claude/skills/{skill}/headless-{mode}-prompt.md`. Plist passes `{mode}` as a second arg; wrapper detects the `skill:args` pair and pipes the prompt file as Claude's user prompt instead of bare `/skill-name`. Prompt MUST forbid clarifying questions, mandate artifact-first ordering, and exit non-zero on any blocker.

2. **POST_RUN_CHECK validator** in the plist's `EnvironmentVariables`. The wrapper runs it after Claude exits 0; non-zero override → Slack alert with "VALIDATOR FAILED" prefix. `$TODAY` is substituted with current YYYY-MM-DD. Driver scripts live in `scripts/validate_*.py`.

3. **SKILL.md mandatory-validator section** naming the validator command in a copyable code block. The in-loop invocation is faster (correct mid-run) and cheaper (no Slack noise on transient gaps).

## Validator depth — mutating vs read-only

**Mutating skills (sheet/Attio/vault/Drive writes):**
Validators check artifact + integrity invariants — row-count delta, schema, header presence, no-clear-rewrite, expected entity-count fan-out. Examples: `validate_phase2_integrity.py`, `validate_conference_discovery_integrity.py`.

**Read-only skills (scans, classifications, snapshot refreshers):**
Lighter validators — at minimum check "did the expected artifact land at the expected path with non-zero size and current timestamp?" Examples: did email-scan-results JSON land in `brain/context/`? Did the snapshot refresh write a file dated today? Read-only skills are NOT exempt — a silent-0 failure on email-intelligence still tanks the morning briefing because pipeline-manager treats absence as "no signals," not "skill broke."

## Reference implementation

- Wrapper: `scripts/run-skill.sh` (HEADLESS_PROMPT_FILE resolution + POST_RUN_CHECK block).
- Driver examples: `scripts/validate_phase2_integrity.py` (per-niche fan-out), `scripts/validate_conference_discovery_integrity.py` (row-count delta).
- Headless prompt example: `.claude/skills/target-discovery/headless-phase2-prompt.md`.
- Skill section example: `.claude/skills/target-discovery/SKILL.md` → "Stop Hook: Call-Tab Enrichment Integrity (MANDATORY)".

## Hardened skills (as of 2026-05-04)

**Mutating, full integrity validators:**
- `target-discovery` Phase 2 (shipped 2026-04-25)
- `jj-operations-sunday`
- `nightly-tracker-audit`
- `weekly-tracker`
- `relationship-manager`
- `conference-discovery` (hardened 2026-05-04 after 70-row wipe incident)

**Pending (read-only + snapshot refreshers + remaining weekly jobs):**
Lighter artifact-landed validators required. Audit and ship same pattern. Examples: `deal-aggregator`, `email-intelligence`, `niche-intelligence`, `attio-snapshot-refresh`, `jj-snapshot-refresh`, `apollo-credits-refresh`.

## Precipitating incidents

- **2026-04-19** — `target-discovery` Phase 2 launchd job exited 0 in 2 minutes 26 seconds without writing any artifacts. Claude hallucinated a "another instance is running, standing down" reason and exited cleanly. Wrapper trusted exit code = success. JJ opened Monday tabs with 36 of 40 rows blank in Col K. Triggered the original mutating-skill pattern (bead `ai-ops-1`).
- **2026-05-03** — `conference-discovery` Sunday-night run wiped ~70 rows on the Conference Pipeline tab and exited 0 silently. Dashboard reported it healthy because no validator gated the exit code. Triggered the universal broadening — read-only skills can hit the same silent-0 failure mode and absence-of-output is NOT recoverable downstream.

**How to apply:** Before merging a new launchd plist, the diff MUST include (a) a `headless-{mode}-prompt.md` file, (b) a `POST_RUN_CHECK` env var pointing at a validator script (lighter for read-only, integrity-grade for mutating), (c) a `MANDATORY` section in SKILL.md naming the validator. If any of the three is missing, send the change back. **No exemptions.**
