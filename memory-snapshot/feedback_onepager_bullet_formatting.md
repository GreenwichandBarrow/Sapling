---
name: One-pager bullet formatting must be consistent
description: python-pptx one-pagers have mixed bullet formatting — some PowerPoint bullets, some text "•" characters. Must use proper paragraph-level bullets only.
type: feedback
---

One-pager bullet points are inconsistent — mixing PowerPoint native bullets with text "•" characters, causing misaligned indentation.

**Why:** Looks unprofessional. Camilla and investors see these.

**How to apply:** When creating pptx with python-pptx, use proper paragraph-level bullet formatting (paragraph.level property) rather than inserting bullet characters as text. All items in a list should use the same formatting method. Match the template's original bullet style.
