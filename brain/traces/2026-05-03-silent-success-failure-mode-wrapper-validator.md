---
schema_version: 1.1.0
date: 2026-05-03
type: trace
title: "Silent-success failure mode in headless skills — wrapper-validator pattern"
trace_type: technical-pattern
tags: ["date/2026-05-03", "trace", "topic/launchd-debugger", "topic/deal-aggregator", "topic/wrapper-hardening", "topic/silent-failure", "person/harrison-wells"]
---

# Silent-success failure mode in headless skills — wrapper-validator pattern

## Trigger

Kay flagged that deal-aggregator "hasn't been working well." launchd-debugger investigation of the past 7 days' deal-aggregator runs surfaced two silent-success incidents (4/27, 4/28 mornings) where Claude received the headless prompt, emitted operator-question framings (`RECOMMEND: Let attempt 2 run, monitor for artifact → YES/NO/DISCUSS`) instead of executing the scan, and exited 0. Wrapper saw exit 0 → no Slack alert fired → afternoon variant was the only thing flagging "morning artifact missing." 4/27 morning artifact never landed; 4/28 stalled 2hr before writing at 8:03am.

## Decision

Hardened the deal-aggregator wrapper with a POST_RUN_CHECK validator pattern that cross-checks artifact presence + structure independent of the wrapper's exit code. Specifically:

1. New `scripts/validate_deal_aggregator_integrity.py` — checks artifact ≥200 bytes, frontmatter present with matching date, all required section headers present (3 modes: morning / afternoon / digest).
2. `scripts/run-skill.sh` — POST_RUN_CHECK env var wired into all 3 deal-aggregator wrapper case branches (morning, afternoon, digest). Validator non-zero → wrapper overrides EXIT_CODE → Slack alert with "VALIDATOR FAILED" prefix.
3. `headless-morning-prompt.md` — added explicit forbidden pattern banning the "ask Kay if I should proceed" branch with 4/27 + 4/28 incident citations. Plain rule: idempotency gate is the ONLY arbiter.
4. `SKILL.md` — added `<wrapper_hardening>` section documenting the validator wiring.

## Alternatives considered

1. **Trust exit code alone** — what was happening before. Defeated by silent-success: prompt completed, wrote no artifact, exit 0. Failed.
2. **Add idempotency-gate-only check** — wrapper could check whether today's artifact exists post-run. Would catch the same failure mode but only the artifact-presence half. Misses cases where artifact exists but is malformed (corrupt / missing sections / wrong date).
3. **Move to in-prompt self-check** — have the prompt validate its own output before exiting. Defeated by the same silent-success mode: the prompt that's misbehaving can't reliably self-validate.
4. **Slack-on-no-artifact directly from wrapper** — works for missing-artifact cases but not malformed-artifact cases. Subset of the validator approach.

The validator-as-POST_RUN_CHECK approach was chosen because it's source-of-truth-independent (validator runs in fresh process, doesn't trust prompt's claim of success), generalizes to other artifact types (3-mode design proves the pattern), and graduates the wrapper from "trust the prompt" to "verify the deliverable."

## Reasoning

The silent-success class of failure has been seen across multiple skills (per `feedback_mutating_skill_hardening_pattern`):

- niche-intelligence Tuesday-night fire (ai-ops-5wx) — fixed 5/1
- target-discovery Phase 2 Sunday — fixed 4/26
- jj-operations-sunday — fixed 4/26
- deal-aggregator (this trace) — fixed 5/3

All shared: headless prompt produces output that LOOKS like work but isn't, wrapper sees exit 0, no alert fires. The pattern is: the LLM under headless mode can produce shapes-of-work (operator questions, plans, framings) that bypass the actual deliverable. The fix is always the same: POST_RUN_CHECK validator + headless-prompt forbidden-pattern entries + SKILL.md mandatory-validator section.

Per Harrison Wells coaching (4/30): "agents-all-the-way-down repair layer." The launchd-debugger catches these post-hoc; the wrapper-validator catches them at the run boundary, BEFORE they propagate.

## Why this trace matters

A future agent shipping a new headless-mode skill (any mutating skill on launchd) might assume exit-code-trust is sufficient. It is not. The pattern is:

1. Mutating skill on launchd → MUST have headless-mode prompt (not bare `/skill-name`)
2. Headless prompt → MUST have explicit forbidden-pattern section banning operator-question framing
3. Wrapper → MUST have POST_RUN_CHECK env var pointing at a per-skill validator
4. Validator → MUST cross-check artifact presence + structure independent of exit code
5. SKILL.md → MUST document the validator wiring in a `<wrapper_hardening>` or equivalent section

Skip any of those four and you re-introduce silent-success.

Read-only skills (deal-aggregator daily-scan output is read-only-ish in that it doesn't write to sheets/Attio) tolerate silent-0 because absence-of-output surfaces in pipeline-manager. But ALL mutating skills (writes to sheets / Attio / vault) need the full hardening pattern.

## Key insight

**Exit code is a liveness signal, not a correctness signal.** The wrapper has to verify the deliverable, not the process.

When the failure mode is "prompt exits cleanly without producing the deliverable," the only fix that catches it is one that runs AFTER the prompt and checks the deliverable independently. Anything inside the prompt's process is corruptible by the same failure mode.

Generalizable beyond launchd: any agent task that's expected to produce an artifact should be guarded by an artifact-validation step that runs in a fresh context. "Trust but verify" — the verify is non-optional for any process you can't watch in real time.
