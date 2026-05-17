---
name: reference_gog_interactive_unlock_recipe
description: "Exact prefix to unlock gog (Gmail/Sheets/etc.) in an interactive session — non-obvious, cost ~10 tool calls to derive 2026-05-17"
metadata: 
  node_type: memory
  type: reference
  originSessionId: 8f278aa1-0390-4c59-a1e0-363cfa6127a3
---

In an interactive (non-launchd) session, `gog` fails with `no TTY available for keyring file backend password prompt; set GOG_KEYRING_PASSWORD` unless the keyring is unlocked via the 1Password service-account path. The scheduled-skill wrapper does this implicitly; interactive shells must replicate it exactly.

**Working prefix (one bash command — shells do not persist env between Bash calls, so prepend this to every gog/Sheets/task_tracker invocation):**

```bash
source ~/.config/op-sa-token.env 2>/dev/null; export OP_SERVICE_ACCOUNT_TOKEN; \
source scripts/load-env.sh 2>/dev/null; set -a; load_env scripts/.env.launchd >/dev/null 2>&1; set +a; \
export GOG_ACCOUNT=kay.s@greenwichandbarrow.com; <gog command>
```

Two non-obvious failure causes, both required:
1. **`~/.config/op-sa-token.env` must be sourced first** (sets `OP_SERVICE_ACCOUNT_TOKEN`). Without it `op inject` inside `load_env` resolves op:// refs to empty. `op whoami` shows "NOT signed-in" even when the SA token is valid — verify instead with `op vault list` (should list "GB Server").
2. **`load_env` must be wrapped in `set -a` / `set +a`** (per `scripts/load-env.sh:11` — "Caller is responsible for `set -a`"). Without it `GOG_KEYRING_PASSWORD` is set in the shell but NOT exported to the `gog` child process, so gog still errors.

Symptom of getting this wrong: gog searches return **empty results with no error**, which is easily misread as "no data" (e.g. misreported Harrison's emails as absent on 2026-05-17 — they existed). Treat empty gog output as suspect until the unlock is confirmed. Never `cat`/`grep` `scripts/.env.launchd` for values — the secret-file hook blocks it; see [[feedback_never_read_config_with_secrets]] and [[feedback_curl_verify_before_mcp]].
