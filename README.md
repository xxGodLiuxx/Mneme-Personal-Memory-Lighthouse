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
- Windows 10/11
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
   git clone https://github.com/YOUR_USERNAME/mneme.git
   cd mneme
   ```

3. **Configure Claude Desktop**
   - Copy `installation/claude_desktop_config.json` content
   - Edit `%APPDATA%\Claude\claude_desktop_config.json`
   - Replace `[YOUR_USERNAME]` with your actual username
   - Update Python path if needed

4. **Place MCP server**
   ```bash
   # Create directory
   mkdir C:\Users\USERNAME\Documents\Mneme
   
   # Copy MCP server
   copy src\hybrid_memory_mcp.py C:\Users\USERNAME\Documents\Mneme\
   ```

5. **Restart Claude Desktop**
   - Exit from system tray
   - Restart Claude Desktop
   - Start a **new conversation**

6. **Verify installation**
   ```
   Type in Claude: "get_memory_stats を実行して"
   ```

## 🎯 Basic Usage

### Morning Routine
```
"今日のインスピレーションを生成して"
```
Generates 5 search prompts for your Notion databases.

### Random Discovery
```
"過去の記憶をランダムに見せて"
```
Retrieves a random memory with bias toward older entries.

### Save Insights
```
"この内容を保存して"
```
Saves current conversation content to local memory.

### Context Search
```
"執筆に関連する記憶を検索"
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
         │              │ (~/.jah_thought)│
         │              └─────────────────┘
         │                       
         ▼                      
┌─────────────────┐            
│ Notion Workspace│            
│ (Your Personal) │            
└─────────────────┘            
```

**Key Advantage**: No need to manage Notion API keys - uses Claude's built-in Notion access.

## 🔄 Multi-Device Sync

### Dropbox Sync (Recommended)
1. **Main PC**: Run `installation/setup_dropbox_sync.bat` as administrator
2. **Other PCs**: Wait for sync, then run same script
3. Each PC needs individual Claude Desktop configuration

### Manual Sync
- Data location: `~/.jah_thoughttrace/`
- Sync folder: `Dropbox/Mneme_Memory_Sync/`

## 📚 Documentation

- **[Initial Concept](docs/01_初期構想書.md)** - Vision and background (Japanese)
- **[User Guide](docs/02_使用ガイド.md)** - Detailed usage guide (Japanese)  
- **[Setup Guide](docs/03_セットアップガイド.md)** - Complete setup instructions (Japanese)
- **[Sync Manual](docs/04_同期マニュアル.md)** - Multi-device configuration (Japanese)
- **[Quick Start](docs/QUICK_START.md)** - 5-minute setup (Japanese)

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
git clone https://github.com/YOUR_USERNAME/mneme.git
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

- [Claude Desktop](https://claude.ai/desktop) for providing the MCP platform
- [FastMCP](https://github.com/jlowin/fastmcp) for the Python MCP framework
- [Notion](https://notion.so) for the knowledge management platform
- Greek mythology for inspiring the name "Mneme"

## 📊 Project Status

- ✅ Core MCP server implementation
- ✅ Basic memory operations (CRUD)
- ✅ Serendipity and inspiration features  
- ✅ Dropbox synchronization
- ✅ Windows environment support
- 🔄 Multi-language documentation (ongoing)
- 🔄 Advanced search algorithms (planned)
- 🔄 Mobile companion app (planned)

---

*Built with ❤️ for personal knowledge workers who believe that every memory contains the seeds of future creativity.*

**Start your journey**: `git clone` → `configure` → `discover`