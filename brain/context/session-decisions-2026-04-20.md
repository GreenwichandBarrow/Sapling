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
- Goodwin Finder's Fee DRAFT ready (`15-BCCvZ_QSbuKNDSp9I-8xxqvDMxnf1PQdvlMWXW59Y`) — awaits Kay's 2 decisions: (1) Finder = Sarah-personal vs Chartwell entity? (2) Expenses clause keep/delete?
- Kay to subscribe to 20 newsletter/alert sources (listed in tomorrow-pins-2026-04-21.md) — Tier 1 marketplaces (BizBuySell / BizQuest / BusinessesForSale / DealStream) highest-leverage.
- Deal-aggregator calibration review scheduled Friday 2026-04-24 — drop non-producing sources, find replacements.

---

## Afternoon Session Work (post-mid-day continuation)

### Decisions
- **APPROVE: Attio threshold rule (river-guide-builder)** — outreach-manager creates Attio records on first outbound only. river-guide-builder never auto-creates.
- **APPROVE: Intermediary dormancy monitoring (relationship-manager)** — passive 100-day silence watch; not active cadence. Kay builds relationship then they send to her.
- **APPROVE: Conference-discovery LinkedIn scraping added** — `site:linkedin.com/posts` searches for broker breakfasts. Twitter/X skipped (low-signal, post-2023 indexing throttled).
- **APPROVE: Business broker associations in conference discovery** — IBBA, M&A Source, TMA, state business broker associations added to Priority 1.
- **APPROVE: Deal-aggregator source overhaul** — 30 Tier 1 parseable sources + 9 Tier 2 (email-alert) + 5 Tier 3 (registration). Removed 10+ dead/mismatched sources. All verified via 2 subagent passes.
- **APPROVE: No priority tiering in deal-aggregator** — all Active-status niches scanned equally. Tracker is source of truth for active list.
- **APPROVE: River Guides tab schema** — canonical 7-col: `Name | Title | Firm | Location | LinkedIn | Industry | Why`. Validation-call-intake format. Skip Location/LinkedIn for already-known contacts.
- **APPROVE: Target-list sheets consolidated** in `OPERATIONS/TARGET LISTS/EMAIL OUTREACH/` (4 sheets moved). Pest stays in `TARGET LISTS/` for JJ.
- **APPROVE: G&B Target List Template** gets new River Guides tab added.
- **APPROVE: Conference Pipeline column reorder** — Decision moved from col O → col C.
- **APPROVE: Kay's time allocation** — conferences, river guides, owner calls only. Saved as memory.
- **DROP: Anthony Monday ping** — his last email confirmed he's on it; Friday 4/24 is natural checkpoint.
- **DROP: Lauren Della Monica catch-up prompt** — Kay: "no need to reconnect." Attio nurture_cadence should be set to Dormant.

### Actions Taken
- **UPDATED:** `conference-discovery` SKILL.md — added broker-association priorities (IBBA, M&A Source, TMA, state orgs), LinkedIn search step, Twitter-skip note, informal-breakfast caveat.
- **UPDATED:** `deal-aggregator` SKILL.md — Channel 1 rewritten with 30 Tier 1 sources + Tier 2 + Tier 3; Channel 3 rewritten per-niche with verified sources. Removed ~10 dead/mismatched sources.
- **UPDATED:** `river-guide-builder` SKILL.md — 7-col canonical schema; Associations-first scope discipline; template pointer; dropped 11-col spec, Score column, Category column, old config flags, old scoring section, stale relationship-manager integration.
- **UPDATED:** `relationship-manager` SKILL.md — added intermediary_dormancy section (100-day silence flag, not active cadence). Skip intermediary types in nurture cadence pass.
- **UPDATED:** `MEMORY.md` index with 10 new pointers.
- **CREATED:** 9 memory files: attio_threshold_rule, intermediary_dormancy_monitoring, model_real_workflow, slash_commands_in_git, surface_data_kay_decides, target_list_canonical_folder, step_by_step_interconnected_plans, briefing_conference_discovery_terse, kay_time_allocation, deal_aggregator_calibration.
- **MOVED:** 4 target-list sheets from scattered folders into `OPERATIONS/TARGET LISTS/EMAIL OUTREACH/` (Estate Mgmt, Coffee, Commercial Cleaning, Vertical SaaS).
- **ADDED:** River Guides tab to G&B Target List Template.
- **NORMALIZED:** 8 niche target-list sheets — River Guides tab schema set to canonical 7-col on all.
- **CLEARED:** 8 River Guides tabs (data rows) after scope correction (Kay: "you were just supposed to do the associations").
- **MOVED:** Conference Pipeline Decision column from O → C.
- **CREATED:** `tomorrow-pins-2026-04-21.md` with 20-source newsletter subscription list.
- **DISPATCHED:** 12+ subagents across the session (8 RGB Phase 2, 3 deal-aggregator verification, 1 second verification pass, locate 2 missing target sheets, coffee verification, clear River Guides, schema normalization, Goodwin doc, Drive parent lookup, RGB Phase 2 audit).
