---
name: feedback-sheet-writes-verify-and-grow-capacity
description: Verify Sheets writes actually persisted (merged cells silently drop them); grow template capacity instead of forcing overflow
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aeb6bdeb-6ad3-4e99-bb96-8eb8797d497b
---

Two linked lessons from the 2026-05-31 Week-tab task spread (Kay caught both):

1. **Verify persisted, don't trust the write call.** Google Sheets silently drops `values.update` writes that land in **merged cells** — only the merge's top-left cell takes a value, the rest are ignored with NO error. On 2026-05-31 I wrote 16 Monday tasks to `Week!E17:E32`, reported "wrote 16", but rows 24+ were a merged per-day notes block (row 24 label + rows 25–32 merged), so only 9 stuck. 17 items dropped across Mon/Wed/Thu/Fri. **After any multi-row Sheets write, read the range back and assert count + content against the source.** Know each tab's merged regions (fetch `sheets.merges`) before writing into a row range.

2. **Grow the template when real volume exceeds the ceiling — don't force-fit.** When Monday legitimately needed 18 task rows against a 15/9-slot grid, the right move was to expand the structure (insert rows, raise to 20 slots), NOT to overflow into backlog, spill into notes, or let writes silently drop. Kay: "the 15 limit is now enough [=not enough], we need to grow the template to 20."

**Why:** Both failures read as "done" when they weren't — the silent kind that erodes trust. A to-do list felt slow because I kept hitting hidden structural walls and reporting sent-not-stuck counts.

**How to apply:**
- Day-tab + Week-tab priority-slot capacity is now **20** (rows 15–34), was 15. Update `DAY_SLOT_LAST_ROW`/`WK_SLOT_LAST_ROW` + builders if touching the template in code; the live 5.24.26 Week tab is already grown.
- Day tabs (Sun–Sat) still need the same 15→20 growth applied before distributing the finalized Week plan to them.
- DAILY FOCUS row lives at **row 13** on day tabs and the Week tab (Kay-added, per [[feedback-task-tracker-pack-to-top]] surface family) — never clear/override it.
- Mirrors the To Do gap-row cleanup pattern in [[feedback-task-tracker-pack-to-top]]: dead `FALSE` checkbox cells render as text; clear only cells with no BOOLEAN validation.
