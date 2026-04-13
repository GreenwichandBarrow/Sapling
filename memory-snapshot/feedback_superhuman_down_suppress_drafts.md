---
name: Suppress draft items when Superhuman MCP is down
description: When Superhuman MCP is unavailable, do not present draft status or "pending send" items — Gmail view is stale and misleading
type: feedback
---

When Superhuman MCP is unavailable (not running with --remote-debugging-port=9333), do NOT present draft status, stale drafts, or "pending send" items in the morning briefing. Gmail's draft view does not reflect what Kay has actually sent or cleared through Superhuman.

**Why:** Kay works in Superhuman. Gmail shows drafts that were already sent via Superhuman. Presenting these as "stale" or "pending" wastes Kay's time and erodes trust in the briefing.

**How to apply:** If Superhuman MCP connection fails, skip the Draft Status section entirely or mark it "Superhuman offline — draft status unavailable." Never fall back to Gmail draft data as if it's current.
