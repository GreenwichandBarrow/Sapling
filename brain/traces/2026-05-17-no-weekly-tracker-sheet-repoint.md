---
schema_version: 1.1.0
date: 2026-05-17
type: trace
today: "[[brain/context/continuation-2026-05-17-2]]"
task: Dashboard data-source diagnosis — task 9 (repoint to weekly-tracker Sheet)
had_human_override: false
review_status: pending
importance: high
target: process
tags: [date/2026-05-17, trace, topic/dashboard, topic/weekly-tracker, pattern/check-existing-impl-before-rebuild, status/done]
---

# Decision Trace: Do NOT Repoint Dashboard to weekly-tracker Google Sheet

## Context
Task 9 originally scoped: make the weekly-tracker Google Sheet the dashboard's system of record. The weekly-tracker skill writes activity metrics to a sheet, so pointing the dashboard at that sheet looks like the clean canonical-source move. The dashboard's pipeline/channel panels were stale, which made "give them a real backing sheet" attractive.

## Decisions

### Reject the sheet-repoint; the M&A Analytics page already implements the archive
**AI proposed (per original task scoping):** Repoint dashboard data layer to read the weekly-tracker Sheet as canonical weekly state.
**Chosen:** Reject. The M&A Analytics page already implements a 9-snapshot weekly archive sourced from vault + Attio. The weekly-tracker Sheet has never been populated because the weekly-tracker skill has never actually run.
**Reasoning:** Building a sheet-source data layer would duplicate working infrastructure that already exists one page over. The premise behind task 9 — "there's no weekly archive" — was false; the gap was that nobody noticed the M&A page already does this. The Sheet being empty was a symptom of weekly-tracker never firing, not evidence that a sheet-backed layer was needed.
**Pattern:** #pattern/check-existing-impl-before-rebuild

## Why This Trace Matters
Without this trace a future agent picks up task 9 verbatim, sees an empty weekly-tracker Sheet, concludes "the data layer is missing," and rebuilds the sheet-ingestion path — re-creating a parallel implementation of the M&A Analytics 9-snapshot archive. The non-obvious fact is that the archive ALREADY exists from a different source (vault/Attio, not the Sheet). The correct follow-up is verifying the existing archive job fires, plus deciding whether to retire weekly-tracker entirely (task 12) — not building around the Sheet.

## Key Insight
An empty backing store is ambiguous: it can mean "this layer is missing" OR "this layer's producer never ran AND a different layer already covers it." Before building a data path, grep for an existing implementation of the same capability — here the M&A Analytics page already owned the weekly archive.
