#!/usr/bin/env python3
"""
Simple Memory MCP Server (for environment variable testing)
"""

import os
import json
from datetime import datetime
from pathlib import Path
from fastmcp import FastMCP

# Data storage directory
DATA_DIR = Path.home() / ".mneme_memory"
DATA_DIR.mkdir(exist_ok=True)
MEMORIES_FILE = DATA_DIR / "simple_memories.json"

# Server initialization
mcp = FastMCP("Simple Memory MCP")

# Memory initialization
if not MEMORIES_FILE.exists():
    with open(MEMORIES_FILE, 'w', encoding='utf-8') as f:
        json.dump([], f)


@mcp.tool()
async def save_simple_memory(content: str) -> dict:
    """Save a simple memory"""
    with open(MEMORIES_FILE, 'r', encoding='utf-8') as f:
        memories = json.load(f)
    
    memory = {
        "id": len(memories) + 1,
        "content": content,
        "timestamp": datetime.now().isoformat()
    }
    
    memories.append(memory)
    
    with open(MEMORIES_FILE, 'w', encoding='utf-8') as f:
        json.dump(memories, f, ensure_ascii=False, indent=2)
    
    return {"success": True, "id": memory["id"], "message": "Memory saved"}


@mcp.tool()
async def get_all_memories() -> dict:
    """Get all memories"""
    with open(MEMORIES_FILE, 'r', encoding='utf-8') as f:
        memories = json.load(f)
    
    return {"success": True, "memories": memories, "count": len(memories)}


if __name__ == "__main__":
    print("Simple Memory MCP Server")
    print(f"Data location: {DATA_DIR}")
    mcp.run()