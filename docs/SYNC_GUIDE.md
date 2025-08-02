# Mneme - Personal Memory Lighthouse Multi-Device Sync Guide

## Overview

This manual explains how to synchronize Mneme data across multiple Windows PCs.

### Benefits of Synchronization
- 🏠 Share the same memories between home and work PCs
- 💼 Seamless work continuation between desktop and laptop
- 🔄 Data protection through automatic backups
- 📱 Preparation for future mobile access

---

## Choosing a Sync Method

### Recommended: Dropbox Sync
- ✅ Easy setup
- ✅ Real-time synchronization
- ✅ Version history feature
- ✅ Selective sync capability

### Alternatives
1. **OneDrive**: Strong Windows integration
2. **Google Drive**: Large storage capacity
3. **Git**: Excellent version control
4. **NAS**: Complete private environment

## Dropbox Sync Detailed Steps

### Prerequisites
- Dropbox account (free or paid)
- Dropbox Desktop app installed on all devices
- Administrator privileges on all PCs

### Step 1: Primary Device Setup

#### 1.1 Install Dropbox Desktop
1. Download from [dropbox.com](https://www.dropbox.com)
2. Install and sign in to your account
3. Wait for initial sync to complete

#### 1.2 Run Automatic Setup
```cmd
# Run as Administrator
installation\setup_dropbox_sync.bat
```

This script will:
- Create sync folder: `%USERPROFILE%\Dropbox\Mneme_Memory_Sync\`
- Set up symbolic links
- Copy existing memory data
- Configure automatic sync

#### 1.3 Verify Setup
Check that the following folders exist:
```
%USERPROFILE%\Dropbox\Mneme_Memory_Sync\
%USERPROFILE%\.jah_thoughttrace\ (linked to above)
```

### Step 2: Secondary Device Setup

#### 2.1 Install Prerequisites
- Install Mneme according to [Installation Guide](INSTALLATION.md)
- Install and configure Dropbox Desktop
- Wait for sync folder to appear

#### 2.2 Run Setup Script
```cmd
# Run as Administrator
installation\setup_dropbox_sync.bat
```

The script will detect existing sync data and create appropriate links.

#### 2.3 Test Synchronization
1. Save a test memory on Device A
2. Check if it appears on Device B within a few minutes
3. Verify both devices can read/write successfully

## Manual Sync Setup

If automatic setup fails, follow these manual steps:

### Step 1: Create Sync Folder
```cmd
mkdir "%USERPROFILE%\Dropbox\Mneme_Memory_Sync"
```

### Step 2: Copy Existing Data (Primary Device Only)
```cmd
xcopy "%USERPROFILE%\.jah_thoughttrace\*" "%USERPROFILE%\Dropbox\Mneme_Memory_Sync\" /E /Y
```

### Step 3: Create Symbolic Links
```cmd
# Remove existing directory (backup first!)
rmdir "%USERPROFILE%\.jah_thoughttrace" /S /Q

# Create symbolic link
mklink /D "%USERPROFILE%\.jah_thoughttrace" "%USERPROFILE%\Dropbox\Mneme_Memory_Sync"
```

### Step 4: Set Permissions
```cmd
icacls "%USERPROFILE%\.jah_thoughttrace" /grant:r "%USERNAME%:(OI)(CI)F"
```

## Alternative Sync Methods

### OneDrive Sync

#### Setup
```cmd
# Replace Dropbox path with OneDrive path
mklink /D "%USERPROFILE%\.jah_thoughttrace" "%USERPROFILE%\OneDrive\Mneme_Memory_Sync"
```

#### Pros
- Built into Windows
- Office integration
- 5GB free storage

#### Cons
- Less reliable for small file changes
- Sync conflicts more common

### Git-Based Sync

#### Setup
```cmd
cd "%USERPROFILE%\.jah_thoughttrace"
git init
git add .
git commit -m "Initial memory data"
git remote add origin https://github.com/yourusername/mneme-memories.git
git push -u origin main
```

#### Daily Workflow
```cmd
# Pull changes
git pull origin main

# After using Mneme
git add .
git commit -m "Memory updates $(date)"
git push origin main
```

#### Pros
- Complete version history
- Merge conflict resolution
- Free private repos

#### Cons
- Requires Git knowledge
- Manual sync required
- More complex setup

## Troubleshooting

### Common Issues

#### Sync Conflicts
**Problem**: Multiple devices modify same memory file
**Solution**:
1. Check Dropbox conflict files
2. Manually merge content
3. Delete duplicate files

#### Permission Errors
**Problem**: "Access denied" when creating links
**Solution**:
1. Run Command Prompt as Administrator
2. Check UAC settings
3. Verify file permissions

#### Symbolic Link Failures
**Problem**: Links not created properly
**Solution**:
1. Enable Developer Mode in Windows
2. Use `mklink` with different parameters
3. Try manual folder copy as fallback

#### Sync Delays
**Problem**: Changes take too long to sync
**Solution**:
1. Check Dropbox sync status
2. Restart Dropbox application
3. Verify network connectivity
4. Check selective sync settings

### Advanced Configuration

#### Selective Sync
Configure Dropbox to only sync memory data:
1. Open Dropbox settings
2. Go to Sync → Selective Sync
3. Uncheck unnecessary folders
4. Keep `Mneme_Memory_Sync` checked

#### Bandwidth Limiting
For slow connections:
1. Dropbox Settings → Network
2. Set upload/download limits
3. Schedule sync during off-hours

#### Conflict Resolution
Set up automatic conflict resolution:
```cmd
# Create conflict resolution script
echo @echo off > resolve_conflicts.bat
echo for %%f in ("%USERPROFILE%\.jah_thoughttrace\*conflicted*") do (>> resolve_conflicts.bat
echo   echo Found conflict: %%f >> resolve_conflicts.bat
echo   rem Add your resolution logic here >> resolve_conflicts.bat
echo ) >> resolve_conflicts.bat
```

## Best Practices

### Data Safety
1. **Regular Backups**: Even with sync, maintain separate backups
2. **Version Control**: Keep important memories in version-controlled files
3. **Conflict Prevention**: Avoid simultaneous editing on multiple devices

### Performance Optimization
1. **Cleanup**: Regularly remove old temp files
2. **Compression**: Use file compression for large memory archives
3. **Monitoring**: Check sync status regularly

### Security Considerations
1. **Encryption**: Consider encrypting sensitive memories
2. **Access Control**: Limit device access to sync folders
3. **Privacy**: Be aware of cloud provider data policies

## Verification Checklist

After setup completion:

- [ ] Memory data syncs within 5 minutes between devices
- [ ] Both devices can save new memories successfully
- [ ] No permission errors when accessing memory files
- [ ] Dropbox shows no sync errors
- [ ] Memory statistics show correct data on all devices
- [ ] Search functionality works on all devices

## Emergency Procedures

### Data Recovery
If sync fails and data is lost:
1. Check Dropbox version history
2. Restore from local backups
3. Use Dropbox recovery tools
4. Contact support if necessary

### Fresh Start
To reset sync completely:
1. Backup current data
2. Unlink all symbolic links
3. Clear sync folders
4. Restart setup process

---

*Multi-device sync enables your memories to follow you wherever you work. Set it up once, and your personal memory lighthouse will be available on all your devices.*