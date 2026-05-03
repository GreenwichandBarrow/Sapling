# pipeline-manager learnings

Skill-local feedback loop per Harrison Wells coaching session 4/30. Pilot skill for the `learnings.md` pattern. Read at start of every run, append at end if anything was learned.

**Bias toward NEGATIVE directives.** Per Harrison: "do NOT do X because Y" outperforms "do A then B." The model is sharper at avoiding flagged anti-patterns than remembering positive instructions.

**Format per entry:**
```
- [YYYY-MM-DD] Do NOT {action}. Reason: {why}. Source: {trace, decision, incident}.
```

**Scope:** pipeline-manager-specific. Cross-skill rules belong in `memory/feedback_*.md`. If a learning here applies to 3+ skills, graduate it to global memory and remove the local entry.

**Lifecycle:** entries that have been honored across 5+ runs without violation can be pruned. Never delete an entry that's been violated within the last 30 days.

---

## Active learnings

- [2026-05-03] Do NOT surface relationship/nurture/cadence-debt items on Mon-Thu briefings. Reason: surfacing them daily creates decision fatigue. Friday-only per `feedback_relationship_cadence_friday_only`. Source: graduated to global memory; kept here as reminder until 5 clean runs.
- [2026-05-03] Do NOT report items Kay completed herself in the briefing. Reason: she already knows; reporting them back is noise. Source: `feedback_briefing_no_done_items`.
- [2026-05-03] Do NOT use ambiguous briefing items. Reason: every item must have an explicit question or action; ambiguity wastes Kay's review time. Source: `feedback_morning_briefing_format`.
- [2026-05-03] Do NOT forget the brief-decisions pre-flight before delivery. Reason: tomorrow's external meetings must be enumerated and surfaced as 🔴 items unless already approved/declined in session-decisions. Source: 4/21 Guillermo miss incident, captured in CLAUDE.md.
- [2026-05-03] Do NOT exceed 5 items in any Decisions bucket. Reason: per `feedback_decision_fatigue_minimization` — recommend, don't ask. Cluster by entity. Sort 🔴 → 🟡 → 🟢.
- [2026-05-03] Do NOT reset numbering in the Decisions list within a single briefing. Reason: Kay replies by number across the whole list; resetting breaks her reply flow. Source: CLAUDE.md morning-workflow doctrine.
- [2026-05-03] Do NOT trust session-decisions alone for "what was planned." Reason: query order is calendar → beads → brain/outputs/ → session-decisions. Session-decisions records what changed, not current state. Source: `feedback_what_was_planned_query_order`.

## Watching for

(Anti-patterns suspected but not yet documented as anti-patterns. Promote to "Active learnings" once observed twice.)

- (none yet)

---

## Append protocol

When a run produces a new learning:
1. Add an entry under "Active learnings" with `[YYYY-MM-DD]` prefix.
2. Cite the source (decision trace, incident, Kay correction).
3. If the learning is general enough to apply to 3+ skills, ALSO graduate to `memory/feedback_*.md` and note "graduated to global memory" inline here.
4. If the learning is too uncertain (one observation), file under "Watching for" instead.

Do NOT append entries that just rephrase existing rules — only NEW anti-patterns.
