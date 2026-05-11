---
name: Conference Pipeline — preserve "week of" row formatting
description: Never clear or overwrite the formatted "week of" header rows on the Conference Pipeline sheet. Only touch data rows.
type: feedback
originSessionId: e01b0f15-d8be-4bd0-8424-2b86790ca0c8
---
The Conference Pipeline sheet has formatted "week of" header rows (bold, background fill, possibly merged) that visually band the weekly groupings. Every prior pass through that sheet has stripped that formatting.

**Rule:** Never `clear` or write values into a "week of" row. Only data rows underneath get touched.

**Why:** Kay flagged this as recurring 2026-04-27. Past failure pattern: when reorganizing or adding conferences I used `gog sheets clear` or `gog sheets update` over ranges that included header rows, which nukes bold + bg color + merge. The visual structure of the sheet collapses.

**How to apply:**
1. **Before any write** to the Conference Pipeline sheet, identify the "week of" rows (bold + filled cells, usually one per week-block) and exclude them from the write range.
2. **Never use `clear` on a range that spans header rows.** Operate on data-only sub-ranges (e.g., `B27:F27` not `A26:F27`).
3. **When inserting new conference rows** under a "week of" header, copy formatting from an existing data row in the same week-block (use `gog sheets format` with explicit bg/bold matching, or `--copy-validation-from` for dropdowns).
4. **When moving rows between weeks**, write only the data cells (Cols B-onward, not Col A which often holds the header marker). If Col A on the destination is part of a "week of" header span, do NOT touch.
5. **Verify after write** — re-read the header rows (`gog sheets read-format`) and confirm bold + background still present. If stripped, restore via explicit `format` command.

**Sheet:** Conference Pipeline (in OPERATIONS Drive folder; ID lookup needed at use-time per `feedback_refresh_state_before_bulk_destructive`).
