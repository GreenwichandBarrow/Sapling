---
name: email-orchestrator
description: "Coordinates G&B email-adjacent workflows across email-intelligence, pipeline-manager, relationship-manager, task-tracker-manager, deal-aggregator, and Good Morning. Use when email signals need to be routed, summarized, drafted, approved, or exposed to the dashboard. Never sends email."
archetype: router
context_budget:
  skill_md: 450
  max_references: 8
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
---

# Email Orchestrator

## Purpose

Email Orchestrator is the traffic controller for email-adjacent work. It does not replace the source skills:

- `email-intelligence` owns Gmail/Granola scanning and writes `brain/context/email-scan-results-{date}.md`.
- `pipeline-manager` owns pipeline-stage recommendations and approved Attio updates.
- `relationship-manager` owns relationship and nurture status.
- `task-tracker-manager` owns approved task writes.
- `deal-aggregator` owns deal-source classification and funnel quality.
- `goodmorning` owns the final decisions-only morning surface.

Use this skill when the work spans two or more of those systems, when Kay asks what email means operationally, or when the dashboard needs one coherent status from multiple email-derived artifacts.

## Hard Safety Boundary

Never send email. Never run send, draft-send, forward, autoreply, schedule-send, or equivalent commands/API calls.

Allowed:

- Read Gmail through `gog` with `--gmail-no-send`.
- Create Gmail drafts only when the command is explicitly draft-only and includes `--gmail-no-send`.
- Prepare draft text in chat.
- Write routing/status artifacts.
- Recommend that Kay review or send something herself.

If a requested action requires sending, stop and surface it as a blocker.

## Credential Rule

Before any op-backed CLI or REST call:

```bash
source /home/ubuntu/projects/Sapling/scripts/op-env.sh
```

Scheduled jobs must use 1Password-backed secrets. MCP tools are optional conveniences and must not be required for scheduled execution.

## Standard Workflow

1. Read the latest `brain/context/email-scan-results-{date}.md`.
2. Check freshness and source status. If today's email scan is missing or stale, route first to `email-intelligence`.
3. Classify each email-derived item into one owner:
   - Deal flow or broker listing -> `deal-aggregator`
   - Active deal stage evidence -> `pipeline-manager`
   - Relationship/nurture/follow-up -> `relationship-manager`
   - Task candidate -> `task-tracker-manager` after Kay approval
   - Morning decision -> `goodmorning`
4. Collapse duplicates by entity, thread, and decision.
5. Produce a decisions-only summary for Kay when human approval is needed.
6. Write dashboard status to `brain/context/email-orchestrator-status.json`.

## Dashboard Status Contract

Write JSON with this shape:

```json
{
  "fetched_at": "2026-06-14T12:00:00-04:00",
  "source_artifact": "brain/context/email-scan-results-2026-06-14.md",
  "source_status": "ok|missing|stale|error",
  "drafts_pending": 0,
  "send_blockers": 0,
  "deal_items": 0,
  "pipeline_items": 0,
  "relationship_items": 0,
  "task_candidates": 0,
  "needs_kay": [],
  "blocked": []
}
```

`send_blockers` is a safety metric: it counts items that would require sending and therefore must stop for Kay review.

## Output Rules

- Keep Kay-facing output brief and decision-oriented.
- Do not dump raw Gmail JSON, raw HTML, or long email bodies.
- For sensitive evidence, cite bounded snippets or source metadata only.
- If the source artifact is missing, do not invent email status. Say it is missing and route to `email-intelligence`.
- If a task is ambiguous, present it for clarification rather than writing it to a tracker.
