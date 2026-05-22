---
schema_version: 1.1.0
date: 2026-05-19
review_status: applied
type: trace
task: Resolve gog auth failure during template-doc fetch
had_human_override: true
tags:
  - date/2026-05-19
  - trace
  - topic/credentials
  - topic/tooling
  - pattern/canonical-source-first
  - status/done
---

# 1Password-first credential resolution

## Context
Needed to read the canonical Intermediary Templates Google Doc to draft a warm-intro reply. `gog` failed with `aes.KeyUnwrap(): integrity check failed`. Sourced `scripts/.env.launchd` raw as a fix attempt; still failed. Kay intervened: "why aren't you going through 1password again" and later "this keeps happening. please figure out what you need to change so this doesn't happen again."

## Decisions

### Diagnose the gog auth failure
**AI proposed:** Treat `aes.KeyUnwrap(): integrity check failed` as a corrupted/mismatched keyring (the literal error points there).
**Chosen:** Root cause is skipping the 1Password resolve — `.env.launchd` holds `op://` *reference strings*, not values; sourcing it raw exports the refs, so gog can't decrypt. Correct path: load the op SA token (`~/.config/op-sa-token.env`) + `op inject` to resolve refs.
**Reasoning:** The error *looks* like keyring corruption, which historically tempted credential rotation (3 rotations on 2026-04-27 from a related misread). The keyring was never corrupt. 1Password is the first rung of the credential ladder and was being skipped.
**Pattern:** #canonical-source-first

### Durable fix scope
**AI proposed:** (initially) just retry with the right command.
**Chosen:** Make the correct path the path of least resistance AND enforce it: `scripts/op-env.sh` one-liner, `op_first_guard.py` PreToolUse hook blocking raw `.env.launchd` source/eval, CLAUDE.md always-loaded pre-flight bullet, `feedback_op_env_before_op_backed_cli` memory.
**Reasoning:** Kay flagged recurrence ("this keeps happening"). A memory alone hopes recall fires; a hook makes the antipattern impossible. Mirrors the secret_file_guard precedent.
**Pattern:** #canonical-source-first

## Learnings
A credential error that *looks* like corruption is, in this system, almost always a skipped 1Password resolve. Never rotate or assume corruption before verifying `source scripts/op-env.sh` works. The fix for a recurring agent failure is enforcement (hook) + frictionless correct path, not just doctrine.
