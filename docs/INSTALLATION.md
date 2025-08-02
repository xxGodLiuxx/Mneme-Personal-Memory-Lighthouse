# Mneme - Personal Memory Lighthouse Installation Guide

## System Requirements

- Windows 10/11
- Python 3.10 or higher
- Claude Desktop (installed)
- Notion account with database access
- Administrator privileges (for symbolic link creation)

---

## Installation Steps

### Step 1: Python Environment Setup

#### 1.1 Verify Python Installation
```cmd
python --version
```

If Python 3.10+ is not installed:
1. Download from [Python official site](https://www.python.org/)
2. Check "Add Python to PATH" during installation

#### 1.2 Install Required Packages
```cmd
pip install fastmcp
```

### Step 2: Program File Placement

#### 2.1 Create Directory Structure
```cmd
mkdir C:\Users\%USERNAME%\Documents\Mneme
```

#### 2.2 Place MCP Server Files

Copy the following files to the above directory:
- `hybrid_memory_mcp.py` (Main MCP server)
- Configuration files as needed

### Step 3: Claude Desktop Configuration

#### 3.1 Locate Configuration File
Navigate to Claude Desktop configuration:
```
%APPDATA%\Claude\claude_desktop_config.json
```

#### 3.2 Add MCP Server Configuration

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "mneme-memory": {
      "command": "python",
      "args": ["C:\\Users\\USERNAME\\Documents\\Mneme\\hybrid_memory_mcp.py"],
      "env": {}
    }
  }
}
```

**Important**: Replace `USERNAME` with your actual Windows username.

### Step 4: Notion Integration Setup

#### 4.1 Enable Claude-Notion Integration
1. Open Claude Desktop
2. Go to Settings → Integrations
3. Connect your Notion workspace
4. Grant necessary permissions

#### 4.2 Verify Database Access
Ensure Claude can access your Notion databases:
- Personal databases should be accessible
- Check sharing permissions if needed

### Step 5: Test Installation

#### 5.1 Restart Claude Desktop
1. Exit Claude Desktop completely (check system tray)
2. Restart the application
3. Start a new conversation

#### 5.2 Verification Commands

Test the following commands in Claude:

```
"Check available MCP tools"
```

Expected tools:
- `get_daily_inspiration_prompt`
- `save_from_notion`
- `get_random_memory`
- `search_by_context`
- `get_memory_stats`

```
"Execute get_memory_stats"
```

Should return memory system status.

## Multi-Device Setup (Optional)

### Dropbox Synchronization

#### Prerequisites
- Dropbox account and desktop client
- Administrator privileges on all devices

#### Setup Process

1. **Primary Device Setup**
   ```cmd
   # Run as Administrator
   installation\setup_dropbox_sync.bat
   ```

2. **Secondary Device Setup**
   - Wait for Dropbox sync to complete
   - Run the same script on each device
   - Configure Claude Desktop individually

#### Manual Sync Alternative

If automatic sync fails:

1. **Create Sync Folder**
   ```
   Dropbox\Mneme_Memory_Sync\
   ```

2. **Copy Memory Data**
   ```cmd
   xcopy C:\Users\%USERNAME%\.mneme_memory\* "%USERPROFILE%\Dropbox\Mneme_Memory_Sync\" /E /Y
   ```

3. **Set Up on Other Devices**
   - Install Mneme normally
   - Copy data from Dropbox folder

## Troubleshooting

### Common Issues

#### MCP Server Not Found
**Error**: "Command not found" or similar

**Solutions**:
1. Check Python path in configuration
2. Verify file paths are correct
3. Ensure no typos in `claude_desktop_config.json`

#### Python Path Issues
**Error**: Python executable not found

**Solutions**:
1. Use full Python path:
   ```json
   "command": "C:\\Python311\\python.exe"
   ```
2. Or use `python.exe` if in PATH

#### Permission Errors
**Error**: Access denied or file not found

**Solutions**:
1. Run as Administrator
2. Check folder permissions
3. Verify antivirus is not blocking

#### Configuration File Errors
**Error**: Invalid JSON format

**Solutions**:
1. Validate JSON syntax online
2. Check for trailing commas
3. Ensure proper escaping of backslashes

### Advanced Configuration

#### Custom Installation Path

To use a different installation directory:

1. **Update Configuration**
   ```json
   {
     "mcpServers": {
       "mneme-memory": {
         "command": "python",
         "args": ["D:\\MyApps\\Mneme\\hybrid_memory_mcp.py"],
         "env": {
           "MNEME_DATA_PATH": "D:\\MyData\\MnemeMemories"
         }
       }
     }
   }
   ```

2. **Create Custom Directories**
   ```cmd
   mkdir D:\MyApps\Mneme
   mkdir D:\MyData\MnemeMemories
   ```

#### Environment Variables

Set custom environment variables if needed:

```json
"env": {
  "PYTHONPATH": "C:\\Users\\USERNAME\\Documents\\Mneme",
  "MNEME_DEBUG": "true",
  "MNEME_LOG_LEVEL": "INFO"
}
```

## Verification Checklist

Before completing setup, verify:

- [ ] Python 3.10+ installed and in PATH
- [ ] FastMCP package installed
- [ ] MCP server files in correct directory
- [ ] Claude Desktop configuration updated
- [ ] Notion integration enabled
- [ ] Test commands work in Claude
- [ ] Memory system responds correctly
- [ ] (Optional) Multi-device sync configured

## Next Steps

After successful installation:

1. **Read the [User Guide](USER_GUIDE.md)** for detailed usage instructions
2. **Set up daily workflow** as described in the user guide
3. **Explore features** with simple test commands
4. **Configure backup strategy** for your memory data

---

*Installation complete! Your personal memory lighthouse is ready to bridge your past and present thoughts.*