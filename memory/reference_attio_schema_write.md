---
name: Attio schema writes via REST API (MCP is read-only on schema)
description: Attio MCP does not allow schema mutations (add select options, create attributes). Use Attio REST API directly via curl.
type: reference
originSessionId: 4d4166cd-0bb3-4a20-887c-1f29801ff285
---
Attio MCP server is deliberately scoped to read-only on schema — it can discover attributes and fetch select options but cannot add options or create fields. To add select options (e.g., when Apollo returns enum values not yet in Attio's option list), use the Attio REST API directly.

## Endpoint

```bash
source "/Users/kaycschneider/Documents/AI Operations/scripts/.env.launchd"  # sets $ATTIO_API_KEY

curl -s -X POST \
  -H "Authorization: Bearer $ATTIO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"data":{"title":"OPTION_VALUE"}}' \
  "https://api.attio.com/v2/objects/{object}/attributes/{attribute_slug}/options"
```

- `{object}` — e.g. `people`, `companies`, `deals`
- `{attribute_slug}` — e.g. `nddl_apollo_departments`, `nddl_apollo_email_status`
- Response: `{"data": {"id": {...}, "title": "...", "is_archived": false}}` on success.

## Real examples (2026-04-20)

- Added `product_mangement` (sic — Apollo's persistent typo) to `people.nddl_apollo_departments`
- Added `extrapolated` to `people.nddl_apollo_email_status`

Both unblocked Apollo enrichment write failures that were piling up on records where Apollo returned those enum values.

## Discovery

To verify an attribute slug or see existing options before writing:

```bash
curl -s -H "Authorization: Bearer $ATTIO_API_KEY" \
  "https://api.attio.com/v2/objects/people/attributes/{slug}/options" | jq
```

## When to use

- When Apollo or any upstream source returns an enum value not in Attio's select list, and that missing option is causing write failures during enrichment runs.
- When creating a new custom enum attribute for a new data source (less common — typically Kay adds these via Attio UI).

## When NOT to use

- Do not use this endpoint to mutate records (use `mcp__attio__update_record` or Attio REST `/records/{id}` PATCH).
- Do not archive, rename, or delete options without Kay's explicit approval — schema changes are permanent and affect all historical records.
