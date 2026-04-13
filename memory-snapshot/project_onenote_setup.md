---
name: OneNote MCP — Working with Known Bug
description: OneNote MCP connected to SEARCH FUND notebook, auth works, but getPage returns wrong content (known bug)
type: project
---

**Status:** Auth works, listNotebooks/listSections/listPages/searchPages work. **getPage has a bug** — returns the same page content regardless of which page ID is requested. Needs fixing.

**Notebook:** SEARCH FUND (hardcoded filter in onenote-mcp.mjs)

**17 Sections:** ACQUISITIONS I ADMIRE, COMPANY MEMOS, DEAL CONV, G AND B, G I B INVESTORS CONVOS, INDUSTRY CONFERENCE LISTS, INDUSTRY MEMOS, INTERMEDIARY CONVOS, INTERMEDIARY MEMOS, INVESTOR CONVOS, MISC CONVOS, OPERATOR CONVOS, R AND D - OPERATING STAGE, R AND D - PRE-SEARCH, R AND D - SEARCH STAGE, SEARCHER CONVOS, SUPPORT TEAM CONVOS

**Auth:** Direct OAuth2 device code flow. Tokens expire ~1hr — re-auth needed each session.

**Integration:** hist-onenote sub-agent in niche-intel HISTORICAL orchestrator. Auth expired during 3/21 pipeline test so OneNote was skipped.

**Known Issues:**
- getPage returns wrong content (same Mike Horowitz page every time) — MCP bug
- Superhuman MCP was dropped from .mcp.json when OneNote was added — re-added 3/21
