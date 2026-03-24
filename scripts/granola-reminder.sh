#!/bin/bash
# Granola Reminder — checks calendar every 5 min, sends Slack reminder
# for in-person meetings (no Zoom/Meet/Teams) starting in the next 10 minutes.
#
# Idempotent: tracks sent reminders in a daily temp file to avoid duplicates.
# Designed to run via launchd every 5 minutes during business hours.

set -euo pipefail

# --- Config ---
WORKDIR="$HOME/Documents/AI Operations"
GOG_ACCOUNT="kay.s@greenwichandbarrow.com"
SENT_FILE="/tmp/granola-reminders-$(date +%Y-%m-%d).txt"
LOG_DIR="$WORKDIR/logs/scheduled"
LOG_FILE="$LOG_DIR/granola-reminder-$(date +%Y-%m-%d).log"

# Source env (launchd doesn't read .zshrc)
if [ -f "$WORKDIR/scripts/.env.launchd" ]; then
  source "$WORKDIR/scripts/.env.launchd"
fi

# Ensure log dir + sent file exist
mkdir -p "$LOG_DIR"
touch "$SENT_FILE"

# Rotate old logs (14 days)
find "$LOG_DIR" -name "granola-reminder-*.log" -mtime +14 -delete 2>/dev/null || true
# Clean up old sent files
find /tmp -name "granola-reminders-*.txt" -mtime +1 -delete 2>/dev/null || true

log() {
  echo "[$(date '+%H:%M:%S')] $*" >> "$LOG_FILE"
}

# Business hours gate: Mon-Fri 8am-7pm ET only
CURRENT_HOUR=$(TZ="America/New_York" date +%H | sed 's/^0//')
CURRENT_DOW=$(TZ="America/New_York" date +%u)  # 1=Mon, 7=Sun
if [ "$CURRENT_DOW" -gt 5 ] || [ "$CURRENT_HOUR" -lt 8 ] || [ "$CURRENT_HOUR" -ge 19 ]; then
  # Outside business hours — skip silently
  exit 0
fi

log "Checking calendar for upcoming in-person meetings..."

# Fetch events starting in the next 15 minutes
NOW_EPOCH=$(date +%s)
WINDOW_START_RFC3339=$(date -u +%Y-%m-%dT%H:%M:%SZ)
WINDOW_END_EPOCH=$((NOW_EPOCH + 900))  # 15 minutes
WINDOW_END_RFC3339=$(date -u -r "$WINDOW_END_EPOCH" +%Y-%m-%dT%H:%M:%SZ)

EVENTS_JSON=$(/opt/homebrew/bin/gog calendar list \
  --account="$GOG_ACCOUNT" \
  --from="$WINDOW_START_RFC3339" \
  --to="$WINDOW_END_RFC3339" \
  --json \
  --max=10 2>/dev/null) || {
  log "ERROR: gog calendar list failed"
  exit 0  # Don't fail launchd job
}

# Parse events: filter out all-day events and virtual meetings
# An event is "in-person" if it:
#   1. Has a dateTime (not all-day)
#   2. Has NO conferenceData
#   3. Has NO hangoutLink
#   4. Description/location doesn't contain zoom/meet/teams/webex URLs
MEETINGS=$(echo "$EVENTS_JSON" | /usr/bin/jq -r '
  .events // [] | map(
    select(
      # Must have a specific time (not all-day)
      .start.dateTime != null
      # No conference data
      and .conferenceData == null
      and .hangoutLink == null
      # No virtual meeting keywords in description or location
      and ((.description // "") | test("zoom\\.us|meet\\.google|teams\\.microsoft|webex\\.com|whereby\\.com"; "i") | not)
      and ((.location // "") | test("zoom\\.us|meet\\.google|teams\\.microsoft|webex\\.com|whereby\\.com"; "i") | not)
      # Not cancelled
      and .status != "cancelled"
    )
  ) | .[] | {
    id: .id,
    summary: (.summary // "Untitled Meeting"),
    startTime: .start.dateTime
  }
' 2>/dev/null) || {
  log "No events found or parse error"
  exit 0
}

if [ -z "$MEETINGS" ]; then
  log "No in-person meetings in the next 15 minutes"
  exit 0
fi

# Process each meeting
echo "$MEETINGS" | /usr/bin/jq -c '.' | while read -r meeting; do
  EVENT_ID=$(echo "$meeting" | /usr/bin/jq -r '.id')
  SUMMARY=$(echo "$meeting" | /usr/bin/jq -r '.summary')
  START_TIME=$(echo "$meeting" | /usr/bin/jq -r '.startTime')

  # Check if already reminded
  if grep -qF "$EVENT_ID" "$SENT_FILE" 2>/dev/null; then
    log "Already sent reminder for: $SUMMARY ($EVENT_ID)"
    continue
  fi

  # Format time for display (e.g., "9:30 AM")
  DISPLAY_TIME=$(date -j -f "%Y-%m-%dT%H:%M:%S%z" "$(echo "$START_TIME" | sed 's/:\([0-9][0-9]\)$/\1/')" "+%-I:%M %p" 2>/dev/null || echo "$START_TIME")

  # Send Slack notification
  SLACK_MSG="🎙️ Granola reminder: Turn on Granola before your ${SUMMARY} at ${DISPLAY_TIME}"

  RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$SLACK_WEBHOOK_OPERATIONS" \
    -H 'Content-Type: application/json' \
    -d "{\"text\":$(echo "$SLACK_MSG" | /usr/bin/jq -Rs '.')}" 2>/dev/null)

  if [ "$RESPONSE" = "200" ]; then
    # Mark as sent
    echo "$EVENT_ID" >> "$SENT_FILE"
    log "Sent reminder: $SUMMARY at $DISPLAY_TIME"
  else
    log "ERROR: Slack send failed (HTTP $RESPONSE) for: $SUMMARY"
  fi
done

log "Check complete"
