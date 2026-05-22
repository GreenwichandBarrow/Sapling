---
name: principal-only-routing-and-counting
description: "Three surfaces (JJ-routing, owner-conversations metric, PE-rollup analyzer) enforce the same principle — only true principals/owners count and route. Non-principals get a different track or no track."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 1a85352f-695a-4c11-bf94-82762838a30f
---

Only true principals (owners, decision-makers, sole proprietors) count toward G&B's principal-engagement metrics and route to principal-only channels. Non-principals (employees, partners without authority, PE-roll-up sponsors) get a different track or no JJ-route.

**Why:** Three independent traces in one week (2026-05-16 Bayonne, 2026-05-18 owner-conversations metric, 2026-05-18 Carlos PE roll-up) hit the same wall — the system was about to route a non-principal as if they were one. JJ time, owner-conv metric integrity, and analyzer classification all depend on this distinction. Conflation across surfaces signals one rule, not three.

**How to apply:**
- **JJ-routing (`skill:jj-operations`, `skill:outreach-manager`):** before adding a company to a JJ-Call-Only target list, verify the named individual is a principal (owner / founder / sole decision-maker). Non-principals → different channel or no add.
- **Owner-conversations metric (`skill:weekly-tracker`, `skill:post-call-analyzer`):** only `type:owner` calls count. Partner calls, employee calls, advisor calls = Quality bucket, never Owner-Conversations.
- **PE-rollup classification (`skill:post-call-analyzer`, `skill:relationship-manager`):** PE roll-up sponsors are exit-channel/intel contacts, NOT deal-flow (same-band price competitor). See [[feedback_pe_rollup_relationship_is_exit_channel_not_dealflow]].

Related: [[feedback_jj_blue_collar_only]], [[feedback_owner_conversations_strict_type_owner]], [[feedback_pe_rollup_relationship_is_exit_channel_not_dealflow]].
