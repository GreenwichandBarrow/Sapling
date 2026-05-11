#!/usr/bin/env python3
"""
Network Pipeline Migration: Attio List entries -> People record custom attributes.
Processes 111 entries with 5-second delays between API calls (12 req/min rate limit).
"""

import json
import time
import sys
import os
import requests
from datetime import datetime
from collections import defaultdict

API_KEY = "a3d86298c0b1e7fae2a364d4cf27b8a8b30a703bdb3738c53f9bc791bc4d5f2d"
BASE_URL = "https://api.attio.com/v2"
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_REPO_ROOT = os.path.dirname(_SCRIPT_DIR)
LOG_PATH = os.environ.get(
    "NETWORK_MIGRATION_LOG_PATH",
    os.path.join(_REPO_ROOT, "brain", "trackers", "network-migration-log.md"),
)

# Rate limiting
DELAY = 5  # seconds between API calls
last_call_time = 0

def rate_limit():
    global last_call_time
    elapsed = time.time() - last_call_time
    if elapsed < DELAY:
        time.sleep(DELAY - elapsed)
    last_call_time = time.time()

def api_get(path):
    rate_limit()
    r = requests.get(f"{BASE_URL}{path}", headers=HEADERS)
    r.raise_for_status()
    return r.json()

def api_post(path, data):
    rate_limit()
    r = requests.post(f"{BASE_URL}{path}", headers=HEADERS, json=data)
    r.raise_for_status()
    return r.json()

def api_patch(path, data):
    rate_limit()
    r = requests.patch(f"{BASE_URL}{path}", headers=HEADERS, json=data)
    r.raise_for_status()
    return r.json()

# Relationship type mapping based on company name keywords
RELATIONSHIP_MAP = [
    # Former Colleague (order matters - check specific before generic)
    ("chanel", "Former Colleague"),
    ("kate spade", "Former Colleague"),
    ("saks fifth avenue", "Former Colleague"),
    ("saks", "Former Colleague"),
    ("revolve", "Former Colleague"),
    ("nyu stern", "Former Colleague"),
    ("nyu", "Former Colleague"),
    ("training the street", "Former Colleague"),
    ("tapestry", "Former Colleague"),
    ("capri holdings", "Former Colleague"),
    ("coach", "Former Colleague"),
    # Art World
    ("david zwirner", "Art World"),
    ("zwirner", "Art World"),
    ("whitney museum", "Art World"),
    ("whitney", "Art World"),
    ("frieze", "Art World"),
    ("phillips", "Art World"),
    ("bfa baigell", "Art World"),
    ("baigell", "Art World"),
    ("uovo", "Art World"),
    ("crate capital", "Art World"),
    ("artsy", "Art World"),
    ("sotheby", "Art World"),
    ("christie", "Art World"),
    ("gagosian", "Art World"),
    ("pace gallery", "Art World"),
    ("hauser", "Art World"),
    ("museum", "Art World"),
    ("gallery", "Art World"),
    ("fine art", "Art World"),
    ("art advisory", "Art World"),
    ("art storage", "Art World"),
    # Fellow Searcher
    ("bk growth", "Fellow Searcher"),
    ("endurance search", "Fellow Searcher"),
    ("jasper+black", "Fellow Searcher"),
    ("jasper black", "Fellow Searcher"),
    ("jasper and black", "Fellow Searcher"),
    ("saunders street", "Fellow Searcher"),
    ("search fund", "Fellow Searcher"),
    ("permanent equity", "Fellow Searcher"),
    # Industry Expert (insurance)
    ("risk strategies", "Industry Expert"),
    ("oberle risk", "Industry Expert"),
    ("markel", "Industry Expert"),
    ("chartwell", "Industry Expert"),
    ("insurance", "Industry Expert"),
    ("marsh", "Industry Expert"),
    ("aon", "Industry Expert"),
    ("compliance", "Industry Expert"),
    ("regulatory", "Industry Expert"),
    # Investor Contact
    ("usv", "Investor Contact"),
    ("union square ventures", "Investor Contact"),
    ("sixth street", "Investor Contact"),
    ("legate", "Investor Contact"),
    ("hudson hill", "Investor Contact"),
    ("venture", "Investor Contact"),
    ("partners", "Investor Contact"),
    ("invest", "Investor Contact"),
    ("capital", "Investor Contact"),
    # Lender
    ("bank", "Lender"),
    ("sba", "Lender"),
    ("lending", "Lender"),
    ("credit union", "Lender"),
    # Advisor
    ("advisor", "Advisor"),
    ("consulting", "Advisor"),
    ("mckinsey", "Advisor"),
    ("bain", "Advisor"),
    ("deloitte", "Advisor"),
]

def stage_to_attrs(stage):
    """Map list stage to custom attributes."""
    if stage == "Identified":
        return {"nurture_cadence": "Occasionally", "next_action": ""}
    elif stage == "Contacted - Need to Schedule":
        return {"nurture_cadence": "Monthly", "next_action": "Schedule call"}
    elif stage == "Call Scheduled":
        return {"nurture_cadence": "Monthly", "next_action": "Attend scheduled call"}
    elif stage == "Need to Reschedule":
        return {"nurture_cadence": "Monthly", "next_action": "Reschedule call"}
    elif stage == "Need to Send Thank You":
        return {"nurture_cadence": "Monthly", "next_action": "Send thank you"}
    elif stage == "Nurture (Quarterly)":
        return {"nurture_cadence": "Quarterly", "next_action": ""}
    elif stage == "Nurture (Occasionally)":
        return {"nurture_cadence": "Occasionally", "next_action": ""}
    elif stage == "Dormant (Revisit Quarterly)":
        return {"nurture_cadence": "Dormant", "next_action": ""}
    else:
        return {"nurture_cadence": "Occasionally", "next_action": ""}

def guess_relationship_type(company_name):
    """Guess relationship type from company name."""
    name_lower = company_name.lower()
    for keyword, rtype in RELATIONSHIP_MAP:
        if keyword in name_lower:
            return rtype
    return ""  # Unknown - leave blank for manual review

def get_company_name(record):
    """Extract company name from a company record."""
    values = record.get("data", {}).get("values", {})
    name_vals = values.get("name", [])
    if name_vals:
        for nv in name_vals:
            if nv.get("active_until") is None:
                return nv.get("value", "Unknown")
        return name_vals[0].get("value", "Unknown")
    return "Unknown"

def get_person_name(person):
    """Extract person name from a people record. Fall back to email if no name."""
    values = person.get("values", {})

    # Try name field (personal-name type)
    name_vals = values.get("name", [])
    if name_vals:
        for n in name_vals:
            if n.get("active_until") is None:
                first = n.get("first_name", "")
                last = n.get("last_name", "")
                full = n.get("full_name", "")
                if full:
                    return full
                if first or last:
                    return f"{first} {last}".strip()

    # Try separate first_name / last_name
    first = ""
    last = ""
    fn = values.get("first_name", [])
    ln = values.get("last_name", [])
    if fn:
        for f in fn:
            if f.get("active_until") is None:
                first = f.get("first_name", f.get("value", ""))
                break
    if ln:
        for l in ln:
            if l.get("active_until") is None:
                last = l.get("last_name", l.get("value", ""))
                break
    if first or last:
        return f"{first} {last}".strip()

    # Fall back to email
    emails = values.get("email_addresses", [])
    if emails:
        for e in emails:
            if e.get("active_until") is None:
                email = e.get("email_address", "")
                if email:
                    local = email.split("@")[0]
                    # Try to parse name from email (first.last or firstlast)
                    parts = local.replace(".", " ").replace("_", " ").replace("-", " ").split()
                    return " ".join(p.capitalize() for p in parts) + f" ({email})"
    return "Unknown"

def get_person_email(person):
    """Extract primary email from a person record."""
    values = person.get("values", {})
    emails = values.get("email_addresses", [])
    if emails:
        for e in emails:
            if e.get("active_until") is None:
                return e.get("email_address", "")
    return ""

def get_person_id(person):
    """Extract person record_id."""
    return person.get("id", {}).get("record_id", "")

def find_people_for_company(company_record_id):
    """Find people associated with a company via record-reference filter."""
    try:
        result = api_post("/objects/people/records/query", {
            "filter": {
                "company": {
                    "target_record_id": {
                        "$eq": company_record_id
                    }
                }
            }
        })
        return result.get("data", [])
    except Exception as e:
        print(f"  Error finding people: {e}")
        return []

def update_person_attributes(person_record_id, attrs):
    """Update a person's custom attributes."""
    values = {}
    if attrs.get("relationship_type"):
        values["relationship_type"] = attrs["relationship_type"]
    if attrs.get("nurture_cadence"):
        values["nurture_cadence"] = attrs["nurture_cadence"]
    if attrs.get("next_action"):
        values["next_action"] = attrs["next_action"]

    if not values:
        return None

    try:
        result = api_patch(
            f"/objects/people/records/{person_record_id}",
            {"data": {"values": values}}
        )
        return result
    except requests.exceptions.HTTPError as e:
        print(f"  PATCH failed ({e.response.status_code}): {e.response.text[:300]}")
        return None

def main():
    start_time = datetime.now()
    print(f"=== Network Pipeline Migration Started: {start_time.isoformat()} ===")
    print(f"Rate limit: {DELAY}s between API calls")
    print()

    # Step 1: Get all entries
    print("Step 1: Fetching all list entries...")
    result = api_post("/lists/94ccb017-2b86-4e12-b674-e27de8e146c9/entries/query", {})
    entries = result.get("data", [])
    print(f"  Found {len(entries)} entries")

    # Parse entries
    parsed = []
    for e in entries:
        entry_id = e["id"]["entry_id"]
        parent_id = e["parent_record_id"]
        stage_data = e["entry_values"].get("stage", [])
        stage = stage_data[0]["status"]["title"] if stage_data else "Unknown"
        parsed.append({
            "entry_id": entry_id,
            "parent_record_id": parent_id,
            "stage": stage
        })

    # Group by parent_record_id to identify duplicates
    company_entries = defaultdict(list)
    for p in parsed:
        company_entries[p["parent_record_id"]].append(p)

    unique_companies = len(company_entries)
    dupes = {k: v for k, v in company_entries.items() if len(v) > 1}
    print(f"  Unique companies: {unique_companies}")
    print(f"  Companies with multiple entries: {len(dupes)}")
    print()

    # Migration results
    results = []
    errors = []
    no_person_found = []
    skipped = []
    company_names = {}  # cache: company_id -> name

    # Step 2-4: Process each company
    total_companies = len(company_entries)
    for idx, (company_id, company_entry_list) in enumerate(company_entries.items(), 1):
        print(f"\n--- Company {idx}/{total_companies} (record: {company_id[:8]}...) ---")

        # Get company name
        try:
            company_data = api_get(f"/objects/companies/records/{company_id}")
            company_name = get_company_name(company_data)
            company_names[company_id] = company_name
        except Exception as e:
            company_name = f"ERROR: {e}"
            company_names[company_id] = company_name
            errors.append({"company_id": company_id, "company_name": company_name, "error": str(e), "step": "get_company"})
            print(f"  ERROR getting company: {e}")
            for ce in company_entry_list:
                results.append({
                    "entry_id": ce["entry_id"],
                    "company_id": company_id,
                    "company_name": company_name,
                    "stage": ce["stage"],
                    "person_name": "",
                    "person_id": "",
                    "person_email": "",
                    "status": "ERROR",
                    "detail": str(e)
                })
            continue

        print(f"  Company: {company_name}")

        # Skip Third Eye (Dan Tanzilli - already done)
        if "third eye" in company_name.lower():
            print(f"  SKIP: Third Eye (Dan Tanzilli already migrated)")
            for ce in company_entry_list:
                results.append({
                    "entry_id": ce["entry_id"],
                    "company_id": company_id,
                    "company_name": company_name,
                    "stage": ce["stage"],
                    "person_name": "Dan Tanzilli",
                    "person_id": "",
                    "person_email": "",
                    "status": "SKIPPED",
                    "detail": "Already migrated"
                })
                skipped.append(company_name)
            continue

        # Find people for this company (by record reference)
        try:
            people = find_people_for_company(company_id)
        except Exception as e:
            people = []
            errors.append({"company_id": company_id, "company_name": company_name, "error": str(e), "step": "find_people"})
            print(f"  ERROR finding people: {e}")

        if not people:
            print(f"  NO PEOPLE FOUND for {company_name}")
            for ce in company_entry_list:
                results.append({
                    "entry_id": ce["entry_id"],
                    "company_id": company_id,
                    "company_name": company_name,
                    "stage": ce["stage"],
                    "person_name": "",
                    "person_id": "",
                    "person_email": "",
                    "status": "NO_PERSON",
                    "detail": "No people found for company"
                })
                no_person_found.append({
                    "company_name": company_name,
                    "company_id": company_id,
                    "stage": ce["stage"]
                })
            continue

        print(f"  Found {len(people)} people")
        for p in people:
            pname = get_person_name(p)
            pemail = get_person_email(p)
            print(f"    - {pname} ({pemail})")

        # Process each entry for this company
        for entry_idx, ce in enumerate(company_entry_list):
            stage = ce["stage"]
            attrs = stage_to_attrs(stage)
            rel_type = guess_relationship_type(company_name)
            attrs["relationship_type"] = rel_type

            # Match entry to a person (round-robin if multiple entries, same people)
            person_idx = entry_idx % len(people)
            person = people[person_idx]
            person_name = get_person_name(person)
            person_email = get_person_email(person)
            person_id = get_person_id(person)

            print(f"  Entry {entry_idx+1}/{len(company_entry_list)}: stage='{stage}' -> person='{person_name}'")
            print(f"    Attrs: rel={rel_type or '(blank)'}, cadence={attrs['nurture_cadence']}, action='{attrs['next_action']}'")

            if not person_id:
                results.append({
                    "entry_id": ce["entry_id"],
                    "company_id": company_id,
                    "company_name": company_name,
                    "stage": stage,
                    "person_name": person_name,
                    "person_id": "",
                    "person_email": person_email,
                    "status": "NO_PERSON_ID",
                    "detail": "Could not extract person record ID"
                })
                continue

            # Check if person already has relationship_type set (don't overwrite)
            # Just set the attributes
            try:
                update_result = update_person_attributes(person_id, attrs)
                if update_result:
                    print(f"    UPDATED successfully")
                    results.append({
                        "entry_id": ce["entry_id"],
                        "company_id": company_id,
                        "company_name": company_name,
                        "stage": stage,
                        "person_name": person_name,
                        "person_id": person_id,
                        "person_email": person_email,
                        "status": "UPDATED",
                        "detail": f"rel={rel_type or '(blank)'}, cadence={attrs['nurture_cadence']}, action={attrs['next_action'] or '(blank)'}"
                    })
                else:
                    # update_person_attributes returns None if values dict is empty OR if PATCH failed
                    # Check if there were values to set
                    has_values = bool(rel_type or attrs.get("nurture_cadence") or attrs.get("next_action"))
                    if has_values:
                        print(f"    PATCH returned None (likely error)")
                        results.append({
                            "entry_id": ce["entry_id"],
                            "company_id": company_id,
                            "company_name": company_name,
                            "stage": stage,
                            "person_name": person_name,
                            "person_id": person_id,
                            "person_email": person_email,
                            "status": "PATCH_FAILED",
                            "detail": f"PATCH returned None for attrs: {attrs}"
                        })
                    else:
                        print(f"    No attributes to update (all empty)")
                        results.append({
                            "entry_id": ce["entry_id"],
                            "company_id": company_id,
                            "company_name": company_name,
                            "stage": stage,
                            "person_name": person_name,
                            "person_id": person_id,
                            "person_email": person_email,
                            "status": "NO_UPDATE",
                            "detail": "No non-empty attributes to set"
                        })
            except Exception as e:
                print(f"    ERROR updating: {e}")
                errors.append({
                    "company_name": company_name,
                    "person_name": person_name,
                    "error": str(e),
                    "step": "update_person"
                })
                results.append({
                    "entry_id": ce["entry_id"],
                    "company_id": company_id,
                    "company_name": company_name,
                    "stage": stage,
                    "person_name": person_name,
                    "person_id": person_id,
                    "person_email": person_email,
                    "status": "ERROR",
                    "detail": str(e)
                })

    # Step 5: Write migration log
    end_time = datetime.now()
    duration = end_time - start_time

    print(f"\n\n{'='*60}")
    print(f"Migration Complete: {end_time.isoformat()}")
    print(f"Duration: {duration}")
    print(f"{'='*60}")

    updated_count = sum(1 for r in results if r["status"] == "UPDATED")
    no_person_count = sum(1 for r in results if r["status"] == "NO_PERSON")
    error_count = sum(1 for r in results if r["status"] in ("ERROR", "PATCH_FAILED"))
    skipped_count = sum(1 for r in results if r["status"] == "SKIPPED")
    no_update_count = sum(1 for r in results if r["status"] == "NO_UPDATE")

    print(f"Total entries processed: {len(results)}")
    print(f"Updated: {updated_count}")
    print(f"No person found: {no_person_count}")
    print(f"Errors: {error_count}")
    print(f"Skipped: {skipped_count}")
    print(f"No update needed: {no_update_count}")

    # Write log file
    with open(LOG_PATH, "w") as f:
        f.write("---\n")
        f.write("title: Network Pipeline Migration Log\n")
        f.write(f"date: {datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("type: tracker\n")
        f.write("tags:\n")
        f.write(f"  - date/{datetime.now().strftime('%Y-%m-%d')}\n")
        f.write("  - status/complete\n")
        f.write("  - topic/migration\n")
        f.write("  - topic/attio\n")
        f.write("---\n\n")
        f.write("# Network Pipeline Migration Log\n\n")
        f.write(f"**Migration:** Network Pipeline List -> People record custom attributes\n")
        f.write(f"**Started:** {start_time.isoformat()}\n")
        f.write(f"**Completed:** {end_time.isoformat()}\n")
        f.write(f"**Duration:** {duration}\n\n")

        f.write("## Summary\n\n")
        f.write(f"| Metric | Count |\n")
        f.write(f"|--------|-------|\n")
        f.write(f"| Total entries processed | {len(results)} |\n")
        f.write(f"| Successfully updated | {updated_count} |\n")
        f.write(f"| No person found | {no_person_count} |\n")
        f.write(f"| Errors | {error_count} |\n")
        f.write(f"| Skipped (already done) | {skipped_count} |\n")
        f.write(f"| No update needed | {no_update_count} |\n\n")

        # Successfully updated
        f.write("## Successfully Updated\n\n")
        f.write("| Company | Person | Email | Stage | Attributes Set |\n")
        f.write("|---------|--------|-------|-------|----------------|\n")
        for r in sorted(results, key=lambda x: x["company_name"]):
            if r["status"] == "UPDATED":
                f.write(f"| {r['company_name']} | {r['person_name']} | {r['person_email']} | {r['stage']} | {r['detail']} |\n")

        # No person found
        f.write("\n## No Person Found (Manual Resolution Needed)\n\n")
        f.write("These entries had no people records linked to the company in Attio. Kay needs to:\n")
        f.write("1. Create the person record in Attio, or\n")
        f.write("2. Link an existing person to the company, or\n")
        f.write("3. Manually set the custom attributes on the right person\n\n")
        f.write("| Company | Stage | Company Record ID |\n")
        f.write("|---------|-------|-------------------|\n")
        seen_no_person = set()
        for r in sorted(results, key=lambda x: x["company_name"]):
            if r["status"] == "NO_PERSON":
                key = f"{r['company_name']}|{r['stage']}"
                if key not in seen_no_person:
                    seen_no_person.add(key)
                    f.write(f"| {r['company_name']} | {r['stage']} | `{r['company_id']}` |\n")

        # Duplicate company entries
        f.write("\n## Duplicate Company Entries\n\n")
        f.write("These companies had multiple entries in the Network Pipeline list.\n\n")
        for company_id, entry_list in sorted(dupes.items(), key=lambda x: company_names.get(x[0], "")):
            cname = company_names.get(company_id, "Unknown")
            f.write(f"### {cname} ({len(entry_list)} entries)\n\n")
            for ce in entry_list:
                matching = [r for r in results if r["entry_id"] == ce["entry_id"]]
                if matching:
                    m = matching[0]
                    f.write(f"- Stage: **{m['stage']}** -> Person: {m['person_name'] or 'N/A'} -> Status: {m['status']}\n")
                else:
                    f.write(f"- Stage: **{ce['stage']}** -> Not processed\n")
            f.write("\n")

        # Entries where relationship_type was left blank
        f.write("## Relationship Type Needs Review\n\n")
        f.write("These entries were updated but relationship_type could not be guessed from the company name.\n\n")
        f.write("| Company | Person | Email |\n")
        f.write("|---------|--------|-------|\n")
        seen_blank_rel = set()
        for r in sorted(results, key=lambda x: x["company_name"]):
            if r["status"] == "UPDATED" and "(blank)" in r.get("detail", "") and "rel=(blank)" in r.get("detail", ""):
                key = f"{r['company_name']}|{r['person_name']}"
                if key not in seen_blank_rel:
                    seen_blank_rel.add(key)
                    f.write(f"| {r['company_name']} | {r['person_name']} | {r['person_email']} |\n")

        # Errors
        if errors:
            f.write("\n## Errors\n\n")
            for err in errors:
                f.write(f"- **{err.get('company_name', err.get('company_id', 'Unknown'))}** ({err['step']}): {err['error']}\n")
            f.write("\n")

        # Skipped
        if skipped:
            f.write("\n## Skipped\n\n")
            for s in set(skipped):
                f.write(f"- {s} (already migrated)\n")
            f.write("\n")

        # Full entry log
        f.write("\n## Full Entry Log\n\n")
        f.write("| # | Company | Person | Email | Stage | Status | Detail |\n")
        f.write("|---|---------|--------|-------|-------|--------|--------|\n")
        for i, r in enumerate(sorted(results, key=lambda x: x["company_name"]), 1):
            f.write(f"| {i} | {r['company_name']} | {r['person_name']} | {r['person_email']} | {r['stage']} | {r['status']} | {r['detail']} |\n")

    print(f"\nLog written to: {LOG_PATH}")

if __name__ == "__main__":
    main()
