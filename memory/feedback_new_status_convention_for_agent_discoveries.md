---
name: new-status-convention-for-agent-discoveries
description: "When an agent surfaces a row/record for human triage (vs. taking a pipeline-stage action), write the literal `NEW` marker (uppercase) in the status/decision field. Universal across every agent-discovery sheet."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 03560fda-4372-4242-bb27-ca05145be53d
---

## Rule

When any skill writes a new row or record that Kay must review before it advances through a pipeline, use the literal `NEW` marker (uppercase) in the status/decision field.

**Never** invent a status like "Future / Map-Only," "Maybe relevant," "Auto-flagged," or "Needs review." Those are agent fabrications that pollute the dropdown and confuse validators. `NEW` is the canonical "I found this, please decide" marker.

## Why

1. **Visual scannability.** `NEW` is uppercase, distinctive, and visually different from human-set values like `Active` / `Tabled` / `Killed` / `Confirmed`. Kay can spot it at a glance when scanning a sheet.
2. **No collision with human values.** Human decision values are mixed-case; `NEW` reserves a slot that humans don't naturally type.
3. **Anti-fabrication anchor.** Gives agents a canonical option for "I'm surfacing this for review" so they don't reach for invented strings. Pairs with `feedback_no_fabricated_status.md` (agent-side) and `feedback_validators_reference_authoritative_source.md` (validator-side).
4. **Validator-friendly.** Validators allow `NEW → {any authoritative dropdown value}` as the authorized transition class. Anything else flowing OUT of `NEW` must land on a value defined in the schema/dropdown — no new invented strings.

## Scope

Applies to **every agent-discovery surface**, including but not limited to:

- **conference-discovery** → Conference Pipeline sheet (precipitating skill).
- **target-discovery** → per-niche target sheets when surfacing newly enriched companies.
- **deal-aggregator** → DealsX agent leads, broker BLAST extractions, marketplace discoveries.
- **niche-intelligence** → Industry Research Tracker rows added from the Tuesday-night scan.
- **outreach-manager** → any sheet rows representing agent-found intermediaries before Kay approves outreach.
- **email-intelligence** → any inbox-triage surface where the skill drafts a routing recommendation.
- Future agent-discovery skills not yet built.

## Precipitating incident

**2026-05-12 conference-discovery rogue-status trace.** The skill wrote `Future / Map-Only` to the Conference Pipeline sheet — an invented status that wasn't in the dropdown — for rows it wanted Kay to look at without committing them to the Active pipeline. Two failures stacked:

1. **Skill side:** invented its own status instead of using a canonical "review me" marker.
2. **Validator side:** codified the invented status as legitimate because it scanned live data instead of the dropdown definition (see `feedback_validators_reference_authoritative_source.md`).

The agent-side fix is this rule: use `NEW`. The validator-side fix is the companion memory.

## How to apply

- **When designing a new agent-discovery skill:** before writing any sheet/Attio row, decide the status convention. If the row needs Kay's review before advancing, write `NEW` in the status field. Document this in the skill's SKILL.md.
- **When updating an existing skill:** if you find it writing invented statuses (anything not in the dropdown), replace those writes with `NEW`.
- **Validator allowlists:** the authoritative dropdown values stay as-is. Add `NEW` as an explicit allowed value with the documented semantic "agent-surfaced, awaiting human triage." Transitions OUT of `NEW` must land on dropdown values; transitions INTO `NEW` are allowed only from agent writes (not human edits, typically).
- **Briefing surfacing:** when summarizing agent-discovery sheets in the morning briefing, count `NEW` rows as the triage queue size. "Conference Pipeline: 4 NEW rows awaiting decision."
- **Sunday rollover / nightly audits:** stale `NEW` rows (e.g. >14 days) should be surfaced as decision-fatigue items — either decide or kill, don't let them rot.

## Related memories

- `feedback_no_fabricated_status.md` — don't invent status values (general agent-side rule).
- `feedback_validators_reference_authoritative_source.md` — validator-side companion to this rule.
- `feedback_decision_fatigue_minimization.md` — `NEW` rows surface as decision items, count toward the ≤5 cap.
