"""Week Archive page — historical weekly tracker snapshots.

Phase E of the dashboard-as-source pivot. Lists every `brain/trackers/weekly/
*-weekly-tracker.md` file via a sidebar dropdown; selecting one renders that
week's metrics + tables. Replaces the manual habit of opening the vault file
to read prior weeks.

The dashboard's M&A Analytics page is always "this week's running view";
this page is the time-machine. Same metrics, frozen in time, scrollable.
"""

from __future__ import annotations

import re
from datetime import date
from html import escape
from pathlib import Path

import sys
_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import WEEKLY_TRACKERS_DIR  # noqa: E402

_FILENAME_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-weekly-tracker\.md$")


def _list_snapshots() -> list[tuple[date, Path]]:
    """Return [(week_ending, path), ...] sorted newest first."""
    if not WEEKLY_TRACKERS_DIR.exists():
        return []
    out: list[tuple[date, Path]] = []
    for entry in WEEKLY_TRACKERS_DIR.iterdir():
        m = _FILENAME_RE.match(entry.name)
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        out.append((d, entry))
    out.sort(key=lambda t: t[0], reverse=True)
    return out


def _strip_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body) for an Obsidian-style markdown file."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end]
    body = text[end + 4:].lstrip("\n")
    fm: dict = {}
    for line in fm_block.splitlines():
        if ":" not in line:
            continue
        k, _, v = line.partition(":")
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def _render_subtitle(count: int, selected: date | None) -> str:
    if count == 0:
        return (
            '<div class="gb-subtitle">'
            "No weekly snapshots in <code>brain/trackers/weekly/</code> yet. "
            'Friday 22:00 ET launchd job <span class="highlight">'
            "<code>com.greenwich-barrow.weekly-snapshot</code></span> writes "
            "the first one — file appears here automatically."
            "</div>"
        )
    sel = selected.strftime("%b %-d, %Y") if selected else "—"
    return (
        '<div class="gb-subtitle">'
        f"{count} historical snapshots · "
        f'<span class="highlight">currently viewing week ending {escape(sel)}</span>. '
        "Same metrics as M&amp;A Analytics, frozen in time."
        "</div>"
    )


def render() -> None:
    import streamlit as st

    snapshots = _list_snapshots()

    if not snapshots:
        st.markdown(_render_subtitle(0, None), unsafe_allow_html=True)
        return

    # Sidebar dropdown — date label + filename. Newest default.
    options = [d for d, _ in snapshots]
    labels = {d: d.strftime("Week ending %b %-d, %Y") for d in options}

    with st.sidebar:
        st.markdown('<div class="gb-archive-picker">', unsafe_allow_html=True)
        st.markdown(
            '<div class="gb-archive-picker-label">WEEK ARCHIVE</div>',
            unsafe_allow_html=True,
        )
        selected = st.selectbox(
            "Select week",
            options=options,
            format_func=lambda d: labels[d],
            label_visibility="collapsed",
            key="week_archive_select",
        )
        st.markdown("</div>", unsafe_allow_html=True)

    path = next(p for d, p in snapshots if d == selected)
    try:
        text = path.read_text(errors="replace")
    except OSError as exc:
        st.error(f"Failed to read {path}: {exc}")
        return

    fm, body = _strip_frontmatter(text)

    st.markdown(_render_subtitle(len(snapshots), selected), unsafe_allow_html=True)

    # Source provenance pill — distinguishes new (dashboard-snapshot) vs legacy.
    schema_version = fm.get("schema_version", "?").strip('"')
    source = (
        "dashboard-snapshot" if schema_version == "2.0.0" else "legacy weekly-tracker"
    )
    pill_class = "" if schema_version == "2.0.0" else " yellow"
    st.markdown(
        f'<div class="gb-archive-meta">'
        f'<span class="pill{pill_class}">schema {schema_version} · {escape(source)}</span> '
        f'<code>{escape(str(path.relative_to(WEEKLY_TRACKERS_DIR.parent.parent)))}</code>'
        f"</div>",
        unsafe_allow_html=True,
    )

    # Render the markdown body directly. Streamlit handles tables + headings
    # cleanly — no need to re-skin into KPI tiles for v1.
    st.markdown(body, unsafe_allow_html=False)

    st.markdown(
        '<div class="gb-page-note">Source file: <code>'
        f"brain/trackers/weekly/{escape(path.name)}</code>. "
        "New snapshots land Fridays at 22:00 ET via the "
        "<code>com.greenwich-barrow.weekly-snapshot</code> launchd job."
        "</div>",
        unsafe_allow_html=True,
    )
