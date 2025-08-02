# Mneme - クイックスタートガイド

## 🚀 5分でセットアップ

### 1. 必要なもの
- Windows 10/11
- Python 3.10以上（[python.org](https://www.python.org/)からダウンロード）
- Claude Desktop（インストール済み）

### 2. Pythonパッケージのインストール
```cmd
pip install fastmcp
```

### 3. ファイルのコピー
1. `INSTALLATION_FILES`フォルダから`hybrid_memory_mcp.py`を以下にコピー：
   ```
   C:\Users\[あなたのユーザー名]\Documents\Mneme\
   ```

2. Claude Desktop設定を開く：
   ```cmd
   notepad %APPDATA%\Claude\claude_desktop_config.json
   ```

3. `claude_desktop_config.json`の内容をコピー＆ペースト
   - `[YOUR_USERNAME]`を実際のユーザー名に置換

### 4. Claude Desktop再起動
1. タスクトレイのClaudeアイコンを右クリック → 終了
2. Claude Desktopを起動
3. **新しい会話を開始**

### 5. 動作確認
新しいClaude会話で：
```
「get_memory_stats を実行して」
```

成功すれば準備完了！

---

## 📝 最初の使い方

### 朝のインスピレーション
```
「今日のインスピレーションを生成して」
```

### ランダムな記憶
```
「過去の記憶をランダムに見せて」
```

### メモリ保存
```
「この内容を保存して」
```

---

## 🔄 Dropbox同期（オプション）

複数のPCで使う場合：
1. `setup_dropbox_sync.bat`を管理者権限で実行
2. 他のPCでも同様の設定

---

## 📚 詳細情報

- **初期構想**: `01_初期構想書.md`
- **使い方**: `02_使用ガイド.md`
- **セットアップ**: `03_セットアップガイド.md`
- **同期設定**: `04_同期マニュアル.md`

---

## 🌟 Mnemeとは

**Mneme**（ムネーメー）は、ギリシャ神話の記憶の女神から名付けられた、あなたの思考と記憶を永続化するシステムです。

「すべての記憶が、新しい創造の種となる」

---

*Start small, grow daily, harvest forever.*