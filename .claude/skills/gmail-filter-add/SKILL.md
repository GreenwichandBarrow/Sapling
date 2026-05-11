---
name: gmail-filter-add
description: Append one or more email addresses to an existing Gmail label's bundled-contacts filter. Use when Kay says "add X to filter Y" or "add X to auto/Y". Part of the Superhuman → Gmail transition — replaces the manual filter-edit workflow Gmail's API doesn't natively support.
invocation: user
context_budget:
  skill_md: 400
  max_references: 0
---

<objective>
Append email address(es) to the bundled-contacts OR-filter for a given Gmail label. Gmail's API has no patch endpoint for filters, so the only safe path is create-new-then-delete-old. Do create-first to avoid an unlabeled window.
</objective>

<auto_trigger>
Human phrases:
- "add {email} to {label} filter"
- "add {email} to auto/{label}"
- "filter {email} as {label}"
- "{name}'s email should go to {label}"
- "route {email} to {label}"

Args typically take the form: `{email} {label}` or `{email}, {email2} {label}`.
</auto_trigger>

<essential_principles>
- **Create first, delete second.** If create succeeds and delete fails, you have a brief duplicate filter (harmless). If delete-first, you have a window with no labeling.
- **Idempotent.** If the email is already in the bundled query, report and stop — don't churn the filter ID.
- **Heuristic match for "bundled" filter.** The bundled filter is the one targeting the label whose `criteria.query` matches `from:(... OR ...)`. There may also be 1-off filters for the same label (single `from:` field) — leave those alone.
- **Multiple bundled candidates → ask Kay which one.** Don't guess.
- **No bundled filter exists yet → create one** with `from:({email})` query targeting the label.
</essential_principles>

<intake>
Args expected: `<email> [more emails comma-or-space-separated] <label-name-or-fragment>`

Examples:
- `/gmail-filter-add jemden@helmsleyspear.com auto/personal & network`
- `/gmail-filter-add jane@acme.com, bob@acme.com personal`
- `/gmail-filter-add new.broker@example.com deal flow`

Label name can be a fragment — match case-insensitive on label display name. If multiple labels match, ask Kay which.
</intake>

<workflow>

### Step 1 — Bootstrap auth
```bash
set -a
source ~/.config/op-sa-token.env
set +a
export GOG_KEYRING_PASSWORD=$(op read 'op://GB Server/GOG Keyring Password/password')
```

If `op read` fails: surface to Kay — 1Password bootstrap is broken, do not proceed.

### Step 2 — Resolve label name → label ID
```bash
gog gmail labels list --account kay.s@greenwichandbarrow.com --json
```

Filter the result for label names matching the user-supplied fragment (case-insensitive substring match). Expected exact match for `auto/...` namespace.

- Zero matches → error: "No label matches '{fragment}'. Run `gog gmail labels list` to see options."
- Multiple matches → ask Kay which one (show name + ID for each candidate).
- One match → proceed with that label ID.

### Step 3 — Find the bundled filter for that label
```bash
gog gmail filters list --account kay.s@greenwichandbarrow.com --json
```

Filter the JSON for filters where `action.addLabelIds` contains the target label ID AND `criteria.query` exists AND query starts with `from:(` (or contains ` OR `). These are the bundled OR-filters.

- Zero bundled filters → **create fresh** (Step 5a).
- Exactly one → proceed (Step 4).
- Multiple → ask Kay which to extend.

### Step 4 — Build extended query

Parse the existing query: strip `from:(` prefix and `)` suffix, split on ` OR `, get the list of emails.

Validation:
- If new email(s) already in the list → report "Already in filter" and stop. No changes.
- Else append new email(s), rebuild query: `from:(addr1 OR addr2 OR ... OR newaddr)`.

### Step 5 — Create new filter, verify, delete old

5a. **Create new filter:**
```bash
gog gmail filters create --account kay.s@greenwichandbarrow.com \
  --query "from:(addr1 OR addr2 OR ... OR newaddr)" \
  --add-label {label_id} --json
```

Capture the new filter ID from the response. If create fails — stop, do NOT touch the old filter. Report the error.

5b. **Verify the new filter exists:**
```bash
gog gmail filters list --account kay.s@greenwichandbarrow.com --json
```

Confirm the new ID is in the list with the expected query.

5c. **Delete the old filter** (only if Step 4 found one to replace):
```bash
gog gmail filters delete --account kay.s@greenwichandbarrow.com --force {old_filter_id}
```

If delete fails: report — Kay can delete manually via Gmail UI. The new filter is already live.

### Step 6 — Report

One-line confirmation to Kay:
```
Added {email} to {label_name}. Filter now contains {N} addresses. (New ID: {new_id}, replaced: {old_id})
```

For fresh creation (no old filter): omit the "replaced" portion.

</workflow>

<error_handling>
- **op bootstrap fails:** Surface to Kay. Likely OP_SERVICE_ACCOUNT_TOKEN expired or 1Password vault renamed.
- **gog keyring auth fails:** Same as above + check `~/.config/op-sa-token.env` exists.
- **Label fragment ambiguous:** Show candidates, ask Kay to pick.
- **Multiple bundled filters for same label:** Show candidates with their query previews, ask Kay which.
- **Create succeeds, verify fails:** Wait 2s and re-list (Gmail eventual consistency). If still missing, surface — do NOT delete old.
- **Create fails:** Stop. Do not touch old filter. Report API error.
- **Delete fails after successful create:** Surface — the new filter is live, but old duplicate remains. Kay can delete via Gmail Settings → Filters → Delete.
</error_handling>

<success_criteria>
- [ ] New filter exists with extended query containing all original emails + new email(s)
- [ ] Old filter deleted (if there was one to replace)
- [ ] Net result: exactly one bundled filter for the target label, containing the new email
- [ ] Kay informed of new filter ID + total address count
</success_criteria>

<edge_cases>
- **Comma vs space in email list:** Accept both. Strip whitespace per email.
- **Mixed-case email:** Preserve case as Kay provided it; Gmail matches case-insensitively anyway.
- **Email format:** Basic sanity check (contains `@` and `.`). Don't block on RFC compliance — Gmail will reject malformed.
- **Adding email already in a 1-off filter (e.g., `from: jniketas@terramarsearch.com`):** Add to bundled filter anyway; the duplicate label-add is harmless. Optionally surface to Kay as a cleanup candidate.
- **Bundled filter has additional criteria** (e.g., `--archive` or `--mark-read`): Preserve them when creating the replacement. Read the full action object and pass equivalent flags. If the action contains anything beyond `addLabelIds`, surface before proceeding so Kay can confirm.
</edge_cases>
