---
schema_version: 1.1.0
date: 2026-06-02
type: trace
task: Handle 3 Kay-directed niches silently auto-excluded by the niche-intelligence Tuesday run
had_human_override: false
tags: [date/2026-06-02, trace, topic/niche-intelligence, pattern/explicit-directive-beats-default-doctrine, person/matt-luczyk]
---

# Decision Trace: Kay-Directed Niches Should Override Auto-Exclude

## Trigger
Kay explicitly directed three niches (carpet installation, veteran-benefits consulting, warranty plumbing/pipe) onto the Industry Research Tracker "to run discovery on tonight." They were queued to `brain/inbox/` as Kay-directed/high-confidence with an explicit note: "context for scoring, NOT suppression — Kay still wants discovery + initial screen run." The 2026-06-02 22:30 niche-intelligence run processed all three, but **surfaced-not-advanced** them under standard G&B exclusion screens (carpet + warranty = construction/trades soft-exclude; VA-benefits = fee-ban + B2C), wrote no tracker rows, and advanced two niches of its own instead. Kay: "I'm not seeing the 3 queued niches within the industry tracker."

## Decision
Recommended **force-advancing all three onto WEEKLY REVIEW as New-Pending-Review with the exclusion verdict attached as a row-flag** (VA-benefits carrying its regulatory kill-reason), so they are visible for the analyst call and Kay makes the keep/kill call. Surfaced the underlying behavior as a calibration miss: an explicit CEO directive was silently overridden by default doctrine.

## Alternatives Considered
- **Accept the skill's exclusion verdict** (leave them off the tracker). Rejected — it silently overrides an explicit, twice-stated Kay directive; she experienced it as the system ignoring an instruction.
- **Manually add bare tracker rows** via tracker-manager. Rejected — violates the niche-intel rule "nothing reaches WEEKLY REVIEW without a one-pager + score"; produces half-baked rows.
- **Re-run niche-intel --from-inbox as-is.** Rejected — same doctrine would re-exclude them; the override intent has to be explicit.

## Reasoning
Exclusion screens (construction-adjacent, B2C) are Kay's own defaults — but defaults exist to filter *undirected* discovery, not to veto an explicit instruction from the CEO. When Kay names specific niches, the right behavior is to evaluate AND advance them with the exclude recorded as a visible flag, so the screen becomes decision *context* rather than a silent gate. The VA-benefits case shows why the flag matters: its exclude reason (federal/state restrictions on charging veterans for benefits help) is materially real, not just doctrine — exactly the kind of thing Kay should see on the row, not have hidden by a drop.

## Why This Trace Matters
A future agent re-running niche-intelligence (or building its headless prompt) needs to know: an inbox niche tagged Kay-directed must reach the tracker even when it hits an exclude. Without this, explicit user instructions keep getting eaten by default screens and the user loses trust that "add this" means it appears.

## Key Insight
Explicit user directive beats default doctrine. An exclusion screen should *flag* a directed item, never silently *drop* it. Pending Kay's confirmation to harden niche-intelligence accordingly.
