<required_reading>
- references/gh-commands.md
</required_reading>

<objective>
Create a new project from a boilerplate repository. Creates new private repo, clones boilerplate, strips git history, pushes fresh to new repo.
</objective>

<when_to_use>
User invokes `/github new-project <name> --from <boilerplate-repo>`
</when_to_use>

<process>
1. **Parse arguments** [LOW freedom]
   Extract:
   - `name`: New project name
   - `boilerplate`: Source repo (`owner/repo` format)

2. **Check authentication** [LOW freedom]
   ```bash
   gh auth status
   ```

3. **Verify boilerplate exists** [LOW freedom]
   ```bash
   gh repo view <boilerplate>
   ```
   If not found, error with helpful message.

4. **Check new repo name available** [LOW freedom]
   ```bash
   gh repo view <name> 2>/dev/null
   ```
   If exists, stop and inform user.

5. **Create new private repository** [LOW freedom]
   ```bash
   gh repo create <name> --private
   ```
   Capture the new repo URL.

6. **Clone boilerplate to temp location** [LOW freedom]
   ```bash
   TEMP_DIR=$(mktemp -d)
   gh repo clone <boilerplate> "$TEMP_DIR/<name>"
   ```

7. **Strip git history** [LOW freedom]
   ```bash
   cd "$TEMP_DIR/<name>"
   rm -rf .git
   ```

8. **Initialize fresh git** [LOW freedom]
   ```bash
   git init
   git add .
   git commit -m "Initial commit from <boilerplate>"
   ```

9. **Add remote and push** [LOW freedom]
   ```bash
   git remote add origin git@github.com:<owner>/<name>.git
   git branch -M main
   git push -u origin main
   ```

10. **Clone to user's home directory** [LOW freedom]
    ```bash
    gh repo clone <owner>/<name> ~/<name>
    rm -rf "$TEMP_DIR"
    ```

11. **Report success** [LOW freedom]
    Show:
    - New repo URL
    - Local path: `~/<name>`
    - Suggest: `cd ~/<name>`
</process>

<error_recovery>
- If any step fails after repo creation, inform user the repo was created but setup incomplete
- Provide manual steps to complete if needed
- Clean up temp directory on failure
</error_recovery>

<success_criteria>
- [ ] New private repo created
- [ ] Boilerplate code copied (no git history)
- [ ] Fresh git history with initial commit
- [ ] Pushed to new remote
- [ ] Cloned to ~/name
</success_criteria>
