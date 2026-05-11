---
name: Pool Select-First, Then Enrich (Phase 2 invariant)
description: Sunday-night target-discovery Phase 2 MUST select this week's 200-row call pool BEFORE enriching. Rows enriched = rows called. Learned 2026-04-20.
type: feedback
originSessionId: c9463652-c8f2-4d3d-b096-737d00fef818
---
## Rule

Target-discovery Phase 2 must select the exact 200 rows that will populate the Mon–Fri Call Log tabs BEFORE running any enrichment step. Enrichment (Linkt / Apollo / web research) then operates only on that pool. Never enrich "oldest un-enriched rows in the Full Target List" as a proxy — it silently desyncs from what jj-operations actually writes to tabs.

**Why:** On Monday 2026-04-20, JJ opened his Call Log 4.20.26 tab to find 36 of 40 rows with blank Col K (Owner Name). Root cause: Phase 2 enriched a different 200 rows than jj-operations prep wrote to tabs. The two "top 200" lists overlapped by coincidence but drifted over time, burying the enriched rows under already-called ones. JJ's shift stalled 20 min in. Apollo rescue cost ~184 credits to backfill.

**How to apply:**
- Phase 2 Step 1 selects the pool (Col T empty, row-order sorted, top 200) and persists row numbers to `brain/context/jj-week-pool-{date}.md`.
- Step 2 (enrichment) loops over that artifact only — not over the Full Target List directly.
- Steps 3–4 (PE re-screen, warm intro) operate on the same pool; any removal triggers a backfill from the next-in-queue rows.
- Step 5 (jj-operations prep) reads the post-backfill pool artifact — never re-selects.
- `.claude/hooks/enrichment_integrity_check.py` enforces the invariant at the end of the pipeline; jj-operations refuses to send the Slack if the hook fails.

**Corollary:** if Linkt or Apollo credits run low mid-pool, STOP and escalate. Don't enrich a different (smaller) set — that re-introduces drift.
