---
name: post-call-analyzer
description: Server-side per-call analysis. Two fires/day (1pm + 6pm ET) poll the Granola REST API via the granola-api wrapper. For each new call, pulls transcript, writes a 1-2 page Google Doc analysis to RESEARCH/MEETINGS, posts Attio notes to matched person + company records, appends review-ready tasks to the TO DO 5.12.26 sheet, and posts ONE Slack message to #ai-operations.
archetype: router
context_budget:
  skill_md: 150
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: false
---

# Post-Call Analyzer

Closes the gap between "Granola transcript landed" and "Kay has the analysis, the tasks, the Attio context, and the Slack ping in hand."

## Architecture (rewritten 2026-05-13)

| Decision | Locked value | Source |
|---|---|---|
| Credential path | 1Password (`op://GB Server/Granola API Key/password`) → `~/.local/bin/granola-api` wrapper → Granola public REST API. **No MCP, no OAuth, no reconnect.** | 2026-05-13 — `feedback_check_credential_source_before_auth.md` + Granola API key path discovery |
| Polling cadence | **2 fires/day: 1pm ET (midday) + 6pm ET (EOD)** | 2026-05-13 — Kay: "I only 1-3 calls per day. thinking midday and eod check" |
| Trigger location | **Server-only.** systemd timer on Hetzner cpx21. No local launchd, no iMac sidecar. | 2026-05-13 — Kay: "we are fully moving to the server, nothing local. one of the reasons is the failure of prior launchd jobs" |
| Call scope | **All calls with transcripts.** No external-only filter. | 2026-05-13 — Kay: "All calls with transcripts need to get processed" |
| Analysis output | **Google Doc (1-2 pages) in RESEARCH/MEETINGS folder** (id `1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz`). One Doc per call. | 2026-05-13 — Kay: "analysis should sit in a folder in the google drive... add each analysis/items as a google doc there" |
| Analysis depth | 1-2 Word-equivalent pages. Can include "further analysis to do" pointers for Kay's approval — no autonomous deep-dive. | 2026-05-13 — Kay: "1-2 pages of a word doc, no more. it can also be a takeway that mentions the analysis that we should do to discover more, but perhaps not done in that moment ahead of my review" |
| Attio integration | **Direct REST API to `/v2/notes`** with API key from 1Password. Writes one note per matched person record + one per matched company record. | 2026-05-13 — Attio Notes write scope verified |
| Task destination | **TO DO 5.12.26 sheet, `TO DO` tab via `task-tracker-manager` skill.** Kay assigns day-slot in morning brief. | 2026-05-13 — Kay: "they should live on the to do tab and then I determine what day you will put each. We can review these in the morning brief" |
| Slack format | **ONE message per call** to `#ai-operations` with: call title + 2-3 line summary + Google Doc link + Granola transcript link + task count. Granola → Slack integration disconnected. | 2026-05-13 — Kay confirmed Path A |
| Idempotency key | Granola note ID (e.g. `not_4rmlqyNoUbrPey`). Ledger at `brain/trackers/post-call-analyzer/processed.json`. | 2026-05-13 |

## Two-stage execution

### Stage 1 — Detector (`scripts/post_call_analyzer_poll.sh`)

Lightweight shell script. **Server-side, fires twice a day at 1pm + 6pm ET via systemd timer.**

1. Reads checkpoint timestamp from `~/.cache/post-call-analyzer/last-checkpoint.txt` (defaults to 24h ago on first run).
2. Calls `granola-api since <checkpoint>` to fetch notes updated after the checkpoint.
3. For each note ID returned that is NOT in `brain/trackers/post-call-analyzer/processed.json`:
   - Write `brain/trackers/post-call-analyzer/queue/{note_id}.json` with note metadata snapshot
4. If queue is non-empty → invokes `scripts/run-skill.sh post-call-analyzer:on-trigger` (background).
5. Updates checkpoint to current UTC timestamp on success.

Defensive: HTTP errors / empty responses / missing `op` resolution → log + exit 0; checkpoint NOT advanced so the next fire retries.

### Stage 2 — Claude run (`headless-on-trigger-prompt.md`)

Triggered by the detector via `run-skill.sh post-call-analyzer:on-trigger`. For each queued note ID:

1. **Pull full note** via `granola-api get-note <id>` — yields transcript, summary_markdown, attendees, web_url, calendar_event.
2. **Match attendees to Attio** — for each non-Kay attendee email, POST `/v2/objects/people/records/query` filtered by `email_addresses`. For each unique company domain, POST `/v2/objects/companies/records/query` filtered by `domains`.
3. **Compose the 1-2 page analysis** — sections: Meeting Overview, Action Items, Search Implications, Operational Implications, Open Loops / Further Analysis Needed (with await-Kay-approval flag), Tasks Created. Anchor on Granola's `summary_markdown`; extend with thinking-layer analysis. Stay inside ~600 words.
4. **Create Google Doc** at `RESEARCH/MEETINGS/{YYYY-MM-DD} — {counterparty-shortname} — Meeting Analysis` via `gog docs create --parent=1CHnc3jtLj7245TZpEP59ZkLPr64RpaCz --file=/tmp/{note_id}.md`.
5. **Write Attio notes** — one note per matched person record + one per matched company record. Title format `{date} — Meeting w/ Kay (G&B)`. Content: short summary + action items + Doc link + Granola transcript link.
6. **Append tasks to TO DO sheet** — for each review-ready item, append `[FALSE, task-text, type, project, due (blank), notes-with-Doc-link]` to `TO DO 5.12.26` sheet, `TO DO` tab. Status=FALSE (unchecked), Due blank (Kay assigns).
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
🎙️ <{granola_url}|Granola transcript>
✅ {N} tasks appended to TO DO tab for your review
```

If the call had zero extractable items: post `*Post-call analysis — {Counterparty} ({date}): no action items / decisions / implications extracted.*` so Kay knows the analyzer ran. Suppress only on processing failure.

## What this skill does NOT do

- **Does not send any email.** Gmail follow-up drafting is OUT OF SCOPE in this rewrite (was previously in scope; deprecated 2026-05-13). If a "send X to Y" item is identified, it becomes a task in the TO DO sheet.
- **Does not auto-assign tasks to day-slots.** Tasks land on the TO DO tab unscheduled. Kay assigns day in morning brief.
- **Does not auto-execute "further analysis" deep-dives.** Pointers are surfaced in the Doc + TO DO sheet; Kay approves before execution.
- **Does not modify Attio person/company FIELDS.** Only writes notes via `/v2/notes`. Field updates remain pipeline-manager territory.
- **Does not aggregate across calls.** One Doc + one Slack message per call. No EOD digest.

## Failure modes + invariants

- If `granola-api` fails (auth, network, 5xx) → detector logs + exits 0; checkpoint NOT advanced; next fire retries.
- If queue contains stale entries (>3 hours old, not processed) → validator flags as RED.
- If Slack webhook fails → log error, mark queue entry `slack_failed: true` but still mark processed (Doc + Attio notes + tasks already landed).
- If Google Doc create fails → log error, fall back to vault-only call note + Slack message with Granola link, no Doc link. Re-queue for next run.
- If Attio note write fails → log error per record, continue with remaining records, surface in Slack with `ATTIO-FAIL: {record}:` prefix.
- If task-tracker append fails → log error, surface in Slack with `TASKS-FAIL:` prefix; vault call note is the fallback record.

## Validator (mandatory per universal POST_RUN_CHECK doctrine)

`scripts/validate_post_call_analyzer_integrity.py` runs after every Claude exit-0.

1. Queue dir empty (all triggers processed) OR all entries <3h old
2. Each processed entry has: matching Google Doc URL captured AND vault call note file present (or explicit failure marker)
3. No file in `processed/` older than 30 days (rotate — warn, not fail)
4. Checkpoint file modification time < 24h ago (detector ran recently)

Validator failure → wrapper overrides exit code → Slack alert with `VALIDATOR FAILED` prefix per `feedback_mutating_skill_hardening_pattern.md`.

## Systemd unit pair (server-side)

- `systemd/post-call-analyzer-poll.service` — Type=oneshot, runs `bash scripts/post_call_analyzer_poll.sh`, EnvironmentFile=`scripts/.env.launchd`
- `systemd/post-call-analyzer-poll.timer` — `OnCalendar=*-*-* 13,18:00 America/New_York` (1pm + 6pm ET daily), `Persistent=true`

Install via `bash scripts/install_systemd_units.sh` then `systemctl --user enable --now post-call-analyzer-poll.timer`.

Logs:
- Detector: `logs/scheduled/post-call-analyzer-poll-{date}.log`
- Claude run: `logs/scheduled/post-call-analyzer-{date}-{HHMM}.log` (via wrapper)
- Wrapper case in `scripts/run-skill.sh` routes `post-call-analyzer:on-trigger` → headless prompt + POST_RUN_CHECK validator.

## Files owned

| Path | Owned? |
|---|---|
| `~/.local/bin/granola-api` | YES (shared utility wrapper — also consumed by future skills) |
| `scripts/post_call_analyzer_poll.sh` | YES (detector) |
| `scripts/validate_post_call_analyzer_integrity.py` | YES (validator) |
| `systemd/post-call-analyzer-poll.service` | YES |
| `systemd/post-call-analyzer-poll.timer` | YES |
| `.claude/skills/post-call-analyzer/SKILL.md` | YES (this file) |
| `.claude/skills/post-call-analyzer/headless-on-trigger-prompt.md` | YES (Claude prompt) |
| `brain/trackers/post-call-analyzer/processed.json` | YES (idempotency ledger) |
| `brain/trackers/post-call-analyzer/queue/*.json` | YES (transient — drained per run) |
| `brain/trackers/post-call-analyzer/processed/*.json` | YES (archive — 30-day rotation) |
| `~/.cache/post-call-analyzer/last-checkpoint.txt` | YES (poll checkpoint) |
| `brain/calls/*.md` | SHARED (writes new files; existing call-note schema) |
| Google Drive `RESEARCH/MEETINGS/` | OWNED for skill outputs |
| Attio Notes (people + companies) | OWNED for `{date} — Meeting w/ Kay (G&B)` titled notes |
| `TO DO 5.12.26` sheet, `TO DO` tab | DELEGATES to `task-tracker-manager` (appends only) |
| Slack `#ai-operations` | OWNED for `*Post-call analysis*` prefixed messages |

## Linked memories

- [[feedback_check_credential_source_before_auth]] — credential ladder (1Password first)
- [[feedback_all_skills_use_1password]] — universal policy
- [[project_drive_research_folder_canonical]] — RESEARCH folder path
- [[feedback_post_call_analyzer_realtime_on_granola]] — original real-time spec; updated 2026-05-13 to 2 fires/day
- [[feedback_mutating_skill_hardening_pattern]] — POST_RUN_CHECK doctrine
- [[project_personal_task_tracker]] — TO DO sheet schema
- [[feedback_inbox_schema_enums]] — vault inbox enum constraints (call notes still use this)
