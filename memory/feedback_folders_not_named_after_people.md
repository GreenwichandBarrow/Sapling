---
name: folders-not-named-after-people
description: Drive folders and vault folders use function/role/purpose names, never person names. CALL LOGS not "JJ", PREP DOCS not "James Emden", TEMPLATES not "Megan Lawlor". People rotate; function names are stable.
metadata:
  type: feedback
---

## Rule

Folder names (in Drive, vault, repo) describe **function/role/purpose**, not the **person** currently fulfilling that function.

- ✅ `CALL LOGS/` — captures the role (cold call logs)
- ❌ `JJ/` — captures the person currently doing the role
- ✅ `PREP DOCS/` — captures the function (broker prep materials)
- ❌ `JAMES EMDEN PREP/` — captures one specific instance
- ✅ `TEMPLATES/` — captures the asset class
- ❌ `MEGAN LAWLOR TEMPLATES/` — captures who modeled them

Individual FILES inside those folders can have person names (e.g., `James Emden Intermediary Prep 5.7.26.doc` is a fine filename). The folder hierarchy stays function-based.

## Why

People change roles, leave, or hand off responsibilities. A folder named after a person ages into wrong-name the moment they move on. Function names stay accurate across role rotations. Also avoids the awkward "rename the folder" task whenever staffing changes.

Precipitating trace: 2026-05-12 — I proposed renaming `CALL LOGS/` → `JJ/` during the OPERATIONS restructure. Kay corrected: "WE DONT MAKE FOLDERS CALLED SOMEONES NAME." CALL LOGS is the correct function-based name.

## How to apply

- Before proposing any new folder name OR rename: check if the name is a person. If yes, rewrite to function/role/asset-class.
- Person-named subdivision happens at the file or row level, not the folder level. (Per-broker prep docs are individual files inside `PREP DOCS/`, not subfolders named per broker.)
- Exception: top-level audience folders like `ANALYST/` or `OPERATIONS/` are role-based (the role of the audience), which is the broader function-name pattern — still allowed.
- Vault `brain/entities/` is the one place person-named files are canonical (the entire schema is "one person per file"). That's the entity-graph layer, not folder structure.

## Related

- `feedback_franchise_firm_one_entry_only` — same family: structure by function, not by every instance
- `feedback_classify_intermediary_by_self_id` — describe what something IS, not who runs it
