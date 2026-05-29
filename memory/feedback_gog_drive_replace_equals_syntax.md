---
name: gog-drive-upload-replace-requires-equals-syntax-not-space
description: "gog drive upload --replace flag silently fails with space-separated value; only --replace=ID (equals syntax) actually replaces the file content. Wasted multiple iterations on 5/27/26 pest deck because tool reported \"replaced: true\" but file content stayed unchanged."
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 5952a433-25a2-4f31-9d05-17a51b2ce6f0
---

`gog drive upload <localPath> --replace <fileId>` (space-separated) SILENTLY FAILS — the tool returns `replaced: true` and `id` matching the target file, but the Drive file's content does not actually change. The upload appears to land in a phantom revision the API drops.

**Working syntax:** `gog drive upload <localPath> --replace=<fileId>` (equals-separated)

**Why:** Tool's flag parser treats the space-separated value as a positional argument rather than the --replace value. The bug is silent — exit code 0, success message, no warning.

**How to apply:**
- ALWAYS use `--replace=ID` (equals syntax) when replacing Drive file content via gog.
- After ANY `gog drive upload --replace` operation, verify by re-downloading and checking file size or content sample — never trust the "replaced: true" output alone.
- Incident: 2026-05-27 pest CIM deck rebuild — 4 silent failures before catching it; cost ~30 minutes and Kay saw stale insurance content in her browser repeatedly.

**Verification pattern:**
```bash
gog drive upload /tmp/file.pptx --replace=FILE_ID
gog drive download FILE_ID --out /tmp/verify.pptx
ls -la /tmp/file.pptx /tmp/verify.pptx  # sizes should match
# or grep for new content
```

Related: [[feedback_check_before_claiming_artifact]] — always verify the live artifact landed before reporting success.
