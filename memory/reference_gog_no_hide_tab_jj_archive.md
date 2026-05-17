---
name: reference_gog_no_hide_tab_jj_archive
description: "gog CLI has no hide-tab/sheet-properties command — JJ-operations prep 'archive previous week' step is not achievable via gog"
metadata: 
  node_type: memory
  type: reference
  originSessionId: af623864-861b-4926-822a-10b4b84c9fdc
---

`gog sheets` exposes `add-tab`, `rename-tab`, `delete-tab` but **no hide-tab / updateSheetProperties / batchUpdate** command (verified v0.15.1, 2026-05-17). Hiding a tab requires Sheets API `batchUpdate{updateSheetProperties,hidden}`, which gog does not surface and `googleapiclient` is not installed on the VPS.

Consequence: jj-operations SKILL Step 1 "Archive previous week's Call Log tabs (hide, don't delete)" cannot be done through gog. The proven production rescue script `scripts/jj_build_week_tabs_2026-04-27.py` also skips hiding — established production behavior is to leave old Call Log tabs visible. This is cosmetic clutter only: harvest mode reads across ALL Call Log tabs by design, and `scripts/validate_jj_operations_integrity.py` gates solely on the 5 new Mon-Fri tabs existing with Col K populated — not on archiving.

**How to apply:** In headless JJ prep, build + validate the 5 new tabs (critical path) and treat archiving as a best-effort no-op — do NOT build a fragile OAuth token-exchange path for it in an unattended run (violates sharp-knife-first + secret-handling doctrine). If true hiding is ever required, it needs either a gog feature add or `pip install google-api-python-client` + the gog-stored token. Related: [[reference_gog_interactive_unlock_recipe]], [[feedback_never_read_config_with_secrets]].
