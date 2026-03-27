#!/usr/bin/env python3
"""List unreviewed decision traces for calibration workflow."""
import os
import sys
import re
from pathlib import Path

TRACES_DIR = Path(__file__).resolve().parent.parent.parent / "brain" / "traces"

def get_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    content = filepath.read_text(encoding='utf-8')
    if not content.startswith('---'):
        return {}
    end = content.index('---', 3)
    fm_text = content[3:end].strip()
    result = {}
    for line in fm_text.split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            result[key.strip()] = val.strip().strip('"').strip("'")
    return result

def main():
    date_filter = sys.argv[1] if len(sys.argv) > 1 else None

    if not TRACES_DIR.exists():
        print("No traces directory found.")
        sys.exit(0)

    # Find all trace .md files (not in agents/ or processed/ subdirs)
    trace_files = []
    for f in sorted(TRACES_DIR.glob("*.md")):
        if f.name.startswith('.'):
            continue
        trace_files.append(f)

    if not trace_files:
        print("No traces found.")
        print(f"Traces directory: {TRACES_DIR}")
        print("Total: 0 unreviewed traces, 0 decisions, 0 learnings")
        sys.exit(0)

    unreviewed = []
    for f in trace_files:
        fm = get_frontmatter(f)
        review_status = fm.get('review_status', 'pending')
        trace_date = fm.get('date', '')

        # Skip if already reviewed
        if review_status in ('applied', 'skipped'):
            continue

        # Apply date filter if provided
        if date_filter:
            dates = [d.strip() for d in date_filter.replace(' and ', ',').split(',')]
            if trace_date not in dates:
                # Also try matching partial dates (MM-DD)
                short_date = trace_date[5:] if len(trace_date) >= 10 else trace_date
                if not any(short_date.endswith(d) or d == short_date for d in dates):
                    continue

        # Count decisions and learnings in the file
        content = f.read_text(encoding='utf-8')
        decisions = len(re.findall(r'^##\s+Decision', content, re.MULTILINE))
        learnings = len(re.findall(r'^##\s+Learning', content, re.MULTILINE))
        # Also count list items under these headers as individual items
        if decisions == 0:
            decisions = len(re.findall(r'^\s*[-*]\s+\*\*Decision', content, re.MULTILINE))
        if learnings == 0:
            learnings = len(re.findall(r'^\s*[-*]\s+\*\*Learning', content, re.MULTILINE))

        task = fm.get('title', fm.get('task', f.stem))
        target = fm.get('target', 'general')

        unreviewed.append({
            'path': str(f),
            'date': trace_date,
            'task': task,
            'target': target,
            'decisions': max(decisions, 1),  # At least 1 if file exists
            'learnings': max(learnings, 0),
        })

    if not unreviewed:
        print("No unreviewed traces found." + (f" (filter: {date_filter})" if date_filter else ""))
        print(f"Total: 0 unreviewed traces, 0 decisions, 0 learnings")
        sys.exit(0)

    total_decisions = sum(t['decisions'] for t in unreviewed)
    total_learnings = sum(t['learnings'] for t in unreviewed)

    print(f"Found {len(unreviewed)} unreviewed traces:")
    print()
    for t in unreviewed:
        print(f"  {t['path']}")
        print(f"    Date: {t['date']} | Task: {t['task']} | Target: {t['target']}")
        print(f"    Decisions: {t['decisions']} | Learnings: {t['learnings']}")
        print()

    print(f"Total: {len(unreviewed)} unreviewed traces, {total_decisions} decisions, {total_learnings} learnings")

if __name__ == '__main__':
    main()
