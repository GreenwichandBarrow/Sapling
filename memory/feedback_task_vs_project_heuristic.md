---
name: Task vs project — heuristic for the post-call-analyzer + task-tracker-manager
description: Task = one-off item, fits in a single sitting or follow-up. Project = multi-week coordinated initiative with multiple work streams (deal-aggregator-build pattern). Locked 2026-05-06 during post-call-analyzer skill spec.
type: feedback
originSessionId: 326c69dd-5175-4205-89f6-eb4a9ec64ab8
---
**Rule:** When classifying call output (and any other source of action items) for routing into Kay's task tracker:

- **Task** = one-off item that fits in a single sitting or single follow-up. Single discrete action. Goes to the **TO DO sheet capture point** (single-line append).
- **Project** = multi-step coordinated initiative spanning weeks, with multiple work streams. Multi-skill, multi-file, multi-week. Goes to a **new (or existing) project tab** on the same TO DO file.

**Examples (Kay's framing):**
- Project: the deal-aggregator build, the intermediary-channel build, the broker-channel formalization. These had multiple sub-builds (Apollo enrichment, Sheet hygiene, dedup logic, template doc, Slack ping wiring) over weeks.
- Task: "submit the Axial member-application form," "send the Lehman-scale screenshot Andrew offered," "reply to Allison Allen's PWIPM offer."

**Classifier signal for the post-call-analyzer skill:** "Is this a single discrete action, or a plan with multiple coordinated sub-builds?" If the call discussed it as a system / channel / build / framework / multi-week plan, it's a project. If it's "send X to Y" or "decide on Z," it's a task.

**Edge case — borderline 2-3 step items:** Default to task. Project = clearly multi-week with multiple work streams. If unsure, ask Kay at the analysis-result point ("This looks like a project — confirm?").

**Three-category outcome from post-call-analyzer:**
1. **Tasks** → task-tracker-manager (capture-point append on TO DO sheet)
2. **Projects** → task-tracker-manager (new or existing project tab)
3. **Decisions** (need Kay's input) → next morning briefing's Decisions list, surfaced via pipeline-manager

**How to apply:**
- post-call-analyzer skill (when built) uses this heuristic in its classifier prompt.
- task-tracker-manager already supports both surfaces (single-task append + Gantt project tabs per its SKILL.md). Routing happens at the analyzer's classifier step.
- For non-call sources (Granola transcripts, Gmail action items, manual asks): same heuristic applies.

**Source:** Kay confirmed 2026-05-06 evening during post-call-analyzer skill spec discussion. Verbatim: "Task is a one off item. Project is more like when we laid out a multi week plan to create our deal aggregator / intermediary channel outreach."
