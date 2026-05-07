You are running the post-call-analyzer skill in headless mode. The poller has detected one or more new Granola transcripts and dropped trigger files into `brain/trackers/post-call-analyzer/queue/`. Your job is to drain the queue and process every entry.

DO NOT ask clarifying questions. Make decisions and execute. Failure to produce artifacts is the top failure mode for this skill.

## Pre-flight reads (mandatory)

1. `.claude/skills/post-call-analyzer/SKILL.md` — full skill spec
2. `CLAUDE.md` — vault writing rules + pre-flight checklists
3. `schemas/vault/call.yaml` — the call note schema you must match
4. `brain/trackers/post-call-analyzer/processed.json` — current ledger

## Per-queued-doc workflow

Run `ls brain/trackers/post-call-analyzer/queue/*.json 2>/dev/null` (excluding `.gitkeep`). For each queue file:

### Step 1 — Read full Granola doc + extract content

Granola stores content in multiple places that populate at different times after a meeting ends:
- `notes_plain` — flat text (often empty for fresh meetings; populates after server-side summarization)
- `notes_markdown` — markdown form (similar lag)
- `notes.content` — rich ProseMirror JSON tree (Kay's hand-typed notes, present immediately)
- `transcripts.{doc_id}` — list of transcript turns with `text` field (populates if user enabled transcription)

Use the helper below — it walks all four sources and returns the richest available text. Read the queue file to get `doc_id`, then:

```bash
python3 -c "
import json, sys
DOC_ID = '${DOC_ID}'
with open('/Users/kaycschneider/Library/Application Support/Granola/cache-v6.json') as f:
    cache = json.load(f)
state = cache['cache']['state']
doc = state['documents'].get(DOC_ID)
if not doc:
    print(json.dumps({'status': 'NOT_FOUND'}))
    sys.exit(0)

def flatten_prosemirror(node):
    parts = []
    if isinstance(node, dict):
        if node.get('text'):
            parts.append(node['text'])
        for child in node.get('content', []) or []:
            parts.extend(flatten_prosemirror(child))
    elif isinstance(node, list):
        for child in node:
            parts.extend(flatten_prosemirror(child))
    return parts

notes_text = '\n'.join(flatten_prosemirror(doc.get('notes') or {}))
transcript = state.get('transcripts', {}).get(DOC_ID) or []
transcript_text = '\n'.join(t.get('text','') for t in transcript if isinstance(t, dict))

# Pick richest source
sources = {
    'notes_plain': doc.get('notes_plain') or '',
    'notes_markdown': doc.get('notes_markdown') or '',
    'notes_tree': notes_text,
    'transcript': transcript_text,
}
best = max(sources.items(), key=lambda kv: len(kv[1].strip()))

print(json.dumps({
    'status': 'OK',
    'id': doc['id'],
    'title': doc.get('title'),
    'created_at': doc.get('created_at'),
    'updated_at': doc.get('updated_at'),
    'people': doc.get('people') or [],
    'google_calendar_event': doc.get('google_calendar_event'),
    'overview': doc.get('overview', ''),
    'meeting_end_count': doc.get('meeting_end_count', 0),
    'content_source': best[0],
    'content': best[1],
    'all_source_lengths': {k: len(v.strip()) for k, v in sources.items()},
}, indent=2, default=str))
"
```

If `status: NOT_FOUND` → mark queue entry as `processing_failed: true` with reason `doc_not_in_cache`, archive to processed/, and continue to next.

If the chosen `content` is shorter than 100 chars → defer this doc by leaving the queue entry in place and moving on (the next poll picks it up after Granola finishes summarization). Log: `defer {doc_id[:8]}: content not yet populated`.

### Step 2 — Resolve attendees

For each person in `people` (excluding Kay):
1. Slugify the name (`firstname-lastname` lowercase)
2. Check `brain/entities/{slug}.md` exists
3. If missing → create a minimal entity stub per `schemas/vault/entity.yaml` with frontmatter only (name, email if available, type: person, schema_version: 1.1.0). Body: one-line "(stub created by post-call-analyzer from Granola call {call_date})"

Don't fabricate emails or roles. If the Granola `people` array doesn't have an email for a person, leave the email field blank.

### Step 3 — Write vault call note

Path: `brain/calls/{YYYY-MM-DD}-{call-slug}.md` where call-slug is derived from the Granola title (lowercase, hyphens, ≤60 chars). If a file at that exact path already exists, append `-2` / `-3` etc.

**Frontmatter MUST follow `schemas/vault/call.yaml`.** Verify by reading the schema example block first. Required fields typically include: date, type: call, title, attendees (people wiki-links), tags (date/, call literal, person/* per attendee), schema_version: 1.1.0.

**Body sections:**
- `## Summary` — copy Granola's `overview` if present, else first 3 paragraphs of `notes_plain`
- `## Key points` — 3-7 bullets distilled from `notes_plain`
- `## Action items` — every concrete next-step (one bullet each, verb-first, owner in brackets)
- `## Decisions captured` — bilateral conclusions only (not action items)
- `## Source` — `Granola doc {doc_id}`, link to calendar event if present

### Step 4 — Classify and route action items

For every action item identified, classify into ONE of:

**A. Task** — one-off action, single step, completable in <2 hours of work.
Route: `python3 scripts/task_tracker.py append --task "{verb-first summary}" --type Work --project "{call context project, e.g. G&B}" --due "{date if mentioned else blank}" --notes "From {call title} {call date}"`

**B. Project** — multi-week initiative spanning multiple work streams.
Route: do NOT auto-create. Add to Slack message under "PROJECTS NEEDING SCOPE" — Kay decides. Examples: "build out a server", "stand up the X program", "launch the Y partnership."

**C. Email follow-up** — next step is "send X to Y" / "follow up with Z" / "intro Z to W."
Route: create Gmail draft via `gog gmail draft --to "{email}" --subject "{subject}" --body "{body}"`. Body should be polite, brief, plain-text (no em dashes per `feedback_email_no_em_dashes`), reference the call, and include whatever the original call said Kay would send. NEVER send. If recipient email is unknown, demote to TASK with note "verify email then send."

If an item is both task AND email (e.g., "I'll send the spec to Sam"), prefer the email-draft route — the draft itself is the artifact.

### Step 5 — Append decisions to session-decisions

If the call had any "we decided" / "the call is" bilateral decisions:

1. Check if `brain/context/session-decisions-{YYYY-MM-DD}.md` exists for today
2. If not → create stub with proper frontmatter per `schemas/vault/output.yaml` or session-decisions convention (look at last existing session-decisions file for shape)
3. Append section `## Auto-extracted from {call slug}` with bullet list of decisions

### Step 6 — Post Slack message

ONE message per call. Use this exact format:

```
[Granola] {Call Title} — {duration if available, else 'duration unknown'} — {N attendees}
{vault note path: brain/calls/...}

Action items:
- TASK: {summary} → Excel To Do
- DRAFT: {to recipient}: {subject} → Gmail drafts
- PROJECT (needs Kay scope): {project name}

Decisions:
- {decision 1}
- {decision 2}

(no decisions captured) ← if list empty
```

If no items extracted at all, still post: `[Granola] {Call Title} — no action items extracted` so Kay knows the analyzer ran.

Send via:
```bash
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H 'Content-type: application/json' \
  --data-binary @<(jq -nc --arg t "$MESSAGE" '{text: $t}')
```

Or write the message text to a temp file first to avoid quoting hell.

### Step 7 — Archive queue entry

Move queue file to processed/. Add archival metadata:

```json
{
  "doc_id": "...",
  "title": "...",
  "processed_at": "ISO8601 with timezone",
  "vault_call_note": "brain/calls/2026-05-07-foo.md",
  "tasks_created": ["task description 1", "..."],
  "drafts_created": [{"to": "...", "subject": "..."}],
  "projects_flagged": ["..."],
  "decisions_extracted": ["..."],
  "slack_posted": true,
  "processing_failed": false
}
```

```bash
mv "brain/trackers/post-call-analyzer/queue/${DOC_ID}.json" \
   "brain/trackers/post-call-analyzer/processed/${DOC_ID}.json"
```

(But you'll be writing the new content — so use `cat > processed/{id}.json` with the archival JSON, then `rm queue/{id}.json`.)

### Step 8 — Update processed.json ledger

Read `brain/trackers/post-call-analyzer/processed.json`, add the new entry:

```json
{
  "{doc_id}": {
    "title": "...",
    "processed_at": "...",
    "vault_call_note": "..."
  }
}
```

Write atomically.

## Hard constraints

- **NEVER send any email.** Drafts only. If `gog gmail draft` flag is unfamiliar, run `gog gmail draft --help` and use the documented form. Do not invent flags.
- **Never re-send Slack on retry.** If `slack_posted: true` already in archive, skip.
- **Do not modify Attio.** That's pipeline-manager's surface.
- **Do not create Excel project tabs.** Project flag in Slack only.
- **Do not write to `brain/inbox/`.** Action items go to Excel, not inbox.
- **No em dashes in any draft body.**
- **Plain text drafts.** No `>` blockquote, no code fence (per `feedback_drafts_no_blockquote.md`).

## Final report

After processing all queued docs, output a short summary:

```
post-call-analyzer run complete
- processed: N docs
- vault notes written: N
- tasks appended: N
- drafts created: N
- projects flagged: N
- decisions captured: N
- slack messages posted: N
- failures: N (if any: list doc_ids + reasons)
```

That's it. Do not ask questions. Do not propose follow-up work. The validator will check your artifacts.
