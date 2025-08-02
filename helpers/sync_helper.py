#!/usr/bin/env python3
"""
Cross-Platform Sync Helper for Mneme
Helps manage synchronization across different cloud storage providers
"""

import os
import json
from pathlib import Path
from datetime import datetime


class SyncHelper:
    """Helper for managing document synchronization"""
    
    def __init__(self):
        self.config_file = Path.home() / '.mneme_sync_config.json'
        self.supported_providers = {
            'dropbox': self._find_dropbox,
            'onedrive': self._find_onedrive,
            'googledrive': self._find_googledrive,
            'icloud': self._find_icloud
        }
        self.load_config()
    
    def load_config(self):
        """Load existing configuration"""
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                self.config = json.load(f)
        else:
            self.config = {
                'providers': {},
                'sync_folders': [],
                'last_check': None
            }
    
    def save_config(self):
        """Save configuration"""
        self.config['last_check'] = datetime.now().isoformat()
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)
    
    def _find_dropbox(self):
        """Find Dropbox folder"""
        paths = [
            Path.home() / "Dropbox",
            Path("C:/Users") / os.environ.get('USERNAME', '') / "Dropbox",
            Path("/Users") / os.environ.get('USER', '') / "Dropbox",
            Path.home() / "Library/CloudStorage/Dropbox"
        ]
        return next((p for p in paths if p.exists()), None)
    
    def _find_onedrive(self):
        """Find OneDrive folder"""
        paths = [
            Path.home() / "OneDrive",
            Path("C:/Users") / os.environ.get('USERNAME', '') / "OneDrive",
            Path.home() / "Library/CloudStorage/OneDrive"
        ]
        return next((p for p in paths if p.exists()), None)
    
    def _find_googledrive(self):
        """Find Google Drive folder"""
        paths = [
            Path.home() / "Google Drive",
            Path("G:/My Drive"),
            Path.home() / "Library/CloudStorage/GoogleDrive"
        ]
        return next((p for p in paths if p.exists()), None)
    
    def _find_icloud(self):
        """Find iCloud folder"""
        paths = [
            Path.home() / "iCloudDrive",
            Path.home() / "Library/Mobile Documents/com~apple~CloudDocs"
        ]
        return next((p for p in paths if p.exists()), None)
    
    def detect_providers(self):
        """Detect available cloud storage providers"""
        print("Detecting cloud storage providers...")
        found = {}
        
        for name, finder in self.supported_providers.items():
            path = finder()
            if path:
                found[name] = str(path)
                print(f"✅ {name.capitalize()}: {path}")
            else:
                print(f"❌ {name.capitalize()}: Not found")
        
        self.config['providers'] = found
        self.save_config()
        return found
    
    def setup_sync_folder(self, provider, folder_name):
        """Set up a sync folder in specified provider"""
        if provider not in self.config['providers']:
            print(f"Error: {provider} not found on this system")
            return False
        
        provider_path = Path(self.config['providers'][provider])
        sync_path = provider_path / folder_name
        
        if not sync_path.exists():
            sync_path.mkdir(parents=True)
            print(f"Created: {sync_path}")
        else:
            print(f"Exists: {sync_path}")
        
        # Save to config
        sync_info = {
            'provider': provider,
            'folder': folder_name,
            'path': str(sync_path),
            'created': datetime.now().isoformat()
        }
        
        self.config['sync_folders'].append(sync_info)
        self.save_config()
        
        return True
    
    def create_shortcuts(self):
        """Create desktop shortcuts for all sync folders"""
        desktop = Path.home() / "Desktop"
        
        for sync_info in self.config['sync_folders']:
            provider = sync_info['provider']
            folder = sync_info['folder']
            path = sync_info['path']
            
            if os.name == 'nt':  # Windows
                # Create batch file
                batch_content = f'''@echo off
echo Opening {folder} on {provider}...
start "" "{path}"
'''
                batch_path = desktop / f"Mneme_{provider}_{folder}.bat"
                with open(batch_path, 'w') as f:
                    f.write(batch_content)
                print(f"Created shortcut: {batch_path}")
            else:
                # Unix-like systems
                print(f"Sync folder: {path}")
                print("Create alias in your shell config:")
                print(f'alias mneme-{provider}="cd \\"{path}\\""')
    
    def status(self):
        """Show sync status"""
        print("\n=== Mneme Sync Status ===")
        
        if not self.config['providers']:
            print("\nNo cloud providers detected.")
            return
        
        print("\nDetected Providers:")
        for provider, path in self.config['providers'].items():
            print(f"  - {provider}: {path}")
        
        if self.config['sync_folders']:
            print("\nConfigured Sync Folders:")
            for info in self.config['sync_folders']:
                print(f"  - {info['folder']} ({info['provider']})")
                print(f"    Path: {info['path']}")
        else:
            print("\nNo sync folders configured.")


def main():
    """Main function"""
    helper = SyncHelper()
    
    print("=== Mneme Cross-Platform Sync Helper ===\n")
    
    while True:
        print("\nOptions:")
        print("1. Detect cloud storage providers")
        print("2. Set up sync folder")
        print("3. Create desktop shortcuts")
        print("4. Show status")
        print("5. Exit")
        
        choice = input("\nSelect option (1-5): ").strip()
        
        if choice == '1':
            helper.detect_providers()
        
        elif choice == '2':
            providers = list(helper.config['providers'].keys())
            if not providers:
                print("No providers detected. Run option 1 first.")
                continue
            
            print("\nAvailable providers:")
            for i, p in enumerate(providers, 1):
                print(f"{i}. {p}")
            
            provider_idx = int(input("Select provider: ")) - 1
            provider = providers[provider_idx]
            
            folder_name = input("Enter folder name: ").strip()
            helper.setup_sync_folder(provider, folder_name)
        
        elif choice == '3':
            helper.create_shortcuts()
        
        elif choice == '4':
            helper.status()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid option")
    
    print("\nGoodbye!")


if __name__ == "__main__":
    main()