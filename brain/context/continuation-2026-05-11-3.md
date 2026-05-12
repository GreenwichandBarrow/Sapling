---
date: 2026-05-11
type: context
title: "Continuation — 2026-05-11 #3"
saved_at: 2026-05-11T16:30:00-04:00
session_number: 3
tags: ["date/2026-05-11", "context", "topic/continuation"]
---

## Active Threads

1. **Granola MCP auth lapsed since 5/8** — silent failure. Detector returns `[]` every 5 min, today's investor call (ended ~2:45pm) never captured. Timer is healthy; the MCP itself returns "Skipping connection (cached needs-auth)."
2. **Architectural rethink in progress** — Kay flagged that the whole point of server+1Password migration was to prevent this. Weighing 4 paths: (a) re-auth Granola MCP now, (b) Granola → Zapier → Drive, (c) switch to Fireflies (native Drive export), (d) vendor-agnostic email-as-trigger via existing email-intelligence + Gmail OAuth.
3. **Task-tracker work — DONE earlier today** (commit a83c6f8). 5 verb gaps shipped, new tabs ("Completed To Do" + "Deal Aggregator Expansion") live in Drive. Structurally validated by Kay.

## Decisions Made This Session

- Confirmed Granola is NOT on 1Password (PKCE OAuth, lives in `~/.claude/.credentials.json`).
- Friday's budget-manager work = budget-reduction assessment, not a re-run. Already on tracker.

## Next Steps

1. Kay to answer: is Fireflies interest UX-driven, integration-driven, or both?
2. Surface whether Granola's post-call email summary contains decisions + action items — if yes, **email-as-trigger** likely dominates both MCP and Zapier paths (zero new infra, vendor-agnostic, one failure surface).
3. Once path decided: re-auth Granola NOW regardless (today's investor call needs capture), then implement chosen long-term path.
4. Add Slack alert on detector auth-failure + MCP health check to validator — regardless of which long-term path wins.

## Open Questions

- Fireflies vs Granola: UX equivalence on inline notes?
- Does Granola's summary email carry enough payload for post-call-analyzer's routing buckets?
- Granola REST API with API-key auth — does it exist? (Would fit 1Password pattern.)
