---
schema_version: 1.1.0
date: 2026-05-09
type: trace
importance: high
target: "skill:run-skill"
tags: ["date/2026-05-09", "trace", "domain/infrastructure", "topic/1password", "topic/op-cli", "pattern/silent-fallback", "status/applied"]
---

# load-env.sh grep pattern bug — quoted values defeated `'=op://'` anchor

## Trigger

After deploying load-env.sh + updating systemd .service files + .env.launchd to op:// references on server, smoke-test of `attio-snapshot-refresh.service` failed with Attio 401: "API Keys should be 64 characters long." But the actual key in 1Password was confirmed 64 chars. So the resolved value reaching Attio's API was wrong.

`bash -x` trace of `load_env` showed: `command -v op` ran (returned 0), `grep -q '=op://' "$f"` ran, then control jumped directly to the FALLBACK `source $f` branch — which sourced the literal op:// reference string into `ATTIO_API_KEY`. The substitution branch was never taken.

## Decision

Patched `load-env.sh` grep pattern from `'=op://'` to `'op://'` (drop the `=` anchor). The bug was that `.env.launchd` content has `="op://..."` — quote between `=` and `op` — so the literal pattern `=op://` doesn't match. Dropping the `=` makes the check match any line containing `op://`, which is what we actually want.

## Alternatives Considered

- **Update `.env.launchd` to omit quotes around op:// values** (e.g., `export ATTIO_API_KEY=op://GB Server/Attio API Key/password`). Rejected: would break `set -a; source $f; set +a` idiom because the value contains spaces (vault name `GB Server`) and would be parsed as multiple tokens. Quotes are required.
- **Match the exact quoted form: `grep -q '="op://'`.** Rejected: brittle. If anyone writes `'op://...'` with single quotes, or no quotes for a no-space vault, it fails. The simpler `'op://'` works for all variants.
- **Remove the conditional entirely; always run `op inject` even if no op:// refs.** Rejected: would require op CLI + auth on every machine that runs the helper, even for env files with only raw values. Breaks backward compatibility.

## Reasoning

The bug is subtle because:
- The check looks correct on a quick read (`=op://` matches "value starts with op://").
- bash trace doesn't show the result of conditional checks, only the commands. So `+ grep -q =op:// $f` looks like it ran successfully — you have to know that `grep -q` returns non-zero on no-match to realize the if branch was false.
- The fallback `source $f` succeeds (reads the file fine), it just produces wrong values (literal op:// strings as env-var contents).
- The downstream API call fails with a misleading "wrong length" error instead of "this isn't a valid API key format" — Attio's error message blamed key length when the actual issue was wholesale string mismatch.

The general lesson: when a feature-flag check decides between "use feature" and "fallback to old path," the fallback path must be designed to fail loudly, not silently produce wrong data. In this case, sourcing literal op:// strings as ATTIO_API_KEY was a silent corruption.

## Outcome

- `load-env.sh` patched on iMac + scp'd to server.
- Re-tested via `bash -x` trace: now shows `op inject` running and substituted values being sourced.
- Smoke test of `attio-snapshot-refresh.service` PASSED on retry: 151 entries fetched, snapshot written, validator PASSED.

## Learnings

- When matching env-file content with `grep`, never anchor on `=` because env-file values may be quoted (`KEY="value"`) or unquoted (`KEY=value`). Use the value-side pattern alone.
- For feature-flag conditionals with a fallback path, design the fallback to fail loudly. Either (a) detect when the fallback is wrong (e.g., grep for `op://` AFTER source — if found, abort), or (b) make the fallback path produce a marker that downstream code can check.
- API errors that blame the wrong attribute ("wrong length" when the actual issue is "wrong format") are common with auth APIs. Don't trust the error wording — verify length AND format AND prefix AND character set when debugging auth failures.
- bash `set -x` is the diagnostic tool for "is this if branch taking the path I expect" — but the trace doesn't show return codes, only commands. Have to infer from which next-command appears.
