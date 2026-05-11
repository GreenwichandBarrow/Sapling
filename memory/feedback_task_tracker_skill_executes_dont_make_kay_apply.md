---
name: task-tracker-manager skill executes — don't make Kay manually apply
description: 2026-05-11 correction. When Kay makes decisions on her personal task tracker (drop / promote / append / archive / done items), the task-tracker-manager skill is the executor — invoke it. Do NOT tell Kay "you'll apply this in Excel when you reopen" as the default move. That's making her do the skill's job.
type: feedback
---

When Kay makes decisions about her personal task tracker (`TO DO M.DD.YY.xlsx` in Drive at `STRATEGIC PLANNING/`):
- DROP / DONE / PROMOTE / APPEND / ARCHIVE / GANTT-TICK / REPORT decisions

**Invoke the `task-tracker-manager` skill to execute them.** Do NOT default to "you'll apply this in Excel when you reopen" — that makes Kay do the skill's job.

**The skill exists specifically to mutate the file** via `scripts/task_tracker.py`:
- `append` — add to To Do
- `promote` — move to specific day's priority slot
- `archive` — Sunday rollover (rename tab, clear slots, archive old)
- `reformat` — fix formatting drift
- `report` — health summary
- `gantt-tick` — milestone completion

**The VPS execution path** (when Mac Excel is closed and Drive sync is current):
1. Download xlsx from Drive via `gog drive download` to `/tmp/todo.xlsx`
2. Set `TASKS_XLSX_LIVE=/tmp/todo.xlsx` env var (per the subagent path fix from 2026-05-11)
3. Run `python3 scripts/task_tracker.py {verb} ...` against the /tmp copy
4. Upload back to Drive via `gog drive upload` (overwriting the original file ID)
5. Kay reopens Excel and gets the updated version

**The script doesn't have a built-in upload-back step** — wrap the invocation in a shell script that handles download + run + upload + cleanup. Worth adding as `scripts/task_tracker_remote.sh` or similar wrapper so the VPS path is one command.

**Drive sync safety:** only run this when Excel is closed on Mac (lock-file absent). Per existing skill guardrails: lsof check on local Mac path; for VPS execution, check Drive's lock-file presence (`~$TO DO M.DD.YY.xlsx`) before downloading + writing.

**When manual application is acceptable:**
- Mac Excel currently has the file open (lock-file present) — must wait or ask Kay to close
- Drive sync is stale (modified-time gap > 24h between Drive copy and Mac local) — risk of conflict
- A specific decision is highly contextual and benefits from Kay touching it directly (rare)

**Default behavior change:** assume invocation, fall back to manual only when a guardrail blocks. Reverse of the prior default.

**Source:** 2026-05-11 mid-day Kay correction during weekly-planning triage. I had been logging decisions in conversation only and telling Kay to apply them manually when she reopened Excel. She challenged: "we have a task manager skill that is responsible for keeping this file updated. why are you telling me I have to make these changes? This is what the skill is for..." Fair — the skill should have been firing per-decision.

**Related memories:**
- `project_personal_task_tracker.md` — full architecture + script path
- `feedback_default_to_now_not_later.md` — do-it-now bias applies here too
- `feedback_decision_fatigue_minimization.md` — Kay's energy is for decisions, not mechanical application
