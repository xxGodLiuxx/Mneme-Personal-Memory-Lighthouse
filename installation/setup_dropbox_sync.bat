@echo off
chcp 65001 >nul
echo ========================================
echo Mneme Dropbox Sync Setup
echo ========================================
echo.

cd C:\Users\%USERNAME%

echo Checking Dropbox folder...
if not exist "%USERPROFILE%\Dropbox" (
    echo Error: Dropbox folder not found.
    echo Please ensure Dropbox is installed.
    pause
    exit /b 1
)

echo 1. Creating sync folder in Dropbox...
mkdir "%USERPROFILE%\Dropbox\Mneme_Memory_Sync" 2>nul

echo 2. Copying current data to Dropbox...
xcopy .mneme_memory "%USERPROFILE%\Dropbox\Mneme_Memory_Sync" /E /I /Y

echo 3. Removing original folder...
rmdir .mneme_memory /S /Q

echo 4. Creating symbolic link...
mklink /D .mneme_memory "%USERPROFILE%\Dropbox\Mneme_Memory_Sync"

echo.
echo ========================================
echo Setup Complete!
echo ========================================
echo.
echo Next steps:
echo 1. Wait for Dropbox sync to complete
echo 2. Run the same setup on other PCs
echo 3. Restart Claude Desktop on each PC
echo.
pause