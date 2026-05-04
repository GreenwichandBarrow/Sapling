---
schema_version: 1.2.0
date: 2026-05-04
type: prd
status: draft
skill_origin: deal-aggregator
kay_approved: null
kay_approval_date: null
people: []
companies: []
projects: []
hypothesis: null
trace: null
task_ref: null
published_url: null
tags: ["date/2026-05-04", "output", "output/prd", "status/draft", "topic/deal-aggregator", "topic/intermediary-channel", "topic/buy-box"]
---

# Deal Aggregator Dual-Filter Spec (STRICT vs OPPORTUNISTIC)

This spec describes the file-level changes required to add a SECOND buy-box filter (broker-channel opportunistic) to the deal-aggregator skill, producing three-tier tagging on every match (`STRICT` / `OPPORTUNISTIC` / `OUT`). It does NOT modify any code or skill file. Implementation order is in section 9.

Authoritative inputs:
- Plan: `/Users/kaycschneider/.claude/plans/vivid-booping-starfish.md`
- Memory: `memory/feedback_broker_channel_opportunistic_floor.md` (G&B 5/3 lock)
- Memory: `memory/feedback_strategic_thresholds_need_grounding.md` (no relaxing financial floor)
- Memory: `memory/feedback_deal_screen_300k_salary_15pct_margin.md` ($2M EBITDA + 15% margin practical floor)
- Current skill: `.claude/skills/deal-aggregator/SKILL.md`

## 1. Filter Logic Flowchart (text form)

For every scraped or email-inbound match, in this exact order:

```
INPUT: listing {company, industry, revenue, ebitda, margin, geography, source_type, source_name}

STEP 1 — HARD-EXCLUDE GATE (applies to BOTH filters):
  IF industry matches: lending | carve-out | fashion
  OR geography == California
  OR PE-consolidator-acquired (already-owned)
    -> TAG = OUT
    -> STOP. Do not continue.

STEP 2 — STRICT FILTER (existing industry buy-box):
  Resolve which buy-box doc applies:
    Insurance brokerage   -> Insurance Buy Box
    Vertical SaaS         -> SaaS Buy Box
    Other                 -> Services Buy Box
  Apply Data Availability Rule (missing field never auto-rejects).
  IF passes industry buy-box (financials + structure + industry hard-excludes per doc + thesis-or-new-niche match):
    -> TAG = STRICT
    -> ROUTE: existing Slack flow (#active-deals, one message per deal, fingerprint dedup)
    -> STOP.

STEP 3 — SOURCE ROUTING GATE for OPPORTUNISTIC eligibility:
  IF source_type NOT IN {Email-only broker, Newsletter blast, Advisory + Deal Platform,
                         Marketplace + Email, Email-only broker + Buyer Portal}:
    -> TAG = OUT
    -> STOP. (Industry-niche-only sources cannot produce OPPORTUNISTIC matches.)

STEP 4 — OPPORTUNISTIC FILTER (broker-channel buy-box, industry-AGNOSTIC):
  Geography hard gate:
    IF geography NOT IN {NY, NJ, PA, CT}  (geography window pending G&B lock; baseline)
    OR geography NOT DISCLOSED  -> TAG = OUT (geography is the load-bearing gate; no
                                              "not disclosed" benefit)
  Financial gates (NEVER relaxed; per feedback_strategic_thresholds_need_grounding):
    EBITDA disclosed AND >= $2M           -> pass
    margin disclosed AND >= 15%            -> pass
    EBITDA or margin "not disclosed"       -> pass (Data Availability Rule)
    EBITDA disclosed AND < $2M             -> TAG = OUT
    margin disclosed AND < 15%             -> TAG = OUT
  Owner-transition viable (30-90 day handover, no irreplaceable founder dependency)
  Revenue band: informational only (NOT a gate on broker channel)
  IF all gates pass:
    -> TAG = OPPORTUNISTIC
    -> ROUTE: Slack #active-deals with explicit "[OPPORTUNISTIC; broker channel]"
              prefix in the message body so G&B reviewer/analyst can read tag instantly
    -> STOP.

DEFAULT (any non-pass at any step that did not tag) -> TAG = OUT.
```

Notes:
- STRICT is checked first. A deal that passes STRICT is NEVER also tagged OPPORTUNISTIC. STRICT supersedes.
- A deal can only be OPPORTUNISTIC if its source_type is in the broker/IB-eligible set AND it failed STRICT.
- Hard-excludes (CA, lending, carve-out, fashion) are evaluated ONCE up-front and apply to both filters.

## 2. Source Routing (which sources can produce OPPORTUNISTIC)

Reads the existing Sourcing Sheet `Type` column (sheet ID `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw`, General Sources + Niche-Specific Sources tabs). No new column. No sheet modifications.

| `Type` value (Sourcing Sheet) | Can produce STRICT? | Can produce OPPORTUNISTIC? |
|---|---|---|
| Marketplace | Yes | No |
| AI Marketplace | Yes | No |
| Private Deal Network | Yes | No |
| Email-only broker | Yes | Yes |
| Newsletter blast | Yes | Yes |
| Advisory + Deal Platform | Yes | Yes |
| Marketplace + Email | Yes | Yes |
| Email-only broker + Buyer Portal | Yes | Yes |
| Strategic Acquirer | INTEL only | No |
| Industry Publication | INTEL only | No |
| News + Community | INTEL only | No |
| Advisory (intel-only) | INTEL only | No |
| `Type` blank or unknown | Yes (default STRICT-only) | No |

Industry-niche-specific sources (Sica Fletcher, Agency Checklists, PCO Bookkeepers, etc.) classify under their actual `Type` value. Most are `Email-only broker` or `Advisory + Deal Platform` and therefore CAN produce OPPORTUNISTIC matches if they happen to send a $2M+ EBITDA + 15%+ margin + NY/NJ/PA/CT deal outside their niche specialty.

## 3. Artifact Schema Additions

File path: `brain/context/deal-aggregator-scan-{date}.md` (and `-{date}-afternoon.md`).

### 3a. New required section header

Insert AFTER `## Deals Surfaced (sent to Slack individually)` and BEFORE `## Email Inbound Deals`:

```markdown
## Broker-Channel Matches (OPPORTUNISTIC)

1. **{Company/Profile}** — {Source} | {Type from Sourcing Sheet} | {Revenue or "not disclosed"} | {EBITDA} | {Margin} | {Geography} | OPPORTUNISTIC | {Link}
```

Conditional rendering rules:
- If artifact has at least one match tagged `OPPORTUNISTIC` -> section is REQUIRED with full row(s).
- If artifact has zero `OPPORTUNISTIC` matches -> header still appears with body `None today.` (matches existing pattern for Email Inbound Deals / Near Misses).

### 3b. Existing "Deals Surfaced" section becomes STRICT-only

Rename body framing (header text unchanged for backwards-compat with the validator section list; see section 4):

```markdown
## Deals Surfaced (sent to Slack individually)

(STRICT matches only; pass industry buy-box.)

1. **{Company/Profile}** — {Source} | {Revenue} | {EBITDA} | STRICT | {Match type} | {Link}
```

### 3c. Frontmatter additions (optional; tracked for analytics)

Add to YAML frontmatter:

```yaml
deals_strict: {n}
deals_opportunistic: {n}
deals_out: {n}
```

`deals_found` (existing) = `deals_strict + deals_opportunistic`. `deals_out` is informational only (does NOT include OUT items already filtered before Near Misses).

### 3d. Source Scorecard column update

Existing 7 columns: `Source | Category | Status | HTTP | Listings Reviewed | Matches | Last Match Date`. Update `Matches` column semantics: it remains TOTAL match count per source (STRICT + OPPORTUNISTIC summed). No new columns required.

(Friday digest may later split STRICT/OPPORTUNISTIC counts per source; out of scope for this spec; tracked in plan section "headless-friday-prompt.md — Source Scorecard reports STRICT/OPPORTUNISTIC/OUT counts per source".)

## 4. Validator Additions (`scripts/validate_deal_aggregator_integrity.py`)

Current state: `DAILY_SECTIONS` list has 5 entries (lines 41-47).

Required change: add `## Broker-Channel Matches (OPPORTUNISTIC)` to the `DAILY_SECTIONS` list, between `## Deals Surfaced` and `## Email Inbound Deals`. New section count is **6** for daily artifacts (morning + afternoon).

Updated list:

```python
DAILY_SECTIONS = [
    "## Deals Surfaced",
    "## Broker-Channel Matches (OPPORTUNISTIC)",
    "## Email Inbound Deals",
    "## Near Misses",
    "## Source Scorecard",
    "## Volume Check",
]
```

Friday digest (`DIGEST_SECTIONS`) **unchanged**; still 5 sections.

Optional add (low priority, defer to Phase 2 hardening): validate that frontmatter contains `deals_strict`, `deals_opportunistic`, `deals_out` keys when filter logic is wired. NOT required for v1 cutover.

## 5. Headless Prompt Additions

### 5a. `headless-morning-prompt.md`

Edit target: "Mandatory ordering — execute in this exact sequence" block, lines 18-27 currently.

Step 2 currently reads "Load buy-boxes (Services / Insurance / SaaS Google Doc IDs in SKILL.md)". Update to:

```
2. **Load buy-boxes** — Services / Insurance / SaaS Google Doc IDs (industry filter)
   AND the Broker-Channel Opportunistic Buy Box doc ID (channel filter). Live read every
   run; never cache.
```

Insert NEW step 6.5 between current step 6 (Apply buy-box filters) and current step 7 (Fingerprint dedup):

```
6.5. **Apply dual-filter logic per the SKILL.md flowchart** —
     For every match: hard-exclude gate -> STRICT industry buy-box check.
     If STRICT pass, tag STRICT. If STRICT fail AND source_type is in the broker-eligible
     set AND deal passes the geography hard gate AND the financial floors, tag
     OPPORTUNISTIC. Else tag OUT. Tag is REQUIRED on every surfaced match; no untagged
     output.
```

Update step 9 (write artifact); add to the section-header inventory:
- Insert `## Broker-Channel Matches (OPPORTUNISTIC)` between Deals Surfaced and Email Inbound Deals. Empty section keeps header with "None today" body (existing convention).

Update "What success looks like" block:
- Bullet 1 currently: "Artifact exists at today's date, ≥ 200 bytes, has frontmatter + all 5 required section headers." -> change "5" to "6".

Add to "Forbidden in headless mode" block (new bullets):
- Auto-promoting an OPPORTUNISTIC match to STRICT to "round it up"; defeats the filter. Tag must reflect actual gate passed.
- Applying any industry-strict screen to the OPPORTUNISTIC filter; that filter is industry-AGNOSTIC by construction. Hard-excludes only (CA, lending, carve-out, fashion).
- Surfacing OPPORTUNISTIC matches from non-broker source_types. If `Type` is `Marketplace` / `AI Marketplace` / `Private Deal Network`, the deal is STRICT-or-OUT; never OPPORTUNISTIC.

### 5b. `headless-afternoon-prompt.md`

Same edits as 5a, applied to the parallel block (currently lines 17-27 for ordering, lines 30-35 for success criteria, lines 37-46 for forbidden-mode list).

Additionally: afternoon Source Scorecard scope is the time-sensitive subset (Rejigg / Flippa / Everingham & Kerr / email channel). Dual-filter applies identically; afternoon-run matches go through the same flowchart.

### 5c. `headless-friday-prompt.md`

Lighter touch; the digest format already differs. Two edits:

1. In step 4 (read fingerprint store), add: "Group fingerprint matches not just by source but also by tag (STRICT vs OPPORTUNISTIC) where the artifact frontmatter records it. Older artifacts (pre-cutover) lack this field; treat as STRICT for backfill."

2. In Source Productivity table (digest section 1), add a note: "Trend arrow reflects total match count. Once frontmatter `deals_strict` / `deals_opportunistic` keys are populated for a full 7-day window, split the table into two columns (`7d STRICT Matches`, `7d OPPORTUNISTIC Matches`); Phase 2."

NO change to Friday digest's 5-section structure or `DIGEST_SECTIONS` validator list.

## 6. Forbidden Patterns to Ban (codified in SKILL.md + headless prompts)

| Forbidden pattern | Why |
|---|---|
| Auto-promote an OPPORTUNISTIC match to STRICT | Defeats the dual-filter; tags must reflect actual gate passed |
| Apply OPPORTUNISTIC industry-strict screen | OPPORTUNISTIC is industry-agnostic by construction (Megan Lawlor pattern, G&B 5/3) |
| Lower EBITDA floor below $2M for OPPORTUNISTIC | Financial floor is constraint-driven ($300K salary + debt service); REJECTED G&B 5/3 |
| Lower margin floor below 15% for OPPORTUNISTIC | Same; constraint-driven, never source-relative |
| Tag a match from a `Marketplace` source as OPPORTUNISTIC | Marketplaces are STRICT-only; opportunistic eligibility is broker/IB sources only |
| Treat geography "not disclosed" as a pass on OPPORTUNISTIC | Geography is the load-bearing gate on the broker buy-box. Undisclosed = OUT, not flag-for-review |
| Skip OPPORTUNISTIC section in artifact when zero matches | Section header must always render (with "None today" body); validator requires it |
| Hardcode buy-box bands in SKILL.md or headless prompts | Buy-box bands live in the 4 Drive docs, period (existing rule reinforced) |
| Surface OPPORTUNISTIC matches without explicit "[OPPORTUNISTIC; broker channel]" prefix in Slack | G&B reviewer/analyst need tag visible at-a-glance to triage thumbs up/down differently |

## 7. Edge Cases

| Case | Disposition |
|---|---|
| Geography fails (e.g., FL deal) but financials clear OPPORTUNISTIC bands | OUT. Geography is hard gate on broker channel. |
| OPPORTUNISTIC hard-exclude hit (CA / lending / carve-out / fashion) | OUT. Hard-excludes evaluated up-front, supersede everything. |
| Source_type unknown or blank on Sourcing Sheet | Default STRICT-only. Cannot produce OPPORTUNISTIC. Log "source type unknown" in scan artifact for calibration. |
| Listing has no source_type because it came via email-scan-results from a sender not yet in the Sourcing Sheet | Default STRICT-only for v1. Phase 2 (email-intelligence reputation rule v1) auto-classifies via Attio Intermediary Pipeline read. |
| Deal disclosed at $1.8M EBITDA, 18% margin, NY-based, broker source | OUT (EBITDA fails $2M floor, never relaxed). |
| Deal disclosed at $2.5M EBITDA, "margin not disclosed", NJ, broker source | OPPORTUNISTIC (Data Availability Rule; undisclosed margin doesn't reject; financials disclosed-and-pass; geo pass; source eligible). |
| Deal passes STRICT (industry-niche thesis) AND would also pass OPPORTUNISTIC | STRICT only. STRICT supersedes; never double-tag. |
| Deal previously surfaced as STRICT, re-listed by a broker today | Fingerprint dedup catches it. Skip Slack regardless of tag. |
| Industry-niche source (e.g., Sica Fletcher) sends a deal with `Type: Email-only broker` that happens to be a NJ specialty insurance deal at $3M EBITDA / 18% margin | STRICT (Insurance buy-box passes). Never escalates to OPPORTUNISTIC because STRICT already passed. |
| Same Sica Fletcher source sends an out-of-niche (e.g., Marble & Granite) NJ deal at $3M EBITDA / 18% margin | OPPORTUNISTIC (industry not on thesis -> STRICT fails -> falls into OPPORTUNISTIC since `Email-only broker` is eligible). |
| OPPORTUNISTIC deal arrives but Broker-Channel Buy Box Drive doc is unreachable | Skill failure mode: log `buy_box_broker_source: cached` in frontmatter, fall back to vault snapshot at `brain/context/buy-box-broker-channel.md` (per plan section "Stored artifacts"). Continue tagging. |

## 8. Test Plan (Tue May 5 work block; validate against last 30 days)

### 8a. Inputs
- Last 30 calendar days of `brain/context/deal-aggregator-scan-*.md` artifacts (~ Apr 5 to May 4). Verified present: 2026-04-10, 04-13, 04-14, 04-15, 04-16, 04-17, 04-20, 04-21, 04-22, 04-22-afternoon, 04-23, 04-23-afternoon, 04-27-afternoon, 04-28, 04-28-afternoon, 04-29, 04-29-afternoon, 04-30-afternoon, 05-01, 05-01-afternoon (>= 20 artifacts; gap days noted).

### 8b. Procedure (offline, no live scrape)
1. Spawn one explore-style subagent with the new flowchart (section 1 of this spec) loaded as input.
2. Subagent reads each scan artifact's `## Near Misses` section and its `## Deals Surfaced` section.
3. For every listing in those sections, subagent re-classifies under the dual-filter:
   - Hard-exclude check (CA / lending / carve-out / fashion)
   - STRICT (industry buy-box, using current Drive doc IDs)
   - OPPORTUNISTIC (geography + $2M / 15% / source-type)
4. Subagent outputs `brain/outputs/2026-05-05-dual-filter-validation.md`:
   - Table: artifact-date | listing | original-tag (STRICT pass / Near Miss) | new-tag (STRICT / OPPORTUNISTIC / OUT)
   - Counts: how many Near Misses would have flipped to OPPORTUNISTIC under the new filter
   - Anomalies: any STRICT matches that the new flowchart would re-classify (should be ZERO if logic is correctly STRICT-supersedes)

### 8c. Acceptance criteria
- >= 1 OPPORTUNISTIC match would have surfaced over the 30-day window (validates filter is not vacuous).
- <= 25 OPPORTUNISTIC matches over 30 days (validates filter is not noise; target is 5-10/week per plan, so 30 days = 20-40 max; over 25 means filter too loose).
- ZERO STRICT matches re-classified to OPPORTUNISTIC (validates STRICT-supersedes logic).
- ZERO OPPORTUNISTIC matches from non-broker source_types (validates source routing).
- Hard-excludes (CA / lending / carve-out / fashion) tag OUT in 100% of cases (validates gate ordering).

### 8d. Live cutover gate (after validation passes)
1. Wire `DAILY_SECTIONS` change in validator (single-line edit).
2. Wire SKILL.md flowchart text + forbidden patterns (one section addition).
3. Wire 3 headless prompts (parallel edits).
4. Trigger one manual run: `launchctl start com.greenwich-barrow.deal-aggregator`
5. Verify: scan artifact has 6 section headers; OPPORTUNISTIC section present (with "None today" body if no matches); validator exits 0; Slack pings (if any) carry `[OPPORTUNISTIC; broker channel]` prefix.
6. If validator fails or Slack format wrong -> revert all 5 files, re-spec.

## 9. Recommended Tuesday Work Order

| Order | File | Reason |
|---|---|---|
| 1 | `scripts/validate_deal_aggregator_integrity.py` | Single-line change to `DAILY_SECTIONS`. Passing tests gate everything downstream; fix the gate first. |
| 2 | `.claude/skills/deal-aggregator/SKILL.md` | Add flowchart + Broker-Channel Buy Box doc ID reference + forbidden patterns. SKILL.md is the source of truth headless prompts reference. |
| 3 | `.claude/skills/deal-aggregator/headless-morning-prompt.md` | Highest-volume run path. Wire dual-filter ordering + tag requirement + section count change. |
| 4 | `.claude/skills/deal-aggregator/headless-afternoon-prompt.md` | Parallel edits to morning. Same dual-filter, narrower source scope. |
| 5 | `.claude/skills/deal-aggregator/headless-friday-prompt.md` | Lightest touch; only narrative additions, no structural section changes (digest stays 5 sections). |

Run validation (section 8) BEFORE step 1 (offline replay against last 30 days of artifacts) to confirm flowchart logic is correct. Don't edit any file until the offline replay passes acceptance criteria.

## 10. Implementation Risks Flagged

1. **Drive doc dependency on Mon work.** The Broker-Channel Opportunistic Buy Box Drive doc has not been created yet (G&B creates Mon per plan). If that doc isn't built before Tue's filter wire-up, headless runs fall back to vault snapshot which may not exist either. Mitigation: gate Tue work on Mon's Block 4 (11:45am-1pm) completion.

2. **Geography gate "not disclosed" semantics conflict with Data Availability Rule.** The Data Availability Rule (SKILL.md line 49) says missing data never auto-rejects. This spec carves out an exception for geography on OPPORTUNISTIC. That conflict needs explicit codification in SKILL.md (and the buy-box Drive doc) or it will get re-litigated. Mitigation: lock language in SKILL.md update and in the Drive doc body when G&B drafts Monday.

3. **Source type drift on Sourcing Sheet.** The dual-filter is critically dependent on the `Type` column of the Sourcing Sheet being correct and current. If a row's `Type` is mis-labeled (e.g., a marketplace mis-tagged as `Email-only broker`), it creates false OPPORTUNISTIC tags. No automated detection. Mitigation: spot-check the 7 broker-eligible Type values during Mon list verification (Block 6), audit Sourcing Sheet types same time.
