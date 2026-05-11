---
name: Verify credential via curl before any MCP call after rotation
description: After rotating an API key, curl-verify the new key with output suppression BEFORE any MCP tool call. MCP error formatters can leak Authorization headers on 401.
type: feedback
originSessionId: e01b0f15-d8be-4bd0-8424-2b86790ca0c8
---
After rotating any API key/token used by an MCP server (Attio, future Slack-MCP, etc.), **curl-verify the key with output suppression BEFORE making any MCP tool call**.

**Why:** MCP server error formatters (proven on `attio-mcp` axios errors) include the full `Authorization: Bearer <token>` header in their 401 response. Calling an MCP tool with a misconfigured token leaks the token into transcript. The PostToolUse `redact_secrets` hook can WARN but cannot SCRUB already-streamed output (Claude Code hook architecture limit — no `output_replacement` field).

**The 2026-04-27 incident:** 4 leaks of the same Attio token across one session. Pattern: rotate → swap into config → call `mcp__attio__*` → 401 → leaked. Each /mcp reconnect surfaced the same hex value because Claude Code caches MCP server configs at session start (separate problem, see `project_claude_code_config_cache.md`).

**How to apply — required flow after rotation:**

1. New key in `/tmp/<service>-key.txt` (silent file transfer per `feedback_secrets_tmp_method`).
2. Swap into config files via Python (no echo of value).
3. **Curl-verify with output discarded — only HTTP status code prints:**
   ```bash
   python3 -c "
   import json, pathlib, subprocess
   key = pathlib.Path('/tmp/attio-key.txt').read_text().strip()
   res = subprocess.run(['curl','-s','-o','/dev/null','-w','%{http_code}',
                         '-H', f'Authorization: Bearer {key}',
                         'https://api.attio.com/v2/lists?limit=1'],
                         capture_output=True, text=True, timeout=15)
   print('status:', res.stdout.strip())
   "
   ```
   - 200 = scopes valid, key live → safe to proceed.
   - 401 = bad key/scopes — **NO LEAK** because response body discarded by `-o /dev/null`. Re-rotate or fix scopes.
4. Only after 200 confirms → user `/mcp` reconnects → ONE MCP smoke test (e.g., `get-lists`) → if also 200, proceed with full skill run.

**Critical:** Step 3 (curl-verify) is non-negotiable. Even if the rotation flow looks fine, the MCP error-leak vector activates on ANY 401. Without curl-verifying first, you're rolling the dice on whether scopes were saved correctly, whether the right token landed in the right place, etc. — and any failure leaks.

**Verify-via-API endpoints by service:**
- Attio: `https://api.attio.com/v2/lists?limit=1` (cheap; needs List Configuration:Read or higher)
- Apollo: `https://api.apollo.io/v1/auth/health` (no scope needed)
- Add others as we wire MCP servers.

**Codified in CLAUDE.md** "Before handling secrets / config" pre-flight (loaded into every session). Adding here for searchability + the procedural detail.
