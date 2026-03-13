# gogcli Command Reference

Complete command reference for the `gog` CLI. Source: [steipete/gogcli](https://github.com/steipete/gogcli)

## Global Flags

| Flag | Env Var | Purpose |
|------|---------|---------|
| `--account <email>` | `GOG_ACCOUNT` | Select Google account (or alias) |
| `--client <name>` | `GOG_CLIENT` | Select OAuth client bucket |
| `--json` | `GOG_JSON` | JSON output |
| `--plain` | `GOG_PLAIN` | TSV output |
| `--enable-commands <list>` | `GOG_ENABLE_COMMANDS` | Allowlist top-level commands (sandboxing) |
| `--access-token <token>` | `GOG_ACCESS_TOKEN` | Direct access token (headless/CI) |
| `--no-input` | — | Non-interactive mode |

## Auth

```bash
gog auth credentials <path>                    # Store OAuth client JSON
gog auth credentials list                      # List stored clients
gog --client <name> auth credentials <path>    # Store named client
gog auth add <email>                           # Authorize account (browser flow)
gog auth add <email> --manual                  # Headless/remote flow
gog auth add <email> --services gmail,calendar # Specific services only
gog auth add <email> --readonly                # Read-only scopes
gog auth add <email> --force-consent           # Re-authorize with new scopes
gog auth status                                # Current auth state
gog auth list                                  # List accounts
gog auth list --check                          # Validate tokens
gog auth remove <email>                        # Remove account
gog auth manage                                # Browser account manager
gog auth alias set <alias> <email>             # Create alias
gog auth alias list                            # List aliases
gog auth keyring [backend]                     # Show/set keyring (auto|keychain|file)
gog auth service-account set <email> --key <path>  # Workspace service account
gog auth services                              # List available services + scopes
```

## Gmail

```bash
# Search and read
gog gmail search '<query>' --max 10
gog gmail thread get <threadId>
gog gmail thread get <threadId> --download --out-dir ./attachments
gog gmail get <messageId>
gog gmail url <threadId>
gog gmail thread modify <threadId> --add STARRED --remove INBOX

# Send
gog gmail send --to a@b.com --subject "Hi" --body "Hello"
gog gmail send --to a@b.com --subject "Hi" --body-file ./msg.txt
gog gmail send --to a@b.com --subject "Hi" --body-html "<p>Hello</p>"
gog gmail send --reply-to-message-id <msgId> --quote --to a@b.com --subject "Re: Hi" --body "Reply"
gog gmail send --to a@b.com --subject "Hi" --body-html "<p>Hello</p>" --track

# Drafts
gog gmail drafts list
gog gmail drafts create --to a@b.com --subject "Draft" --body "Body"
gog gmail drafts update <draftId> --subject "Updated" --body "New body"
gog gmail drafts send <draftId>

# Labels
gog gmail labels list
gog gmail labels get INBOX --json
gog gmail labels create "My Label"
gog gmail labels rename "Old" "New"
gog gmail labels delete <labelId>

# Batch
gog gmail batch delete <msgId> <msgId>
gog gmail batch modify <msgId> <msgId> --add STARRED --remove INBOX

# Filters
gog gmail filters list
gog gmail filters create --from 'noreply@ex.com' --add-label 'Notifications'
gog gmail filters delete <filterId>
gog gmail filters export --out ./filters.json

# Settings
gog gmail vacation get
gog gmail vacation enable --subject "OOO" --message "..."
gog gmail vacation disable
gog gmail autoforward get/enable/disable
gog gmail sendas list/create
gog gmail delegates list/add/remove

# Watch (Pub/Sub)
gog gmail watch start --topic projects/<p>/topics/<t> --label INBOX
gog gmail watch serve --bind 127.0.0.1 --token <shared> --hook-url <url>
gog gmail history --since <historyId>
```

## Calendar

```bash
# List
gog calendar calendars
gog calendar events <calId> --today
gog calendar events <calId> --tomorrow
gog calendar events <calId> --week
gog calendar events <calId> --days 3
gog calendar events <calId> --from today --to friday
gog calendar events --all                        # All calendars
gog calendar events --cal Work --cal Personal    # By name
gog calendar search "meeting" --today
gog calendar search "meeting" --days 365

# Create
gog calendar create <calId> --summary "Meeting" --from <start> --to <end>
gog calendar create <calId> --summary "Sync" --from <start> --to <end> \
  --attendees "a@ex.com,b@ex.com" --location "Zoom" --send-updates all

# Update
gog calendar update <calId> <eventId> --summary "New Title" --from <start> --to <end>
gog calendar update <calId> <eventId> --add-attendee "c@ex.com"

# Delete
gog calendar delete <calId> <eventId> --send-updates all --force

# RSVP
gog calendar respond <calId> <eventId> --status accepted|declined|tentative

# Availability
gog calendar freebusy --calendars "primary,work@ex.com" --from <start> --to <end>
gog calendar conflicts --all --today

# Special events
gog calendar focus-time --from <start> --to <end>
gog calendar out-of-office --from <date> --to <date> --all-day
gog calendar working-location --type office --office-label "HQ" --from <date> --to <date>

# Recurrence
gog calendar create <calId> --summary "Payment" --from <start> --to <end> \
  --rrule "RRULE:FREQ=MONTHLY;BYMONTHDAY=11" --reminder "email:3d" --reminder "popup:30m"

# Team
gog calendar team <group-email> --today
gog calendar team <group-email> --freebusy

# Time
gog time now
gog time now --timezone UTC
```

## Drive

```bash
# List and search
gog drive ls --max 20
gog drive ls --parent <folderId> --max 20
gog drive search "invoice" --max 20
gog drive search "mimeType = 'application/pdf'" --raw-query
gog drive get <fileId>
gog drive url <fileId>
gog drive copy <fileId> "Copy Name"

# Upload and download
gog drive upload ./file.pdf --parent <folderId>
gog drive upload ./file.pdf --replace <fileId>       # In-place replace
gog drive upload ./report.docx --convert             # Convert to Google format
gog drive download <fileId> --out ./file.bin
gog drive download <fileId> --format pdf --out ./export.pdf

# Organize
gog drive mkdir "New Folder" --parent <parentId>
gog drive rename <fileId> "New Name"
gog drive move <fileId> --parent <destFolderId>
gog drive delete <fileId>
gog drive delete <fileId> --permanent

# Permissions
gog drive permissions <fileId>
gog drive share <fileId> --to user --email u@ex.com --role reader|writer
gog drive share <fileId> --to domain --domain ex.com --role reader
gog drive unshare <fileId> --permission-id <permId>

# Shared drives
gog drive drives --max 100
```

## Docs

```bash
gog docs info <docId>
gog docs cat <docId>
gog docs cat <docId> --tab "Notes" | --all-tabs
gog docs create "My Doc"
gog docs create "My Doc" --file ./doc.md             # Import markdown
gog docs copy <docId> "Copy Name"
gog docs export <docId> --format pdf|docx|txt|md|html --out ./doc.pdf
gog docs list-tabs <docId>
gog docs update <docId> --text "Append text"
gog docs update <docId> --file ./insert.txt --index 25
gog docs write <docId> --text "Replace all content"
gog docs write <docId> --file ./body.txt --append
gog docs find-replace <docId> "old" "new"
gog docs sed <docId> 's/pattern/replacement/g'       # Regex editing with markdown formatting
```

## Sheets

```bash
# Read
gog sheets metadata <spreadsheetId>
gog sheets get <spreadsheetId> 'Sheet1!A1:B10'
gog sheets get <spreadsheetId> MyNamedRange

# Write
gog sheets update <spreadsheetId> 'A1' 'val1|val2,val3|val4'
gog sheets update <spreadsheetId> 'A1' --values-json '[["a","b"],["c","d"]]'
gog sheets append <spreadsheetId> 'Sheet1!A:C' 'new|row|data'
gog sheets clear <spreadsheetId> 'Sheet1!A1:B10'

# Validation copy (preserves dropdowns/rules from source row)
gog sheets update <spreadsheetId> 'Sheet1!A1:C1' 'data' --copy-validation-from 'Sheet1!A2:C2'
gog sheets append <spreadsheetId> 'Sheet1!A:C' 'data' --copy-validation-from 'Sheet1!A2:C2'

# Format
gog sheets format <spreadsheetId> 'Sheet1!A1:B2' --format-json '{"textFormat":{"bold":true}}' --format-fields 'userEnteredFormat.textFormat.bold'
gog sheets merge <spreadsheetId> 'Sheet1!A1:B2'
gog sheets unmerge <spreadsheetId> 'Sheet1!A1:B2'
gog sheets number-format <spreadsheetId> 'Sheet1!C:C' --type CURRENCY --pattern '$#,##0.00'
gog sheets freeze <spreadsheetId> --rows 1 --cols 1
gog sheets resize-columns <spreadsheetId> 'Sheet1!A:C' --auto

# Named ranges
gog sheets named-ranges <spreadsheetId>
gog sheets named-ranges add <spreadsheetId> MyRange 'Sheet1!A1:B2'

# Structure
gog sheets create "My Spreadsheet" --sheets "Sheet1,Sheet2"
gog sheets copy <spreadsheetId> "Copy Name"
gog sheets export <spreadsheetId> --format pdf|xlsx --out ./sheet.pdf
gog sheets add-tab <spreadsheetId> <tabName>
gog sheets rename-tab <spreadsheetId> <old> <new>
gog sheets delete-tab <spreadsheetId> <tabName> --force
gog sheets insert <spreadsheetId> "Sheet1" rows 2 --count 3
gog sheets insert <spreadsheetId> "Sheet1" cols 3 --after

# Notes and links
gog sheets notes <spreadsheetId> 'Sheet1!A1:B10'
gog sheets update-note <spreadsheetId> 'Sheet1!A1' --note 'My note'
gog sheets links <spreadsheetId> 'Sheet1!A1:B10'
gog sheets find-replace <spreadsheetId> "old" "new" --sheet Sheet1
```

## Slides

```bash
gog slides info <presentationId>
gog slides create "My Deck"
gog slides create-from-markdown "My Deck" --content-file ./slides.md
gog slides create-from-template <templateId> "My Deck" --replace "name=John"
gog slides copy <presentationId> "Copy Name"
gog slides export <presentationId> --format pdf --out ./deck.pdf
gog slides list-slides <presentationId>
gog slides add-slide <presentationId> ./slide.png --notes "Speaker notes"
gog slides update-notes <presentationId> <slideId> --notes "Updated"
gog slides replace-slide <presentationId> <slideId> ./new.png
```

## Contacts

```bash
# Personal
gog contacts list --max 50
gog contacts search "Ada" --max 50
gog contacts get people/<resourceName>
gog contacts get user@example.com

# Other contacts
gog contacts other list --max 50
gog contacts other search "John"

# Create/update
gog contacts create --given "John" --family "Doe" --email "j@ex.com" --phone "+1234567890"
gog contacts update people/<resourceName> --given "Jane" --email "jane@ex.com"
gog contacts delete people/<resourceName>

# Workspace directory
gog contacts directory list --max 50
gog contacts directory search "Jane"
```

## Tasks

```bash
# Task lists
gog tasks lists --max 50
gog tasks lists create <title>

# Tasks
gog tasks list <tasklistId> --max 50
gog tasks get <tasklistId> <taskId>
gog tasks add <tasklistId> --title "Task title"
gog tasks add <tasklistId> --title "Weekly sync" --due 2025-02-01 --repeat weekly --repeat-count 4
gog tasks update <tasklistId> <taskId> --title "New title"
gog tasks done <tasklistId> <taskId>
gog tasks undo <tasklistId> <taskId>
gog tasks delete <tasklistId> <taskId>
gog tasks clear <tasklistId>
```

## Forms

```bash
gog forms get <formId>
gog forms create --title "Check-in" --description "Friday update"
gog forms update <formId> --title "New Title" --quiz true
gog forms add-question <formId> --title "What shipped?" --type paragraph --required
gog forms move-question <formId> 3 1
gog forms delete-question <formId> 2 --force
gog forms responses list <formId> --max 20
gog forms responses get <formId> <responseId>
gog forms watch create <formId> --topic projects/<p>/topics/<t>
```

## Chat (Workspace only)

```bash
# Spaces
gog chat spaces list
gog chat spaces find "Engineering"
gog chat spaces create "Engineering" --member a@co.com --member b@co.com

# Messages
gog chat messages list spaces/<spaceId> --max 5
gog chat messages list spaces/<spaceId> --unread
gog chat messages send spaces/<spaceId> --text "Hello!"
gog chat messages react spaces/<spaceId>/messages/<msgId> "thumbsup"

# Threads
gog chat threads list spaces/<spaceId>

# DMs
gog chat dm space user@company.com
gog chat dm send user@company.com --text "ping"
```

## Classroom (Workspace for Education)

```bash
gog classroom courses list
gog classroom courses get <courseId>
gog classroom courses create --name "Math 101"
gog classroom roster <courseId>
gog classroom coursework list <courseId>
gog classroom coursework create <courseId> --title "HW1" --type ASSIGNMENT --state PUBLISHED
gog classroom submissions list <courseId> <courseworkId>
gog classroom submissions grade <courseId> <courseworkId> <submissionId> --grade 85
gog classroom announcements list <courseId>
gog classroom announcements create <courseId> --text "Welcome!"
gog classroom topics list <courseId>
```

## Keep (Workspace + service account only)

```bash
gog keep list --account you@domain.com
gog keep get <noteId>
gog keep search <query>
gog keep create --title "Todo" --item "Milk" --item "Eggs"
gog keep create --title "Note" --text "Remember this"
gog keep delete <noteId> --force
gog keep attachment <attachmentName> --out ./file.bin
```

## Apps Script

```bash
gog appscript get <scriptId>
gog appscript content <scriptId>
gog appscript create --title "Automation"
gog appscript create --title "Bound" --parent-id <driveFileId>
gog appscript run <scriptId> myFunction --params '["arg1", 123]'
```

## People

```bash
gog people me
gog people get people/<userId>
gog people search "Ada Lovelace" --max 5
gog people relations
gog people relations people/<userId> --type manager
```

## Admin (Workspace + service account)

```bash
gog admin users list --domain example.com
gog admin users get user@example.com
gog admin users create user@ex.com --given Ada --family Lovelace --password 'TempPass!'
gog admin users suspend user@ex.com --force
gog admin groups list --domain example.com
gog admin groups members list eng@ex.com
gog admin groups members add eng@ex.com user@ex.com --role MEMBER
gog admin groups members remove eng@ex.com user@ex.com --force
```

## Groups (Workspace)

```bash
gog groups list
gog groups members engineering@company.com
```

## Config

```bash
gog config path                          # Show config file location
gog config list                          # Show all config
gog config get default_timezone          # Get a key
gog config set default_timezone UTC      # Set a key
gog config unset default_timezone        # Remove a key
```

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `GOG_ACCOUNT` | Default account email or alias |
| `GOG_ACCESS_TOKEN` | Direct access token (CI/headless) |
| `GOG_CLIENT` | OAuth client name |
| `GOG_JSON` | Default JSON output |
| `GOG_PLAIN` | Default plain output |
| `GOG_COLOR` | Color mode: auto, always, never |
| `GOG_TIMEZONE` | Default timezone (IANA/UTC/local) |
| `GOG_ENABLE_COMMANDS` | Command allowlist for sandboxing |
| `GOG_KEYRING_BACKEND` | Keyring backend override |
| `GOG_KEYRING_PASSWORD` | File keyring password (CI) |
