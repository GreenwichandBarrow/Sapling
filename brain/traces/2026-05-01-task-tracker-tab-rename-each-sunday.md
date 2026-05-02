---
schema_version: 1.1.0
date: 2026-05-01
type: trace
today: "[[notes/daily/2026-05-01]]"
task: Define personal task tracker live-tab naming convention
had_human_override: false
importance: medium
target: skill:task-tracker-manager
tags: [date/2026-05-01, trace, topic/personal-task-tracker, topic/excel-tooling, pattern/dynamic-tab-naming-by-week]
---

# Decision Trace: Live Task-Tracker Tab Renamed Each Sunday to Current Mon-Sun Range

## Context

The personal task tracker (TO DO 4.26.26.xlsx) has a live working tab — originally named "This Week" (static). Each Sunday, the goodnight Sunday rollover ceremony copies the live tab → hides the copy as `archive_{label}` → clears habit/priority/notes data on the live tab → ready for the new week.

Two naming conventions were possible for the live tab:
- **Static name "This Week":** Always identifies the working tab by role; archive copies get the dated label.
- **Dynamic Mon-Sun range:** Live tab renamed each Sunday to the current week's range (`Apr 27-May 3`, `May 4-10`, etc.); archives keep the dated label they had at archive time.

## Decisions

### Tab-naming convention → Dynamic Mon-Sun range on the live tab

**AI proposed:** Static "This Week" name, since the live tab's role doesn't change.

**Chosen:** Live tab renamed each Sunday to current `Mmm D-D` range. Replaces static "This Week" name. Date formulas remain tab-name-agnostic (use TODAY() not tab references).

**Reasoning:** Excel's tab strip at the bottom of the window shows tab names directly. Kay can see the current week range without opening any tab — the tab strip itself becomes the at-a-glance "what week am I in" indicator. With a static "This Week" name, Kay would have to open the tab to see the date range, which defeats the purpose of having a tab strip. The dynamic name uses Excel's existing UI (tab strip) as a passive display surface.

The tradeoff — losing the role-identifying name — is mitigated by the fact that the live tab is always the leftmost or rightmost tab depending on archive ordering, so its position alone identifies its role. The date range is the more useful information.

**Pattern:** #pattern/dynamic-tab-naming-by-week

## Learnings

- **Use Excel's tab strip as a passive display surface.** Tab names are visible without opening anything; encode information into them when the information matters more than role-identification.
- **Tab-name-agnostic formulas required:** When tab names are dynamic, all cross-tab and date formulas must use TODAY() / WEEKNUM() / row-relative references — never `'This Week'!A1`-style absolute tab references.
- **Sunday rollover sequence (codified):** copy live → hide as `archive_{label}` → rename live to next Mon-Sun range → clear habit/priority/notes data. Order matters: hiding before rename avoids name-collision; clearing after rename means the new tab name applies to the cleared state, not the carried state.
- **Future agents:** Don't rename the live tab back to "This Week" thinking it's a one-off mistake. The rename IS the design.
