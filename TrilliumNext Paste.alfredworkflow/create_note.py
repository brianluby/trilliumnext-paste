#!/usr/bin/env python3
"""
Creates a note in TrilliumNext via ETAPI
"""
import json
import sys
import os
import urllib.request
import urllib.error
from datetime import datetime

def create_note(url, token, parent_note_id, title, content):
    """Create a note in TrilliumNext using ETAPI"""
    
    # Prepare the API endpoint
    api_url = f"{url.rstrip('/')}/etapi/create-note"
    
    # Prepare the note data
    note_data = {
        "parentNoteId": parent_note_id,
        "title": title,
        "type": "text",
        "content": content
    }
    
    # Prepare the request
    json_data = json.dumps(note_data).encode('utf-8')
    req = urllib.request.Request(
        api_url,
        data=json_data,
        headers={
            "Authorization": token,
            "Content-Type": "application/json"
        },
        method="POST"
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return True, result.get('note', {}).get('noteId', 'unknown')
    except urllib.error.HTTPError as e:
        error_msg = e.read().decode('utf-8')
        return False, f"HTTP Error {e.code}: {error_msg}"
    except urllib.error.URLError as e:
        return False, f"Connection Error: {e.reason}"
    except Exception as e:
        return False, f"Error: {str(e)}"

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Get configuration from environment variables
    url = os.environ.get("trilliumnext_url", "http://localhost:8080")
    token = os.environ.get("trilliumnext_token", "")
    parent_note_id = os.environ.get("trilliumnext_parent_note_id", "root")
    
    if not token:
        print("Error: ETAPI token not configured")
        sys.exit(1)
    
    if not query:
        print("Error: No content provided")
        sys.exit(1)
    
    # Extract title from first line, use rest as content
    lines = query.split('\n', 1)
    title = lines[0][:100]  # Limit title length
    content = query  # Keep full content including title
    
    # If no title was provided, generate one
    if not title.strip():
        title = f"Note {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    
    # Create the note
    success, result = create_note(url, token, parent_note_id, title, content)
    
    if success:
        print(f"Note created successfully (ID: {result})")
    else:
        print(f"Failed to create note: {result}")
        sys.exit(1)

if __name__ == "__main__":
    main()
