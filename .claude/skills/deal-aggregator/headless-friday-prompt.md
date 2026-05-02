# deal-aggregator — Headless Friday Digest Run

You are running the `deal-aggregator` skill non-interactively under launchd at 6:00 AM ET on Friday with the `--digest-mode` flag. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates inside the run itself (the digest artifact contains YES/NO/DISCUSS lines for Kay's later review — that's expected output, NOT operator-question framing), do not request approvals from the harness, do not wait for permission.

## Idempotency gate (run FIRST, before anything else)

Before reading SKILL.md or doing any work:

1. Compute `TODAY` as today's date in `YYYY-MM-DD` (Eastern Time).
2. Check whether `brain/trackers/weekly/{TODAY}-deal-aggregator-digest.md` already exists.
3. If it exists AND its size is ≥ 200 bytes, **STOP IMMEDIATELY**. Print `DEAL-AGGREGATOR ABORT: weekly digest already exists for {TODAY} — refusing to double-write` to stdout and exit normally (exit 0). Do not re-scan, do not re-Slack, do not append, do not overwrite. A prior attempt (this run's earlier child, or a manual re-fire) already produced the deliverable.
4. If it does not exist (or is < 200 bytes — treat as a corrupt partial), continue to the execution section.

## Mandatory ordering — execute in this exact sequence

This is the **weekly source-productivity digest** path (Phase 2 in SKILL.md). It is distinct from the daily morning run — different reads, different artifact path, different Slack-trigger logic. Do NOT also run the morning daily-scan flow; the regular Friday morning plist (`com.greenwich-barrow.deal-aggregator`) handles that separately at the same 6:00 AM fire.

1. **Read SKILL.md fully** at `.claude/skills/deal-aggregator/SKILL.md`. Follow the SKILL.md `<weekly_digest>` section exclusively. Ignore the daily-scan path — that's for morning/afternoon runs without the `--digest-mode` flag.
2. **Compute the 7-day window:** `window_end = TODAY`, `window_start = TODAY - 7 days` (ET).
3. **Read last 7 days of daily scorecards** from `brain/context/deal-aggregator-scan-{date}.md` (one file per weekday). Missing files = note in digest, continue.
4. **Read last 30 days of fingerprint store** from `brain/context/deal-aggregator-fingerprints.jsonl`. Group matches by source + date for the Source Productivity table.
5. **Read last 7 days of email-scan-results** from `brain/context/email-scan-results-{date}.md`. This feeds the Source Scout subagent's new-source discovery (sender domains).
6. **Read the Sourcing Sheet** (ID `1z8o2obq2mOG9drQ0umCmBk31K3OS2afMNGpVAlbLljw`) — both `General Sources` and `Niche-Specific Sources` tabs. This is the active-source roster the digest reports against.
7. **Run Source Scout subagent** per SKILL.md spec — both sides:
   - **Scouting side:** Enumerate inbox sender domains (last 7 days), cross-reference against Sourcing Sheet, classify any new domains as broker platform / M&A advisory / newsletter / industry publication, web-verify each URL resolves, propose additions. Also scan newsletter body text for AI-marketplace launches and named niche-broker mentions.
   - **Retirement side:** For every Sourcing Sheet source with `Status: Active`, check fingerprint store for last attributed match. If 30+ days silent → run 3 live-checks (URL resolves with GET 200, domain still registered, email-channel status if applicable). Propose retirement only if all 3 live-checks have been performed (passed OR documented why one failed). Per `feedback_test_before_concluding_channel_dead`: never retire on silence alone.
8. **Compute volume stats:** 7-day rolling deals/day average, status (`✅ ≥1/day` / `⚠️ 0.5-0.9/day` / `🔴 <0.5/day`), trend arrows per source row.
9. **Write the digest artifact** at `brain/trackers/weekly/{TODAY}-deal-aggregator-digest.md` matching the SKILL.md weekly_digest template — frontmatter (`date`, `type: tracker`, `title`, `window_start`, `window_end`, `volume_7d_avg`, `volume_status`, `opportunistic_count`, `proposed_additions`, `proposed_retirements`, `tags`), all 6 sections (Source Productivity / Volume Check / **Broker-channel opportunistic deals** / Proposed Additions / Proposed Retirements / Recommended Actions). Empty sections keep their header with "None this week" body. For the new opportunistic section: re-screen the week's daily-scan listings against the OPPORTUNISTIC floor ($1M EBITDA, 12% margin, broad services/SaaS/insurance pool, broker/intermediary-curated source per `feedback_broker_channel_opportunistic_floor`) and list each match with one-line teaser per the SKILL.md template.
10. **Slack-trigger logic — silence = healthy:**
    - IF `proposed_additions ≥ 1` OR `proposed_retirements ≥ 1` OR `volume_status == 🔴` → POST to `SLACK_WEBHOOK_OPERATIONS` with one-line summary + link to digest file path.
    - ELSE (zero proposals AND volume healthy) → **DO NOT Slack**. Silent digest is the correct behavior on a healthy week.
11. **NO auto-writes to the Sourcing Sheet.** All proposals stay in the digest file awaiting Kay's approval. Sheet write is a separate post-approval invocation.
12. **Exit normally** (exit 0).

## What success looks like

- Digest exists at `brain/trackers/weekly/{TODAY}-deal-aggregator-digest.md`, ≥ 200 bytes, has frontmatter + all 5 required section headers.
- Source Productivity table has one row per source on the Sourcing Sheet (General + Niche tabs combined, Active status only).
- Each proposed addition includes: name, category, URL, rationale, recommended tab, access method, RECOMMEND→YES/NO/DISCUSS line.
- Each proposed retirement includes: name, days silent, 3 live-check results, RECOMMEND→YES/NO/DISCUSS line.
- Trend arrows populated via prior-week comparison (prior digest file or prior 7-day fingerprint window).
- Slack ping sent ONLY if there's at least one decision-worthy item (proposal or critical volume).
- No writes to the Sourcing Sheet.
- No double-write if a prior child already produced today's digest.

## Forbidden in headless mode

- Asking the user anything ("would you like me to...", "should I proceed...", "do you want me to...").
- Presenting operator-decision gates **outside the digest file body**. The digest file's `## 5. Recommended Actions` section legitimately contains RECOMMEND/YES/NO/DISCUSS lines for Kay's later async review — that's expected output. The forbidden pattern is the Claude run itself emitting RECOMMEND→YES/NO/DISCUSS to the harness as if waiting for an answer (the 4/28 morning incident).
- Meta-commentary about the run state, retries, parallel children, or wrapper attempts. The wrapper is responsible for retry logic; the skill body just executes.
- Re-firing or "monitoring" — you are the run, you don't observe one. If the idempotency gate fires, you abort cleanly; do not announce that you'll watch for completion.
- Auto-writing to the Sourcing Sheet. Hard requirement: every proposal awaits Kay's explicit approval.
- Halting on a single source failure — degrade gracefully, log the failure in the digest, continue.
- Slacking on a healthy silent week — `proposed_additions = 0 AND proposed_retirements = 0 AND volume_status != 🔴` means no Slack ping. Silence is the correct deliverable.
- Running the daily morning-scan flow — that's a separate plist firing at the same 6 AM time. This run is digest-only.

## Failure handling

- **Sourcing Sheet unreachable** → fall back to last known source list cached in vault context; note `sourcing_sheet_source: cached` in digest frontmatter; continue.
- **Fingerprint store missing or empty** → write digest with all sources showing 0 matches and "no fingerprint data" note in Source Productivity section; continue.
- **A daily scan artifact missing for a day in the window** → note the gap in the digest's Volume Check section; compute average over available days only; continue.
- **Source Scout web-verify fails for a candidate addition** → drop that candidate (don't propose unverified sources); log in digest; continue.
- **Live-check fails for a retirement candidate** → keep the source on the active roster, log "live-check failed: {reason}" in digest's Proposed Retirements section as evidence of due diligence; continue. Never retire on silence alone.

The digest is the deliverable. As long as it lands at today's path with frontmatter and the 5 section headers, the run succeeded.

## Why this prompt exists

Bare `claude -p '/deal-aggregator --digest-mode'` invocations under launchd risk the operator-question failure mode (4/28 incident: morning run emitted `RECOMMEND: Let attempt 2 run, monitor for artifact (~45 min) → YES / NO / DISCUSS` instead of executing). This prompt forbids that path and adds a strict idempotency gate so retried digest runs cannot double-write or double-Slack. The digest mode also has a unique nuance: RECOMMEND/YES/NO/DISCUSS lines ARE expected output (in the digest file body) but FORBIDDEN as run-level meta-output to the harness — this prompt clarifies the distinction explicitly.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Templated on `headless-morning-prompt.md`.
