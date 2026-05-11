---
name: Motion API responses contain unescaped control chars — use Python, not jq
description: Motion's task API embeds raw control characters (newlines, tabs) in description fields, breaking strict JSON parsers like jq. Always use Python json with strict=False to parse.
type: feedback
originSessionId: 54785998-5c5c-4c8d-956a-e32941f2ea6d
---
**Rule:** When calling the Motion API (`api.usemotion.com`) for any task/project read endpoint, parse the response with `json.loads(text, strict=False)` in Python. Do NOT use `jq` or other strict JSON parsers — they will fail on embedded control characters.

**Why:** 2026-04-26 — first Motion export attempt used `curl | jq '.tasks[]'`. Response was 76KB of valid-structure JSON but contained raw `\n`/`\t`/`\r` inside task description text fields. `jq` errored: `Invalid string: control characters from U+0000 through U+001F must be escaped`. The bash background loop silently swallowed the error (jq output went to /dev/null) and the export appeared to hang. Switched to Python `json.loads(s, strict=False)` and got clean parsing immediately.

**How to apply:**
- For any `gog`-equivalent or direct curl call to Motion API, pipe response through Python with `strict=False`, not jq.
- Pattern:
  ```python
  import json, urllib.request
  with urllib.request.urlopen(req) as r:
      data = json.loads(r.read().decode('utf-8'), strict=False)
  ```
- Motion's rate limit is 12 req/min — pace at 7s between calls minimum, with 60s+ retry on HTTP 403/429.
- Pagination via `meta.nextCursor` in response; URL-encode cursor when passing back.
- Workspace ID for "My Tasks - Private": `ws_fnSjxkfnWpcCPke4cknr9r`.
