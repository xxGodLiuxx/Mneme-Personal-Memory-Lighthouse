#!/usr/bin/env python3
"""
Simple Memory MCP Server (Fixed Version for environment variable testing)
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

try:
    from fastmcp import FastMCP
except ImportError:
    print("Error: fastmcp package not found. Please install it with: pip install fastmcp")
    sys.exit(1)

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


def load_memories():
    """Load memories with error handling"""
    try:
        with open(MEMORIES_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_memories(memories):
    """Save memories with error handling"""
    try:
        with open(MEMORIES_FILE, 'w', encoding='utf-8') as f:
            json.dump(memories, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"Error saving memories: {e}")
        return False


@mcp.tool()
async def save_simple_memory(content: str) -> dict:
    """Save a simple memory"""
    try:
        memories = load_memories()
        
        memory = {
            "id": len(memories) + 1,
            "content": content,
            "timestamp": datetime.now().isoformat()
        }
        
        memories.append(memory)
        
        if save_memories(memories):
            return {
                "success": True, 
                "id": memory["id"], 
                "message": "Memory saved successfully"
            }
        else:
            return {
                "success": False,
                "message": "Failed to save memory to file"
            }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error saving memory: {str(e)}"
        }


@mcp.tool()
async def get_all_memories() -> dict:
    """Get all memories"""
    try:
        memories = load_memories()
        
        return {
            "success": True, 
            "memories": memories, 
            "count": len(memories)
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error loading memories: {str(e)}"
        }


@mcp.tool()
async def clear_all_memories() -> dict:
    """Clear all memories (for testing purposes)"""
    try:
        if save_memories([]):
            return {
                "success": True,
                "message": "All memories cleared"
            }
        else:
            return {
                "success": False,
                "message": "Failed to clear memories"
            }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error clearing memories: {str(e)}"
        }


if __name__ == "__main__":
    print("Simple Memory MCP Server (Fixed Version)")
    print(f"Data location: {DATA_DIR}")
    try:
        mcp.run()
    except Exception as e:
        print(f"Error running MCP server: {e}")
        sys.exit(1)