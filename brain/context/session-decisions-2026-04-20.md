---
schema_version: 1.1.0
date: 2026-04-20
type: context
title: "Session Decisions — 2026-04-20"
tags: ["date/2026-04-20", "context", "topic/session-decisions", "topic/apollo-enrichment", "topic/river-guide-builder", "topic/network-matches", "topic/attio-schema"]
---

# Session Decisions — 2026-04-20

Full-day covering Apollo bulk enrichment completion, river-guide-builder 3-phase skill ship, Attio schema patch, and Phase 3 Network Matches calibration. Split across morning session (pre-3:30pm continuation) + evening session (post-5:30pm resume).

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

### Network Matches Phase 3 calibration

- **APPROVE (evening):** Calibration-only scan before any Network Matches writes — Kay cap of ~10 strong connections per niche, flag-and-pause if exceeded. No writes permitted until counts confirmed.
- **REJECT (evening):** Proceed with 5-row Network Matches writes on the art-world-adjacent hits (Kate Reibel ×2 Attio records, Britta Nelson, Amanda Lo Iacono, Rick Hiebert). Kay rejected on thin-yield grounds: her lived network knowledge says there are more legitimate contacts across 8 niches than the skill surfaced. Instrument or data gap suspected, not true absence.
- **DEFER:** Phase 2+3 writes + investigation → 2026-04-21 morning session.
- **DEFER:** Kate Reibel Attio duplicate merge → 2026-04-21 morning (pre-write cleanup).
- **DEFER:** Q2 (River Guides Attio auto-create) + Q3 (Network Matches Attio tagging) write flags — both remain OFF pending Kay decision.

## Actions Taken

- **CREATED:** `brain/outputs/2026-04-21-apollo-prioritized-enrichment-report.md` (500-record run report, subagent authored).
- **CREATED:** 2 Attio select options via REST API — `nddl_apollo_departments:product_mangement`, `nddl_apollo_email_status:extrapolated`. Verified POST returned `data.title` matches.
- **UPDATED (via commit 4773d72 earlier today):** `.claude/skills/river-guide-builder/SKILL.md` — 3-phase unified skill.
- **UPDATED (via commit 4773d72):** `.claude/skills/niche-intelligence/SKILL.md` — Step 5b sunset.
- **CREATED (via commit 4773d72):** 8 niche-keyword YAMLs.

## Deferred

- **2026-04-21 morning:** Investigate why Phase 3 calibration yield was thin (5 hits across 8 niches vs Kay's lived knowledge of more). Decision tree: (a) skill bug — matcher logic too strict or tokenization gaps; (b) data gap — Attio has 388 populated employment_history vs 1,825 total; (c) Kay's knowledge is outside Attio (LinkedIn head-knowledge, Gmail, vault). Verify each before any Phase 3 writes.
- **2026-04-21 morning:** Kate Reibel Attio duplicate merge (two record IDs for same human).
- **2026-04-21 morning:** Verify Coffee subagent writes landed on Specialty Coffee Equipment Service target-list sheet (subagent stalled on chatroom post earlier today per continuation).
- **2026-05-03:** Step 1b Apollo full-enrichment run — drain remaining 1,029 matchable records + 8 retry records (now unblocked by schema patch).
- **Open (Kay decision):** Q2 — River Guides Attio auto-create behavior (auto / sheet-only / prompt-on-send).
- **Open (Kay decision):** Q3 — Network Matches Attio tagging behavior (tag existing records with industry metadata / sheet-only).

## Open Loops

- **Phase 3 thin-yield investigation (tomorrow, high priority)** — Kay insists network contacts exist across the 6 zero-hit niches. Must investigate before any writes or further calibration. Likely vectors: keyword tokenization (substring collisions), H-criterion too strict (should include M-tier for Network Matches context), Attio enrichment coverage 21%, Kay's knowledge held outside Attio.
- **Coffee subagent verification** — earlier today's rgb-coffee subagent completed writes but stalled on chatroom post. Need to confirm Coffee sheet tab state before retroactive Phase 2+3 run.
- **Kate Reibel Attio duplicate** — blocks art-storage Network Matches write.
- **Apollo Step 1b backlog** — 1,029 matchable + 8 retry records queued for May 2.

## System Status

- **Apollo enrichment:** completed cleanly this afternoon, full report at [[outputs/2026-04-21-apollo-prioritized-enrichment-report]].
- **Attio schema:** patched this evening, both enum values now valid.
- **River-guide-builder:** 3-phase skill shipped (morning commit 4773d72), Phase 2+3 held for investigation.
- **Network Matches tabs on 8 target-list sheets:** Kay set up tabs manually today on MacBook — confirmed ready to receive writes once investigation resolves.
