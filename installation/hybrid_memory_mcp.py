#!/usr/bin/env python3
"""
Mneme - ハイブリッドメモリMCPサーバー
ClaudeのネイティブNotion連携と連動して動作
"""

import os
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Any
from fastmcp import FastMCP

# データ保存先
DATA_DIR = Path.home() / ".jah_thoughttrace"
DATA_DIR.mkdir(exist_ok=True)
MEMORIES_FILE = DATA_DIR / "memories.json"
INDEX_FILE = DATA_DIR / "index.json"
SERENDIPITY_FILE = DATA_DIR / "serendipity_cache.json"

# サーバーの初期化
mcp = FastMCP("Mneme - Personal Memory Lighthouse")

# ファイル初期化
for file_path in [MEMORIES_FILE, INDEX_FILE, SERENDIPITY_FILE]:
    if not file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)


def load_json(file_path):
    """JSONファイルを読み込む"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(file_path, data):
    """JSONファイルに保存"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


@mcp.tool()
async def save_from_notion(
    content: str,
    title: str,
    source_db: str,
    notion_url: Optional[str] = None,
    tags: Optional[List[str]] = None
) -> Dict:
    """
    ClaudeがNotionから取得した情報をローカルメモリに保存
    
    Args:
        content: Notionから取得した内容
        title: ページのタイトル
        source_db: 取得元のデータベース名（日記、総合メモなど）
        notion_url: NotionページのURL
        tags: タグのリスト
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # メモリIDの生成
    memory_id = f"notion_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # メモリオブジェクト作成
    memory = {
        "id": memory_id,
        "type": "notion_import",
        "content": {
            "original": content,
            "title": title,
            "summary": content[:200] + "..." if len(content) > 200 else content
        },
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "source": f"Notion:{source_db}",
            "notion_url": notion_url,
            "tags": tags or [],
            "importance": 0.7,
            "access_count": 0
        }
    }
    
    # 保存
    memories[memory_id] = memory
    save_json(MEMORIES_FILE, memories)
    
    # インデックス更新
    if "notion_imports" not in index:
        index["notion_imports"] = {}
    if source_db not in index["notion_imports"]:
        index["notion_imports"][source_db] = []
    index["notion_imports"][source_db].append(memory_id)
    
    # タグインデックス
    if "tags" not in index:
        index["tags"] = {}
    for tag in (tags or []):
        if tag not in index["tags"]:
            index["tags"][tag] = []
        index["tags"][tag].append(memory_id)
    
    save_json(INDEX_FILE, index)
    
    return {
        "success": True,
        "memory_id": memory_id,
        "message": f"Notionデータを保存しました: {title}",
        "summary": memory["content"]["summary"]
    }


@mcp.tool()
async def get_daily_inspiration_prompt() -> Dict:
    """
    今日のインスピレーションのためのプロンプトを生成
    ClaudeがNotionから検索する際のガイド
    """
    today = datetime.now()
    prompts = {
        "morning_quote": {
            "databases": ["フレーズ", "名句集"],
            "prompt": "今日の朝にふさわしい、インスピレーションを与える言葉を1つ選んでください"
        },
        "one_year_ago": {
            "databases": ["日記", "総合メモ"],
            "date": (today - timedelta(days=365)).strftime("%Y-%m-%d"),
            "prompt": f"1年前（{(today - timedelta(days=365)).strftime('%Y年%m月%d日')}）の記録を探してください"
        },
        "forgotten_idea": {
            "databases": ["アイディア集"],
            "days_ago": 180,
            "prompt": "180日以上前の、まだ実現していないアイデアを1つ見つけてください"
        },
        "past_learning": {
            "databases": ["Learning Log"],
            "days_ago": 90,
            "prompt": "90日以上前の学習記録から、今でも役立つ学びを1つ選んでください"
        },
        "creative_seed": {
            "databases": ["梗概ライティング練習"],
            "prompt": "過去の創作練習から、新しい物語の種となりそうなものを1つ選んでください"
        }
    }
    
    return {
        "success": True,
        "date": today.strftime("%Y-%m-%d"),
        "prompts": prompts,
        "message": "Notion検索用のプロンプトを生成しました",
        "instruction": "これらのプロンプトを使って、ClaudeのNotion連携で検索してください"
    }


@mcp.tool()
async def create_serendipity_cache(
    discoveries: List[Dict[str, str]]
) -> Dict:
    """
    セレンディピティ（偶然の発見）をキャッシュ
    
    Args:
        discoveries: [{"content": "...", "source": "...", "date": "..."}]
    """
    cache = load_json(SERENDIPITY_FILE)
    
    today = datetime.now().strftime("%Y-%m-%d")
    cache[today] = {
        "created_at": datetime.now().isoformat(),
        "discoveries": discoveries,
        "accessed": 0
    }
    
    save_json(SERENDIPITY_FILE, cache)
    
    return {
        "success": True,
        "cached_count": len(discoveries),
        "message": "セレンディピティをキャッシュしました"
    }


@mcp.tool()
async def get_random_memory(memory_type: Optional[str] = None) -> Dict:
    """
    ランダムなローカルメモリを取得（過去の発見を呼び起こす）
    """
    memories = load_json(MEMORIES_FILE)
    
    if not memories:
        return {
            "success": False,
            "message": "まだメモリが保存されていません"
        }
    
    # フィルタリング
    filtered_memories = memories
    if memory_type:
        filtered_memories = {
            k: v for k, v in memories.items() 
            if v.get("type") == memory_type
        }
    
    if not filtered_memories:
        return {
            "success": False,
            "message": f"タイプ '{memory_type}' のメモリが見つかりません"
        }
    
    # ランダム選択（古いものを優先）
    memory_list = list(filtered_memories.items())
    # 重み付け：古いものほど選ばれやすく
    weights = []
    now = datetime.now()
    for _, memory in memory_list:
        created = datetime.fromisoformat(memory["metadata"]["timestamp"])
        days_old = (now - created).days
        weights.append(days_old + 1)  # 古いほど重みが大きい
    
    selected_key, selected_memory = random.choices(memory_list, weights=weights)[0]
    
    # アクセスカウント更新
    memories[selected_key]["metadata"]["access_count"] += 1
    save_json(MEMORIES_FILE, memories)
    
    return {
        "success": True,
        "memory": selected_memory,
        "days_old": weights[memory_list.index((selected_key, selected_memory))] - 1,
        "message": "過去の記憶を呼び起こしました"
    }


@mcp.tool()
async def link_claude_conversation(
    summary: str,
    key_insights: List[str],
    related_topics: List[str]
) -> Dict:
    """
    現在のClaude会話の要点を保存
    
    Args:
        summary: 会話の要約
        key_insights: 重要な洞察のリスト
        related_topics: 関連トピック
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # 会話メモリの作成
    conversation_id = f"conv_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    memory = {
        "id": conversation_id,
        "type": "conversation",
        "content": {
            "summary": summary,
            "insights": key_insights,
            "topics": related_topics
        },
        "metadata": {
            "timestamp": datetime.now().isoformat(),
            "source": "Claude Conversation",
            "importance": 0.8,
            "access_count": 0
        }
    }
    
    memories[conversation_id] = memory
    save_json(MEMORIES_FILE, memories)
    
    # トピックインデックス更新
    if "topics" not in index:
        index["topics"] = {}
    for topic in related_topics:
        if topic not in index["topics"]:
            index["topics"][topic] = []
        index["topics"][topic].append(conversation_id)
    
    save_json(INDEX_FILE, index)
    
    return {
        "success": True,
        "conversation_id": conversation_id,
        "message": "会話の要点を保存しました",
        "insights_count": len(key_insights)
    }


@mcp.tool()
async def search_by_context(
    context: str,
    limit: int = 5
) -> Dict:
    """
    文脈に基づいてローカルメモリを検索
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # 簡易的なキーワード抽出
    keywords = context.lower().split()
    
    # スコアリング
    scores = {}
    for memory_id, memory in memories.items():
        score = 0
        content_lower = json.dumps(memory["content"]).lower()
        
        # キーワードマッチング
        for keyword in keywords:
            if keyword in content_lower:
                score += 1
        
        # メタデータマッチング
        for tag in memory.get("metadata", {}).get("tags", []):
            if any(keyword in tag.lower() for keyword in keywords):
                score += 2
        
        if score > 0:
            scores[memory_id] = score
    
    # ソートして上位を返す
    sorted_results = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:limit]
    
    results = []
    for memory_id, score in sorted_results:
        memory = memories[memory_id]
        memory["relevance_score"] = score
        results.append(memory)
    
    return {
        "success": True,
        "context": context,
        "found": len(results),
        "memories": results,
        "message": f"{len(results)}件の関連メモリが見つかりました"
    }


@mcp.tool()
async def get_memory_stats() -> Dict:
    """
    メモリシステムの統計情報を取得
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # タイプ別集計
    type_counts = {}
    for memory in memories.values():
        memory_type = memory.get("type", "unknown")
        type_counts[memory_type] = type_counts.get(memory_type, 0) + 1
    
    # 時間分析
    if memories:
        timestamps = [
            datetime.fromisoformat(m["metadata"]["timestamp"]) 
            for m in memories.values()
        ]
        oldest = min(timestamps)
        newest = max(timestamps)
        days_span = (newest - oldest).days
    else:
        days_span = 0
        oldest = newest = None
    
    return {
        "success": True,
        "total_memories": len(memories),
        "type_distribution": type_counts,
        "total_tags": len(index.get("tags", {})),
        "total_topics": len(index.get("topics", {})),
        "notion_sources": len(index.get("notion_imports", {})),
        "time_span_days": days_span,
        "oldest_memory": oldest.isoformat() if oldest else None,
        "newest_memory": newest.isoformat() if newest else None,
        "message": "Mnemeメモリシステムの統計情報"
    }


if __name__ == "__main__":
    print("Mneme - Personal Memory Lighthouse MCP Server")
    print("ClaudeのNotion連携と連動して動作します")
    print(f"データ保存先: {DATA_DIR}")
    mcp.run()