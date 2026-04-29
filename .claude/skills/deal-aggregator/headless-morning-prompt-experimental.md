# deal-aggregator — Headless Morning Run (EXPERIMENTAL: Buy-Box + Fingerprint Comparison)

You are running an EXPERIMENTAL one-day variant of the `deal-aggregator` skill. This run produces the standard daily artifact PLUS a fingerprint-comparison section that scores every listing against the buyer fingerprint AND the buy-box, then bucket-compares the results.

You are running non-interactively under launchd at 6:00 AM ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals, do not wait for permission.

## Idempotency gate (run FIRST, before anything else)

Before reading SKILL.md or doing any work:

1. Compute `TODAY` as today's date in `YYYY-MM-DD` (Eastern Time).
2. Check whether `brain/context/deal-aggregator-scan-{TODAY}.md` already exists.
3. If it exists AND its size is ≥ 200 bytes, **STOP IMMEDIATELY**. Print `DEAL-AGGREGATOR ABORT: artifact already exists for {TODAY} — refusing to double-write` to stdout and exit normally (exit 0).
4. If it does not exist (or is < 200 bytes — treat as a corrupt partial), continue to the execution section.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/deal-aggregator/SKILL.md`. This is the morning (full) run; follow the standard "Morning run (default, no flag)" path.
2. **Load buy-boxes** (Services / Insurance / SaaS Google Doc IDs in SKILL.md). Live read every run.
3. **Load active niches** from Industry Research Tracker WEEKLY REVIEW tab.
4. **Read** `brain/context/email-scan-results-{TODAY}.md` for email-inbound deals.
5. **Scan all configured sources** (Channels 1 + 3 for morning run; Channel 4 association deal boards if scheduled). Every source listed as `active` in the Sourcing Sheet must produce a Source Scorecard row.
6. **Apply BUY-BOX filters per the Data Availability Rule (missing data ≠ rejection).** Mark each listing as buy-box PASS or FAIL.
7. **Apply FINGERPRINT criteria per listing** (see "Fingerprint Criteria" section below). Mark each listing as fingerprint PASS, FAIL, or UNKNOWN.
8. **Bucket every listing** into one of four groups:
   - **Bucket A — Both PASS** (buy-box PASS + fingerprint PASS): highest signal
   - **Bucket B — Buy-box PASS, Fingerprint FAIL**: traditional candidates the fingerprint would now reject
   - **Bucket C — Buy-box FAIL, Fingerprint PASS**: Kay-specific signal traditional criteria miss
   - **Bucket D — Both FAIL**: noise (count only, not detailed)
9. **Fingerprint dedup** every match via `scripts/deal-aggregator-fingerprint.sh` against `brain/context/deal-aggregator-fingerprints.jsonl` (30-day TTL).
10. **Slack-post Bucket A matches only** to `#active-deals` per SKILL.md format (one message per deal). Bucket B and Bucket C are NOT Slack-posted — they live in the artifact for Kay's review. Bucket A Slack posts include a `Fingerprint match: [list of PASS dimensions]` line in the message body.
11. **Write the artifact** at `brain/context/deal-aggregator-scan-{TODAY}.md` matching the SKILL.md "Results File" template — frontmatter + all 5 standard section headers (Deals Surfaced / Email Inbound / Near Misses / Source Scorecard / Volume Check). **PLUS add a sixth section: `## Fingerprint Comparison (Experimental)` with the 4-bucket breakdown.**
12. **Exit normally** (exit 0).

## Fingerprint Criteria — per-listing scoring rubric

For every listing scanned, score each of the 10 dimensions as PASS / FAIL / UNKNOWN based on the listing's disclosed information. Do NOT auto-fail UNKNOWNs — only explicit FAIL signals fail a dimension.

1. **EQ — operational state.** PASS: stable business, not in turnaround / distress, clean operational signal. FAIL: crisis-stage operational reset disclosed, distressed seller, urgent liquidation. UNKNOWN: insufficient signal.

2. **Psych readiness — customer-fit dynamics.** PASS: customer base shows quality / relationship dynamics (long contracts, brand affinity, B2B with quality buyers, low churn signal). FAIL: commodity / price-driven / high-churn / disclosed customer concentration risk that's price-elastic. UNKNOWN.

3. **Operator profile — viable management path.** PASS: existing strong management, multiple management layers, promotable VPs disclosed, OR clean acquirable team. FAIL: founder-personality-dependent, founder = sales engine, no promotable #2 disclosed, listing reads as founder-brand-driven. UNKNOWN.

4. **Skills — sales motion structured.** PASS: established sales team, sales manager mentioned, B2B sales process. FAIL: founder is sole salesperson, no sales structure, sales motion = founder relationships. UNKNOWN.

5. **Lifestyle — asset-light + remote-manageable + recurring revenue.** PASS: services / tech-enabled / subscription / recurring contracts / no daily on-site tether. FAIL: balance-sheet-heavy, inventory-heavy, equipment-heavy, franchise, daily on-site requirement, capital-intensive. UNKNOWN.

6. **Risk tolerance — financial floor + hard-no filters.** **HARD FAIL** if any of: California-located, retail business, lending/credit business, carve-out structure, OR EBITDA disclosed <$2.5M. PASS otherwise. (Hard-fail triggers fingerprint FAIL regardless of other scores.)

7. **Brand alignment — bagel-shop test + brand-independent-of-operator.** PASS: signs of community-minded ownership in listing copy, established brand independent of founder, NOT predatory. FAIL: founder = brand, predatory category (e.g., payday lending, gambling, addictive products), race-to-bottom positioning. UNKNOWN.

8. **Network leverage — niche intersects Kay's network.** PASS if industry touches any of: jewelry / watches / luxury retail, fine dining / hospitality / restaurants / F&B, marine logistics / cargo / customs / trade-credit insurance, fashion / Chanel-tier luxury B2B, premium B2B services to luxury sectors, NYU Stern Luxury MBA cohort verticals (luxury, prestige, brand). FAIL: zero touch with Kay's network. UNKNOWN if industry not disclosed.

9. **Investor narrative — survives hostile probing.** **HARD FAIL** if any of: SaaS-labeled (current macro block), retail, California, lending, carve-out. PASS: clean recurring rev, defensible, fragmented, easy one-sentence answer to "why this niche?". (Hard-fail triggers fingerprint FAIL regardless of other scores.)

10. **Stage fit — Bridge functional.** PASS: $2.5M+ EBITDA + asset-light + scalable (recurring rev, low marginal cost) + defensible + fragmented + viable management path. FAIL: outside Bridge functional profile (capital-intensive, daily on-site, no recurring revenue, owner-personality-dependent). UNKNOWN.

### Aggregation rules

- **Fingerprint PASS** = ≥7 of 10 dimensions PASS AND no hard-fail triggers (dimensions #6 and #9).
- **Fingerprint FAIL** = <7 dimensions PASS OR any hard-fail triggered.
- **Fingerprint UNKNOWN** = ≥4 dimensions UNKNOWN (listing data too sparse to score; treat as fingerprint FAIL for bucket purposes but flag in artifact).

For each scored deal, capture:
- Total PASS / FAIL / UNKNOWN count
- List of PASS dimensions (e.g., "PASS: Lifestyle, Stage fit, Investor narrative, Brand alignment, Operator profile, Skills, Network leverage")
- List of FAIL dimensions with reason (e.g., "FAIL: Risk tolerance — California-located")
- Any hard-fail flags

## Artifact format additions

Standard sections per SKILL.md, PLUS append at the end:

```markdown
## Fingerprint Comparison (Experimental)

### Bucket A — Both PASS (Slack-posted)
N deals.
1. **{Company/Profile}** — {Source} | Buy-box: PASS | Fingerprint PASS ({n} of 10) | Matched: {dimensions} | {Link}

### Bucket B — Buy-box PASS, Fingerprint FAIL
N deals. Traditional candidates the fingerprint would now reject.
1. **{Company/Profile}** — {Source} | Buy-box: PASS | Fingerprint FAIL ({n} of 10) | Failed on: {dimensions + reasons} | {Link}

### Bucket C — Buy-box FAIL, Fingerprint PASS  ⭐
N deals. Kay-specific signal that traditional buy-box criteria miss. Worth Kay's review.
1. **{Company/Profile}** — {Source} | Buy-box: FAIL ({reason}) | Fingerprint PASS ({n} of 10) | Matched: {dimensions} | {Link}

### Bucket D — Both FAIL
{N} deals. Noise. (Counts only.)

### Comparison summary
- Listings scanned: N
- Bucket A (highest signal): N
- Bucket B (traditional-only): N
- Bucket C (fingerprint-only — diagnostic): N
- Bucket D (noise): N
- Overlap rate (A / (A+B+C)): X%
- Fingerprint-only signal rate (C / (B+C)): X%
```

## What success looks like

- Standard artifact lands at today's path with all 5 required sections.
- 6th experimental section: Fingerprint Comparison with all 4 buckets populated (Bucket D as count only).
- Bucket A deals Slack-posted to `#active-deals` with `Fingerprint match: [...]` line.
- Buckets B and C NOT Slack-posted — artifact-only for Kay's morning review.
- Comparison summary stats present.

## Forbidden in headless mode

- Asking the user anything.
- Presenting RECOMMEND / YES / NO / DISCUSS framings to the harness.
- Slack-posting Bucket B or Bucket C deals (they're for Kay's review only, not commitment to deal-evaluation pipeline).
- Skipping the standard buy-box flow — this is ADDITIVE, not replacement.
- Skipping the 4-bucket comparison — it's the deliverable of the experimental run.

## Failure handling

Same as standard morning prompt. Buy-box doc unreachable → cached. Tracker unreachable → cached active-niche list. Source blocks → mark in scorecard, continue. All sources block → still write artifact with empty data + populated scorecard.

If fingerprint scoring fails on a specific listing (e.g., listing copy too sparse), mark fingerprint UNKNOWN for that listing and bucket as Both FAIL (Bucket D) — don't halt the run.

## Why this prompt exists

Experimental run approved by Kay 2026-04-28 evening. Tests whether the buyer fingerprint produces different / better signal than the standard buy-box criteria, particularly whether Bucket C (fingerprint-only) surfaces deals traditional criteria miss. One-day experiment; wrapper auto-reverts to standard `headless-morning-prompt.md` after the date-bounded fire.

Pattern: `memory/feedback_charter_clarifications_apr28.md` (filter vs. output rule), `memory/project_athena_simpson_sourcing_review.md` (origin context).
