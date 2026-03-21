#!/usr/bin/env python3
"""
Format a Google Doc with G&B brand standards.

Usage:
    python3 format-gdoc.py <doc_id> [--all] [--logo] [--footer] [--font]

Brand standards:
    - Font: Avenir (with Nunito Sans fallback if not available)
    - Text color: Black (#000000)
    - Header: G&B logo centered at top
    - Footer: "Strictly Confidential" centered on every page
"""

import argparse
import json
import os
import subprocess
import sys
import tempfile

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# --- Config ---
GOG_ACCOUNT = "kay.s@greenwichandbarrow.com"
GOG_CREDS_PATH = os.path.expanduser(
    "~/Library/Application Support/gogcli/credentials.json"
)
LOGO_DRIVE_ID = "1YNyoG3uWRhDX2z7-wlhm941rb9VO_jc6"  # G&B FULL LOGO ON WHT.png (monogram + GREENWICH & BARROW)
# Try Avenir first — may render if user has it installed. Nunito Sans is the Google Fonts fallback.
BRAND_FONT = "Avenir"
BRAND_COLOR = {"red": 0.0, "green": 0.0, "blue": 0.0}  # #000000
TOKEN_URI = "https://oauth2.googleapis.com/token"
SCOPES = [
    "https://www.googleapis.com/auth/documents",
    "https://www.googleapis.com/auth/drive",
]


def get_credentials():
    """Get Google API credentials using gog's stored OAuth tokens."""
    # Read client credentials
    with open(GOG_CREDS_PATH) as f:
        client_creds = json.load(f)

    # Export refresh token from gog keyring
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [
                "gog", "auth", "tokens", "export", GOG_ACCOUNT,
                "--out", tmp_path, "--overwrite",
            ],
            capture_output=True, text=True, check=True,
        )
        with open(tmp_path) as f:
            token_data = json.load(f)
    finally:
        os.unlink(tmp_path)

    refresh_token = token_data["refresh_token"]

    creds = Credentials(
        token=None,
        refresh_token=refresh_token,
        token_uri=TOKEN_URI,
        client_id=client_creds["client_id"],
        client_secret=client_creds["client_secret"],
        scopes=SCOPES,
    )

    # Force token refresh
    from google.auth.transport.requests import Request
    creds.refresh(Request())

    return creds


def get_document(docs_service, doc_id):
    """Fetch the full document."""
    return docs_service.documents().get(documentId=doc_id).execute()


def get_body_end_index(doc):
    """Get the end index of the document body."""
    body = doc.get("body", {})
    content = body.get("content", [])
    if content:
        return content[-1].get("endIndex", 1)
    return 1


def apply_font(docs_service, doc_id, doc):
    """Set all body text to brand font and black color."""
    end_index = get_body_end_index(doc)
    if end_index <= 1:
        print("  Document body is empty, skipping font formatting.")
        return

    requests = [
        {
            "updateTextStyle": {
                "range": {"startIndex": 1, "endIndex": end_index},
                "textStyle": {
                    "weightedFontFamily": {
                        "fontFamily": BRAND_FONT,
                    },
                    "foregroundColor": {
                        "color": {"rgbColor": BRAND_COLOR}
                    },
                },
                "fields": "weightedFontFamily,foregroundColor",
            }
        }
    ]

    docs_service.documents().batchUpdate(
        documentId=doc_id, body={"requests": requests}
    ).execute()
    print(f"  Font set to {BRAND_FONT}, color set to black.")


def apply_footer(docs_service, doc_id, doc):
    """Add 'Strictly Confidential' centered footer."""
    # Check if a footer already exists
    headers_footers = doc.get("footers", {})
    footer_id = None

    if headers_footers:
        # Footer already exists
        footer_id = list(headers_footers.keys())[0]
        # Check if it already has our text
        footer = headers_footers[footer_id]
        footer_content = footer.get("content", [])
        for element in footer_content:
            paragraph = element.get("paragraph", {})
            for pe in paragraph.get("elements", []):
                text_run = pe.get("textRun", {})
                if "Strictly Confidential" in text_run.get("content", ""):
                    # Text exists but may have wrong formatting (blue font from prior run)
                    # Re-apply formatting to ensure black text, correct font
                    start_idx = pe.get("startIndex", 0)
                    end_idx = pe.get("endIndex", start_idx + len("Strictly Confidential"))
                    requests = [{
                        "updateTextStyle": {
                            "range": {
                                "segmentId": footer_id,
                                "startIndex": start_idx,
                                "endIndex": end_idx,
                            },
                            "textStyle": {
                                "weightedFontFamily": {"fontFamily": BRAND_FONT},
                                "fontSize": {"magnitude": 8, "unit": "PT"},
                                "italic": True,
                                "foregroundColor": {"color": {"rgbColor": BRAND_COLOR}},
                            },
                            "fields": "weightedFontFamily,fontSize,italic,foregroundColor",
                        }
                    }]
                    docs_service.documents().batchUpdate(
                        documentId=doc_id, body={"requests": requests}
                    ).execute()
                    print("  Footer exists — re-applied black formatting.")
                    return

    requests = []

    if not footer_id:
        # Create a default footer
        requests.append({
            "createFooter": {
                "type": "DEFAULT",
                "sectionBreakLocation": {"index": 0},
            }
        })
        # Execute to create footer first, then re-fetch doc
        docs_service.documents().batchUpdate(
            documentId=doc_id, body={"requests": requests}
        ).execute()
        # Re-fetch to get footer ID
        doc = get_document(docs_service, doc_id)
        headers_footers = doc.get("footers", {})
        footer_id = list(headers_footers.keys())[0]
        requests = []

    # Find the insertion point in the footer
    footer = doc["footers"][footer_id]
    footer_content = footer.get("content", [])
    # Insert at the start of the first paragraph in the footer
    if footer_content:
        insert_index = footer_content[0].get("startIndex", 0)
    else:
        insert_index = 0

    footer_text = "Strictly Confidential"

    # Insert the text
    requests.append({
        "insertText": {
            "location": {"segmentId": footer_id, "index": insert_index},
            "text": footer_text,
        }
    })

    # Format the text: centered, brand font, black, italic
    requests.append({
        "updateParagraphStyle": {
            "range": {
                "segmentId": footer_id,
                "startIndex": insert_index,
                "endIndex": insert_index + len(footer_text),
            },
            "paragraphStyle": {"alignment": "CENTER"},
            "fields": "alignment",
        }
    })
    requests.append({
        "updateTextStyle": {
            "range": {
                "segmentId": footer_id,
                "startIndex": insert_index,
                "endIndex": insert_index + len(footer_text),
            },
            "textStyle": {
                "weightedFontFamily": {
                    "fontFamily": BRAND_FONT,
                },
                "fontSize": {"magnitude": 8, "unit": "PT"},
                "italic": True,
                "foregroundColor": {
                    "color": {"rgbColor": BRAND_COLOR}
                },
            },
            "fields": "weightedFontFamily,fontSize,italic,foregroundColor",
        }
    })

    docs_service.documents().batchUpdate(
        documentId=doc_id, body={"requests": requests}
    ).execute()
    print("  Footer added: 'Strictly Confidential' (centered, italic).")


def apply_logo(docs_service, drive_service, doc_id, doc):
    """Insert G&B logo centered at the top of the document."""
    # Get file metadata
    try:
        file_meta = drive_service.files().get(
            fileId=LOGO_DRIVE_ID, fields="mimeType,name,webContentLink"
        ).execute()
        mime = file_meta.get("mimeType", "")
        name = file_meta.get("name", "logo")
        print(f"  Logo file: {name} ({mime})")
    except Exception as e:
        print(f"  WARNING: Could not access logo file: {e}")
        print("  Skipping logo insertion.")
        return

    # Temporarily share the file publicly so Docs API can fetch it
    shared_perm_id = None
    try:
        perm = drive_service.permissions().create(
            fileId=LOGO_DRIVE_ID,
            body={"role": "reader", "type": "anyone"},
        ).execute()
        shared_perm_id = perm.get("id")
    except Exception as e:
        print(f"  WARNING: Could not share logo (may already be shared): {e}")

    # Use the direct content link format that Google Docs API accepts
    logo_url = f"https://lh3.googleusercontent.com/d/{LOGO_DRIVE_ID}"

    # Insert a newline first, then the image before it
    requests = [
        {
            "insertText": {
                "location": {"index": 1},
                "text": "\n",
            }
        },
        {
            "insertInlineImage": {
                "location": {"index": 1},
                "uri": logo_url,
                "objectSize": {
                    "height": {"magnitude": 50, "unit": "PT"},
                    "width": {"magnitude": 150, "unit": "PT"},
                },
            }
        },
    ]

    try:
        docs_service.documents().batchUpdate(
            documentId=doc_id, body={"requests": requests}
        ).execute()
    except Exception as e:
        print(f"  WARNING: Logo insertion via lh3 URL failed, trying alternate URL...")
        # Fallback: try the uc?export=download URL
        requests[1]["insertInlineImage"]["uri"] = (
            f"https://drive.google.com/uc?export=download&id={LOGO_DRIVE_ID}"
        )
        try:
            docs_service.documents().batchUpdate(
                documentId=doc_id, body={"requests": requests}
            ).execute()
        except Exception as e2:
            print(f"  FAILED: Could not insert logo: {e2}")
            _revoke_logo_sharing(drive_service, shared_perm_id)
            return

    # Center the logo paragraph
    doc = get_document(docs_service, doc_id)
    body_content = doc.get("body", {}).get("content", [])

    logo_para = None
    for element in body_content:
        if "paragraph" in element:
            for pe in element["paragraph"].get("elements", []):
                if "inlineObjectElement" in pe:
                    logo_para = element
                    break
            if logo_para:
                break

    if logo_para:
        start = logo_para["startIndex"]
        end = logo_para["endIndex"]
        docs_service.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": [{
                "updateParagraphStyle": {
                    "range": {"startIndex": start, "endIndex": end},
                    "paragraphStyle": {"alignment": "CENTER"},
                    "fields": "alignment",
                }
            }]},
        ).execute()
        print("  Logo inserted and centered at top of document.")
    else:
        print("  Logo inserted but could not locate paragraph for centering.")

    # Revoke temporary public access
    _revoke_logo_sharing(drive_service, shared_perm_id)


def _revoke_logo_sharing(drive_service, perm_id):
    """Remove the temporary public sharing permission from the logo."""
    if not perm_id:
        return
    try:
        drive_service.permissions().delete(
            fileId=LOGO_DRIVE_ID, permissionId=perm_id
        ).execute()
    except Exception:
        pass


def main():
    parser = argparse.ArgumentParser(
        description="Format a Google Doc with G&B brand standards."
    )
    parser.add_argument("doc_id", help="Google Doc ID to format")
    parser.add_argument("--all", action="store_true", default=False,
                        help="Apply all formatting (default if no flags given)")
    parser.add_argument("--logo", action="store_true",
                        help="Insert G&B logo at top")
    parser.add_argument("--footer", action="store_true",
                        help="Add 'Strictly Confidential' footer")
    parser.add_argument("--font", action="store_true",
                        help="Set brand font and black text color")
    args = parser.parse_args()

    # Default to --all if no specific flags
    if not (args.logo or args.footer or args.font):
        args.all = True

    do_font = args.all or args.font
    do_footer = args.all or args.footer
    do_logo = args.all or args.logo

    print(f"Authenticating with Google APIs...")
    try:
        creds = get_credentials()
    except Exception as e:
        print(f"FAILED: Could not authenticate: {e}", file=sys.stderr)
        sys.exit(1)

    docs_service = build("docs", "v1", credentials=creds)
    drive_service = build("drive", "v3", credentials=creds)

    print(f"Fetching document {args.doc_id}...")
    try:
        doc = get_document(docs_service, args.doc_id)
    except Exception as e:
        print(f"FAILED: Could not fetch document: {e}", file=sys.stderr)
        sys.exit(1)

    title = doc.get("title", "(untitled)")
    print(f"Document: {title}")

    if do_font:
        print("Applying font formatting...")
        apply_font(docs_service, args.doc_id, doc)
        # Re-fetch after font changes
        doc = get_document(docs_service, args.doc_id)

    if do_footer:
        print("Applying footer...")
        apply_footer(docs_service, args.doc_id, doc)
        doc = get_document(docs_service, args.doc_id)

    if do_logo:
        print("Inserting logo...")
        apply_logo(docs_service, drive_service, args.doc_id, doc)

    print(f"\nDone. View: https://docs.google.com/document/d/{args.doc_id}/edit")


if __name__ == "__main__":
    main()
