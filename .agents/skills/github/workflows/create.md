<required_reading>
- references/gh-commands.md
</required_reading>

<objective>
Create a new private GitHub repository.
</objective>

<when_to_use>
User invokes `/github create <name>`
</when_to_use>

<process>
1. **Parse arguments** [LOW freedom]
   Extract repository name from args.
   Name can be `repo-name` or `org/repo-name`.

2. **Check authentication** [LOW freedom]
   ```bash
   gh auth status
   ```
   If not authenticated, instruct user to run `gh auth login`.

3. **Check if repo exists** [LOW freedom]
   ```bash
   gh repo view <name> 2>/dev/null
   ```
   If exists, inform user and ask if they want to proceed with a different name.

4. **Create repository** [LOW freedom]
   ```bash
   gh repo create <name> --private --description "<optional description>"
   ```

   Default flags:
   - `--private` (always)
   - `--description` (if user provided one)

5. **Report success** [LOW freedom]
   Display the repo URL: `https://github.com/<owner>/<name>`
   Ask if user wants to clone it locally.
</process>

<success_criteria>
- [ ] Repo created as private
- [ ] User sees repo URL
- [ ] Errors handled gracefully
</success_criteria>
