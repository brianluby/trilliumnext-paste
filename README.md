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

Invoke Alfred and type:

```
tn <your snippet text>
```

A new text note will be created in TrilliumNext with the snippet content. A notification confirms success or reports any error.

## Development

```
trilliumnext-paste/
├── info.plist          # Alfred workflow definition
├── scripts/
│   └── paste.sh        # Main script — posts to TrilliumNext ETAPI
├── LICENSE
└── README.md
```

To test the script outside Alfred, export the required variables and run directly:

```bash
export TRILLIUMNEXT_URL="http://localhost:37840"
export TRILLIUMNEXT_TOKEN="your-etapi-token"
./scripts/paste.sh "Test snippet"
```

## License

MIT
