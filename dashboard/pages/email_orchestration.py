"""Email Orchestration page.

Routes email-derived signals into the correct operating workflow while keeping
the hard no-send boundary visible. This page intentionally does not show raw
email bodies or Gmail JSON.
"""

from __future__ import annotations

from html import escape
from textwrap import dedent

import sys
from pathlib import Path

_DASHBOARD_DIR = Path(__file__).resolve().parent.parent
if str(_DASHBOARD_DIR) not in sys.path:
    sys.path.insert(0, str(_DASHBOARD_DIR))

from data_sources import load_email_orchestrator_status  # noqa: E402


def _status_dot(status: str) -> str:
    if status == "ok":
        return "green"
    if status == "warn":
        return "yellow"
    if status == "alert":
        return "red"
    return "grey"


def _status_label(status: str) -> str:
    return {
        "ok": "Ready",
        "warn": "Needs review",
        "alert": "Blocked",
    }.get(status, "Unknown")


def _queue_card(title: str, items: list[str], empty: str, status: str) -> str:
    if items:
        body = "".join(f"<li>{escape(item)}</li>" for item in items[:8])
    else:
        body = f"<li>{escape(empty)}</li>"
    return dedent(
        f"""
        <div class="gb-email-queue">
          <div class="gb-source-group-title">
            <span class="gb-status-dot {_status_dot(status)}"></span>{escape(title)}
          </div>
          <ul>{body}</ul>
        </div>
        """
    ).strip()


def render() -> None:
    import streamlit as st

    email = load_email_orchestrator_status()
    review_items = email.review_count
    fetched = email.fetched_at or "not fetched"
    source = email.source_artifact or "no source artifact"

    st.markdown(
        dedent(
            f"""
            <div class="gb-zone gb-zone-plain">
              <div class="gb-zone-head">
                <div>
                  <div class="gb-zone-label">Email Orchestration</div>
                  <div class="gb-zone-subtitle">Routes email-derived signals into deal flow, relationships, tasks, and Good Morning without sending email</div>
                </div>
                <div class="gb-zone-meta"><span class="gb-status-dot {_status_dot(email.status)}"></span>{escape(_status_label(email.status))}</div>
              </div>
              <div class="gb-deal-status-grid">
                <div><span class="num">{escape(email.source_status)}</span>source</div>
                <div><span class="num">{email.drafts_pending}</span>drafts pending</div>
                <div><span class="num {'red' if email.send_blockers else 'dim'}">{email.send_blockers}</span>send blockers</div>
                <div><span class="num">{email.deal_items}</span>deal items</div>
                <div><span class="num">{email.pipeline_items}</span>pipeline items</div>
                <div><span class="num">{email.relationship_items}</span>relationship items</div>
                <div><span class="num">{email.task_candidates}</span>task candidates</div>
                <div><span class="num {'yellow' if review_items else 'green'}">{review_items}</span>review items</div>
              </div>
              <div class="gb-source-detail" style="margin: 10px 0 14px;">Source: {escape(source)} · fetched {escape(fetched)}</div>
            </div>
            """
        ).strip(),
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gb-email-queues">'
        + _queue_card("Needs Kay", email.needs_kay, "No Kay review items currently surfaced.", "warn" if email.needs_kay else "ok")
        + _queue_card("Blocked", email.blocked, "No email orchestration blockers currently surfaced.", "alert" if email.blocked else "ok")
        + "</div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="gb-page-note">Safety boundary: this page may summarize, route, and expose draft/review status. It must not send email, forward email, schedule-send, or call any Gmail send API.</div>',
        unsafe_allow_html=True,
    )
