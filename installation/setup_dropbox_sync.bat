@echo off
chcp 65001 >nul
echo ========================================
echo Mneme Dropbox同期セットアップ
echo ========================================
echo.

cd C:\Users\%USERNAME%

echo Dropboxフォルダを確認中...
if not exist "%USERPROFILE%\Dropbox" (
    echo エラー: Dropboxフォルダが見つかりません。
    echo Dropboxがインストールされていることを確認してください。
    pause
    exit /b 1
)

echo 1. Dropboxに同期フォルダを作成中...
mkdir "%USERPROFILE%\Dropbox\Mneme_Memory_Sync" 2>nul

echo 2. 現在のデータをDropboxにコピー中...
xcopy .jah_thoughttrace "%USERPROFILE%\Dropbox\Mneme_Memory_Sync" /E /I /Y

echo 3. 元のフォルダを削除中...
rmdir .jah_thoughttrace /S /Q

echo 4. シンボリックリンクを作成中...
mklink /D .jah_thoughttrace "%USERPROFILE%\Dropbox\Mneme_Memory_Sync"

echo.
echo ========================================
echo セットアップ完了！
echo ========================================
echo.
echo 次のステップ：
echo 1. Dropboxの同期が完了するまで待つ
echo 2. 他のPCで同様の設定を実行
echo 3. 各PCでClaude Desktopを再起動
echo.
pause