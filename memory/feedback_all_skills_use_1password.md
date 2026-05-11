---
name: All skills must use 1Password for credential resolution
description: Universal policy locked 2026-05-11. Every skill, scheduled job, validator, dashboard refresher, and ad-hoc API call resolves credentials via `op://` references — never plaintext, never env-var-on-disk, never hardcoded.
type: feedback
---

Every G&B skill, scheduled job, validator script, dashboard refresher, and ad-hoc API call on the VPS resolves credentials via 1Password (`op read 'op://{vault}/{item}/{field}'`) — never via plaintext in shell files, never via env vars baked into plists/timers, never via hardcoded strings.

**Why:** Plaintext-secret incidents (.bashrc with `GOG_KEYRING_PASSWORD=...`, `.env.launchd.bak` files with rotated-out Attio/Apollo keys, etc.) have been the primary credential-leak surface for the last two months. The Sunday 2026-05-10 migration moved all 7 production secrets to op://; the only path forward is to make 1P the ONLY credential source going forward. Skills that bypass 1P recreate the leak surface. Source: 2026-05-11 directive from Kay during ACG cross-reference work, after I noted "Attio MCP not loaded" instead of resolving the API key via 1P + calling the API directly.

**How to apply:**

1. **Bash invocations:** Bootstrap pattern at the top of any block touching secrets:
   ```bash
   set -a
   source ~/.config/op-sa-token.env
   set +a
   export GOG_KEYRING_PASSWORD=$(op read 'op://GB Server/GOG Keyring Password/password')
   # ... then your work
   ```
   Or for one-off API calls: `curl -H "Authorization: Bearer $(op read 'op://GB Server/{Item}/password')" ...`

2. **Skill scripts:** Use `scripts/load-env.sh`'s `load_env "$REPO_ROOT/scripts/.env.launchd"` helper, which auto-resolves op:// references via `op inject` when available, falls back to source-as-is otherwise.

3. **systemd units / plists:** Reference `EnvironmentFile=scripts/.env.launchd` (which contains op:// strings) and let the wrapper resolve them at runtime via `op inject`. Never inline plaintext secrets in the service unit.

4. **Direct API calls (curl):** Always pipe `op read` directly into the auth header. Never write the resolved key to a file unless absolutely necessary, and if you do, write to `/tmp/`, set chmod 600, delete after use. Suppress curl response output when verifying auth: `-s -o /dev/null -w "%{http_code}\n"` per `feedback_curl_verify_before_mcp`.

5. **MCP servers:** If an MCP exists for the service (Attio MCP, Granola MCP, etc.), let the MCP server handle credential resolution — but verify the MCP itself was configured against op:// references in `~/.claude.json`, not against plaintext API keys. If MCP isn't loaded in the current session, fall through to direct API calls with op://-resolved keys.

6. **Don't conflate "MCP not loaded" with "can't write."** MCP is one path. Direct API with op://-resolved key is another. Always available as long as the OP service account token is loadable.

**Failure modes to catch:**
- A new skill author writes `export API_KEY=sk_live_...` in a shell script → BLOCK at code review.
- A subagent proposes "store the API key in a config file" → redirect to op://.
- A "quick fix" plist Environment= line with plaintext value → redirect to EnvironmentFile= + op:// in scripts/.env.launchd.
- "I can't do X because MCP isn't loaded" → check if direct API + op:// resolves it first.

**Exceptions:** Read-only ephemeral data with no auth required (e.g., public website fetches) doesn't apply. Anything authenticated does.

**Related memories:**
- `feedback_credential_extraction_clean_terminal.md` — extraction terminal hygiene
- `feedback_curl_verify_before_mcp.md` — verify auth via output-suppressed curl before MCP calls
- `project_server_migration_status.md` — Sunday 2026-05-10 1P migration state
- `feedback_integration_priority_mcp_api_local.md` — MCP first → API → local, but ALL of those use 1P for auth
