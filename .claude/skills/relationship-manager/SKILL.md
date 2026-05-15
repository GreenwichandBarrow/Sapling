---
name: relationship-manager
description: "Nurture cadence monitoring, action-already-taken verification, overdue contact surfacing, and People record management in Attio. Writes relationship-status artifact for morning briefing."
archetype: router
context_budget:
  skill_md: 200
  max_references: 12
  learnings_md: 40
  sub_agent_limit: 500
user_invocable: true
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
4. Attio `next_action` field: if it references recent contact (e.g., "Texted recently", "Spoke at event"), treat as recent interaction even without Gmail/calendar evidence

**Limitation:** Gmail and calendar are the only channels this skill can verify. Kay also communicates via text, phone, and in-person. When surfacing overdue contacts, note this caveat. If Attio `next_action` was recently updated with evidence of contact, trust it over Gmail silence.

### Trigger-Based vs Cadence-Based Contacts (CRITICAL)

Before surfacing ANY contact, check their `next_action` field in Attio:
- If `next_action` contains trigger language ("when", "once", "after", "if", "re-engage when") → this is a **trigger-based contact**. Do NOT surface based on time elapsed. Only surface when the trigger condition is met.
- If `next_action` is empty or contains a standard action (e.g., "Send thank you", "Schedule call") → this is cadence-based, surface normally.
- If `nurture_cadence` is "Dormant" → NEVER surface regardless of next_action content.

**Example:** `next_action: "Re-engage when we have an insurance deal for him to review"` → Do NOT surface this person as overdue. The trigger is having a deal, not elapsed time.

### Cadence Field Is Sole Source of Truth (CRITICAL — added 2026-04-23 after Lauren miss)

The `nurture_cadence` field is the **only** source of truth for the threshold to apply. Cadence thresholds:

| Cadence | Threshold |
|---------|-----------|
| Weekly | 10 days |
| Monthly | 5 weeks (35 days) |
| Quarterly | 14 weeks (98 days) |
| Occasionally | 7 months (213 days) |
| Dormant | Never surface |

**Do NOT infer the threshold from the `next_action` text.** If `nurture_cadence = Occasionally` but `next_action = "Maintain quarterly touchpoint"`, apply the **Occasionally** threshold (213 days), not the Quarterly threshold (98 days). The cadence field reflects Kay's most recent decision; next_action text may be stale and is informational only.

If next_action text and cadence field conflict (e.g., text says "quarterly" but cadence is "Occasionally"), flag the contact in the artifact under "Metadata Drift" so Kay can decide which to update — but do NOT surface as overdue based on the text.

**Lauren Della Monica precedent (2026-03-31):** Cadence changed Quarterly → Occasionally. Next_action text said "Maintain quarterly touchpoint." Skill mistakenly surfaced her as 97 days overdue against quarterly threshold for 3 weeks. She is NOT overdue under Occasionally (195/213 days). Bug: skill read text as override. Fix: text is informational, cadence rules.

### Within-Cadence Commitment Drift (added 2026-04-23 after Stanley miss)

Do **NOT** surface a contact who is within their cadence window just because `next_action` references an aged commitment. Stanley Rodos: Quarterly cadence, 37 days since last contact (well within 98-day quarterly threshold), next_action mentions "Follow up on Art Restoration Services opportunity (Mar 17)." The aged commitment text is captured in next_action; surfacing him as a "drifting commitment" is noise. Trust the cadence — Kay knows when she'll see him next.

If Kay has explicit named commitments she wants tracked separately from cadence (e.g., "follow up on X opportunity"), those go in a separate Beads task or a To Do row (via task-tracker-manager), not as relationship-manager surfacing.

### Processing

1. Query all Attio People records where `nurture_cadence` is set and not "Dormant"
2. For each, check `next_action` for trigger language — skip trigger-based contacts
3. For remaining contacts, determine last interaction date from data sources above
4. Compare against the threshold from the **cadence field only** (ignore next_action text for threshold)
5. Surface the top 5 overdue contacts (prioritized by: how far overdue, relationship value, recency of last interaction)
6. For each overdue contact, suggest an action: email, coffee, event invite, or just a check-in
7. Note in the artifact that Gmail/calendar are the only verified channels — text and phone interactions may not be captured
</nurture_monitoring>

<action_verification>
## Action-Already-Taken Verification (CRITICAL)

Before surfacing ANY "overdue" or "needs action" contact, verify whether Kay already acted between sessions.

Search by **recipient + recency**, NOT by subject keyword — Kay's follow-ups are often replies in existing threads with unrelated subjects.

```bash
# For each contact about to be surfaced:
gog gmail search "from:kay.s@greenwichandbarrow.com to:{contact_email} newer_than:14d" --json --max 5
```

**Use a 14-day search window** (not 7 days) to catch thank-yous and follow-ups that were sent earlier in the period. A thank-you sent 8 days ago is still a valid interaction.

- **Outbound email found** → Read the email content to confirm it's a substantive interaction (not just a calendar confirmation). If substantive → Action was taken. Auto-update the contact's last interaction date. Do NOT surface to Kay. Log: "Auto-resolved: {name} — email sent {date}."
- **No email found** → Surface in the relationship-status artifact.

### Session Decision Log Check
Also check `brain/context/session-decisions-{previous-workday}.md` for prior decisions on contacts:
- If Kay PASS'd a contact (e.g., "don't contact X"), do not surface regardless of cadence status
- If Kay APPROVE'd an action on a contact and it appears in Actions Taken (SENT/DRAFTED), treat as resolved
- If Kay DEFER'd a contact with a trigger condition, exclude from overdue list until trigger is met

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

### Assistant vs Principal Detection (CRITICAL)

When surfacing a contact for outreach, check whether the person is an assistant or the decision-maker:
- If the contact's role contains "assistant", "admin", "coordinator", "EA", or "office manager" — they are likely an assistant
- If next_action references a different person's name (e.g., "Reschedule call" but the principal is someone else at the same company) — surface the principal, not the assistant
- Cross-check: search Attio for other People at the same company. If one is clearly the owner/principal and the other is support staff, the outreach recommendation should name the principal.
- **Example:** Chase Lacson (assistant) at Goodman Taft has next_action "Reschedule call" — but the email should go to Molly Epstein (principal). Surface as "Molly Epstein (Goodman Taft)" not "Chase Lacson."
</people_records>

<vault_to_attio_sync>
## Vault → Attio Sync (Engagement Notes Backfill)

**Purpose:** When skills like `conference-engagement` write a vault entity with engagement notes BEFORE the corresponding Attio person record exists (because Attio auto-creates the person only on email send/receive), this step closes the loop. It runs every morning as part of relationship-manager and ensures Kay's engagement context lands in Attio once the auto-created stub exists.

**Why this exists:** Per `feedback_close_out_executes_mutation`, every signal must mutate source-of-truth in the same window. The conference-engagement skill writes the vault entity at card-collection time, but cannot write to Attio until the auto-created person record exists (which happens only when Kay sends the draft). This sync bridges the two events.

### Detection — which entities to sync

Scan `brain/entities/` for files matching ALL of:
1. Modified in the last 7 days
2. `type: person` in frontmatter
3. EITHER `attio_id` field is empty OR `attio_synced_at` field is missing/older than the file's `modified` time
4. Has a non-empty `## Relationship Notes` section in the body

### Sync flow per entity

For each entity matching detection criteria:

1. **Look up Attio person by email** (preferred) or `name + company`:
   - `gog` not used here — use Attio MCP `search_records` with email filter
   - If Attio person not found → skip (will retry tomorrow; person record auto-creates on next email send/receive)
   - If Attio person found → proceed

2. **Check whether engagement note already attached** (idempotency):
   - Use Attio `list_notes` filtered to that person record
   - If a note titled `"{conference_or_source} {date} — engagement context"` already exists → skip (already synced)

3. **Build the note content** from the vault entity:
   - Pull `## Relationship Notes` section verbatim (date-prefixed bullets)
   - Pull the `## Key Context` section if present (background)
   - Append a footer linking back: `Vault: [[entities/{slug}]]`

4. **Attach the note to the Attio person record** via `create_note`:
   - Title: `{source} {date} — engagement context` (e.g., "XPX 2026-04-23 — engagement context")
   - Format: markdown
   - Content: the constructed body

5. **Set Attio attributes from vault frontmatter** (only if Attio field is empty — never overwrite Kay's manual edits):
   - `nurture_cadence` — derive from entity status (prospect → Quarterly default; partner → Monthly; etc.)
   - `relationship_type` — derive from entity classification if explicit (Intermediary → "Industry Expert" or "River Guide" if connector signal present; Owner → "Fellow Searcher" if relevant; otherwise leave for Kay)
   - `how_introduced` — pull from `## Quick Facts` or first relationship note (e.g., "Met at XPX 2026-04-23, came over after panel")
   - `value_to_search` — pull from one-line summary in `## Key Context` if available

6. **Update the vault entity frontmatter** to mark synced:
   - Set `attio_id: {record_id}` (if not already set)
   - Set `attio_synced_at: {ISO timestamp}`
   - Re-write file with updated frontmatter

7. **Log to artifact** under new section "Vault → Attio Syncs" (see Output Artifact below).

### Failure modes to handle

- **Attio note creation fails 403** → API token is missing `notes:read-write` scope. Surface this in the artifact as a System Status alert ("Attio token scope insufficient — engagement notes not syncing"). Do NOT retry repeatedly; one log per missing-scope event per day is enough. Kay must fix the scope at the Attio admin / Smithery connector level.
- **Multiple Attio person matches** (e.g., two records with the same email due to dedup misses) → log to artifact under "Attio Dedup Needed", do not pick one arbitrarily.
- **Vault entity has `attio_id` but the record doesn't exist** (deleted in Attio) → clear the `attio_id` field, retry detection on next run.

### Idempotency requirement

This step MUST be safe to run multiple times. Re-running on the same vault entity must NOT create duplicate notes. Idempotency hinges on the note-title check in step 2 — if that check fails (e.g., Kay renamed the note manually), the duplicate-detection breaks. Acceptable risk for now; tighten if Kay reports duplicates.

</vault_to_attio_sync>

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

## Vault → Attio Syncs
- {Name}: engagement note attached, attio_id captured in vault entity
- ...
- (Or "None — no vault entities pending sync")

## Attio Dedup Needed (if any)
- {Email}: N matching person records — Kay must merge

## System Status Alerts (if any)
- "Attio API token missing notes:read-write scope — engagement notes not syncing. Fix at Smithery / Attio admin."
```

Pipeline-manager reads this artifact and presents it in Section 4 (Gmail email drafts to review/approve) of the morning briefing.

## Validator (Stop Hook) — MANDATORY

**Wrapper-level POST_RUN_CHECK validator** (authoritative): `scripts/validate_relationship_manager_integrity.py`

Runs after `claude -p` exits, regardless of skill-internal logic. Catches the silent-success failure mode where Claude exits 0 but no artifact landed.

**Copyable invocation (manual run):**
```bash
python3 "/Users/kaycschneider/Documents/AI Operations/scripts/validate_relationship_manager_integrity.py"
# Pass --date YYYY-MM-DD to validate a different date
```

**What the validator checks:**
- Artifact exists at `brain/context/relationship-status-{YYYY-MM-DD}.md` for run date
- Artifact has YAML frontmatter with `date:` and `type: relationship-status`
- At least one expected section header is present
- Artifact is ≥200 bytes (rejects empty stubs)

**What it does NOT check:** Attio write success. The skill is designed to graceful-degrade when Attio MCP is down — the artifact + "System Status Alerts" section is the deliverable, Attio sync is downstream-best-effort.

The launchd wrapper (`scripts/run-skill.sh`) overrides EXIT_CODE on POST_RUN_CHECK failure and emits a Slack alert prefixed `VALIDATOR FAILED`. Pattern: `memory/feedback_mutating_skill_hardening_pattern.md`. Bead: `ai-ops-jrj.4`.
</artifact>

<stop_hooks>
## Stop Hooks

- [ ] All overdue contacts verified against Gmail before surfacing (no false positives)
- [ ] Trigger-based contacts (next_action contains "when"/"once"/"after"/"if") excluded from overdue list
- [ ] Auto-resolved contacts had their Attio records updated
- [ ] Vault → Attio sync ran for any vault entity modified in last 7 days with unsynced engagement notes
- [ ] Sync writes are idempotent (re-runs don't duplicate notes)
- [ ] Vault entity frontmatter updated with `attio_id` + `attio_synced_at` for every successful sync
- [ ] Artifact written to `brain/context/relationship-status-{date}.md`
- [ ] Artifact has all sections (even if empty, mark "None")
- [ ] No contacts surfaced that Kay already emailed in the last 7 days
- [ ] Artifact notes that Gmail/calendar are the only verified channels (text/phone not captured)
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
