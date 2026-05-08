---
schema_version: 1.1.0
date: 2026-05-08
type: trace
importance: medium
target: process
tags: ["date/2026-05-08", "trace", "domain/migration", "pattern/shadow-mode", "topic/mutating-skill", "topic/sheets-doublewrite", "topic/timer-migration", "status/applied"]
---

# Mutating skills cannot use shadow-mode for migration — cutover required

## Trigger

While migrating timers from iMac launchd to server systemd, the standard pattern was: enable on server, leave iMac plist active, compare auto-fire results next morning, retire iMac plist after one shadow-mode cycle. This worked cleanly for read-mostly skills (snapshot trio, email-intelligence, relationship-manager, deal-aggregator, launchd-debugger).

When the migration hit `nightly-tracker-audit` (Daily 23:30 ET, mutates Industry Research Tracker Google Sheet), shadow mode would mean BOTH iMac AND server fire at 23:30 against the same Google Sheet. Same-row writes would race. Last-write-wins. Status moves, WEEKLY REVIEW re-sorts, Drive folder moves — all contended.

## Decision

Defer `nightly-tracker-audit` migration from tonight to Saturday morning. Use cutover (not shadow) pattern: disable iMac plist + enable server timer atomically. Eyes-on validation Saturday morning to catch any failures before next 23:30 fire.

## Alternatives Considered

- **Shadow mode anyway** — accept the double-write race for one cycle, manually reconcile any conflicts. Rejected: Sheet writes are not idempotent at the row level (e.g., status moves with timestamp suffixes); manual reconciliation cost > deferral cost.
- **Disable iMac plist tonight, enable server timer** — eliminates the race but commits the migration without validation. If server has an unrelated bug (gog auth, MCP, validator), 23:30 fires fail silently and iMac no longer covers. Rejected for tonight; safe to do Saturday with eyes-on.
- **Add a Sheet-level "last writer wins by mtime" guard at app layer.** Rejected — would require modifying the skill code to add advisory locking, scope creep beyond migration.
- **Migrate everything tonight including nightly-tracker-audit; debug Saturday morning if broken.** Rejected — Kay's calendar Saturday morning isn't open for emergency Sheet recovery if Friday-night double-write corrupted state.

## Reasoning

Shadow mode works only when both detectors produce *equivalent* output without conflict. The conditions:

1. **Read-only skills** — both detectors observe the same input, produce the same artifact. Last-write-wins is benign (artifacts overwrite to same content).
2. **Different output destinations** — both fire but write to non-overlapping resources. No conflict.
3. **Idempotent mutations** — both fire, mutate the same resource, but the mutation is idempotent (set-not-append). Final state is correct regardless of order.

`nightly-tracker-audit` violates all three. It mutates a Google Sheet (shared mutable resource) with non-idempotent operations (status moves, sort re-orders, Drive folder relocations). Two simultaneous fires can produce inconsistent state — e.g., row A gets sorted to position 5 by iMac fire, then to position 8 by server fire because iMac's pre-sort state was different.

Cutover (not shadow) is the safe pattern for mutating skills. Loss of fallback risk is real (if server fails, no recovery without manual re-run), but it's bounded (single 24h cycle, easily detectable Saturday morning, easy to roll back by re-enabling iMac plist).

## Why This Trace Matters

The migration pattern doctrine for the remaining 6-8 timers needs this distinction explicit:

- **Shadow-mode candidates** (read-mostly, idempotent, different destinations): email-intelligence, relationship-manager, launchd-debugger, deal-aggregator variants, snapshot refresh trio. Pattern proven tonight.
- **Cutover-only candidates** (mutating shared resources): `nightly-tracker-audit`, `weekly-tracker`, `conference-discovery` (all touch Sheets), `niche-intelligence` (touches Industry Research Tracker), `jj-operations-sunday` (touches per-niche target sheets).

Future migrations should classify each timer up front. Shadow vs cutover is not interchangeable.

## Key Insight

**Shadow mode is a luxury of read-only systems.** The default migration pattern (both fire, retire iMac after one clean cycle) silently assumes idempotency. For any skill that mutates a shared resource, that assumption is wrong, and the migration must use cutover. The pre-migration question to ask: "If both fire simultaneously, what state ends up in the shared resource — correct, or undefined?" If undefined, cutover.
