---
description: Evening shutdown — carry forward unfinished tasks, inventory active threads, session decisions, decision traces, memory updates, git commit
---

# /goodnight

Close the day. Bookend `/goodmorning`. Every night Kay invokes `/goodnight`, the system:

1. Moves incomplete items from today's day tab to tomorrow's day tab without asking Kay item-by-item.
2. Inventories all active Codex threads/worktrees so evening closeout covers the full day, not only the current chat.
3. Writes `brain/context/session-decisions-{date}.md` covering the full day (merging continuation files, email threads, thread outputs, and in-session decisions).
4. Extracts decision traces to `brain/traces/{date}-{slug}.md` for any APPROVE/REJECT with non-obvious reasoning (human override, judgment call, surprising choice).
5. Updates repo memory with new feedback/project/reference/user entries whenever the day produced a durable insight.
6. Scans for stop-hook / new-skill / feedback-memory candidates (patterns repeated 3+ times this session → propose formalization). Existing-skill *improvements* are routed to Phase 2.5 skill review.
7. Commits the vault/repo changes to git.
8. Returns a concise summary to Kay (carry-forward, decisions, traces written, memory delta, commit SHA).

## Execute Now

### Step 1 — Carry forward unfinished daily tasks

Run:

```bash
python3 /home/ubuntu/projects/Sapling/scripts/task_tracker.py carry-forward-day
```

Default behavior is today's day tab → tomorrow's day tab. It moves only non-empty unchecked priority slots. Completed tasks and empty rows stay where they are. This does **not** require Kay approval; she already approved automatic daily carry-forward.

If the destination day is full, surface the refusal in the evening summary and do not force-overwrite.

### Step 2 — Gather day's signals

Collect inputs:
- Read `brain/context/continuation-{date}*.md` if a continuation file exists (mid-day resume).
- Scan the current session transcript for all APPROVE / REJECT / PASS / SENT / CREATED / UPDATED / DELETED / DRAFTED / DEFER verb tags.
- Include all Step 2A thread-inventory outcomes and any decisions/actions/artifacts from active/recent threads.
- Read `brain/context/email-scan-results-{date}.md` and `brain/context/deal-aggregator-scan-{date}.md` for day's skill outputs.
- Read prior `session-decisions-{previous-workday}.md` to confirm which deferrals triggered today and which carry forward.

### Step 2A — Multi-thread inventory (mandatory)

Before writing `session-decisions`, inventory other Codex threads so the closeout covers all work done today, not only this chat. Use Codex thread tools when available: search for `list_threads` / `read_thread` with `tool_search`, then list active/recent threads and read any thread updated today or explicitly referenced by Kay. If thread tools are unavailable, fall back to repo evidence: `git status --short`, today's `brain/context/continuation-{date}*.md`, `brain/context/verb-logs/`, and files changed/created today.

For each active/recent thread, record one of these outcomes in the session-decisions source notes:
- **Included** — decisions/actions/artifacts were incorporated into tonight's session-decisions, trace scan, memory scan, and commit plan.
- **No repo delta** — thread had discussion only, no durable artifact or task output to commit.
- **Excluded with reason** — thread is intentionally not part of tonight's closeout (for example: user asked to pause, work is blocked, separate repo/worktree, or unsafe to stage).

Do not use thread inventory to re-open decisions or ask Kay to adjudicate routine bookkeeping. If another thread produced repo changes, either commit them in the goodnight commit or explicitly list why they were left uncommitted.

### Step 3 — Write session-decisions file

Write `brain/context/session-decisions-{date}.md` with YAML frontmatter (tags inline array, required fields: date, type, title, tags) and 4 sections:

- **Decisions** — PASS/APPROVE/REJECT verb-tagged, grouped by topic (one H3 per topic cluster)
- **Actions Taken** — SENT/CREATED/UPDATED/DELETED/DRAFTED confirmations with artifact paths
- **Deferred** — items explicitly postponed, each with trigger date or condition
- **Open Loops** — unresolved items carried to next day's briefing

Wiki-link every person/company/call/output/trace referenced. Tag by person/, company/, topic/, status/ namespaces. Do NOT silently skip items — if a carried deferral is resolved today, record the resolution; if it's still open, restate it in Open Loops.

### Step 4 — Extract decision traces

For each APPROVE/REJECT in the session-decisions file, apply the litmus test:

> "Would a future agent make a different choice without knowing this?"

If YES → write a trace at `brain/traces/{date}-{slug}.md` using schema `schemas/vault/trace.yaml` (schema_version 1.1.0, tags inline array per `feedback_trace_schema_format`). Trace sections: **Trigger**, **Decision**, **Alternatives Considered**, **Reasoning**, **Why This Trace Matters**, **Key Insight**.

If NO for all decisions → write a one-line confirmation in the evening summary: "Decision traces scanned — N APPROVE/REJECT items reviewed, 0 met litmus because: [reason per category]."

**DO NOT silently skip this step.** Either produce trace files OR produce the explicit zero-trace confirmation. Silent skipping is a calibration-pipeline failure.

### Step 5 — Memory deltas

Scan the session for:
- **User memory** candidates — new facts about Kay's role/goals/preferences
- **Feedback memory** candidates — corrections ("don't do X"), confirmations ("yes that was right"), or rules
- **Project memory** candidates — in-progress work state, deadlines, stakeholder context (convert relative dates → absolute)
- **Reference memory** candidates — external system pointers

For each candidate, check `MEMORY.md` index first. Update an existing memory if the topic already has one; only create a new file if the topic is genuinely new. Keep `MEMORY.md` entries to one line under ~150 chars.

### Step 6 — Skill / hook calibration scan

Scan the session for patterns repeated ≥3 times that suggest formalization:
- Same ad-hoc task requested multiple ways → propose **new** skill
- Same correction given multiple times → propose stop hook or `feedback_*.md` memory
- Same lookup repeated → propose reference memory or skill helper

This step proposes only NEW formalizations. An **existing skill repeatedly underperforming is NOT a /goodnight concern** — that is the `evolve` skill's job (`dodo-digital/evolving-skills` plugin: it promotes a skill's `learnings.md` into durable SKILL.md / workflow / reference changes). /goodnight does not read `learnings.md` and does not edit skill files. If the session surfaced a skill that should improve, flag it as an `evolve` candidate in the summary; do not edit it here.

Surface proposals in the evening summary under "Calibration candidates." Do NOT create skills/hooks autonomously — Kay must approve.

### Step 7 — Git commit

Path is environment-dependent — use whichever is the active repo root:
- Mac: `/Users/kaycschneider/Documents/AI Operations`
- VPS: `/home/ubuntu/projects/Sapling`

```bash
git status --short
git add brain/context/session-decisions-*.md brain/traces/ brain/trackers/ memory/ .claude/skills/ .claude/commands/ .claude/hooks/ scratch/ dashboard/data/ 2>/dev/null
git status --short
```

Review the full dirty tree before staging and the staged tree after staging. Stage all repo changes from included active threads, but do **not** stage unrelated dirty files, secret/config files, or work from a thread that Step 2A marked excluded. If any changed files remain unstaged after the goodnight commit, the summary must say why.

Commit with a message in the form:

```
evening {YYYY-MM-DD}: {top-line summary} (N traces, M memory updates)

{one-line per major decision or artifact created}
```

Push only when the current repo workflow expects it and the remote is clean. During the Codex migration branch, commit is required; push is explicit or handled by the deployment/PR workflow.

### Step 8 — Summary to Kay

Return a concise summary:

```
Evening — {YYYY-MM-DD}
- Carry-forward: {N moved from Today → Tomorrow, or refusal reason}
- Thread inventory: {N included / M no repo delta / K excluded with reason}
- Decisions logged: N (X APPROVE / Y REJECT / Z PASS)
- Traces written: {list slugs} OR "0 met litmus — [reason]"
- Memory delta: {new files, updated files}
- Calibration candidates: {list, or "none"}
- Commit: {SHA short} — "{commit title}"
- Open loops carried to tomorrow: {count + 1-line summary}
```

No extra commentary. No "have a good night" unless Kay says it first.

## Behaviors

- **Don't re-ask Kay to confirm decisions already made in-session.** The session transcript IS the source of truth for what was decided. Use `feedback_never_reask_decided`.
- **Do NOT write trace files for routine briefing acknowledgments or standard pipeline moves.** The litmus is "future agent would choose differently without this." A trace for "Kay approved today's pipeline summary" is noise.
- **If Kay explicitly says "don't save X" or "that's not a trace-worthy decision," honor it.** But default to writing the trace — calibration-workflow filters noise later; it can't recover missing data.
- **If Superhuman MCP is down (token expired), suppress all draft-status claims in the summary** per `feedback_superhuman_down_suppress_drafts`.
- **If the day has no decisions worth tracing, no memory updates, and no calibration candidates,** still write the session-decisions file (even if short) and still commit-and-push. The discipline of the bookend is the point, not the volume.
- **Commit is default.** The commit must account for all included active threads, not only the current chat. Push follows the current branch/release workflow and should not be forced during migration.
- **Hook / feedback-memory updates within /goodnight scope — but NOT skill edits.** Step 5's calibration scan is not just *propose* for the items `evolve` does not cover: if a **stop hook** or **`feedback_*.md` memory** has been surfaced and confirmed by Kay within the session, apply it before commit and let it ride the evening commit. **Skill-file edits do NOT happen in /goodnight** — skill improvement is owned by the `evolve` skill (learnings.md → durable changes), which runs on its own cadence/on-demand. Surface a confirmed skill-improvement as an `evolve` candidate in the summary instead of editing the skill here. (Trimmed 2026-05-17: nightly ad-hoc skill editing was redundant with `evolve` per Harrison's Evolving Skills framework.)

## Variables

- `{date}` = today's date (YYYY-MM-DD)
- `{previous-workday}` = last weekday before today
- `{slug}` = kebab-case topic descriptor for trace filenames
