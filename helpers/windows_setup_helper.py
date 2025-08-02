#!/usr/bin/env python3
"""
Windows Setup Helper for Mneme
Simplifies the setup process for Windows users
"""

import os
import sys
import subprocess
from pathlib import Path


def check_requirements():
    """Check if all requirements are met"""
    print("Checking requirements...")
    
    # Check Python version
    if sys.version_info < (3, 7):
        print(f"❌ Python {sys.version_info.major}.{sys.version_info.minor} detected.")
        print("   Please install Python 3.7 or higher.")
        return False
    else:
        print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Check for Dropbox
    dropbox_paths = [
        Path.home() / "Dropbox",
        Path("C:/Users") / os.environ.get('USERNAME', '') / "Dropbox"
    ]
    
    dropbox_found = any(p.exists() for p in dropbox_paths)
    if dropbox_found:
        print("✅ Dropbox folder found")
    else:
        print("❌ Dropbox folder not found")
        print("   Please install and set up Dropbox first.")
        return False
    
    return True


def download_setup_script():
    """Download the main setup script"""
    print("\nDownloading Mneme setup script...")
    
    # URL of the setup script
    script_url = "https://raw.githubusercontent.com/xxGodLiuxx/mneme-sync/master/mneme_standalone_setup.py"
    
    try:
        # Try using curl (usually available on Windows 10+)
        result = subprocess.run([
            "curl", "-L", "-o", "mneme_setup.py", script_url
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Setup script downloaded successfully")
            return True
        else:
            # Fallback to PowerShell
            ps_command = f'Invoke-WebRequest -Uri "{script_url}" -OutFile "mneme_setup.py"'
            result = subprocess.run([
                "powershell", "-Command", ps_command
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                print("✅ Setup script downloaded successfully")
                return True
    except Exception as e:
        print(f"❌ Failed to download: {e}")
    
    return False


def run_setup():
    """Run the main setup script"""
    print("\nRunning Mneme setup...")
    
    # Set any custom environment variables
    custom_folder = input("\nEnter custom folder name (press Enter for default): ").strip()
    if custom_folder:
        os.environ['MNEME_FOLDER_NAME'] = custom_folder
    
    # Run the setup
    try:
        subprocess.run([sys.executable, "mneme_setup.py"])
        return True
    except Exception as e:
        print(f"❌ Setup failed: {e}")
        return False


def main():
    """Main helper function"""
    print("=== Mneme Windows Setup Helper ===\n")
    print("This helper will:")
    print("1. Check your system requirements")
    print("2. Download the latest setup script")
    print("3. Run the setup with your preferences\n")
    
    if not check_requirements():
        print("\n⚠️  Please fix the issues above and run again.")
        input("\nPress Enter to exit...")
        return
    
    if not download_setup_script():
        print("\n⚠️  Could not download setup script.")
        print("Please download manually from:")
        print("https://github.com/xxGodLiuxx/mneme-sync")
        input("\nPress Enter to exit...")
        return
    
    if run_setup():
        print("\n✅ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Check your desktop for new shortcuts")
        print("2. Launch Mneme with the desktop shortcut")
        print("3. Start using Claude Desktop with your documents")
    else:
        print("\n⚠️  Setup encountered issues.")
        print("Please check the error messages above.")
    
    # Cleanup
    try:
        if Path("mneme_setup.py").exists():
            os.remove("mneme_setup.py")
    except:
        pass
    
    input("\nPress Enter to exit...")


if __name__ == "__main__":
    main()