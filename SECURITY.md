# Security Policy

## 🛡️ Security Overview

Mneme is designed as a **personal-use system** with the following security considerations:

### Data Privacy
- **Local-First**: All personal memories are stored locally (`~/.jah_thoughttrace/`)
- **Optional Sync**: Cloud synchronization via Dropbox is optional and user-controlled
- **No Telemetry**: No usage data is collected or transmitted

### API Security
- **Your Own Keys**: You must provide your own Notion API key
- **Environment Variables**: API keys should be stored in environment variables, not in code
- **No Default Credentials**: The system includes no default API keys or credentials

## 🔒 Security Best Practices

### Before Use
1. **Review Code**: Inspect all code before running, especially MCP servers
2. **Set Strong API Keys**: Use secure, unique API keys for Notion integration
3. **Limit Notion Access**: Grant minimal necessary permissions to Notion integrations
4. **Backup Regularly**: Keep backups of your memory data

### During Use
1. **Private Repositories**: Keep your configured version in a private repository
2. **Secure Sync**: If using Dropbox sync, ensure your Dropbox account is secure
3. **Regular Updates**: Keep dependencies updated for security patches

### Configuration Security
```bash
# ✅ GOOD: Use environment variables
export NOTION_API_KEY="secret_xxxxxxxxxxxx"

# ❌ BAD: Hardcode in files
notion_api_key = "secret_xxxxxxxxxxxx"  # Never do this!
```

## 🚨 Reporting Security Issues

If you discover a security vulnerability in Mneme:

1. **DO NOT** create a public GitHub issue
2. **Email**: Send details to [your-email@example.com]
3. **Include**: 
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if any)

### Response Timeline
- **24 hours**: Acknowledgment of your report
- **72 hours**: Initial assessment
- **1 week**: Resolution or mitigation plan

## 🔍 Security Checklist

Before deploying Mneme:

- [ ] Reviewed all source code
- [ ] Set up environment variables for API keys
- [ ] Configured Notion API with minimal permissions
- [ ] Enabled 2FA on Notion and sync service accounts
- [ ] Tested with sample data before using real personal data
- [ ] Set up regular backups of memory data
- [ ] Configured secure sync service (if using)

## ⚠️ Known Limitations

### Windows Security
- MCP servers run with user privileges
- File system permissions depend on Windows user configuration
- Dropbox sync relies on Dropbox desktop client security

### Claude Desktop Integration
- MCP communication happens over local channels
- Claude Desktop handles external API communication
- Your Claude conversations may be subject to Anthropic's terms

### Third-Party Dependencies
- FastMCP: Python MCP framework
- Notion Client: Official Notion API client
- Other dependencies listed in requirements.txt

## 🛠️ Secure Development

### For Contributors
1. **Code Review**: All changes require review
2. **No Secrets**: Never commit API keys, tokens, or personal data
3. **Dependency Audit**: Use `pip-audit` to check for vulnerable packages
4. **Input Validation**: Sanitize all user inputs
5. **Error Handling**: Avoid exposing sensitive information in error messages

### Testing Security
```bash
# Check for secrets in code
git secrets --scan

# Audit dependencies
pip-audit

# Static analysis
bandit -r src/
```

## 📋 Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | ✅ Yes    |
| < 1.0   | ❌ No     |

## 🔄 Security Updates

Security updates will be:
- **Prioritized**: Released as soon as possible
- **Documented**: With clear upgrade instructions
- **Backwards Compatible**: When possible

## 📚 Additional Resources

- [Notion API Security](https://developers.notion.com/docs/authorization)
- [MCP Security Guidelines](https://modelcontextprotocol.io/docs/security)
- [Python Security Best Practices](https://python.org/dev/security/)
- [FastMCP Documentation](https://github.com/jlowin/fastmcp)

---

**Remember**: Mneme handles your personal memories and thoughts. Treat it with the same security consideration as your personal diary or private documents.