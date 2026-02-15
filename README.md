# trilliumnext-paste

An [Alfred](https://www.alfredapp.com/) workflow to capture snippets or ideas quickly to [TrilliumNext](https://github.com/TriliumNext/Notes).

## Prerequisites

- Alfred 5 with the Powerpack
- A running TrilliumNext instance with ETAPI enabled
- An ETAPI token (generate one in TrilliumNext under Options > ETAPI)

## Installation

1. Clone or download this repo.
2. Double-click the `info.plist` or symlink this directory into your Alfred workflows folder:
   ```
   ln -s "$(pwd)" ~/Library/Application\ Support/Alfred/Alfred.alfredpreferences/workflows/trilliumnext-paste
   ```
3. Open the workflow in Alfred and configure the workflow variables:
   - **TrilliumNext URL** — your server URL (e.g. `http://localhost:37840`)
   - **ETAPI Token** — your authentication token
   - **Parent Note ID** — the note under which snippets are created (defaults to `root`)

## Usage

There are three ways to send content to TrilliumNext:

### Keyword — type a snippet

Invoke Alfred and type:

```
tn <your snippet text>
```

### Clipboard — paste what you've copied

Invoke Alfred and type:

```
tnc
```

This grabs the current clipboard contents and sends them as a new note.

### Universal Action — send selected text

1. Select text in any application.
2. Invoke Alfred's Universal Actions (default: select text then press your Universal Action hotkey).
3. Choose **Send to TrilliumNext** from the action list.

All three methods create a new text note in TrilliumNext and show a notification confirming success or reporting any error.

## Development

```
trilliumnext-paste/
├── info.plist              # Alfred workflow definition
├── scripts/
│   ├── paste.sh            # Core script — posts content to TrilliumNext ETAPI
│   └── paste-clipboard.sh  # Reads clipboard via pbpaste, delegates to paste.sh
├── LICENSE
└── README.md
```

To test the script outside Alfred, export the required variables and run directly:

```bash
export TRILLIUMNEXT_URL="http://localhost:37840"
export TRILLIUMNEXT_TOKEN="your-etapi-token"

# Type input directly
./scripts/paste.sh "Test snippet"

# Pipe input
echo "Piped content" | ./scripts/paste.sh

# Clipboard (macOS only)
./scripts/paste-clipboard.sh
```

## License

MIT
