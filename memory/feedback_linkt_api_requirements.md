---
name: Linkt Integration via MCP
description: Linkt connected as MCP server. Use MCP tools not raw API. Always hide_duplicates, name ICPs by date, 2 credits per target.
type: feedback
---

## Linkt Integration — MCP Tools (Updated 2026-03-31)

### Use MCP, Not Raw API
Linkt is configured as an MCP server in `.mcp.json`. All operations use `mcp__linkt__*` tools, not curl/API calls. The MCP server handles authentication via `LINKT_API_KEY` env var.

### Correct MCP Flow
1. Create ICP with `entity_targets` array (company root + person) — `mcp__linkt__create_icp_v1_icp_post`
2. Create sheets (company + person) — `mcp__linkt__create_sheet_v1_sheet_post`
3. Create search task — `mcp__linkt__create_task_v1_task_post` with `task_config: {"type": "search"}`
4. Execute task — `mcp__linkt__execute_task_v1_task` with `icp_id` passed explicitly
5. Monitor — `mcp__linkt__get_run_v1_run`
6. Export — `mcp__linkt__export_entities_v1_entity_export_get` with `hide_duplicates: true`

### Naming Convention
Name ICPs by date: `"{Niche} {YYYY-MM-DD}"`. Never use version numbers (v1, v2, v3).

**Why:** Kay requested date-based naming for traceability. Version numbers are ambiguous across niches.

### Always Use `hide_duplicates: true`
Every entity list/export call MUST pass `hide_duplicates: true`. Without it, Linkt returns multiple entries per company (the Howard & Gay triple-entry issue on 2026-03-30).

### Credit Model
1 credit = 1 entity. Each target = ~2 credits (company + person). 15 targets ≈ 30 credits.

### `desired_count` Is Ignored
Put target count in the ICP description text, not the API parameter.

### Platform Bug (2026-03-30)
4 of 5 ICPs failed because icp_id was null on run documents. If this recurs via MCP, delete broken ICP + task and recreate from scratch.

**How to apply:** target-discovery skill updated to use MCP flow. weekly-tracker updated to reference MCP tools for credit tracking.
