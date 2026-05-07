---
schema_version: 1.1.0
date: 2026-04-26
type: trace
today: "[[notes/daily/2026-04-26]]"
task: Skill audit recommended HYBRID migration off Superhuman — migrate READ paths to gog Gmail, keep DRAFT path via superhuman-draft.sh wrapper
had_human_override: false
importance: medium
target: skill:email-intelligence, skill:pipeline-manager, bead:ai-ops-eg3
tags: [date/2026-04-26, trace, topic/superhuman-migration, topic/skill-architecture, pattern/separate-read-and-write-paths, domain/technical]
---

# Decision Trace: Hybrid migration — READ paths off Superhuman, DRAFT path stays

## Context

Kay set up Gmail-native `auto/*` filters (replacing Superhuman's locked-in LLM autolabels) and asked for a skill audit: *"please review any skills that may be looking for tags or triggers in superhuman. We should work directly with gmail."*

The audit found 8 skills referencing Superhuman:
- 2 with READ-path dependencies (`email-intelligence`, `pipeline-manager`) — call `superhuman_search` MCP to enumerate drafts/sent and detect cadence/aging
- 3 with WRITE-path dependencies only (`outreach-manager`, `conference-engagement`, `deal-aggregator`) — use `~/.local/bin/superhuman-draft.sh` for drafting outbound mail
- 3 with doc-only references (`relationship-manager`, `weekly-tracker`, `health-monitor`)

## Decision

Hybrid migration: migrate the 2 READ paths to `gog gmail` queries (`label:SENT`, `label:DRAFT`, age detection) but keep the DRAFT path via `superhuman-draft.sh` wrapper. Bead `ai-ops-eg3` (P1, ~2-3 hr) created.

## Alternatives Considered

1. **Full Superhuman removal** — migrate everything off Superhuman including drafting. Rejected per CLAUDE.md: drafting via the Bash wrapper is INTENTIONAL because Superhuman's draft system shows drafts in Kay's UI where she reviews before send. MCP tools route through Gmail API, creating "invisible drafts Kay never sees" — that's the failure mode the wrapper exists to avoid.
2. **Keep status quo** (no migration) — rejected. Kay explicitly asked for migration off Superhuman READ paths since auto/* labels are now in Gmail directly. Continuing to call Superhuman MCP for inbox scanning when the labels live in Gmail is wasteful and brittle (Superhuman MCP token has expired periodically).
3. **Migrate READ paths but kill drafting via wrapper too** — rejected. Even if Kay leaves Superhuman the product, the Bash wrapper is a thin shim. As long as Superhuman is being used for compose, the wrapper handles drafts safely. Removing it preemptively breaks her review workflow.

## Reasoning

The intent behind the original "Superhuman wrapper for drafts only" rule was to prevent invisible drafts. That intent doesn't change just because we're moving label scanning to Gmail. Read paths and write paths can be migrated independently because they have different failure modes:
- READ path failure: skill silently misses inbox state → wrong briefing
- WRITE path failure (the wrapper): draft created in Gmail API instead of Superhuman → Kay never sees it, never sends it

The hybrid maintains the safety property of write-side intent while gaining the simplicity of read-side native Gmail.

## Why This Trace Matters

Future agents tasked with "remove Superhuman" or "fully migrate off Superhuman" might naively rip out both paths. This trace documents that the drafting wrapper is INTENTIONAL and KEEP-AS-IS even when migrating away from Superhuman as a primary client. The migration is to Gmail-native READS while the wrapper continues to handle drafts until Kay actively switches her compose UI.

When Kay eventually lands on a replacement client (Mimestream, Apple Mail), the wrapper migration is a separate decision with its own bead — not part of `ai-ops-eg3`.

## Key Insight

When a "remove dependency on X" task surfaces, decompose by READ vs WRITE paths before scoping. Different paths often have different costs, different intents, and different correct answers. Don't migrate them as a single unit unless the analysis confirms they should move together.
