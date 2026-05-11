---
name: Gmail drafts cleared, use Superhuman only for email reference
description: Kay cleared all stale Gmail drafts on April 1. Never reference Gmail drafts — only use Superhuman for email/draft status.
type: feedback
---

Kay cleared all old Gmail drafts on April 1, 2026. They were all stale. From now on, NEVER use Gmail (gog) as a reference for draft status. Only use Superhuman MCP for email and draft information.

**Why:** Gmail shows stale drafts that don't reflect Superhuman's state. Presenting Gmail draft data causes false positives (items flagged as "stale" that were already sent or intentionally deleted).

**How to apply:** In email-intelligence and pipeline-manager, skip any Gmail draft queries. If Superhuman MCP is unavailable, report "draft status unavailable" rather than falling back to Gmail. This supersedes the previous feedback about suppressing drafts when Superhuman is down — the rule is now stronger: never use Gmail drafts at all.
