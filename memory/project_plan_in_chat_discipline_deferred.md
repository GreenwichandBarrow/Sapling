---
name: Plan-in-chat / execute-in-code discipline — deferred at current scale
description: 2026-05-11 decision to NOT adopt the "draft prompts in cheap Claude AI, paste into expensive Claude Code" technique from the Clay+Claude Code GTM transcript. Friction outweighs token savings at G&B's current volume. Trigger to revisit recorded.
type: project
---

Decision: Do not adopt the "plan in cheap Claude AI chat, execute in Claude Code" token-discipline technique from the 2026-05-06 Clay+Claude Code GTM session (see `[[calls/2026-05-06-clay-gtm]]`). Skip the workflow split for now.

**Why:** Technique pays off when tokens are a real operating expense (Sales Captain runs 100K-emails/month motions; their daily token spend is meaningful and visible). G&B's daily ops are NOT token-bound — most skills run via systemd on small payloads (sheet reads, ~50 inbound emails/day, a few hundred Apollo lookups). The biggest token consumers are already gated behind triggers (target-discovery enrichment fires on niche-activation or weekly refill, not daily). The cognitive friction of "draft prompt in claude.ai web → copy → paste into Claude Code" outweighs the savings at this volume.

**How to apply:**

1. Do not propose the plan-in-chat workflow as standard operating procedure in any skill, briefing, or CLAUDE.md update.
2. Keep using Claude Code directly for both planning and execution.
3. Continue the existing discipline of using subagents for expensive work — that's the functional equivalent at our scale (offloads heavy work without context-switching tools).

**Trigger to revisit (any one of):**
- Outbound scale grows 10x via DealsX expansion (Kay's curated motion crosses ~500-1000 personalized sends/week)
- Apollo + Claude API bill becomes a line-item visible on the monthly burn report (currently lost in noise)
- A specific skill's per-fire token cost crosses a threshold worth optimizing (e.g., a single niche-intelligence run consuming >$5 in Claude API costs)

When any trigger fires, re-read the Clay+Claude Code call note and reconsider. Until then: skip.
