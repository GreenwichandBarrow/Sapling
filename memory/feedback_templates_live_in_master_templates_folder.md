---
name: templates-live-in-master-templates-folder
description: All G&B templates (email, outreach, brief, doc, sheet) live in MANAGER DOCUMENTS / G&B MASTER TEMPLATES/ — single canonical home. Never replicate templates into channel-specific or workflow folders.
metadata:
  type: feedback
---

## Rule

Every G&B template file lives in `MANAGER DOCUMENTS / G&B MASTER TEMPLATES/`. Channel sourcing folders, project folders, and workflow folders reference templates by Doc/Sheet ID — they do NOT hold their own copies of template files.

- ✅ `MANAGER DOCUMENTS/G&B MASTER TEMPLATES/EMAILS/G&B Intermediary Email Templates` — canonical home
- ❌ `OPERATIONS/INTERMEDIARY SOURCING/TEMPLATES/G&B Intermediary Email Templates` — replication; wrong

## Why

Templates are master assets. Replicating them across channel folders creates drift (which copy is current?) and confusion. Single-canonical-home means there's exactly one place to update a template; every reference resolves through the same Doc/Sheet ID.

Precipitating trace: 2026-05-12 — during the OPERATIONS restructure subagent run, I moved 3 intermediary template files OUT of `MANAGER DOCUMENTS/G&B MASTER TEMPLATES` INTO `OPERATIONS/INTERMEDIARY SOURCING/TEMPLATES/`. Kay corrected: "ALL TEMPLATES GO IN THE G&B MASTER TEMPLATES FOLDER, NOT THESE."

## How to apply

- When proposing a folder restructure: NEVER include a TEMPLATES/ subfolder under a channel/project folder. Templates stay in `MANAGER DOCUMENTS/G&B MASTER TEMPLATES/`.
- When the work needs a template, reference by ID. Skill code already does this (`feedback_no_intermediary_drafts_outside_template` pins the canonical Doc IDs).
- Channel/project folders hold execution artifacts (drafts, outputs, prep docs, per-instance materials) — NOT master assets.
- If a new template type emerges (e.g., conference reply template), the home is `MANAGER DOCUMENTS/G&B MASTER TEMPLATES/` (possibly with a new subfolder by template type), not a local channel folder.

## Subfolder convention within G&B MASTER TEMPLATES

Existing structure (as observed 2026-05-12):
- `EMAILS/` — email templates (intermediary email templates, etc.)
- `TO DO TEMPLATE.xlsx` — task tracker template
- Other template types as they emerge

## Related

- `feedback_no_intermediary_drafts_outside_template` — canonical Doc IDs for intermediary outreach templates
- `feedback_folders_not_named_after_people` — folders are function/role-named; templates folder is correctly named G&B MASTER TEMPLATES (asset-class, not person)
