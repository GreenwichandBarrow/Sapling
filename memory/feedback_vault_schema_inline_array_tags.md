---
name: Vault schema 1.1.0 requires inline-array tags
description: Entity and call schema validators at v1.1.0 require the `tags` field as inline JSON array (["x","y"]) not block-style YAML list — block style fails silently with "Missing: tags"
type: feedback
originSessionId: 3d944631-1e1f-43d0-88c1-6fdd795901fd
---
All vault schemas at version 1.1.0 (entity, call, trace, context) require the `tags:` frontmatter field as an **inline JSON array** — `tags: ["date/2026-04-24", "type", "topic/x"]`. Block-style YAML lists fail the validator with a misleading "Missing: tags" error despite the field being present.

Additionally, the call schema (`schemas/vault/call.yaml` v1.1.0) requires ALL three tag namespaces to appear in every call file: `client/{slug}`, `person/{slug}`, `company/{slug}`. Calls that reference a company with no person attendee still need a person-anchor stub created to satisfy this — precedent: 4/23 XPX panel call required creating `andrew-lowis.md` (the panel speaker) to validate.

**Why:** Discovered 4/24 during entity-stub creation subagent run — 4 consecutive entity writes failed on block-style tags before switching to inline array. Cost ~4 silent retry cycles in one agent session. Also why the 4/23 Granola transcripts sat blocked for 4 sessions: the call schema's three-namespace requirement wasn't obvious from a quick read of the schema file. Documented here so future agents catch both gotchas on first attempt.

**How to apply:** When writing ANY `brain/` file, use `tags: ["x", "y"]` not `tags:\n  - x\n  - y`. When writing a `brain/calls/` file, confirm all three `client/`, `person/`, `company/` tag namespaces appear (create anchor-entity stubs if needed). Existing memory `feedback_trace_schema_format` already covers traces; this extends the rule to entities and calls.
