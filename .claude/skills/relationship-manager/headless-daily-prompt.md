# relationship-manager — Headless Daily Run

You are running the `relationship-manager` skill non-interactively under launchd at 7am ET. There is no human in the loop. Do not ask clarifying questions, do not present YES/NO/DISCUSS gates, do not request approvals.

## Mandatory ordering — execute in this exact sequence

1. **Read SKILL.md fully** at `.claude/skills/relationship-manager/SKILL.md`.
2. **Pull source data** in parallel where possible:
   - Attio People (cadence, last_interaction, owner status) — if MCP returns 401 or `hasAttioWorkspaceId: false`, fall back to local cache + Gmail signal-counting. Add a "System Status Alerts" entry naming the failure mode; do NOT halt.
   - Recent Gmail traffic for last_interaction inference
   - Vault `brain/calls/` and `brain/entities/` for engagement signals
   - `brain/context/session-decisions-{previous-workday}.md` for action-already-taken verification
3. **Process per SKILL.md sections**: nurture cadence monitoring → action-already-taken verification → People record management → vault→Attio sync → warm intro tracking.
4. **Write the artifact** at `brain/context/relationship-status-{YYYY-MM-DD}.md` matching the SKILL.md "Output Artifact" template — frontmatter (`date`, `type: relationship-status`), all section headers (omit body if section is empty but keep the header with "None — no X").

## What success looks like

- Artifact exists at today's date, ≥200 bytes, has frontmatter + at least one section header.
- Attio writes attempted; failures gracefully recorded in "System Status Alerts" (not silently dropped).
- Action-already-taken verification suppressed contacts where Kay's outbound landed yesterday (no double-surfacing).

## Forbidden in headless mode

- Asking the user anything.
- Halting on Attio MCP failures — graceful-degrade, keep producing the artifact.
- Drafting outreach (that's outreach-manager's job — surface targets only).
- Presenting RECOMMEND / YES / NO / DISCUSS framings.
- Skipping the artifact write because "nothing material today" — always write the artifact, even if all sections are "None".

## Failure handling

If Attio reads/writes fail (401, network, timeout):
- Continue with cached + Gmail-only data.
- Record exact failure mode in "System Status Alerts" section so pipeline-manager surfaces it as 🔴 broken-system.
- Do NOT exit non-zero — the artifact is the deliverable; Attio sync is downstream.

If Gmail or vault reads fail:
- Retry once.
- If still failing, write a minimal artifact with "System Status Alerts" describing the gap and exit normally.

The wrapper-side validator (`scripts/validate_relationship_manager_integrity.py`) verifies artifact existence + structure. Attio write success is intentionally NOT validated at the wrapper layer — that's pipeline-manager's job to surface as a system status.

## Why this prompt exists

Bare `claude -p '/relationship-manager'` invocations under launchd risk the silent-exit-0 failure mode. This prompt forbids that path and codifies the graceful-degrade pattern for Attio MCP outages.

Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead `ai-ops-jrj.4`.
