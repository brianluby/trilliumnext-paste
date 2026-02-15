# Installation Guide

## Prerequisites

Before installing the TrilliumNext Paste workflow, ensure you have:

1. **macOS** with Alfred Powerpack installed
2. **TrilliumNext Notes** running (locally or remotely)
3. **Python 3** (pre-installed on macOS)

## Step 1: Get an ETAPI Token

1. Open your TrilliumNext instance
2. Click the gear icon (⚙️) to open Options
3. Navigate to **ETAPI** section
4. Click **Create new token** or use an existing token
5. Copy the token - you'll need it in Step 3

## Step 2: Install the Workflow

### Option A: Download Pre-packaged Workflow (Recommended)

1. Download `TrilliumNext-Paste.alfredworkflow` from the [latest release](https://github.com/brianluby/trilliumnext-paste/releases)
2. Double-click the downloaded file
3. Alfred will prompt you to import the workflow - click **Import**

### Option B: Install from Source

1. Clone or download this repository
2. Navigate to the `TrilliumNext Paste.alfredworkflow` directory
3. Create a zip file:
   ```bash
   cd "TrilliumNext Paste.alfredworkflow"
   zip -r "../TrilliumNext-Paste.alfredworkflow" *
   ```
4. Double-click the `TrilliumNext-Paste.alfredworkflow` file
5. Alfred will prompt you to import - click **Import**

## Step 3: Configure the Workflow

After importing, you need to configure the workflow:

1. Open Alfred Preferences (`⌘,`)
2. Go to the **Workflows** tab
3. Find and select **TrilliumNext Paste** in the list
4. Click the `[x]` button (Configure Workflow) in the top-right corner
5. Fill in the configuration:

   - **TrilliumNext URL**: Enter your TrilliumNext instance URL
     - For local: `http://localhost:8080`
     - For remote: `https://your-trilliumnext-domain.com`
   
   - **ETAPI Token**: Paste the token you got in Step 1
   
   - **Parent Note ID** (optional): 
     - Leave as `root` to create notes at the root level
     - Or specify a note ID to organize captured notes under a specific parent

### Finding a Parent Note ID

If you want notes saved to a specific location:

1. Open TrilliumNext
2. Navigate to the note you want to use as parent
3. Right-click on the note title
4. Select **Note Info**
5. Copy the **Note ID** from the info panel
6. Paste it into the workflow configuration

## Step 4: Test the Workflow

1. Open Alfred (`⌘Space` or your custom hotkey)
2. Type: `tn This is my first note`
3. Press **Enter**
4. You should see a notification confirming the note was created
5. Check TrilliumNext - your note should appear!

## Troubleshooting

### Problem: "Configuration Required" message

**Solution**: Make sure you've completed Step 3 and entered both the URL and ETAPI token.

### Problem: "Connection Error"

**Solutions**:
- Verify TrilliumNext is running
- Check the URL is correct and accessible
- For remote instances, ensure the URL includes the protocol (`https://`)
- Try accessing the URL in your browser to confirm it's reachable

### Problem: "HTTP Error 401" or "Unauthorized"

**Solutions**:
- Your ETAPI token may be invalid or expired
- Generate a new token in TrilliumNext (Options → ETAPI)
- Update the workflow configuration with the new token

### Problem: Notes appear but in wrong location

**Solution**: Check the Parent Note ID in your workflow configuration. Make sure:
- The note ID exists in your TrilliumNext instance
- You have permission to create notes under that parent
- Use `root` if you want notes at the top level

### Problem: Python not found

**Solution**: macOS includes Python 3 by default. If you get a Python error:
```bash
# Check Python version
python3 --version

# If not installed, install via Homebrew
brew install python3
```

## Updating the Workflow

To update to a new version:

1. Download the latest `TrilliumNext-Paste.alfredworkflow`
2. Double-click to import
3. Alfred will ask if you want to replace the existing workflow
4. Click **Replace** - your configuration will be preserved

## Uninstalling

1. Open Alfred Preferences (`⌘,`)
2. Go to **Workflows** tab
3. Select **TrilliumNext Paste**
4. Right-click and select **Delete**
5. Confirm the deletion

## Advanced Configuration

### Customizing the Keyword

If you don't like the default `tn` keyword:

1. Open Alfred Preferences → Workflows
2. Select **TrilliumNext Paste**
3. Double-click the **Script Filter** node
4. Change the **Keyword** field to your preference
5. Click **Save**

### Using Environment Variables (Alternative Configuration)

Instead of workflow configuration, you can also use environment variables:

```bash
# Add to your ~/.zshrc or ~/.bash_profile
export trilliumnext_url="http://localhost:8080"
export trilliumnext_token="your_etapi_token"
export trilliumnext_parent_note_id="root"
```

## Getting Help

If you encounter issues not covered here:

1. Check the [README](README.md) for general information
2. Open an issue on [GitHub](https://github.com/brianluby/trilliumnext-paste/issues)
3. Include:
   - Your macOS version
   - Alfred version
   - TrilliumNext version
   - Any error messages you see
