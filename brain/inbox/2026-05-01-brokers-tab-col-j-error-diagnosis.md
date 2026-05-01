---
schema_version: 1.2.0
date: 2026-05-01
title: Brokers tab col J #ERROR! diagnosis — data-in-wrong-column, not formula bug
status: backlog
source: manual
urgency: low
automated: true
tags: [date/2026-05-01, inbox, source/manual, topic/intermediary-target-list, topic/brokers-tab]
---

# Brokers tab col J `#ERROR!` diagnosis (2026-05-01)

## Description

NOT a broken formula. Col J is `LinkedIn (Person)` per the header row, but rows 2, 4, 5, 6, 7, 8, 9, 10, 11 had **phone numbers** stored there as plain strings (e.g. `+1 972-232-1100`, `+1 213-457-7948`). Col J appears to have a number/phone format applied that fails to parse the leading `+1 ` prefix, so Sheets renders `#ERROR!` for those cells while the underlying value is just a string.

This is a **data-in-wrong-column** bug, not a formula error. The phone numbers belong in col H (Office Phone) or col I (Direct/Mobile), not col J (LinkedIn Person).

### What I did

Cleared col J for the 9 affected rows (2, 4, 5, 6, 7, 8, 9, 10, 11). Original phone-string values are preserved in the snapshot at:
- `brain/context/rollback-snapshots/intermediary-brokers-transworld-fix-2026-05-01.json` (FORMULA values for col J)

Also cleared row 47 col H — that was a real `#ERROR! ()` formula (literal text, not a working formula). Row 47 is Hedgestone Business Advisors. Office phone for Hedgestone needs re-research if Kay wants to re-populate.

### Schema drift to investigate

The Brokers tab has rows of **inconsistent column count** (14, 16, 18, and 19 cols). The 19-col rows put data into different positions than the 16-col header expects:
- 14-col rows: phone in col H, no email
- 19-col rows: email in col I, phone in col J, LinkedIn in col L (which header says is "Credentials")

This suggests two batches of data were appended with different schemas. Rows 2-11 (the cleared phone-in-J rows) were likely an early batch that misaligned with the canonical header.

### Recommendation

If Kay wants to keep the Brokers tab clean long-term, a one-shot column-realignment pass would map the 19-col rows back into the 16-col schema (move email from I→G, phone from J→H, LinkedIn from L→J/K, etc.). Out of scope for today's fix bundle — flagging only.

## Notes

Cross-refs:
- See [[entities/kay-schneider]] (Kay)
- Snapshot: `brain/context/rollback-snapshots/intermediary-brokers-transworld-fix-2026-05-01.json`

## Outcome

*Pending Kay's review.*
