<required_reading>
- references/gh-commands.md
</required_reading>

<objective>
Change the visibility of an existing GitHub repository.
</objective>

<when_to_use>
User invokes `/github visibility <repo> <public|private>`
</when_to_use>

<process>
1. **Parse arguments** [LOW freedom]
   Extract:
   - Repository name (`owner/repo` or `repo`)
   - Target visibility (`public` or `private`)

2. **Check authentication** [LOW freedom]
   ```bash
   gh auth status
   ```

3. **Verify repo exists and user has access** [LOW freedom]
   ```bash
   gh repo view <repo> --json visibility
   ```
   Show current visibility to user.

4. **Confirm change** [LOW freedom]
   **Critical**: Changing to public exposes all code.
   If changing to public, warn user:
   > "This will make the repository publicly visible. All code, issues, and history will be accessible. Continue?"

5. **Change visibility** [LOW freedom]
   ```bash
   gh repo edit <repo> --visibility <public|private> --accept-visibility-change-consequences
   ```

6. **Report success** [LOW freedom]
   Confirm new visibility.
   Show repo URL.
</process>

<success_criteria>
- [ ] Visibility changed
- [ ] User warned before making public
- [ ] Confirmation of new state
</success_criteria>
