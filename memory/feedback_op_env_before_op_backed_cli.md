---
name: feedback_op_env_before_op_backed_cli
description: Always resolve credentials through 1Password (source scripts/op-env.sh) before any op://-backed CLI; never source .env.launchd raw
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 8204e9db-579c-412b-8bf1-3682a28e14d1
---

Before any `gog` / `attio` / `apollo` / op://-backed CLI in an interactive session, run `source scripts/op-env.sh && <command>`. NEVER `source scripts/.env.launchd` raw.

**Why:** `.env.launchd` holds `op://...` *reference strings*, not secret values. Sourcing it raw exports the literal refs, so `gog` fails with `aes.KeyUnwrap(): integrity check failed` — which looks like a corrupted keyring and led to flailing and (historically) spurious credential rotations. The real cause every time was skipping the 1Password resolve. 1Password is the first rung of the credential ladder, not an afterthought. Recurred enough times (2026-05-18 the trigger) that it is now hook-enforced, not memory-hoped.

**How to apply:** Canonical one-liner: `source scripts/op-env.sh && gog docs export <id> --format txt --account kay.s@greenwichandbarrow.com`. The helper loads `~/.config/op-sa-token.env` (the op SA token systemd injects) then `op inject`-resolves `.env.launchd`. Shell state does not persist between Bash tool calls, so re-source the helper in every command that needs creds. Hook `.claude/hooks/router/handlers/op_first_guard.py` BLOCKS raw `source`/`eval` of `.env.launchd` without `op inject` or the wrapper. CLAUDE.md "Before handling secrets / config" carries the always-loaded version. Related: [[feedback_all_skills_use_1password]], [[feedback_check_credential_source_before_auth]], [[feedback_curl_verify_before_mcp]], [[feedback_never_read_config_with_secrets]], [[feedback_secrets_tmp_method]].
