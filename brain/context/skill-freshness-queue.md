---
schema_version: 1.0.0
date: 2026-05-15
type: context
purpose: Rotating freshness-audit queue for calibration-workflow bucket 6
tags: [context, calibration, skill-audit]
---

# Skill Freshness Queue

Owned by `calibration-workflow` bucket 6 (Skill freshness audit). Each Thursday meta-calibration picks the 2 stalest skills relative to their cadence and runs `create-skill/workflows/verify-skill.md` on each.

## Cadence by Dependency Type

| Type | Re-verify Every | Why |
|------|-----------------|-----|
| API | 60 days | Vendor endpoints/auth/scopes shift fastest |
| Framework | 90-180 days | SDK patterns + Claude Code conventions evolve |
| CLI | 180 days | Local tool flags + subcommands move slower |
| Pure-process | 365 days | No external deps — only revisit when doctrine drifts |

## Queue (sorted alphabetically)

| Skill | Dependency Type | Last Verified | Notes |
|-------|-----------------|---------------|-------|
| agent-chatroom | Framework | 2026-05-15 | Claude Code Task/chatroom conventions |
| budget-manager | API | 2026-05-15 | Google Sheets (gog) + bookkeeper P&L parsing |
| calibration-workflow | Framework | 2026-05-15 | Self-audit allowed but lower priority |
| cass | CLI | 2026-05-15 | `cass` binary; index format |
| conference-discovery | API | 2026-05-15 | Web scraping + Google Sheets + Gmail |
| conference-engagement | API | 2026-05-15 | Gmail + Sheets templates |
| create-agent-skills | Pure-process | 2026-05-15 | Skill authoring guidance only |
| create-skill | Pure-process | 2026-05-15 | Plugin-installed reference template |
| deal-aggregator | API | 2026-05-15 | Broker platforms + Gmail + Sheets |
| deal-evaluation | API | 2026-05-15 | Gmail, Drive, Docs, Sheets |
| decision-traces | Pure-process | 2026-05-15 | Vault-only trace extraction |
| email-intelligence | API | 2026-05-15 | Gmail + Granola APIs |
| evolve | Pure-process | 2026-05-15 | Plugin-installed; reads skill dirs only |
| generate-prd | Pure-process | 2026-05-15 | Conversational PRD authoring |
| generate-stories | Pure-process | 2026-05-15 | PRD → story breakdown |
| generate-visuals | CLI | 2026-05-15 | `nano-banana` CLI to Gemini image API |
| github | CLI | 2026-05-15 | `gh` CLI |
| gmail-filter-add | API | 2026-05-15 | Gmail filter API |
| gogcli | CLI | 2026-05-15 | `gog` CLI surface across all Google services |
| health-monitor | API | 2026-05-15 | Mixed probes — services, hooks, vault |
| investor-update | API | 2026-05-15 | Gmail + Docs + Drive |
| jj-operations | API | 2026-05-15 | Google Sheets + Slack |
| launchd-debugger | CLI | 2026-05-15 | launchctl + log parsing (now systemd on VPS) |
| list-builder | API | 2026-05-15 | Apollo REST API |
| meeting-brief | API | 2026-05-15 | Calendar + Drive + Docs |
| meeting-brief-manager | API | 2026-05-15 | Calendar scan + sub-agent routing |
| migration-workflow | Pure-process | 2026-05-15 | Vault schema migrations |
| niche-intelligence | API | 2026-05-15 | Newsletters + web + Sheets |
| nightly-tracker-audit | API | 2026-05-15 | Google Sheets + Drive moves |
| obsidian-vault-ops | Pure-process | 2026-05-15 | Local vault file ops |
| onboard | Pure-process | 2026-05-15 | Interview + context-file population |
| outreach-manager | API | 2026-05-15 | Gmail + Sheets + Attio |
| pipeline-manager | API | 2026-05-15 | Gmail + Calendar + Attio + vault |
| plan-refinery | Framework | 2026-05-15 | Opus sub-agent coordination patterns |
| post-call-analyzer | API | 2026-05-15 | Granola REST + Docs + Sheets + Attio + Slack |
| post-loi | API | 2026-05-15 | Mixed deal-room services |
| relationship-manager | API | 2026-05-15 | Attio API + nurture cadence reads |
| river-guide-builder | API | 2026-05-15 | Sheets + web research |
| socrates | Pure-process | 2026-05-15 | Conversational technique only |
| target-discovery | API | 2026-05-15 | Apollo + web + Sheets |
| task-tracker-manager | API | 2026-05-15 | Google Sheets (TO DO sheet) |
| today | Pure-process | 2026-05-15 | Daily aggregation orchestrator |
| tracker-manager | API | 2026-05-15 | Google Sheets across operational sheets |
| triage | Pure-process | 2026-05-15 | Inbox item flow |
| warm-intro-finder | API | 2026-05-15 | Attio + Gmail + LinkedIn |
| weekly-tracker | API | 2026-05-15 | Gmail + Calendar + Attio + Sheets |

## How `calibration-workflow` picks the weekly 2

1. Compute `days_since_verified` per row.
2. Compute `staleness_ratio = days_since_verified / cadence_days` where cadence is from the table above (API=60, Framework=180, CLI=180, Pure-process=365).
3. Sort descending by `staleness_ratio`.
4. Pick top 2. Run `verify-skill` on each. Update `Last Verified` to the run date and append a one-line note (`fresh` / `needs updates` / `stale — fixed inline`).
5. If both top picks return `fresh`, that's healthy — no action needed beyond date bump.

## Open classification questions

None at seed time. Re-classify a skill only when its scope materially changes (e.g., a Pure-process skill grows an API dependency).
