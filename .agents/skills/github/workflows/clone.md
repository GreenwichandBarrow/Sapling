<required_reading>
- references/gh-commands.md
</required_reading>

<objective>
Clone a GitHub repository locally.
</objective>

<when_to_use>
User invokes `/github clone <repo>`
</when_to_use>

<process>
1. **Parse arguments** [LOW freedom]
   Extract repository identifier. Accepts:
   - `owner/repo`
   - `repo` (assumes current authenticated user)
   - `https://github.com/owner/repo`
   - `git@github.com:owner/repo.git`

2. **Check authentication** [LOW freedom]
   ```bash
   gh auth status
   ```

3. **Determine clone location** [MEDIUM freedom]
   Default: Clone to current directory.
   If user specifies path, use that.
   If cloning to home, use `~/<repo-name>`.

4. **Clone repository** [LOW freedom]
   ```bash
   gh repo clone <repo> [<directory>]
   ```

5. **Report success** [LOW freedom]
   Show:
   - Local path where cloned
   - Suggest `cd <path>` command
</process>

<success_criteria>
- [ ] Repo cloned to local filesystem
- [ ] User knows where to find it
</success_criteria>
