---
description: Evening shutdown — session decisions, decision traces, memory updates, git commit
---

# /goodnight

Close the day. Bookend `/start`. Every night Kay invokes `/goodnight`, the system:

1. Writes `brain/context/session-decisions-{date}.md` covering the full day (merging continuation files, email threads, and in-session decisions).
2. Extracts decision traces to `brain/traces/{date}-{slug}.md` for any APPROVE/REJECT with non-obvious reasoning (human override, judgment call, surprising choice).
3. Updates memory (`/Users/kaycschneider/.claude/projects/-Users-kaycschneider-Documents-AI-Operations/memory/`) with new feedback/project/reference/user entries whenever the day produced a durable insight.
4. Scans for stop-hook or skill update candidates (patterns repeated 3+ times this session → propose formalization).
5. Commits the vault changes to git with a concise message.
6. Returns a 4-6 line summary to Kay (decisions, traces written, memory delta, commit SHA).

## Execute Now

### Step 1 — Gather day's signals

Collect inputs:
- Read `brain/context/continuation-{date}*.md` if a continuation file exists (mid-day resume).
- Scan the current session transcript for all APPROVE / REJECT / PASS / SENT / CREATED / UPDATED / DELETED / DRAFTED / DEFER verb tags.
- Read `brain/context/email-scan-results-{date}.md` and `brain/context/deal-aggregator-scan-{date}.md` for day's skill outputs.
- Read prior `session-decisions-{previous-workday}.md` to confirm which deferrals triggered today and which carry forward.

### Step 2 — Write session-decisions file

Write `brain/context/session-decisions-{date}.md` with YAML frontmatter (tags inline array, required fields: date, type, title, tags) and 4 sections:

- **Decisions** — PASS/APPROVE/REJECT verb-tagged, grouped by topic (one H3 per topic cluster)
- **Actions Taken** — SENT/CREATED/UPDATED/DELETED/DRAFTED confirmations with artifact paths
- **Deferred** — items explicitly postponed, each with trigger date or condition
- **Open Loops** — unresolved items carried to next day's briefing

Wiki-link every person/company/call/output/trace referenced. Tag by person/, company/, topic/, status/ namespaces. Do NOT silently skip items — if a carried deferral is resolved today, record the resolution; if it's still open, restate it in Open Loops.

### Step 3 — Extract decision traces

For each APPROVE/REJECT in the session-decisions file, apply the litmus test:

> "Would a future agent make a different choice without knowing this?"

If YES → write a trace at `brain/traces/{date}-{slug}.md` using schema `schemas/vault/trace.yaml` (schema_version 1.1.0, tags inline array per `feedback_trace_schema_format`). Trace sections: **Trigger**, **Decision**, **Alternatives Considered**, **Reasoning**, **Why This Trace Matters**, **Key Insight**.

If NO for all decisions → write a one-line confirmation in the evening summary: "Decision traces scanned — N APPROVE/REJECT items reviewed, 0 met litmus because: [reason per category]."

**DO NOT silently skip this step.** Either produce trace files OR produce the explicit zero-trace confirmation. Silent skipping is a calibration-pipeline failure.

### Step 4 — Memory deltas

Scan the session for:
- **User memory** candidates — new facts about Kay's role/goals/preferences
- **Feedback memory** candidates — corrections ("don't do X"), confirmations ("yes that was right"), or rules
- **Project memory** candidates — in-progress work state, deadlines, stakeholder context (convert relative dates → absolute)
- **Reference memory** candidates — external system pointers

For each candidate, check `MEMORY.md` index first. Update an existing memory if the topic already has one; only create a new file if the topic is genuinely new. Keep `MEMORY.md` entries to one line under ~150 chars.

### Step 5 — Skill / hook calibration scan

Scan the session for patterns repeated ≥3 times that suggest formalization:
- Same ad-hoc task requested multiple ways → propose new skill
- Same correction given multiple times → propose stop hook or `feedback_*.md` memory
- Same lookup repeated → propose reference memory or skill helper

Surface proposals in the evening summary under "Calibration candidates." Do NOT create skills/hooks autonomously — Kay must approve.

### Step 6 — Git commit

```bash
cd "/Users/kaycschneider/Documents/AI Operations"
git add brain/context/session-decisions-*.md brain/traces/ .claude/skills/ .claude/commands/ .claude/hooks/ 2>/dev/null
git status --short
```

Review staged files. Commit with a message in the form:

```
evening {YYYY-MM-DD}: {top-line summary} (N traces, M memory updates)

{one-line per major decision or artifact created}
```

Do NOT push to remote automatically — Kay approves pushes separately via `/push` or by explicit request. Exception: if the `/goodnight` invocation included `--push` argument, push after commit.

### Step 7 — Summary to Kay

Return 4-6 lines:

```
Evening — {YYYY-MM-DD}
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
- **If the day has no decisions worth tracing, no memory updates, and no calibration candidates,** still write the session-decisions file (even if short) and still commit. The discipline of the bookend is the point, not the volume.
- **Never push to remote without explicit approval** except when `--push` flag passed.

## Variables

- `{date}` = today's date (YYYY-MM-DD)
- `{previous-workday}` = last weekday before today
- `{slug}` = kebab-case topic descriptor for trace filenames
