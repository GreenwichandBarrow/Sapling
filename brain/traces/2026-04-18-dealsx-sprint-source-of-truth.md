---
schema_version: 1.1.0
date: 2026-04-18
type: trace
title: "DealsX Sprint Composition — Source-of-Truth Hierarchy"
tags: ["date/2026-04-18", "trace", "topic/source-of-truth", "topic/dealsx-sprint", "topic/vault-vs-drive", "person/kay-schneider", "person/sam-singh", "company/dealsx"]
people: ["[[entities/kay-schneider]]", "[[entities/sam-singh]]"]
companies: ["[[entities/dealsx]]"]
---

# Trace: DealsX Sprint Composition Source-of-Truth

## Trigger

On 4/18, Kay asked what niches were given to DealsX for the current sprint (driven by the Saltoun software compression signal → wanted to check the sprint wasn't over-indexed on software). Claude answered three times, wrong each time in a different way, before Kay instructed to read the authoritative Drive file.

**Three wrong answers in sequence:**
1. "4 niches, all software (100% software)" — sourced from Sam Singh 4/15 call note which listed 4 go-to-market macros. Not the sprint submission.
2. "13 niches, 11 software (85% software)" — sourced from Industry Research Tracker WEEKLY REVIEW tab Col D = "DealsX Email." This is routing intent, not sprint submission.
3. "6 niches, 4 software / 2 services (67% software)" — correct, sourced from the actual DealsX Verticals Drive sheet (1n5zMVL4...) that Kay submitted to Sam.

## Decision

Establish a source-of-truth hierarchy for questions about what DealsX is actively building against:

1. **Primary source:** `Greenwich & Barrow / DealsX Industry Verticals` Drive sheet (ID: `1n5zMVL4V0mk0Mv0b2pRzl5QZDINevmuL09PwEvMOsPg`) — what Kay submitted, what Sam is building lists against.
2. **Secondary source:** Industry Research Tracker Col D "DealsX Email" — routing **intent**, not sprint **submission**. Shows which niches are eventually bound for DealsX, not which are in the current sprint.
3. **Tertiary source:** Sam Singh call notes — contain Sam's go-to-market macro framing (bucket names like "Specialty Healthcare SaaS"), not the per-niche submission.

For any sprint-composition question: read the Drive sheet first. The tracker and call notes are supporting context only.

## Alternatives Considered

1. **Trust the tracker as source of truth.** Standard CLAUDE.md pattern ("always read the tracker sheet"). Works for niche status, outreach channel, score — fails for "what's in the current DealsX sprint" because Col D reflects intent, not submission.
2. **Trust the call note.** Felt authoritative because it was recent and Sam confirmed. Sam's framing was macro-level; the actual sprint has finer-grained niches under each macro.
3. **Always read the operational Drive file first for operational questions** — chosen. The Drive file is Sam's working input. Everything else is derivative.

## Reasoning

The core mistake was assuming one source-of-truth rule applies universally. CLAUDE.md says "always read the tracker sheet" for niche status. That was correct advice for its intended scope but over-applied here. The DealsX sprint is an operational artifact living in the partner's workspace (the Verticals sheet in Drive), not in the Industry Research Tracker.

**Rule generalization:** when asking what an external partner is actively building against, read the artifact the partner is working from. Tracker = G&B internal strategy state. Drive Verticals sheet = Kay↔Sam contract.

## Why This Trace Matters

Without this trace, the next time any agent is asked "what's DealsX working on," the pattern is:
- Read Col D in tracker → wrong answer (routing intent)
- Read Sam call note → wrong answer (macro framing)
- Three-attempt correction required, Kay burns cycles pointing to the right file

With this trace, any agent on first attempt reads the DealsX Verticals Drive sheet. One read, correct answer.

## Key Insight

**Source-of-truth is per-question, not per-system.** The tracker is source of truth for *niche status* and *outreach channel assignment*. The DealsX Verticals Drive sheet is source of truth for *what Sam is building against this sprint*. Call notes are source of truth for *what was discussed*, not *what was submitted*.

**Rule for agents:** if the question is "what is partner X actually doing right now," find the artifact partner X is working from and read that first. Strategy state in vault/tracker is derivative.

**Applies beyond DealsX:** same pattern holds for JJ's daily call logs (JJ's call log is source of truth for what JJ actually dialed, not tracker assignment), for bookkeeper reports (Start Virtual's EOW PDF is source of truth for recorded transactions, not budget-manager vault state), etc.
