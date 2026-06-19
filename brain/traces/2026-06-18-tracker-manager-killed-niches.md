---
schema_version: 1.1.0
date: 2026-06-18
type: trace
task: Kill niche-intelligence tracker rows
had_human_override: false
tags: [date/2026-06-18, trace, client/greenwich-and-barrow, topic/niche-intelligence, topic/tracker-manager, status/done]
---

## Context

Kay directed that three niches be marked killed in the Industry Research Tracker: SaaS for luxury, specialty coffee equipment servicing, and private art advisory. These rows were located in `TABLED` and moved to `KILLED` so the source-of-truth sheet reflects the decision.

## Decisions

### Move Tabled Rows To Killed Tab
**AI proposed:** Treat the instruction as a tracker-manager status update and write directly to the tracker after snapshotting.
**Chosen:** Copied `Private art advisory firms`, `Specialty Coffee Equipment Service`, and `Vertical SaaS for Luxury & High-Value Asset Service Industries` from `TABLED!A23:H25` into `KILLED!A39:H41` with status `Killed` and kill date `2026-06-18`, then cleared the original `TABLED!A23:H25` rows.
**Reasoning:** Kay explicitly said these niches should be killed in the niche-intel tracker; leaving them in `TABLED` with status text changed would preserve an inconsistent tracker state.
**Pattern:** #tracker-source-of-truth

## Learnings

When Kay says a niche is killed and it is already in `TABLED`, move it to `KILLED` rather than simply changing status in place. Snapshot both tabs and verify the writeback.
