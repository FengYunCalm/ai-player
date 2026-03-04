<div align="center">

# 🤖 AI-Player 智能游戏测试工具

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP-协议-green.svg)](https://modelcontextprotocol.io/)
[![Tests](https://github.com/FengYunCalm/ai-player/workflows/Tests/badge.svg)](https://github.com/FengYunCalm/ai-player/actions)
[![Downloads](https://img.shields.io/github/downloads/FengYunCalm/ai-player/total.svg)](https://github.com/FengYunCalm/ai-player/releases)

**基于 MCP 协议的 MUD 游戏自动化测试与智能修复工具**

[📖 中文文档](#快速开始) | [📖 English Docs](docs/README_EN.md) | [💡 使用示例](examples/) | [🚀 立即安装](#安装)

</div>

---

## ✨ 功能特性

- 🤖 **AI 驱动** - 基于 MCP 协议，与大模型无缝集成
- 🔌 **实时通信** - 通过 TCP 与 MUD 服务器实时交互
- 🐛 **Bug 检测** - 自动监控服务器日志，实时发现错误
- 🔧 **智能修复** - 自动修复常见 LPC 代码错误
- 🎮 **游戏测试** - 自动化游戏可玩性测试
- 📊 **知识库** - 维护测试历史与代码基线
- 🔄 **热更新** - 支持游戏运行时热更新（无需重启）
- 🌐 **双语支持** - 中文/English 完整文档

---

## 🚀 快速开始

### 📦 安装

```bash
# 方式一：通过 pip 安装
pip install ai-player-mud

# 方式二：从源码安装
git clone https://github.com/FengYunCalm/ai-player.git
cd ai-player
pip install -r requirements.txt
```

### ⚙️ 配置

```bash
# 复制配置文件
cp config/config.example.yaml config/config.yaml

# 编辑配置
vim config/config.yaml
```

**基本配置示例：**

```yaml
server:
  host: "localhost" # 服务器地址
  port: 3939 # 服务器端口
  encoding: "utf-8" # 字符编码

login:
  separator: "|" # 账号密码分隔符
  default_gender: "男" # 默认性别

test:
  default_account: "test" # 测试账号
  default_password: "test123" # 测试密码
```

### 🎮 运行

```bash
# 方式一：作为 MCP 服务器运行
python -m ai_player.mcp_server

# 方式二：运行示例
python examples/basic_connection.py
```

---

## 📖 使用指南

### 1️⃣ 连接游戏服务器

```python
from ai_player.core.connection import GameConnection

# 创建连接
conn = GameConnection()

# 连接服务器
conn.connect(host="localhost", port=3939)

# 登录游戏（支持自动注册）
conn.login(account="test", password="test123")
```

### 2️⃣ 发送游戏命令

```python
# 发送命令
conn.send("look")

# 获取响应消息
messages = conn.get_messages(timeout=1.0)
for msg in messages:
    print(msg["text"])
```

### 3️⃣ Bug 检测与报告

```python
# 获取自动检测到的 Bug
bugs = conn.get_recent_bugs(count=5)

for bug in bugs:
    print(f"类型: {bug['type']}")
    print(f"严重级别: {bug['severity']}")
    print(f"消息: {bug['message']}")
    if bug['source_file']:
        print(f"位置: {bug['source_file']}:{bug['line_number']}")
```

---

## 🛠️ MCP 工具列表

| 工具名              | 描述                     | 参数                  |
| ------------------- | ------------------------ | --------------------- |
| `connect_server`    | 连接 MUD 游戏服务器      | `host`, `port`        |
| `login_game`        | 登录游戏（支持自动注册） | `account`, `password` |
| `send_game_command` | 发送游戏命令             | `command`             |
| `get_game_status`   | 获取游戏状态             | -                     |
| `disconnect_server` | 断开连接                 | -                     |
| `get_bug_report`    | 获取 Bug 检测报告        | `count`               |

---

## 🐛 支持的 Bug 修复类型

### ✅ 自动修复（无需确认）

| 类型           | 描述                  | 示例                   |
| -------------- | --------------------- | ---------------------- |
| **空指针检查** | 添加 `objectp()` 验证 | `if (objectp(target))` |
| **未定义变量** | 声明缺失变量          | `var_type xxx;`        |
| **缺失返回值** | 添加 `return` 语句    | `return 0;`            |
| **拼写错误**   | 修正字符串拼写        | `qury` → `query`       |

### ⚠️ 需要确认

- 架构变更
- 多文件修改
- 游戏平衡调整

---

## 🧪 测试场景

- **新手村可玩性测试** - 验证基础游戏功能
- **战斗系统测试** - 测试战斗机制
- **物品系统测试** - 测试物品交互
- **通信系统测试** - 测试聊天功能
- **压力测试** - 服务器稳定性测试

---

## 📂 项目结构

```
ai-player/
├── ai_player/              # 主包
│   ├── mcp_server.py       # MCP 服务器（核心代码）
│   ├── utils/              # 工具模块
│   │   └── config_loader.py
│   └── knowledge/          # 知识库
├── config/                 # 配置文件
│   ├── config.yaml
│   └── config.example.yaml
├── examples/               # 使用示例
│   ├── basic_connection.py
│   ├── automated_test.py
│   └── bug_detection.py
├── tests/                  # 测试用例
├── docs/                   # 文档
│   ├── README_EN.md        # 英文文档
│   └── configuration.md
├── .github/                # GitHub 配置
│   ├── workflows/          # CI/CD
│   └── ISSUE_TEMPLATE/     # Issue 模板
├── requirements.txt        # 依赖
├── setup.py               # 安装脚本
└── README.md              # 本文件
```

---

## 🤝 贡献指南

我们欢迎所有形式的贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

### 快速开始贡献

```bash
# 1. Fork 本仓库
# 2. 克隆你的 Fork
git clone https://github.com/YOUR_USERNAME/ai-player.git

# 3. 创建分支
git checkout -b feature/amazing-feature

# 4. 提交更改
git commit -m "feat: 添加 amazing 功能"

# 5. 推送分支
git push origin feature/amazing-feature

# 6. 创建 Pull Request
```

---

## 📝 开发计划

查看 [ROADMAP.md](ROADMAP.md) 了解项目的未来计划。

### 版本规划

| 版本   | 时间    | 主要特性                   |
| ------ | ------- | -------------------------- |
| v1.1.0 | 2026-Q2 | 连接池管理、WebSocket 支持 |
| v1.2.0 | 2026-Q3 | 测试场景 DSL、可视化编辑器 |
| v1.3.0 | 2026-Q4 | 智能修复引擎增强           |
| v2.0.0 | 2027    | 企业级功能、Web 管理界面   |

---

## 📜 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

```
MIT License

Copyright (c) 2026 AI-Player Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files...
```

---

## 🙏 致谢

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP 协议
- [FluffOS](https://github.com/fluffos/fluffos) - LPC 驱动
- 所有贡献者和用户！

---

## 📮 联系我们

- 📧 邮箱: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues)
- 💬 讨论: [GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！**

[🔝 回到顶部](#-ai-player-智能游戏测试工具)

</div>
