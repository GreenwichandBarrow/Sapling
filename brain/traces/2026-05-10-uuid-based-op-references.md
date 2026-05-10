---
schema_version: 1.1.0
date: 2026-05-10
type: trace
title: "Use UUID-based op:// references when 1P item titles contain em-dashes or non-ASCII chars"
had_human_override: false
importance: medium
target: "process, memory, future-credential-migrations"
tags: ["date/2026-05-10", "trace", "topic/1password", "topic/credential-migration", "topic/op-cli", "pattern/uuid-stable-identifier"]
---

# Trace: UUID-based op:// references when 1P titles contain em-dashes

## Context

During the 2026-05-10 credential migration, Kay created 5 new 1Password items in vault `GB Server` (1 GOG keyring + 4 Slack webhooks) using the same naming pattern as existing items (`Slack Webhook — Operations`, etc.) — em-dashes in titles to match the visual convention of `Attio API Key`, `Apollo API Key`, etc.

When the server tried to resolve the first webhook with the natural title-based path:

```
op read 'op://GB Server/Slack Webhook — Operations/password'
```

The op CLI rejected it:

```
[ERROR] could not read secret 'op://GB Server/Slack Webhook — Operations/password':
invalid secret reference: invalid character in secret reference: '—'
```

This was the second time the trap fired — earlier in the same migration, Kay's first attempt at the Operations item used a regular hyphen (`Slack Webhook - Operations`), then she renamed it to em-dash for visual consistency with the others, breaking the title-based resolution path.

## Decisions

### Path strategy

**AI proposed:** Three options — (1) ask Kay to rename all em-dash titles to ASCII hyphens (visual consistency hit), (2) URL-encode the em-dash in the op:// path (op rejects this; not actually supported), (3) reference items by their stable UUIDs (`op://GB Server/<uuid>/field`).

**Chosen:** Option 3 — UUID-based references. Resolution syntax: `op://GB Server/u2shpr72znynqh2s62jue25wzi/password` for the Operations webhook, and similar 26-char base32-style UUIDs for the other 3 webhooks + GOG keyring item.

**Reasoning:** UUIDs are op's primary identifier; titles are display-layer metadata. UUID-based references survive renames, special-char insertions, and trailing-whitespace bugs (two of Kay's 4 webhook items had trailing spaces in their titles — invisible visually, would break any title-based lookup that didn't normalize). The cost: `.env.launchd` is slightly less human-readable (you can't tell from the env file which 1P item maps to which env var without looking it up). The benefit: zero fragility around 1P naming conventions.

**Pattern:** #pattern/uuid-stable-identifier

## Learnings

When migrating credentials to op:// references, prefer UUID-based paths from the start — even for items with currently-clean ASCII titles. Future renames are unpredictable; UUIDs aren't. The marginal readability loss in the env file is offset by total robustness.

The em-dash trap specifically: op rejects ANY non-ASCII character in the URI path component, not just em-dash. Em-dash, en-dash, smart quotes, accented chars, fullwidth ASCII — all rejected. Trailing whitespace in titles (which 1P preserves verbatim) ALSO breaks title-based lookup silently because op trims neither the input nor the stored title before comparison.

A future agent migrating new credentials should:
1. Run `op item list --vault=<vault> --format=json` and grab the `id` field for each target item.
2. Write `op://<vault>/<id>/<field>` references in `.env.launchd`, not `op://<vault>/<title>/<field>`.
3. Ignore the readability concern. The env file is read by machines (op inject); humans should look up which UUID corresponds to which item via 1P CLI when needed.

## Why This Trace Matters

The non-obvious part is that op's rejection of em-dash isn't documented in the most-frequently-read 1Password CLI quickstart pages — Kay and I both defaulted to title-based references and burned 30+ minutes on the trap (false-positive 401 reports, multiple "verify by length" round-trips with iMac). Future credential migrations should bypass the trap entirely by going UUID-first.

## Key Insight

**Pick the most-stable identifier op exposes**, not the most-human-readable one. UUIDs survive renames, character-class changes, and whitespace bugs. Titles don't.
