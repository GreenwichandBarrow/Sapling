---
schema_version: 1.2.0
date: 2026-05-26
type: audit
status: draft
title: "Cross-Channel Dedup Audit — Week of 2026-05-24"
tags:
  - date/2026-05-26
  - output
  - output/audit
  - topic/outreach-channel-separation
  - topic/dealsx
  - topic/jj-operations
  - status/draft
---

# Cross-Channel Dedup Audit — Week of 2026-05-24

Wiki-links: [[entities/jj-operations-skill|jj-operations]] · [[entities/target-discovery-skill|target-discovery]] · [[entities/outreach-manager-skill|outreach-manager]] · [[entities/conference-discovery-skill|conference-discovery]] · related doctrine `memory/feedback_outreach_channel_universes_separate.md`.

## A. Headline verdict

**ALL CLEAN** — no DealsX-universe companies are present in any other channel's *active* outreach target list as of audit time (2026-05-26 ~15:00 ET). The four JJ Call Log tabs cleaned earlier today (5.26.26 / 5.27.26 / 5.28.26 / 5.29.26, 44 rows removed per snapshot — *not* 43 as paraphrased; snapshot's `matched_rows` totals 7+10+11+16=44) are the only week-of write surface that ever needed a dedup pass. All other write-capable skills that fired this week either did not touch company-level target lists (read-only / artifact-only) or wrote to surfaces orthogonal to DealsX (Conference Pipeline events, daily intelligence artifacts, task tracker). 0 exact-normalized matches across 469 active non-pest target rows + intermediary firms checked. Latent overlap exists in the Premium Pest **Full Target List** source pool (300 of 868 rows overlap DealsX) — this is by design, dedup happens at jj-operations Sunday-build time, not at source. No remediation required this week. Two skills lack documented DealsX-dedup gates and should be hardened before they next fire — see Section F.

## B. Skill firings inventory — week of 2026-05-24

| Skill | Fired | Write surface | DealsX-overlap risk |
|---|---|---|---|
| target-discovery | Sun 15:00 | `brain/context/jj-week-pool-2026-05-24.md` (artifact, no sheet write) | None (read-only pool builder) |
| jj-operations-sunday | Sun 18:00 | Premium Pest target sheet — Call Log tabs 5.25-5.29.26 | **Resolved** at build time (15 DNC + 0 dedup at build; today's 5/26 retroactive sweep removed 44 more) |
| conference-discovery | Sun 21:00 | Conference Pipeline `1bdf7xlcRjOTlVkuXA-HNGOQgjtDRmVN2RfDf9aUsDpY` (events, not companies) | N/A (event surface, not company-level) |
| nightly-tracker-audit | Sun 23:30, Mon 23:30 | Industry Research Tracker (WEEKLY REVIEW reorder) | N/A (status/sort only, no targets) |
| email-intelligence | Mon 07:00, Tue 07:00 | `brain/context/email-scan-results-{date}.md` (artifact); no Active Deals writes (Carlos NDA suppressed pre-write) | None this week |
| relationship-manager | Mon 06:50, Tue 06:50 | `brain/context/relationship-status-{date}.md` (artifact); MCP down → no Attio writes | None |
| deal-aggregator (2/day) | Mon 07:30 + 14:00, Tue 07:30 + 14:00 | `brain/context/deal-aggregator-scan-{date}.md` (artifact); 0 PASS → 0 Slack posts → 0 fingerprint writes | None |
| task-tracker (`TO DO 5.12.26`) | Tue 13:13 (manual via skill) | TO DO Sheet Capture tab (G&B task list, not outreach) | N/A |

**Read-only / probe / cache jobs fired but excluded from audit:** apollo-credits-refresh, attio-snapshot-refresh, external-services-probe, jj-snapshot-refresh, launchd-debugger, post-call-analyzer-poll. None mutate target lists.

**Pending firings Wed-Sat (see Section F).**

## C. Audit results per skill

DealsX universe pulled fresh: sheet `1VaviHqaJT9Wtm6X1h9B6Q8aOrA8adTiBvt851pkEUFg`, all 4 Pest tabs (Good Fit / Probable Fit, raw + Valid) — **2,521 unique normalized companies**. Normalization: lowercased, suffix-stripped (Inc/LLC/Corp/Co/Company/Ltd/Limited/LP/LLP/Services/Service/Solutions/Group/Holdings/Enterprises/The), punctuation collapsed.

### target-discovery (Sun 15:00)
- Wrote artifact only (`brain/context/jj-week-pool-2026-05-24.md`, 200 row pointers). No sheet writes. **0 overlap risk.** Apollo enrichment hit 2 blank-K rows, 0 matches — wrote nothing to the sheet.

### jj-operations-sunday (Sun 18:00) + retroactive sweep today (Tue 13:23 UTC)
- Built Call Log 5.25-5.29.26 from 185 Tier-1 rows. Sunday build dropped 15 DNC matches. 0 dedup against DealsX at Sunday-build time — Step 6 doctrine codified 2026-05-26 was not yet in the headless prompt last Sunday, so the dedup ran today as a one-shot sweep. Snapshot `brain/context/rollback-snapshots/jj-dealsx-dedup-2026-05-26T17-23-52Z.json` shows **44 rows removed** (7 / 10 / 11 / 16 across the four weekday tabs; 5/25 was Memorial Day and not built). 42 rows backfilled afterward; Friday 5.29.26 still ≥20 floor.
- **Post-sweep verification:** Call Log tabs 5.26-5.29.26 zero overlap. Confirmed against today's snapshot. Not re-audited per scope.

### conference-discovery (Sun 21:00)
- Wrote 8 rows to Conference Pipeline (6 new events + 2 new week headers) + archived 15 + deferred 3. Event-level surface, **not company-level — N/A for DealsX dedup.**

### email-intelligence (Mon 07:00, Tue 07:00)
- 2 runs. Both surfaced Project Drone Carlos Nieto / DCA. Carlos's "NDA Signed" Attio auto-write was suppressed Mon (REJECT-conflict precedent), CIM auto-trigger also suppressed Tue. **No Active Deals or target-list writes this week.** 0 overlap risk.

### relationship-manager (Mon 06:50, Tue 06:50)
- Artifact-only writes. Attio MCP outage (17 days carry-forward) means no Attio side-effects. **0 overlap risk.**

### deal-aggregator (Mon ×2, Tue ×2)
- 0 PASS verdicts across all 4 runs → 0 Slack posts → 0 fingerprint additions → 0 Active Deals creations. **0 overlap risk.**

### Other niche target lists scanned (defense-in-depth)
- **Art Insurance** (`15M76-...`) Active tab: 44 rows · 0 DealsX-pest matches
- **Domestic TCI** (`1lEAx-...`) Active tab: 48 rows · 0 matches
- **IPLC** (`1Cdw6yb8-...`) Active tab: 39 rows · 0 matches
- **Art Storage** (`1PDprJ_...`) Active tab: 83 rows · 0 matches
- **Art Advisory** (`1c6Db21D2...`) Active tab: 63 rows · 0 matches
- **Intermediary List** (`18zzE1y-...`) all 8 firm tabs: 192 firms · 0 matches (4 fuzzy substring/token hits all false-positives — pest-industry trade associations like NPMA / state PMA chapters, and unrelated brokers sharing common words like "First Choice" / "East Coast" / "North"; none are operating-company collisions)

Cross-niche dedup is structurally easy here because the only DealsX-active niche overlapping with current channel mix is Pest (DealsX) ↔ Premium Pest Management (JJ). The Art / TCI / IPLC niches operate in different verticals — natural separation. Specialty Insurance Brokerage, Estate Management, and Fractional CFO are DealsX niches with **no parallel JJ or Kay-Email target list active**, so no overlap possible there this week.

## D. Already-clean callouts

- **JJ Premium Pest Management Call Log tabs 5.26.26 / 5.27.26 / 5.28.26 / 5.29.26** — cleaned at Tue 13:23 UTC, 44 rows removed per snapshot `brain/context/rollback-snapshots/jj-dealsx-dedup-2026-05-26T17-23-52Z.json`, 42 rows backfilled, Fri tab ≥20 floor confirmed. Not re-audited per scope instructions.
- Call Log 5.25.26 was Memorial Day and not built — out of scope.

## E. Remediation needed

**None.** No DELETE, MOVE, or escalate actions required. All active outreach target lists across all channels are clean of DealsX-universe overlap as of this audit.

Latent state: 300 of 868 rows in the Premium Pest **Full Target List** (source pool, sheet `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`) match DealsX-pest normalized names. This is **expected and not actionable** — the JJ Sunday-build dedup (Step 6 of `headless-sunday-prep-prompt.md`, codified 2026-05-26) catches them at tab-write time, which is the correct enforcement point. Cleaning the source pool would only matter if a non-JJ channel ever reads from it, which currently nothing does.

## F. Pending firings (Wed-Sat) and inheritance status

| Timer | Next fire | Inherits build-time DealsX dedup? |
|---|---|---|
| nightly-tracker-audit | Wed-Fri 23:30 | N/A (no target writes) |
| relationship-manager | Wed-Fri 06:50 | N/A (artifact + Attio People sync, no target lists) |
| email-intelligence | Wed-Fri 07:00 | N/A this week (no auto-create flows fired this week; CIM/Active-Deal flows have separate dedup at intake) |
| deal-aggregator + Fri 07:30 | Wed-Fri 07:30 + Wed-Thu 14:00 + Fri 07:30 special | N/A (artifact only unless PASS verdict triggers Slack — no current PASS pattern) |
| calibration-workflow | Thu 23:00 | N/A (calibration meta-analysis, no target writes) |
| health-monitor | Fri 00:30 | N/A (monitoring) |
| niche-intelligence | Tue 22:30 (tonight) → Wed AM ready | **GAP — see below** |
| target-discovery-sunday | Sun 5/31 15:00 (next week) | Reads Full Target List, writes artifact. DealsX dedup not in this skill's writes but its output feeds jj-operations which has it |
| jj-operations-sunday | Sun 5/31 18:00 (next week) | **YES** — Step 6 enforced per SKILL.md L95 and headless prompt L21 (codified 2026-05-26) |
| conference-discovery | Sun 5/31 21:00 (next week) | N/A (event surface) |
| weekly-snapshot / weekly-archive-export | Fri 22:00 / Sat 09:00 | N/A (backup) |

### Skills-needing-update (follow-up for /evolve)

1. **niche-intelligence** (fires tonight Tue 22:30, ready Wed AM). When it screens a new niche and proposes target channels / scoring, it should explicitly cross-check candidate company seeds against the DealsX universe before recommending Kay-Email or JJ-Call-Only routing. Currently no DealsX-overlap gate documented. Risk surface is low (niche-intelligence proposes niches, doesn't append targets), but if it auto-seeds a target list at activation, the gate becomes load-bearing. **Recommendation:** add a "DealsX universe scan" step before any niche is marked Active-Outreach with non-DealsX channel.

2. **outreach-manager (Kay Email subagent)** — when it appends to a niche's per-niche target sheet (currently target-discovery is paused and outreach-manager append paths haven't fired this week, so no immediate gap, but the doctrine note exists at SKILL.md L3 only as a description claim "Attio dedup catches crossover" without an actual DealsX-sheet cross-reference). **Recommendation:** before the next Kay-Email cadence cycle on a niche with any DealsX adjacency (currently none, but Specialty Commercial Equipment / Storage / Estate Management blur), add explicit pre-append DealsX cross-reference per the same pattern jj-operations now enforces.

3. **conference-engagement** (didn't fire — no conference T-7 window hit this week). When it eventually fires and appends attendee rows to a target sheet or Intermediary List, it should run the same dedup. **Recommendation:** add at the post-conference attendee-ingest step.

4. **list-builder** (Apollo discovery — pause-status; would fire if target-discovery resumes). Same pattern: any company appended from Apollo must be DealsX-universe checked before insert.

No emergency for any of the above this week; the only skill that actually fired in the build-time-write category (jj-operations) already has the doctrine.

## Methodology notes

- DealsX universe: 2,521 unique normalized companies across 4 Pest tabs in sheet `1VaviHqaJT9Wtm6X1h9B6Q8aOrA8adTiBvt851pkEUFg`.
- Match logic: lowercase + strip suffixes (Inc/LLC/Corp/Co/Company/Ltd/Limited/LP/LLP/Services/Service/Solutions/Group/Holdings/Enterprises/The) + collapse punctuation + token-sort. Strict-on-match (exact normalized equality, no fuzzy in primary check); fuzzy pass run separately, all 26 fuzzy hits manually disqualified as false positives.
- Sources audited: 5 non-pest niche Active tabs + 8 Intermediary List firm tabs + Premium Pest Full Target List (sanity check on source pool).
- Out of scope per request: Attio Active Deals records (different surface, different rules), JJ Call Log tabs 5.26-5.29.26 (already cleaned today).
