---
name: Always check for existing files before Drive upload
description: Check if file exists in target folder before uploading to avoid duplicates. Delete or replace, never create second copy.
type: feedback
---

Before uploading ANY file to Google Drive, always check the target folder for an existing file with the same or similar name. If one exists, either delete it first or use an update/replace operation. Never create duplicates.

**Why:** Kay flagged this as a recurring problem. Duplicate files in niche folders create confusion about which version is current.

**How to apply:**
1. Before `gog drive upload`, run `gog drive ls --parent {folder_id}` 
2. Check if a file with the same name (or close match) exists
3. If yes: delete the old one first (`gog drive rm {id} -y`), then upload
4. If no: upload directly
