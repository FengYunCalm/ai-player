<div align="center">

<img src="https://img.shields.io/badge/AI--Player-智能游戏测试工具-blue?style=for-the-badge&logo=python&logoColor=white" alt="AI-Player">

<p>
  <a href="https://www.python.org/downloads/">
    <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?style=flat-square&logo=python" alt="Python 3.8+">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License: MIT">
  </a>
  <a href="https://modelcontextprotocol.io/">
    <img src="https://img.shields.io/badge/MCP-协议-green.svg?style=flat-square" alt="MCP Protocol">
  </a>
  <a href="https://github.com/FengYunCalm/ai-player/actions">
    <img src="https://img.shields.io/github/workflow/status/FengYunCalm/ai-player/Tests?style=flat-square&logo=github" alt="Tests">
  </a>
</p>

<p>
  <a href="https://github.com/FengYunCalm/ai-player/releases">
    <img src="https://img.shields.io/github/v/release/FengYunCalm/ai-player?style=flat-square&logo=github" alt="Latest Release">
  </a>
  <a href="https://github.com/FengYunCalm/ai-player/releases">
    <img src="https://img.shields.io/github/downloads/FengYunCalm/ai-player/total.svg?style=flat-square" alt="Downloads">
  </a>
  <a href="https://github.com/FengYunCalm/ai-player/stargazers">
    <img src="https://img.shields.io/github/stars/FengYunCalm/ai-player?style=flat-square&logo=github" alt="Stars">
  </a>
</p>

<h3>🤖 基于 MCP 协议的 MUD 游戏自动化测试与智能修复工具</h3>

<p>
  <strong>中文</strong> | 
  <a href="docs/README_EN.md"><strong>English</strong></a>
</p>

<p>
  <a href="#快速开始"><strong>🚀 快速开始</strong></a> •
  <a href="#功能特性"><strong>✨ 功能特性</strong></a> •
  <a href="#使用文档"><strong>📖 使用文档</strong></a> •
  <a href="#示例"><strong>💡 示例</strong></a> •
  <a href="#贡献"><strong>🤝 贡献</strong></a>
</p>

</div>

---

## 📋 目录

- [项目简介](#项目简介)
- [功能特性](#功能特性)
- [快速开始](#快速开始)
- [使用文档](#使用文档)
- [项目结构](#项目结构)
- [贡献指南](#贡献指南)
- [更新日志](#更新日志)
- [许可证](#许可证)

---

## 项目简介

**AI-Player** 是一个专为 MUD（多用户地下城）游戏设计的智能自动化测试工具。它基于 **MCP（Model Context Protocol）协议**，能够与大型语言模型无缝集成，实现游戏功能的自动化测试、Bug 检测和智能修复。

### 什么是 MUD 游戏？

MUD（Multi-User Dungeon）是一种文字类多人在线角色扮演游戏，玩家通过命令行与游戏世界交互。MUD 游戏通常使用 LPC（Lars Pensj C）语言开发，运行在 MUD 驱动（如 FluffOS）上。

### 为什么选择 AI-Player？

- 🎯 **专为 MUD 设计** - 深度理解 MUD 游戏特性和 LPC 代码
- 🚀 **AI 驱动测试** - 利用大模型智能分析游戏逻辑
- 🔧 **自动修复** - 检测并修复常见代码错误
- 📊 **完整报告** - 生成详细的测试报告和 Bug 分析
- 🌐 **开源免费** - MIT 许可证，可自由使用和修改

---

## 功能特性

### ✨ 核心功能

| 功能         | 描述                             | 状态      |
| ------------ | -------------------------------- | --------- |
| **AI 驱动**  | 基于 MCP 协议，与大模型无缝集成  | ✅ 已实现 |
| **实时通信** | 通过 TCP 与 MUD 服务器实时交互   | ✅ 已实现 |
| **Bug 检测** | 自动监控服务器日志，实时发现错误 | ✅ 已实现 |
| **智能修复** | 自动修复常见 LPC 代码错误        | ✅ 已实现 |
| **游戏测试** | 自动化游戏可玩性测试             | ✅ 已实现 |
| **知识库**   | 维护测试历史与代码基线           | ✅ 已实现 |
| **热更新**   | 支持游戏运行时热更新（无需重启） | ✅ 已实现 |
| **双语支持** | 完整的中文/英文文档              | ✅ 已实现 |

### 🐛 支持的 Bug 修复

#### ✅ 自动修复（无需确认）

| 类型           | 描述                  | 示例                   |
| -------------- | --------------------- | ---------------------- |
| **空指针检查** | 添加 `objectp()` 验证 | `if (objectp(target))` |
| **未定义变量** | 声明缺失变量          | `var_type xxx;`        |
| **缺失返回值** | 添加 `return` 语句    | `return 0;`            |
| **拼写错误**   | 修正字符串拼写        | `qury` → `query`       |

#### ⚠️ 需要确认

- 架构变更
- 多文件修改
- 游戏平衡调整

---

## 快速开始

### 📦 安装

```bash
# 克隆仓库
git clone https://github.com/FengYunCalm/ai-player.git

# 进入目录
cd ai-player

# 安装依赖
pip install -r requirements.txt

# 安装项目包（开发模式）
pip install -e .
```

### ⚙️ 配置

1. **复制配置文件**

```bash
cp config/config.example.yaml config/config.yaml
```

2. **编辑配置**

```bash
vim config/config.yaml
```

3. **基本配置示例**

```yaml
# 服务器连接配置
server:
  host: "localhost" # MUD 服务器地址
  port: 3939 # MUD 服务器端口
  encoding: "utf-8" # 字符编码
  connect_timeout: 10 # 连接超时（秒）

# 登录配置
login:
  separator: "|" # 账号密码分隔符
  default_gender: "男" # 默认性别（创建角色时使用）
  wait_time: 2 # 登录等待时间（秒）

# 测试账号配置
test:
  default_account: "test" # 测试账号
  default_password: "test123" # 测试密码
```

### 🎮 运行

#### 方式一：作为 MCP 服务器运行

```bash
python -m ai_player.mcp_server
```

#### 方式二：运行示例脚本

```bash
# 基础连接示例
python examples/basic_connection.py

# 自动化测试示例
python examples/automated_test.py

# Bug 检测示例
python examples/bug_detection.py
```

---

## 🤖 在 AI 助手中使用

AI-Player 完全支持 **MCP（Model Context Protocol）协议**，可以作为 Claude Code 和 OpenCode 的技能（Skill）使用，让 AI 助手直接控制 MUD 游戏进行自动化测试。

### 📌 支持的 AI 助手

| AI 助手 | 支持状态 | 说明 |
|---------|---------|------|
| **Claude Code** | ✅ 完全支持 | Anthropic 官方 AI 编程助手 |
| **OpenCode** | ✅ 完全支持 | 开源 AI 编程助手 |
| **其他 MCP 客户端** | ✅ 兼容 | 任何支持 MCP 协议的客户端 |

---

### 🚀 Claude Code 安装

#### 方式一：使用 MCP 配置文件（推荐）

1. **编辑 Claude Code MCP 配置文件**

   **macOS:**
   ```bash
   vim ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

   **Windows:**
   ```powershell
   notepad %APPDATA%\Claude\claude_desktop_config.json
   ```

   > **注意**: Claude Desktop 目前仅支持 macOS 和 Windows，不支持 Linux。
2. **添加 ai-player 配置**

   在 `mcpServers` 部分添加：

   ```json
   {
     "mcpServers": {
       "ai-player": {
         "command": "python",
         "args": ["-m", "ai_player.mcp_server"],
         "cwd": "C:\\Users\\你的用户名\\ai-player"
       }
     }
   }
   ```

   **Linux/macOS 路径示例：**
   ```json
   "cwd": "/home/你的用户名/ai-player"
   ```

3. **重启 Claude Code**

   重启后，Claude Code 会自动加载 ai-player 工具。

4. **验证安装**

   在 Claude Code 中输入：
   ```
   请列出可用的 MCP 工具
   ```

   应该能看到以下工具：
   - `xiakexing-ai_connect_server` - 连接游戏服务器
   - `xiakexing-ai_login_game` - 登录游戏
   - `xiakexing-ai_send_game_command` - 发送游戏命令
   - `xiakexing-ai_get_game_status` - 获取游戏状态
   - `xiakexing-ai_disconnect_server` - 断开连接
   - `xiakexing-ai_get_bug_report` - 获取 Bug 报告

---

#### 方式二：使用 Python 虚拟环境（推荐用于生产环境）

1. **创建虚拟环境**
   ```bash
   cd /path/to/ai-player
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   # 或
   venv\Scripts\activate     # Windows
   ```

2. **安装依赖**
   ```bash
   pip install -e .
   ```

3. **更新 MCP 配置**

   ```json
   {
     "mcpServers": {
       "ai-player": {
         "command": "/path/to/ai-player/venv/bin/python",
         "args": ["-m", "ai_player.mcp_server"],
         "cwd": "/path/to/ai-player"
       }
     }
   }
   ```

---

### 🚀 OpenCode 安装

#### 方式一：作为 Skill 文件使用（推荐）

1. **创建 Skill 目录和文件**

   OpenCode 使用特定的目录结构来存储 Skills：

   ```bash
   # 创建 Skill 目录
   mkdir -p .opencode/skills/ai-player
   
   # 创建 Skill 文件（必须是 SKILL.md，全大写）
   vim .opencode/skills/ai-player/SKILL.md
   ```

2. **添加 Skill 内容（必须包含 YAML frontmatter）**

   ```markdown
   ---
   name: ai-player
   description: AI-powered MUD game automation and testing tool using MCP protocol
   license: MIT
   compatibility: opencode
   metadata:
     tools: connect_server, login_game, send_game_command, get_game_status, disconnect_server, get_bug_report
   ---

   # AI-Player Skill

   ## 安装
   ```bash
   git clone https://github.com/FengYunCalm/ai-player.git
   cd ai-player
   pip install -e .
   ```

   ## 使用方法
   通过 MCP 协议调用以下工具：
   - `connect_server`: 连接游戏服务器
   - `login_game`: 登录游戏
   - `send_game_command`: 发送命令
   - `get_game_status`: 获取状态
   - `disconnect_server`: 断开连接
   - `get_bug_report`: 获取 Bug 报告
   ```

   > **重要**: 
   > - Skill 文件名必须是 `SKILL.md`（全大写）
   > - 目录名必须与 frontmatter 中的 `name` 字段一致
   > - 必须包含 YAML frontmatter

3. **Skill 文件位置说明**

   OpenCode 会搜索以下位置（按优先级）：
   
   **项目级**（推荐）：
   - `.opencode/skills/ai-player/SKILL.md`
   - `.claude/skills/ai-player/SKILL.md`
   - `.agents/skills/ai-player/SKILL.md`
   
   **全局级**：
   - `~/.config/opencode/skills/ai-player/SKILL.md`
   - `~/.claude/skills/ai-player/SKILL.md`
   - `~/.agents/skills/ai-player/SKILL.md`

4. **配置 MCP 服务器（可选）**

   如果需要直接使用 MCP 服务器，在 `opencode.json` 中添加：

   ```json
   {
     "mcp": {
       "ai-player": {
         "command": "python",
         "args": ["-m", "ai_player.mcp_server"],
         "cwd": "/path/to/ai-player"
       }
     }
   }

---

#### 方式二：直接集成到项目中

1. **作为依赖安装**

   在项目的 `requirements.txt` 中添加：
   ```
   git+https://github.com/FengYunCalm/ai-player.git@main
   ```

2. **在代码中使用**

   ```python
   from ai_player.mcp_server import MCPStdioServer
   import asyncio

   # 启动 MCP 服务器
   server = MCPStdioServer()
   asyncio.run(server.run())
   ```

---

### 💡 使用示例

#### 在 Claude Code 中测试新手村

```
请帮我测试侠客行新手村的可玩性：
1. 连接到 localhost:3939
2. 使用测试账号 test/test123 登录
3. 执行新手引导任务
4. 检查是否有 Bug
```

#### 在 OpenCode 中检测 Bug

```
请帮我检查 MUD 服务器的日志：
1. 连接到游戏服务器
2. 获取最近 10 个 Bug 报告
3. 分析 Bug 的严重程度
4. 给出修复建议
```

---

### 🔧 高级配置

#### 自定义配置文件路径

```json
{
  "mcpServers": {
    "ai-player": {
      "command": "python",
      "args": ["-m", "ai_player.mcp_server", "--config", "/custom/path/config.yaml"],
      "cwd": "/path/to/ai-player"
    }
  }
}
```

#### 使用环境变量

```bash
# Linux/macOS
export AI_PLAYER_CONFIG=/path/to/config.yaml

# Windows
set AI_PLAYER_CONFIG=C:\path\to\config.yaml
```

---

### 🐛 常见问题

#### Q: Claude Code 无法连接到 MCP 服务器？

**A:** 检查以下几点：
1. Python 路径是否正确（使用绝对路径）
2. 工作目录（cwd）是否正确
3. 依赖是否已安装（`pip install -e .`）
4. 配置文件是否有效（运行 `python -m ai_player.mcp_server` 测试）

#### Q: OpenCode 找不到 Skill 文件？

**A:** 确保：
1. Skill 文件位于 `.opencode/skills/` 目录
2. 文件名为 `.md` 格式
3. OpenCode 配置文件中已启用该 Skill

#### Q: MCP 工具调用失败？

**A:** 检查：
1. MUD 服务器是否正在运行
2. 服务器地址和端口是否正确
3. 防火墙是否允许连接
4. 查看 MCP 服务器日志输出

---

## 使用文档

### 📖 基础用法

#### 1. 连接游戏服务器

```python
from ai_player.core.connection import GameConnection

# 创建连接实例
conn = GameConnection()

# 连接到 MUD 服务器
conn.connect(host="localhost", port=3939)

# 登录游戏（账号不存在会自动注册）
conn.login(account="test", password="test123")

print(f"登录成功！当前房间：{conn.game_state['room']}")
```

#### 2. 发送游戏命令

```python
# 发送 "look" 命令查看房间
conn.send("look")

# 等待并获取响应
messages = conn.get_messages(timeout=1.0)

# 打印收到的消息
for msg in messages:
    print(msg["text"])
```

#### 3. Bug 检测与报告

```python
# 获取最近检测到的 Bug
bugs = conn.get_recent_bugs(count=5)

if bugs:
    print(f"发现 {len(bugs)} 个 Bug：")
    for bug in bugs:
        print(f"\n类型：{bug['type']}")
        print(f"严重级别：{bug['severity']}")
        print(f"消息：{bug['message']}")
        if bug['source_file']:
            print(f"位置：{bug['source_file']}:{bug['line_number']}")
else:
    print("未发现 Bug！")
```

### 🛠️ MCP 工具列表

AI-Player 提供以下 MCP 工具供 AI 调用：

| 工具名              | 描述                     | 参数                  |
| ------------------- | ------------------------ | --------------------- |
| `connect_server`    | 连接 MUD 游戏服务器      | `host`, `port`        |
| `login_game`        | 登录游戏（支持自动注册） | `account`, `password` |
| `send_game_command` | 发送游戏命令             | `command`             |
| `get_game_status`   | 获取当前游戏状态         | -                     |
| `disconnect_server` | 断开服务器连接           | -                     |
| `get_bug_report`    | 获取 Bug 检测报告        | `count`               |

### 🧪 测试场景

AI-Player 支持以下测试场景：

- **新手村可玩性测试** - 验证基础游戏功能是否正常
- **战斗系统测试** - 测试战斗机制、伤害计算等
- **物品系统测试** - 测试物品拾取、使用、交易等
- **通信系统测试** - 测试聊天、邮件等功能
- **压力测试** - 测试服务器在高负载下的稳定性

---

## 项目结构

```
ai-player/                          # 项目根目录
├── ai_player/                      # 主 Python 包
│   ├── __init__.py                 # 包初始化
│   ├── cli.py                      # CLI 入口
│   ├── mcp_server.py               # MCP 服务器（核心代码）
│   ├── config/                     # 配置文件目录
│   │   ├── config.yaml             # 主配置文件
│   │   └── config.example.yaml     # 配置示例
│   ├── core/                       # 核心模块
│   │   └── __init__.py
│   ├── utils/                      # 工具模块
│   │   ├── __init__.py
│   │   └── config_loader.py        # 配置加载器
│   └── knowledge/                  # 知识库
│       ├── __init__.py
│       ├── baseline.json           # 代码基线
│       ├── test_history.json       # 测试历史
│       └── README.md               # 知识库说明
├── docs/                           # 文档目录
├── docs/                           # 文档目录
│   ├── README_EN.md                # 英文版 README
│   ├── configuration.md            # 配置指南
│   └── index.md                    # 文档索引
├── examples/                       # 示例代码
│   ├── README.md                   # 示例说明
│   ├── basic_connection.py         # 基础连接示例
│   ├── automated_test.py           # 自动化测试示例
│   └── bug_detection.py            # Bug 检测示例
├── tests/                          # 测试目录
│   ├── __init__.py
│   ├── conftest.py                 # 测试配置
│   ├── test_connection.py          # 连接测试
│   └── README.md                   # 测试说明
├── .github/                        # GitHub 配置
│   ├── workflows/                  # CI/CD 工作流
│   │   ├── tests.yml               # 测试工作流
│   │   └── release.yml             # 发布工作流
│   ├── ISSUE_TEMPLATE/             # Issue 模板
│   │   ├── bug_report.md           # Bug 报告模板
│   │   └── feature_request.md      # 功能请求模板
│   ├── CODE_OF_CONDUCT.md          # 行为准则
│   ├── CONTRIBUTING.md             # 贡献指南（双语）
│   ├── SECURITY.md                 # 安全政策
│   ├── PROFILE.md                  # 组织简介
│   ├── pull_request_template.md    # PR 模板
│   └── README.md                   # GitHub 说明
├── LICENSE                         # MIT 许可证
├── CHANGELOG.md                    # 更新日志
├── ROADMAP.md                      # 开发路线图
├── README.md                       # 本文件（中文主文档）
├── setup.py                        # 安装脚本
├── pyproject.toml                  # 项目配置
├── requirements.txt                # 依赖列表
└── requirements-dev.txt            # 开发依赖
```

---

## 贡献指南

我们欢迎所有形式的贡献！无论是报告 Bug、提出功能建议，还是提交代码改进。

### 🤝 如何贡献

1. **Fork 本仓库** - 点击右上角的 "Fork" 按钮
2. **克隆你的 Fork** - `git clone https://github.com/YOUR_USERNAME/ai-player.git`
3. **创建分支** - `git checkout -b feature/amazing-feature`
4. **提交更改** - `git commit -m "feat: 添加 amazing 功能"`
5. **推送分支** - `git push origin feature/amazing-feature`
6. **创建 Pull Request** - 在 GitHub 上创建 PR

### 📝 代码规范

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) Python 代码规范
- 使用 4 个空格缩进
- 最大行长度 100 字符
- 提交信息使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式

详细的贡献指南请参阅 [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md)。

---

## 更新日志

### v1.0.0 (2025-03-04)

#### ✨ 新功能

- 初始开源版本发布
- MCP stdio 服务器实现
- TCP 连接管理
- Bug 自动检测引擎
- 配置管理系统
- 完整的中英文文档
- GitHub Actions CI/CD

查看完整的更新日志请参阅 [CHANGELOG.md](CHANGELOG.md)。

---

## 致谢

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP 协议
- [FluffOS](https://github.com/fluffos/fluffos) - LPC 驱动
- 所有贡献者和用户！

---

## 联系我们

- 📧 **邮箱**: fengyun.calm@users.noreply.github.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues)
- 💬 **讨论**: [GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

---

## 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

```
MIT License

Copyright (c) 2025 AI-Player Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个 Star！**

[🔝 回到顶部](#ai-player-智能游戏测试工具)

</div>
