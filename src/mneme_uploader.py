#!/usr/bin/env python3
"""
Mneme専用アップローダー
新しいNotionデータベース用のカスタムアップローダー
"""

import os
import sys
from pathlib import Path
from notion_client import Client
from datetime import datetime
import time

# 環境変数からNotion APIキーを取得
NOTION_API_KEY = os.environ.get('NOTION_API_KEY')
if not NOTION_API_KEY:
    print("エラー: NOTION_API_KEY環境変数が設定されていません")
    sys.exit(1)

# Notionクライアント初期化
notion = Client(auth=NOTION_API_KEY)

def upload_to_mneme(file_path: str, title: str, tags: list, database_id: str):
    """
    MnemeデータベースにMarkdownファイルをアップロード
    
    Args:
        file_path: Markdownファイルのパス
        title: ページタイトル
        tags: タグリスト
        database_id: NotionデータベースID
    
    Returns:
        dict: 結果情報
    """
    try:
        # ファイル内容を読み込む
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Notionページを作成
        # プロパティ名は実際のデータベースに合わせて調整が必要
        page = notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "名前": {  # データベースの実際のプロパティ名
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                },
                # Tagsプロパティが存在する場合のみ追加
                # "Tags": {
                #     "multi_select": [{"name": tag} for tag in tags]
                # },
            },
            children=[
                {
                    "object": "block",
                    "type": "paragraph",
                    "paragraph": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {"content": content[:500] + "\\n\\n[Full document content available in the uploaded file]"}
                            }
                        ]
                    }
                }
            ]
        )
        
        return {
            "success": True,
            "url": page.get("url", ""),
            "id": page.get("id", "")
        }
        
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def main():
    """メイン処理"""
    # ドキュメントフォルダ
    docs_folder = Path(r'C:\Users\liuco\Desktop\JaH思考トレースプログラム_完全ドキュメント')
    
    # データベースID
    database_id = 'YOUR_DATABASE_ID'
    
    # アップロードファイル（アップロード済みをスキップ）
    already_uploaded = ['README.md', '01_初期構想書.md']
    files = [
        ('02_使用ガイド.md', 'Mneme - 使用ガイド', ['Mneme', 'ドキュメント', 'ガイド', 'Day16']),
        ('03_セットアップガイド.md', 'Mneme - セットアップガイド', ['Mneme', 'ドキュメント', 'セットアップ', 'Day16']),
        ('04_同期マニュアル.md', 'Mneme - 同期マニュアル', ['Mneme', 'ドキュメント', '同期', 'Day16'])
    ]
    
    # 最初にデータベースのプロパティを確認
    print("データベースのプロパティを確認中...")
    try:
        db_info = notion.databases.retrieve(database_id)
        print("\n利用可能なプロパティ:")
        for prop_name, prop_info in db_info.get("properties", {}).items():
            print(f"  - {prop_name}: {prop_info.get('type')}")
        print("\n")
    except Exception as e:
        print(f"データベース情報の取得に失敗: {e}")
        return
    
    # 各ファイルをアップロード
    success_count = 0
    for filename, title, tags in files:
        file_path = docs_folder / filename
        if file_path.exists():
            print(f"アップロード中: {filename}")
            result = upload_to_mneme(str(file_path), title, tags, database_id)
            
            if result["success"]:
                success_count += 1
                print(f"[SUCCESS] {title}")
                print(f"  URL: {result['url']}")
            else:
                print(f"[FAILED] {title}")
                print(f"  Error: {result['error']}")
            
            # API制限対策
            time.sleep(2)
        else:
            print(f"[NOT FOUND] {filename}")
    
    print(f"\n完了: {success_count}/{len(files)} ファイルがアップロードされました")


if __name__ == "__main__":
    main()