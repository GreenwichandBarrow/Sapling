---
schema_version: 1.1.0
date: 2026-05-08
type: trace
importance: high
target: process
tags: ["date/2026-05-08", "trace", "domain/auth", "pattern/oauth-pkce", "topic/granola", "topic/mcp", "topic/server-migration", "status/applied"]
---

# Granola MCP same-session PKCE workaround for headless server auth

## Trigger

Granola MCP authentication on the Linux server blocked Phase 4 detector from returning real meetings. The detector was inert — the prompt's defensive fallback ("if MCP fails or returns no meetings, output exactly: []") was masking the auth failure as a clean no-op.

Standard OAuth PKCE flow assumes:
1. Authenticator process opens browser
2. Browser hits user's localhost callback after authorize
3. Same process catches the callback and exchanges code for token

On a headless VPS this breaks because:
- `claude -p` is a one-shot subprocess. The PKCE state lives in-process. Process exits after printing the authenticate URL.
- Next `claude -p` call (paste callback URL) is a fresh process with no flow state. `complete_authentication` errors with "no flow in progress."
- Granola's `mcp__granola__authenticate` tool is designed to auto-open the system browser. Headless server has no display. Tool returns silently with no URL printed.

## Decision

Run an **interactive `claude` session** on the server (not `claude -p` one-shot). Manually copy the failed-callback URL from the iMac browser's address bar back to the same interactive session. Both `mcp__granola__authenticate` and `mcp__granola__complete_authentication` execute in the SAME process, so PKCE state persists across the two tool calls.

No SSH tunneling required. No port forwarding required. The trick is keeping the process alive across the URL copy.

## Alternatives Considered

- **claude -p subprocess approach.** Failed — cross-process PKCE state breaks.
- **SSH tunnel + interactive session.** Initially proposed; rejected when discovered Granola's authenticate tool doesn't print the URL inline (designed for desktop browser auto-open). Tunneling the callback port wouldn't help if no URL ever surfaces.
- **scp Claude Code MCP token from iMac to server.** Token storage format is opaque (likely macOS Keychain-bound or in `~/.claude.json` — not easily portable). Investigation cost > likely payoff.
- **Granola Enterprise API key** (static auth, no OAuth). Granola docs mention as separate access path; would require Kay obtaining an API key from Granola support. Not investigated.
- **Path B (defer Phase 4 as canary).** Considered as fallback if A/D failed. Phase 4 server detector remains inert; iMac sidecar continues as actual processor. Rejected because it punted the entire Phase 4 completion.

## Reasoning

Three constraints converged:

1. **PKCE state is in-memory in the issuer process.** Cannot be serialized across process boundaries. Anything that exits between `authenticate` and `complete_authentication` breaks the flow.

2. **Granola's authenticate tool doesn't print the URL inline in interactive mode.** It auto-opens the browser via macOS desktop integration; on Linux headless server, the call succeeds but produces no visible artifact. The URL is sent to nowhere.

3. **The browser callback port is ephemeral.** Each authenticate call picks a fresh port (e.g., 57529, 58777, etc.). The listener is bound inside the issuing process. On a headless server, no browser can reach `localhost:<port>` from the user's iMac.

The same-session pattern threads this needle: the issuing process stays alive, the URL is captured manually by inspecting the failed-callback URL in the iMac browser address bar, and the captured URL is fed back into the same process via `complete_authentication`. The PKCE state matches because no process boundary was crossed.

## Why This Trace Matters

Future MCP integrations that need OAuth on the server will hit this exact pattern. Granola is one example; any MCP using PKCE will require the same workaround on headless infrastructure. Without this trace, the next agent will burn hours rediscovering that:

- `claude -p` subprocess loop doesn't work for OAuth flows
- SSH port forwarding doesn't help when the URL itself never surfaces
- Granola-specific tools that rely on desktop browser integration silently no-op on Linux

Adjacent learning for `vps-toolkit` skill (planned 5/9): server-side OAuth flows need interactive Claude on server, not `claude -p` subprocess from iMac.

## Key Insight

**OAuth PKCE on headless servers requires a single long-lived process spanning both sides of the user-interaction step.** The user-interaction (browser click) happens off-process; the authenticate-issue and authenticate-complete steps must happen inside the SAME process. The "no port forwarding" insight is that the callback URL itself contains the auth code — you don't need the browser to actually reach the listener; you just need to manually relay the URL contents into the same process that issued the request.
