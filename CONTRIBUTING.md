# Contributing to Mneme

Thank you for your interest in contributing to Mneme! 🎉

## 🌟 Getting Started

### Code of Conduct
- Be respectful and inclusive
- Focus on constructive feedback
- Help maintain a welcoming environment for all contributors

### Development Philosophy
- **Personal-First**: Remember this is a personal knowledge management tool
- **Privacy-Focused**: Always consider data privacy implications  
- **Windows-Friendly**: Ensure compatibility with Windows environments
- **Documentation**: Write clear, bilingual documentation when possible

## 🛠️ Development Setup

### Prerequisites
- Python 3.10+
- Git
- Claude Desktop (for testing)
- Notion account (for integration testing)

### Setup Steps
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/mneme.git
cd mneme

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Set up pre-commit hooks
pre-commit install
```

### Testing Setup
```bash
# Copy example config
cp .env.example .env

# Edit .env with your test credentials
# NOTION_API_KEY=your_test_key_here

# Run tests
pytest tests/
```

## 📝 Types of Contributions

### 🐛 Bug Reports
Before creating an issue:
- Check existing issues for duplicates
- Test with the latest version
- Provide minimal reproduction steps

**Bug Report Template:**
```markdown
**Environment:**
- OS: Windows 11
- Python: 3.10.2
- Claude Desktop: x.x.x

**Description:**
Clear description of the bug

**Steps to Reproduce:**
1. Step one
2. Step two
3. ...

**Expected Behavior:**
What should happen

**Actual Behavior:**
What actually happens

**Additional Context:**
Screenshots, logs, etc.
```

### ✨ Feature Requests
We welcome feature ideas! Please:
- Check existing issues and discussions
- Describe the use case clearly
- Consider privacy implications
- Think about Windows compatibility

### 🔧 Code Contributions

#### Before You Start
- Open an issue to discuss major changes
- Check the project roadmap
- Ensure your idea aligns with project goals

#### Coding Standards
```python
# Use type hints
def save_memory(content: str, tags: List[str]) -> Dict[str, Any]:
    pass

# Clear variable names  
user_memories = load_memories()  # Good
data = load_data()  # Less clear

# Error handling
try:
    result = api_call()
except NotionAPIError as e:
    logger.error(f"Notion API failed: {e}")
    return fallback_response()
```

#### Pull Request Process
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

#### Pull Request Template
```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix (non-breaking change)
- [ ] New feature (non-breaking change)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update

## Testing
- [ ] Tested locally
- [ ] Added/updated tests
- [ ] All tests pass

## Security Considerations
- [ ] No personal data exposed
- [ ] No hardcoded credentials
- [ ] Input validation added where needed

## Documentation
- [ ] Updated README if needed
- [ ] Added/updated code comments
- [ ] Updated relevant documentation
```

## 🧪 Testing Guidelines

### Test Categories
```bash
# Unit tests
pytest tests/unit/

# Integration tests (requires Notion API)
pytest tests/integration/

# Windows-specific tests
pytest tests/windows/
```

### Writing Tests
```python
def test_memory_creation():
    """Test basic memory creation functionality."""
    memory = create_memory("Test content", ["tag1", "tag2"])
    
    assert memory["content"] == "Test content"
    assert "tag1" in memory["tags"]
    assert memory["timestamp"] is not None
```

### Test Data
- Use fake/sample data only
- Never commit real personal information
- Mock external API calls when possible

## 📚 Documentation

### Languages
- **English**: Primary language for code and main documentation
- **Japanese**: Secondary language for user guides (community maintained)

### Documentation Types
- **README**: Project overview and quick start
- **Code Comments**: Inline documentation
- **User Guides**: Step-by-step instructions
- **API Docs**: Function and class documentation

### Writing Style
- Clear and concise
- Include examples
- Consider non-native speakers
- Use consistent terminology

## 🚀 Release Process

### Versioning
We use [Semantic Versioning](https://semver.org/):
- **MAJOR**: Breaking changes
- **MINOR**: New features (backwards compatible)
- **PATCH**: Bug fixes

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] Security review completed
- [ ] Version number updated
- [ ] Changelog updated
- [ ] Git tag created

## 🔒 Security Guidelines

### Security-First Development
- Never commit API keys or secrets
- Validate all user inputs
- Use environment variables for configuration
- Follow least-privilege principles

### Security Review
All security-related changes require:
- Extra careful code review
- Testing with limited permissions
- Documentation of security implications

## 🤝 Community

### Communication Channels
- **Issues**: Bug reports and feature requests
- **Discussions**: General questions and ideas
- **Pull Requests**: Code contributions

### Getting Help
- Check existing documentation
- Search closed issues
- Ask in GitHub Discussions
- Be patient and respectful

## 🎯 Project Roadmap

### Current Priorities
1. **Stability**: Bug fixes and reliability improvements
2. **Documentation**: Better user guides and examples
3. **Testing**: Comprehensive test coverage
4. **Security**: Enhanced security features

### Future Ideas
- Mobile companion app
- Advanced search algorithms
- Plugin system
- Multi-language support

## 🙏 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes (for significant contributions)
- Given credit in relevant documentation

### Hall of Fame
- **Creator**: xxGodLiuxx - Original concept and implementation
- **Contributors**: [Your name could be here!]

---

**Thank you for helping make Mneme better for everyone!** 🚀

*Remember: Every contribution, no matter how small, helps build a better tool for personal knowledge management.*