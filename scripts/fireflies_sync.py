#!/usr/bin/env python3
"""One-time Fireflies.ai → brain/calls/ sync script."""

import json
import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

API_KEY = os.environ.get("FIREFLIES_API_KEY", "d8f7aba5-557b-45e5-bad2-354678e5e305")
API_URL = "https://api.fireflies.ai/graphql"
BRAIN = Path(__file__).resolve().parent.parent / "brain"
CALLS_DIR = BRAIN / "calls"
ENTITIES_DIR = BRAIN / "entities"

# Known email → company mappings
COMPANY_MAP = {
    "greenwichandbarrow.com": ("greenwich-and-barrow", "Greenwich & Barrow", "internal"),
    "dododigital.ai": ("dodo-digital", "Dodo Digital", "partner"),
    "startvirtual.com": ("start-virtual", "StartVirtual", "partner"),
    "plexuscap.com": ("plexus-capital", "Plexus Capital", "prospect"),
    "magratheapartners.com": ("magrathea-partners", "Magrathea Partners", "prospect"),
    "ashfordventures.com": ("ashford-ventures", "Ashford Ventures", "prospect"),
    "njbsoft.com": ("njbsoft", "NJBSoft", "prospect"),
}


def graphql(query, variables=None):
    import subprocess
    payload = json.dumps({"query": query, "variables": variables or {}})
    result = subprocess.run(
        [
            "curl", "-s", "-X", "POST", API_URL,
            "-H", "Content-Type: application/json",
            "-H", f"Authorization: Bearer {API_KEY}",
            "-d", payload,
        ],
        capture_output=True, text=True, timeout=60,
    )
    if result.returncode != 0:
        raise RuntimeError(f"curl failed: {result.stderr}")
    return json.loads(result.stdout)


def slugify(name):
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")


def ms_to_date(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def format_duration(minutes):
    if minutes < 1:
        return "< 1 min"
    return f"{int(minutes)} min"


def get_company_from_email(email):
    if not email:
        return None
    domain = email.split("@")[-1].lower()
    return COMPANY_MAP.get(domain)


def ensure_entity(slug, name, entity_type="person", email=None, company_slug=None, company_name=None, status="prospect"):
    path = ENTITIES_DIR / f"{slug}.md"
    if path.exists():
        return

    today = datetime.now().strftime("%Y-%m-%d")
    tags = [f"date/{today}", "entity", entity_type, f"{entity_type}/{slug}"]

    company_line = ""
    if entity_type == "person" and company_slug:
        company_line = f'company: "[[entities/{company_slug}]]"\n'
        tags.append(f"company/{company_slug}")

    email_line = ""
    if email:
        email_line = f"email: {email}\n"

    if entity_type == "person" and company_slug:
        status_val = COMPANY_MAP.get(email.split("@")[-1].lower(), (None, None, "prospect"))[2] if email else "prospect"
    elif entity_type == "company":
        status_val = status
    else:
        status_val = status

    tags_str = "\n".join(f"    - {t}" for t in tags)

    if entity_type == "person":
        body = f"""# {name}

## Quick Facts
- Contact from Fireflies calls
{f'- Works at [[entities/{company_slug}|{company_name}]]' if company_slug else ''}

## Communication Style
- **Tone:** TBD
- **Format:** TBD
- **Frequency:** TBD

## Key Context
- Imported from Fireflies call recordings
"""
    else:
        body = f"""# {name}

## Quick Facts
- Organization from Fireflies calls

## Communication Style
- **Tone:** TBD
- **Format:** TBD
- **Frequency:** TBD

## Key Context
- Imported from Fireflies call recordings
"""

    content = f"""---
schema_version: "1.1.0"
date: {today}
type: {entity_type}
status: {status_val}
{company_line}{email_line}tags:
{tags_str}
---

{body}"""

    path.write_text(content)
    print(f"  Created entity: {slug} ({name})")


def classify_call(participants, organizer_email, speakers):
    """Classify call type based on participants."""
    domains = set()
    for p in (participants or []):
        if "@" in p:
            domains.add(p.split("@")[-1].lower())

    if not domains or domains == {"greenwichandbarrow.com"}:
        return "internal"

    for d in domains:
        info = COMPANY_MAP.get(d)
        if info and info[2] == "partner":
            return "partner"

    return "client"


def fetch_all_transcripts():
    """Fetch list of all transcripts."""
    result = graphql("""{
        transcripts {
            id title date organizer_email participants duration
            speakers { name }
        }
    }""")
    return result["data"]["transcripts"]


def fetch_transcript_detail(tid):
    """Fetch full detail for a single transcript."""
    result = graphql("""query($id: String!) {
        transcript(id: $id) {
            id title date organizer_email participants duration
            speakers { name }
            summary {
                overview action_items shorthand_bullet outline
                short_summary keywords
            }
            sentences { speaker_name text start_time end_time }
            audio_url video_url transcript_url
        }
    }""", {"id": tid})
    return result["data"]["transcript"]


def deduplicate(transcripts):
    """Keep the longer transcript when duplicates exist (same title + date)."""
    seen = {}
    for t in transcripts:
        key = (t["title"], t["date"])
        if key not in seen or (t["duration"] or 0) > (seen[key]["duration"] or 0):
            seen[key] = t
    return list(seen.values())


def format_transcript_text(sentences):
    """Format sentences into readable transcript."""
    if not sentences:
        return "*No transcript available.*"

    lines = []
    current_speaker = None
    for s in sentences:
        speaker = s.get("speaker_name", "Unknown")
        text = s.get("text", "").strip()
        if not text:
            continue
        if speaker != current_speaker:
            if lines:
                lines.append("")
            lines.append(f"**{speaker}:** {text}")
            current_speaker = speaker
        else:
            lines.append(text)

    return "\n".join(lines)


def create_call_file(t):
    """Create a call markdown file from transcript data."""
    date_str = ms_to_date(t["date"])
    title_slug = slugify(t["title"])[:50]
    filename = f"{date_str}-{title_slug}.md"
    filepath = CALLS_DIR / filename

    if filepath.exists():
        print(f"  Skipping (exists): {filename}")
        return

    # Gather speaker/people info
    speaker_names = [s["name"] for s in (t.get("speakers") or []) if s.get("name")]
    # Deduplicate speakers
    speaker_names = list(dict.fromkeys(speaker_names))

    participant_emails = t.get("participants") or []

    # Build people list and ensure entities
    people_slugs = []
    people_links = []
    companies_slugs = set()
    companies_links = set()

    # Map emails to speaker names where possible
    email_map = {}
    for email in participant_emails:
        if "@" in email:
            email_map[email] = email

    for name in speaker_names:
        slug = slugify(name)
        if not slug or slug == "1-626-710-6172":  # Skip phone numbers
            continue
        people_slugs.append(slug)
        people_links.append(f'"[[entities/{slug}]]"')

        # Try to find email for this person
        person_email = None
        for email in participant_emails:
            email_lower = email.lower()
            name_parts = name.lower().split()
            if any(part in email_lower for part in name_parts if len(part) > 2):
                person_email = email
                break

        # Get company info
        company_info = None
        if person_email:
            company_info = get_company_from_email(person_email)

        company_slug = company_info[0] if company_info else None
        company_name = company_info[1] if company_info else None
        company_status = company_info[2] if company_info else "prospect"

        if company_slug:
            companies_slugs.add(company_slug)
            companies_links.add(f'"[[entities/{company_slug}]]"')
            ensure_entity(company_slug, company_name, "company", status=company_status)

        ensure_entity(slug, name, "person", email=person_email,
                      company_slug=company_slug, company_name=company_name)

    # Also create entities for email-only participants
    for email in participant_emails:
        company_info = get_company_from_email(email)
        if company_info:
            companies_slugs.add(company_info[0])
            companies_links.add(f'"[[entities/{company_info[0]}]]"')
            ensure_entity(company_info[0], company_info[1], "company", status=company_info[2])

    classification = classify_call(participant_emails, t.get("organizer_email"), speaker_names)
    call_id = str(uuid.uuid4())

    # Build tags
    tags = [f"date/{date_str}", "call"]
    if classification == "client":
        for cs in sorted(companies_slugs):
            tags.append(f"client/{cs}")
    for ps in people_slugs:
        tags.append(f"person/{ps}")
    for cs in sorted(companies_slugs):
        tags.append(f"company/{cs}")

    # Add topic tags from summary keywords
    summary = t.get("summary") or {}
    keywords = summary.get("keywords") or []
    if keywords:
        for kw in keywords[:5]:
            if isinstance(kw, str):
                tags.append(f"topic/{slugify(kw)}")

    tags.append(f"source/fireflies")

    tags_str = "\n".join(f"    - {tag}" for tag in tags)
    people_str = ", ".join(people_links) if people_links else "[]"
    companies_str = ", ".join(sorted(companies_links)) if companies_links else "[]"

    # Summary sections
    overview = summary.get("overview") or summary.get("short_summary") or ""
    action_items_text = summary.get("action_items") or ""
    outline = summary.get("outline") or ""
    shorthand = summary.get("shorthand_bullet") or ""

    # Transcript
    sentences = t.get("sentences") or []
    transcript_text = format_transcript_text(sentences)

    # Audio/video links
    media_links = ""
    if t.get("audio_url"):
        media_links += f"**Audio:** [{t['audio_url']}]({t['audio_url']})\n"
    if t.get("video_url"):
        media_links += f"**Video:** [{t['video_url']}]({t['video_url']})\n"
    if t.get("transcript_url"):
        media_links += f"**Fireflies:** [{t['transcript_url']}]({t['transcript_url']})\n"

    attendees_str = ", ".join(speaker_names) if speaker_names else "Unknown"
    duration_str = format_duration(t.get("duration") or 0)

    # Build notes section
    notes_parts = []
    if overview:
        notes_parts.append(f"### Overview\n{overview}")
    if shorthand:
        notes_parts.append(f"### Key Points\n{shorthand}")
    if outline:
        notes_parts.append(f"### Outline\n{outline}")

    notes_section = "\n\n".join(notes_parts) if notes_parts else "*No summary available from Fireflies.*"

    # Action items section
    ai_analysis = ""
    if action_items_text:
        ai_analysis = f"""
## AI Analysis

### Action Items
{action_items_text}
"""

    content = f"""---
schema_version: "1.0.0"
date: {date_str}
type: call
call_id: {call_id}
source: fireflies
classification_type: {classification}
people: [{people_str}]
companies: [{companies_str}]
tags:
{tags_str}
---

# {t['title']}

**Date:** {date_str}
**Duration:** {duration_str}
**Attendees:** {attendees_str}
{media_links}
---

## Notes

{notes_section}
{ai_analysis}
---

## Transcript

<details>
<summary>Full transcript ({len(sentences)} segments)</summary>

{transcript_text}

</details>

---
*Imported from Fireflies.ai*
"""

    filepath.write_text(content)
    print(f"  Created call: {filename}")


def main():
    print("Fetching transcript list...")
    transcripts = fetch_all_transcripts()
    print(f"Found {len(transcripts)} transcripts")

    transcripts = deduplicate(transcripts)
    print(f"After deduplication: {len(transcripts)}")

    # Sort by date descending
    transcripts.sort(key=lambda t: t["date"], reverse=True)

    print("\nFetching full details and creating files...\n")
    for i, t in enumerate(transcripts):
        title = t["title"]
        date_str = ms_to_date(t["date"])
        print(f"[{i+1}/{len(transcripts)}] {date_str} - {title}")

        # Fetch full detail
        try:
            detail = fetch_transcript_detail(t["id"])
            if detail:
                create_call_file(detail)
            else:
                print(f"  WARNING: No detail returned for {t['id']}")
        except Exception as e:
            print(f"  ERROR: {e}")

        # Small delay to be nice to the API
        time.sleep(0.3)

    print("\nDone!")

    # Count results
    call_files = list(CALLS_DIR.glob("*.md"))
    entity_files = list(ENTITIES_DIR.glob("*.md"))
    print(f"Created {len(call_files)} call files and {len(entity_files)} entity files")


if __name__ == "__main__":
    main()
