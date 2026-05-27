---
name: feedback-task-tracker-pack-to-top
description: "Day tabs and Week tab MUST keep items packed at the top of the priority-slot range (rows 14-28 day tabs / rows 24-38 Week tab). No leading empty rows, no gaps between items. Codified 2026-05-26."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37de3c90-d2d0-44f1-9b4b-ddb0727158c9
---

Every task-tracker-manager verb that writes to a day tab or Week tab MUST keep the priority-slot range packed: items at the top, empty slots only below the last item. No leading empty rows. No gaps between items.

**Why:** Kay 2026-05-26: *"Skills should not allow empty rows at the top of the daily lists."* Empty slots at the top or between items make the list look messy, force visual scanning past whitespace to find the next item, and break the implicit "your day from top down" reading model. The 15-slot range is a capacity ceiling, not a fixed seating chart — items live at the top until used up, empties live below as available capacity.

**How to apply:**

1. **Day tabs (rows 14-28, cols A=status, B=task):** every verb that touches a day tab — `promote`, `schedule-to-day-slot`, `move-day-item`, `distribute-week`, `sync-done-status`, `recurring-add` stamping — packs items into the lowest-numbered empty slots. Never write to slot N if slots 1..N-1 are empty.

2. **Week tab (rows 24-38 per day-block):** same rule for each of the 7 day-blocks. Recurring stamps + cross-file carryover writes pack-to-top per day.

3. **schedule-to-day-slot with `--slot N`:** if Kay explicitly names a slot, honor it (override pack-to-top). But warn if N skips empty earlier slots: `WARN: scheduling to slot 5 leaves slots 1-4 empty — confirm intent`.

4. **Mid-week edits Kay makes manually in the Sheet UI** create gaps when she deletes a task mid-list. The `reformat` verb should detect + auto-compact (move later items up to fill gaps). Add this as a `reformat` extension.

5. **build-week (weekly-files architecture):** the carryover-pull + recurring-stamp into the new file's day tabs must produce packed lists. The current `_stamp_recurring_day_tabs` + `_carryover_cross_file` helpers use next-empty-slot logic, which packs naturally as long as the day tab starts empty (which it does after the day-tab clear step). VERIFIED 2026-05-26 sandbox rehearsal.

6. **distribute-week (legacy mode):** if invoked under `--legacy`, the fan-out from Week tab to day tabs must also produce packed lists on day tabs (skip empty Week-tab slots when writing to day tabs).

**Verification:** after any write that touches priority slots, the slot range should satisfy: for all i, j in [1..15] where i < j, if slot j is non-empty, slot i is also non-empty. (Empty rows only at the bottom.)

**Re-pack utility:** ad-hoc compaction can be done by reading the 15-slot range, filtering to non-empty (status, task) pairs, padding empties at the bottom, writing back. Inline-able in any verb. The 2026-05-26 manual re-pack on `TO DO 5.24.26` used this pattern (see Tue Week tab post-fix: 1 item at slot 1 + 14 empty below; Wed day tab: 11 items packed slots 1-11 + 4 empty below).

See also: [[user-task-management]], [[feedback-no-time-blocking-item-list-scheduling]] (related — item-list scheduling means the LIST should look like a list, not a sparse grid).
