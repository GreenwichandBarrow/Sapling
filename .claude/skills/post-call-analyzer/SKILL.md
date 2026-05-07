---
name: post-call-analyzer
description: Real-time post-call processing. Polls Granola's local cache every 10 min during business hours; when a new transcript lands, writes a vault call note, routes action items to task-tracker-manager (one-off → Excel), routes projects to project tabs, drafts (not sends) Gmail follow-ups for "send X to Y" items, and posts ONE Slack message per call. Trigger-driven, not batched.
user_invocable: false
---

# Post-Call Analyzer

Standing-on owner of the post-meeting loop. Closes the gap between "Granola transcript landed" and "vault + tracker + drafts updated."

## Architecture (locked 2026-05-06 + 2026-05-07)

| Decision | Locked value | Source |
|---|---|---|
| ONE skill or two | ONE — routes through existing infra (task-tracker-manager + pipeline-manager) | session-decisions 2026-05-06 |
| Polling cadence | 10 min via launchd | session-decisions 2026-05-06 |
| Slack timing | Real-time per-call when transcript populates (NOT EOD digest) | `feedback_post_call_analyzer_realtime_on_granola.md` 2026-05-07 |
| Email follow-up scope | Skill DRAFTS (never sends) Gmail follow-ups for action items where next-step is "send X to Y" | `feedback_post_call_analyzer_realtime_on_granola.md` 2026-05-07 |
| Task vs project | Task = one-off; Project = multi-week coordinated initiative w/ multiple work streams | `feedback_task_vs_project_heuristic.md` |

## Two-stage execution

The analyzer is split into a cheap detector + an expensive Claude run. The detector fires only when Granola writes to its cache file (event-driven via launchd `WatchPaths`); the Claude run fires only when the detector finds new content.

### Stage 1 — Detector (`scripts/post_call_analyzer_poll.py`)

Cheap Python script. **Triggered by macOS launchd `WatchPaths`** when `~/Library/Application Support/Granola/cache-v6.json` changes — NOT on a fixed interval. No polling.

This means:
- Granola flushes its cache → detector fires within seconds
- Granola idle → detector never fires (zero cost on no-call days)
- The detector inherits Granola's flush cadence as its trigger cadence

1. Business-hours gate: Mon-Fri 8am-7pm ET; outside → exit 0 silently (defense-in-depth against accidental off-hours flushes)
2. Load `~/Library/Application Support/Granola/cache-v6.json`
3. Load `brain/trackers/post-call-analyzer/processed.json`
4. Find docs where:
   - `meeting_end_count > 0` (Granola's "meeting ended" signal)
   - `updated_at` within last 60 min
   - `id` not in processed
   - Has extractable content via multi-source check: `notes_plain` ≥100 chars OR `notes_markdown` ≥100 chars OR transcripts entry with ≥5 turns
   - `deleted_at` is null
5. For each new doc → write `brain/trackers/post-call-analyzer/queue/{doc_id}.json` with extracted metadata
6. If queue is non-empty → invoke `run-skill.sh post-call-analyzer on-trigger`
7. Else → exit 0 silently (no Slack, no log noise)

**Why no calendar-event gate:** Granola flushes its JSON cache lazily — sometimes hours after a call ends. A calendar-event-end gate (with 60-min lookback) would falsely reject Granola flushes that arrive late. Idempotency via `processed.json` + `meeting_end_count > 0` filter handles deduplication correctly without needing a calendar cross-check.

**Known limitation (accepted 2026-05-07):** Granola encrypts its real-time cache (`cache-v6.json.enc`); the unencrypted JSON we read flushes lazily (typically every few hours, on app activity). So the "lag from call end → Slack" is bounded by Granola's flush schedule, not by our trigger. Kay's spec is "same-day, ideally fast, lag OK." See `feedback_post_call_analyzer_realtime_on_granola.md`.

**Idempotency:** writing to the queue dir is overwrite-safe. If the same doc is detected on consecutive polls (e.g., still being edited), the queue entry just refreshes; processed.json gates duplicate processing downstream.

### Stage 2 — Claude run (headless prompt)

Triggered by the poller via `run-skill.sh post-call-analyzer on-trigger`. Headless prompt at `headless-on-trigger-prompt.md`.

For each queued doc:

1. Read full doc from Granola cache (notes_plain, transcribe, title, people, google_calendar_event)
2. Resolve attendees → vault entity slugs (create stubs for new people)
3. Write vault call note `brain/calls/{date}-{slug}.md` per `schemas/vault/call.yaml`
4. Extract action items into three buckets:
   - **Tasks** (one-off) → `python3 scripts/task_tracker.py append` (Excel To Do tab)
   - **Projects** (multi-week, multi-stream) → flag in Slack message with project name; do NOT auto-create project tab (Kay decides scope)
   - **Email follow-ups** (next step is "send X to Y") → create Gmail draft via `gog gmail draft` (NEVER send)
5. Extract decisions → append to today's `brain/context/session-decisions-{date}.md` under `## Auto-extracted from {call}` (if file doesn't exist, create stub)
6. Post ONE Slack message to `#operations` with:
   - Call title + duration + attendees
   - Action items (tasks created, drafts created, projects flagged)
   - Decisions captured
   - Vault note link
7. Move queue file → `brain/trackers/post-call-analyzer/processed/{doc_id}.json`
8. Append doc_id to `processed.json`

## Routing rules

| Item type | Pattern in transcript | Route |
|---|---|---|
| **Task** | "I'll do X" / "next step: I do X" / "Kay to follow up on X" — one-off, single action | task-tracker-manager → Excel To Do |
| **Project** | Multi-step initiative spanning weeks ("we should build a server", "stand up the X program") | Slack-flag only; Kay decides scope + creates project tab manually |
| **Email follow-up** | "I'll send Y to Z" / "follow up with Z about Y" / "intro Z to W" | Gmail draft (NEVER send) |
| **Decision** | "we decided", "we're going to", "the call is" — bilateral conclusion | Append to today's session-decisions |

When the same item could route two ways (e.g., "I'll send the spec to Sam" = both task AND email), prefer email-draft route (richer artifact), and the draft itself counts as the task.

## Slack message format

ONE message per call. Posts to webhook in `$SLACK_WEBHOOK_OPERATIONS`.

```
[Granola] {Call Title} — {duration} — {attendee count} attendees
{vault link}

Action items:
- TASK: {task summary} → Excel To Do
- DRAFT: {to recipient}: {subject} → Gmail drafts
- PROJECT (needs Kay scope): {project name}

Decisions:
- {decision 1}
- {decision 2}

(no decisions captured) ← if empty
```

If the call had zero extractable items (all small talk / no actions / no decisions), still post a one-line "[Granola] {title} — no action items extracted" so Kay knows the analyzer ran. Suppresses only on processing failure.

## What this skill does NOT do

- **Does not send any email.** Only drafts.
- **Does not create Motion/Beads tasks.** Excel To Do via task-tracker-manager is the task system.
- **Does not modify Attio.** Pipeline-manager owns Attio writes.
- **Does not create project tabs.** Project flag in Slack → Kay creates tab manually if she agrees scope is project-sized.
- **Does not run during weekends or off-hours.** Business-hours gate in poller.
- **Does not aggregate across calls.** One Slack message per call. No EOD digest.

## Failure modes + invariants

- If `cache-v6.json` is locked (Granola actively writing) → poller catches IOError, logs warning, exits 0. Next poll picks up.
- If queue contains stale entries (>24h old, not processed) → validator flags as RED.
- If Slack webhook fails → log error, mark queue entry as `slack_failed: true` but still mark processed (vault + drafts + tasks already landed; Slack is the notification, not the artifact).
- If Gmail draft creation fails → log error, demote to TASK with note "draft failed, manual send needed".

## Validator (mandatory)

`scripts/validate_post_call_analyzer_integrity.py` runs after every Claude exit-0. Checks:

1. Queue dir is empty (all triggers processed) OR all queue entries are <30 min old (still mid-flight)
2. processed.json grew by N entries where N = queue size at start
3. Each processed entry has corresponding vault call note OR explicit failure marker
4. No file in `processed/` is older than 30 days (rotate)

Validator failure → wrapper overrides exit code → Slack alert with "VALIDATOR FAILED" prefix per `feedback_mutating_skill_hardening_pattern.md`.

## Plist

`~/Library/LaunchAgents/com.greenwich-barrow.post-call-analyzer.plist`

- **Trigger:** `WatchPaths` on `~/Library/Application Support/Granola/cache-v6.json` (no `StartInterval`, no polling)
- Business-hours gating happens inside `post_call_analyzer_poll.py` (defense-in-depth)
- Logs: `logs/scheduled/post-call-analyzer-poll-{date}.log` (detector) + `logs/scheduled/post-call-analyzer-{date}-{HHMM}.log` (Claude run)
- Wrapper: `scripts/run-skill.sh post-call-analyzer on-trigger`
- POST_RUN_CHECK: `python3 scripts/validate_post_call_analyzer_integrity.py`

The plist runs the detector. The detector invokes the wrapper internally only when the queue has work. The wrapper invokes the headless Claude prompt with POST_RUN_CHECK validator. This means:
- launchd fires detector only on Granola cache writes (event-driven)
- Detector exits silently if no new docs (zero token cost)
- Claude only fires when there's actual work (one run per call)

Activation: `launchctl load ~/Library/LaunchAgents/com.greenwich-barrow.post-call-analyzer.plist`

If the trigger doesn't fire reliably (e.g., Granola batches flushes across multiple calls or skips flushes entirely), pivot to: (a) decrypt `cache-v6.json.enc` via Keychain `safeStorage`, OR (b) add a fallback `StartInterval` of 4 hours alongside `WatchPaths` to catch missed events.

## Files owned

| Path | Owned? |
|---|---|
| `scripts/post_call_analyzer_poll.py` | YES (poller) |
| `scripts/validate_post_call_analyzer_integrity.py` | YES (validator) |
| `.claude/skills/post-call-analyzer/SKILL.md` | YES (this file) |
| `.claude/skills/post-call-analyzer/headless-on-trigger-prompt.md` | YES (Claude prompt) |
| `brain/trackers/post-call-analyzer/processed.json` | YES (idempotency ledger) |
| `brain/trackers/post-call-analyzer/queue/*.json` | YES (transient — drained per run) |
| `brain/trackers/post-call-analyzer/processed/*.json` | YES (archive — 30-day rotation) |
| `brain/calls/*.md` | SHARED (writes new files; existing call-note convention) |
| Excel To Do (task-tracker) | DELEGATES to task-tracker-manager |
| Gmail drafts | DELEGATES to `gog gmail draft` |
| Slack `#operations` | OWNED for `[Granola]` prefixed messages |
