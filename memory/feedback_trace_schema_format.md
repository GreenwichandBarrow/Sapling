---
name: Vault schema requires inline array tags format (traces, inbox, all schemas)
description: Vault schema validator rejects block-list YAML tags across all schemas (traces, inbox, calls, outputs, entities). Tags MUST be inline array. Use current schema_version per schema file, usually 1.0.0 or 1.1.0 — not the newest changelog entry.
type: feedback
originSessionId: 04cda994-9d0c-4401-8a83-d7e4b3e0cc04
---
When writing ANY file under `brain/` (traces, inbox, calls, outputs, entities, etc.), the vault schema validator has two gotchas:

1. **Tags must be inline YAML array format**, not block-list.
   - **Correct:** `tags: [date/2026-04-17, trace, pattern/automation-gap]`
   - **Rejected:** 
     ```yaml
     tags:
       - date/2026-04-17
       - trace
     ```
   - Block-list format reads as empty to the validator. This is a validator quirk, not a YAML standard issue.

2. **schema_version must be `1.1.0`**, despite the schema file showing a 1.2.0 entry in the changelog. The `current` field on `schema_version` is 1.1.0 and that's what the validator enforces.

**How to apply:**
- When writing any trace file (or any vault file with a schema), use inline array format for tags
- If a vault write fails schema validation, check: (a) tags format inline?, (b) schema_version = current listed in schema file (usually not the newest changelog entry)?
- Run `python3 "$CLAUDE_PROJECT_DIR"/.claude/hooks/router/pre_tool_use.py` against a test payload to see the exact validator error if unsure

**Why this exists:** Two vault writes on 2026-04-17 failed before landing because of these two issues. On 2026-04-18 an inbox write failed the same way — confirming this is a cross-schema validator rule, not trace-specific. Wasted ~3 tool calls per retry.
