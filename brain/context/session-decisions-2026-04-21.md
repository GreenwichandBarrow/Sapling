---
schema_version: 1.1.0
date: 2026-04-21
type: context
title: "Session Decisions — 2026-04-21"
tags: ["date/2026-04-21", "context", "topic/session-decisions", "topic/guillermo-biweekly", "topic/niche-ranking", "topic/tracker-update", "topic/meeting-brief-repair"]
---

# Session Decisions — 2026-04-21

Mid-day session covering Guillermo biweekly call review, meeting-brief skill diagnosis + repair, specialty coffee equipment deep DD, traditional-searcher niche ranking, Industry Research Tracker re-rank, and calibration memory captures.

## Decisions

### Meeting-brief skill gap (identified + repaired)
- **APPROVE:** Diagnosed that `meeting-brief-manager` launchd was intentionally retired 2026-04-12 and replaced with pipeline-manager's "Brief needed?" Decisions-bucket prompt, but the pipeline-manager skill had stale contradictory documentation at line 1177 and no mandatory pre-flight enforcement in CLAUDE.md morning workflow.
- **APPROVE:** Patched `pipeline-manager/SKILL.md` line 1177 — removed stale "handled by meeting-brief-manager launchd" paragraph; replaced with on-demand Decisions-prompt protocol for ALL external meetings (investor, advisor, target, general).
- **APPROVE:** Added Brief-Decisions pre-flight invariant to `CLAUDE.md` morning workflow step 9 — briefing is malformed if any tomorrow's external meeting isn't either prior-approved or surfaced in Decisions. Fri scan covers Mon+Tue; Sun scan covers Mon.

### Guillermo biweekly call (2026-04-21 1:30pm + 5:59pm resume)
- **APPROVE:** Saved full call note at `brain/calls/2026-04-21-guillermo-kay-biweekly.md` (both Granola transcript parts merged, AI analysis attached).
- **APPROVE:** Captured Guillermo's "tools-for-walls" framework as the dominant strategic insight — applies cross-niche, not just coffee. Diligence question: "who else walks into the four walls."
- **APPROVE:** Kay to follow up with Guillermo on WhatsApp this week for pressure-test on Insurance + Pest theses. Draft ping prepared, Kay to copy-send.

### Specialty Coffee Equipment Service — DD complete
- **APPROVE:** Research sprint delivered GREEN verdict with 2 YELLOW caveats: contract length lands on 1-year commoditized side (defensibility leans on OEM authorization breadth + parts + factory-trained techs); Cimbali/Faema + Lavazza Espresso Point have exclusivity friction. Output: `brain/outputs/2026-04-21-coffee-equipment-servicing-dd-research.md`.
- **APPROVE:** Most important finding — Smart Care Solutions (Wind Point Partners, 1,500+ techs) acquired Espresso Partners 2022. PE already building "tools-for-walls" platform in espresso category. Validates exit path AND sets competitive timer.
- **APPROVE:** OEM exclusivity map (`brain/outputs/2026-04-21-oem-exclusivity-map.md`) — no single-operator state lockouts across 6 target OEMs in NY/NJ/CT. NYC-metro acquirable pool: 3 confirmed Tier-1 independents (Liemco NY, Cafe Techs NJ, Bean and Brew NJ) + Full Espresso Repair borderline. No NYC operator stacks 4+ OEM certs — play becomes buy-and-build, not turnkey acquisition.
- **APPROVE:** Slayer-Cimbali ownership surfaced as watch-item (if Cimbali folds Slayer into Prime Line's territorial structure, NYC loses Slayer as acquirable brand). 8-year independence suggests non-imminent.
- **APPROVE:** OEM authorized-dealer ecosystem reframed as POSITIVE signal for equipment-servicing thesis (not a risk). Codified as `feedback_oem_authorized_dealer_supports_thesis.md`.

### Niche ranking — traditional searcher analysis
- **REJECT:** First-pass 4-dimension ranking (warm-network + tri-state density + PE competition + differentiation fit, scored against vault internals). Ranked Art Advisory primary, Art Storage backup. Kay called it "full of holes and fluff" — internal data was thin (empty river-guide tabs, Apollo gaps) and propagated into the rank.
- **APPROVE:** Second-pass ranking using traditional ETA searcher criteria on external data only (IBISWorld, MarshBerry, Capstone, Stanford search-fund study, industry M&A reports). Luxury-fit applied as final multiplier. Output: `brain/outputs/2026-04-21-traditional-searcher-niche-analysis.md`.
- **APPROVE:** New ranking:
  1. Specialty Insurance Brokerage (Art & Collectibles / HNW) — 43.2 [primary]
  2. Premium Pest Management — 39.0 [backup]
  3. High-End Commercial Cleaning — 33.0
  4. Estate Management — 30.8
  5. Specialty Coffee Equipment Service — 28.0
  6. Private Art Advisory — 27.5
  7. Vertical SaaS for Luxury — 23.0
  8. Art Storage — 23.0
- **APPROVE:** Codified methodology as `feedback_niche_ranking_searcher_criteria_only.md` — future rankings under acquisition-timeline constraints default to external-data searcher criteria, not internal warm-network scores.

### Tracker update
- **APPROVE:** Industry Research Tracker WEEKLY REVIEW rank column updated to match searcher ranking. 8 cells updated at A4:A11, validated on read-back. Trace: `brain/traces/2026-04-21-tracker-manager-rank-reorder.md`. No status changes.

### Silent focus vs. formal drop (Kay override)
- **REJECT:** Claude's proposal to frame non-top-two niches as "disqualified" with downstream drops (tracker status changes, advisor notifications, outreach pause).
- **APPROVE:** Silent focus protocol — redirect new effort and attention to top 2, keep everything else in current state. Tracker statuses unchanged on all 8 niches, advisor comms unchanged, ongoing outreach unchanged. Codified as `feedback_silent_focus_not_formal_drop.md`.
- **UPDATED:** Guillermo WhatsApp draft revised from "Art Advisory, Storage, Coffee disqualified" to "focusing on Insurance and Pest."

### 6-month acquisition constraint (Kay override)
- **REJECT:** Claude's proposal to codify "Feb 2027 wrap → Oct 2026 close deadline" as `project_six_month_acquisition_deadline.md`. Kay clarified: "Project six months was a one off request, not a fact."
- **APPROVE:** Constraint served as stress-test lens for the niche ranking only. Not a durable operational deadline. Within-session effects stand (niche re-ranking, primary-vehicle identification); after-session codification dropped.
- **APPROVE:** Methodology captured as `feedback_stress_test_constraints_not_facts.md` — future hypothetical constraints treated as stress-test framing unless Kay explicitly commits them as operating reality.

### Intermediary outreach (Kay override)
- **REJECT:** Claude's proposal to draft + send 6 M&A intermediary outreach emails (3 specialty insurance, 3 pest management). Kay: "These are not people I know. Do not draft or send outreach."
- **APPROVE:** Drafts stay in `brain/outputs/2026-04-21-intermediary-outreach-drafts.md` as reference material only. No sends, no Apollo verifications, not in tomorrow-pins. If warm intros to any of these 6 surface via advisor network, revisit.
- **APPROVE:** Codified as `feedback_no_cold_outreach_to_strangers.md` — never draft Kay-to-stranger outreach without warm intro path.

## Actions Taken

- **UPDATED:** `.claude/skills/pipeline-manager/SKILL.md` — line 1177 stale paragraph replaced with on-demand brief protocol + mandatory scan procedure
- **UPDATED:** `CLAUDE.md` — morning workflow step 9 Brief-Decisions pre-flight invariant added
- **CREATED:** `brain/calls/2026-04-21-guillermo-kay-biweekly.md` (vault schema validated)
- **CREATED:** `brain/outputs/2026-04-21-coffee-equipment-servicing-dd-research.md`
- **CREATED:** `brain/outputs/2026-04-21-oem-exclusivity-map.md`
- **CREATED:** `brain/outputs/2026-04-21-luxury-coffee-searcher-analysis.md`
- **CREATED:** `brain/outputs/2026-04-21-active-niche-ranking-6mo-reset.md` (first-pass ranking — superseded)
- **CREATED:** `brain/outputs/2026-04-21-traditional-searcher-niche-analysis.md` (authoritative ranking)
- **CREATED:** `brain/outputs/2026-04-21-intermediary-outreach-drafts.md` (reference only — no sends)
- **UPDATED:** Industry Research Tracker WEEKLY REVIEW rank column A4:A11 (8 cells)
- **CREATED:** `brain/traces/2026-04-21-tracker-manager-rank-reorder.md`
- **CREATED:** `brain/traces/2026-04-21-niche-ranking-methodology-pivot.md`
- **CREATED:** `brain/traces/2026-04-21-stress-test-constraint-methodology.md`
- **CREATED:** `brain/traces/2026-04-21-silent-focus-protocol.md`
- **CREATED:** `brain/traces/2026-04-21-oem-authorized-dealer-thesis.md`
- **CREATED:** `memory/feedback_oem_authorized_dealer_supports_thesis.md`
- **CREATED:** `memory/feedback_niche_ranking_searcher_criteria_only.md`
- **CREATED:** `memory/feedback_silent_focus_not_formal_drop.md`
- **CREATED:** `memory/feedback_stress_test_constraints_not_facts.md`
- **CREATED:** `memory/feedback_no_cold_outreach_to_strangers.md`
- **UPDATED:** `memory/MEMORY.md` — 5 new feedback entries indexed

## Deferred

- **Next session:** River-guide-builder skill upgrade. Flagged today as recurring miss — Claude deflected multiple times. Related unresolved item from 2026-04-20: Phase 3 Network Matches thin-yield investigation (why only 5 hits across 8 niches vs. Kay's lived network knowledge). Both needed before any further niche-network build work. Deferred explicitly to next session when capacity is fresh.
- **Open:** Coffee-niche primary-call validation (3 NYC independents: Liemco, Cafe Techs NJ, Bean and Brew NJ) — not urgent given Coffee dropped to rank 5. Revisit only if needed.
- **Open:** Smart Care Solutions monitor (monthly check on their acquisition announcements) — lightweight watch-item, formalize if/when Coffee returns to active priority.
- **Open:** Intermediary contacts (6 named in drafts output) — sit as reference material only. Revisit only if warm-intro path surfaces through advisor network.

## Open Loops

- **River-guide-builder upgrade** — recurring miss, explicitly deferred to next session. Highest priority for next session's agenda.
- **Phase 3 Network Matches thin-yield investigation** (carried from 2026-04-20) — still unresolved. Likely vectors: keyword tokenization, H-criterion too strict, Attio enrichment coverage 21%, Kay's knowledge held outside Attio.
- **Guillermo WhatsApp follow-up** — draft prepared, Kay to copy-send. Not on tomorrow-pins (Kay-owned).
- **Specialty Insurance + Premium Pest** remain the top-2 primary/backup focus. Any outreach to intermediaries or advisors must route through warm-intro paths — no cold outreach to strangers.

## System Status

- **Pipeline-manager:** patched today, Brief-Decisions pre-flight now enforced.
- **Meeting-brief-manager:** retired (Apr 12, intentional) — pipeline-manager owns the Decisions prompt.
- **Tracker-manager:** executed rank update cleanly, 8 cells, validated.
- **Deal-aggregator:** upgraded earlier today (per Kay).
- **River-guide-builder:** needs upgrade — DEFERRED to next session.
- **Niche-intelligence:** no changes (Kay declined one-off lesson being baked into the skill).
