---
schema_version: 1.1.0
date: 2026-05-13
type: trace
today: "[[notes/daily/2026-05-13]]"
task: Decide how skills should access Granola transcripts durably (no reconnect)
output: "[[context/session-decisions-2026-05-13]]"
had_human_override: true
tags: [date/2026-05-13, trace, topic/granola-api-wrapper, topic/credential-architecture, person/harrison-wells, pattern/oauth-mcp-bypass-with-1password-wrapper]
---

# Decision Trace: Bypass OAuth MCP — 1Password-Resolved REST Wrapper Instead

## Context
Kay wanted post-call-analyzer to pull Granola transcripts within an hour of a call ending, in headless/scheduled jobs, with no browser dance and no reconnect. The Granola MCP is PKCE-OAuth: Claude Code owns the tokens in its own cache and loses them at session boundaries. Claude initially proposed (a) re-running OAuth, then (b) stashing a refresh token in 1Password. Kay pushed: "once it is in 1password, how do I do the reconnect? I thought I wouldnt have to do this once its in 1password."

## Decisions

### How do skills/scheduled jobs authenticate to Granola?
**AI initially proposed:** OAuth once → capture refresh token → 1Password → wrapper mints access tokens (still MCP-shaped).
**Chosen (after Kay pushback + discovery):** Granola exposes a **static API key** + a public REST API at `public-api.granola.ai` (separate from the OAuth MCP). Build `~/.local/bin/granola-api` reading `op://GB Server/Granola API Key/password`, curling REST directly. Disconnect the MCP entirely.
**Reasoning:** OAuth-MCP credentials are owned by Claude Code's internal client, not 1Password — so "put it in 1Password" does NOT eliminate the reconnect for an OAuth MCP. Only routing *around* the MCP (static key + direct REST + wrapper) delivers the "set once, works forever, works headless" property Kay expected. Username/password in 1Password is login-storage only and 401s the MCP (verified live).
**Pattern:** #pattern/oauth-mcp-bypass-with-1password-wrapper

## Alternatives Considered
- Re-OAuth each session / `/mcp` reconnect — rejected: defeats headless + scheduled use; the original problem.
- Refresh-token-in-1Password + MCP-shaped wrapper — rejected: still couples to Claude Code's token model.
- Keep MCP, accept manual reconnects — rejected: prior launchd failures + Kay's explicit "I shouldn't have to do this" requirement.

## Why This Trace Matters
The credential ladder ([[feedback_check_credential_source_before_auth]], [[feedback_all_skills_use_1password]]) says "1Password first." This trace adds the *architectural* corollary: for an **OAuth/PKCE MCP**, putting a credential in 1Password is insufficient — the MCP client still owns its own token cache. A future agent must check whether the service has a **static API key + public REST API** and build a thin wrapper around that BEFORE assuming 1Password alone solves the reconnect problem. Probe `public-api.<service>` / `docs.<service>/api-reference` before concluding "OAuth-only."

## Key Insight
"Put it in 1Password" fixes static-key services, not OAuth MCPs. For OAuth MCPs, the durable fix is to discover the static-API-key path and wrap it — bypassing the MCP, not feeding it.
