---
schema_version: 1.1.0
date: 2026-05-05
type: trace
today: "[[notes/daily/2026-05-05]]"
task: DealsX New Verticals (May) target-list dedup against Kay's network
had_human_override: true
importance: high
target: skill:outreach-manager
tags: ["date/2026-05-05", "trace", "topic/dealsx-dedup", "topic/intermediary-channel", "pattern/engagement-bar-not-record-existence", "pattern/visual-only-on-external-sheets"]
---

# Decision Trace: DealsX DNC Engagement-Bar + Visual-Only Marking

## Context

Sam @ DealsX delivered a target sourcing universe of 20,606 companies across 12 tabs ("Greenwich & Barrow - New Verticals (May)", file id `1VaviHqaJT9Wtm6X1h9B6Q8aOrA8adTiBvt851pkEUFg`). Sam collects success fees only on engaging "new" targets — meaning anyone Kay has already engaged contaminates the new-target claim AND risks brand damage if Sam touches a contact Kay was warming. Need was: cross-check the universe against Kay's network and tag DNC where Sam should not call.

The first dry-run pass over-flagged: it used Attio Company existence as the bar and produced 65 candidate matches across 12 tabs. Kay reviewed and refined.

## Decisions

### DNC threshold: engagement bar, not record existence

**AI proposed (initial pass):** Mark "DO NOT CALL" if the company appears in Attio Companies AT ALL (any record, even stubs Linkt-built or auto-created and never engaged). Bias toward over-flagging per Kay's earlier instruction.

**Chosen (Kay refined):** Mark "DO NOT CALL" only if ANY of:
- Material engagement: Gmail thread (sent or received) within 24 months, vault call note, Granola transcript, Attio Person record with `status` ≠ `prospect`, OR Attio Company with linked notes/interactions/pipeline membership
- LinkedIn 1st-degree connection (from `Complete_LinkedInDataExport_03-23-2026.zip.zip`)

Stub-only Attio records (record exists, zero engagement, no LI tie) → **GO for Sam, no DNC tag.**

**Reasoning:** Kay's lens — preserving optionality on a stub Kay was never going to chase herself is low-value. Letting Sam test the universe is free intelligence. The cost of over-flagging is real (every false-positive shrinks Sam's call universe and undercuts the success-fee economics). The cost of under-flagging is brand damage on an actually-warmed contact. Engagement-bar splits the difference — strict on the "we're warming this" side, permissive on the "we never touched this" side.

**Pattern:** #pattern/engagement-bar-not-record-existence

### Visual-only marking on Sam's sheet (no text writes to his columns)

**AI proposed:** Write `DO NOT CALL — Kay engaged via {channel}` text into the blank scratch field on Sam's sheet. Use Kay's mirror sheet as a separate audit reference.

**Chosen (Kay overrode mid-execution):** Pure visual highlight only. Apply red background fill to the populated columns of each DNC row. Do NOT write any text into Sam's sheet columns. The DNC reasoning lives only in Kay's separate G&B-owned mirror sheet (file id `1zxi7G-1oYBKv1yKzmqJaTzC5oGgkNV7iPfL1nMgEtkQ`).

**Reasoning:** Sam @ DealsX requested visual highlighting specifically. Sam's team has its own data model and workflow on his sheet — adding text into scratch columns may interfere with how their callers process rows. Visual highlighting is non-destructive and channel-agnostic. The brief audit trail still exists in Kay's mirror sheet (which Sam can read but Kay owns).

The first execution subagent was killed cleanly before any text writes happened (verified scratch field G8:G10 still empty post-kill). Re-spawned with visual-only scope.

**Pattern:** #pattern/visual-only-on-external-sheets

### Pre-approved targets ignore DNC logic entirely

**AI proposed:** Apply the same DNC bar to all 65 candidates uniformly.

**Chosen:** Drop from DNC list any company that appears in `SHARED WITH DEALS X` Drive folder (id `12UgqowuC8Hm7fj80r4bxHeuVb25hzkJQ`). These are companies Kay explicitly handed Sam — pre-approved go regardless of engagement signal. The dedup logic ignores them.

**Reasoning:** Kay sending a target to Sam IS the explicit "go." Re-applying engagement-bar logic on top would re-flag her own intentional handoffs. Final classification: 23 of 65 dropped as pre-approved (largest overlap was the 20 art storage targets Kay had already shared).

**Pattern:** #pattern/explicit-handoff-overrides-derived-rules

### Name-fallback matches require domain confirmation (false-positive guard)

**AI proposed:** Use both domain match (primary) AND normalized name match (fallback for Attio records lacking domain field) when computing matches.

**Chosen (kept the strategy, but added validation):** Name-fallback matches must have a corroborating signal beyond name string-similarity. The classifier subagent caught 3 false positives mid-pass and reclassified them as GO_stub_only:
- **Reliance** — vault hits were Reliance the *insurance company* in unrelated calls, not the DealsX target's website `artcloud.com` (which itself was a data leak from a prior row)
- **Bill** — DealsX name field was just "Bill" (truncated); 17 vault hits were proper-noun "Bill" across calls, no `ba-law.com` engagement
- **Archive Corporation** — vault grep matched the generic word "archive" (Camilla calls, Rauschenberg entity), not `archivecorp.com`

**Reasoning:** Generic short tokens ("Bill", "archive") and common-word company names cause noisy name-match hits. Domain-grounding (does the matched signal actually involve the company's domain?) cuts these. This is implicit in the FINAL JSON's `false_positive_notes` block but worth codifying.

**Pattern:** #pattern/name-match-needs-domain-corroboration

## Why This Trace Matters

A future agent re-running this dedup or a similar one (e.g., next batch of DealsX targets, or a new sourcing partner relationship) will face the same forks:

1. **The "any record" lazy default.** It's tempting to treat Attio existence as the DNC bar — it's the simplest set membership check. But it over-restricts and misses the asymmetric cost: false-positives directly hurt Sam's economics, false-negatives only matter if you actually re-engage the contact (and you usually won't). Engagement-bar is harder to compute but correct.

2. **The "obvious place to write" default.** When marking up an external partner's sheet, Claude's default move is to write text into a scratch column. That's the right move on G&B-owned sheets. On a partner's sheet, it can interfere with their workflow. Always ask — or default to the lowest-impact marking convention (visual-only) and let the partner ask for more.

3. **The "uniform rule" trap.** Applying the dedup rule to all candidates uniformly missed the explicit-handoff carve-out. Kay sending targets to Sam is itself a decision; that decision overrides the derived rule.

4. **The "name-similarity is enough" trap.** Generic words and truncated names cause false-positive hits in name-only matching. Domain-grounding is the cheap fix.

## Key Insight

**The DNC bar is a tradeoff between brand damage (false-negatives) and success-fee economics (false-positives), not a data-completeness exercise.** The right bar minimizes the asymmetric cost. For DealsX-style success-fee partnerships, that's engagement-bar; for a relationship Kay actively wants to protect (e.g., direct cold outreach by Kay herself), the bar may be tighter. Re-derive per partner.
