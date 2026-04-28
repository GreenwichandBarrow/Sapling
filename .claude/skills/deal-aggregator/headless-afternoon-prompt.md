# deal-aggregator — Headless Afternoon Run

You are running the `deal-aggregator` skill non-interactively under launchd at 2:00 PM ET (Mon-Fri) with the `--afternoon` flag. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals, do not wait for permission.

## Idempotency gate (run FIRST, before anything else)

Before reading SKILL.md or doing any work:

1. Compute `TODAY` as today's date in `YYYY-MM-DD` (Eastern Time).
2. Check whether `brain/context/deal-aggregator-scan-{TODAY}-afternoon.md` already exists.
3. If it exists AND its size is ≥ 200 bytes, **STOP IMMEDIATELY**. Print `DEAL-AGGREGATOR ABORT: afternoon artifact already exists for {TODAY} — refusing to double-write` to stdout and exit normally (exit 0). Do not re-scan, do not re-Slack, do not append, do not overwrite. A prior attempt (this run's earlier child, or a manual re-fire) already produced the deliverable.
4. If it does not exist (or is < 200 bytes — treat as a corrupt partial), continue to the execution section.

The afternoon artifact is **separate from the morning artifact**. Never overwrite `brain/context/deal-aggregator-scan-{TODAY}.md` (morning) with afternoon output — they coexist, distinct files, distinct deliverables.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/deal-aggregator/SKILL.md`. This is the afternoon (top-up) run — `--afternoon` flag — so follow the SKILL.md "Afternoon Run (`--afternoon` flag)" path: lightweight rescan of email channel + time-sensitive platforms only. Skip full Channel 1 + 3 scans (morning run already covered those).
2. **Re-read buy-boxes** (Services / Insurance / SaaS Google Doc IDs in SKILL.md). Live read — Kay may have edited during the day.
3. **Re-read active niches** from Industry Research Tracker WEEKLY REVIEW tab (sheet ID in SKILL.md). Kay may have toggled niche statuses since morning.
4. **Read** `brain/context/email-scan-results-{TODAY}.md` for any new email-inbound deals (CIMs, broker blasts, intro forwards) that landed after the morning email-intelligence run.
5. **Rescan time-sensitive platforms only:** Rejigg (afternoon listings), Flippa (afternoon updates), Everingham & Kerr (afternoon blasts). Skip the full broker-platform sweep — morning run covered those. Channel 4 (association deal boards) skipped in afternoon run.
6. **Apply buy-box filters** per the Data Availability Rule (missing data ≠ rejection).
7. **Fingerprint dedup** every match via `scripts/deal-aggregator-fingerprint.sh` against `brain/context/deal-aggregator-fingerprints.jsonl` (30-day TTL). Skip Slack post for any match whose fingerprint already exists — this catches morning-run dupes.
8. **Slack-post each new match** to `#active-deals` per SKILL.md format (one message per deal).
9. **Write the artifact** at `brain/context/deal-aggregator-scan-{TODAY}-afternoon.md` matching the SKILL.md "Results File" template — frontmatter (`date`, `deals_found`, `sources_scanned`, `sources_blocked_verified`, `sources_blocked_single_attempt`, `email_deals`), all section headers (Deals Surfaced / Email Inbound Deals / Near Misses / Source Scorecard / Volume Check). Empty sections keep their header with "None today" body. Source Scorecard rows = the time-sensitive platforms you actually scanned this run (Rejigg / Flippa / Everingham & Kerr / email channel), not all sources.
10. **Exit normally** (exit 0).

## What success looks like

- Afternoon artifact exists at `brain/context/deal-aggregator-scan-{TODAY}-afternoon.md`, ≥ 200 bytes, has frontmatter + all 5 required section headers.
- Source Scorecard has one row per time-sensitive source actually scanned this run.
- New matches Slack-posted to `#active-deals` (idempotent — fingerprint store catches morning-run dupes).
- Morning artifact (`brain/context/deal-aggregator-scan-{TODAY}.md`) is untouched.
- No double-write if a prior child already produced today's afternoon artifact.

## Forbidden in headless mode

- Asking the user anything ("would you like me to...", "should I proceed...", "do you want me to...").
- Presenting RECOMMEND / YES / NO / DISCUSS framings or any operator-decision gate.
- Meta-commentary about the run state, retries, parallel children, or wrapper attempts. The wrapper is responsible for retry logic; the skill body just executes.
- Re-firing or "monitoring" — you are the run, you don't observe one. If the idempotency gate fires, you abort cleanly; do not announce that you'll watch for completion.
- Halting on a single source failure — degrade gracefully, mark the source `blocked (verified)` or `blocked (single-attempt)` in the scorecard, continue.
- Skipping the artifact write because "nothing material today" — always write the artifact, even if all sections are empty.
- Overwriting the morning artifact (`-{TODAY}.md` without the `-afternoon` suffix). Morning and afternoon are separate deliverables.
- Running a full Channel 1 + 3 sweep — that was the morning run's job. Afternoon is a top-up, not a re-run.

## Failure handling

- **Buy-box doc unreachable** → use last cached version if present, write a note in the artifact's frontmatter (`buy_box_source: cached`); do NOT exit non-zero.
- **Industry Research Tracker unreachable** → fall back to last known active-niche list cached in vault context; write a note in the artifact; do NOT exit non-zero.
- **email-scan-results artifact missing for today** → write artifact with `email_deals: 0` and a Near Misses row noting the gap; continue.
- **Single source blocks (HTTP 403, timeout, Cloudflare)** → mark blocked in scorecard, continue scanning other sources.
- **All time-sensitive sources block** → still write the artifact with a fully populated scorecard (every scanned source as `blocked`); the artifact existing is the deliverable, the scorecard tells the operator what failed.
- **Morning artifact missing for today** → not your problem; the afternoon run executes regardless. Note `morning_artifact_missing: true` in afternoon frontmatter for diagnostics, continue.

The afternoon artifact is the deliverable. As long as it lands at today's afternoon path with frontmatter and the 5 section headers, the run succeeded.

## Why this prompt exists

Bare `claude -p '/deal-aggregator --afternoon'` invocations under launchd risk the operator-question failure mode (4/28 incident: morning run emitted `RECOMMEND: Let attempt 2 run, monitor for artifact (~45 min) → YES / NO / DISCUSS` instead of executing the scan). This prompt forbids that path and adds a strict idempotency gate so retried afternoon runs cannot double-write or double-Slack.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Templated on `headless-morning-prompt.md`.
