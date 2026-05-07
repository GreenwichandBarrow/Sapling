---
name: Google Doc formatting standards
description: All Google Docs created for Kay must use G&B letterhead, Avenir font, black text only (never blue). Apply letterhead from Master Templates.
type: feedback
---

All Google Docs created for Kay must follow these formatting rules:

- **Letterhead:** Use the G&B letterhead from Master Templates (`G&B Letterhead Template`, native Google Doc, ID: `1hXnexnOTDQwAo4lII2kbsPY3IsbcfKyaJthrAPjGb78`). The original `.docx` (ID `1PLYz2WH4Zqy4h2gYVqC8SVGyDrvy_ILF`, renamed to archive) is preserved for Word/Pages workflows but is NOT copyable via `gog drive copy` for native-Doc edits.
- **Logo placement:** Always centered on the page
- **Font:** Avenir (all text, all sizes, headings and body)
- **Font color:** Black only. NEVER blue. NEVER any other color.
- **Shading/highlights:** NONE. No blue shading, no colored header rows, no colored backgrounds. Everything black and white.
- **Tables:** Black borders on white background. Bold header text is fine, but NO colored shading on header rows.
- **If a template already exists:** Use the template (it already has letterhead/formatting)
- **If no template exists:** Start from the letterhead doc as the base, then add content

**Why:** Kay's strong preference. Black and white only, Avenir font, G&B letterhead. No exceptions.

**How to apply:**
- All Master Templates were manually formatted by Kay on 3/20/2026. They are now the source of truth for formatting.
- When creating a new Google Doc, ALWAYS copy from a template (`gog docs create` or `gog drive copy`) so it inherits the formatting.
- For docs created without a template, run `python3 scripts/format-gdoc.py <doc_id> --all` to apply brand standards.
- The formatter uses the G&B FULL LOGO ON WHT.png (Drive ID: `1YNyoG3uWRhDX2z7-wlhm941rb9VO_jc6`) — the monogram with GREENWICH & BARROW text.
- When generating .docx with python-docx, do NOT add shading/fill colors to table rows. Use 'Table Grid' style with no modifications.
