---
schema_version: 1.1.0
date: 2026-04-25
type: trace
today: "[[notes/daily/2026-04-25]]"
task: Enumerate JJ Call Log tabs to capture dials that working-tab-only scan misses
had_human_override: false
importance: high
target: script:refresh_jj_snapshot
tags: [date/2026-04-25, trace, topic/jj-operations, topic/dashboard, pattern/oauth-refresh-when-cli-lacks-metadata, domain/technical]
---

# Decision Trace: Direct Sheets API call (via gog refresh_token) when gog itself doesn't expose the metadata

## Context

JJ activity snapshot for the dashboard initially scanned each niche sheet's working tab only (T+V Call Date columns). Result: 2 lifetime dials surfaced. But per `feedback_jj_call_date_from_field_not_tab.md` and direct precedent in session-decisions-2026-04-24, JJ also logs on per-day `Call Log M.DD.YY` tabs — 9 Friday dials were on the 4.21.26 prep tab, not the 4.24.26 tab. Working-tab-only scan was undercounting massively.

To enumerate those Call Log tabs at runtime, need to list all tabs in each niche sheet. `gog sheets` only has cell-level commands (get/update/append/clear) — no metadata/list-sheets command. `gog drive get` returns file-level metadata but not sheet-level.

## Decisions

### How to get sheet metadata (tab list) from a Google Sheet

**Considered:**
- (a) Wait for gog to add a `sheets metadata` subcommand. Indefinite timeline, blocks shipping.
- (b) Try common tab names heuristically (Call Log {date}). Brittle — only catches what we guess.
- (c) Use Sheets API directly via Python `requests` — `GET /v4/spreadsheets/{id}?fields=sheets(properties(title))` returns all tab names cheaply.
- (d) Add `gspread` or `google-api-python-client` dependency. Heavy for one endpoint.

**Chosen:** (c). Built `_get_access_token()` that exports gog's refresh_token via `gog auth tokens export`, refreshes against `https://oauth2.googleapis.com/token` with the same client_id/client_secret gog uses, returns an access token good for ~1h. Plus `_list_sheet_tabs()` that hits the Sheets API `spreadsheets.get` endpoint with `?fields=sheets(properties(title))`.

**Reasoning:** Single dependency (`requests`, already installed), reuses gog's existing OAuth setup (no separate auth flow), and the refresh_token export → access_token pattern is reusable for any Google API gog doesn't fully wrap. Refresh-token export is to a tempfile that's deleted on the same call so secrets aren't at rest.

**Pattern:** #pattern/oauth-refresh-when-cli-lacks-metadata

### Tab name pattern matching

**Chosen:** Regex `^Call Log\s+\d+[./]\d+[./]\d+$` (case-insensitive).

**Reasoning:** JJ uses both `4.21.26` and `4/21/26` separators in tab names; the regex tolerates both. Locked-anchor (^...$) avoids accidental matches.

## Outcome

Lifetime dials jumped 2 → 133. This-week dials 0 → 80. Premium Pest had 8 hidden Call Log tabs holding 131 dials. Without the enumeration, the dashboard was structurally undercounting JJ's work by ~98%.

## Learnings

- **When a CLI wraps an API but doesn't expose every endpoint, OAuth refresh-token export → direct API call is the escape hatch.** gog gives us refresh_token + client_id/secret; everything Google's REST API supports is reachable.
- **For data sources with multiple tabs/pages/sections, ALWAYS enumerate before scanning.** A "scan the working tab" assumption silently missed 98% of the data here. The enumeration cost (one extra API call per sheet) is trivial.
- **Future agent instruction:** when building a snapshot of multi-tab data (Google Sheets, Notion databases, Linear projects), the first design question is "how do I list the tabs/pages/projects?" — not "what's in the tab I know about?" The latter assumes you know which tab matters; the former discovers it.
