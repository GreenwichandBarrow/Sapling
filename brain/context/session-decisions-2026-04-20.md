---
schema_version: 1.1.0
date: 2026-04-20
type: context
title: "Session Decisions — 2026-04-20"
tags: ["date/2026-04-20", "context", "topic/session-decisions", "topic/apollo-enrichment", "topic/river-guide-builder", "topic/network-matches", "topic/attio-schema", "topic/attio-architecture", "topic/relationship-management", "person/lauren-della-monica"]
---

# Session Decisions — 2026-04-20

Full-day spanning multiple work streams across both Macs:
- Apollo bulk enrichment (500-credit prioritized run + Attio schema patch).
- River-guide-builder 3-phase skill ship + Network Matches Phase 3 calibration.
- Attio threshold rule + intermediary dormancy monitoring + relationship-manager update.
- Deal-aggregator source overhaul + conference-discovery LinkedIn additions.
- Target-list sheet consolidation + River Guides canonical schema.

Reconciled 2026-05-07 from two parallel session-decisions files (iMac + MacBook) created independently — both narratives preserved below.

## Decisions

### Apollo prioritized bulk enrichment

- **APPROVE (morning):** Run 500-credit prioritized bulk enrichment on highest-priority Attio People (nurture_cadence → relationship_type → recent interactions). Hard cap at 500, 250 reserved for overflow.
- **APPROVE (morning):** 5-record pre-test → GO verdict — multi-role `employment_history` returns cleanly; schema holds at scale.
- **APPROVE (evening, verify):** Enrichment report [[outputs/2026-04-21-apollo-prioritized-enrichment-report]] landed at 3:05pm. 500/500 credits burned, 100% Apollo match, 492/500 (98.4%) written to Attio. 8 write failures from two Apollo enum mismatches.
- **APPROVE (evening, executed):** Patch Attio schema — add `product_mangement` to `nddl_apollo_departments`, `extrapolated` to `nddl_apollo_email_status` — unblocks 8 retry records for May 2 reset.
- **DEFER:** Step 1b full enrichment (1,029 remaining matchable records + 8 retries) → 2026-05-03 when Apollo credit month resets.

### River-Guide-Builder 3-phase upgrade

- **APPROVE (morning):** Plan at `~/.claude/plans/dapper-wishing-swing.md` — unify river-guide-builder + niche-intelligence Step 5b into 3-phase "Niche Network" skill. Attio write flags default OFF.
- **APPROVE (morning):** Sunset niche-intelligence Step 5b validation-contacts; concept lifts into Phase 1 Category 6 of river-guide-builder.
- **UPDATED (morning, commit 4773d72):** `.claude/skills/river-guide-builder/SKILL.md` rewritten to 3 phases. `.claude/skills/niche-intelligence/SKILL.md` edited (Step 5b removed).
- **CREATED (morning):** 8 niche-keyword YAMLs at `.claude/skills/river-guide-builder/references/niche-keywords/` — art-storage, estate-management, high-end-commercial-cleaning, premium-pest, private-art-advisory, specialty-coffee-equipment, specialty-insurance, vertical-saas-luxury.
- **APPROVE (morning):** 8 of 8 river-guide-builder Phase 1 runs completed on today's active niches (adding Vertical SaaS for Luxury + Private Art Advisory to bring pool from 6 → 8).
- **APPROVE (afternoon — MacBook session):** River Guides canonical 7-col tab schema: `Name | Title | Firm | Location | LinkedIn | Industry | Why`. Validation-call-intake format. Skip Location/LinkedIn for already-known contacts.
- **APPROVE (afternoon):** River Guides tab added to G&B Target List Template; River Guides tab schema normalized on all 8 niche target-list sheets.

### Network Matches Phase 3 calibration

- **APPROVE (evening):** Calibration-only scan before any Network Matches writes — Kay cap of ~10 strong connections per niche, flag-and-pause if exceeded. No writes permitted until counts confirmed.
- **REJECT (evening):** Proceed with 5-row Network Matches writes on the art-world-adjacent hits (Kate Reibel ×2 Attio records, Britta Nelson, Amanda Lo Iacono, Rick Hiebert). Kay rejected on thin-yield grounds — her lived network knowledge says there are more legitimate contacts across 8 niches than the skill surfaced. Instrument or data gap suspected, not true absence.
- **DEFER:** Phase 2+3 writes + investigation → 2026-04-21 morning session.
- **DEFER:** Kate Reibel Attio duplicate merge → 2026-04-21 morning (pre-write cleanup).

### Attio architecture + relationship-manager

- **PASS: Lauren Della Monica (LPDM, Industry Expert)** — remove from overdue/catch-up surfacing. Kay: "no need to reconnect." Relationship-manager must not surface her as needing catch-up going forward. Permanent fix: set `nurture_cadence = "Dormant"` on her Attio record.
- **APPROVE: Attio threshold rule** — People records only created when Kay sends her first outbound. Target lists stay in Google Sheets until then. Matches Attio's native inbound filter (no record until Kay replies). Retires `ATTIO_WRITE_RIVER_GUIDES` and `ATTIO_TAG_NETWORK_MATCHES` config flags. Memory: `feedback_attio_threshold_rule.md`.
- **APPROVE: Intermediary dormancy monitoring (not cadence)** — Intermediaries (River Guide, Industry Expert, Advisor) are passively watched for 100-day silence (90-day quarterly cycle + 10-day buffer). Kay does NOT reach out on a cadence — she builds the relationship once, they send to her. Relationship-manager surfaces dormant intermediaries for re-engage-or-drop decisions only. Memory: `feedback_intermediary_dormancy_monitoring.md`.
- **APPROVE: Model real workflow, not aspirational** — Design principle: don't build cadences/prompts for behaviors Kay doesn't run. Match her actual workflow, not generic CRM defaults. Memory: `feedback_model_real_workflow.md`.

### Deal-aggregator + conference-discovery overhaul

- **APPROVE: Conference-discovery LinkedIn scraping added** — `site:linkedin.com/posts` searches for broker breakfasts. Twitter/X skipped (low-signal, post-2023 indexing throttled).
- **APPROVE: Business broker associations in conference discovery** — IBBA, M&A Source, TMA, state business broker associations added to Priority 1.
- **APPROVE: Deal-aggregator source overhaul** — 30 Tier 1 parseable sources + 9 Tier 2 (email-alert) + 5 Tier 3 (registration). Removed 10+ dead/mismatched sources. All verified via 2 subagent passes.
- **APPROVE: No priority tiering in deal-aggregator** — all Active-status niches scanned equally. Tracker is source of truth for active list.
- **APPROVE: Target-list sheets consolidated** in `OPERATIONS/TARGET LISTS/EMAIL OUTREACH/` (4 sheets moved). Pest stays in `TARGET LISTS/` for JJ.
- **APPROVE: Conference Pipeline column reorder** — Decision moved to col C.

### Operational

- **APPROVE: Slash commands live in git** — All slash commands go in `.claude/commands/` (tracked), never `~/.claude/commands/` (untracked). Syncs across Macs. Memory: `feedback_slash_commands_in_git.md`.
- **APPROVE: Becreative SEO-spam Gmail filter** — `from:form-submission@squarespace.info` + SEO keywords → skip inbox, mark read, label `Filtered/SEO-Spam`. 2 existing threads (10 messages) retroactively archived.
- **APPROVE: Kay's time allocation** — conferences, river guides, owner calls only. Saved as memory.
- **DROP: Anthony (bookkeeper) Monday ping** — briefing item #11. His last email confirmed he's working on the monthly report. No ping needed. Friday 4/24 remains the natural review checkpoint.
- **DEFER:** Q2 (River Guides Attio auto-create) + Q3 (Network Matches Attio tagging) write flags — both remain OFF pending Kay decision.

## Actions Taken

### iMac side
- **CREATED:** `brain/outputs/2026-04-21-apollo-prioritized-enrichment-report.md` (500-record run report, subagent authored).
- **CREATED:** 2 Attio select options via REST API — `nddl_apollo_departments:product_mangement`, `nddl_apollo_email_status:extrapolated`. Verified POST returned `data.title` matches.
- **UPDATED (via commit 4773d72):** `.claude/skills/river-guide-builder/SKILL.md` — 3-phase unified skill.
- **UPDATED (via commit 4773d72):** `.claude/skills/niche-intelligence/SKILL.md` — Step 5b sunset.
- **CREATED (via commit 4773d72):** 8 niche-keyword YAMLs.

### MacBook side
- **CREATED:** 9+ memory files: attio_threshold_rule, intermediary_dormancy_monitoring, model_real_workflow, slash_commands_in_git, surface_data_kay_decides, target_list_canonical_folder, step_by_step_interconnected_plans, briefing_conference_discovery_terse, kay_time_allocation, deal_aggregator_calibration.
- **UPDATED:** `conference-discovery` SKILL.md — added broker-association priorities (IBBA, M&A Source, TMA, state orgs), LinkedIn search step, Twitter-skip note, informal-breakfast caveat.
- **UPDATED:** `deal-aggregator` SKILL.md — Channel 1 rewritten with 30 Tier 1 sources + Tier 2 + Tier 3; Channel 3 rewritten per-niche with verified sources. Removed ~10 dead/mismatched sources.
- **UPDATED:** `river-guide-builder` SKILL.md — 7-col canonical schema; Associations-first scope discipline; template pointer; dropped 11-col spec, Score column, Category column, old config flags, old scoring section, stale relationship-manager integration.
- **UPDATED:** `relationship-manager` SKILL.md — added intermediary_dormancy section (100-day silence flag, not active cadence). Skip intermediary types in nurture cadence pass.
- **UPDATED:** `MEMORY.md` index with 14 new memory pointers (4 morning + 10 afternoon).
- **MOVED:** 4 target-list sheets from scattered folders into `OPERATIONS/TARGET LISTS/EMAIL OUTREACH/` (Estate Mgmt, Coffee, Commercial Cleaning, Vertical SaaS).
- **ADDED:** River Guides tab to G&B Target List Template.
- **NORMALIZED:** 8 niche target-list sheets — River Guides tab schema set to canonical 7-col on all.
- **CLEARED:** 8 River Guides tabs (data rows) after scope correction (Kay: "you were just supposed to do the associations").
- **MOVED:** Conference Pipeline Decision column to col C.
- **CREATED:** Gmail label `Filtered/SEO-Spam` (id Label_26) + Gmail filter id `ANe1Bmg9bSJjIgLMjTgxHE76yLyZCjp6AqP1Zw` for Squarespace SEO spam.
- **ARCHIVED:** 2 Becreative threads (ids `19da9ada4a95b86f`, `19da47506f52803d`) + labeled + marked read.
- **CREATED:** `tomorrow-pins-2026-04-21.md` with 20-source newsletter subscription list.
- **DISPATCHED:** 12+ subagents across the session.

## Deferred

- **2026-04-21 morning:** Investigate why Phase 3 calibration yield was thin (5 hits across 8 niches vs Kay's lived knowledge of more). Decision tree: (a) skill bug — matcher logic too strict or tokenization gaps; (b) data gap — Attio has 388 populated employment_history vs 1,825 total; (c) Kay's knowledge is outside Attio. Verify each before any Phase 3 writes.
- **2026-04-21 morning:** Kate Reibel Attio duplicate merge.
- **2026-04-21 morning:** Verify Coffee subagent writes landed on Specialty Coffee Equipment Service target-list sheet.
- **2026-05-03:** Step 1b Apollo full-enrichment run.
- **Open (Kay decision):** Q2 — River Guides Attio auto-create behavior.
- **Open (Kay decision):** Q3 — Network Matches Attio tagging behavior.
- **Goodwin finder's fee agreement for Sarah de Blasio** — Drive scan complete, 3 open questions before production. Template located at Drive id `1eNG3AaR-yPgnu4NE3hK4sLNiFsSEt3lr`.

## Open Loops

- **Phase 3 thin-yield investigation (high priority for tomorrow)** — likely vectors: keyword tokenization (substring collisions), H-criterion too strict, Attio enrichment coverage 21%, Kay's knowledge held outside Attio.
- **Coffee subagent verification** — MacBook session reported rgb-coffee output verified CLEAN (29 River Guides + 14 Associations, no gaps).
- **Kate Reibel Attio duplicate** — blocks art-storage Network Matches write.
- **Apollo Step 1b backlog** — 1,029 matchable + 8 retry records queued for May 2.
- **Steps 3-4 of today's plan pending:** Network Matches tab addition + retroactive Phase 2+3 on today's niches.
- **Goodwin Finder's Fee DRAFT ready** (`15-BCCvZ_QSbuKNDSp9I-8xxqvDMxnf1PQdvlMWXW59Y`) — awaits Kay's 2 decisions: (1) Finder = Sarah-personal vs Chartwell entity? (2) Expenses clause keep/delete?
- **Newsletter subscriptions** — Kay to subscribe to 20 sources (in tomorrow-pins-2026-04-21.md).
- **Deal-aggregator calibration review** scheduled Friday 2026-04-24.

## System Status

- **Apollo enrichment:** completed cleanly this afternoon, full report at [[outputs/2026-04-21-apollo-prioritized-enrichment-report]].
- **Attio schema:** patched this evening, both enum values now valid.
- **River-guide-builder:** 3-phase skill shipped (morning commit 4773d72), Phase 2+3 held for investigation; afternoon canonical 7-col schema applied across 8 sheets.
- **Network Matches tabs on 8 target-list sheets:** Kay set up tabs manually today on MacBook — confirmed ready to receive writes once investigation resolves.
- **Conference Pipeline:** Decision column moved; LinkedIn search added; broker associations promoted to Priority 1.
- **Deal-aggregator:** source list overhauled (30 + 9 + 5 across 3 tiers); ~10 dead sources removed.
