---
name: Never hardcode column letters in skills
description: Use header-based column lookup (col-lookup.sh) instead of Col O, Col K, etc.
type: feedback
---

Never reference Google Sheets columns by letter (Col O, Col K, etc.) in skills. Use the header-based lookup script `scripts/col-lookup.sh` to resolve header names to column letters at runtime.

**Why:** Kay's insight — hardcoded column letters are like hardcoded cell references in Excel. If anyone inserts a column, every downstream reference shifts silently. Wrong data, not errors. The INDEX/MATCH pattern (column header × row key = exact cell) is bulletproof regardless of column or row movement.

**How to apply:** Skills call `scripts/col-lookup.sh <sheet_id> <tab> "Header Name"` to resolve columns. For cell-specific operations, use `--cell "Company=Target Name" "Header"` to get exact cell coordinates. Migration is incremental — target-discovery first, then cascade to other skills. Plan approved 2026-04-04.
