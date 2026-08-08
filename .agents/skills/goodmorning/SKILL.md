---
name: goodmorning
description: "Morning operating bookend for Kay and Greenwich & Barrow. Use when Kay says \"good morning\", invokes /goodmorning, asks for a morning briefing, or starts the daily operating rhythm. Preserves the Claude-era morning orchestration: email intelligence, relationship manager, pipeline manager, prior decisions, day-of-week overlays, Sunday tracker build, and a concise decisions-only briefing."
---

# Good Morning

## Contract

Run the morning operating system, not a generic greeting. Preserve the Claude-era `/goodmorning` behavior unless a Phase 2.5 improvement explicitly changed it.

Non-negotiables:
- Never send emails.
- Do not depend on Superhuman.
- Use 1Password-backed credentials for external services.
- Do not make scheduled jobs depend on MCP until tested.
- Do not create duplicate weekly tracker files.
- Keep the final briefing decision-oriented, with no filler.
- Use plain business language. Do not mention validator names, exit codes, JSON, scripts, stack traces, or code-level diagnoses unless Kay explicitly asks for technical detail. Translate technical health into what changed, whether it matters to Kay, and whether action is needed.

## Morning Flow

1. Read the latest Good Night / closeout context if available. Resolve this by globbing `brain/context/session-decisions-*.md` and selecting the latest file at or before the operating date; if none exists, continue and mark the source as absent rather than failing.
2. Run or review `email-intelligence` and `relationship-manager` in parallel when credentials and schedules allow.
3. Cross-reference open items from `brain/context/session-decisions-*.md` and recent Good Night ledgers. Use the latest existing file at or before the operating date; never hard-fail because an exact prior-day file is missing.
4. Run or review `pipeline-manager` for deal, niche, investor, and relationship context.
5. Check Active Outreach:
   - Skip DealsX Email unless Kay explicitly re-enables it.
   - Use Kay Email and cold-call channels only.
   - Treat old `JJ` references as legacy cold-call compatibility, not current user-facing naming.
6. Verify cold-call operations fired when scheduled. Do not re-run if the job already produced a current artifact.
7. Apply day-of-week overlays.

## Day-Triggered Weekly Skills Section

Every Good Morning brief must include a compact section for skills that are expected specifically because of the day of week. This is a dashboard-facing status section, not a task-list repeat.

Section label: `Day-Triggered Weekly Skills`

Rules:
- Include only skills whose schedule or doctrine is specific to the current weekday.
- State `done / pending / failed / not scheduled today` with the latest artifact or failure signal when available. For scheduled Friday weekly tracker/dashboard copy-down work, do not ask Kay whether to run it; verify it, run/repair it if missing, and report only the plain-language result.
- If a scheduled strategic cycle was expected to run and did not produce its artifact, Good Morning must surface it as a red decision item the next morning. Use the format: `🔴 [System] RECOMMEND: Investigate failed {cycle name} run -- {plain-language missing artifact / impact} -> YES / NO / DISCUSS`. This applies especially to Monday-night `niche-intelligence` for Tuesday review and Thursday-night thesis signal scan for Friday review and Sunday-night `conference-discovery` for Monday registration review.
- If a scheduled weekly skill has not run yet because Kay launched Good Morning early, say so plainly and give the expected run window.
- If the skill is trigger-based rather than weekday-scheduled, mention it only when the trigger is present or when Kay has specifically asked about it.
- Numbering continues from the rest of the brief.

Day map:
- Sunday: weekly task tracker build; target-discovery Phase 2 at 3pm ET; cold-call operations prep at 6pm ET; conference-discovery at 9pm ET.
- Monday: conference-discovery / Conference Pipeline status from the Sunday run.
- Tuesday: niche-intelligence CEO-decision status from Monday night.
- Friday: Thursday-night thesis signal scan status before Friday systems work; weekly-tracker/dashboard copy-down snapshot/export; health-monitor Friday report; calibration-workflow Thursday-night run for Friday meta-calibration. The weekly tracker/dashboard copy-down is expected every Friday; Good Morning should verify it and trigger/repair it when missing rather than asking Kay.

Budget manager note:
- `budget-manager` is not a standing Friday weekly skill. It is trigger-based from bookkeeper/StartVirtual monthly P&L or Balance Sheet delivery. Surface it in this section only when a budget-manager trigger/output exists, or when the month-end missing-report watchdog is relevant.

## Email Orchestration Pre-Dashboard Rule

The Good Morning brief is the edit surface; the dashboard becomes the reference after the brief. For the `Email Orchestration` section, `24-hour thank-yous` must be built from **prior-day external meetings/calls**, not same-day calendar items. Before briefing:

1. Run or review `scripts/refresh_email_orchestrator_status.py`; it seeds prior-day external meetings/calls into `brain/context/email-follow-through-backlog.json`.
2. Verify each prior-day thank-you against Gmail sent mail via `gog`/email-orchestrator evidence.
3. If sent evidence exists, report it as verified/completed and do not ask Kay to approve it.
4. If no sent evidence exists, surface the person/event as a numbered Good Morning item for Kay approval before writing or keeping it active on the dashboard.
5. For 48-hour follow-ups and EOW follow-ups, check Gmail sent-mail evidence before surfacing the row. Suppress completed rows; include first names for verified completions and active rows. Never say only "N rows completed" or hide names behind "+N more".
6. EOW follow-ups must name each unresolved person. If the identity/source is unclear, raise the exact person/context in the morning brief instead of posting a generic reminder.
7. After Kay responds, route approved unsent thank-you work through the email-orchestrator/task-manager path; never send email.

## Task Manager Carry-Forward Stop Hook

Good Morning is not complete until Task Manager has been verified. Before writing the morning brief:

1. Run `task-tracker-manager` / `scripts/task_tracker.py sync-done-status` to reconcile checked day-tab items back to the To Do tab.
2. Determine the current live day tab. For every earlier live day tab in the current week (`Sun` through yesterday), run a dry-run carry-forward into the current day: `scripts/task_tracker.py carry-forward-day --from {prior_day} --to {current_day} --dry-run`.
3. If any prior-day dry run shows pending moves, execute those carry-forwards before the brief, earliest day first, then run `scripts/task_tracker.py report`.
4. Carry-forward must include overflow task rows above the visible `NOTES` header, not just canonical rows 17-41. If report/carry-forward disagree on counts, treat that as a Task Manager health failure.
5. If carry-forward cannot run, is blocked, or the report still shows unprocessed items on any earlier live day tab, surface this in the **System Health** section as a numbered failure item. Do not say the task tracker is ready.
6. Do not repeat the user's full To Do list in the brief. Do not report total open-task counts or overdue-task counts; Kay will work the list directly and the count is not healthy/helpful for her. Only surface new system-generated items that are not already on the To Do sheet, or a Task Manager failure that blocks the list from being usable.

Stop condition: if Task Manager verification is skipped or inconclusive, the Good Morning brief must mark **System Health: Task Manager carry-forward unverified** and recommend repair before day planning.


## Post-Call Task Intake Stop Hook

Good Morning is not complete until staged post-call action items have been reviewed. This prevents Granola/post-call analysis from creating hidden task debt.

Before writing the morning brief:

1. Scan `brain/trackers/post-call-analyzer/pending-tasks/*.json`, excluding `pending-tasks/processed/`.
2. Parse every JSON array or object with a `tasks` / `items` array. Ignore files with zero tasks only after naming them in the operator notes or health detail.
3. Deduplicate against the current To Do sheet by exact `task_text` match plus obvious already-completed task text match. Do not surface tasks already present on the To Do sheet unless the staged item contains materially new context.
4. Group remaining staged tasks by source call title/person when available; include the source analysis Doc link when present.
5. Surface only actionable next steps in a numbered **Post-Call Action Items** section with the format: `{task} -- from {call/person}; RECOMMEND: add to {suggested_day or today/this week} -> YES / NO / DISCUSS`. Do not convert decisions, strategy questions, or discussion prompts into tasks. If an item is a decision rather than an action, either omit it or put it in the relevant dashboard/business section as a concise discussion item.
6. Keep this section decision-oriented. If there are many items, prioritize 3-5 highest-signal items and do not dump the whole backlog. Avoid backlog counts unless they indicate a system failure Kay must act on.
7. After Kay responds, approved items route through `task-tracker-manager`; rejected/skipped items are recorded in the session decisions or staging resolution notes. Only after approval/rejection is recorded should the related staged task file move to `brain/trackers/post-call-analyzer/pending-tasks/processed/{note_id}.json`.

Stop condition: if staged post-call tasks exist and are not surfaced, the Good Morning brief must mark **System Health: post-call staged tasks pending but not surfaced** and recommend repair before saying the morning run is complete.

## Day Overlays

Sunday:
- Prepare the weekly task canvas.
- Use `task-tracker-manager` and `scripts/task_tracker.py build-week` where appropriate.
- Dry-run or check for an existing current-week file before creating anything.
- Prior week files are immutable history.
- Carry incomplete prior daily tasks into the new weekly review surface.
- Do not distribute tasks into new daily tabs until Kay has reviewed/approved the week.

Monday:
- Confirm `conference-discovery` status and whether the Conference Pipeline was updated.
- If the Sunday conference-discovery run failed, did not run, or did not update/land the expected status artifact, surface it as a red system decision item before normal Monday planning.
- Keep Slack notification tight: link + number added this week + number added future weeks.

Tuesday:
- Confirm `niche-intelligence` CEO-decision status from the Monday-night full run.
- If the Monday-night niche-intelligence run failed, did not run, or did not land the expected Tuesday review artifact, surface it as a red system decision item before normal Tuesday planning.
- If the Monday-night niche-intelligence run succeeded, Tuesday Good Morning must surface the top thesis recommendations directly to Kay as `Activate / Hold / Kill / Test` decisions. For any `Activate` or `Test` recommendation, include a separate **Channel Decision** before target build or outreach begins.
- Tuesday channel-decision format: `RECOMMEND: Activate/Test {niche}; Tracker Channel = {Kay Email / DealsX Email / Cold-Call-Only / No outreach yet}; Execution Path = {Kay warm outreach / DealsX batch / call-first / conference / intermediary}; Reason = {one sentence} -> APPROVE CHANNEL / EDIT / DISCUSS`. Include owner split: Kay / Camilla / DealsX / Codex. Do not allow target-discovery, DealsX, Camilla cold qualifiers, or Kay outreach to start from an activated thesis until the channel is approved and written to the Industry Research Tracker `Outreach Channel` field. If the execution path is conference/intermediary/no-outreach, do not run target-discovery until a target-build channel is separately approved.
- Do not defer default thesis review to Camilla or an analyst call; Camilla is routed in after Kay chooses where economics, modeling, or diligence support is needed. After Kay makes a thesis and channel decision, route the update through `tracker-manager`/`niche-intelligence` so the Industry Research Tracker reflects the decision, Outreach Channel, and next channel owner; do not leave the decision only in chat.

Friday:
- Confirm the Thursday-night thesis signal scan landed before Friday systems work.
- If the scan failed, surface it as a red system decision item.
- If the scan succeeded, surface only signal-change decisions: urgent fast sprint, queue for Monday full run, park, or no-action. If a Friday urgent fast sprint is recommended, include the same **Channel Decision** format before any target build or outreach begins. Do not create a full thesis-review block on Friday unless a signal is genuinely time-sensitive.
- Surface any new niches that emerged from calls, email, or pipeline activity only when they change a Friday decision.
- Confirm weekly tracker/dashboard copy-down snapshot/export, `health-monitor`, and `calibration-workflow` status. If the weekly snapshot/export is missing by the morning run, run the copy-down/weekly snapshot path or flag a repair, not a Kay decision.
- For July 2026 focus, suppress broad non-urgent post-call backlog and source/plumbing prompts that are not tied to jewelry or the long-term holdco vision. The next two-week operating focus is jewelry and long-term holdco vision unless Kay changes it.

## Briefing Format

The Good Morning brief is Kay's daily edit surface. Keep all existing checks running underneath, but organize the final output around the correct weekday operating rhythm so Kay can decide what belongs in each work block.

Monday-Thursday use the deal-momentum operating rhythm:

```
Good morning. {Weekday}, {Month D}. Dashboard: [https://agent-vps-7731c88b.tail868ef9.ts.net](https://agent-vps-7731c88b.tail868ef9.ts.net)

No emails were sent.

**Today's Operating Read**
- What changed:
- Must-win outcome:
- Park / ignore today:

**9:30-11:00 Outreach Work**
- Highest-leverage seller / investor / broker / analyst actions:
- Direct asks that need to go out:
- Follow-ups that should be dropped or deferred:

**11:00-1:00 Relationship / Call Window**
- Confirmed calls:
- Prep needed:
- Desired outcome for each call:

**1:00-4:00 Strategy / Research**
- Core strategic question:
- Deck / model / research work:
- What would increase conviction or expose a no:

**8:30 Decision Review**
- What to review tonight:
- What to roll forward:
- Optional bounded continuation block, only if energy is there:

**System Health**
- Include only if something needs Kay's attention or a broken-system escalation is required.
```

Friday uses a different operating rhythm and should not be forced into the Monday-Thursday deal-momentum blocks.

Summer Friday format:

```
Good morning. Friday, {Month D}. Dashboard: [https://agent-vps-7731c88b.tail868ef9.ts.net](https://agent-vps-7731c88b.tail868ef9.ts.net)

No emails were sent.

**Today's Operating Read**
- What changed:
- Must-win outcome:
- Park / ignore today:

**10:30-11:30 Personal Finance / Wealth Monitor**
- What needs review:
- Direct asks or follow-ups:
- What can wait:

**11:30-12:30 Nonprofit Operations**
- Required actions:
- Decisions or approvals:
- What can wait:

**12:30-1:30 Family Admin**
- Required actions:
- Decisions or approvals:
- What can wait:

**1:30-2:30 Systems / G&B Housekeeping**
- System or dashboard work:
- Website / file / tracker cleanup:
- What can wait:

**8:30 Decision Review**
- What to review tonight:
- What to roll forward:
- Optional bounded continuation block, only if energy is there:

**System Health**
- Include only if something needs Kay's attention or a broken-system escalation is required.
```

Post-9/10 Friday format:

```
Good morning. Friday, {Month D}. Dashboard: [https://agent-vps-7731c88b.tail868ef9.ts.net](https://agent-vps-7731c88b.tail868ef9.ts.net)

No emails were sent.

**Today's Operating Read**
- What changed:
- Must-win outcome:
- Park / ignore today:

**9:30-11:00 Personal Finance / Wealth Monitor**
- What needs review:
- Direct asks or follow-ups:
- What can wait:

**11:00-12:00 Nonprofit Operations**
- Required actions:
- Decisions or approvals:
- What can wait:

**12:00-1:00 Family Admin**
- Required actions:
- Decisions or approvals:
- What can wait:

**1:00-3:00 Systems / Website / G&B Housekeeping**
- System or dashboard work:
- Website / file / tracker cleanup:
- What can wait:

**3:00-4:00 Weekly Review + Next Week Setup**
- Weekly review:
- Next-week setup:
- What to close before Monday:

**8:30 Decision Review**
- What to review tonight:
- What to roll forward:
- Optional bounded continuation block, only if energy is there:

**System Health**
- Include only if something needs Kay's attention or a broken-system escalation is required.
```

Presentation rules:
- Write the brief in Kay's working style: direct, practical, plain-spoken, and close to her language. Prefer phrases like `what changed`, `must-win`, `park / ignore today`, `what needs to go out`, `what can wait`, `where this belongs`, and `does this need action?`. Avoid consultant-y polish, generic productivity coaching, and technical/internal wording unless Kay asks for it.
- Every surfaced item that Kay may respond to must be numbered. Numbering should continue across the whole brief and should not reset by section. Section headings stay unnumbered; `N/A` lines can be unnumbered when there is truly nothing to decide.
- Answer these questions explicitly: what changed since yesterday, today's must-win outcome, what should be ignored or parked, what belongs in Outreach Work, what belongs in Relationship / Call Window, what belongs in Strategy / Research, and what should wait for 8:30 Decision Review.
- Preserve the underlying intelligence sources and checks: Email Orchestration, Active Pipeline, Deal Aggregator, Schedule / Meeting Briefs, Week Schedule / Task Manager, Post-Call Action Items, Day-Triggered Weekly Skills, and System Health.
- Map each surfaced item into the work block where Kay should decide or act on it. Do not keep legacy buckets as the main visible structure unless Kay asks for diagnostic detail.
- Monday-Thursday route recommendations into the deal-momentum blocks: Outreach Work, Relationship / Call Window, Strategy / Research, and 8:30 Decision Review.
- Friday route recommendations into the Friday blocks instead: Personal Finance / Wealth Monitor, Nonprofit Operations, Family Admin, Systems / G&B Housekeeping, Weekly Review + Next Week Setup when post-9/10, and 8:30 Decision Review.
- On Friday, do not recommend normal outreach, email pushes, or calls unless tied to a live seller, investor, lender, or LOI-critical deadline.
- Keep the output decision-oriented and short. Do not create a long task dump, do not repeat the To Do list, and do not report total open-task counts or overdue-task counts.
- Protect peak energy: put external-momentum work first in the Outreach block, especially seller, investor, broker, analyst, and direct-ask items.
- Preserve afternoon for strategy, research, deck work, model thinking, thesis-building, diligence questions, and conviction-building.
- Use `RECOMMEND: ... -> YES / NO / DISCUSS` only where Kay needs to approve a write, draft, brief, tracker change, or work-block choice.
- Use plain business language. Avoid technical names unless the system issue is actionable for Kay.
- Include "No emails were sent" whenever email was inspected or drafts were discussed.
- If a section has nothing useful, write `N/A` for that line rather than inventing filler.

Include:
- current blockers
- dashboard pointer in the header
- explicit note if no email was sent
- broken-system escalation at the end only if attention is needed

Avoid:
- raw logs
- long summaries
- unapproved execution
- burying the recommendation

## Success Criteria

The run is complete when Kay has a concise daily decision brief, scheduled/core status has been checked, Task Manager carry-forward has been verified or repaired, staged post-call tasks have been surfaced or explicitly marked as a System Health failure, Sunday tracker behavior is safe, and no unreviewed email-sending or duplicate tracker action occurred.
