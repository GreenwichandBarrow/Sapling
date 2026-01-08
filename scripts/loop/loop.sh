#!/bin/bash
set -e

# Loop Agent - AFK Multi-Iteration Mode
# Runs Claude Code in a loop until all tasks complete or max iterations reached
# Uses beads for task management - each story is a bead tagged with loop/{session}

MAX_ITERATIONS=${1:-25}
SESSION_NAME=${2:-"default"}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export SESSION_NAME

echo "🤖 Starting Loop Agent (AFK Mode)"
echo "📊 Max iterations: $MAX_ITERATIONS"
echo "🏷️  Session: $SESSION_NAME"
echo "📁 Working directory: $SCRIPT_DIR"
echo ""

# Initialize progress file if it doesn't exist
PROGRESS_FILE="$SCRIPT_DIR/progress-${SESSION_NAME}.txt"
if [ ! -f "$PROGRESS_FILE" ]; then
  echo "# Progress: $SESSION_NAME" > "$PROGRESS_FILE"
  echo "" >> "$PROGRESS_FILE"
  echo "## Codebase Patterns" >> "$PROGRESS_FILE"
  echo "(Add patterns discovered during implementation here)" >> "$PROGRESS_FILE"
  echo "" >> "$PROGRESS_FILE"
  echo "---" >> "$PROGRESS_FILE"
  echo "" >> "$PROGRESS_FILE"
fi

for i in $(seq 1 $MAX_ITERATIONS); do
  echo "═══════════════════════════════════════"
  echo "    Iteration $i of $MAX_ITERATIONS"
  echo "    Session: $SESSION_NAME"
  echo "═══════════════════════════════════════"
  echo ""

  # Check if any work remains BEFORE starting iteration
  REMAINING=$(bd ready --tag="loop/$SESSION_NAME" 2>/dev/null | grep -c "^" || echo "0")
  if [ "$REMAINING" -eq 0 ]; then
    echo ""
    echo "✅ All tasks complete!"
    echo "🎉 Loop agent finished successfully"
    exit 0
  fi

  echo "📋 $REMAINING stories remaining"
  echo ""

  # Pipe prompt into Claude Code with session context substituted
  OUTPUT=$(cat "$SCRIPT_DIR/prompt.md" \
    | sed "s/\${SESSION_NAME}/$SESSION_NAME/g" \
    | claude --model opus --dangerously-skip-permissions 2>&1 \
    | tee /dev/stderr) || true

  # Check for completion signal (backup check)
  if echo "$OUTPUT" | grep -q "<promise>COMPLETE</promise>"; then
    echo ""
    echo "✅ All tasks complete!"
    echo "🎉 Loop agent finished successfully"
    exit 0
  fi

  echo ""
  echo "⏳ Waiting 3 seconds before next iteration..."
  sleep 3
done

echo ""
echo "⚠️  Maximum iterations ($MAX_ITERATIONS) reached"
echo "📝 Check progress-${SESSION_NAME}.txt for status"
echo "💡 Run with higher limit: ./loop.sh 50 $SESSION_NAME"
exit 1
