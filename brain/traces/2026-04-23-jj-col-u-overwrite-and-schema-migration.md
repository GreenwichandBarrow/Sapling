---
schema_version: 1.1.0
date: 2026-04-23
type: trace
title: "JJ Col U Overwrite — Pace Cannot Be Measured Without Per-Attempt Columns"
tags: ["date/2026-04-23", "trace", "topic/jj-operations", "topic/sheet-schema", "topic/pace-measurement", "topic/data-structure-bottleneck", "topic/multi-attempt-tracking", "person/jj"]
had_human_override: true
importance: high
target: skill
people: ["[[entities/kay-schneider]]", "[[entities/jj]]"]
companies: []
---

# Trace: JJ Col U Overwrite + Schema Migration to 6-Col Date+Status Pairs

## Context

Kay raised a concern: "JJ said yesterday he finished with the 4/20 list. So I think he is behind our 40/day goal. Can you look and see if you can tell how many he is calling per day and see if we need to reduce our lists?"

This unlocked a 3-stage analytical arc, each stage producing a wrong recommendation, with Kay's domain knowledge unlocking the actual problem at the end.

**Stage 1 (wrong by tab grouping):** First analysis grouped dials by Call Log tab name (e.g., "Call Log 4.20.26"). Reported JJ at 36-39 dials/day, ~93% of target — recommendation: hold 40/day, fix logging gap on 4/22. Tab name was the estimated date, not actual dial date.

**Stage 2 (wrong by Col U as last touch):** After Kay's correction "tab name is estimated, Col U is actual dial date — please re-analyze," the second pass grouped by Col U date. Reported 5 dark workdays out of 13 (4/15-17 + 4/22-23) and 20-25 dials/day on working days. Recommendation: attendance gap is primary issue, reset target to 25/day. Both numbers wrong because the 5 "dark days" were actually re-dial days and the ~21/day was undercount.

**Stage 3 (Kay's insight unlocked it):** "I think what is happening is the ones that don't answer he is calling back the next day and we don't have a column to track the 2nd attempt." This identified the actual bottleneck: Col U holds only ONE date per row. When JJ re-dials a No Answer, he overwrites the original date (or doesn't update because the row is "already logged"). Col U is the date of LAST touch for that company, not "dials made on date X." Pace is unmeasurable from this schema.

## Decisions

### Schema is the bottleneck, not JJ's behavior
**AI proposed (twice):** Behavioral interventions — "hold 40/day," "reset to 25/day," "investigate logging gap," "have attendance conversation."
**Chosen:** Add 2nd-attempt columns. Acknowledged Stage 1 + Stage 2 recommendations were both wrong because the data structure didn't permit the question being asked. JJ's actual pace is unknown until the schema captures multi-attempts.
**Reasoning:** Stage 1 and Stage 2 both treated the visible data as ground truth without questioning whether the schema could represent reality. Kay's domain knowledge ("they don't answer, he calls back") was the unlock. The fix is structural; behavioral recommendations on top of an undercounting schema are noise that creates false-narrative pressure on JJ.
**Pattern:** #pattern/check-schema-can-represent-question-before-analyzing-data

### Column-based migration over row-based (preserve list workflow)
**AI proposed:** Activity Log tab — one row per dial event. Pace becomes a one-line query.
**Kay rejected:** "A row does not make sense" — same company appearing 4 times breaks JJ's call-list workflow, can't easily see prior attempts without scrolling.
**Chosen:** Column-based pairs. Schema specified by Kay: JJ: 1st Call Date / JJ: 1st Call Status / JJ: 2nd Call Date / JJ: 2nd Call Status. Two-attempt cap, then move to Do Not Pursue.
**Reasoning:** JJ's mental model is "list of companies to call." Row-per-dial breaks that. Column-per-attempt preserves the list while capturing per-attempt timestamps.
**Pattern:** #pattern/preserve-user-mental-model-when-changing-schema

### 39a (clean swap) over 39b (minimum migration)
**AI recommended 39b** (rename T/U headers, append V/W as new cols at end — zero migration risk).
**Kay chose 39a** (swap T↔U values, insert V/W as new "2nd Call" cols, shift V/W → X/Y — clean visual order, ~150 row swaps required).
**Reasoning (Kay's):** Visual consistency matters more than migration cost. Status-then-Date for 1st but Date-then-Status for 2nd would confuse JJ.
**Pattern:** #pattern/visual-consistency-over-migration-minimization

### Don't change historical tabs ("don't misrepresent the data")
**AI implicitly assumed** all tabs (Full Target List + Call Log) would migrate.
**Kay specified:** Migrate Call Log 4.21.26 forward + the "template" (Full Target List). Historical Call Log tabs (4.20.26 and earlier) preserved as-is to maintain audit trail. Their data is in the OLD schema; reinterpreting under the NEW schema would mislabel historical statuses as dates.
**Reasoning:** Schema migrations on data already collected under a different structure CAN preserve values mechanically (T↔U swap is reversible) but the AUDIT TRAIL meaning changes. JJ's old logs are evidence of his work under the old rules; rewriting them creates retroactive ambiguity.
**Pattern:** #pattern/preserve-audit-trail-on-schema-migration

### Migration executed via subagent with snapshot-first protocol
**Chosen:** Delegate to subagent per `feedback_subagent_sheet_write_safety` (post 4/17 near-miss). Snapshot every tab before mutation, swap row-by-row, validate read-back diff against snapshot, abort on any mismatch.
**Outcome:** 868 row swaps validated, 0 mismatches. 4 future Call Log tabs migrated cleanly (40 rows each preserved, T-Y empty as expected).
**Reasoning:** This is exactly the kind of high-blast-radius write that needs the safety protocol. Subagent delegation also keeps the analytical context out of the migration execution context.
**Pattern:** #pattern/snapshot-validate-on-shared-sheet-mutation

## Why This Trace Matters

Three failure modes are documented here that a future agent would absolutely repeat:

1. **Reading tab names as ground truth dates.** Spreadsheet tabs are organizational — they often have date-like names that don't reflect when the row data was actually entered. Always check whether there's a per-row timestamp column.
2. **Reading "single-value-per-row" fields as "events per day" data.** A Col like "JJ: Call Date" looks like an event timestamp but is actually a state-snapshot ("most recent call"). Counting populated dates groups by "rows last touched on date X," not "events on date X." Different metric.
3. **Recommending behavioral fixes on top of structural-data bottlenecks.** Stage 1 and Stage 2 both produced confident wrong recommendations because the schema couldn't represent the question. Both would have created false friction with JJ if Kay had acted.

The schema migration also documents the Date-then-Status order convention and the 2-attempt cap rule — both Kay-specific that a future agent would otherwise need to discover.

## Key Insight

Before delivering an analytical recommendation about a person's behavior based on a sheet of data, verify that the schema can represent the metric being measured. "Daily dials" requires a per-dial event record OR per-attempt columns. "Latest call date" + "latest status" cannot answer "dials per day" — it can only answer "rows touched on or before date X." Don't conflate the two.

## Closure Mechanism

- Migrated Premium Pest Management sheet (`1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`) to 6-col schema (T-Y) on Full Target List + Call Log 4.21.26 / 4.22.26 / 4.23.26 / 4.24.26.
- Updated `.claude/skills/jj-operations/SKILL.md` — new column docs, harvest reads across all weekly tabs, pace measured by populated date cells (T or V) where date = today, two-attempt cap rule, never-overwrite-1st-call protection.
- Slack message sent to JJ via #operations-sva explaining new layout (HTTP 200).
- Snapshots saved at `/tmp/jj-schema-migration/` for rollback if needed.
- Stage 1 and Stage 2 recommendations explicitly retracted in conversation per `feedback_close_the_loop`.
