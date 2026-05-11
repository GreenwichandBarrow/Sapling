# email-intelligence - Headless Weekday Run

You are running the `email-intelligence` skill non-interactively under systemd at 7am ET (Mon-Fri). There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals, do not wait for permission.

## Mandatory ordering - execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/email-intelligence/SKILL.md`. Internalize every `<*_auto_trigger>` block and the `<artifact>` schema.
2. **Pull source data:**
   - Inbound Gmail (`gog gmail search "newer_than:2d label:INBOX" --json --max 50`)
   - Outbound Gmail (`gog gmail search "from:kay.s@greenwichandbarrow.com newer_than:2d" --json --max 50`)
   - Gmail drafts (`gog gmail draft list --json`)
   - Granola transcripts via MCP for any meetings since last run
   - `brain/context/session-decisions-{previous-workday}.md` for cross-check before flagging drafts as stale
3. **Per-email classification + urgent side effects.** Walk the inbound list. For each email:
   - Classify (DIRECT / BLAST / NEWSLETTER) per `<deal_flow_classification>`.
   - If CIM detected → fire `<cim_auto_trigger>` 4-step pipeline immediately (folder, file, inbox, deal-evaluation invoke). Do not defer.
   - If Active Deals stage-3-through-9 match → fire `<active_deal_fast_path>` immediately.
   - If bookkeeper P&L detected (sender `*@startvirtual.com`, OR subject contains "Management Report" + month/year, OR attachment filename contains "Profit and Loss" / "Balance Sheet" / "P&L" / "Management Report") → fire `<bookkeeper_pl_auto_trigger>` 4-step pipeline. **CRITICAL ordering below.**
   - If NDA/CIM attachment from broker → create auto-acknowledgment Gmail draft per `<auto_ack_drafts>`.
   - If broker BLAST with broker-signal keywords → run per-listing extraction per `<broker_blast_listing_extraction>`.
   - If intro detected → create entity stub if missing + inbox item per `<intro_detection>`.
4. **Bookkeeper P&L chain - mandatory imperative ordering.** If ANY inbound email this run matched the bookkeeper P&L detection signal above, you MUST execute these three steps before writing the email-scan-results artifact:
   - **4a. File PDFs** to `BOOKKEEPING / MONTHLY REPORTING / {MONTH YEAR}` Drive subfolder (parent folder ID `1Z__A8AXWBCwQN7x1nK2fqaqhVKlJBJOb`). Create the month subfolder if it doesn't exist.
   - **4b. Write the trigger inbox item** to `brain/inbox/{YYYY-MM-DD}-{month}-management-report-budget-trigger.md` with `urgency: trigger` and tags `topic/bookkeeper-pl-received`, `trigger/budget-manager-monthly`. Use the inbox schema (`schemas/vault/inbox.yaml`).
   - **4c. Invoke `budget-manager monthly` IN THIS SESSION.** Pass `period: {YYYY-MM}` for the detected month (the month named in Anthony's email subject / attachment). Wait for budget-manager to complete its 3-subagent pipeline. Do NOT defer to a later run, do NOT just create the inbox item and stop, do NOT surface this as a Decision for Kay's approval - per `memory/feedback_bookkeeper_pl_auto_trigger_budget_manager.md` the trigger is deterministic and auto-firing. Forbidden pattern: writing only the inbox item and skipping the budget-manager invocation. That is the exact gap the March 2026 run hit (file landed 2026-04-29 but budget-manager never ran).
   - **4d. Log the chain.** Emit the literal string `BOOKKEEPER-PL-CHAIN: invoked budget-manager monthly for period {YYYY-MM}` to stdout (the wrapper log) so the post-run validator can confirm the chain fired. If budget-manager returned non-zero or did not produce `brain/outputs/{YYYY-MM-DD}-budget-report-{month-year}.md`, emit `BOOKKEEPER-PL-CHAIN: FAILED for period {YYYY-MM} reason: {brief}` and continue with artifact write - surface the failure in the artifact's Actionable Items section so pipeline-manager flags it.
5. **Smoke-test path (no-op when env unset).** If env var `EMAIL_INTEL_DRY_RUN_BUDGET_CHAIN` is set to `1`, skip the actual budget-manager invocation in step 4c but still emit `BOOKKEEPER-PL-CHAIN: dry-run for period {YYYY-MM}` to stdout. Used by smoke tests to verify wiring without actually re-running budget-manager.
6. **Write the artifact** at `brain/context/email-scan-results-{YYYY-MM-DD}.md` matching the SKILL.md `<artifact>` schema - all 8 sections present (sections 7 broker-BLAST listings and 8 auto-drafts get explicit "None" body when empty, never omitted).
7. **Exit normally** (exit 0).

## What success looks like

- Artifact exists at today's date, ≥200 bytes, has frontmatter + all 8 required section headers.
- Every CIM, Active Deal fast-path, and bookkeeper P&L trigger detected was processed in-session, not deferred.
- If a bookkeeper P&L email was detected: `BOOKKEEPER-PL-CHAIN:` line present in the log AND `brain/outputs/{run-date}-budget-report-{month-year}.md` exists (unless dry-run env set).
- Granola meetings ingested to `brain/calls/` (idempotent by call_id).
- Slack pings fired for CIM and Active Deal fast-path with HTTP 200.

## Forbidden in headless mode

- Asking the user anything ("would you like me to...", "should I run budget-manager...", "do you want me to proceed...").
- Presenting RECOMMEND / YES / NO / DISCUSS framings for any auto-trigger pathway. The auto-triggers (CIM, Active Deal Fast-Path, bookkeeper P&L) are deterministic - they fire without approval per their SKILL.md sections.
- **Creating the bookkeeper trigger inbox item and stopping there.** Step 4c (invoke budget-manager) is mandatory, not optional. Skipping it is the root failure this prompt exists to prevent.
- Surfacing the bookkeeper P&L trigger as a Decision item in any artifact section. The trigger is wired; only the OUTPUT (variance flags, runway change) is decision-worthy and that lives in budget-manager's own artifact.
- Halting on a single MCP failure (Granola 401, Attio timeout) - graceful-degrade, log the failure mode in the artifact's Actionable Items section, continue.
- Skipping the artifact write because "nothing material today" - always write the artifact, even if every section is "None".
- Overwriting an existing same-day artifact silently - if `brain/context/email-scan-results-{TODAY}.md` already exists with ≥200 bytes, abort cleanly and emit `EMAIL-INTEL ABORT: artifact already exists for {TODAY}` (idempotency for retry safety).

## Failure handling

- **Gmail API 401** → exit non-zero immediately so the wrapper Slack-alerts; do NOT silently proceed with stale data.
- **Granola MCP unavailable** → continue without Granola ingestion, note in artifact's Actionable Items, exit 0.
- **Drive folder creation fails on bookkeeper P&L step 4a** → still write inbox item + invoke budget-manager (it reads from email attachment in worst case), note the Drive failure in the artifact.
- **budget-manager invocation fails (step 4c)** → log `BOOKKEEPER-PL-CHAIN: FAILED ...`, surface in artifact, continue with rest of email-intelligence run, exit 0. The wrapper-level validator catches this and Slack-alerts.
- **Attio MCP 401** → CIM auto-trigger Attio write skipped, surfaced in artifact under Actionable Items so pipeline-manager flags it; continue.

## Why this prompt exists

Bare `claude -p '/email-intelligence'` invocations under systemd produced the silent-skip failure mode on the bookkeeper P&L auto-trigger: the agent created the trigger inbox item (SKILL.md step 2) but never invoked `budget-manager monthly` (SKILL.md step 3). March 2026 P&L landed 2026-04-28, inbox item written 2026-04-29, but no budget-manager output existed 13 days later. This prompt makes step 3 imperative, adds a stdout log line for validator gating, and forbids the "create-inbox-only and stop" pattern.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md` + `memory/feedback_bookkeeper_pl_auto_trigger_budget_manager.md`.
