<div align="center">

# 🤖 AI-Player - Intelligent Game Testing Tool

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-MIT-yellow.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green.svg)](https://modelcontextprotocol.io/)
[![Tests](https://github.com/FengYunCalm/ai-player/workflows/Tests/badge.svg)](https://github.com/FengYunCalm/ai-player/actions)
[![Downloads](https://img.shields.io/github/downloads/FengYunCalm/ai-player/total.svg)](https://github.com/FengYunCalm/ai-player/releases)

**MUD Game Automation and Testing Tool Based on MCP Protocol**

[📖 中文文档](../README.md) | [📖 English Docs](#quick-start) | [💡 Examples](../examples/) | [🚀 Install](#installation)

</div>

---

## ✨ Features

- 🤖 **AI Powered** - MCP protocol integration for seamless LLM compatibility
- 🔌 **Real-time Communication** - TCP interaction with MUD servers
- 🐛 **Bug Detection** - Automatic log monitoring and error detection
- 🔧 **Smart Fixes** - Automatic repair of common LPC code errors
- 🎮 **Game Testing** - Automated playability testing
- 📊 **Knowledge Base** - Test history and code baseline tracking
- 🔄 **Hot Reload** - Runtime updates without server restart
- 🌐 **Bilingual Support** - Complete Chinese/English documentation

---

## 🚀 Quick Start

### 📦 Installation

```bash
# Method 1: Install via pip
pip install ai-player-mud

# Method 2: Install from source
git clone https://github.com/FengYunCalm/ai-player.git
cd ai-player
pip install -r requirements.txt
```

### ⚙️ Configuration

```bash
# Copy configuration file
cp config/config.example.yaml config/config.yaml

# Edit configuration
vim config/config.yaml
```

**Basic Configuration Example:**

```yaml
server:
  host: "localhost"      # Server address
  port: 3939            # Server port
  encoding: "utf-8"     # Character encoding

login:
  separator: "|"        # Account/password separator
  default_gender: "Male"  # Default gender

test:
  default_account: "test"      # Test account
  default_password: "test123"  # Test password
```

### 🎮 Run

```bash
# Method 1: Run as MCP server
python -m ai_player.mcp_server

# Method 2: Run examples
python examples/basic_connection.py
```

---

## 📖 Usage Guide

### 1️⃣ Connect to Game Server

```python
from ai_player.core.connection import GameConnection

# Create connection
conn = GameConnection()

# Connect to server
conn.connect(host="localhost", port=3939)

# Login (supports auto-registration)
conn.login(account="test", password="test123")
```

### 2️⃣ Send Game Commands

```python
# Send command
conn.send("look")

# Get response messages
messages = conn.get_messages(timeout=1.0)
for msg in messages:
    print(msg["text"])
```

### 3️⃣ Bug Detection and Reporting

```python
# Get auto-detected bugs
bugs = conn.get_recent_bugs(count=5)

for bug in bugs:
    print(f"Type: {bug['type']}")
    print(f"Severity: {bug['severity']}")
    print(f"Message: {bug['message']}")
    if bug['source_file']:
        print(f"Location: {bug['source_file']}:{bug['line_number']}")
```

---

## 🛠️ MCP Tools List

| Tool Name | Description | Parameters |
|-----------|-------------|------------|
| `connect_server` | Connect to MUD game server | `host`, `port` |
| `login_game` | Login (supports auto-registration) | `account`, `password` |
| `send_game_command` | Send game command | `command` |
| `get_game_status` | Get game status | - |
| `disconnect_server` | Disconnect | - |
| `get_bug_report` | Get bug detection report | `count` |

---

## 🐛 Supported Bug Fix Types

### ✅ Auto-Fix (No Confirmation Needed)

| Type | Description | Example |
|------|-------------|---------|
| **Null Check** | Add `objectp()` validation | `if (objectp(target))` |
| **Undefined Variable** | Declare missing variable | `var_type xxx;` |
| **Missing Return** | Add `return` statement | `return 0;` |
| **Typo Fix** | Fix string typos | `qury` → `query` |

### ⚠️ Requires Confirmation

- Architecture changes
- Multi-file modifications
- Game balance adjustments

---

## 🧪 Test Scenarios

- **Newbie Village Playability** - Verify basic game functionality
- **Combat System Test** - Test combat mechanics
- **Item System Test** - Test item interactions
- **Communication Test** - Test chat functionality
- **Stress Test** - Server stability testing

---

## 📂 Project Structure

```
ai-player/
├── ai_player/              # Main package
│   ├── mcp_server.py       # MCP server (core code)
│   ├── utils/              # Utilities
│   │   └── config_loader.py
│   └── knowledge/          # Knowledge base
├── config/                 # Configuration files
│   ├── config.yaml
│   └── config.example.yaml
├── examples/               # Usage examples
│   ├── basic_connection.py
│   ├── automated_test.py
│   └── bug_detection.py
├── tests/                  # Test cases
├── docs/                   # Documentation
│   ├── README_EN.md        # English docs
│   └── configuration.md
├── .github/                # GitHub configuration
│   ├── workflows/          # CI/CD
│   └── ISSUE_TEMPLATE/     # Issue templates
├── requirements.txt        # Dependencies
├── setup.py               # Installation script
└── README.md              # Main document (Chinese)
```

---

## 🤝 Contributing

We welcome all forms of contributions! See [CONTRIBUTING.md](../CONTRIBUTING.md) for details.

### Quick Start for Contributing

```bash
# 1. Fork this repository
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/ai-player.git

# 3. Create branch
git checkout -b feature/amazing-feature

# 4. Commit changes
git commit -m "feat: add amazing feature"

# 5. Push branch
git push origin feature/amazing-feature

# 6. Create Pull Request
```

---

## 📝 Development Roadmap

See [ROADMAP.md](../ROADMAP.md) for future plans.

### Version Planning

| Version | Timeline | Major Features |
|---------|----------|----------------|
| v1.1.0 | 2026-Q2 | Connection pool, WebSocket support |
| v1.2.0 | 2026-Q3 | Test scenario DSL, visual editor |
| v1.3.0 | 2026-Q4 | Enhanced smart fix engine |
| v2.0.0 | 2027 | Enterprise features, web management |

---

## 📜 License

This project is open source under the [GPL v3 License](../LICENSE).

```
MIT License

Copyright (c) 2026 AI-Player Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🙏 Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP Protocol
- [FluffOS](https://github.com/fluffos/fluffos) - LPC Driver
- All contributors and users!

---

## 📮 Contact Us

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

---

<div align="center">

**⭐ If this project helps you, please give us a Star!**

[🔝 Back to Top](#-ai-player---intelligent-game-testing-tool)

</div>
