---
name: drive-research-folder-canonical
description: "The canonical \"RESEARCH\" folder Kay refers to is a top-level Drive folder (NOT \"ANALYST - RESEARCH & DUE DILIGENCE\"). MEETINGS folder for post-call-analyzer artifacts lives at RESEARCH/MEETINGS."
metadata: 
  node_type: memory
  type: project
  originSessionId: 7dc0f575-9c45-4aad-9c1c-4d9782371a2c
---

# Canonical RESEARCH folder location

When Kay says "the research folder" — she means the top-level `RESEARCH` folder in Drive, NOT `ANALYST - RESEARCH & DUE DILIGENCE` (which sounds similar but is a different folder from the 5/12 restructure).

## Key folder IDs

- **RESEARCH (canonical "research" folder)** — children include BRIEFS, BROKERS, CONFERENCES, FIREFLIES, INDUSTRY ANALYSIS & SCORING, MEETINGS, OUTREACH, PE DEALS. Find via `gog drive tree | grep "^RESEARCH/"`.
- **RESEARCH/MEETINGS** — `1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz` — post-call-analyzer outputs (Google Docs, 1-2 pages each, one per processed call).
- **RESEARCH/BRIEFS** — `1qDTfP3YImnOK8n_wHXy2jTxzZi_UtzDQ` — pre-meeting briefs (where meeting-brief skill outputs go).
- **RESEARCH/FIREFLIES** — pre-Granola call-recording artifacts. Legacy.
- **ANALYST - RESEARCH & DUE DILIGENCE** — `1kUz7hJ3we-xTyabmytDH1u2egacbx5FL` — DIFFERENT folder. Has ACTIVE DEALS, FINANCIAL MODELS, INDUSTRY RESEARCH, WEEKLY AGENDAS subfolders. Not where call analyses go.

## Why this matters

Precipitating incident — 2026-05-13 post-call-analyzer demo. I created the MEETINGS folder under `ANALYST - RESEARCH & DUE DILIGENCE` because my Drive search for "research" returned that folder, missing the canonical top-level `RESEARCH` folder entirely. Kay had to manually move MEETINGS to the correct parent and flag the location issue.

The `gog drive search "name contains 'research'"` query I ran did NOT surface the top-level `RESEARCH` folder. `gog drive tree | grep "^RESEARCH/"` does — the tree command is the reliable way to find canonical top-level folders.

## How to apply

Whenever a skill or scheduled job needs to create a Drive artifact under "the research folder":
- Default to `RESEARCH/<subfolder>` via the top-level path
- The post-call-analyzer wrapper / scheduled job hardcodes `--parent=1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz` for MEETINGS writes — that ID is stable
- For new subfolders, create them under the top-level RESEARCH folder, not under ANALYST

## Linked rules

- [[project_drive_research_dd_restructure_2026_05_12]] (5/12 restructure context — but does NOT govern this folder)
- [[feedback_folders_not_named_after_people]] — function-based folder names rule still applies
