---
name: Write-capable skills get a Friday-afternoon dry run before launchd activation
description: Skills that mutate shared state (Sheets, Attio, Gmail-send) must pass a manual dry-run on a Friday before being scheduled. Read-only skills ship straight.
type: feedback
originSessionId: 79f2536c-7455-4155-bafd-6653508b83e4
---
**Rule: any skill that MUTATES shared state must pass a manual Friday-afternoon dry-run before being added to launchd or any automation schedule.**

Mutating = writes to Industry Research Tracker (Sheets), Attio, Gmail/Superhuman send, Drive moves/renames, Motion task creation, Slack webhook sends.

Read-only = scans, artifact writes to `brain/`, decision traces, log files. These ship straight.

**Why:** The 2026-04-17 near-miss where a subagent clobbered master-list rows by passing empty `tab_name` to a sheet write was exactly the failure mode this rule guards against. Friday afternoon is the lowest-stakes window of the week (less active pipeline, no JJ calls pending, Kay has Saturday to recover). Per the Harry Liu "Going Deeper with Claude" webinar (Apr 17): *"Don't boil the ocean. Start with Friday afternoon."* Our mutating skills have real reputation and data-integrity blast radius, so the rule has teeth for us.

**How to apply:**

1. **When proposing a new mutating skill or mutating change to an existing skill:** ship a Friday-afternoon dry-run plan first. Kay runs the skill manually, inspects diff, gives go-ahead before launchd is edited.

2. **Dry-run requires:**
   - `--dry-run` or equivalent flag that logs intended mutations without executing
   - Pre-write snapshot of every target (sheet, record) so we can compare before/after
   - Input validation that fails loudly on empty/null keys (learned from 4/17)

3. **Never add a WRITE-capable skill to launchd the same day it was built.** Minimum: one Friday cycle between creation and schedule activation.

4. **Read-only skills ship straight.** Don't add friction where there's no risk. Morning briefing reads, email-intelligence scans, relationship-manager reads — all fine to deploy without this gate.

**Scope exceptions (bypass rule with reason):**
- Critical production fix on a live skill that's already mutating — document and proceed
- Kay explicit override — document and proceed

**Source:** 2026-04-19 Anacapa deck analysis + 2026-04-17 subagent-sheet-write near-miss (see `feedback_subagent_sheet_write_safety`).
