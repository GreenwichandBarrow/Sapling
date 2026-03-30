---
name: relationship-manager
description: "Nurture cadence monitoring, action-already-taken verification, overdue contact surfacing, and People record management in Attio. Writes relationship-status artifact for morning briefing."
user_invocable: true
context_budget:
  skill_md: 2000
  max_references: 2
  sub_agent_limit: 2000
---

<objective>
Manage long-term relationship health across Kay's entire network. This skill monitors nurture cadences, verifies whether Kay already took pending actions, surfaces overdue contacts, and maintains People record attributes in Attio.

**Output:** Writes `brain/context/relationship-status-{date}.md` artifact that pipeline-manager reads for Section 4 of the morning briefing.

**This skill does NOT:**
- Move deals through pipeline stages (that's pipeline-manager)
- Create outreach drafts for targets (that's outreach-manager)
- Manage JJ's call operations (that's jj-operations)
- Scan email for deal signals (that's email-intelligence, future)
</objective>

<nurture_monitoring>
## Nurture Cadence Monitoring

### Cadence Thresholds

| Cadence | Overdue After |
|---------|---------------|
| Weekly | 10 days since last interaction |
| Monthly | 5 weeks since last interaction |
| Quarterly | 14 weeks since last interaction |
| Occasionally | 7 months since last interaction |
| Dormant | Do not surface |

### Data Sources for Last Interaction

Check these in order (most recent wins):
1. Gmail: last email to/from contact (`gog gmail search "to:{email} OR from:{email}" --max 1 --plain`)
2. Calendar: last meeting with contact
3. Vault: last call note in `brain/calls/` mentioning the entity

### Processing

1. Query all Attio People records where `nurture_cadence` is set and not "Dormant"
2. For each, determine last interaction date from data sources above
3. Compare against cadence threshold
4. Surface the top 5 overdue contacts (prioritized by: how far overdue, relationship value, recency of last interaction)
5. For each overdue contact, suggest an action: email, coffee, event invite, or just a check-in
</nurture_monitoring>

<action_verification>
## Action-Already-Taken Verification (CRITICAL)

Before surfacing ANY "overdue" or "needs action" contact, verify whether Kay already acted between sessions.

Search by **recipient + recency**, NOT by subject keyword — Kay's follow-ups are often replies in existing threads with unrelated subjects.

```bash
# For each contact about to be surfaced:
gog gmail search "from:kay.s@greenwichandbarrow.com to:{contact_email} newer_than:7d" --json --max 5
```

- **Outbound email found** → Action was taken. Auto-update the contact's last interaction date. Do NOT surface to Kay. Log: "Auto-resolved: {name} — email sent {date}."
- **No email found** → Surface in the relationship-status artifact.

This applies to ALL relationship actions: thank-yous, follow-ups, check-ins, intros owed. The pattern: if the system thinks Kay needs to do something, check if she already did it.
</action_verification>

<people_records>
## People Record Management

### Attio People Attributes Owned by This Skill

| Attribute | Description |
|-----------|-------------|
| relationship_type | How this person relates to G&B (Fellow Searcher, Industry Expert, Advisor, Art World, Friend/Personal, Investor, River Guide) |
| nurture_cadence | How often to touch base (Weekly, Monthly, Quarterly, Occasionally, Dormant) |
| next_action | What's pending (free text, e.g., "Send Zoe intro", "Schedule Q2 check-in") |
| value_to_search | Why this person matters to the search (free text) |
| how_introduced | Origin of the relationship (free text) |

### Update Rules

- Only update attributes when there's a clear signal (email sent, meeting held, Kay instruction)
- Never overwrite `how_introduced` — it's historical
- `next_action` should be cleared when the action is verified complete
- `nurture_cadence` can be adjusted based on interaction frequency (upgrade if engaging more, downgrade if going cold)
</people_records>

<intro_tracking>
## Warm Intro Tracking

Track intros Kay has promised or owes. When processing contacts:
- Check `next_action` field for intro-related text ("Connect X with Y", "Send intro to Z")
- Verify whether the intro email was sent via Gmail search
- If sent → clear the next_action
- If not sent → surface in the artifact: "{name} — intro to {person} still pending"

Also detect new intro opportunities when processing targets (from target-discovery handoff):
- Search Attio People for connections to the target's company or owner
- Search vault entities for prior mentions
- Search Gmail for prior correspondence
- If warm path exists, flag it: "Warm intro possible via {contact name} — {how connected}"
</intro_tracking>

<artifact>
## Output Artifact

Write to `brain/context/relationship-status-{date}.md` after processing:

```markdown
---
date: {YYYY-MM-DD}
type: relationship-status
---

## Overdue Contacts (Top 5)
1. {Name} ({Company}) — {cadence}, last contact {date}, {days} overdue
   Suggested action: {email/coffee/event invite/check-in}
2. ...

## Auto-Resolved (No Action Needed)
- {Name}: email sent {date}, updated last interaction
- ...

## Pending Intros
- {Name}: intro to {person} still outstanding
- ...

## Warm Intro Opportunities (from target-discovery)
- {Target Company}: warm path via {contact} — {connection}
- ...
```

Pipeline-manager reads this artifact and presents it in Section 4 (Superhuman email drafts to review/approve) of the morning briefing.
</artifact>

<stop_hooks>
## Stop Hooks

- [ ] All overdue contacts verified against Gmail before surfacing (no false positives)
- [ ] Auto-resolved contacts had their Attio records updated
- [ ] Artifact written to `brain/context/relationship-status-{date}.md`
- [ ] Artifact has all 4 sections (even if empty, mark "None")
- [ ] No contacts surfaced that Kay already emailed in the last 7 days
</stop_hooks>

<success_criteria>
## Success Criteria

- [ ] Overdue contacts surfaced with suggested actions
- [ ] No false positives (Kay already took the action)
- [ ] Pending intros tracked and surfaced
- [ ] Warm intro paths detected for new targets
- [ ] People records updated accurately
- [ ] Pipeline-manager can read the artifact and render Section 4
</success_criteria>
