You are running the post-call-analyzer skill in headless mode. A detector (server-side `post_call_analyzer_mcp_poll.py` OR legacy iMac `post_call_analyzer_poll.py`) has dropped one or more queue files at `brain/trackers/post-call-analyzer/queue/{meeting_id}.json`. Your job is to drain the queue and process every entry.

DO NOT ask clarifying questions. DO NOT propose follow-up work. Make decisions and execute. Failure to produce artifacts is the top failure mode for this skill.

## Pre-flight reads (mandatory)

1. `.claude/skills/post-call-analyzer/SKILL.md` — full skill spec including the 5-bucket routing table
2. `CLAUDE.md` — vault writing rules + pre-flight checklists
3. `schemas/vault/call.yaml` — the call note schema you must match
4. `schemas/vault/research-prompt.yaml` — research-prompt schema (Thought Analysis bucket)
5. `schemas/vault/socrates-question.yaml` — socrates-question schema (Thought Analysis bucket)
6. `brain/trackers/post-call-analyzer/processed.json` — current ledger

## Per-queued-meeting workflow

Run `ls brain/trackers/post-call-analyzer/queue/*.json 2>/dev/null` (excluding `.gitkeep`). For each queue file, read it to get `meeting_id` (top-level `id` field) and the `detector` flag (`mcp` or absent/`watchpaths`).

### Step 1 — Read full transcript

**If `detector == "mcp"` (server path, default in Phase 4+):**

Call `mcp__granola__get_meeting_transcript({meeting_id})` to get the full transcript. Pull the meeting metadata from the queue file directly (title, attendees, ended_at, duration). The MCP response gives you the transcript turns; concatenate them into a single string for analysis.

**If `detector` is absent or `"watchpaths"` (legacy iMac sidecar, shadow mode):**

Read from the local Granola cache. The queue file's `id` field is the local doc_id. Use this Python helper:

```bash
python3 -c "
import json, sys, os
DOC_ID = '${DOC_ID}'
CACHE = os.path.expanduser('~/Library/Application Support/Granola/cache-v6.json')
with open(CACHE) as f:
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
}, indent=2, default=str))
"
```

If this Python path errors because the cache file isn't on the host (server-side, no Granola installed) → fall back to the MCP path: call `mcp__granola__get_meeting_transcript({queue_file.id})` instead. The cloud transcript is authoritative.

If status `NOT_FOUND` (or MCP returns empty) → mark queue entry `processing_failed: true` with reason `transcript_unavailable`, archive to `processed/`, and continue to next.

### Step 2 — Resolve attendees

For each person in the meeting metadata (excluding Kay):
1. Slugify the name (`firstname-lastname` lowercase, ASCII)
2. Check `brain/entities/{slug}.md` exists
3. If missing → create a minimal entity stub per `schemas/vault/entity.yaml` (frontmatter only — name, email if available, type: person, schema_version: 1.1.0; body: one-line "(stub created by post-call-analyzer from Granola call {call_date})")

Don't fabricate emails or roles. Leave fields blank when unknown.

### Step 3 — Write vault call note

Path: `brain/calls/{YYYY-MM-DD}-{call-slug}.md` where call-slug derives from the Granola title (lowercase, hyphens, ≤60 chars). If file at that path already exists, append `-2` / `-3`.

**Frontmatter MUST follow `schemas/vault/call.yaml`.** Verify by reading the schema example block first. Required fields typically include: date, type: call, title, attendees (people wiki-links), tags (date/, call literal, person/* per attendee), schema_version: 1.1.0.

**Body sections:**
- `## Summary` — copy MCP/Granola overview if present, else first 3 paragraphs of transcript
- `## Key points` — 3-7 bullets distilled from the transcript
- `## Action items` — every concrete next-step (one bullet each, verb-first, owner in brackets)
- `## Decisions captured` — bilateral conclusions only (not action items)
- `## Source` — `Granola meeting {meeting_id}`, link to calendar event if present

### Step 4 — Classify and route into FIVE buckets

For every signal you extract from the transcript, classify into ONE of:

**A. Task** — one-off action, single step, completable in <2 hours.
Route: write `brain/trackers/post-call-analyzer/task_queue/{meeting_id}-{seq}.json` with shape:
```json
{
  "summary": "verb-first task summary",
  "type": "Work",
  "project": "G&B (or call context)",
  "due_date": "YYYY-MM-DD or null",
  "notes": "From {call title} {call date}",
  "source_call": "brain/calls/{date}-{slug}.md",
  "source_meeting_id": "{meeting_id}",
  "queued_at": "ISO 8601 with timezone"
}
```
Phase 4.5 will drain this dir into the iMac Excel tracker. For now, just queue.

**B. Project** — multi-week initiative spanning multiple work streams.
Route: NO file write. Add to Slack message under `PROJECT (needs Kay scope):` line. Examples: "build out a server", "stand up the X program", "launch the Y partnership."

**C. Email follow-up** — next step is "send X to Y" / "follow up with Z" / "intro Z to W."
Route: create Gmail draft via `gog gmail drafts create --to "{email}" --subject "{subject}" --body "{body}" --gmail-no-send` (note: `drafts` plural, v0.15+ syntax). Body MUST be:
- Plain text (no `>` blockquote, no code fence per `feedback_drafts_no_blockquote`)
- No em dashes per `feedback_email_no_em_dashes`
- Polite, brief, references the call
- Includes whatever the call said Kay would send

NEVER send. The `--gmail-no-send` flag is defense-in-depth; the `drafts create` subcommand only creates a draft anyway. If recipient email is unknown → demote to TASK with note "verify email then send."

If an item is both task AND email (e.g., "I'll send the spec to Sam"), prefer email-draft route — the draft is the artifact.

**D. Decision** — bilateral conclusion ("we decided," "we're going to," "the call is").
Route:
1. Check if `brain/context/session-decisions-{YYYY-MM-DD}.md` exists for today
2. If not → create stub with proper frontmatter (look at the most recent existing session-decisions file for shape)
3. Append section `## Auto-extracted from {call slug}` with bullet list of decisions

**E. Thought Analysis** (NEW in Phase 4) — questions surfaced during the call that need follow-up beyond a task.

Apply this heuristic FIRST to every potential thought-analysis signal:

| Cue | Routes to |
|---|---|
| Numerical answer would resolve it ("what's the TAM," "how many," "what multiple") | research-prompt |
| Lookupable fact ("I should check," "do we know," "let me look that up") | research-prompt |
| Direction-setting ("should we," "is this the right," "are we optimizing for") | socrates-question |
| Identity / scope frame ("are we still a holding company," "do we even do this size") | socrates-question |
| Stress-test of an assumption ("but what if," "the assumption there is") | socrates-question |

If both apply, prefer **socrates-question** — strategic frames are higher-leverage.

**Research prompt route:** Write `brain/inbox/{YYYY-MM-DD}-{slug}-research-prompt.md` per `schemas/vault/research-prompt.yaml`. Required frontmatter:
- `schema_version: 1.0.0`
- `date: {call date}`
- `type: inbox`
- `source_call: "[[calls/{date}-{slug}]]"`
- `source_meeting_id: "{meeting_id}"`
- `question: "{full sentence question}"`
- `urgency: high|normal|low (default normal; high if Kay or counterparty flagged time-pressure)`
- `target_skill: niche-intelligence | list-builder | target-discovery | warm-intro-finder | unassigned`
- `tags: [date/{date}, inbox, source/call, type/research-prompt, person/{slug per attendee}, urgency/{level}]`

Body sections: `## Question` (restate with full context), `## Why it matters`, `## How to answer`, `## Answer` (leave as `*Pending*`).

**Socrates question route:** Write `brain/inbox/{YYYY-MM-DD}-{slug}-socrates-question.md` per `schemas/vault/socrates-question.yaml`. Required frontmatter:
- `schema_version: 1.0.0`
- `date: {call date}`
- `type: inbox`
- `source_call: "[[calls/{date}-{slug}]]"`
- `source_meeting_id: "{meeting_id}"`
- `question: "{strategic question, framed as a question}"`
- `frame: strategic | identity | scope | timing`
- `urgency: high|normal|low`
- `surfaced_by: "[[entities/{slug of person who raised it}]]"` if not Kay
- `tags: [date/{date}, inbox, source/call, type/socrates-question, frame/{frame}, person/{slug per attendee}, urgency/{level}]`

Body sections: `## Question` (full context), `## Assumptions to surface`, `## Alternatives in scope`, `## Resolution` (leave as `*Pending — needs /socrates session before any plan*`).

### Step 5 — Post Slack message

ONE message per call. Use this exact format:

```
[Granola] {Call Title} — {duration if available, else 'duration unknown'} — {N attendees}
{vault note path: brain/calls/...}

Action items:
- TASK: {summary} → task_queue
- DRAFT: {to recipient}: {subject} → Gmail drafts
- PROJECT (needs Kay scope): {project name}

Decisions:
- {decision 1}
- {decision 2}

Thought analysis:
- RESEARCH: {question} → brain/inbox/{file}
- SOCRATES: {question} → brain/inbox/{file}
```

If a section is empty:
- Action items section: omit
- Decisions section: write `(no decisions captured)`
- Thought analysis section: write `(no thought analysis)`

If no extractables at all, post: `[Granola] {Call Title} — no action items extracted` so Kay knows the analyzer ran.

Send via:
```bash
MESSAGE_FILE=$(mktemp)
cat > "$MESSAGE_FILE" <<'EOF'
{your message text here}
EOF
curl -s -X POST "$SLACK_WEBHOOK_OPERATIONS" \
  -H 'Content-type: application/json' \
  --data-binary @<(jq -nc --arg t "$(cat $MESSAGE_FILE)" '{text: $t}')
rm "$MESSAGE_FILE"
```

### Step 6 — Archive queue entry

Write `brain/trackers/post-call-analyzer/processed/{meeting_id}.json` with archival metadata:

```json
{
  "meeting_id": "...",
  "title": "...",
  "processed_at": "ISO8601 with timezone",
  "vault_call_note": "brain/calls/2026-05-08-foo.md",
  "tasks_queued": ["task_queue/{meeting_id}-1.json", "..."],
  "drafts_created": [{"to": "...", "subject": "..."}],
  "projects_flagged": ["..."],
  "decisions_extracted": ["..."],
  "research_prompts_created": ["brain/inbox/2026-05-08-foo-research-prompt.md", "..."],
  "socrates_questions_created": ["brain/inbox/2026-05-08-foo-socrates-question.md", "..."],
  "slack_posted": true,
  "processing_failed": false,
  "detector": "mcp"
}
```

**Critical:** include `research_prompts_created` and `socrates_questions_created` arrays — the validator checks these named files exist on disk and will fail the run if any path is fabricated.

Then remove the queue file:
```bash
rm "brain/trackers/post-call-analyzer/queue/${MEETING_ID}.json"
```

### Step 7 — Update processed.json ledger

Read `brain/trackers/post-call-analyzer/processed.json`, add the new entry:

```json
{
  "{meeting_id}": {
    "title": "...",
    "processed_at": "...",
    "vault_call_note": "...",
    "detector": "mcp"
  }
}
```

Write atomically (write to `processed.json.tmp`, then `mv`).

## Hard constraints

- **NEVER send any email.** Drafts only. Use `gog gmail drafts create` (plural `drafts`, v0.15+) with `--gmail-no-send` for defense-in-depth. If the flag is unfamiliar, run `gog gmail drafts create --help` and use the documented form. Do not invent flags.
- **Never re-send Slack on retry.** If `slack_posted: true` already in archive, skip.
- **Do not modify Attio.** That's pipeline-manager's surface.
- **Do not auto-drain task_queue/.** That's Phase 4.5 — just write the queue files.
- **Do not auto-answer research-prompts or run socrates sessions.** Surface the artifact; Kay or the named target_skill picks it up via `/triage`.
- **Do not write to `brain/inbox/`** for plain action items — those go to `task_queue/`. Only thought-analysis artifacts land in inbox.
- **No em dashes in any draft body.**
- **Plain text drafts.** No `>` blockquote, no code fence.
- **Wiki-link every entity** referenced in any vault file. Tags must include `person/{slug}` for every attendee.

## Final report

After processing all queued meetings, output a short summary:

```
post-call-analyzer run complete
- processed: N meetings
- vault notes written: N
- tasks queued: N
- drafts created: N
- projects flagged: N
- decisions captured: N
- research prompts written: N
- socrates questions written: N
- slack messages posted: N
- failures: N (if any: list meeting_ids + reasons)
```

That's it. Do not ask questions. Do not propose follow-up work. The validator will check your artifacts.
