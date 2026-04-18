---
description: Mid-day save — write continuation file for later session resume
---

# /savestate

Mid-day bookend. When the connection is getting thin or Kay needs to step away mid-task, `/savestate` captures everything needed for a clean resume.

## Execute Now

### Step 1 — Determine filename

```
brain/context/continuation-{date}-{N}.md
```

Where `{N}` is the next integer for today (first save today = 1, second = 2, etc.). Glob `continuation-{date}-*.md` to find the highest existing N and increment.

### Step 2 — Scan session for content

Walk the current conversation and extract:

- **Active threads** — work in-flight, not yet resolved. Each gets a short paragraph: name, state, what's pending, who's waiting on whom.
- **Decisions made this session** — PASS/APPROVE/REJECT verb-tagged, one line each with the *why*. Do NOT include routine acknowledgments.
- **Next steps** — numbered, ordered by priority. Each step names an owner (Kay / Claude / JJ / system) and a trigger date if applicable.
- **Open questions** — things waiting on Kay's decision. One line each, explicit about what's needed.

### Step 3 — Write file

Use this frontmatter exactly:

```yaml
---
date: {YYYY-MM-DD}
type: context
title: "Continuation — {YYYY-MM-DD} #{N}"
saved_at: {ISO-8601 UTC timestamp}
session_number: {N}
tags: ["date/{YYYY-MM-DD}", "context", "topic/continuation"]
---
```

Body sections in this order:
1. `## Active Threads`
2. `## Decisions Made This Session`
3. `## Next Steps`
4. `## Open Questions`

### Step 4 — Summary to Kay

Return 3-4 lines:
```
Saved state — continuation #{N} for {date}
- Active threads: {count} ({1-line headline})
- Open questions: {count}
- Next session opens with /pickingback or natural-language "picking back up"
```

No commit unless explicitly requested. `/savestate` is a session-local checkpoint, not an end-of-day bookend.

## Behaviors

- **Do NOT run the full evening workflow** (no traces, no memory updates, no commit). That's `/goodnight`.
- **Do NOT re-surface items already in session-decisions files** — the continuation file is scoped to THIS session.
- **Preserve drafts in-flight.** If Kay has an email/Slack/DM draft half-composed, include the current version verbatim under Active Threads so the resume can pick it up mid-sentence.
- **If `/savestate` is invoked with the `--commit` flag**, git-add the continuation file and commit with message `save state: continuation {date} #{N}`. Otherwise leave uncommitted.
- **Never push to remote** — `/savestate` is always local-only.
