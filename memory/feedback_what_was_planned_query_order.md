---
name: What was planned — query order
description: When Kay asks "what was planned/scheduled for X," query calendar → beads → brain/outputs/ → session-decisions in that order. Never trust session-decisions alone.
type: feedback
originSessionId: dd4c82da-5390-4ce9-b7be-4739713ae9be
---
When Kay asks "what was planned for X," "what was scheduled for X," or "what session was supposed to happen on X" — query in this order:

1. **Calendar first** (`gog calendar events --from "DATE" --to "DATE+1" --json`). Time-blocked commitments live here. Created-date on the event tells you when the commitment was made. Description field often points at the plan file + bead.
2. **Beads second** (`bd ready` / `bd show <id>`). Active multi-step work tracked here per CLAUDE.md.
3. **`brain/outputs/` third** (`grep -rni "TERM" brain/outputs/`). Plans, deliverables, and tech-debt docs live here per CLAUDE.md "Outputs → Deliverables." Tagged with `topic/`, `output/plan`, `status/draft`.
4. **`brain/context/session-decisions-*.md` last.** These capture *retrospective* in-conversation decisions, not *prospective* schedule. They are partial.

**Why:** 2026-04-25 miss — Kay had a 7-hour calendared block "Tech-debt block: launchd hardening" (created 4/20, plan in `brain/outputs/2026-04-25-saturday-launchd-hardening-plan.md`, bead `ai-ops-1`). When she asked "did the multi-hour tech debt session happen today?" Claude searched only `brain/context/` and `memory/`, missed the plan file in `brain/outputs/`, never queried the calendar, never queried beads. Took two follow-up prompts ("look at earlier in the week" then "what specifically scheduled for 11am") before Claude checked the calendar. The word "tech-debt" was literally a tag on the plan file.

Root pattern: Claude conflated "what did Claude write about" with "what was planned." Session-decisions are one source out of four.

**How to apply:** Any time the question references *future-tense planning* ("planned," "scheduled," "supposed to," "going to," "blocked off"), the answer-finder must run all four queries before reporting "not found." If calendar returns nothing, say so explicitly — "no calendar event found for that day" — rather than reporting from session-decisions alone.
