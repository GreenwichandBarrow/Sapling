---
schema_version: 1.1.0
date: 2026-05-08
type: trace
importance: critical
target: claude-md
tags: ["date/2026-05-08", "trace", "domain/architecture", "pattern/integration-priority", "topic/mcp", "topic/skill-design", "status/applied"]
---

# MCP-first integration doctrine

## Trigger

Phase 4 (Granola sidecar handoff) was originally designed to watch a local Granola cache file (`~/Library/Application Support/Granola/cache-v6.json`) on iMac, accept hours of lazy-flush lag, and miss MacBook + phone calls entirely. The architecture was fundamentally constrained because no one checked whether Granola already exposed an MCP server.

It does. `https://mcp.granola.ai/mcp` is registered in `~/.claude.json` and is already used by 3 existing skills (niche-intelligence, meeting-brief-manager, others). The existence of that MCP would have invalidated the entire local-cache-watching architecture from day one.

Cost of the near-miss: ~hours of design discussion + a complete plan of the wrong architecture. Pivoting to MCP-based design (server-side puller, all 3 devices covered via cloud) collapsed Phase 4 to a fraction of its original scope.

## Decision

Codify "MCP first → public API second → ask Kay before falling back to local" as durable doctrine in three layers:

1. Memory file `feedback_integration_priority_mcp_api_local.md` (durable record).
2. CLAUDE.md preflight block `### Before building any new skill or skill integration` (loads every session).
3. `create-agent-skills` SKILL.md `Step 0: Integration Priority Check (MANDATORY before any design)` (fires at the action moment).

Each layer references the others so the rule survives if any single layer drifts.

## Alternatives Considered

- **Memory only.** Rejected — memory recall is unreliable; future agents would design wrong architectures despite the rule existing. Recall failure is the dominant failure mode.
- **CLAUDE.md only.** Better than memory but doesn't fire at the *moment* of designing a skill. The rule is most needed when authoring SKILL.md, where create-agent-skills is loaded.
- **Code-level enforcement** (e.g., a hook that blocks new skills referencing local paths without checking MCP first). Rejected — too brittle, would block legitimate local-only patterns.
- **Single-layer documentation.** Rejected — single layer = single point of failure. Multi-layer with cross-references is the pattern that actually survives drift.

## Reasoning

Three observations from the near-miss:

1. **MCPs are easy to overlook because they look like infrastructure.** They appear in the "still connecting" list at session start, fade into the background, and get treated as already-handled. Designers default to "the data must come from somewhere local" without checking the MCP-tool inventory.

2. **Local-fallback architectures are systematically the most fragile path** (single-device, lazy-flush, encryption gotchas, OAuth flow blockers when generalizing to other contexts) and almost always have an MCP equivalent that's been overlooked.

3. **The rule needs to fire BEFORE design starts**, not during code review. Once a designer has invested 30+ min in a local architecture, sunk-cost makes the pivot costly. Step-0 placement in create-agent-skills SKILL.md ensures the check runs before any architecture is sketched.

## Why This Trace Matters

Without this trace, future agents will repeat the Phase 4 pattern: design a local-watcher architecture, accept its lag/coverage/auth limitations as inherent, never check whether the vendor offers an MCP. The rule is durable doctrine for a recurring blind spot.

Adjacent: this is the first instance of multi-layer-defense doctrine for a single rule. The pattern (memory + CLAUDE.md + relevant SKILL.md) is reusable for any rule that's load-bearing across contexts.

## Key Insight

**Connecting != broken.** When an MCP server appears in the session-start "still connecting" list, designers infer it's unavailable and design around it. Reality: connecting means *the connection handshake is in progress*, not that it failed. Wait for the connection or run `ToolSearch` with the service name before assuming unavailable. The original Phase 4 plan was a multi-day build of an architecture made unnecessary by a server that was, in fact, available — just not yet visible at session-start.
