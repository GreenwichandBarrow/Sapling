---
name: feedback_snapshot_col_range_validator_mismatch
description: Snapshot must be captured with A:O range (not A:P) to avoid false-positive soft mutations in the conference-discovery validator
metadata: 
  node_type: memory
  type: feedback
  originSessionId: aee13273-2463-4c92-a170-e5d1833158aa
---

Snapshot for conference-discovery must be captured with `Pipeline!A2:O500` (not A2:P500) to match the validator's `DATA_RANGE = "A2:O500"`. If the snapshot includes col P (Notes), the validator compares snapshot col P (has values) to live col P (always empty, because it reads only A:O) → generates false-positive soft mutations for every event with Notes, easily exceeding MAX_SOFT_CELL_MUTATIONS=5.

**Why:** Validator reads A:O from live sheet and uses `max(len(snap_row), len(live_row))` for iteration. If snap has 16 cols and live has 15, col P in live is always "" → spurious soft mutation.

**How to apply:** When taking the pre-run snapshot in Step 0, use range `Pipeline!A2:O500` not `Pipeline!A2:P500`. The Notes column is not needed for mutation checking. If the snapshot was already taken with P, trim it: `snap['rows'] = [r[:15] for r in snap['rows']]`.

Discovered 2026-05-31 headless run — validator failed with 18 soft mutations (all false positives from col P mismatch).
