---
date: 2026-05-28
type: context
title: "Session Decisions — 2026-05-28 (Thu, Guillermo prep redrafted in canonical format, post-call-analyzer task-staging doctrine + systemd cgroup-kill fix, JJ-Mondays-only memory)"
tags:
  - date/2026-05-28
  - context
  - topic/session-decisions
  - topic/investor-update-format-pivot
  - topic/post-call-analyzer-task-staging
  - topic/systemd-cgroup-detached-children
  - topic/jj-10am-slack-mondays-only
  - person/guillermo-lavergne
  - person/sam-transworld
  - person/carlos-in3o
  - person/greg-pitkoff
  - person/marsha-weiner
  - person/megan-lawlor
  - person/kyle-mcgrath
  - person/christopher-wise
  - company/ashford-ventures
  - company/transworld
  - status/done
---

# Session Decisions — 2026-05-28

Long Thursday that opened with a /goodmorning carried over from Wednesday's date rollover. Three doctrinal shifts (investor-update brief format anchored to April 9 golden + numbered situational sections + Insight lines; derived skills stage tasks for Kay's morning-briefing approval instead of writing direct to To Do; JJ 10am Slack delivery is Monday-only — Tue-Sun absence is by design). One infra fix landed (systemd KillMode=process on post-call-analyzer-poll service — root cause of 3 dropped call analyses this week). Guillermo biweekly brief rewritten end-to-end after format rejection.

## Decisions

### Skill format / doctrine

- **APPROVE:** **Investor-update biweekly + monthly format pivot.** Rejected the thematic-wall template (Headline / Buy-box / Thesis / etc.). Canonical format is the April 9, 2026 Guillermo doc: opening `Insight:` anchor line, numbered situational sections, each section = short bold title + 2-4 line body + underlined `Insight:` line, one bulleted niche section, NO Questions-for-{investor} section, NO frontmatter in Doc body. Promoted April 9 to [[entities/.claude/skills/investor-update/examples/biweekly/2026-04-09-guillermo-lavergne|examples/biweekly/2026-04-09-guillermo-lavergne]] as the new golden. Template rewritten + learnings.md entry added. See [[brain/traces/2026-05-28-investor-update-biweekly-format-pivot]].

- **APPROVE:** **Derived skills stage tasks for morning-briefing approval, never write direct to TO DO.** Kay: "Instead of just adding them there, can you include them in the morning brief and then I can decide what days they should be done and if they are approved before adding to the file." post-call-analyzer SKILL.md rewritten: step 6 now writes to `brain/trackers/post-call-analyzer/pending-tasks/{note_id}.json` instead of calling task-tracker-manager append; Slack message wording updated; failure handling updated; files-owned table updated. Memory: [[feedback-no-direct-task-writes-from-skills]]. pipeline-manager SKILL.md read-side update DEFERRED — needs Section-4 rewrite tomorrow.

- **APPROVE:** **JJ 10am Slack delivery is Monday-only.** Tue-Sun morning briefings will NOT flag missing daily jj-operations log as broken-system. Kay correction after I surfaced it 🔴 on Wed 5/27 brief. Memory: [[feedback-jj-10am-slack-monday-only]]. MEMORY.md updated.

### Infra fix

- **APPROVE:** **systemd KillMode=process on `post-call-analyzer-poll.service`.** Root cause of 3 dropped call analyses this week (Oswaldo 5/26 + Team TB JJ 5/27 + Jeff Stevens 5/27): oneshot service was cgroup-killing the `setsid nohup & disown` detached headless child. Fix landed: `KillMode=process` added to [Service] block; `systemctl --user daemon-reload && systemctl --user restart post-call-analyzer-poll.timer`; verified active(waiting), next fire 1pm ET 5/29. See [[brain/traces/2026-05-28-systemd-killmode-process-for-detached-children]].

### Morning briefing items (Wed 5/27 → Thu 5/28)

- **APPROVE (verb-fired by Kay):** Item 7 (post-call systemd fix) → APPLIED.
- **APPROVE:** Item 11 (office rent cut decision) → SCHEDULED to Fri 5/29 slot 5.
- **APPROVE:** Item 12 (walk through 7 calibration proposals) → QUEUED for post-Guillermo; did not execute today (Kay stepped away to draft thesis deck 12-1pm, then went into Guillermo prep).
- **REJECT:** Item 8 (Megan brief Fri 5/29 1:30pm) → SKIP.
- **PASS:** Item 6 (Carlos in3o demur) → Kay handles.
- **PASS:** Item 9 (Greg Pitkoff warm reply) → Kay handles.
- **DRAFTED:** Item 16 (Sam Curcio thank-you) → chat-only draft per `feedback_chat_drafts_dont_land_in_gmail`. Awaiting Kay's send approval + open question on search-fund redirect framing.
- **DEFERRED (not decided today):** Item 13 (weekly-tracker retire-vs-keep) — Kay asked for clarification, I explained historical preservation is safe either way; recommendation stands: keep through Q1, re-defer to 6/15.
- **DEFERRED (not decided today):** Item 14 (`_retired_*` tab delete) — Kay confirmed they're tabs in current TO DO file; awaiting delete decision.
- **DEFERRED (not decided today):** Item 15 (investor format kill-vs-close) — Kay didn't recognize the deferral; recommendation: kill from list as not load-bearing.

### Guillermo brief date bug

- **APPROVE (fix landed):** Guillermo biweekly call prep had wrong date (Fri 5/29) — actual call is Thu 5/28 at 2pm. Drive Doc `1ZCbN029W06gkIBB7oEUZ0ijm49MW1TXjd58xAc4aYlg` + vault file `brain/briefs/2026-05-28-guillermo-lavergne-biweekly-call-prep.md` corrected: "May 29, 2026" → "May 28, 2026"; "38 days since last live call" → "37 days"; Doc renamed to "Lavergne Call Prep 5.28.26".

## Actions Taken

- **CREATED:** `brain/briefs/2026-05-28-guillermo-lavergne-biweekly-call-prep.md` + Drive Doc `1ZCbN029W06gkIBB7oEUZ0ijm49MW1TXjd58xAc4aYlg` (BI-WEEKLY folder) — drafted then re-drafted in canonical format
- **CREATED:** `.claude/skills/investor-update/examples/biweekly/2026-04-09-guillermo-lavergne.md` (new biweekly golden, exported from Drive Doc `1dOBedsknSZWYdqQZfDC1aptp-a90_p4LHvFHjqPkYMQ`)
- **UPDATED:** `.claude/skills/investor-update/templates/biweekly-call-prep.md` (10 structural invariants encoded, April 9 anchored, thematic walls forbidden)
- **CREATED:** `.claude/skills/investor-update/learnings.md` with 2026-05-28 entry on format rejection
- **CREATED:** `memory/feedback_jj_10am_slack_monday_only.md` (new feedback memory)
- **CREATED:** `memory/feedback_no_direct_task_writes_from_skills.md` (new doctrine memory)
- **UPDATED:** `memory/MEMORY.md` index — JJ ops cluster line extended with 10am-Slack-Mondays-only rule
- **UPDATED:** `.claude/skills/post-call-analyzer/SKILL.md` (9 edits — description, policy table row 28, step 6 task-stage rewrite, Slack format line, "Does NOT" block, failure handling, files-owned table, linked memories)
- **UPDATED:** `~/.config/systemd/user/post-call-analyzer-poll.service` — added `KillMode=process` to [Service] block, daemon-reload + timer-restart verified active(waiting)
- **CREATED:** Task on Fri 5/29 day tab slot 5 — "Decide on office rent cut (15d deferred 5/13)"
- **DRAFTED:** Sam Curcio thank-you in chat (template-driven from canonical Intermediary Email Templates Doc) — NOT in Gmail per `feedback_chat_drafts_dont_land_in_gmail`
- **CORRECTED:** Guillermo Drive Doc title (`Lavergne Call Prep 5.29.26` → `Lavergne Call Prep 5.28.26`) + body date stamps
- **SENT:** 3 Slack pings to `#operations` (Guillermo prep ready × 2 + brief date corrected) — all 200 OK

## Deferred

- **Item 12 — Walk through 7 calibration proposals** — staged for next sit-down session; trigger = Kay says go. Per `feedback_decision_fatigue_minimization`, suggest bundling: I pre-rank with RECOMMEND on each, you YES/NO each in one pass.
- **Item 13 — `weekly-tracker` skill retire-vs-keep** — trigger 2026-06-15 per my standing recommendation (keep through Q1 investor update for closing-row data).
- **Item 14 — Delete `_retired_*` tabs in TO DO file** — awaiting Kay's go/no-go.
- **Item 15 — Investor-update purpose-first format choice** — recommend kill from list (not load-bearing); awaiting Kay's confirmation.
- **Item 16 — Sam Curcio thank-you SEND + Attio Contacted → Warmed** — drafted, awaiting Kay's send approval + open question on search-fund redirect framing for this email vs next touch.
- **post-call-analyzer pipeline-manager read-side wiring** — pipeline-manager SKILL.md Section 4 still references old "Granola transcripts" pull pattern; needs rewrite to read `brain/trackers/post-call-analyzer/pending-tasks/{note_id}.json` and present each task with RECOMMENDed day + YES/NO/DISCUSS. Trigger: tomorrow's /goodmorning OR explicit Kay instruction.
- **Carlos in3o broker-intro punt (item 6) + Greg Pitkoff warm reply (item 9)** — Kay handles personally.
- **Aging deferrals carried from 5/27** — only item 11 fired today; 12-16 still open. Recoverable when Kay returns.
- **DealsX + JJ wind-down notices** — paused pending pest 10-co June experiment outcome (6/30 verdict).
- **Phase 5 weekly-files first real rollover** — auto-fires Sun 5/31 AM via /goodmorning.

## Open Loops

1. **Sam Curcio thank-you send + Attio stage move** — chat-drafted today; needs Kay's send + send-decision on search-fund redirect framing.
2. **Items 12-15** — carryover from this morning's brief; tomorrow's /goodmorning surfaces them again if not addressed in next sit-down.
3. **pipeline-manager Section 4 read-side update** — the doctrine shift (staged-task review) is half-implemented (post-call-analyzer staging side done, pipeline-manager surfacing side not yet wired).
4. **Project Drone CIM review** — sits at Financials Received since 5/26; Kay's Slide-36 question to Carlos sent 5/26 19:44 still has no reply.
5. **Q1 investor update + thesis deck** — Kay's stated top priority today; thesis deck was the 12-1pm focus block.
6. **Capacity letter for broker-channel positioning** — open since 5/4 per Guillermo brief; Guillermo question seeded for this afternoon's 2pm call.
7. **Apollo / niche-intelligence Wed analyst-call decisions** — Truck Licensing & Compliance Platform ADVANCE/DROP, MGA build-vs-buy 3-rec debt, OneNote MCP install + Granola MCP headless-OAuth path — carried from 5/26 23:30 niche-intelligence run.
