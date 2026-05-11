#!/usr/bin/env python3
"""Create people records in Attio from SalesFlare contacts."""

import json
import os
import re
import asyncio
import aiohttp
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_REPO_ROOT = _SCRIPT_DIR.parent
BASE_DIR = Path(
    os.environ.get(
        "ATTIO_CREATE_PEOPLE_BASE_DIR",
        str(_REPO_ROOT / "brain" / "library" / "internal" / "salesflare"),
    )
)
API_KEY = "5e22aa80b4507b4b38d9b4211cf0c24978657f99c8bc345923f0a34959531ad0"
API_URL = "https://api.attio.com/v2/objects/people/records"
BATCH_SIZE = 10
DELAY_BETWEEN_BATCHES = 4.5  # ~133/min, under 150 limit

def normalize_phone(phone_str):
    """Normalize phone to E.164 format. Assumes US if no country code."""
    if not phone_str:
        return None
    # Strip all non-digit chars except leading +
    digits = re.sub(r'[^\d+]', '', phone_str)
    if digits.startswith('+'):
        return digits  # Already has country code
    # Remove leading 1 if 11 digits (US format with country code)
    if len(digits) == 11 and digits.startswith('1'):
        return '+' + digits
    if len(digits) == 10:
        return '+1' + digits
    # For other lengths, try with + prefix
    if len(digits) > 10:
        return '+' + digits
    # Too short, skip
    return None

def parse_name(contact):
    """Parse contact into first_name, last_name, full_name. Always returns all three."""
    firstname = (contact.get("firstname") or "").strip()
    lastname = (contact.get("lastname") or "").strip()
    full_name = (contact.get("name") or "").strip()

    if firstname or lastname:
        if not full_name:
            full_name = f"{firstname} {lastname}".strip()
        return firstname or "", lastname or "", full_name

    # No firstname/lastname - parse from name
    if full_name:
        parts = full_name.split()
        if len(parts) >= 2:
            return parts[0], " ".join(parts[1:]), full_name
        else:
            # Single word - use as first_name, empty last_name
            return full_name, "", full_name

    return None, None, None

def build_payload(contact):
    """Build Attio API payload from a SalesFlare contact record."""
    firstname, lastname, full_name = parse_name(contact)

    if not full_name:
        return None

    values = {
        "name": [{
            "full_name": full_name,
            "first_name": firstname,
            "last_name": lastname,
        }]
    }

    # Email
    email = contact.get("email")
    if email:
        values["email_addresses"] = [email]

    # Phone - normalize to E.164
    phone = contact.get("phone_number") or contact.get("mobile_phone_number")
    if phone:
        normalized = normalize_phone(phone)
        if normalized:
            values["phone_numbers"] = [normalized]

    # Job title from positions
    positions = contact.get("positions") or []
    if positions and positions[0].get("title"):
        values["job_title"] = [positions[0]["title"]]

    return {"data": {"values": values}}

async def create_person(session, sf_id, contact, semaphore):
    """Create a single person record in Attio."""
    payload = build_payload(contact)
    if not payload:
        return {"salesflare_id": sf_id, "status": "skipped", "reason": "no name"}

    async with semaphore:
        try:
            async with session.post(API_URL, json=payload) as resp:
                body = await resp.json()
                if resp.status in (200, 201):
                    record_id = body["data"]["id"]["record_id"]
                    name = contact.get("name") or f'{contact.get("firstname","")} {contact.get("lastname","")}'.strip()
                    email = contact.get("email")
                    return {
                        "salesflare_id": sf_id,
                        "attio_record_id": record_id,
                        "name": name,
                        "email": email,
                        "status": "created"
                    }
                else:
                    return {
                        "salesflare_id": sf_id,
                        "status": "failed",
                        "error": body.get("message", str(body)),
                        "http_status": resp.status,
                        "payload": payload
                    }
        except Exception as e:
            return {
                "salesflare_id": sf_id,
                "status": "failed",
                "error": str(e)
            }

async def process_batch(session, batch, semaphore):
    tasks = [create_person(session, sf_id, contact, semaphore) for sf_id, contact in batch]
    return await asyncio.gather(*tasks)

def load_data():
    with open(BASE_DIR / "contact_crossref.json") as f:
        crossref = json.load(f)
    with open(BASE_DIR / "contacts.json") as f:
        contacts_list = json.load(f)
    contacts_by_id = {c["id"]: c for c in contacts_list}
    return crossref, contacts_by_id

def load_already_created():
    """Load already-created records to skip them."""
    path = BASE_DIR / "people_created.json"
    if path.exists():
        with open(path) as f:
            existing = json.load(f)
        return {r["salesflare_id"] for r in existing}, existing
    return set(), []

async def main():
    crossref, contacts_by_id = load_data()
    already_created_ids, already_created = load_already_created()

    print(f"Already created from previous run: {len(already_created_ids)}")

    new_contacts = crossref["new"]
    no_email = crossref["no_email"]

    # Build work items, skipping already created
    work_items = []
    for item in new_contacts + no_email:
        sf_id = item["salesflare_id"]
        if sf_id in already_created_ids:
            continue
        contact = contacts_by_id.get(sf_id)
        if contact:
            work_items.append((sf_id, contact))
        else:
            # Fallback for no_email entries not in contacts.json
            fallback = {
                "name": item.get("name", ""),
                "firstname": None,
                "lastname": None,
                "email": None,
                "phone_number": item.get("phone_number"),
                "mobile_phone_number": None,
                "positions": []
            }
            work_items.append((sf_id, fallback))

    print(f"Remaining to create: {len(work_items)}")

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    semaphore = asyncio.Semaphore(BATCH_SIZE)
    results = []

    async with aiohttp.ClientSession(headers=headers) as session:
        for i in range(0, len(work_items), BATCH_SIZE):
            batch = work_items[i:i + BATCH_SIZE]
            batch_num = i // BATCH_SIZE + 1
            total_batches = (len(work_items) + BATCH_SIZE - 1) // BATCH_SIZE

            batch_results = await process_batch(session, batch, semaphore)
            results.extend(batch_results)

            created = sum(1 for r in batch_results if r["status"] == "created")
            failed = sum(1 for r in batch_results if r["status"] == "failed")
            print(f"Batch {batch_num}/{total_batches}: {created} created, {failed} failed", flush=True)

            if i + BATCH_SIZE < len(work_items):
                await asyncio.sleep(DELAY_BETWEEN_BATCHES)

    # Summary
    new_created = [r for r in results if r["status"] == "created"]
    new_failed = [r for r in results if r["status"] == "failed"]
    new_skipped = [r for r in results if r["status"] == "skipped"]

    print(f"\n=== THIS RUN ===")
    print(f"Created: {len(new_created)}")
    print(f"Failed:  {len(new_failed)}")
    print(f"Skipped: {len(new_skipped)}")

    if new_failed:
        print(f"\nFailed records (first 10):")
        for r in new_failed[:10]:
            print(f"  SF ID {r['salesflare_id']}: {r.get('error', 'unknown')}")
            if r.get('payload'):
                print(f"    Payload: {json.dumps(r['payload']['data']['values']['name'])}")

    # Merge with existing
    all_created = already_created + [
        {
            "salesflare_id": r["salesflare_id"],
            "attio_record_id": r["attio_record_id"],
            "name": r["name"],
            "email": r.get("email")
        }
        for r in new_created
    ]

    output_path = BASE_DIR / "people_created.json"
    with open(output_path, "w") as f:
        json.dump(all_created, f, indent=2)

    print(f"\n=== TOTAL ===")
    print(f"Total created (all runs): {len(all_created)}")
    print(f"Mapping saved to {output_path}")

    # Save failed for inspection
    if new_failed:
        failed_path = BASE_DIR / "people_failed.json"
        with open(failed_path, "w") as f:
            json.dump([{
                "salesflare_id": r["salesflare_id"],
                "error": r.get("error"),
                "payload": r.get("payload")
            } for r in new_failed], f, indent=2)
        print(f"Failed records saved to {failed_path}")

if __name__ == "__main__":
    asyncio.run(main())
