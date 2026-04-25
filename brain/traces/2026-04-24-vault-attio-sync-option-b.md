---
schema_version: 1.1.0
date: 2026-04-24
type: trace
today: "[[notes/daily/2026-04-24]]"
task: Architect engagement-notes sync between vault entities and Attio person records
had_human_override: false
importance: high
target: skill:relationship-manager
tags: [date/2026-04-24, trace, topic/attio, topic/vault, pattern/morning-sync-over-webhook, domain/technical]
---

# Decision Trace: Vault→Attio Sync via Morning Run, Not Real-Time Webhook

## Context

Yesterday's XPX 8-card processing produced email drafts in Superhuman but never wrote the corresponding vault entities or Attio enrichment (vault schema validator blocked, deferral never picked up). The deeper architectural problem: when `conference-engagement` collects cards, the Attio person record does NOT yet exist (Attio auto-creates a stub only when an email actually sends or arrives). So the skill cannot write engagement notes to Attio at card-collection time — it can only write them to the vault. Kay's engagement context (the "Joe McConnell archetype" read on Jim, etc.) needs a path into Attio *after* the auto-stub appears.

Two architectures considered for closing this loop:

- **Option A (event-driven):** Attio webhook fires when a new person is auto-created → matches the email to a vault entity with that email → attaches the notes. Real-time sync. Cleanest UX.
- **Option B (morning sync):** Each morning, scan recent vault entities (last 7 days) for any with empty `attio_id` AND a matching email auto-create → attach notes, set source tag, set cadence. Daily run. Slower but uses existing infrastructure.

## Decisions

### Sync architecture
**AI proposed:** Option B — fold the sync into `relationship-manager` which already runs daily during goodmorning.
**Chosen:** Option B (Kay approved without pushback).
**Reasoning:** Three factors. (1) **Lower complexity:** Option A needs new infrastructure — webhook endpoint, auth, retry logic, ordering guarantees, none of which exist today. (2) **Time-decay tolerance:** engagement notes are durable context (weeks to months of relevance), not perishable signals. A 12-hour delay between email-send and Attio-note-attach is invisible to Kay's workflow. (3) **Existing daily infrastructure:** `relationship-manager` already scans vault and Attio every morning; adding one more pass over recent entities is a marginal cost. Option A would require building entirely new plumbing for a use case that doesn't reward real-time.
**Pattern:** #pattern/morning-sync-over-webhook

### Idempotency strategy
**AI proposed:** Note-title check (look for existing note titled `"{source} {date} — engagement context"` before creating).
**Chosen:** Same.
**Reasoning:** Re-running the sync on the same vault entity must not duplicate notes. The note-title check is brittle if Kay manually renames notes, but acceptable for v1 — tighten if duplicates surface in practice.
**Pattern:** #pattern/idempotent-write-by-title-check

### Failure handling for the missing Attio token scope
**AI proposed:** Surface as System Status alert in the morning artifact, log once per day, don't retry repeatedly until Kay re-authorizes scope.
**Chosen:** Same.
**Reasoning:** 403 from missing `notes:read-write` is not a transient error — retrying does nothing. One alert per missing-scope event per day prevents log spam while keeping the issue visible until Kay fixes it at the Smithery / Attio admin level.

## Learnings

- **Default to "fold into existing daily run" before "build a new event-driven pipeline."** Webhooks have hidden costs (auth, retries, ordering, observability) that don't pay for themselves unless real-time is actually needed.
- **The trigger event for "real-time vs daily-sync"** is whether the data has time-decay. Engagement notes don't; pipeline-stage changes Kay needs to act on within hours might.
- **Whenever a skill must defer a write because a downstream record doesn't exist yet, the gap needs a closing-loop sync somewhere.** Otherwise the deferred write silently never lands. Today's diagnosis of the 8-card miss was a direct symptom of an unclosed loop.
- **Future agent instruction:** when designing a skill that depends on a downstream record being created out-of-band (auto-import, email auto-create, OAuth callback), specify the closing-loop sync as part of the skill design, not as an afterthought. Use the daily relationship-manager run as the default landing zone for this pattern.
