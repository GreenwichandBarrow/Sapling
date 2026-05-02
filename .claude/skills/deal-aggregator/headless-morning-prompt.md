# deal-aggregator — Headless Morning Run

You are running the `deal-aggregator` skill non-interactively under launchd at 6:00 AM ET (Mon-Fri). There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals, do not wait for permission.

## Idempotency gate (run FIRST, before anything else)

Before reading SKILL.md or doing any work:

1. Compute `TODAY` as today's date in `YYYY-MM-DD` (Eastern Time).
2. Check whether `brain/context/deal-aggregator-scan-{TODAY}.md` already exists.
3. If it exists AND its size is ≥ 200 bytes, **STOP IMMEDIATELY**. Print `DEAL-AGGREGATOR ABORT: artifact already exists for {TODAY} — refusing to double-write` to stdout and exit normally (exit 0). Do not re-scan, do not re-Slack, do not append, do not overwrite. A prior attempt (this run's earlier child, or a manual re-fire) already produced the deliverable.
4. If it does not exist (or is < 200 bytes — treat as a corrupt partial), continue to the execution section.

This gate prevents the 4/27 race-condition failure mode (two parallel scans clobbering the artifact + double-Slacking matches).

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/deal-aggregator/SKILL.md`. This is the morning (full) run — no `--afternoon` or `--digest-mode` flag — so follow the SKILL.md "Morning run (default, no flag)" path: full Channel 0a/0b/0c load, full Channel 1 + 3 scan, read `brain/context/email-scan-results-{TODAY}.md`, write `brain/context/deal-aggregator-scan-{TODAY}.md`.
2. **Load buy-boxes** (Services / Insurance / SaaS Google Doc IDs in SKILL.md). Live read every run — never cache.
3. **Load active niches** from Industry Research Tracker WEEKLY REVIEW tab (sheet ID in SKILL.md).
4. **Read** `brain/context/email-scan-results-{TODAY}.md` for email-inbound deals (CIMs, broker blasts, intro forwards).
5. **Scan all configured sources** (Channels 1 + 3 for morning run; Channel 4 association deal boards if scheduled). Every source listed as `active` in the Sourcing Sheet must produce a Source Scorecard row — no exceptions.
6. **Apply buy-box filters** per the Data Availability Rule (missing data ≠ rejection).
7. **Fingerprint dedup** every match via `scripts/deal-aggregator-fingerprint.sh` against `brain/context/deal-aggregator-fingerprints.jsonl` (30-day TTL). Skip Slack post for any match whose fingerprint already exists.
8. **Slack-post each new match** to `#active-deals` per SKILL.md format (one message per deal).
9. **Write the artifact** at `brain/context/deal-aggregator-scan-{TODAY}.md` matching the SKILL.md "Results File" template — frontmatter (`date`, `deals_found`, `sources_scanned`, `sources_blocked_verified`, `sources_blocked_single_attempt`, `email_deals`), all section headers (Deals Surfaced / Email Inbound Deals / Near Misses / Source Scorecard / Volume Check). Empty sections keep their header with "None today" body.
10. **Exit normally** (exit 0).

## What success looks like

- Artifact exists at today's date, ≥ 200 bytes, has frontmatter + all 5 required section headers.
- Source Scorecard has one row per `active` source in the Sourcing Sheet.
- New matches Slack-posted to `#active-deals` (idempotent — fingerprint store catches re-runs).
- No double-write if a prior child already produced today's artifact.

## Forbidden in headless mode

- Asking the user anything ("would you like me to...", "should I proceed...", "do you want me to...").
- Presenting RECOMMEND / YES / NO / DISCUSS framings or any operator-decision gate.
- Meta-commentary about the run state, retries, parallel children, or wrapper attempts. The wrapper is responsible for retry logic; the skill body just executes.
- Re-firing or "monitoring" — you are the run, you don't observe one. If the idempotency gate fires, you abort cleanly; do not announce that you'll watch for completion.
- **Detecting another run in-flight and surfacing it as a decision.** If you see a `claude` process, a wrapper PID, or a parallel attempt while doing your idempotency-gate check, you do NOT pause and ask the operator what to do. The idempotency gate (artifact path check, ≥200 bytes) is the ONLY arbiter. If the artifact exists with content → you abort silently. If it doesn't → you execute. There is no third "let me ask Kay if I should proceed" branch. (Roots: 4/27 + 4/28 incidents where the run emitted `RECOMMEND: Let attempt 2 run, monitor for artifact` instead of executing.)
- Halting on a single source failure — degrade gracefully, mark the source `blocked (verified)` or `blocked (single-attempt)` in the scorecard, continue.
- Skipping the artifact write because "nothing material today" — always write the artifact, even if all sections are empty.
- Overwriting an existing same-day artifact (idempotency gate above prevents this).

## Failure handling

- **Buy-box doc unreachable** → use last cached version if present, write a note in the artifact's frontmatter (`buy_box_source: cached`); do NOT exit non-zero.
- **Industry Research Tracker unreachable** → fall back to last known active-niche list cached in vault context; write a note in the artifact; do NOT exit non-zero.
- **email-scan-results artifact missing for today** → write artifact with `email_deals: 0` and a Near Misses row noting the gap; continue.
- **Single source blocks (HTTP 403, timeout, Cloudflare)** → mark blocked in scorecard, continue scanning other sources.
- **All sources block** → still write the artifact with a fully populated scorecard (every source as `blocked`); the artifact existing is the deliverable, the scorecard tells the operator what failed.

The artifact is the deliverable. As long as it lands at today's path with frontmatter and the 5 section headers, the run succeeded.

## Why this prompt exists

Bare `claude -p '/deal-aggregator'` invocations under launchd risk the operator-question failure mode (4/28 incident: agent emitted `RECOMMEND: Let attempt 2 run, monitor for artifact (~45 min) → YES / NO / DISCUSS` instead of executing the scan, while a prior child was hung). This prompt forbids that path and adds a strict idempotency gate so retried runs cannot double-write the artifact or double-Slack matches.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Templated on `relationship-manager/headless-daily-prompt.md`.
