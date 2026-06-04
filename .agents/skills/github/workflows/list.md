<required_reading>
- references/gh-commands.md
</required_reading>

<objective>
List repositories for the authenticated user or a specified owner.
</objective>

<when_to_use>
User invokes `/github list` or asks "what repos do I have?"
</when_to_use>

<process>
1. **Check authentication** [LOW freedom]
   ```bash
   gh auth status
   ```

2. **Determine scope** [MEDIUM freedom]
   Default: List user's own repos.
   If user specifies an org/owner, list that instead.

3. **List repositories** [LOW freedom]
   ```bash
   # List own repos (default 30)
   gh repo list --limit 50

   # List specific owner's repos
   gh repo list <owner> --limit 50

   # Filter by visibility
   gh repo list --visibility private
   gh repo list --visibility public

   # Show only source repos (not forks)
   gh repo list --source

   # JSON output for parsing
   gh repo list --json name,visibility,updatedAt,description
   ```

4. **Format output** [MEDIUM freedom]
   Present as a readable list showing:
   - Repository name
   - Visibility (public/private)
   - Description (if any)
   - Last updated

   Group by visibility if helpful.
</process>

<common_filters>
| Filter | Command |
|--------|---------|
| Private only | `--visibility private` |
| Public only | `--visibility public` |
| Exclude forks | `--source` |
| Only forks | `--fork` |
| By language | `--language python` |
| Archived | `--archived` |
</common_filters>

<success_criteria>
- [ ] Repos listed with visibility status
- [ ] Output is readable and organized
</success_criteria>
