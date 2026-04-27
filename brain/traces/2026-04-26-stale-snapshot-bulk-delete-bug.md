---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Self-inflicted bulk-delete bug — used stale label snapshot, deleted 2 freshly-created auto/* filters
had_human_override: false
importance: high
target: memory feedback_refresh_state_before_bulk_destructive.md, process
tags: [date/2026-04-26, trace, topic/bulk-operations, topic/state-management, pattern/post-mortem, domain/technical]
---

# Decision Trace: Refresh state before bulk-destructive ops

## Context

During the Gmail filter migration, I:
1. Captured a snapshot of all Gmail labels at session start (`/tmp/filter-audit/labels.json`).
2. Created 2 new labels mid-session (`auto/team` Label_38 and `auto/industry research` Label_39) plus their filters.
3. Built the "to-delete" set for the bulk filter cleanup using the SNAPSHOT from step 1, which did not include Label_38/39.
4. Deletion logic: "delete any filter whose action label ID is NOT in the auto/* set." Since 38/39 weren't in the snapshot's auto/* set, the filters routing to them got included in the delete batch.

Result: my own newly-created `auto/team` and `auto/industry research` filters were deleted alongside the legacy filters they were meant to replace. The labels persisted (deletion only removes filters, not labels), and historical backfill held — but going-forward routing was broken until I noticed and recreated the 2 filters.

## Decision

Saved feedback memory `feedback_refresh_state_before_bulk_destructive.md` with the rule: *"Always re-fetch live state right before bulk-destructive ops. Never reuse a snapshot taken earlier in the session if intermediate creates/modifies happened."*

## Alternatives Considered

1. **Just be more careful next time** — rejected. Discipline isn't a fix; it's a hope. The pattern (snapshot → mutate → use stale snapshot) is the actual failure mode and needs codification.
2. **Track all mutations via a session log and validate before any bulk op** — overkill for the cost. Re-fetching is cheap (~1 API call); session-log machinery is heavy.
3. **No memory, just remember the recovery** — rejected. The bug is silent (the deletion appears successful). Without an explicit rule, next session repeats the failure.

## Reasoning

Snapshots have a TTL of "until the next mutation in this session." Once you create or modify state, any earlier snapshot is stale and unsafe for use as the basis of a destructive operation. The cost of refreshing is one API call; the cost of a wrong delete is recovery work + potential silent data loss. Cheap-to-refresh, expensive-to-recover.

## Why This Trace Matters

Future agents doing bulk operations on Gmail filters, Google Sheets rows, Attio records, etc., will be tempted to reuse a snapshot file generated earlier in the session for "efficiency." This trace is the specific receipt: doing exactly that on 2026-04-26 deleted 2 filters that had to be recreated from scratch. The new memory codifies the rule; this trace documents WHY the rule exists.

## Key Insight

Bulk-delete bugs based on stale state are silent failures. The deletion succeeds, no error fires, and the bug only surfaces when a downstream consumer (in this case, my own verification step listing filters by label) reveals the missing piece. Make the refresh a hard precondition, not a recommendation.
