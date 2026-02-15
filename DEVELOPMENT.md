# Development Notes

## Project Overview

TrilliumNext Paste is an Alfred Workflow that enables quick note capture to TrilliumNext Notes via the ETAPI (External Trilium API).

## Architecture

### Workflow Components

1. **Script Filter** (`capture_note.py`)
   - Triggered by `tn` keyword in Alfred
   - Previews the note before creation
   - Validates configuration
   - Returns JSON for Alfred to display

2. **Run Script** (`create_note.py`)
   - Executes when user presses Enter
   - Makes HTTP POST to TrilliumNext ETAPI
   - Creates note with title and content
   - Shows success/error notification

3. **Configuration** (`info.plist`)
   - Defines workflow metadata
   - Connects script filter to action
   - Declares user configuration variables

### API Integration

The workflow uses TrilliumNext's ETAPI endpoint:

```
POST /etapi/create-note
Authorization: {ETAPI_TOKEN}
Content-Type: application/json

{
  "parentNoteId": "root",
  "title": "Note title",
  "type": "text",
  "content": "Note content"
}
```

### Design Decisions

1. **No External Dependencies**: Uses only Python standard library to avoid installation complexity
2. **Title Extraction**: First line becomes the title, full content saved as body
3. **Configurable Parent**: Users can organize notes under specific parent note
4. **Minimal Workflow**: Single input -> single action pattern for simplicity

## File Structure

```
TrilliumNext Paste.alfredworkflow/
├── info.plist           # Alfred workflow definition (XML)
├── capture_note.py      # Script filter (preview)
├── create_note.py       # Action script (create note)
├── constants.py         # Shared constants
├── icon.png            # Workflow icon (256x256)
└── README.md           # Workflow documentation
```

## Testing

### Manual Testing

```bash
# Test script filter
cd "TrilliumNext Paste.alfredworkflow"
trilliumnext_url="http://localhost:8080" \
trilliumnext_token="test_token" \
python3 capture_note.py "Test note"

# Test note creation (requires running TrilliumNext)
trilliumnext_url="http://localhost:8080" \
trilliumnext_token="your_real_token" \
python3 create_note.py "Test note content"
```

### Syntax Validation

```bash
python3 -m py_compile capture_note.py create_note.py constants.py
```

## Packaging

The workflow is packaged as a ZIP file with `.alfredworkflow` extension:

```bash
cd "TrilliumNext Paste.alfredworkflow"
zip -r "../TrilliumNext-Paste.alfredworkflow" *
```

Users double-click this file to import into Alfred.

## Release Process

1. Tag a release: `git tag v1.0.0`
2. Push tag: `git push origin v1.0.0`
3. GitHub Actions automatically:
   - Packages the workflow
   - Creates a GitHub release
   - Attaches the `.alfredworkflow` file

## Configuration Flow

1. User imports workflow
2. Alfred prompts for configuration
3. User provides:
   - TrilliumNext URL
   - ETAPI token
   - (Optional) Parent note ID
4. Values stored as environment variables
5. Scripts read `os.environ.get()`

## Error Handling

- **Missing Config**: Script filter shows "Configuration Required"
- **Connection Error**: Create script catches `urllib.error.URLError`
- **HTTP Error**: Create script catches `urllib.error.HTTPError`
- **Invalid Token**: Returns 401, shown to user

## Future Enhancements

Possible improvements:
- Support for note types (code, image, etc.)
- Tag/attribute assignment
- Parent note selection via Alfred
- Multi-line input support
- Clipboard content capture
- Selected text capture

## Contributing

When making changes:
1. Update Python scripts if modifying behavior
2. Update `info.plist` if changing workflow structure
3. Repackage the workflow
4. Update documentation
5. Test with real TrilliumNext instance
6. Run security checks (CodeQL)

## Dependencies

**Runtime:**
- macOS 10.15+
- Alfred 4+ with Powerpack
- Python 3 (system)
- TrilliumNext Notes

**Development:**
- Git
- Text editor
- Alfred for testing

## License

MIT License - see LICENSE file
