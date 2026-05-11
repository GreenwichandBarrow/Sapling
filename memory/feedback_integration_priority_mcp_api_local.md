---
name: Integration priority — MCP first, API second, ask before local
description: When building any skill needing an external integration, check MCP availability first, then API, then ask Kay before falling back to local
type: feedback
originSessionId: d5485724-ca82-4a50-bf98-38302fa9db3d
---
When building any skill that needs to integrate with an external tool, service, or data source, follow this priority order:

1. **Check for an MCP server first.** Search the `mcp__<service>__*` tool inventory + `~/.claude.json` `mcpServers` config. If an MCP exists and is healthy → use it.
2. **If no MCP, check for a public API.** Web search the vendor's developer docs. If a usable API exists → use it.
3. **If neither MCP nor API is available (or both are down), STOP and ask Kay.** Surface the integration gap and let her decide between (a) request/build an MCP, (b) request the vendor add API, (c) plan a local-only workaround, or (d) skip the integration.

**Why:** Phase 4 (post-call-analyzer Granola sidecar) was originally designed last night around watching a local cache file on iMac, accepting lazy-flush lag, and missing phone + MacBook calls entirely — because the existing Granola MCP server (`https://mcp.granola.ai/mcp`) was never checked. Three existing skills already use that MCP (niche-intelligence, meeting-brief-manager, others). Switching to MCP-based design (server-side puller) collapses to one source of truth across all 3 devices and eliminates the iMac sidecar. The cost of skipping the MCP check was almost a multi-hour build of the wrong architecture.

**How to apply:**
- Fires before any new skill SKILL.md that integrates with an external service.
- Fires before any architecture decision involving "how does the system get data from / push data to {external system}."
- Especially relevant when an MCP server appears in the session-start "still connecting" list — connecting is not broken; wait for connection or run `ToolSearch` with the service name before assuming unavailable.
- When Kay shares a constraint mid-design ("Granola is on phone too"), re-run this check — the new constraint may invalidate a non-MCP path that worked under the old assumption.
- Applies symmetrically: MCP that exists but is *unhealthy* (auth broken, rate-limited, offline) → still surface to Kay rather than silently falling back to local. She decides whether to fix the MCP or work around it.
