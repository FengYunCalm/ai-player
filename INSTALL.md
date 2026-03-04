# 🚀 AI-Player 快速安装指南

## 📌 适配的 AI 助手

AI-Player 完全支持 **MCP（Model Context Protocol）协议**，可以作为以下 AI 助手的技能使用：

- ✅ **Claude Code** (Anthropic)
- ✅ **OpenCode** (开源)
- ✅ **任何支持 MCP 协议的客户端**

---

## 🎯 快速安装（5分钟）

### 步骤 1: 克隆仓库

```bash
git clone https://github.com/FengYunCalm/ai-player.git
cd ai-player
```

### 步骤 2: 安装依赖

```bash
pip install -e .
```

### 步骤 3: 配置 AI 助手

#### Claude Code 配置

编辑配置文件：

- **macOS/Linux**: `~/.config/claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

添加以下内容：

```json
{
  "mcpServers": {
    "ai-player": {
      "command": "python",
      "args": ["-m", "ai_player.mcp_server"],
      "cwd": "/path/to/ai-player"
    }
  }
}
```

**Windows 示例：**

```json
"cwd": "C:\\Users\\你的用户名\\ai-player"
```

**Linux/macOS 示例：**

```json
"cwd": "/home/你的用户名/ai-player"
```

#### OpenCode 配置

在项目目录下创建 `.opencode/skills/ai-player.md`：

````markdown
# AI-Player Skill

## 安装

```bash
git clone https://github.com/FengYunCalm/ai-player.git
cd ai-player
pip install -e .
```
````

## 配置 MCP

在 OpenCode 配置文件中添加：

```yaml
mcp:
  servers:
    ai-player:
      command: python
      args: [-m, ai_player.mcp_server]
      cwd: /path/to/ai-player
```

```

### 步骤 4: 重启 AI 助手

重启 Claude Code 或 OpenCode，工具会自动加载。

### 步骤 5: 验证安装

在 AI 助手中输入：
```

请列出可用的 MCP 工具

```

应该看到以下工具：
- `xiakexing-ai_connect_server` - 连接游戏服务器
- `xiakexing-ai_login_game` - 登录游戏
- `xiakexing-ai_send_game_command` - 发送游戏命令
- `xiakexing-ai_get_game_status` - 获取游戏状态
- `xiakexing-ai_disconnect_server` - 断开连接
- `xiakexing-ai_get_bug_report` - 获取 Bug 报告

---

## 💡 使用示例

### 示例 1: 测试新手村

```

请帮我测试侠客行新手村的可玩性：

1. 连接到 localhost:3939
2. 使用测试账号 test/test123 登录
3. 执行新手引导任务
4. 检查是否有 Bug

```

### 示例 2: 检测 Bug

```

请帮我检查 MUD 服务器的日志：

1. 连接到游戏服务器
2. 获取最近 5 个 Bug 报告
3. 分析 Bug 的严重程度
4. 给出修复建议

```

### 示例 3: 自动化测试

```

请帮我执行以下自动化测试：

1. 创建一个新角色
2. 测试基础移动命令（north, south, east, west）
3. 测试物品拾取和使用
4. 测试战斗系统
5. 生成测试报告

````

---

## 🔧 高级配置

### 使用虚拟环境（推荐）

```bash
cd /path/to/ai-player
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或
venv\Scripts\activate     # Windows

pip install -e .
````

更新 MCP 配置：

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

### 自定义配置文件

```bash
# 复制示例配置
cp config/config.example.yaml config/config.yaml

# 编辑配置
vim config/config.yaml
```

在 MCP 配置中指定配置文件：

```json
{
  "mcpServers": {
    "ai-player": {
      "command": "python",
      "args": [
        "-m",
        "ai_player.mcp_server",
        "--config",
        "/custom/path/config.yaml"
      ],
      "cwd": "/path/to/ai-player"
    }
  }
}
```

---

## 🐛 常见问题

### Q: Claude Code 无法连接到 MCP 服务器？

**A:** 检查以下几点：

1. ✅ Python 路径是否正确（使用绝对路径）
2. ✅ 工作目录（cwd）是否正确
3. ✅ 依赖是否已安装（`pip install -e .`）
4. ✅ 配置文件格式是否正确（JSON 格式）
5. ✅ 重启 Claude Code

### Q: OpenCode 找不到 Skill 文件？

**A:** 确保：

1. ✅ Skill 文件位于 `.opencode/skills/` 目录
2. ✅ 文件名为 `.md` 格式
3. ✅ OpenCode 配置文件中已启用该 Skill

### Q: MCP 工具调用失败？

**A:** 检查：

1. ✅ MUD 服务器是否正在运行
2. ✅ 服务器地址和端口是否正确（默认 localhost:3939）
3. ✅ 防火墙是否允许连接
4. ✅ 查看 MCP 服务器日志输出

### Q: 如何查看 MCP 服务器日志？

**A:** 手动启动服务器查看输出：

```bash
python -m ai_player.mcp_server
```

---

## 📚 更多资源

- **完整文档**: [README.md](README.md)
- **英文文档**: [docs/README_EN.md](docs/README_EN.md)
- **配置指南**: [docs/configuration.md](docs/configuration.md)
- **示例代码**: [examples/](examples/)
- **更新日志**: [CHANGELOG.md](CHANGELOG.md)
- **开发路线图**: [ROADMAP.md](ROADMAP.md)

---

## 🤝 获取帮助

- 📧 **邮箱**: fengyun.calm@users.noreply.github.com
- 🐛 **Bug 报告**: [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues)
- 💬 **讨论**: [GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

---

## ⭐ Star History

如果这个项目对你有帮助，请给我们一个 Star！

[![Star History Chart](https://api.star-history.com/svg?repos=FengYunCalm/ai-player&type=Date)](https://star-history.com/#FengYunCalm/ai-player&Date)

---

<div align="center">

**🎉 安装完成！开始使用 AI-Player 进行 MUD 游戏自动化测试吧！**

</div>
