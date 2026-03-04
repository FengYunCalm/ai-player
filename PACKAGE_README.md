# AI-Player Open Source Package

## Package Contents

This is the open-source version of AI-Player, an MCP-based MUD game automation and testing tool.

## Quick Start

1. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

2. **Configure**:

   ```bash
   cp config/config.example.yaml config/config.yaml
   # Edit config.yaml with your settings
   ```

3. **Run example**:

   ```bash
   python examples/basic_connection.py
   ```

4. **Run as MCP server**:
   ```bash
   python -m ai_player.mcp_server
   ```

## Project Structure

```
ai-player-open-source/
├── ai_player/              # Main package
│   ├── mcp_server.py       # MCP server implementation
│   ├── utils/              # Utilities
│   │   └── config_loader.py
│   ├── core/               # Core modules (for future)
│   └── knowledge/          # Knowledge base
├── config/                 # Configuration files
│   ├── config.yaml
│   └── config.example.yaml
├── examples/               # Usage examples
├── tests/                  # Test suite
├── docs/                   # Documentation
├── .github/                # GitHub Actions
├── requirements.txt        # Dependencies
├── setup.py               # Package setup
└── README.md              # Main documentation
```

## Documentation

- [README.md](README.md) - Main documentation
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [CHANGELOG.md](CHANGELOG.md) - Version history
- [ROADMAP.md](ROADMAP.md) - Future plans
- [SECURITY.md](SECURITY.md) - Security policy
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community guidelines

## License

MIT License - See [LICENSE](LICENSE)

## Support

- GitHub Issues: https://github.com/yourusername/ai-player/issues
- GitHub Discussions: https://github.com/yourusername/ai-player/discussions

---

**Packaged**: 2026-03-04
**Version**: 1.0.0
