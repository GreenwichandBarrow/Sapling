---
name: Salesforge caused spam
description: Salesforge connected to Kay's mailbox/LinkedIn caused spam — disconnected both sides, evaluate before reconnecting
type: feedback
---

Salesforge MCP connection + mailbox/LinkedIn integration caused spam reaching Kay. She deleted her mailbox and LinkedIn from Salesforge directly, and MCP config was removed from .mcp.json.

**Why:** Salesforge had access to Kay's email sending infrastructure and LinkedIn. The integration generated unwanted spam activity, which directly threatens Kay's sender domain reputation — her entire business depends on clean email deliverability.

**How to apply:** Do NOT reconnect Salesforge without Kay's explicit decision after evaluating alternatives. If outreach tooling is needed, research tools that are draft-only or require explicit send approval. Salesforge's auto-send capability is fundamentally at odds with Kay's review-first workflow.
