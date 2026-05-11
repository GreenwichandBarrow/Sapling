---
name: One-pager creation method — clone working file, swap text
description: Always clone a working one-pager pptx (Art Advisory) and replace text in existing runs. Never build from the raw template.
type: feedback
---

When creating new one-pager pptx files, ALWAYS clone a known-working one-pager (Art Advisory March 2026 is the gold standard) and replace only the text in existing runs. Never build from the raw customs-bonds template — it produces white-on-white invisible text in Google Slides.

**Why:** Three attempts at template-based generation failed. The template's run formatting chain breaks when python-pptx creates new runs. Cloning a working file preserves all formatting, merged cells, and color rendering.

**How to apply:**
1. Download Art Advisory one-pager: `gog drive download 1GDBgRyNWJ2vGn7niEeqjrAGfyqPRK9eX`
2. Open with python-pptx
3. For each cell `(row, col)`, find `cell.text_frame.paragraphs[0].runs[0]` and set `.text`
4. Clear subsequent runs/paragraphs
5. Save and upload
6. Google Slides format is also acceptable if pptx keeps fighting
