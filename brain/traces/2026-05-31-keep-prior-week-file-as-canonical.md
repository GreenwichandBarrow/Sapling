---
schema_version: "1.1.0"
date: 2026-05-31
type: trace
title: "Keep prior-week file (5.24.26) as canonical despite build-week creating 5.31.26"
tags:
  - date/2026-05-31
  - trace
  - skill/task-tracker-manager
  - topic/weekly-files-architecture
  - status/done
---

# Keep prior-week file as canonical despite build-week rollover

## Trigger
Sunday `build-week` (first real Phase 5 rollover) created `TO DO 5.31.26` and repointed the resolver to it. But Kay had stayed working in `TO DO 5.24.26` all weekend — adding `DAILY FOCUS` rows to every tab and editing tasks — none of which existed on the auto-created file.

## Decision
Treat `5.24.26` (the file Kay is actually in) as canonical going forward, not the build-week output. Asked Kay; she chose "keep the file I'm in."

## Alternatives Considered
- **Migrate her focus rows + edits into the new `5.31.26`** and point her there (honors the weekly-files architecture's fresh-file cadence). Rejected: more migration steps, real risk of dropping a manual edit, and Kay was already oriented in `5.24.26`.
- **Force the weekly-files flow** (silently make her switch). Rejected: orphans her work; she never opted into the new file.

## Reasoning
The user's live working surface beats the architecture's nominal "current file." Kay's edits are the source of truth; the auto-created file was empty of them. Lowest-risk path preserves her work in place.

## Why This Trace Matters
This is a **deviation from the weekly-files `build-week` doctrine** (which assumes the newest Drive-copied file is canonical and the prior file is frozen history). A future agent reading the resolver pointer (`5.31.26`) would target the wrong file. Two cleanups are owed: repoint the resolver to `5.24.26`, and decide rename-to-this-week / trash the `5.31.26` duplicate.

## Key Insight
When the weekly rollover creates a new file but the user keeps editing the old one, the old one wins — but the resolver pointer and the build-week assumption must be reconciled, or scripted writes silently hit the wrong file.
