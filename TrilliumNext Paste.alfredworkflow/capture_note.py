#!/usr/bin/env python3
"""
Script filter for capturing notes to TrilliumNext
Returns JSON items for Alfred to display
"""
import json
import sys
import os
from constants import MAX_TITLE_LENGTH

def main():
    query = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # Check if configuration is available
    url = os.environ.get("trilliumnext_url", "")
    token = os.environ.get("trilliumnext_token", "")
    
    items = []
    
    if not url or not token:
        items.append({
            "title": "Configuration Required",
            "subtitle": "Please configure TrilliumNext URL and ETAPI token in workflow settings",
            "valid": False,
            "icon": {
                "path": "icon.png"
            }
        })
    elif not query:
        items.append({
            "title": "Type your note...",
            "subtitle": "Press Enter to save to TrilliumNext",
            "valid": False,
            "icon": {
                "path": "icon.png"
            }
        })
    else:
        # Extract title (first line) and content
        lines = query.split('\n', 1)
        title = lines[0][:MAX_TITLE_LENGTH]  # Limit title length
        
        items.append({
            "title": f"Save: {title}",
            "subtitle": f"Create note in TrilliumNext ({len(query)} characters)",
            "arg": query,
            "valid": True,
            "icon": {
                "path": "icon.png"
            }
        })
    
    output = {"items": items}
    print(json.dumps(output))

if __name__ == "__main__":
    main()
