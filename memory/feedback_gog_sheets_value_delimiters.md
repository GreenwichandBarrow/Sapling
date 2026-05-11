---
name: gog_sheets_value_delimiters
description: Never use pipe `|` or comma `,` in `gog sheets update` value args — they're parsed as cell/row delimiters and corrupt adjacent cells.
type: feedback
originSessionId: a7305dfd-d3d9-44c7-840b-f8de8eb9bfd8
---
The `gog sheets update` CLI parses positional value arguments using `|` as cell-delimiter and `,` as row-delimiter. Passing either character INSIDE a cell value will split the string across multiple cells (or rows) and overflow into adjacent cells, corrupting unrelated data.

**Symptoms:**
- A long Notes-column write splits into 2+ cells
- Content overflows into the next row (e.g., row N+1 P column gets clobbered)
- The visible Sheet shows partial values where you expected the full string

**Safe write paths (in order of preference):**
1. **`--values-json` flag** — pass values as JSON, no delimiter parsing. Always safe for content with punctuation.
2. **Direct Sheets API** via Python script (`spreadsheets.values.update` with the OAuth refresh-token pattern from `scripts/format-gdoc.py` / `/tmp/delete_ib_row11.py`).
3. **Strip `|` and `,` from the value string** before passing positionally. Replace with parentheses, dashes, or periods.

**Forbidden:**
- `gog sheets update {sheet} --range A1 "long, comma-separated, value"` → corrupts row 1
- `gog sheets update {sheet} --range A1 "value with | pipes inside"` → corrupts cells A1-AN1

**How to apply:**
- For ANY Notes column write longer than ~10 words OR containing user prose (which often has commas) — use `--values-json` or the direct API. Don't pass positionally.
- For simple single-word writes (status flags, IDs, dates) — positional is fine.
- After any write that includes punctuation, verify by re-reading the cell range to confirm no corruption. If corrupted, restore from snapshot and retry with the safe path.

**Source:** Discovered 2026-05-01 during the NPMA WIPM Forum conference pipeline status update — first attempt corrupted row 29 (overflowed into ACG NJ NextGen's P column). Caught immediately, restored from snapshot, retried via safer path.

**Adjacent rule:** Always snapshot pre-write per `Before writing to a Google Sheet` pre-flight in CLAUDE.md. This is the rule that lets you recover when the delimiter bug bites.
