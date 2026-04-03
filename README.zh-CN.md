# AI-Player

[English](README.md) | 简体中文

AI-Player 是一个面向 MCP 驱动 MUD 自动化的 Python 代码库。当前仓库的核心重点是 stdio MCP 服务器、基于 TCP 的游戏交互、登录辅助、消息采集，以及面向 FluffOS 风格 MUD 项目的日志型 Bug 报告能力。

## 仓库包含什么

- `ai_player/mcp_server.py` — MCP stdio 服务器与 TCP 游戏连接主流程
- `ai_player/config/` — 随仓库提供的配置文件（`config.example.yaml` 与 `config.yaml`）
- `ai_player/utils/config_loader.py` — 配置加载与项目路径辅助
- `examples/` — 基础连接、自动化测试、Bug 检测示例
- `tests/` — 当前基于 pytest 的测试集
- `.github/workflows/tests.yml` — 测试执行的 CI 工作流

## 获取源码

```bash
git clone https://github.com/FengYunCalm/ai-player.git
cd ai-player
```

这个仓库按源码优先来说明，不声明 pip 包发布、托管部署，或一键式分发流程。

## 当前技术基线

- 默认服务器目标：`localhost:3939`
- 当 YAML 配置文件不存在时，配置加载器会回退到内置默认值
- 登录设置、日志路径和错误关键词都来自配置
- pytest 已针对当前 `tests/` 目录配置覆盖率输出

## 仓库结构

```text
ai-player/
├── ai_player/                 # 主包
│   ├── mcp_server.py          # MCP stdio 服务器
│   ├── config/                # 随仓库提供的配置
│   ├── core/                  # 核心模块
│   ├── knowledge/             # 知识相关数据
│   └── utils/                 # 工具辅助
├── examples/                  # 示例脚本
├── tests/                     # Pytest 测试集
├── docs/                      # 补充文档
├── .github/                   # GitHub 工作流与社区文件
├── pyproject.toml             # 仓库中的打包元数据
└── README.md                  # 英文主 README
```

## 贡献与安全

- 贡献指南：`.github/CONTRIBUTING.md`
- 安全策略：`.github/SECURITY.md`
- 行为准则：`.github/CODE_OF_CONDUCT.md`

## 许可证

GPL-3.0
