# Daily Note Template

**Schema:** `schemas/vault/daily-note.yaml`

Read the schema's `example:` block for the complete template structure.

## Merge Behavior

When updating an existing daily note:

1. **Preserve Focus section** - don't overwrite user's decision
2. **Merge tasks** - add new items, don't remove existing
3. **Preserve checkmarks** - if user checked something, keep it
4. **Append triage items** - add new ones to existing list
5. **Preserve reflection** - don't touch evening section

## Section Mapping

| Source | Target Section |
|--------|----------------|
| Previous day incomplete (in-system) | ### In-System |
| Previous day incomplete (async) | ### Async |
| Inbox item (confidence: high, in-system work) | ### In-System |
| Inbox item (confidence: high, async work) | ### Async |
| Inbox item (confidence: medium/low) | ### Triage |
| Email scan results (actionable items) | ### Async or ### In-System |
| Email scan results (medium/low) | ### Triage |
| In-person meetings from email-scan-results | Granola reminder (top of daily note) |

## Granola Reminder

If `brain/context/email-scan-results-{date}.md` contains an "In-Person Meetings Today" section, add a reminder at the top of the daily note, right after the Focus section:

```markdown
**Granola reminder:** Turn on Granola before your {time} with {person} at {location}
```

One line per in-person meeting. Skip if no in-person meetings today.

## Task Formatting

**Standard task:**
```markdown
- [ ] Review contract changes from Sarah
```

**Task with source (for triage items):**
```markdown
- [ ] Review contract changes from Sarah (source: email)
```

**Task with entity link (when known):**
```markdown
- [ ] Send proposal to [[entities/jane-smith|Jane]] (due: Dec 30)
```
