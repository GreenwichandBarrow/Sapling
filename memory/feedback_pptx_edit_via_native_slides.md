---
name: feedback-pptx-edit-via-native-slides
description: "To edit a deck live, convert .pptx to native Google Slides and edit via gog slides API — .pptx in Drive only renders (cache-laggy) in the Slides UI"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: cc01242c-29bf-4bfa-9909-e5f21886ab38
---

A **.pptx** file stored in Drive is only *rendered* (not natively editable) by the Google Slides UI, and the render caches — edits pushed to the .pptx (via python-pptx + re-upload) do not reliably show up for Kay even when the file content is correct. This burned a long confusion loop on the pest deck (Kay: "I dont see any new slides").

**Fix:** Convert to a **native Google Slides** file once (`gog drive upload <file.pptx> --convert --parent=<folderId>`), then make all subsequent edits through the **`gog slides`** API (`replace-text`, `read-slide`, etc.) so changes appear in Kay's browser instantly. Native Slides is the live editing target; keep the .pptx only as a source/backup.

**Why:** Kay edits Drive docs directly and expects to see updates on refresh. The .pptx render lag makes it look like nothing landed.

**How to apply:** When a deliverable deck needs iterative live editing with Kay, make the working file native Google Slides from the start. Related gotcha: `gog drive upload --replace=<id>` must use **equals syntax** — space-separated `--replace <id>` silently no-ops. See [[feedback_gog_drive_replace_equals_syntax]].
