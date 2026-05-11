---
name: Granola MCP same-session PKCE workaround for headless servers
description: When authenticating Granola MCP on a headless Linux server, run interactive `claude` (NOT `claude -p`) and manually relay the failed-callback URL back to the same session
type: feedback
originSessionId: d5485724-ca82-4a50-bf98-38302fa9db3d
---
When authenticating Granola MCP (or any PKCE-based OAuth MCP) on a headless server, the standard `claude -p` subprocess approach breaks because PKCE state lives in-process and the subprocess exits between `authenticate` (issues URL) and `complete_authentication` (consumes callback). The next subprocess has no flow state.

**Rule:** Use an interactive `claude` session on the server, kept alive across both tool calls. The user opens the URL in their browser on a Mac, lets the callback fail at `localhost:<port>` (no listener reachable from the Mac), copies the failed-callback URL from the browser address bar, and pastes it back into the SAME interactive session as `mcp__granola__complete_authentication callback_url="<URL>"`. PKCE state matches because no process boundary was crossed.

**Why:** The full design rationale is in `brain/traces/2026-05-08-granola-mcp-same-session-pkce.md`. Short version: PKCE state is in-memory; can't cross processes. Granola's `authenticate` tool doesn't print the URL inline either (designed for desktop browser auto-open which fails silently on headless). Same-session is the only path that works without Granola Enterprise API key access.

**How to apply:**
- For any new MCP integration that requires OAuth on a non-Mac server: ssh in, run interactive `claude` (not `claude -p`), execute `mcp__<server>__authenticate` first.
- If the URL isn't visible after the tool call, ask Claude in the same session: "Print the full tool response verbatim, character-for-character, wrapped in triple backticks. If empty, write EMPTY." This forces the URL out of any TUI buffering.
- Open the URL in a Mac browser on the same Tailscale network. Authorize. Browser will hit a `localhost:<port>` callback that fails (no listener reachable from Mac). Copy the FULL failed-callback URL from the address bar — including the `code=...&state=...` query params.
- Paste back to the same Claude session as `mcp__<server>__complete_authentication callback_url="<URL>"`. Token persists to disk; future `claude -p` subprocesses inherit the auth.
- **No SSH port forwarding required.** The trick is keeping the issuing process alive, not tunneling the callback.

**When this fails:** If the MCP doesn't expose a `complete_authentication` tool (some MCPs only support browser-callback), fallback paths are: (a) Granola Enterprise API key (static auth, no OAuth), (b) defer the integration and run from Mac side, (c) scp the Mac's already-authenticated MCP token (rarely portable due to Keychain bindings).

**Source incident:** 2026-05-08 Phase 4 server-migration, blocked Granola MCP detector for ~30 minutes until this pattern was discovered. Without it, Phase 4 would have stayed inert as a canary timer indefinitely.
