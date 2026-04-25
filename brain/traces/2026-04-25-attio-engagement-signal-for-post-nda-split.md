---
schema_version: 1.1.0
date: 2026-04-25
type: trace
today: "[[notes/daily/2026-04-25]]"
task: Split Attio closed deals into post-NDA failures vs pre-NDA outreach attrition
had_human_override: false
importance: high
target: script:refresh_attio_snapshot
tags: [date/2026-04-25, trace, topic/attio, topic/dashboard, pattern/engagement-signal-as-stage-history-proxy, domain/technical]
---

# Decision Trace: Use meaningful_conversation/notes as engagement signal when stage history isn't available

## Context

Active Deal Pipeline closed strip lumped all 132 lifetime closures together, including ~130 cold-outreach attrition that never reached NDA. Mockup wanted post-NDA failures only (~12 per the fake mockup data). Without splitting, Kay's "what deals did I lose meaningful conversations on" surface was buried in noise.

The clean approach would be to query Attio's stage history per record — show me deals that ever reached NDA before closing. But Attio's `entries/query` endpoint returns ONLY current state per `entry_values.stage` (single entry, no historical array). No `previous_stage` field. No activity log endpoint that gives stage transitions cheaply.

## Decisions

### Heuristic for "did this deal have real engagement?"

**Considered:**
- (a) `created_at != stage.active_from` — moved through ≥1 stage before close. Ran the test: 29 of 132 closures matched, but 28 of those were `created=2026-03-14, closed=2026-03-30` (bulk-import artifact). Heuristic too noisy.
- (b) Query stage history via separate Attio endpoint. Doesn't appear to exist for list entries (only person/company record values via `?show_historic=true` which adds expense + complexity).
- (c) Use `meaningful_conversation` checkbox + `notes` field on the entry. Both are populated only when there was actual engagement.

**Chosen:** (c). Audit across all 132 closures: 2 had engagement signal (both via notes attached), 130 did not. Matches Kay's mental model — she'd remember talking to those 2.

**Reasoning:** Attio's data model gives us a *behavioral* signal (did anyone attach a note?) when *structural* signal (stage history) isn't available. Behavioral is sometimes better — a deal that reached NDA but had no real conversation isn't actually a "failure worth remembering," and a deal that never officially reached NDA but had a substantive call IS worth remembering. The heuristic surfaces the latter and excludes the former.

**Pattern:** #pattern/engagement-signal-as-stage-history-proxy

### Snapshot field shape

**Chosen:** Snapshot writes `closed_count` (lifetime total), `closed_count_post_nda`, `closed_count_pre_nda`. `closed_recent` filters to post-NDA only.

**Reasoning:** Total stays available for backward compat + situational use. Splits expose the meaningful number. Renderer can choose which to show without re-computing.

## Learnings

- **When a system doesn't expose the structural data you want, look for a behavioral proxy that's already populated by the existing workflow.** Don't reach for a custom data source first.
- **Heuristic noise audit before commit:** Always run the heuristic across the full dataset and verify the bucket sizes are plausible against the human's mental model. The "29 candidates" from the created_at heuristic looked plausible until I saw 28 were the same bulk-import day.
- **Future agent instruction:** when adding a new derived field that requires inferring something Attio doesn't directly store, default to (1) check if any existing field is populated by the relevant workflow (notes, meaningful_conversation, last_interaction), (2) audit across the full dataset to confirm the proxy actually correlates with the target concept, (3) only THEN consider building a new data source.
