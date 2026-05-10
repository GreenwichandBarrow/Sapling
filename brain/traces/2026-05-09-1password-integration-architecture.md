---
schema_version: 1.1.0
date: 2026-05-09
type: trace
importance: high
target: "skill:run-skill"
tags: ["date/2026-05-09", "trace", "domain/infrastructure", "topic/1password", "topic/op-cli", "topic/secrets-management", "status/applied"]
---

# 1Password integration architecture — helper file + op inject (rejected: systemd-wrap, per-script re-exec)

## Trigger

After tonight's first leak (`grep -rE` exposed live ATTIO + APOLLO keys), Kay agreed to migrate raw `.env.launchd` values to 1Password `op://` references. Architectural choice: how does the chain `systemd timer fires → bash wrapper → python script → API call` resolve op:// references to actual secret values?

## Decision

Two-part pattern:
1. **`scripts/load-env.sh` helper** with `load_env <file>` function. All consumer scripts source the helper + call the function instead of `source $env_file` directly. The helper checks if op CLI is available + file has `op://` references; if both true, resolves via `op inject -i $file` and sources the result. Else direct source (backward compatible).
2. **`op inject` for resolution, NOT `op run`.** Inject substitutes references in-place + emits to stdout. Run wraps an entire command. Inject fits existing `source <(...)` pattern; run would require restructuring every caller.

## Alternatives Considered

- **Per-script `op run` re-exec at top.** Each consumer detects op:// refs + re-execs itself under `op run --env-file=... -- /bin/bash $0 $@`. Rejected: identical 8-line block would need to live in 4+ scripts; if I had to fix the re-exec pattern later, every script would need updating. Fragmented.
- **systemd `ExecStart=op run --env-file=... -- /bin/bash <script>` wrapping.** Pre-process at the systemd level so scripts never see op:// refs. Rejected: requires editing all 21 .service files AND modifying `generate_systemd_units.py` to emit the wrap (which doesn't currently support `op run` syntax). Also requires `op` to be on PATH at unit-load time, which couples auth context to systemd in a fragile way.
- **`op run` instead of `op inject`.** op run wraps a command and passes resolved env vars to the wrapped process. The wrapped process can't `source` the resolved env file (the file passed to op run is the raw op:// version; the resolved values exist only in env). Doesn't fit the `set -a; source $f; set +a` idiom that 4 scripts already use. Inject is a drop-in substitution.

## Reasoning

The helper-file pattern centralizes the op-detection logic in one place. If `op inject` behavior changes, or we want to add caching, or we need to add error handling, it's one file. Consumer scripts are 2-line edits each:

```bash
# Before:
source "$REPO_ROOT/scripts/.env.launchd"

# After:
source "$REPO_ROOT/scripts/load-env.sh"
load_env "$REPO_ROOT/scripts/.env.launchd"
```

`op inject` was chosen because it preserves the file format. The output of `op inject -i .env.launchd` is the same `.env.launchd` file with op:// references substituted to actual values. So `source <(op inject -i $f)` is exactly equivalent to `source $f` from the consumer's perspective — same env-var-export semantics.

`op run` would have required either (a) re-exec the whole script under op run, or (b) abandon source-based env loading entirely and rely on op run's env injection. Both invasive. Inject is invisible to existing callers.

## Outcome

- Helper landed at `scripts/load-env.sh` (30 lines).
- 4 consumer scripts updated: `run-skill.sh`, `refresh-attio-snapshot.sh`, `refresh-apollo-credits.sh`, `probe-external-services.sh`.
- All 21 server systemd `.service` files received `EnvironmentFile=%h/.config/op-sa-token.env` line via in-place sed (so `OP_SERVICE_ACCOUNT_TOKEN` is set when bash invokes scripts).
- Smoke test on `attio-snapshot-refresh.service` PASSED end-to-end: 151 entries fetched, snapshot written, validator PASSED.

## Learnings

- When integrating with a new CLI tool, prefer the substitution-style verb (`inject`, `read`) over the wrapping-style verb (`run`, `exec`) if existing callers use `source` patterns.
- Helper-file pattern beats per-caller copy-paste for cross-cutting concerns — even if the helper is only 30 lines, it saves maintenance cost across N callers.
- For systemd services, `EnvironmentFile=` is the cleanest way to inject secrets without baking values into unit files. The token file is chmod 600, lives outside the repo.
- This pattern generalizes to any future secret migration: Slack webhooks, KEYCHAIN_PASSWORD, future API keys can all use the same `op://Vault/Item/field` reference + load_env helper combo.
