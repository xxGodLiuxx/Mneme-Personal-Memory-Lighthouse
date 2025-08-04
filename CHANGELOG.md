# Changelog

All notable changes to the Mneme - Personal Memory Lighthouse project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - 2025-08-04

### Added
- **New MCP Servers**: Added `hybrid_memory_mcp_fixed.py` and `simple_memory_mcp_fixed.py` with improved error handling
- **Cross-platform Support**: Full support for Windows, macOS, and Linux environments
- **Configuration Example**: Added `installation/claude_desktop_config.json` for easier setup
- **Enhanced Documentation**: Updated README with clearer installation instructions
- **Simple Memory Server**: Lightweight option for testing and basic memory operations

### Changed
- **README Updates**: Improved installation guide with OS-specific paths
- **Project Structure**: Better organization of MCP server files
- **Error Handling**: Enhanced error recovery in fixed versions

### Fixed
- **Path Issues**: Resolved Windows-specific path problems
- **Encoding Issues**: Fixed UTF-8 encoding for international users
- **Configuration**: Clarified Claude Desktop configuration steps
- **Timezone Handling**: All timestamps now use UTC for global compatibility

## [1.1.0] - 2025-08-02

### Added
- **Daily Summary Generation**: Automatic daily activity summaries
- **Notion Sync**: Direct synchronization with Notion databases
- **Session Context**: Preserve context across Claude sessions
- **Dropbox Sync**: Multi-device synchronization support

### Changed
- **Memory Storage**: Improved local storage structure
- **Search Algorithm**: Enhanced context-based search

### Fixed
- **Memory Persistence**: Fixed issues with memory loss on restart
- **Timezone Handling**: Proper JST timezone support

## [1.0.0] - 2025-07-28

### Added
- **Initial Release**: Core MCP server implementation
- **Serendipity Engine**: Random memory retrieval with aging bias
- **Daily Inspiration**: Automated prompt generation for Notion searches
- **Hybrid Memory System**: Local storage with cloud synchronization
- **Conversation Preservation**: Automatic Claude conversation summarization
- **Basic CRUD Operations**: Create, Read, Update, Delete memories
- **Topic Indexing**: Automatic topic extraction and indexing

### Features
- Integration with Claude Desktop's native Notion support
- Local memory storage in `~/.mneme_memory`
- JSON-based data persistence
- Windows 10/11 support
- Python 3.10+ compatibility

---

## Roadmap

### Planned Features
- [ ] Advanced search algorithms with semantic similarity
- [ ] Mobile companion app for on-the-go access
- [ ] Multi-language support (Japanese, Chinese, French)
- [ ] Voice note integration
- [ ] Memory visualization dashboard
- [ ] Automated backup to multiple cloud services
- [ ] Plugin system for custom memory processors

### Under Consideration
- Memory encryption for sensitive data
- Collaborative memory sharing
- AI-powered memory consolidation
- Integration with other note-taking apps (Obsidian, Roam)

---

*For detailed release notes and migration guides, please refer to the [Releases](https://github.com/xxGodLiuxx/Mneme-Personal-Memory-Lighthouse/releases) page.*