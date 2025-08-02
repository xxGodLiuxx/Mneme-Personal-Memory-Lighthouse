# Mneme Quick Start Guide

**Get Mneme up and running in 5 minutes!**

---

> "Every memory becomes a seed of new creation."  
> — Start small, grow daily, harvest forever.

---

## 🎯 What is Mneme?

Mneme (mnemosyne) — named after the Greek goddess of memory, mother of the nine Muses. This system preserves and cultivates your daily memories, allowing them to bloom into new creations at unexpected moments.

---

## ⚡ 5-Minute Setup

### Prerequisites
- Windows 10/11
- Python 3.10 or higher
- Claude Desktop

### Installation Steps

#### 1. Install Python (2 minutes)
Download and install from [python.org](https://www.python.org/downloads/).

#### 2. Install Dependencies (30 seconds)
```bash
pip install fastmcp
```

#### 3. Deploy Files (1 minute)
1. Create folder: `Documents\Mneme`
2. Copy `hybrid_memory_mcp.py` to this folder

#### 4. Configure Claude Desktop (1 minute)
Add to your Claude Desktop config file:
```json
{
  "mcpServers": {
    "memory": {
      "command": "python",
      "args": ["C:/Users/YOUR_USERNAME/Documents/Mneme/hybrid_memory_mcp.py"]
    }
  }
}
```

#### 5. Restart Claude Desktop (30 seconds)
Completely quit and restart Claude Desktop.

---

## 🚀 First Experience

### 1. Morning Inspiration
```
"Generate today's inspiration"
```
Receive 5 elements combining past memories with new discoveries.

### 2. Random Memory
```
"Show me a random memory from the past"
```
Rediscover forgotten memories and gain new insights.

### 3. Save Memory
```
"Save this content"
```
Important conversations and discoveries are permanently preserved.

---

## 📱 Multi-Device Sync (Optional)

### Dropbox Setup
1. Install Dropbox
2. Move the `mneme_memories.json` file to Dropbox folder
3. Create a symbolic link:
```cmd
mklink "C:\Users\YOUR_USERNAME\Documents\Mneme\mneme_memories.json" "C:\Users\YOUR_USERNAME\Dropbox\Mneme\mneme_memories.json"
```

Now your memories sync across all devices!

---

## 💡 Next Steps

1. **Read the [User Guide](USER_GUIDE.md)** — Master all features
2. **Check [Sync Guide](SYNC_GUIDE.md)** — Set up multi-device synchronization
3. **Explore [Architecture](ARCHITECTURE.md)** — Understand the technical design

---

**Begin your memory journey today. Small seeds grow into mighty forests.**