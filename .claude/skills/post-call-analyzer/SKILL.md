---
name: post-call-analyzer
description: Real-time post-call processing. Polls Granola cloud via MCP every 5 min on the server (24/7); when a new meeting lands, writes a vault call note, queues tasks, drafts Gmail follow-ups for "send X to Y" items, flags projects, appends decisions, surfaces thought-analysis prompts, and posts ONE Slack message per call. Trigger-driven downstream, server-polled upstream.
user_invocable: false
---

# Post-Call Analyzer

Standing-on owner of the post-meeting loop. Closes the gap between "Granola transcript landed" and "vault + tracker + drafts + thought-analysis prompts updated."

## Architecture (locked 2026-05-06 → 2026-05-08)

| Decision | Locked value | Source |
|---|---|---|
| ONE skill or two | ONE — routes through existing infra (task-tracker-manager + pipeline-manager + /triage) | session-decisions 2026-05-06 |
| Detector | Server-side MCP poll via `mcp__granola__list_meetings` (replaces iMac local-cache reader) | Phase 4 spec 2026-05-08 |
| Polling cadence | 5 min via systemd `OnUnitActiveSec=5min` (was 10 min via launchd; rate-limit GREEN at 0.07% capacity) | Phase 4 spec 2026-05-08 |
| Business-hours gate | NONE — server runs 24/7; Kay's call cadence determines load | Phase 4 spec 2026-05-08 |
| MCP lookback | 24h (processed.json does dedup) | Phase 4 spec 2026-05-08 |
| Idempotency key | Granola **cloud** meeting ID (not local doc_id) | Phase 4 spec 2026-05-08 |
| Routing buckets | 5: Tasks, Projects, Email, Decisions, **Thought Analysis** (new) | Phase 4 spec 2026-05-08 |
| Slack timing | Real-time per-call when transcript populates (NOT EOD digest) | `feedback_post_call_analyzer_realtime_on_granola.md` 2026-05-07 |
| Email follow-up scope | Skill DRAFTS (never sends) Gmail follow-ups for "send X to Y" items | `feedback_post_call_analyzer_realtime_on_granola.md` 2026-05-07 |
| Task vs project | Task = one-off; Project = multi-week coordinated initiative | `feedback_task_vs_project_heuristic.md` |
| Deferred-content gate | DROPPED in Phase 4 — MCP returns server-summarized transcripts, no lazy-flush issue | Phase 4 spec 2026-05-08 |

## Two-stage execution

### Stage 1 — Detector (`scripts/post_call_analyzer_mcp_poll.py`)

Cheap Python script. **Server-side, fires every 5 min via systemd timer.** Replaces the iMac WatchPaths-driven `post_call_analyzer_poll.py` (that script stays alive during shadow mode but is retired in Phase 4.5).

1. Calls `mcp__granola__list_meetings` via `claude -p` as a thin MCP client subprocess. Granola MCP is OAuth-gated; Claude Code handles the auth handshake when `claude mcp add granola https://mcp.granola.ai/mcp` has been run once on the server.
2. Filters to meetings with `ended_at` within last 24h.
3. Skips any meeting whose ID is already in `brain/trackers/post-call-analyzer/processed.json`.
4. Skips any meeting whose ID is already a queue file (race with iMac sidecar during shadow mode).
5. For each remaining meeting → writes `brain/trackers/post-call-analyzer/queue/{meeting_id}.json` with `detector: "mcp"` flag.
6. If queue is non-empty → invokes `run-skill.sh post-call-analyzer on-trigger` (background, non-blocking).
7. Defensive against MCP downtime / auth failure / timeout / malformed JSON: log + exit 0. The validator on the next successful run will catch stale queue entries (>30 min old).

**No business-hours gate.** Server runs 24/7; the cadence + Anthropic rate-limit headroom handle the cost question.

**Why the iMac script stays during shadow mode:** Both detectors write to the same `queue/` dir + `processed.json` ledger. Whichever detects a meeting first writes the queue file; the other no-ops on its next tick (existing-queue-file guard). Neither double-processes (processed.json dedup). Phase 4.5 retires the iMac plist after Kay validates output parity.

### Stage 2 — Claude run (headless prompt)

Triggered by either detector via `run-skill.sh post-call-analyzer on-trigger`. Headless prompt at `headless-on-trigger-prompt.md`.

For each queued meeting:

1. Read queue file → get `meeting_id` + metadata.
2. Read full transcript via `mcp__granola__get_meeting_transcript({meeting_id})` (Phase 4 path) — falls back to local cache read for queue entries with `detector: "watchpaths"` from the iMac sidecar during shadow mode.
3. Resolve attendees → vault entity slugs (create stubs for new people).
4. Write vault call note `brain/calls/{date}-{slug}.md` per `schemas/vault/call.yaml`.
5. Extract and route into FIVE buckets (see Routing rules below).
6. Post ONE Slack message to `#operations` with action items + decisions + thought-analysis section.
7. Move queue file → `brain/trackers/post-call-analyzer/processed/{meeting_id}.json` archive.
8. Append to `processed.json` ledger.

## Routing rules

| Bucket | Pattern in transcript | Route |
|---|---|---|
| **Task** | "I'll do X" / "next step: I do X" / "Kay to follow up on X" — one-off, single action | Write `brain/trackers/post-call-analyzer/task_queue/{meeting_id}.json` (Phase 4.5 will drain to Excel; for now just queue) |
| **Project** | Multi-step initiative spanning weeks ("we should build X", "stand up the Y program") | Slack-flag only; Kay decides scope + creates project tab manually |
| **Email follow-up** | "I'll send Y to Z" / "follow up with Z about Y" / "intro Z to W" | Gmail draft via `gog gmail drafts create` (NEVER send) |
| **Decision** | "we decided" / "we're going to" / "the call is" — bilateral conclusion | Append to today's `brain/context/session-decisions-{date}.md` under `## Auto-extracted from {call}` |
| **Thought Analysis** (new in Phase 4) | Factual unknown OR strategic frame surfaced during call | Factual ("what's the TAM," "I should look up X") → `brain/inbox/{date}-{slug}-research-prompt.md` per `schemas/vault/research-prompt.yaml`. Strategic ("should we be in this niche," "is this the right approach") → `brain/inbox/{date}-{slug}-socrates-question.md` per `schemas/vault/socrates-question.yaml` |

When the same item could route two ways (e.g., "I'll send the spec to Sam" = both task AND email), prefer email-draft (richer artifact); the draft itself counts as the task.

When the same item is both a research-prompt AND a socrates-question, prefer socrates-question — strategic frames are higher-leverage for Kay's review.

### Heuristic: research vs socrates

| Cue | Routes to |
|---|---|
| Numerical answer would resolve it ("what's the TAM," "how many," "what multiple") | research-prompt |
| Lookupable fact ("I should check," "do we know," "let me look that up") | research-prompt |
| Direction-setting ("should we," "is this the right," "are we optimizing for") | socrates-question |
| Identity / scope frame ("are we still a holding company or a search fund," "do we even do this size") | socrates-question |
| Stress-test of an assumption ("but what if," "the assumption there is") | socrates-question |

## Slack message format

ONE message per call. Posts to webhook in `$SLACK_WEBHOOK_OPERATIONS`.

```
[Granola] {Call Title} — {duration} — {attendee count} attendees
{vault link}

Action items:
- TASK: {task summary} → task_queue
- DRAFT: {to recipient}: {subject} → Gmail drafts
- PROJECT (needs Kay scope): {project name}

Decisions:
- {decision 1}
- {decision 2}

Thought analysis:
- RESEARCH: {question} → brain/inbox/{file}
- SOCRATES: {question} → brain/inbox/{file}

(no decisions captured) ← if section empty
(no thought analysis) ← if section empty
```

If the call had zero extractable items, still post `[Granola] {title} — no action items extracted` so Kay knows the analyzer ran. Suppresses only on processing failure.

## What this skill does NOT do

- **Does not send any email.** Drafts only.
- **Does not auto-drain `task_queue/`.** That's Phase 4.5 — the queue files accumulate; iMac task-tracker-manager (or its successor) drains them.
- **Does not modify Attio.** Pipeline-manager owns Attio writes.
- **Does not create project tabs.** Project flag in Slack → Kay creates tab manually if she agrees scope is project-sized.
- **Does not auto-answer research-prompts or run socrates sessions.** It surfaces; Kay or the named target_skill picks them up via `/triage`.
- **Does not aggregate across calls.** One Slack message per call. No EOD digest.

## Failure modes + invariants

- If MCP call fails (auth, network, timeout) → detector logs + exits 0. Timer keeps firing.
- If queue contains stale entries (>30 min old, not processed) → validator flags as RED.
- If Slack webhook fails → log error, mark queue entry `slack_failed: true` but still mark processed (vault + drafts + tasks already landed).
- If Gmail draft creation fails → log error, demote to TASK with note "draft failed, manual send needed".
- If a thought-analysis artifact write fails → log error, surface in Slack with `THOUGHT-WRITE-FAIL:` prefix; downgrade-route the bullet to plain decision-list.

## Validator (mandatory)

`scripts/validate_post_call_analyzer_integrity.py` runs after every Claude exit-0. Self-locating REPO_ROOT works on both iMac (`~/Documents/AI Operations`) and Linux server (`~/projects/Sapling`).

1. Queue dir is empty (all triggers processed) OR all queue entries are <30 min old (still mid-flight from a fresh detector tick)
2. Each processed entry has corresponding vault call note OR explicit failure marker
3. **Thought-analysis artifacts named in `processed/{id}.json`'s `research_prompts_created` / `socrates_questions_created` arrays exist on disk in `brain/inbox/`** (Phase 4 check)
4. No file in `processed/` is older than 30 days (rotate — warn, not fail)

Validator failure → wrapper overrides exit code → Slack alert with "VALIDATOR FAILED" prefix per `feedback_mutating_skill_hardening_pattern.md`.

## Systemd unit pair (server-side, Phase 4)

- `systemd/post-call-analyzer-poll.service` — Type=oneshot, runs `python3 scripts/post_call_analyzer_mcp_poll.py`, EnvironmentFile=`scripts/.env.launchd`
- `systemd/post-call-analyzer-poll.timer` — `OnBootSec=2min`, `OnUnitActiveSec=5min`, `Persistent=true`

Install via `bash scripts/install_systemd_units.sh` then `systemctl --user enable --now post-call-analyzer-poll.timer`.

Logs:
- Detector: `logs/scheduled/post-call-analyzer-mcp-poll-{date}.log`
- Claude run: `logs/scheduled/post-call-analyzer-{date}-{HHMM}.log` (via wrapper)
- Wrapper case in `scripts/run-skill.sh` already routes `post-call-analyzer:on-trigger` → headless prompt + POST_RUN_CHECK validator.

## iMac sidecar (legacy, retired Phase 4.5)

`~/Library/LaunchAgents/com.greenwich-barrow.post-call-analyzer.plist` keeps running unchanged on the iMac during shadow mode. It uses `WatchPaths` on the local Granola cache and writes to the same `queue/` + `processed.json` as the server detector. Both can coexist; whichever detects first wins via the existing-queue-file guard in the MCP detector.

Phase 4.5 (after shadow-mode validation): unload the plist, delete `scripts/post_call_analyzer_poll.py`, drain the leftover task_queue/, retire this row from the architecture table.

## Files owned

| Path | Owned? |
|---|---|
| `scripts/post_call_analyzer_mcp_poll.py` | YES (Phase 4 server detector) |
| `scripts/post_call_analyzer_poll.py` | LEGACY (iMac sidecar, retire Phase 4.5) |
| `scripts/validate_post_call_analyzer_integrity.py` | YES (validator) |
| `systemd/post-call-analyzer-poll.service` | YES |
| `systemd/post-call-analyzer-poll.timer` | YES |
| `.claude/skills/post-call-analyzer/SKILL.md` | YES (this file) |
| `.claude/skills/post-call-analyzer/headless-on-trigger-prompt.md` | YES (Claude prompt) |
| `schemas/vault/research-prompt.yaml` | YES (Phase 4 thought-analysis schema) |
| `schemas/vault/socrates-question.yaml` | YES (Phase 4 thought-analysis schema) |
| `brain/trackers/post-call-analyzer/processed.json` | YES (idempotency ledger) |
| `brain/trackers/post-call-analyzer/queue/*.json` | YES (transient — drained per run) |
| `brain/trackers/post-call-analyzer/processed/*.json` | YES (archive — 30-day rotation) |
| `brain/trackers/post-call-analyzer/task_queue/*.json` | YES (Phase 4 task bucket — Phase 4.5 drains) |
| `brain/calls/*.md` | SHARED (writes new files; existing call-note convention) |
| `brain/inbox/*-research-prompt.md` | YES (Phase 4 thought-analysis output) |
| `brain/inbox/*-socrates-question.md` | YES (Phase 4 thought-analysis output) |
| Excel To Do (task-tracker) | DELEGATES to task-tracker-manager (Phase 4.5) |
| Gmail drafts | DELEGATES to `gog gmail drafts create` |
| Slack `#operations` | OWNED for `[Granola]` prefixed messages |
