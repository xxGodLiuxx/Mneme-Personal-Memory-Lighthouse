# Mneme - Personal Memory Lighthouse 🧠

> *"Every memory is a seed for future creation"*

Mneme is a personal knowledge management system that bridges your past memories with present thinking through Claude Desktop integration. Named after the Greek goddess of memory, Mneme helps you discover forgotten insights and create new ideas through serendipity.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![MCP](https://img.shields.io/badge/protocol-MCP-purple.svg)](https://modelcontextprotocol.io/)

## ✨ Features

### 🎲 **Serendipity Engine**
- Random memory retrieval with aging bias
- Rediscover forgotten valuable insights
- Cross-temporal idea connections

### 🌅 **Daily Inspiration**
- Automated prompt generation for Notion searches
- 5 daily elements: quotes, past records, ideas, learnings, creative seeds
- Structured exploration of your knowledge base

### 🔗 **Hybrid Memory System**
- Local storage with cloud synchronization
- Leverages Claude's native Notion integration
- Session-persistent knowledge accumulation

### 💬 **Conversation Preservation**
- Automatic Claude conversation summarization
- Key insight extraction and storage
- Topic-based indexing and retrieval

## 🚀 Quick Start

### Prerequisites
- Windows 10/11, macOS, or Linux
- Python 3.10+
- [Claude Desktop](https://claude.ai/desktop) with Notion integration enabled
- Notion account (connected to Claude)

### Installation

1. **Install Python dependencies**
   ```bash
   pip install fastmcp
   ```

2. **Clone and setup**
   ```bash
   git clone https://github.com/xxGodLiuxx/Mneme-Personal-Memory-Lighthouse.git
   cd Mneme-Personal-Memory-Lighthouse
   ```

3. **Configure Claude Desktop**
   - Copy `installation/claude_desktop_config.json` content
   - Windows: Edit `%APPDATA%\Claude\claude_desktop_config.json`
   - macOS: Edit `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Linux: Edit `~/.config/Claude/claude_desktop_config.json`
   - Replace `[YOUR_USERNAME]` with your actual username
   - Update Python path if needed

4. **Place MCP server**
   ```bash
   # Create directory (adjust path for your OS)
   mkdir ~/Documents/Mneme
   
   # Copy MCP server (choose one)
   # Standard version:
   cp src/hybrid_memory_mcp.py ~/Documents/Mneme/
   
   # Or fixed version (recommended for latest features):
   cp src/hybrid_memory_mcp_fixed.py ~/Documents/Mneme/
   ```

5. **Restart Claude Desktop**
   - Exit from system tray
   - Restart Claude Desktop
   - Start a **new conversation**

6. **Verify installation**
   ```
   Type in Claude: "Execute get_memory_stats"
   ```

## 🎯 Basic Usage

### Morning Routine
```
"Generate today's inspiration"
```
Generates 5 search prompts for your Notion databases.

### Random Discovery
```
"Show me a random memory from the past"
```
Retrieves a random memory with bias toward older entries.

### Save Insights
```
"Save this content"
```
Saves current conversation content to local memory.

### Context Search
```
"Search for memories related to writing"
```
Finds memories related to specific topics.

## 🏗️ Architecture

**Hybrid Approach**: Leverages Claude's native Notion integration for seamless data access.

```
┌─────────────────┐     ┌─────────────────┐
│ Claude Desktop  │────▶│  MCP Server     │
│ (Notion Native) │     │ (Local Memory) │
└─────────────────┘     └─────────────────┘
         │                       │
         │                       ▼
         │              ┌─────────────────┐
         │              │ Local Storage   │
         │              │ (~/.mneme_memory)│
         │              └─────────────────┘
         │                       
         ▼                      
┌─────────────────┐            
│ Notion Workspace│            
│ (Your Personal) │            
└─────────────────┘            
```

**Key Advantage**: No need to manage Notion API keys - uses Claude's built-in Notion access.

## 📦 Available MCP Servers

### 1. **Hybrid Memory MCP** (`hybrid_memory_mcp.py`)
Full-featured server with Notion integration, serendipity engine, and daily summaries.

### 2. **Hybrid Memory MCP Fixed** (`hybrid_memory_mcp_fixed.py`)
Enhanced version with improved error handling and stability. Recommended for production use.

### 3. **Simple Memory MCP Fixed** (`simple_memory_mcp_fixed.py`)
Lightweight server for basic memory operations. Perfect for testing and minimal setups.

## 🔄 Multi-Device Sync

### Dropbox Sync (Recommended)
1. **Main PC**: Run `installation/setup_dropbox_sync.bat` as administrator
2. **Other PCs**: Wait for sync, then run same script
3. Each PC needs individual Claude Desktop configuration

### Manual Sync
- Data location: `~/.mneme_memory/`
- Sync folder: `Dropbox/Mneme_Memory_Sync/`

## 📚 Documentation

- **[Architecture Guide](docs/ARCHITECTURE.md)** - System design and technical overview
- **[Installation Guide](docs/INSTALLATION.md)** - Complete setup instructions
- **[User Manual](docs/USER_GUIDE.md)** - Detailed usage guide and best practices
- **[Multi-Device Setup](docs/SYNC_GUIDE.md)** - Cross-device synchronization
- **[Quick Start](docs/QUICK_START.md)** - 5-minute setup guide

## 🛡️ Security & Privacy

⚠️ **Important Security Notes:**

- **Personal Use Only**: This system is designed for individual use
- **API Keys**: Never commit your Notion API key to version control
- **Database IDs**: Replace all database IDs with your own
- **Local Storage**: Memory data is stored locally and optionally synced

### Setup Required
1. **Enable Notion in Claude Desktop**: Connect your Notion workspace through Claude's official integration
2. **No API Keys Needed**: Mneme leverages Claude's native Notion access  
3. **Update File Paths**: Modify paths in MCP server to match your system
4. **Database Access**: Ensure your Notion databases are accessible to Claude

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guidelines](CONTRIBUTING.md) before submitting PRs.

### Development Setup
```bash
git clone https://github.com/xxGodLiuxx/mneme.git
cd mneme
pip install -r requirements.txt
```

### Reporting Issues
- Use GitHub Issues for bug reports
- Include system information and error messages
- Check existing issues before creating new ones

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Original Inspiration**: [zhizhiarv](https://zenn.dev/zhizhiarv/articles/local-memory-mcp-for-claude-desktop) for the foundational concept of local memory MCP for Claude Desktop
- [Claude Desktop](https://claude.ai/desktop) for providing the MCP platform
- [FastMCP](https://github.com/jlowin/fastmcp) for the Python MCP framework
- [Notion](https://notion.so) for the knowledge management platform
- Greek mythology for inspiring the name "Mneme"

### Special Thanks

This project was inspired by the excellent work of **zhizhiarv** on local memory systems for Claude Desktop. Their [original article](https://zenn.dev/zhizhiarv/articles/local-memory-mcp-for-claude-desktop) provided the foundational concept that evolved into Mneme's hybrid memory approach. We extend our deepest gratitude for their pioneering work in the MCP ecosystem.

## 📊 Project Status

**Current Version**: v1.2.0 (Released: August 2025)

### What's New
- ✅ **Fixed Version MCP Servers**: Improved stability and error handling
- ✅ **Cross-platform Support**: Full support for Windows, macOS, and Linux
- ✅ **Enhanced Configuration**: Simplified setup with example configurations
- ✅ **Simple Memory Server**: Lightweight option for testing and basic usage

### Features
- ✅ Core MCP server implementation
- ✅ Basic memory operations (CRUD)
- ✅ Serendipity and inspiration features  
- ✅ Dropbox synchronization
- ✅ Multi-OS environment support
- ✅ Daily summary generation and Notion sync
- ✅ Session context preservation
- 🔄 Multi-language documentation (ongoing)
- 🔄 Advanced search algorithms (planned)
- 🔄 Mobile companion app (planned)

---

*Built with ❤️ for personal knowledge workers who believe that every memory contains the seeds of future creativity.*

**Start your journey**: `git clone` → `configure` → `discover`