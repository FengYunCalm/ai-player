# AI-Player for MUD Games

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![MCP Protocol](https://img.shields.io/badge/MCP-Protocol-green.svg)](https://modelcontextprotocol.io/)

一个基于 **MCP (Model Context Protocol)** 的 MUD 游戏自动化测试与智能修复工具。支持实时 TCP 通信、Bug 自动检测、代码智能修复和游戏可玩性测试。

## ✨ 特性

- 🤖 **AI 驱动**: 基于 MCP 协议，与大模型无缝集成
- 🔌 **实时通信**: 通过 TCP 与 MUD 服务器实时交互
- 🐛 **Bug 检测**: 自动监控服务器日志，实时发现错误
- 🔧 **智能修复**: 自动修复常见 LPC 代码错误
- 🎮 **游戏测试**: 自动化游戏可玩性测试
- 📊 **知识库**: 维护测试历史与代码基线
- 🔄 **热更新**: 支持游戏运行时热更新（无需重启）

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/ai-player.git
cd ai-player

# 安装依赖
pip install -r requirements.txt

# 复制配置文件
cp config/config.example.yaml config/config.yaml
```

### 配置

编辑 `config/config.yaml`：

```yaml
server:
  host: "localhost"
  port: 3939
  encoding: "utf-8"

login:
  separator: "║"
  default_gender: "男"

test:
  default_account: "test"
  default_password: "test123"
```

### 运行

```bash
# 作为 MCP 服务器运行
python -m ai_player.mcp_server

# 或运行增强版
python -m ai_player.mcp_enhanced
```

## 📖 使用示例

### 1. 连接游戏服务器

```python
from ai_player.core.connection import GameConnection

conn = GameConnection()
conn.connect(host="localhost", port=3939)
conn.login(account="test", password="test123")
```

### 2. 发送游戏命令

```python
conn.send("look")
messages = conn.get_messages(timeout=1.0)
for msg in messages:
    print(msg["text"])
```

### 3. 获取 Bug 报告

```python
bugs = conn.get_recent_bugs(count=5)
for bug in bugs:
    print(f"[{bug.type}] {bug.message}")
```

## 🏗️ 项目结构

```
ai-player/
├── ai_player/              # 主包
│   ├── core/               # 核心模块
│   │   ├── connection.py   # TCP 连接管理
│   │   ├── log_monitor.py  # 日志监控
│   │   └── bug_fixer.py    # Bug 修复器
│   ├── utils/              # 工具模块
│   │   └── config_loader.py # 配置加载
│   └── knowledge/          # 知识库
├── tests/                  # 测试用例
├── docs/                   # 文档
├── examples/               # 使用示例
├── config/                 # 配置文件
└── .github/                # GitHub 配置
```

## 🔧 MCP 工具列表

| 工具名              | 描述                     |
| ------------------- | ------------------------ |
| `connect_server`    | 连接 MUD 游戏服务器      |
| `login_game`        | 登录游戏（支持自动注册） |
| `send_game_command` | 发送游戏命令             |
| `get_game_status`   | 获取游戏状态             |
| `disconnect_server` | 断开连接                 |
| `get_bug_report`    | 获取 Bug 检测报告        |

## 📝 支持的 Bug 修复类型

### 自动修复（无需确认）

- ✅ **空指针检查**: 添加 `objectp()` 验证
- ✅ **未定义变量**: 声明缺失变量
- ✅ **缺失返回值**: 添加 `return` 语句
- ✅ **拼写错误**: 修正字符串拼写

### 需要确认

- ⚠️ **架构变更**: 结构性修改
- ⚠️ **多文件修改**: 跨文件协调修复
- ⚠️ **游戏平衡**: 影响游戏机制的修改

## 🧪 测试场景

- **新手村可玩性测试**: 验证基础游戏功能
- **战斗系统测试**: 测试战斗机制
- **物品系统测试**: 测试物品交互
- **通信系统测试**: 测试聊天功能
- **压力测试**: 服务器稳定性测试

## 🤝 贡献

我们欢迎所有形式的贡献！请参阅 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何参与。

### 开发环境设置

```bash
# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -r requirements-dev.txt

# 运行测试
pytest
```

## 📜 许可证

本项目采用 [MIT 许可证](LICENSE) 开源。

## 🙏 致谢

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP 协议
- [FluffOS](https://github.com/fluffos/fluffos) - LPC 驱动
- 所有贡献者和用户！

## 📮 联系方式

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/ai-player/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/ai-player/discussions)

---

⭐ 如果这个项目对你有帮助，请给我们一个 Star！
