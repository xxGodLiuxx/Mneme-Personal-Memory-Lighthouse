#!/usr/bin/env python3
"""
Hybrid Memory MCP Server
Works in conjunction with Claude's native Notion integration
"""

import os
import json
import random
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional, Any
from fastmcp import FastMCP

# Data storage directory
DATA_DIR = Path.home() / ".mneme_memory"
DATA_DIR.mkdir(exist_ok=True)
MEMORIES_FILE = DATA_DIR / "memories.json"
INDEX_FILE = DATA_DIR / "index.json"
SERENDIPITY_FILE = DATA_DIR / "serendipity_cache.json"

# Server initialization
mcp = FastMCP("Mneme - Personal Memory Lighthouse")

# File initialization
for file_path in [MEMORIES_FILE, INDEX_FILE, SERENDIPITY_FILE]:
    if not file_path.exists():
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump({}, f)


def load_json(file_path):
    """Load JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(file_path, data):
    """Save to JSON file"""
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
    Save information retrieved by Claude from Notion to local memory
    
    Args:
        content: Content retrieved from Notion
        title: Page title
        source_db: Source database name (diary, general notes, etc.)
        notion_url: Notion page URL
        tags: List of tags
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # Generate memory ID
    memory_id = f"notion_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    
    # Create memory structure
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
    
    # Save memory
    memories[memory_id] = memory
    save_json(MEMORIES_FILE, memories)
    
    # Update index
    if "notion_imports" not in index:
        index["notion_imports"] = {}
    if source_db not in index["notion_imports"]:
        index["notion_imports"][source_db] = []
    index["notion_imports"][source_db].append(memory_id)
    
    # Update tag index
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
        "message": f"Notion data saved: {title}",
        "summary": memory["content"]["summary"]
    }


@mcp.tool()
async def get_daily_inspiration_prompt() -> Dict:
    """
    Generate daily inspiration prompts
    Guide for Claude to search Notion
    """
    today = datetime.now()
    prompts = {
        "morning_quote": {
            "databases": ["Phrases", "Quote Collection"],
            "prompt": "Find an inspiring quote suitable for this morning"
        },
        "one_year_ago": {
            "databases": ["Diary", "General Notes"],
            "date": (today - timedelta(days=365)).strftime("%Y-%m-%d"),
            "prompt": f"Search for records from one year ago ({(today - timedelta(days=365)).strftime('%Y-%m-%d')})"
        },
        "forgotten_idea": {
            "databases": ["Idea Collection"],
            "days_ago": 180,
            "prompt": "Find an unrealized idea from 180+ days ago"
        },
        "past_learning": {
            "databases": ["Learning Log"],
            "days_ago": 90,
            "prompt": "Find a valuable learning from 90+ days ago"
        },
        "creative_seed": {
            "databases": ["Creative Writing Practice"],
            "prompt": "Find a past creative exercise that could inspire new stories"
        }
    }
    
    return {
        "success": True,
        "date": today.strftime("%Y-%m-%d"),
        "prompts": prompts,
        "message": "Generated Notion search prompts",
        "instruction": "Use these prompts to search your Notion databases with Claude's Notion integration"
    }


@mcp.tool()
async def cache_serendipity(
    discoveries: List[Dict[str, str]]
) -> Dict:
    """
    Cache serendipitous discoveries for later retrieval
    
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
        "message": "Serendipity cached successfully"
    }


@mcp.tool()
async def get_random_memory(memory_type: Optional[str] = None) -> Dict:
    """
    Retrieve a random memory with aging bias (older memories more likely)
    """
    memories = load_json(MEMORIES_FILE)
    
    if not memories:
        return {
            "success": False,
            "message": "No memories saved yet"
        }
    
    # Filter by type if specified
    filtered_memories = memories
    if memory_type:
        filtered_memories = {
            k: v for k, v in memories.items() 
            if v.get("type") == memory_type
        }
    
    if not filtered_memories:
        return {
            "success": False,
            "message": f"No memories of type '{memory_type}' found"
        }
    
    # Apply aging bias (older memories have higher weight)
    memory_list = list(filtered_memories.items())
    
    weights = []
    now = datetime.now()
    for _, memory in memory_list:
        created = datetime.fromisoformat(memory["metadata"]["timestamp"])
        days_old = (now - created).days
        weights.append(days_old + 1)  # Older = higher weight
    
    selected_key, selected_memory = random.choices(memory_list, weights=weights)[0]
    
    # Update access count
    memories[selected_key]["metadata"]["access_count"] += 1
    save_json(MEMORIES_FILE, memories)
    
    return {
        "success": True,
        "memory": selected_memory,
        "days_old": weights[memory_list.index((selected_key, selected_memory))] - 1,
        "message": "Retrieved a memory from the past"
    }


@mcp.tool()
async def link_claude_conversation(
    summary: str,
    key_insights: List[str],
    related_topics: List[str]
) -> Dict:
    """
    Save key points from current Claude conversation
    
    Args:
        summary: Conversation summary
        key_insights: List of important insights
        related_topics: Related topics
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # Generate conversation ID
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
    
    # Update topic index
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
        "message": "Conversation key points saved",
        "insights_count": len(key_insights)
    }


@mcp.tool()
async def search_by_context(
    context: str,
    limit: int = 5
) -> Dict:
    """
    Search memories by context keywords
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # Simple keyword matching
    keywords = context.lower().split()
    
    # Score memories based on keyword matches
    scores = {}
    for memory_id, memory in memories.items():
        score = 0
        content_lower = json.dumps(memory["content"]).lower()
        
        # Check content matches
        for keyword in keywords:
            if keyword in content_lower:
                score += 1
        
        # Check tag matches (higher weight)
        for tag in memory.get("metadata", {}).get("tags", []):
            if any(keyword in tag.lower() for keyword in keywords):
                score += 2
                
        if score > 0:
            scores[memory_id] = score
    
    # Sort by relevance score
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
        "message": f"Found {len(results)} related memories"
    }


@mcp.tool()
async def get_memory_stats() -> Dict:
    """
    Get memory system statistics
    """
    memories = load_json(MEMORIES_FILE)
    index = load_json(INDEX_FILE)
    
    # Count by type
    type_counts = {}
    for memory in memories.values():
        memory_type = memory.get("type", "unknown")
        type_counts[memory_type] = type_counts.get(memory_type, 0) + 1
    
    # Calculate time span
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
        "message": "Memory system statistics"
    }


if __name__ == "__main__":
    print("Mneme - Personal Memory Lighthouse MCP Server")
    print("Works in conjunction with Claude's Notion integration")
    print(f"Data storage location: {DATA_DIR}")
    mcp.run()