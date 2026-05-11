---
name: Snapshot before overwriting sheets or docs
description: Always version/snapshot existing content before replacing rows, sheets, or docs — never destructive overwrites without a restore path
type: feedback
originSessionId: aaa48d69-b635-4ce4-8a5c-8371cb1bcc33
---
Before overwriting any existing content on a Google Sheet, Google Doc, or vault file, save a versioned snapshot so the prior state can be restored.

**Why:** On 2026-04-14, the 3 luxury niches on Sam's DealsX sheet were replaced with 3 new SaaS niches. On 2026-04-15, Kay changed her mind and wanted the originals back — but no snapshot existed, so the prior content had to be reconstructed from memory/Drive one-pagers. Kay: "in the future we need to save versions and not overwrite things."

**How to apply:**
- Before any Sheet row replacement: dump current values (via `gog sheets read`) to a timestamped vault snapshot file (`brain/snapshots/{sheet-name}-{YYYY-MM-DD-HHMM}.tsv` or `.json`) and commit.
- Before any Doc content replacement: duplicate the Doc in Drive with a `-snapshot-{date}` suffix, OR export to `brain/snapshots/` as markdown.
- Before any vault file rewrite (not append): git commit the current version first with a clear "pre-change snapshot" message.
- The snapshot is not optional — treat overwrites as two steps: (1) snapshot, (2) overwrite. Skipping step 1 is a bug.
- Applies to: DealsX sheets, Industry Research Tracker, target lists, any living doc Kay edits, Google Sheets generally.

Exceptions: routine field-level edits (e.g., updating a single status cell, setting Rev Source) don't need snapshots. The rule is for bulk content replacement where restoring the prior state would be hard.
