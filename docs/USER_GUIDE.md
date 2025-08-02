# Mneme - Personal Memory Lighthouse User Guide

## Table of Contents
1. [Getting Started](#getting-started)
2. [Basic Usage](#basic-usage)
3. [Daily Workflow](#daily-workflow)
4. [Advanced Features](#advanced-features)
5. [Troubleshooting](#troubleshooting)
6. [Best Practices](#best-practices)

---

## Getting Started

Mneme is a bridge connecting your past memories with present thinking. This guide explains how to maximize the system's potential.

### System Features
- 🧠 **Persistent Memory**: Data retained across sessions
- 🎲 **Serendipity**: Promotes accidental discoveries
- 🔄 **Auto Sync**: Data sharing across multiple devices
- 🤖 **AI Integration**: Seamless Claude Desktop connectivity

## Basic Usage

### 1. First Launch

In a new Claude Desktop session:

```
"Check available MCP tools"
```

The following tools should appear when ready:
- `get_daily_inspiration_prompt`
- `save_from_notion`
- `get_random_memory`
- `search_by_context`
- `link_claude_conversation`
- `get_memory_stats`

### 2. Basic Commands

#### Get Inspiration
```
"Generate today's inspiration"
```

#### Random Memory
```
"Show me a random memory from the past"
```

#### Save Memory
```
"Save this content to memory"
```

#### Search
```
"Search for memories related to [keyword]"
```

#### Statistics
```
"Show memory system statistics"
```

## Daily Workflow

### 🌅 Morning Routine (5 minutes)

1. **Generate Inspiration**
   ```
   You: Generate today's inspiration prompts
   ```

2. **Notion Search**
   Use generated prompts to search Notion:
   ```
   You: Search my Notion databases for [generated prompt]
   ```

3. **Save Insights**
   ```
   You: Save this inspiration to memory
   ```

### 🌆 Evening Reflection (10 minutes)

1. **Session Review**
   ```
   You: Summarize today's key insights
   ```

2. **Memory Integration**
   ```
   You: Save today's session summary
   ```

3. **Random Discovery**
   ```
   You: Show me a random old memory for reflection
   ```

## Advanced Features

### Memory Search Strategies

#### Context-Based Search
```
"Find memories related to creative writing"
"Search for problem-solving experiences"
"Look for memories about productivity techniques"
```

#### Time-Based Discovery
```
"Show me memories from exactly one year ago"
"Find old ideas that were never implemented"
"What was I learning 6 months ago?"
```

### Cross-Session Continuity

#### Link Conversations
```
"Link this conversation to my memory system"
"Connect today's insights with past discussions"
```

#### Memory Threading
```
"Find related memories from previous sessions"
"Show the evolution of this idea over time"
```

## Troubleshooting

### Common Issues

#### MCP Tools Not Available
**Problem**: Commands not recognized
**Solution**: 
1. Restart Claude Desktop
2. Check `claude_desktop_config.json`
3. Verify Python path in configuration

#### Memory Not Saving
**Problem**: Data not persisting
**Solution**:
1. Check directory permissions
2. Verify `.mneme_memory` folder exists
3. Test with simple save command

#### Sync Issues
**Problem**: Data not syncing across devices
**Solution**:
1. Check Dropbox connection
2. Verify sync folder permissions
3. Manual folder comparison

### Error Messages

#### "Memory file not found"
- Run setup script again
- Check file paths in configuration

#### "Notion integration failed"
- Verify Claude's Notion connection
- Check database permissions

## Best Practices

### Daily Habits

1. **Consistent Morning Check-in**: Start each day with inspiration generation
2. **End-of-Session Summaries**: Always save key insights before closing
3. **Weekly Memory Reviews**: Browse random memories to spark connections

### Memory Organization

#### Effective Saving
- **Descriptive Context**: Include enough detail for future understanding
- **Tag Important Insights**: Use consistent keywords
- **Cross-Reference**: Link to related memories when saving

#### Search Optimization
- **Use Varied Vocabulary**: Try different search terms
- **Time-Based Queries**: Explore different time periods
- **Thematic Exploration**: Focus on specific topics or projects

### Data Hygiene

1. **Regular Backups**: Weekly backup of memory data
2. **Privacy Checks**: Avoid saving sensitive personal information
3. **Quality Control**: Review and clean low-value memories periodically

### Maximizing Serendipity

#### Creating Connections
- Ask open-ended questions about past memories
- Look for patterns across different time periods
- Use random memories as creative prompts

#### Building on Discoveries
- Follow up on interesting connections
- Document new insights that emerge
- Create action items from old ideas

---

## Advanced Usage Tips

### Creative Applications
- Use old memories as writing prompts
- Find patterns in your thinking evolution
- Discover forgotten project ideas worth revisiting

### Productivity Enhancement
- Learn from past problem-solving approaches
- Identify recurring themes in your work
- Build on previous successful strategies

### Personal Growth
- Track your learning journey over time
- Recognize personal development patterns
- Celebrate progress and insights

---

*Remember: Mneme works best when used consistently. The more you feed it quality memories, the more valuable discoveries it can offer in return.*