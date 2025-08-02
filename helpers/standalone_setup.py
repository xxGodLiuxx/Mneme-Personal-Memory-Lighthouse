#!/usr/bin/env python3
"""
Mneme Standalone Setup Script
Fully independent version that works without PharosSystem
"""

import os
import sys
import json
import shutil
import subprocess
from pathlib import Path
from datetime import datetime

# Embedded tool code
MNEME_UPLOADER_CODE = '''#!/usr/bin/env python3
"""
Mneme Notion Preparation Tool (Standalone Version)
"""
import os
from pathlib import Path
from datetime import datetime

def prepare_for_notion(docs_folder):
    """Prepare files for Notion upload"""
    output_folder = docs_folder / "Notion_Ready"
    output_folder.mkdir(exist_ok=True)
    
    # Files to process
    files = [
        ('02_Usage_Guide.md', 'Mneme - Usage Guide'),
        ('03_Setup_Guide.md', 'Mneme - Setup Guide'),
        ('04_Sync_Manual.md', 'Mneme - Sync Manual')
    ]
    
    success_count = 0
    for filename, title in files:
        file_path = docs_folder / filename
        if file_path.exists():
            # Create file with header
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            header = f"# {title}\\n\\n"
            header += f"**Created**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\\n\\n"
            header += "---\\n\\n"
            
            output_path = output_folder / f"{title}.md"
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(header + content)
            
            success_count += 1
            print(f"[OK] {title}")
    
    return success_count, output_folder

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        docs_folder = Path(sys.argv[1])
    else:
        # Try default path
        default_folder = os.environ.get('MNEME_FOLDER_NAME', 'Mneme_Documents')
        docs_folder = Path.home() / "Dropbox" / default_folder
        if not docs_folder.exists():
            docs_folder = Path(input("Enter Mneme documents folder path: "))
    
    if docs_folder.exists():
        count, output = prepare_for_notion(docs_folder)
        print(f"\\nComplete: {count} files prepared")
        print(f"Output: {output}")
    else:
        print("[ERROR] Folder not found")
'''

class MnemeStandaloneSetup:
    """Standalone Mneme Setup"""
    
    def __init__(self):
        self.setup_file = Path.home() / '.mneme_setup_complete'
        self.mneme_tools_dir = Path.home() / '.mneme_tools'
        self.dropbox_root = None
        # Folder name can be customized via environment variable
        self.mneme_folder = os.environ.get('MNEME_FOLDER_NAME', 'Mneme_Documents')
        # Database URL from environment or config
        self.database_url = os.environ.get('MNEME_DATABASE_URL', 'https://www.notion.so/YOUR_DATABASE_ID')
    
    def create_standalone_tools(self):
        """Create standalone tools"""
        self.mneme_tools_dir.mkdir(exist_ok=True)
        
        # Create uploader tool
        uploader_path = self.mneme_tools_dir / "mneme_uploader.py"
        with open(uploader_path, 'w', encoding='utf-8') as f:
            f.write(MNEME_UPLOADER_CODE)
        
        print(f"[OK] Tool created: {uploader_path}")
        return uploader_path
    
    def find_dropbox(self):
        """Detect Dropbox folder"""
        common_paths = [
            Path.home() / "Dropbox",
            Path("C:/Users") / os.environ.get('USERNAME', '') / "Dropbox",
            Path("D:/Dropbox"),
            Path("E:/Dropbox")
        ]
        
        # Add custom paths from config if exists
        config_path = Path(__file__).parent / "config_local.json"
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                if 'dropbox_paths' in config:
                    for path_str in config['dropbox_paths']:
                        common_paths.append(Path(path_str).expanduser())
        
        for path in common_paths:
            if path.exists() and path.is_dir():
                mneme_path = path / self.mneme_folder
                if mneme_path.exists():
                    self.dropbox_root = path
                    return True
        
        # Manual input
        print("\nMneme folder not found in Dropbox.")
        print("Please enter one of the following:")
        print("1. Dropbox folder path")
        print(f"2. Full path to '{self.mneme_folder}' folder")
        
        user_path = input("\nPath: ").strip()
        if user_path:
            path = Path(user_path)
            if path.name == self.mneme_folder and path.exists():
                # Direct Mneme folder specified
                self.dropbox_root = path.parent
                return True
            elif (path / self.mneme_folder).exists():
                # Dropbox folder specified
                self.dropbox_root = path
                return True
        
        return False
    
    def create_desktop_shortcuts(self):
        """Create desktop shortcuts and batch files"""
        desktop = Path.home() / "Desktop"
        mneme_path = self.dropbox_root / self.mneme_folder
        
        # 1. Mneme launcher batch
        batch_content = f'''@echo off
echo === Mneme Launcher ===
echo.
echo Opening Mneme folder...
start "" "{mneme_path}"
echo.
echo Starting Claude Desktop...
start "" "claude"
echo.
echo [OK] Ready to use!
echo.
pause
'''
        batch_path = desktop / "Mneme_Launch.bat"
        with open(batch_path, 'w', encoding='utf-8') as f:
            f.write(batch_content)
        print(f"[OK] Launcher created: {batch_path}")
        
        # 2. Notion preparation batch
        uploader_path = self.mneme_tools_dir / "mneme_uploader.py"
        notion_batch = f'''@echo off
echo === Mneme Notion Preparation ===
echo.
python "{uploader_path}" "{mneme_path}"
echo.
echo Notion Database:
echo {self.database_url}
echo.
pause
'''
        notion_batch_path = desktop / "Mneme_Notion_Prep.bat"
        with open(notion_batch_path, 'w', encoding='utf-8') as f:
            f.write(notion_batch)
        print(f"[OK] Notion prep batch created: {notion_batch_path}")
        
        # 3. Folder shortcut (junction)
        try:
            shortcut_path = desktop / self.mneme_folder
            if not shortcut_path.exists():
                subprocess.run(['cmd', '/c', 'mklink', '/J', str(shortcut_path), str(mneme_path)], 
                             check=True, capture_output=True)
                print(f"[OK] Folder shortcut created: {shortcut_path}")
        except:
            print("[INFO] Please create folder shortcut manually")
        
        return True
    
    def setup_claude_mcp(self):
        """Configure Claude Desktop MCP"""
        mcp_config_path = Path.home() / "AppData" / "Roaming" / "Claude" / "claude_desktop_config.json"
        mcp_config_path.parent.mkdir(parents=True, exist_ok=True)
        
        if mcp_config_path.exists():
            with open(mcp_config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
        else:
            config = {"mcpServers": {}}
        
        mneme_docs_path = str(self.dropbox_root / self.mneme_folder).replace('\\', '/')
        config["mcpServers"]["filesystem"] = {
            "command": "npx",
            "args": [
                "@modelcontextprotocol/server-filesystem",
                mneme_docs_path
            ]
        }
        
        with open(mcp_config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print(f"[OK] Claude Desktop configuration updated")
        return True
    
    def save_setup_info(self):
        """Save setup information"""
        setup_info = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "dropbox_path": str(self.dropbox_root),
            "mneme_path": str(self.dropbox_root / self.mneme_folder),
            "tools_dir": str(self.mneme_tools_dir),
            "version": "2.0"
        }
        
        with open(self.setup_file, 'w', encoding='utf-8') as f:
            json.dump(setup_info, f, indent=2, ensure_ascii=False)
    
    def run(self):
        """Main setup process"""
        print("\n=== Mneme Standalone Setup (v2.0) ===\n")
        print("This setup works without PharosSystem.\n")
        
        # Check existing setup
        if self.setup_file.exists():
            with open(self.setup_file, 'r', encoding='utf-8') as f:
                info = json.load(f)
            print(f"[INFO] Previous setup: {info['date']}")
            if input("\nRe-run setup? (y/N): ").lower() != 'y':
                return
        
        # Step 1: Find Dropbox
        print("\n[1/4] Searching for Dropbox folder...")
        if not self.find_dropbox():
            print("[ERROR] Mneme folder not found")
            return
        
        print(f"[OK] Found Mneme folder: {self.dropbox_root / self.mneme_folder}")
        
        # Step 2: Create tools
        print("\n[2/4] Creating standalone tools...")
        self.create_standalone_tools()
        
        # Step 3: Create shortcuts
        print("\n[3/4] Creating desktop shortcuts...")
        self.create_desktop_shortcuts()
        
        # Step 4: Configure Claude
        print("\n[4/4] Configuring Claude Desktop...")
        if (Path.home() / "AppData" / "Local" / "Claude").exists():
            self.setup_claude_mcp()
        else:
            print("[INFO] Claude Desktop not installed")
        
        # Complete
        self.save_setup_info()
        
        print("\n=== Setup Complete! ===\n")
        print("Created on desktop:")
        print("  - Mneme_Launch.bat : Launch Mneme and Claude")
        print("  - Mneme_Notion_Prep.bat : Prepare files for Notion")
        print(f"  - {self.mneme_folder} : Folder shortcut")
        print("\nUsage:")
        print("1. Double-click 'Mneme_Launch.bat'")
        print("2. In Claude Desktop: 'Show me the Mneme documents'")
        print("\nNotion upload:")
        print("1. Run 'Mneme_Notion_Prep.bat'")
        print("2. Upload to Notion via Claude Desktop")


def main():
    """Main entry point"""
    try:
        setup = MnemeStandaloneSetup()
        setup.run()
    except Exception as e:
        print(f"\n[ERROR] An error occurred: {e}")
        import traceback
        traceback.print_exc()
        
        print("\n=== Manual Setup Instructions ===")
        print(f"1. Verify '{setup.mneme_folder}' exists in Dropbox")
        print("2. Create desktop shortcut manually")
        print("3. Configure Claude Desktop to access the folder")


if __name__ == "__main__":
    main()