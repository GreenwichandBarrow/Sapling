You are running the `post-call-analyzer` skill in headless mode. The detector (`scripts/post_call_analyzer_poll.codex.sh`) has dropped one or more queue files at `brain/trackers/post-call-analyzer/queue/{note_id}.json`. Your job is to drain the queue and process every entry end-to-end.

**DO NOT ask clarifying questions. DO NOT propose follow-up work. Make decisions and execute. The top failure mode is producing zero artifacts.**

## Architecture summary (read SKILL.md for full detail)

- Credential path: `op://GB Server/Granola API Key/password` → `~/.local/bin/granola-api`
- No MCP, no OAuth, no reconnect anywhere
- All writes are: saved transcript Google Doc (RESEARCH/MEETINGS) + analysis Google Doc (RESEARCH/MEETINGS) + Attio notes (person+company) + staged task JSON for Good Morning approval + Slack (#ai-operations) + vault call note
- Never send email and never write directly to the TO DO sheet from this skill

## Pre-flight reads (mandatory)

1. `.agents/skills/post-call-analyzer/SKILL.md` — full skill spec including Slack format + failure invariants
2. `AGENTS.md` — vault writing rules + pre-flight checklists (especially "Before writing a brain/ vault file" + "Before handling secrets / config")
3. `schemas/vault/call.yaml` — the call note schema you must match
4. `brain/trackers/post-call-analyzer/processed.json` — current ledger

## Bootstrap credentials

```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
export GRANOLA_KEY="$(op read 'op://GB Server/Granola API Key/password')"
export ATTIO_KEY="$(op read 'op://GB Server/Attio API Key/password')"
```

If `op-env.sh` or either required secret fails, stop and leave queue files in place for retry. Do not fall back to raw local env files.

Granola transcript access is expected through this 1Password-backed REST path.
Do not use Granola MCP, OAuth, or local browser auth. The known historical
failure mode was Claude Code concluding transcript access was unavailable after
forgetting the 1Password wrapper. If `granola-api get-note` returns a note but
you cannot find transcript content, log the returned top-level keys and leave
the queue file in place for retry unless the response clearly proves there is no
transcript.

## Per-queued-note workflow

Run `ls brain/trackers/post-call-analyzer/queue/*.json 2>/dev/null | grep -v gitkeep`. For each queue file:

### Step 1 — Pull full note

```bash
granola-api get-note <note_id> > /tmp/{note_id}.json
```

Parse: `id`, `title`, `created_at`, `updated_at`, `web_url`, `owner`, `attendees`, `calendar_event`, `summary_markdown`, `transcript`.

If `transcript` is missing, inspect adjacent fields before failing:
`transcript_markdown`, `transcript_plain`, `notes_markdown`, `notes_plain`,
`summary_markdown`, and any nested transcript arrays. Save the best available
verbatim transcript-like content. If only summary text exists, save it clearly
as "Granola summary only; full transcript unavailable in response" and keep a
`transcript_failed: true` marker in the processed ledger.

### Step 2 — Save transcript Google Doc

Create `/tmp/{note_id}-transcript.md` from the Granola note. Include:

- Call title
- Date/time
- Attendees
- Granola source URL
- Granola summary, if present
- Full transcript, speaker-labelled if available

Then save it to Drive:

```bash
TRANSCRIPT_RESULT=$(gog docs create "{date} — {counterparty-shortname} — Granola Transcript" \
  --parent=1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz \
  --file=/tmp/{note_id}-transcript.md \
  --account=kay.s@greenwichandbarrow.com \
  --json)
TRANSCRIPT_DOC_ID=$(echo "$TRANSCRIPT_RESULT" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")
TRANSCRIPT_DOC_URL="https://docs.google.com/document/d/$TRANSCRIPT_DOC_ID/edit"
```

Folder ID `1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz` = `RESEARCH/MEETINGS`.

### Step 3 — Match attendees to Attio

For each non-Kay attendee email:
```bash
curl -s -X POST -H "Authorization: Bearer $ATTIO_KEY" -H "Content-Type: application/json" \
  -d "{\"filter\": {\"email_addresses\": {\"email_address\": \"{email}\"}}, \"limit\": 3}" \
  https://api.attio.com/v2/objects/people/records/query
```

For each unique counterparty domain (from email after `@`):
```bash
curl -s -X POST -H "Authorization: Bearer $ATTIO_KEY" -H "Content-Type: application/json" \
  -d "{\"filter\": {\"domains\": {\"domain\": \"{domain}\"}}, \"limit\": 3}" \
  https://api.attio.com/v2/objects/companies/records/query
```

Capture `record_id` for each match. If no match for a person, skip (do NOT auto-create — pipeline-manager owns Attio person creation).

### Step 4 — Compose the analysis

Anchor on the saved transcript and `summary_markdown` (Granola has already extracted the meeting structure). Layer on the THINKING analysis:

1. **Meeting Overview** (1 paragraph)
2. **Acquisition / Search Takeaways** — 3-5 bullets. What does this tell us about thesis/niche/buyer pool/broker channel/specific deal? Cross-reference G&B doctrine (Charter / scorecard / buy-box) where relevant.
3. **Process / Operating Takeaways** — 2-3 bullets. What does this surface about G&B's own processes (briefs, voice, tracker, drift between commitments)?
4. **For Kay + DaVinci to Discuss** — questions or judgement calls worth discussing together.
5. **Potential Action Items for Good Morning** — counterparty commitments + Kay commitments. These are candidates only; do not add them to the TO DO sheet.
6. **Open Loops / Further Analysis Needed** — bulleted, EACH with "await Kay approval before deep-dive" flag. Do NOT execute any deep-dive in this run.
7. **Tasks Staged** — short cross-reference list pointing at the pending task file for Good Morning review.

Target: ~600 words / 1-2 Word-equivalent pages. Stay tight. Write to `/tmp/{note_id}-analysis.md`.

### Step 5 — Create analysis Google Doc

```bash
DOC_RESULT=$(gog docs create "{date} — {counterparty-shortname} — Meeting Analysis" \
  --parent=1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz \
  --file=/tmp/{note_id}-analysis.md \
  --account=kay.s@greenwichandbarrow.com \
  --json)
DOC_ID=$(echo "$DOC_RESULT" | python3 -c "import json,sys; print(json.load(sys.stdin)['id'])")
DOC_URL="https://docs.google.com/document/d/$DOC_ID/edit"
```

Folder ID `1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz` = `RESEARCH/MEETINGS`. Confirmed canonical per memory `project_drive_research_folder_canonical.md`.

### Step 6 — Write Attio notes

For each matched record (person + company), write a note. Content: short summary (3-4 lines), key takeaways bullets, links to analysis Doc + saved transcript Doc + Granola source.

```bash
curl -s -X POST -H "Authorization: Bearer $ATTIO_KEY" -H "Content-Type: application/json" \
  -d '{"data": {"parent_object": "people|companies", "parent_record_id": "<id>", "title": "{date} — Meeting w/ Kay (G&B)", "content": "<markdown>", "format": "markdown"}}' \
  https://api.attio.com/v2/notes
```

### Step 7 — Stage tasks for Kay's Good Morning review

Write review-ready tasks to `brain/trackers/post-call-analyzer/pending-tasks/{note_id}.json`. Do NOT write to the TO DO sheet directly and do NOT invoke any TO DO write path.

Each staged task object must include:

```json
{
  "task_text": "Concrete task phrased for Kay",
  "type": "Follow-up | Analysis | Ops | Deal | Relationship",
  "project": "Best-fit project or blank if unclear",
  "suggested_day": "Best recommendation, not a commitment",
  "suggested_due_date": "YYYY-MM-DD or blank",
  "notes_with_doc_link": "From {counterparty} {date} mtg. Analysis: {DOC_URL}",
  "source_call_id": "{note_id}",
  "source_doc_url": "{DOC_URL}",
  "source_transcript_url": "{TRANSCRIPT_DOC_URL}",
  "staged_at": "<ISO8601>"
}
```

Good Morning/pipeline-manager surfaces these in the next morning briefing with YES/NO/DISCUSS and a recommended day. Only after Kay approves and decides timing does task-manager append to the TO DO sheet.

### Step 8 — Write vault call note

`brain/calls/{date}-{counterparty-slug}.md` per `schemas/vault/call.yaml`. Required: frontmatter with people + companies wiki-linked to `[[entities/{slug}]]`, tags including `person/{slug}` + `company/{slug}` + `date/{YYYY-MM-DD}` + `call`, schema_version 1.1.0. Body links to analysis Doc + saved transcript Doc + Granola source.

If any referenced entity doesn't exist in `brain/entities/`, create the stub per the entity schema. Do NOT leave broken wiki-links.

### Step 9 — Post Slack message

Format per SKILL.md "Slack message format" section. Post via `$SLACK_WEBHOOK_OPERATIONS`.

Before posting, build a final per-call result object containing the actual artifact URLs and failure markers that will be written to `processed.json`. The Slack message MUST be generated from that final result object, not from intermediate variables or earlier fallback state. Do not post a "failed" Slack message if the final result object has a valid `doc_url` / `transcript_doc_url`.

```python
import os, json, urllib.request
msg = {"blocks": [
  {"type": "section", "text": {"type": "mrkdwn", "text":
    f"*Post-call analysis — {counterparty} ({date} {time})*\n_{location}_\n\n{summary_2to3_lines}"
  }},
  {"type": "section", "text": {"type": "mrkdwn", "text":
    f":memo: <{doc_url}|Full analysis (Google Doc)>\n"
    f":page_facing_up: <{transcript_doc_url}|Saved transcript (Google Doc)>\n"
    f":microphone: <{granola_url}|Granola source>\n"
    f":white_check_mark: {task_count} tasks staged for Good Morning review"
  }}
]}
req = urllib.request.Request(os.environ["SLACK_WEBHOOK_OPERATIONS"], method="POST",
  headers={"Content-Type": "application/json"}, data=json.dumps(msg).encode())
urllib.request.urlopen(req)
```

### Step 10 — Move queue file → processed archive

```bash
mv brain/trackers/post-call-analyzer/queue/{note_id}.json \
   brain/trackers/post-call-analyzer/processed/{note_id}.json
```

Replace the moved archive file's contents with the final per-call result object before appending to the ledger. The per-note archive and `processed.json` ledger must agree on `id`, `doc_url`, `transcript_doc_url`, `vault_call_note`, `tasks_file`, `processed_at`, `slack_posted`, and any explicit failure markers.

Append `{note_id}` to `brain/trackers/post-call-analyzer/processed.json` ledger. Use object entries rather than bare IDs when possible, including `id`, `doc_url`, `transcript_doc_url`, `vault_call_note`, `tasks_file`, `processed_at`, and any explicit failure markers.

## Failure handling

- `granola-api` fails for one queue entry → log + skip THAT entry (do not abort the loop); leave queue file in place for next run.
- Transcript Doc create fails → continue with analysis + Attio + staged tasks + Slack + vault, BUT only if the final result object has `transcript_failed: true`, Slack message must say `Transcript save failed — Granola source only` and skip the transcript Doc link.
- Analysis Doc create fails → continue with Attio + staged tasks + Slack + vault, BUT only if the final result object has `doc_failed: true`, Slack message must say `Analysis Doc creation failed — saved transcript only` and skip the analysis Doc link.
- Attio match fails for an attendee → continue without writing that note; log `ATTIO-MATCH-FAIL: {email}`.
- Attio note POST fails → log `ATTIO-WRITE-FAIL: {record_id}`; continue with the other writes.
- Task staging fails → surface `TASKS-FAIL:` prefix in Slack; vault note is the fallback record.
- Slack POST fails → log error, mark queue entry `slack_failed: true`, BUT still mark processed (other artifacts have landed).

## Done definition

For each queue entry, before considering it processed, you MUST have produced:
- Google Doc in RESEARCH/MEETINGS (or explicit `doc_failed: true` marker)
- Transcript Doc in RESEARCH/MEETINGS (or explicit `transcript_failed: true` marker)
- ≥1 Attio note on a matched record (or `attio_failed: true` if zero matches)
- Staged task JSON in `pending-tasks/` (or `tasks_failed: true` if no review-ready items)
- Vault call note at `brain/calls/{date}-{slug}.md`
- Slack message to #ai-operations (or `slack_failed: true`)
- Queue file moved to `processed/{id}.json`
- Entry appended to `processed.json` ledger
