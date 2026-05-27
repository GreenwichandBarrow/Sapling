---
name: feedback-outreach-channel-universes-separate
description: "Hard rule — outreach target universes across channels (DealsX / JJ / Kay-Email / Conference / Intermediary) must remain separate. No company appears in two channels' active target lists. Codified 2026-05-26."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 37de3c90-d2d0-44f1-9b4b-ddb0727158c9
---

A company that is being touched by one outreach channel MUST NOT appear in another channel's active target list. Cross-channel touching of the same company is forbidden. This is a HARD rule, not a soft preference.

**Why:** Kay 2026-05-26: *"outreach targets must remain separate."* The failure mode: uncoordinated phone + email + LinkedIn DM from G&B (across DealsX + JJ + Kay-Email) hitting the same owner in the same week reads as spam, burns sender reputation, and signals desperation. Multi-touch sequencing CAN outperform single-channel — but only when sequenced and coordinated, never parallel. G&B cannot coordinate with Sam's DealsX team at the per-company level (Sam owns the contact universe externally), so the only safe operating mode is hard separation.

**How to apply:**

1. **Every target-list build (any channel) cross-references all other active channels' target universes BEFORE adding a row.** The dedup is a build-time precondition, not a post-build cleanup.

2. **Channel target universes to cross-reference:**
   - DealsX — Drive Verticals sheet `1VaviHqaJT9Wtm6X1h9B6Q8aOrA8adTiBvt851pkEUFg` ("Greenwich & Barrow - New Verticals (May)"), per-niche tabs (e.g. `Specialty Pest & ENV Service (Good Fit) Valid`)
   - JJ (cold call) — `Premium Pest Management - Target List` `1Y0ZjEkc2LHhBoO4QGO8Ny9MvG90NpojQn8bloKA291I`, per-week `Call Log M.D.YY` tabs + Full Target List
   - Kay Email (warm + cold-email niches) — niche-specific target list sheets per the Industry Research Tracker Col D = `Kay Email`
   - Conference — Conference Pipeline sheet (attendee lists registered as outreach pool)
   - Intermediary — `Intermediary Target List` Sheet `18zzE1y-BU1xuD-y0BOmEl8GtJ4I-iclSuBqAi0q3pkk`

3. **Removal pattern:** when cross-referencing finds an overlap, the OWNING-CHANNEL target stays; the new-tab target is REMOVED (row deleted, not annotated). This is the 2026-05-26 calibration — see [[feedback-jj-excludes-dealsx-touched-companies]] for the JJ-specific implementation. Annotation-and-keep is the OLD pattern, replaced.

4. **Owning channel = first-touch:** the channel that started outreach to that company owns it until either (a) the cadence closes (reply received OR final no-reply touch sent), or (b) Kay explicitly reassigns. The other channel can pick up only AFTER ownership releases.

5. **Apollo enrichment runs AFTER dedup, never before.** Apollo credits cost money and the cost of enriching a row about to be deleted is pure waste. Build target tab → cross-reference all channels → remove overlaps → THEN run Apollo enrichment on the survivors. Per Kay 2026-05-26: *"enRich through Apollo, not before you eliminate those ones."*

6. **Match logic:** lowercased company name, strip entity suffixes (Inc/LLC/Corp/Co/Ltd), collapse punctuation. Address/zip secondary signal for ambiguous names. Strict-on-match (avoid false positives that lose a real outreach row); if uncertain, KEEP and flag for Kay rather than delete.

**Snapshot before any cross-channel dedup deletion** — `brain/context/rollback-snapshots/{channel}-dedup-{ISO timestamp}.json`.

**Tab-floor flag:** if dedup drops a JJ daily Call Log tab below 20 rows (JJ's call floor), surface to Kay loudly — do NOT auto-backfill from other lanes (that could re-introduce overlap).

**Skill homes that need this baked in:**
- `target-discovery` — pre-build dedup before Apollo enrichment
- `list-builder` — same
- `jj-operations` Sunday weekly build — dedup before tab finalize (currently retro-cleanup; bake it forward)
- `conference-engagement` — when adding conference attendees to a tab, check they're not on DealsX/JJ active lists
- `outreach-manager` — when scheduling a new cadence on a target, check no other channel is mid-cadence

See also: [[feedback-jj-excludes-dealsx-touched-companies]], [[feedback-dealsx-skip-target-discovery]], [[feedback-dealsx-sprint-source-of-truth]], [[feedback-attio-autocreate-person-not-list]].
