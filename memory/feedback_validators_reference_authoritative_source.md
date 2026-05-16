---
name: validators-reference-authoritative-source-not-observed-data
description: "Validators must source allowed values from schemas/yaml dropdown definitions, NOT from a SELECT DISTINCT of live data. Observed-data-as-source-of-truth launders agent fabrications into \"approved\" status."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 03560fda-4372-4242-bb27-ca05145be53d
---

## Rule

When writing or updating any validator (POST_RUN_CHECK script, schema check, integrity guard, dashboard health probe), source the set of allowed values from the **authoritative definition** — schema files, dropdown configurations, yaml enums, code constants — **not** from what currently appears in live data.

## Why

Validators that learn from observed data can launder agent fabrications into "approved" status. If an agent invents a status value and writes it to a sheet, and a validator later runs `SELECT DISTINCT status FROM live_data` to build its allowlist, the invented value is now permanently codified as legitimate. The validator becomes a downstream amplifier of upstream noise rather than a gate against it.

This is distinct from `feedback_no_fabricated_status.md`, which is the agent-side rule about not inventing values in the first place. This memory is the validator-side rule: even if upstream fabrications slip through, the validator must not bless them.

## Precipitating incident

**2026-05-12 conference-discovery rogue-status trace.** A prior run of the conference-discovery skill wrote `Future / Map-Only` as a status value to the Conference Pipeline sheet — a value that was never in the dropdown definition. When the integrity validator (`scripts/validate_conference_discovery_integrity.py`) was first written, it built its allowed-status set by scanning the live sheet rows, which included the agent-invented value. The validator therefore "approved" the fabrication on every subsequent run, hiding the original drift.

The fix was to point the validator at the dropdown configuration (in this case, the data-validation rule attached to the Status column via the Sheets API), not at observed rows.

## How to apply

- **When writing a validator:** locate the authoritative source. Examples:
  - Google Sheets → read the column's `dataValidation` rule via Sheets API; use its `condition.values` as the allowlist.
  - YAML schema → load the `enum:` list from the schema file.
  - Python skill code → import the constant/enum directly.
  - Attio → read the select-field options from the Attio schema endpoint, not from existing record values.
- **When reviewing an existing validator:** check whether its allowlist comes from a config file/schema definition or from a live-data query. If the latter, rewrite to pull from the authoritative source.
- **If no authoritative source exists yet:** create one (a yaml file, a dropdown rule, a code constant) and have BOTH the writer and the validator reference it. Single source of truth for allowed values.
- **Symptom to watch for:** "the validator passed but the sheet looks wrong." That's usually this bug.

## Related memories

- `feedback_no_fabricated_status.md` — agent-side counterpart (don't invent values).
- `feedback_new_status_convention_for_agent_discoveries.md` — the canonical `NEW` marker that agents use instead of inventing statuses.
