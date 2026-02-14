# TrilliumNext Paste

An Alfred Workflow for quickly capturing notes to [TrilliumNext](https://github.com/TriliumNext/Notes).

## Features

- Quick note capture with keyboard shortcut
- Configurable TrilliumNext instance URL
- Uses TrilliumNext ETAPI for reliable note creation
- Automatic title extraction from first line
- Supports custom parent note for organization

## Requirements

- macOS with [Alfred](https://www.alfredapp.com/) (Powerpack required for workflows)
- [TrilliumNext Notes](https://github.com/TriliumNext/Notes) instance running locally or remotely
- Python 3 (pre-installed on macOS)

## Installation

### Option 1: Import the Workflow

1. Download the `TrilliumNext Paste.alfredworkflow` file
2. Double-click the file to import it into Alfred
3. Configure the workflow (see Configuration section below)

### Option 2: Build from Source

1. Clone this repository
2. Package the workflow:
   ```bash
   cd "TrilliumNext Paste.alfredworkflow"
   zip -r "../TrilliumNext Paste.alfredworkflow" .
   ```
3. Double-click the resulting `.alfredworkflow` file to import it into Alfred

## Configuration

After importing the workflow, you need to configure it with your TrilliumNext instance details:

1. Open Alfred Preferences (⌘,)
2. Go to the Workflows tab
3. Select "TrilliumNext Paste"
4. Click the `[x]` button in the top right to open workflow configuration
5. Set the following variables:

   - **TrilliumNext URL**: The URL of your TrilliumNext instance (e.g., `http://localhost:8080`)
   - **ETAPI Token**: Your ETAPI authentication token (see below)
   - **Parent Note ID** (optional): The note ID where captured notes should be created (defaults to `root`)

### Getting Your ETAPI Token

1. Open TrilliumNext
2. Go to **Options** (gear icon) → **ETAPI**
3. Create a new ETAPI token or copy an existing one
4. Paste the token into the workflow configuration

## Usage

1. Activate Alfred (default: ⌘Space)
2. Type `tn` followed by your note content
3. Press Enter to create the note in TrilliumNext

### Examples

- `tn Quick reminder to check email`
- `tn Meeting notes: Discussed project timeline`
- `tn Ideas for weekend project`

### Tips

- The first line of your input becomes the note title
- The entire content (including the first line) is saved as the note body
- If you don't provide any text, the workflow will generate a timestamped title

## Workflow Structure

The workflow consists of:

- **Script Filter** (`capture_note.py`): Displays the preview of what will be saved
- **Run Script** (`create_note.py`): Creates the note in TrilliumNext via ETAPI
- **Notification**: Shows confirmation when the note is created

## Troubleshooting

### "Configuration Required" message

Make sure you've set the TrilliumNext URL and ETAPI token in the workflow configuration.

### "Connection Error" message

- Verify your TrilliumNext instance is running
- Check that the URL is correct and accessible
- Ensure your ETAPI token is valid

### Notes not appearing in the expected location

Check the Parent Note ID in the workflow configuration. You can find a note's ID by:
1. Opening the note in TrilliumNext
2. Right-clicking on the note title
3. Selecting "Note Info"
4. Copying the Note ID

## Development

The workflow is built with:
- Python 3 (standard library only, no external dependencies)
- TrilliumNext ETAPI (REST API)

### File Structure

```
TrilliumNext Paste.alfredworkflow/
├── info.plist           # Alfred workflow configuration
├── capture_note.py      # Script filter for displaying preview
├── create_note.py       # Script for creating notes in TrilliumNext
├── icon.png            # Workflow icon
└── README.md           # This file
```

## License

MIT License - see [LICENSE](../LICENSE) file for details

## Author

Brian Luby

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgments

- [TrilliumNext Notes](https://github.com/TriliumNext/Notes) - The hierarchical note-taking application
- [Alfred](https://www.alfredapp.com/) - The productivity app for macOS
