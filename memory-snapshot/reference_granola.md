---
name: Granola MCP & Integration
description: Granola meeting intelligence — MCP server configured, Attio native integration enabled, stealth recording tool
type: reference
---

**Granola** — stealth meeting intelligence tool. Captures audio locally on laptop, no bot, no participant notification.

**MCP Server:** Configured in `.claude.json` under this project.
- URL: `https://mcp.granola.ai/mcp`
- Transport: HTTP
- Authenticated via OAuth (completed 2026-03-14)
- Tools: `query_granola_meetings`, `list_meetings`, `get_meetings`, `get_meeting_transcript`

**Native Attio integration:** Enabled in Granola settings. Auto-matches meeting notes to CRM contacts/companies/deals.

**Still to build:**
- Granola → `brain/calls/` automation (pull meeting notes into vault)
- Granola action items → Motion tasks

**Replaces:** Fireflies.ai (canceled 2026-03-14). Fireflies API key still in memory but deprecated.
