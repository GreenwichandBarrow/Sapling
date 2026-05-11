---
name: parallel_tracks_pipeline_during_build
description: Never sacrifice pipeline work for infrastructure builds. Parallel tracks required, even mid-major build phase.
type: feedback
originSessionId: a7305dfd-d3d9-44c7-840b-f8de8eb9bfd8
---
When Kay greenlights a significant infrastructure build (server migration, new skill development, system refactor), she expects the work to run on a **parallel track** alongside ongoing pipeline work — never as a substitute for it.

**The rule:** If a build day or build week is happening, pipeline work (intermediary outreach, Active Deals advancement, Templates Doc iteration, target-list build, deal-evaluation followups) MUST continue in parallel. Don't pause pipeline to "focus on the build." Don't surface infra-only briefings on build days.

**Why:** Kay learned this from a prior session where pipeline decayed during an infrastructure phase. Quote: *"my learning from previously is we can loose our pipeline while building, we have to do both."* The deal funnel doesn't tolerate quiet weeks. A 2-week build phase with no pipeline activity = a 2-month gap in deal flow because of cold-restart inertia on outreach threads.

**How to apply:**
- When approving a build (server, skill, refactor), explicitly name what Track B (pipeline) work runs in parallel that day/week.
- Morning briefings during build phases must surface BOTH infra decisions AND pipeline decisions. Never collapse to one bucket.
- If Track A (infra) is consuming all of Claude's tool budget, push Track B work to subagents and run concurrently. Don't serialize.
- When Kay says "we have to do both" — that's the doctrine, not a one-off preference. Apply forward.
- If a deferred pipeline item (e.g., V2-V8 Templates rebuild from 4/30) is sitting >2 days while build work proceeds, re-surface it explicitly as a Track B reminder.

**Source:** Kay 2026-05-01, after approving Harrison server-migration + launchd-debugger skill build alongside intermediary-list build-out.
