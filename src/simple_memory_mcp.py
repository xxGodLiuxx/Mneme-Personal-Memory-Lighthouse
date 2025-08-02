#!/usr/bin/env python3
"""
シンプルなメモリMCPサーバー（環境変数テスト用）
"""

import os
import json
from datetime import datetime
from pathlib import Path
from fastmcp import FastMCP

# データ保存先
DATA_DIR = Path.home() / ".jah_thoughttrace"
DATA_DIR.mkdir(exist_ok=True)
MEMORIES_FILE = DATA_DIR / "simple_memories.json"

# サーバーの初期化
mcp = FastMCP("Simple Memory MCP")

# メモリの初期化
if not MEMORIES_FILE.exists():
    with open(MEMORIES_FILE, 'w', encoding='utf-8') as f:
        json.dump({}, f)

def load_memories():
    with open(MEMORIES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_memories(memories):
    with open(MEMORIES_FILE, 'w', encoding='utf-8') as f:
        json.dump(memories, f, ensure_ascii=False, indent=2)

@mcp.tool()
async def create_memory(content: str) -> dict:
    """新しいメモリを作成"""
    memories = load_memories()
    
    # タイムスタンプベースのキー
    key = datetime.now().strftime("memory_%Y%m%d_%H%M%S")
    
    memories[key] = {
        "content": content,
        "created_at": datetime.now().isoformat(),
        "accessed": 0
    }
    
    save_memories(memories)
    
    return {
        "success": True,
        "key": key,
        "message": f"メモリを作成しました: {key}"
    }

@mcp.tool()
async def get_memory(key: str) -> dict:
    """特定のメモリを取得"""
    memories = load_memories()
    
    if key in memories:
        memory = memories[key]
        memory["accessed"] += 1
        save_memories(memories)
        
        return {
            "success": True,
            "memory": memory
        }
    else:
        return {
            "success": False,
            "error": f"メモリが見つかりません: {key}"
        }

@mcp.tool()
async def list_memories() -> dict:
    """すべてのメモリをリスト"""
    memories = load_memories()
    
    return {
        "success": True,
        "count": len(memories),
        "memories": list(memories.keys())
    }

@mcp.tool()
async def check_env() -> dict:
    """環境変数をチェック（デバッグ用）"""
    notion_key = os.environ.get("NOTION_API_KEY")
    
    return {
        "NOTION_API_KEY_exists": notion_key is not None,
        "NOTION_API_KEY_length": len(notion_key) if notion_key else 0,
        "All_env_vars_count": len(os.environ),
        "Python_executable": os.sys.executable,
        "Working_directory": os.getcwd()
    }

if __name__ == "__main__":
    # デバッグ情報
    print(f"Simple Memory MCP Server starting...")
    print(f"Data directory: {DATA_DIR}")
    print(f"NOTION_API_KEY: {'SET' if os.environ.get('NOTION_API_KEY') else 'NOT SET'}")
    
    mcp.run()