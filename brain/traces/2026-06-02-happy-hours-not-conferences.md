---
schema_version: 1.1.0
date: 2026-06-02
type: trace
task: Back-fill conference attendance record to launch
had_human_override: true
importance: medium
target: skill:conference-discovery
tags: [date/2026-06-02, trace, topic/conference-attendance, pattern/conference-definition, status/done]
---

# Decision Trace: Happy Hours and Annual Meetings Are Not "Conferences"

## Context
Back-filling Kay's conference attendance record (Conference Pipeline `Attended` tab) from Google Calendar, Feb-2025 launch to present. The calendar included recurring searcher "One Hanover Happy Hour" events and a "NYU FCU Annual Meeting," which I included as in-person networking.

## Decisions

### What counts as a "conference" in the attendance record
**AI proposed:** Include One Hanover Happy Hours and the NYU FCU annual meeting as networking attendance.
**Chosen:** **Remove all happy hours and the annual meeting** — Kay: "not a conference." Final record = conferences + industry/association events + summits/galas only (28 events).
**Reasoning:** Kay distinguishes a *conference/industry event* (owner/intermediary sourcing value, the budget + ROI unit) from a recurring social/peer happy hour. The attendance record and the $700/mo conference budget should reflect the former only, or both the cadence count and the ROI picture get distorted.
**Pattern:** #pattern/conference-definition

## Learnings
- For the conference attendance record and budget: **exclude recurring searcher/peer happy hours and routine membership annual meetings.** Include industry conferences, association chapter meetings/breakfasts, broker breakfasts, summits, galas, expos.
- Art-world/insurance networking (Frieze, Art Basel week receptions, PRMA, NAEPC) DOES count — it maps to Kay's art-advisory / art-insurance niches and women-led/luxury thesis.
- When back-filling, present a NUMBERED list for Kay to validate by number before/after writing — she edits by row number quickly.
