---
name: feedback-no-direct-task-writes-from-skills
description: "Derived skills (post-call-analyzer, etc.) stage tasks for Kay's morning-briefing approval; they NEVER write directly to the TO DO sheet."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9955477e-c1cb-4801-b01e-ad731993a6df
---

When a skill produces tasks for Kay (action items from a call transcript, follow-ups from a CIM read, intermediary touch reminders, etc.), it MUST stage the tasks for the next morning-briefing review instead of appending them directly to the TO DO sheet.

**Why:** Kay needs to (a) approve each task and (b) assign which day it belongs on before anything lands on her tracker. Direct writes by skills create surprise tasks she didn't approve, surface no day-context, and corrupt her morning planning by mixing pre-approved work with derivative-skill noise. Stated 2026-05-28 in the context of post-call-analyzer: "Instead of just adding them there, can you include them in the morning brief and then I can decide what days they should be done and if they are approved before adding to the file."

**How to apply:**
- Skills that derive task-shaped items from upstream signals (post-call-analyzer, deal-evaluation, pipeline-manager future expansions, niche-intelligence follow-ups) write to a per-skill `pending-tasks/{run_id}.json` staging dir under `brain/trackers/{skill}/`. Each task object includes `task_text, type, project, suggested_day, suggested_due_date, notes, source_ref, staged_at`.
- Pipeline-manager's morning briefing Section reads ALL pending-tasks directories (one per task-staging skill), surfaces each task with Obama framing: **RECOMMEND: Schedule "{task}" on {suggested_day}** → YES (with day) / NO / DISCUSS.
- On Kay's YES + day assignment, pipeline-manager (or Claude orchestrator) invokes `task-tracker-manager append` with the chosen placement. The staged file moves to `pending-tasks/processed/{run_id}.json` after success.
- On Kay's NO, the staged file moves to `pending-tasks/declined/{run_id}.json` with the decline reason captured.
- Skills retain the right to write Google Docs, Attio notes, vault call notes, and Slack pings autonomously — those are read-only-for-Kay artifacts, not commitments on her time. The TO DO sheet is uniquely time-commitment territory and needs human-in-the-loop.

**Mistake to avoid (recurring failure mode):** delegating "append to TO DO via task-tracker-manager" inside a derived skill's stop-hook chain. That's a direct write — wrong shape even with the delegation pattern. The DELEGATES-TO-task-tracker-manager wording in old SKILL.md files is the smell; rewrite as STAGES-FOR-PIPELINE-MANAGER-APPROVAL.

**Related:** [[feedback-decision-fatigue-minimization]] (each staged task gets Obama framing), [[project-personal-task-tracker]] (TO DO sheet schema), [[feedback-kay-handles-all-replies]] (analogous human-in-the-loop pattern for outbound email).
