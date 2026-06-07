---
name: post-call-analyzer
description: Server-side per-call analysis. Two fires/day (1pm + 6pm ET) poll the Granola REST API via the granola-api wrapper. For each new call, pulls transcript, saves the transcript to Google Drive, writes a 1-2 page Google Doc analysis to RESEARCH/MEETINGS, posts Attio notes to matched person + company records, **stages review-ready tasks for Kay's Good Morning approval (NEVER writes to the TO DO sheet directly)**, and posts ONE Slack message to #ai-operations.
archetype: router
context_budget:
  skill_md: 150
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: false
---

# Post-Call Analyzer

Closes the gap between "Granola transcript landed" and "Kay has the saved transcript, acquisition/process analysis, staged action items, Attio context, and Slack ping in hand."

## Architecture (rewritten 2026-05-13)

| Decision | Locked value | Source |
|---|---|---|
| Credential path | 1Password (`op://GB Server/Granola API Key/password`) → `~/.local/bin/granola-api` wrapper → Granola public REST API. **No MCP, no OAuth, no reconnect.** | 2026-05-13 — `feedback_check_credential_source_before_auth.md` + Granola API key path discovery |
| Polling cadence | **2 fires/day: 1pm ET (midday) + 6pm ET (EOD)** | 2026-05-13 — Kay: "I only 1-3 calls per day. thinking midday and eod check" |
| Trigger location | **Server-only.** systemd timer on Hetzner cpx21. No local launchd, no iMac sidecar. | 2026-05-13 — Kay: "we are fully moving to the server, nothing local. one of the reasons is the failure of prior launchd jobs" |
| Call scope | **All calls with transcripts.** No external-only filter. | 2026-05-13 — Kay: "All calls with transcripts need to get processed" |
| Transcript output | **Google Doc transcript in RESEARCH/MEETINGS folder** (id `1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz`). One transcript Doc per call, saved before analysis. | 2026-06-07 — Kay wants Granola transcripts saved down into Google Drive |
| Analysis output | **Google Doc (1-2 pages) in RESEARCH/MEETINGS folder** (id `1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz`). One Doc per call. | 2026-05-13 — Kay: "analysis should sit in a folder in the google drive... add each analysis/items as a google doc there" |
| Analysis depth | 1-2 Word-equivalent pages. Focus on acquisition/process takeaways, issues Kay and DaVinci should discuss, and further analysis pointers for Kay's approval — no autonomous deep-dive. | 2026-05-13 + 2026-06-07 |
| Attio integration | **Direct REST API to `/v2/notes`** with API key from 1Password. Writes one note per matched person record + one per matched company record. | 2026-05-13 — Attio Notes write scope verified |
| Task destination | **Staged to `brain/trackers/post-call-analyzer/pending-tasks/{note_id}.json` for Kay's review in the next Good Morning flow.** Good Morning/pipeline-manager surfaces each staged task with a RECOMMENDed day + YES/NO/DISCUSS. ONLY after Kay's approval and timing decision does task-manager append to the TO DO sheet. **Post-call-analyzer NEVER writes to the TO DO sheet directly.** | 2026-05-28 + 2026-06-07 |
| Slack format | **ONE message per call** to `#ai-operations` with: call title + 2-3 line summary + Google Doc link + Granola transcript link + task count. Granola → Slack integration disconnected. | 2026-05-13 — Kay confirmed Path A |
| Idempotency key | Granola note ID (e.g. `not_4rmlqyNoUbrPey`). Ledger at `brain/trackers/post-call-analyzer/processed.json`. | 2026-05-13 |

## Two-stage execution

### Stage 1 — Detector (`scripts/post_call_analyzer_poll.sh`)

Lightweight shell script. **Server-side, fires twice a day at 1pm + 6pm ET via systemd timer.**

1. Reads checkpoint timestamp from `~/.cache/post-call-analyzer/last-checkpoint.txt` (defaults to 24h ago on first run).
2. Calls `granola-api since <checkpoint>` to fetch notes updated after the checkpoint.
3. For each note ID returned that is NOT in `brain/trackers/post-call-analyzer/processed.json`:
   - Write `brain/trackers/post-call-analyzer/queue/{note_id}.json` with note metadata snapshot
4. If queue is non-empty → invokes `scripts/run-agent-skill.sh post-call-analyzer:on-trigger` (background).
5. Updates checkpoint to current UTC timestamp on success.

Defensive: HTTP errors / empty responses / missing `op` resolution → log + exit 0; checkpoint NOT advanced so the next fire retries.

### Stage 2 — Codex run (`headless-on-trigger-prompt.md`)

Triggered by the detector via `run-agent-skill.sh post-call-analyzer:on-trigger`. For each queued note ID:

**Granola access doctrine (important):** Granola transcript access is expected to work through the 1Password-backed REST wrapper. Do not conclude "transcript unavailable" because MCP/OAuth is unavailable. The old Claude Code failure mode was forgetting the 1Password path and getting stuck on OAuth. Codex must use:

```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
granola-api get-note <note_id>
```

If transcript extraction fails, log the actual JSON keys returned by `granola-api get-note` and keep the queue entry for retry unless the note definitively has no transcript field/content. Do not try Granola MCP or local OAuth.

1. **Pull full note** via `granola-api get-note <id>` — yields transcript, summary_markdown, attendees, web_url, calendar_event.
2. **Save transcript Google Doc** at `RESEARCH/MEETINGS/{YYYY-MM-DD} — {counterparty-shortname} — Granola Transcript` via `gog docs create --parent=1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz --file=/tmp/{note_id}-transcript.md`.
3. **Match attendees to Attio** — for each non-Kay attendee email, POST `/v2/objects/people/records/query` filtered by `email_addresses`. For each unique company domain, POST `/v2/objects/companies/records/query` filtered by `domains`.
4. **Compose the 1-2 page analysis** — sections: Meeting Overview, Acquisition/Search Takeaways, Process/Operating Takeaways, Items for Kay + DaVinci to Discuss, Potential Action Items for Good Morning, Open Loops / Further Analysis Needed (with await-Kay-approval flag). Anchor on the saved transcript + Granola's `summary_markdown`; extend with thinking-layer analysis. Stay inside ~600 words.
5. **Create analysis Google Doc** at `RESEARCH/MEETINGS/{YYYY-MM-DD} — {counterparty-shortname} — Meeting Analysis` via `gog docs create --parent=1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz --file=/tmp/{note_id}-analysis.md`.
6. **Write Attio notes** — one note per matched person record + one per matched company record. Title format `{date} — Meeting w/ Kay (G&B)`. Content: short summary + key takeaways + analysis Doc link + transcript Doc link + Granola transcript link.
7. **Stage tasks for Good Morning approval** — for each review-ready item, write to `brain/trackers/post-call-analyzer/pending-tasks/{note_id}.json` (one file per source call, JSON array of task objects). Each task object: `{task_text, type, project, suggested_day, suggested_due_date, notes_with_doc_link, source_call_id, source_doc_url, source_transcript_url, staged_at}`. **DO NOT invoke any TO DO write path from this skill.** Good Morning/pipeline-manager picks up the staged tasks in the next morning briefing and surfaces each with a RECOMMENDed day + YES/NO/DISCUSS for Kay. Only on Kay's approval and timing decision does task-manager add approved tasks to the TO DO sheet, after which pipeline-manager moves the staged file to `brain/trackers/post-call-analyzer/pending-tasks/processed/{note_id}.json`.
7. **Write vault call note** at `brain/calls/{date}-{slug}.md` per `schemas/vault/call.yaml` — for knowledge graph + Obsidian Dataview queries. Wiki-links all attendees + company + Doc.
8. **Post Slack message** to `#ai-operations` webhook with the format below.
9. **Move queue file** → `brain/trackers/post-call-analyzer/processed/{note_id}.json` archive + append to `processed.json` ledger.

## Slack message format

ONE message per call. Posts to `$SLACK_WEBHOOK_OPERATIONS`.

```
*Post-call analysis — {Counterparty} ({date} {time})*
_{location or "remote"}_

{2-3 line summary — anchor on Granola's summary_markdown}

📝 <{doc_url}|Full analysis (Google Doc)>
📄 <{transcript_doc_url}|Saved transcript (Google Doc)>
🎙️ <{granola_url}|Granola source>
✅ {N} tasks staged for morning briefing — you'll assign days + approve before any land on the TO DO sheet
```

If the call had zero extractable items: post `*Post-call analysis — {Counterparty} ({date}): no action items / decisions / implications extracted.*` so Kay knows the analyzer ran. Suppress only on processing failure.

## What this skill does NOT do

- **Does not send any email.** Gmail follow-up drafting is OUT OF SCOPE in this rewrite (was previously in scope; deprecated 2026-05-13). If a "send X to Y" item is identified, it becomes a staged task surfaced in the morning briefing.
- **Does not write to the TO DO sheet directly.** Tasks are STAGED for Kay's approval in the next Good Morning flow. Pipeline-manager presents each with a RECOMMENDed day + YES/NO/DISCUSS; only on Kay's approval and timing decision does task-manager append (2026-05-28 + 2026-06-07 doctrine — [[feedback-no-direct-task-writes-from-skills]]).
- **Does not assign suggested days as commitments.** The `suggested_day` field in the staged task JSON is a hint for pipeline-manager's RECOMMEND framing, not a write target. Kay's response is the only signal that schedules a task.
- **Does not auto-execute "further analysis" deep-dives.** Pointers are surfaced in the analysis Doc and staged Good Morning items; Kay approves before execution.
- **Does not modify Attio person/company FIELDS.** Only writes notes via `/v2/notes`. Field updates remain pipeline-manager territory.
- **Does not aggregate across calls.** One Doc + one Slack message per call. No EOD digest.

## Failure modes + invariants

- If `granola-api` fails (auth, network, 5xx) → detector logs + exits 0; checkpoint NOT advanced; next fire retries.
- If queue contains stale entries (>3 hours old, not processed) → validator flags as RED.
- If Slack webhook fails → log error, mark queue entry `slack_failed: true` but still mark processed (Doc + Attio notes + staged-tasks file already landed).
- If Google Doc create fails → log error, fall back to vault-only call note + Slack message with Granola link, no Doc link. Re-queue for next run.
- If Attio note write fails → log error per record, continue with remaining records, surface in Slack with `ATTIO-FAIL: {record}:` prefix.
- If staged-tasks file write fails → log error, surface in Slack with `STAGE-FAIL:` prefix; vault call note is the fallback record. Pipeline-manager will not see the tasks until the next run picks up the retry.

## Validator (mandatory per universal POST_RUN_CHECK doctrine)

`scripts/validate_post_call_analyzer_integrity.py` runs after every Codex exit-0.

1. Queue dir empty (all triggers processed) OR all entries <3h old
2. Each processed entry has: matching Google Doc URL captured AND vault call note file present (or explicit failure marker)
3. No file in `processed/` older than 30 days (rotate — warn, not fail)
4. Checkpoint file modification time < 24h ago (detector ran recently)

Validator failure → wrapper overrides exit code → Slack alert with `VALIDATOR FAILED` prefix per `feedback_mutating_skill_hardening_pattern.md`.

## Systemd unit pair (server-side)

- `systemd/post-call-analyzer-poll.service` — Type=oneshot, runs `bash scripts/post_call_analyzer_poll.codex.sh`; wrapper sources `scripts/op-env.sh` for 1Password-backed credentials
- `systemd/post-call-analyzer-poll.timer` — `OnCalendar=*-*-* 13,18:00 America/New_York` (1pm + 6pm ET daily), `Persistent=true`

Install via `bash scripts/install_systemd_units.sh` then `systemctl --user enable --now post-call-analyzer-poll.timer`.

Logs:
- Detector: `logs/scheduled/post-call-analyzer-poll-{date}.log`
- Codex run: `logs/scheduled/post-call-analyzer-{date}-{HHMM}.log` (via wrapper)
- Wrapper case in `scripts/run-agent-skill.sh` routes `post-call-analyzer:on-trigger` → headless prompt + POST_RUN_CHECK validator.

## Files owned

| Path | Owned? |
|---|---|
| `~/.local/bin/granola-api` | YES (shared utility wrapper — also consumed by future skills) |
| `scripts/post_call_analyzer_poll.sh` | YES (detector) |
| `scripts/validate_post_call_analyzer_integrity.py` | YES (validator) |
| `systemd/post-call-analyzer-poll.service` | YES |
| `systemd/post-call-analyzer-poll.timer` | YES |
| `.agents/skills/post-call-analyzer/SKILL.md` | YES (this file) |
| `.agents/skills/post-call-analyzer/headless-on-trigger-prompt.md` | YES (Codex prompt) |
| `brain/trackers/post-call-analyzer/processed.json` | YES (idempotency ledger) |
| `brain/trackers/post-call-analyzer/queue/*.json` | YES (transient — drained per run) |
| `brain/trackers/post-call-analyzer/processed/*.json` | YES (archive — 30-day rotation) |
| `brain/trackers/post-call-analyzer/pending-tasks/*.json` | YES (staged tasks awaiting Kay's Good Morning approval — pipeline-manager reads, moves to `pending-tasks/processed/` after Kay's approval) |
| `brain/trackers/post-call-analyzer/pending-tasks/processed/*.json` | YES (archive of approved task batches; pipeline-manager moves files here after task-manager confirms the approved tasks landed) |
| `~/.cache/post-call-analyzer/last-checkpoint.txt` | YES (poll checkpoint) |
| `brain/calls/*.md` | SHARED (writes new files; existing call-note schema) |
| Google Drive `RESEARCH/MEETINGS/` | OWNED for transcript + analysis outputs |
| Attio Notes (people + companies) | OWNED for `{date} — Meeting w/ Kay (G&B)` titled notes |
| `TO DO` sheet (current week) | **NEVER writes directly.** Tasks staged in `pending-tasks/` for Kay's Good Morning approval. Task-manager adds approved tasks ONLY after Kay's YES/day-assignment. |
| Slack `#ai-operations` | OWNED for `*Post-call analysis*` prefixed messages |

## Linked memories

- [[feedback_check_credential_source_before_auth]] — credential ladder (1Password first)
- [[feedback_all_skills_use_1password]] — universal policy
- [[project_drive_research_folder_canonical]] — RESEARCH folder path
- [[feedback_post_call_analyzer_realtime_on_granola]] — original real-time spec; updated 2026-05-13 to 2 fires/day
- [[feedback_mutating_skill_hardening_pattern]] — POST_RUN_CHECK doctrine
- [[project_personal_task_tracker]] — TO DO sheet schema
- [[feedback_inbox_schema_enums]] — vault inbox enum constraints (call notes still use this)
- [[feedback_no_direct_task_writes_from_skills]] — 2026-05-28 doctrine: derived skills stage tasks for Kay's briefing approval, never write directly to the TO DO sheet
