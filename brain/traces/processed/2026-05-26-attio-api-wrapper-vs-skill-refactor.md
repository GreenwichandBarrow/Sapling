---
review_status: applied
schema_version: 1.1.0
date: 2026-05-26
type: trace
title: "Build attio-api wrapper instead of refactoring each MCP-using skill"
tags:
  - date/2026-05-26
  - trace
  - skill/relationship-manager
  - skill/post-call-analyzer
  - skill/email-intelligence
  - skill/launchd-debugger
  - verb/APPROVE
  - topic/attio-doctrine
  - topic/credential-ladder
  - topic/1password
  - pattern/wrapper-not-refactor
---

## Trigger

Three days of artifact-propagated "Attio MCP disconnected (~14 days)" framing in relationship-manager + post-call-analyzer + health-monitor outputs. Kay called out the dissonance: *"attio is in 1password as well."* Live verification (HTTP 200 against `/v2/self` with op-resolved `ATTIO_API_KEY`) confirmed Attio REST has been fully healthy throughout — the "MCP outage" was a phantom. The real blocker was skill-code calling `mcp__attio__*` tools that aren't registered (`claude mcp get attio` returns "No MCP server found"), with no REST fallback path. Same pattern Granola had solved with `~/.local/bin/granola-api` per `2026-05-13-granola-api-wrapper-bypasses-oauth-mcp.md`.

## Decision

**Build `~/.local/bin/attio-api` as a thin REST shim with 1Password credential resolution at every invocation. Mirror granola-api's design. Do NOT refactor each MCP-calling skill in-line.**

Wrapper subcommands: `health`, `query-people`, `query-companies`, `get-person`, `list-notes`, `create-note`, `update-person`. 191 LOC. Resolves `op://GB Server/Attio API Key/password` at every call. Falls back to `$ATTIO_API_KEY` env var if already set (so scheduled jobs skip the op-read overhead).

Skills route through the wrapper instead of the MCP. The MCP becomes optional / cosmetic.

## Alternatives Considered

1. **Reconnect the Attio MCP interactively** — `claude mcp add --transport http attio <url>` once the URL is known. Restores tomorrow, doesn't fix the recurrence. The same MCP outage will re-happen the next time the OAuth session expires; doesn't change the doctrine gap.
2. **Refactor each MCP-calling skill to fall back to REST when `mcp__attio__*` is unavailable.** Touches relationship-manager, post-call-analyzer, email-intelligence — at minimum. Per-skill refactor is N edits, each with its own retest cycle. Code-duplication across skills (each has to encode the same REST signatures).
3. **Status quo + add doctrine memory only.** Document that 1Password works, hope skills self-correct. Doesn't actually fix anything; the artifact-propagated false claims continue.
4. **Build the wrapper (chosen).** ONE binary, N skills route through it. Refactor of each skill is later/optional and small (`mcp__attio__create_note` → `attio-api create-note --parent-object people --parent-record-id ...`). MCP can come and go without breaking anything.

## Reasoning

The granola-api precedent already proved this pattern works (`2026-05-13-granola-api-wrapper-bypasses-oauth-mcp.md`). Mirror it. The advantages compound:

- **Single source of truth for the credential resolution.** All skills go through the same `op://` resolve. If 1Password reorganizes the vault, fix one binary not N skills.
- **Smoke-testable end-to-end before any skill change.** `attio-api health` returns HTTP 200 → confirms credential + API + scope before touching downstream code.
- **MCP-optional design.** When the MCP is up, skills can still use it. When it's down (as it was for 14 days), wrapper is the load-bearing path. Either way, no silent-degrade.
- **Discoverable from terminal.** Future agent running an investigation can `attio-api query-people '{...}'` directly — same UX as `gog gmail`. No need to spin up a Python session to import an SDK.

The cost: ONE bash file to maintain. The wrapper itself is dumb plumbing — no business logic, no defaults beyond curl. New endpoints get a new subcommand; old endpoints don't change.

## Why This Trace Matters

Future agents will hit MCP outages again — that's a fact, OAuth sessions expire, hosted MCPs go offline. The pattern in this trace is the canonical workaround: **wrapper not refactor**. If a service has a 1Password-backed key + REST API, build the wrapper before assuming the MCP outage is a blocker. The "MCP disconnected as system outage" framing is a phantom 90% of the time — the credential is right there.

This trace also documents the discovery that during the 14-day "Attio MCP outage," Attio was NEVER ACTUALLY CONFIGURED as an MCP server (`claude mcp get attio` → "No MCP server found"). The outage was structural, not transient. Skills calling `mcp__attio__*` had been silently no-op'ing the entire time. Without the wrapper, this gap would have persisted indefinitely.

## Key Insight

**1Password is the FIRST rung of the credential ladder, not the LAST resort.** When a doctrine memory says "MCP first → API second → ask Kay before local," remember that "API second" means REST-via-1Password is fully credentialed — not a fallback. The wrapper makes that path obvious + idiomatic so the next agent doesn't bury it three skill-execution-layers deep.
