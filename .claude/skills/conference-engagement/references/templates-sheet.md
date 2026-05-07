# Conference Engagement Templates Sheet — Runtime Reference

## Location
- **Sheet name:** `G&B Conference Engagement Templates`
- **Sheet ID:** `1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ`
- **Folder:** G&B Master Templates (ID `19TxdV5GHHbYq_O8YupQ-gkEH7V00iykx`)
- **URL:** https://docs.google.com/spreadsheets/d/1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ/edit

## Structure

### Tab: `Templates`
| Col | Field | Description |
|-----|-------|-------------|
| A | template_id | Stable ID referenced by skill (`preconf_intermediary`, etc.) |
| B | audience | Intermediary / Owner / Peer |
| C | mode | Pre-Conference / Post-Conference |
| D | subject | Email subject template (may contain `{{variables}}`) |
| E | body | Email body template (may contain `{{variables}}`) |
| F | notes | Usage guidance (not rendered) |

Template IDs (rows 2-7):
1. `preconf_intermediary`
2. `preconf_owner`
3. `postconf_intermediary`
4. `postconf_intermediary_deal`
5. `postconf_owner`
6. `postconf_peer`

### Tab: `Snippets`
| Col | Field | Description |
|-----|-------|-------------|
| A | snippet_id | Stable ID (`buy_box_intermediary`) |
| B | content | Snippet text to substitute |
| C | notes | Usage guidance |

### Tab: `README`
Human-readable overview. Skill does not read this tab.

## Runtime Read Commands

```bash
# Load all templates
gog sheets get 1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ "Templates!A2:F7" --json

# Load all snippets
gog sheets get 1Y4XcQJDe28RB7k_Cw5NZNjKRyX4d1qEczadXdQrjpaQ "Snippets!A2:C10" --json
```

## Variable Substitution Order

The skill must perform substitutions in this order:

1. **Snippet substitution first.** Replace `{{buy_box_intermediary}}` with the content of that snippet row before populating other variables. This prevents nested substitution bugs.
2. **Template variables second.** `{{first_name}}`, `{{conference}}`, `{{conference_day}}`, `{{callback}}`, `{{personalization}}`, `{{reciprocal_hook}}`, `{{deal_sector}}`.

## Editing Rules

Kay edits templates directly in the Sheet. Any edit is live immediately — skill reads from sheet at every run.

**If Kay changes the buy-box paragraph:**
- Edit ONLY the `buy_box_intermediary` row in the Snippets tab
- Do NOT edit the intermediary template body rows (they contain `{{buy_box_intermediary}}`, not the literal paragraph)

**If Kay adds a new template:**
- Add a new row to the Templates tab with a unique `template_id`
- Update SKILL.md to reference the new template_id

**If Kay adds a new snippet:**
- Add a new row to the Snippets tab with a unique `snippet_id`
- Reference as `{{new_snippet_id}}` in any template body

## Fallback

If the Sheet is unreachable at runtime, fall back to the local copy at `templates/email-templates.md`. Log a warning that Kay's recent edits may not be reflected.
