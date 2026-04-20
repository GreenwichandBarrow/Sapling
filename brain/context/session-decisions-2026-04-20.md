---
schema_version: 1.1.0
date: 2026-04-20
type: context
title: "Session Decisions — 2026-04-20"
tags: ["date/2026-04-20", "context", "topic/session-decisions", "topic/attio-architecture", "topic/relationship-management", "person/lauren-della-monica"]
---

# Session Decisions — 2026-04-20

In-progress file. Full decisions + actions log written at `/goodnight`. Started mid-session to capture the Lauren Della Monica PASS so relationship-manager respects it tomorrow.

## Decisions

- **PASS: Lauren Della Monica (LPDM, Industry Expert)** — remove from overdue/catch-up surfacing. Kay: "no need to reconnect." Relationship-manager must not surface her as needing catch-up going forward. Permanent fix: set `nurture_cadence = "Dormant"` on her Attio record.

- **APPROVE: Attio threshold rule** — People records only created when Kay sends her first outbound. Target lists stay in Google Sheets until then. Matches Attio's native inbound filter (no record until Kay replies). Retires `ATTIO_WRITE_RIVER_GUIDES` and `ATTIO_TAG_NETWORK_MATCHES` config flags. Memory: `feedback_attio_threshold_rule.md`.

- **APPROVE: Intermediary dormancy monitoring (not cadence)** — Intermediaries (River Guide, Industry Expert, Advisor) are passively watched for 100-day silence (90-day quarterly cycle + 10-day buffer). Kay does NOT reach out on a cadence — she builds the relationship once, they send to her. Relationship-manager surfaces dormant intermediaries for re-engage-or-drop decisions only. Memory: `feedback_intermediary_dormancy_monitoring.md`.

- **APPROVE: Model real workflow, not aspirational** — Design principle: don't build cadences/prompts for behaviors Kay doesn't run. Match her actual workflow, not generic CRM defaults. Memory: `feedback_model_real_workflow.md`.

- **APPROVE: Slash commands live in git** — All slash commands go in `.claude/commands/` (tracked), never `~/.claude/commands/` (untracked). Syncs across Macs. Memory: `feedback_slash_commands_in_git.md`.

- **APPROVE: Becreative SEO-spam Gmail filter** — `from:form-submission@squarespace.info` + SEO keywords → skip inbox, mark read, label `Filtered/SEO-Spam`. 2 existing threads (10 messages) retroactively archived.

- **DROP: Anthony (bookkeeper) Monday ping** — briefing item #11. His last email confirmed he's working on the monthly report. No ping needed. Friday 4/24 remains the natural review checkpoint.

## Actions Taken

- **CREATED:** 3 feedback memory files (`feedback_attio_threshold_rule.md`, `feedback_intermediary_dormancy_monitoring.md`, `feedback_model_real_workflow.md`) + `feedback_slash_commands_in_git.md`
- **UPDATED:** `.claude/skills/relationship-manager/SKILL.md` — added `<intermediary_dormancy>` section with 100-day threshold, updated `<nurture_monitoring>` to skip intermediary types
- **UPDATED:** `.claude/skills/river-guide-builder/SKILL.md` — replaced config-flag Attio write behavior with threshold rule (Attio creation only on first outbound via outreach-manager)
- **UPDATED:** `MEMORY.md` index with 4 new memory pointers
- **CREATED:** Gmail label `Filtered/SEO-Spam` (id Label_26)
- **CREATED:** Gmail filter id `ANe1Bmg9bSJjIgLMjTgxHE76yLyZCjp6AqP1Zw` for Squarespace SEO spam
- **ARCHIVED:** 2 Becreative threads (ids `19da9ada4a95b86f`, `19da47506f52803d`) + labeled + marked read

## Deferred

- **Goodwin finder's fee agreement for Sarah de Blasio** — Drive scan complete, 3 open questions before production: (1) Andy Lock review status on the template, (2) fee %/trigger terms Kay wants, (3) verbatim Goodwin language vs. G&B voice rewrite. Template located at Drive id `1eNG3AaR-yPgnu4NE3hK4sLNiFsSEt3lr`; G&B letterhead at `1PLYz2WH4Zqy4h2gYVqC8SVGyDrvy_ILF`; MASTER TEMPLATES folder at `19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`.

## Open Loops

- Apollo bulk enrichment subagent still running on other Mac (~500 records, ~250 credits remaining after). Report expected at `brain/outputs/2026-04-21-apollo-prioritized-enrichment-report.md`.
- Coffee rgb-coffee output verified CLEAN (29 River Guides + 14 Associations, no gaps). Safe for retroactive Phase 2+3 run.
- Steps 3-4 of today's plan pending: Network Matches tab addition to 8 target-list sheets + retroactive Phase 2+3 on today's niches.
