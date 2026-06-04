"""Memory handler: vault search stub with extension points.

This is a no-op stub. To enable memory recall on UserPromptSubmit,
plug in your preferred vault search tool:

- OBX (Go binary): https://github.com/zach-snell/obx
  Standalone, works directly on vault files, no Obsidian needed.
  Supports fuzzy search, regex, tag queries, frontmatter filtering.

- obsidiantools (Python library): pip install obsidiantools
  Rich programmatic access (backlinks, graph analysis, frontmatter).
  Needs a thin CLI wrapper for hook use.

- Custom: implement memory_recall() to query your vault and return
  HandlerResult with additional_context for context injection.
"""

from ..models import HandlerResult


def memory_recall(input_data: dict) -> HandlerResult:
    """UserPromptSubmit: memory recall stub.

    Extension point: plug in your preferred vault search tool here.
    Replace this function body with your implementation.

    Expected input_data keys:
        - prompt (str): the user's prompt text

    Expected return:
        - HandlerResult with additional_context containing relevant vault context
        - None to skip (no context to inject)
    """
    return None
