---
description: Launch the G&B Command Center dashboard (Streamlit, localhost:8501)
---

Launch the Command Center dashboard.

**Steps:**
1. Check whether the dashboard is already running: `lsof -i :8501 2>/dev/null | grep LISTEN`
2. If already running, tell Kay the URL (http://localhost:8501) and stop — don't start a second instance.
3. If not running, start it in the background using the venv:
   ```bash
   cd "/Users/kaycschneider/Documents/AI Operations" && \
     dashboard/.venv/bin/streamlit run dashboard/command_center.py \
     --server.headless true --server.port 8501 \
     > logs/dashboard-streamlit.log 2>&1 &
   ```
   Make sure `logs/` exists first (`mkdir -p logs`).
4. Wait ~3 seconds, then confirm it's serving with `curl -s -o /dev/null -w "%{http_code}" http://localhost:8501`.
5. Tell Kay it's live at http://localhost:8501 and note that refresh polling is every 60s.

**Scope & visual reference:**
- Scope doc: `brain/context/continuation-2026-04-24-dashboard-scope-locked.md`
- Visual language memory: `memory/feedback_dashboard_visual_language_locked.md`
- Mockups: `dashboard/mockup-landing.html`, `dashboard/mockup-deal-aggregator.html`

**If launch fails:** read `logs/dashboard-streamlit.log` and surface the error. Don't attempt to reinstall dependencies without asking — the venv at `dashboard/.venv` was set up in Session 1 and should not be recreated casually.
