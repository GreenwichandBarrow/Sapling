You are running the `post-call-analyzer` skill in headless mode. The detector (`scripts/post_call_analyzer_poll.sh`) has dropped one or more queue files at `brain/trackers/post-call-analyzer/queue/{note_id}.json`. Your job is to drain the queue and process every entry end-to-end.

**DO NOT ask clarifying questions. DO NOT propose follow-up work. Make decisions and execute. The top failure mode is producing zero artifacts.**

## Architecture summary (read SKILL.md for full detail)

- Credential path: `op://GB Server/Granola API Key/password` → `~/.local/bin/granola-api`
- No MCP, no OAuth, no reconnect anywhere
- All writes are: Google Doc (RESEARCH/MEETINGS) + Attio notes (person+company) + TO DO sheet (tasks) + Slack (#ai-operations) + vault call note

## Pre-flight reads (mandatory)

1. `.claude/skills/post-call-analyzer/SKILL.md` — full skill spec including Slack format + failure invariants
2. `CLAUDE.md` — vault writing rules + pre-flight checklists (especially "Before writing to a Google Sheet" + "Before writing a brain/ vault file" + "Before handling secrets / config")
3. `schemas/vault/call.yaml` — the call note schema you must match
4. `brain/trackers/post-call-analyzer/processed.json` — current ledger

## Bootstrap credentials

```bash
set -a; source ~/.config/op-sa-token.env; set +a
export GRANOLA_KEY=$(op read 'op://GB Server/Granola API Key/password')
export ATTIO_KEY=$(op read 'op://GB Server/Attio API Key/password')
export GOG_KEYRING_PASSWORD=$(op read 'op://GB Server/GOG Keyring Password/password')
export SLACK_WEBHOOK_OPERATIONS=$(op read 'op://GB Server/u2shpr72znynqh2s62jue25wzi/password')
```

## Per-queued-note workflow

Run `ls brain/trackers/post-call-analyzer/queue/*.json 2>/dev/null | grep -v gitkeep`. For each queue file:

### Step 1 — Pull full note

```bash
granola-api get-note <note_id> > /tmp/{note_id}.json
```

Parse: `id`, `title`, `created_at`, `updated_at`, `web_url`, `owner`, `attendees`, `calendar_event`, `summary_markdown`, `transcript`.

### Step 2 — Match attendees to Attio

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

### Step 3 — Compose the analysis

Anchor on `summary_markdown` (Granola has already extracted the meeting structure). Layer on the THINKING analysis:

1. **Meeting Overview** (1 paragraph)
2. **Action Items** — bulleted: counterparty commitments (inbound) + Kay commitments (outbound)
3. **Search Implications** — 3-5 bullets. What does this tell us about thesis/niche/buyer pool/broker channel/specific deal? Cross-reference G&B doctrine (Charter / scorecard / buy-box) where relevant.
4. **Operational Implications** — 2-3 bullets. What does this surface about G&B's own processes (briefs, voice, tracker, drift between commitments)?
5. **Open Loops / Further Analysis Needed** — bulleted, EACH with "await Kay approval before deep-dive" flag. Do NOT execute any deep-dive in this run.
6. **Tasks Created** — short cross-reference list pointing at the TO DO sheet

Target: ~600 words / 1-2 Word-equivalent pages. Stay tight. Write to `/tmp/{note_id}-analysis.md`.

### Step 4 — Create Google Doc

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

### Step 5 — Write Attio notes

For each matched record (person + company), write a note. Content: short summary (3-4 lines), action items bullets, links to Doc + Granola transcript.

```bash
curl -s -X POST -H "Authorization: Bearer $ATTIO_KEY" -H "Content-Type: application/json" \
  -d '{"data": {"parent_object": "people|companies", "parent_record_id": "<id>", "title": "{date} — Meeting w/ Kay (G&B)", "content": "<markdown>", "format": "markdown"}}' \
  https://api.attio.com/v2/notes
```

### Step 6 — Append tasks to TO DO sheet

Sheet ID `1ewqQshtN5pz8kmMTEvBZgAFy-0XB37-MVONkN_mdZmk`. Tab `TO DO`. Schema: `[Status, Task, Type, Project, Due, Notes]`. Status always FALSE (unchecked). Due blank (Kay assigns the day-slot in morning brief).

Use `gog sheets append --values-json` (per `feedback_gog_sheets_value_delimiters` — never positional for prose values).

Each task gets a Notes column entry: `From {counterparty} {date} mtg. Analysis: {DOC_URL}`.

### Step 7 — Write vault call note

`brain/calls/{date}-{counterparty-slug}.md` per `schemas/vault/call.yaml`. Required: frontmatter with people + companies wiki-linked to `[[entities/{slug}]]`, tags including `person/{slug}` + `company/{slug}` + `date/{YYYY-MM-DD}` + `call`, schema_version 1.1.0. Body links to Doc + Granola transcript.

If any referenced entity doesn't exist in `brain/entities/`, create the stub per the entity schema. Do NOT leave broken wiki-links.

### Step 8 — Post Slack message

Format per SKILL.md "Slack message format" section. Post via `$SLACK_WEBHOOK_OPERATIONS`.

```python
import os, json, urllib.request
msg = {"blocks": [
  {"type": "section", "text": {"type": "mrkdwn", "text":
    f"*Post-call analysis — {counterparty} ({date} {time})*\n_{location}_\n\n{summary_2to3_lines}"
  }},
  {"type": "section", "text": {"type": "mrkdwn", "text":
    f":memo: <{doc_url}|Full analysis (Google Doc)>\n"
    f":microphone: <{granola_url}|Granola transcript>\n"
    f":white_check_mark: {task_count} tasks appended to TO DO tab for your review"
  }}
]}
req = urllib.request.Request(os.environ["SLACK_WEBHOOK_OPERATIONS"], method="POST",
  headers={"Content-Type": "application/json"}, data=json.dumps(msg).encode())
urllib.request.urlopen(req)
```

### Step 9 — Move queue file → processed archive

```bash
mv brain/trackers/post-call-analyzer/queue/{note_id}.json \
   brain/trackers/post-call-analyzer/processed/{note_id}.json
```

Append `{note_id}` to `brain/trackers/post-call-analyzer/processed.json` ledger (which is `{ "processed": [list of ids], "last_updated": "<iso>" }`). Update with both the new id AND `doc_url` so the validator can verify Doc existence.

## Failure handling

- `granola-api` fails for one queue entry → log + skip THAT entry (do not abort the loop); leave queue file in place for next run.
- Doc create fails → continue with Attio + tasks + Slack + vault, BUT Slack message must say `⚠️ Doc creation failed — Granola transcript only` and skip the Doc link.
- Attio match fails for an attendee → continue without writing that note; log `ATTIO-MATCH-FAIL: {email}`.
- Attio note POST fails → log `ATTIO-WRITE-FAIL: {record_id}`; continue with the other writes.
- Task append fails → surface `TASKS-FAIL:` prefix in Slack; vault note is the fallback record.
- Slack POST fails → log error, mark queue entry `slack_failed: true`, BUT still mark processed (other artifacts have landed).

## Done definition

For each queue entry, before considering it processed, you MUST have produced:
- Google Doc in RESEARCH/MEETINGS (or explicit `doc_failed: true` marker)
- ≥1 Attio note on a matched record (or `attio_failed: true` if zero matches)
- ≥1 task appended to TO DO tab (or `tasks_failed: true` if no review-ready items)
- Vault call note at `brain/calls/{date}-{slug}.md`
- Slack message to #ai-operations (or `slack_failed: true`)
- Queue file moved to `processed/{id}.json`
- Entry appended to `processed.json` ledger
