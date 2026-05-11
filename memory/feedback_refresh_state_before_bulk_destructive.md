---
name: Refresh state snapshots before bulk-destructive operations
description: When bulk-deleting based on a captured snapshot (filter list, label list, sheet rows, etc.), always re-fetch live state right before the delete loop runs — never reuse a snapshot taken earlier in the same session if any creates/modifies happened in between.
type: feedback
originSessionId: 54785998-5c5c-4c8d-956a-e32941f2ea6d
---
**Rule:** Before any bulk-destructive operation (mass delete, mass overwrite, mass archive), re-fetch the live state from the source of truth and rebuild the "things to delete/touch" set from that fresh snapshot. Never reuse a snapshot file that was generated earlier in the session if intermediate creates/modifies have happened.

**Why:** 2026-04-26 — during Gmail filter cleanup, I built a "to-delete" list using `/tmp/filter-audit/labels.json` captured at the start of the session. After capture, I created 2 new auto/* labels (`auto/team`, `auto/industry research`) and their filters. The deletion logic used the stale labels file to determine which Label_IDs were "auto/*" (and thus protected from delete). The new labels weren't in the stale snapshot, so the filters routing to them got deleted alongside the legacy filters they were meant to replace. Recovery required recreating the 2 lost filters. Backfill was intact (labels persist on historical threads), but going-forward routing was broken until recovery.

**How to apply:**
- For Gmail filters: re-run `gog gmail filters list ... > current.json` and `gog gmail labels list ... > current-labels.json` immediately before the delete loop. Build the "to-delete" set from those two fresh files, not from earlier session artifacts.
- For Google Sheets: re-fetch the target tab's row IDs/values right before mass-update, not from a snapshot taken at task start.
- For Attio: re-query record IDs immediately before bulk action.
- The principle: any snapshot has a TTL of "until the next mutation in this session." Once you mutate, the snapshot is stale.
- Cheap to refresh, expensive to recover from a wrong delete. Refresh by default.
