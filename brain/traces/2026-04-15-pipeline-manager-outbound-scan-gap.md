---
schema_version: "1.2.0"
date: 2026-04-15
type: trace
title: "Pipeline-manager misses Attio list-entry creation for emailed targets (Person exists, List entry doesn't)"
tags: ["date/2026-04-15", "trace", "role/coo", "topic/pipeline-manager", "topic/attio-sync", "topic/outbound-scan", "company/mmpc"]
target: skill:pipeline-manager
importance: high
---

### Attio auto-adds People from email, but does NOT auto-add to Lists — pipeline-manager must bridge the gap
**Reasoning:** Discovered via MMPC / Timothy Wong on 2026-04-15.

Sequence:
1. JJ called MMPC 4/8, got gatekeeper (captured in Call Log 4.08.26)
2. Kay emailed `timothy.wong@mmenviro.net` on 4/9 ("Introduction, Greenwich & Barrow", Variant B)
3. Attio auto-created the **Person record** for Timothy Wong on 4/9 (from the outbound email interaction) and linked to MMPC company record
4. **No Active Deals list entry was created** — Attio's auto-sync creates Person records, not list memberships
5. Timothy responded on Slack (not email) — invisible to any Gmail-based scan
6. 6 days later, Kay had to tell COO manually that the pipeline was behind

Two separate gaps compounded:

**Gap 1 — Scan window too narrow.**
Pipeline-manager's outbound email scan uses `newer_than:2d`. An email sent 4/9 falls outside that window as of 4/11. By the time Kay surfaced it (4/15), it was 6 days stale — way beyond the scan's reach.

**Gap 2 — Missing cross-reference.**
Even within the 2-day window, the scan matches recipients against *existing Active Deals list entries*. If the recipient is only a Person record (auto-created by Attio) but not yet in the Active Deals list, the scan skips them. This is exactly backwards — an outbound email IS the signal that the list entry should be created.

**Trigger:**
- Extend outbound scan window to `newer_than:14d` (covers slow-reply JJ-route follow-ups, Variant B Days 3/6/14, vacation gaps).
- For each outbound email to an external recipient:
  - Match recipient email against Attio People (always succeeds since Attio auto-creates).
  - Check if that Person's company has an **Active Deals list entry**. If not, create one at "Contacted" stage with source inferred from context (target sheet niche column, or "cold-outreach" default).
  - Cross-reference recipient against active niche target sheets; tag list entry with niche if matched.
- Deduplicate: never create a duplicate list entry if one already exists (match by company record ID).

## Secondary learning — Slack replies are invisible to the system
Timothy responded to Kay via **team Slack**, not email. Every current scan assumes Gmail is the inbound channel. For any target routed through a Slack-enabled intermediary (DealsX platform, team Slack for JJ-route escalations, shared workspace with partners), replies will never hit pipeline-manager unless Kay surfaces them manually.

**Trigger (separate fix):** Slack MCP integration for read-only scan of Kay's Slack workspaces, pattern-matching for names/companies in active Attio records. Out of scope for immediate fix — flag for future system-expansion pin.

## Learnings
- "Attio auto-creates" is a partial contract — it covers People but not List memberships. Never assume list coverage from Person existence.
- Scan windows must match the slowest cadence the route tolerates. JJ-route Day-0 outreach can wait weeks for a reply; a 2-day window creates invisible backlog.
- Channel-mix expansion (Slack, LinkedIn DMs, text) means pipeline-manager needs inbound scans beyond Gmail, or explicit Kay-surfaces-it protocols for non-Gmail channels.

## Remediation
- Immediate (done today): Manual Attio entry for MMPC at Contacted stage.
- Next week (Apr 20+ during Week-1 agent refactor): fix pipeline-manager outbound scan per Trigger above.
- Future: Slack inbound scan.

frame_learning: true
