---
date: 2026-06-21
type: session-decisions
title: Session Decisions - 2026-06-21
tags: [date/2026-06-21, context, session-decisions, status/done]
---

# Session Decisions - 2026-06-21

## Decisions

- APPROVE: Good Morning Email Orchestration must mirror the dashboard follow-up buckets only: `24-hour thank-yous`, `48-hour follow-ups`, and `EOW follow-ups`.
- REJECT: Generic `Draft review` and `Deal-flow email` rows inside Email Orchestration. Drafts appear only inside a concrete follow-up bucket with recipient/subject/purpose; deal-flow belongs in Deal Aggregator.
- REJECT: Generic unread-email reminders in Good Morning. Emails should surface only when there is a concrete action or analysis recommendation, e.g. budget assessment from Start Virtual financials.
- APPROVE: Tasks & Follow-up must not repeat the To Do list. It may report the open task count, then only surface items not already on the To Do list, post-call analysis candidates, or new routing decisions.
- APPROVE: Dashboard sections come before Meeting Briefs in Good Morning: Email Orchestration, Active Pipeline, Deal Aggregator, C-Suite & Skills, System Health, then Meeting Briefs and Tasks & Follow-up.
- APPROVE: Active Pipeline in Good Morning must match the dashboard engaged-pipeline scope: `Contacted` as `Warmed / Teaser`, plus `NDA`, `Financials Received`, `Submitted LOI`, and `Signed LOI`. Exclude raw `Identified` rows from the active count.
- APPROVE: Deal Aggregator section remains sparse/action-only until the deal-aggregator plumbing review finalizes its dashboard-aligned subsections. Completed source-admin items such as Baton Market should be omitted.
- APPROVE: Sam Hyde / Steuart Botchford and Mike Horowitz briefs are needed for Monday 2026-06-22. Juan brief is already done and Kay will edit it herself.

## Actions Taken

- UPDATED `pipeline-manager` Good Morning format rules for Email Orchestration, Active Pipeline, Deal Aggregator, C-Suite & Skills/System Health ordering, Meeting Brief placement, and Tasks & Follow-up scope.
- UPDATED dashboard pipeline plumbing to expose an explicit engaged pipeline scope and align the dashboard pipeline pages to it.
- RENAMED the Sam Hyde / Steuart Botchford Drive brief from `6.17.26` to `6.22.26`.
- RENAMED the Sam Hyde / Steuart Botchford vault brief to `brain/briefs/2026-06-22-sam-hyde-steuart-botchford-call-2.md` and corrected its date tag.
- VERIFIED the Mike Horowitz brief exists for Monday 2026-06-22 in Drive and vault.
- RAN Good Night task carry-forward for Sunday 2026-06-21: no incomplete Sunday items to move; packed Sunday checked rows to the top.
- SENT no emails.

## Deferred

- DEFER final Deal Aggregator morning-brief layout until the deal-aggregator plumbing review is complete.
- DEFER broad dashboard/product dirty-tree commit review. Several dashboard files were already dirty from other workstreams; do not stage wholesale without review.
- DEFER broad skill updates outside `pipeline-manager` to their owning workstreams unless Kay approves a dedicated skill-evolution commit.
- DEFER runtime snapshot and rollback-snapshot cleanup; classify before staging because many files are generated operational noise or unrelated workstream artifacts.
- DEFER task item `21` from the morning review as `resolve today`; next operating pass should resolve it or identify the exact item if it remains ambiguous.

## Open Loops

- Monday 2026-06-22 morning should not resurface Juan brief prep; Kay already said it is done and she will edit it.
- Monday 2026-06-22 morning can point to the Sam/Steuart and Mike briefs as ready, not ask again whether they are needed.
- Email Orchestration should render only the three follow-up buckets unless a draft is concretely tied to one of those buckets.
- Deal-flow emails from Baton, DealForce/Generational, Flippa, Quiet Light, SMB Deal Hunter, Everingham & Kerr, and DealsX should route to Deal Aggregator, not Email Orchestration.
- Start Virtual EOW report should not be surfaced as `read this email`; surface only if there is a concrete budget/financial assessment action.
- Dashboard active pipeline currently validates as 4 Warmed / Teaser plus 1 Financials item; raw Identified rows should not inflate the Good Morning active-pipeline count.

## Sources Reviewed

- Chief of Staff Daily Operating Rhythm thread: Included.
- Codex thread tools: unavailable after tool search; fallback evidence path used.
- `git status --short --branch`: Included.
- `brain/context/session-decisions-2026-06-19.md`: Included as recent prior closeout style/context.
- `brain/traces/2026-06-19-good-morning-brief-restructure.md`: Included as related trace.
- Task tracker carry-forward output for 2026-06-21: Included.
- Google Drive search results for Sam Hyde / Steuart Botchford and Mike Horowitz briefs: Included.
- Vault brief files for Sam Hyde / Steuart Botchford and Mike Horowitz: Included.
