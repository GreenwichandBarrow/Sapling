---
name: Collapse thin boundaries before building
description: When two pages/sections of an internal tool have overlapping mental models, recommend the merge before coding — Kay consistently prefers fewer, denser pages over more, narrower ones.
type: feedback
originSessionId: de241b73-de99-4d21-bbd3-29fb672018c8
---
When designing internal tools (dashboards, briefings, surface areas), if two pages or sections answer the same underlying question with different sort orders or subsets of the same data, recommend collapsing them before writing code.

**Why:** Validated 2026-04-24 during Command Center Session 4 design review. Two calls in one session: (1) dropped a "Today's Skill Activity Digest" zone from Infrastructure because it was a chronological re-sort of data already on C-Suite & Skills + Deal Aggregator + Dashboard landing tiles. (2) Merged Tech Stack page into Infrastructure because the connectivity-canary boundary was thin and split the mental model of "is the plumbing OK?" Kay confirmed: "wow I love infrastructure now." Merge cut 1 sidebar item, 1 landing tile, and shortened the build plan by half a session.

**How to apply:**
- Before building any new internal-tool surface, ask: "what unique question does this answer that nothing else does?" If the answer is "a different sort/filter of data already shown elsewhere," propose a filter tab on the existing surface instead.
- If two pages share an auth/health/status canary domain, default to one page with zoned sections, not two pages.
- Counterargument: depth justifies a separate page (e.g., Deal Aggregator vs. Deal Pipeline are both deal-related but answer different questions: "what's coming in?" vs. "what's in motion?"). Don't over-merge — the test is "would Kay get confused which page to open?"
- Frame the merge as a Decision (Obama framing) with the concrete sidebar/tile/build-plan deltas, not as an open question. Kay greenlit it immediately when given the count of what changed.
