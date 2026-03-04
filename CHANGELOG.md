# 更新日志

[![Keep a Changelog](https://img.shields.io/badge/Keep%20a%20Changelog-1.0.0-%23E05935?style=flat-square)](https://keepachangelog.com/zh-CN/1.0.0/)
[![Semantic Versioning](https://img.shields.io/badge/Semantic%20Versioning-2.0.0-%233F9BDB?style=flat-square)](https://semver.org/lang/zh-CN/)

> 所有项目的显著变更都将记录在此文件中。
>
> 本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/) 规范，变更日志格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

---

## [未发布] - Unreleased

### 🔮 计划中

#### 新增功能 (Added)

- 连接池管理系统 - 支持多账号并发连接
- WebSocket 协议支持 - 替代 TCP 长连接
- 测试场景 DSL - 领域特定语言编写测试用例
- LLM 深度集成 - OpenAI/Claude API 支持
- Web 管理界面 - 可视化监控和控制

#### 变更 (Changed)

- 重构核心架构为插件化设计
- 优化 TCP 连接性能和稳定性
- 改进日志监控效率

#### 计划废弃 (Deprecated)

- 旧版配置文件格式（v2.0 后移除）

---

## [1.0.0] - 2026-03-04

### 🎉 重大发布

这是 **AI-Player** 的首个开源版本！经过 4 个月的内部开发和测试，我们很高兴将这个工具分享给开源社区。

### ✨ 新增功能 (Added)

#### 核心功能

- **MCP stdio 服务器** - 完整实现 Model Context Protocol 标准
  - 支持 6 个核心 MCP 工具
  - 符合 MCP 规范的 JSON-RPC 通信
  - stdio 传输层实现
- **TCP 连接管理器** - 稳定的 MUD 服务器连接
  - 自动重连机制
  - 连接超时处理
  - 消息队列缓冲
  - 编码自动检测（UTF-8/GBK）
- **实时消息接收系统** - 异步消息处理
  - 后台线程持续监听
  - 消息解析和分类
  - 游戏状态跟踪
- **Bug 自动检测引擎** - 智能日志分析
  - 20+ 种常见 LPC 错误模式识别
  - 错误严重程度分级（Critical/Error/Warning）
  - 源文件和行号定位
  - 错误频率统计
- **知识库系统** - 测试历史和代码基线
  - JSON 格式的代码基线存储
  - 测试历史记录
  - 支持基线对比和回滚

#### MCP 工具集

提供 6 个标准 MCP 工具供 AI 调用：

1. **connect_server** - 连接 MUD 游戏服务器
   - 参数: `host`, `port`
   - 自动连接和初始化
2. **login_game** - 登录游戏（支持自动注册）
   - 参数: `account`, `password`
   - 新账号自动创建角色
3. **send_game_command** - 发送游戏命令
   - 参数: `command`
   - 支持 MUD 标准命令格式
4. **get_game_status** - 获取当前游戏状态
   - 返回: 连接状态、房间信息、玩家状态等
5. **disconnect_server** - 断开服务器连接
   - 安全关闭连接和清理资源
6. **get_bug_report** - 获取 Bug 检测报告
   - 参数: `count`（获取最近 N 个 Bug）
   - 返回: Bug 列表及详细信息

#### 配置管理

- **YAML 配置系统** - 灵活的配置管理
  - 单例模式配置加载器
  - 支持环境变量覆盖
  - 配置验证和默认值
- **配置项支持**:
  - 服务器连接参数
  - 登录和测试账号
  - Bug 检测规则
  - 日志监控路径
  - 知识库路径

#### 日志和监控

- **实时日志监控** - 后台日志文件监控
  - 支持 FluffOS 标准日志格式
  - 多日志文件并发监控
  - 错误实时捕获

#### 文档和示例

- **完整的双语文档**
  - 中文主 README（448 行）
  - 英文版 README
  - API 使用指南
  - 配置详细说明
- **示例代码**
  - `basic_connection.py` - 基础连接示例
  - `automated_test.py` - 自动化测试示例
  - `bug_detection.py` - Bug 检测示例

#### 开发者工具

- **GitHub Actions CI/CD**
  - 自动测试工作流
  - 自动发布工作流
  - 多 Python 版本测试（3.8-3.11）
- **测试框架**
  - pytest 测试套件
  - 测试覆盖率报告
  - conftest.py 共享配置

### 🔧 技术特性

- **语言和版本**: Python 3.8+
- **协议标准**: 完全遵循 MCP 协议规范
- **跨平台**: 支持 Windows/Linux/macOS
- **许可证**: MIT 开源许可证
- **代码质量**:
  - 遵循 PEP 8 规范
  - 类型提示（Type Hints）
  - 文档字符串覆盖

### 📦 依赖管理

- `pyyaml>=6.0` - YAML 配置解析
- `mcp>=0.9.0` - MCP 协议 SDK

### 🙏 致谢

感谢以下项目和社区：

- [Model Context Protocol](https://modelcontextprotocol.io/) - MCP 协议标准
- [FluffOS](https://github.com/fluffos/fluffos) - LPC 游戏驱动
- 所有内部测试用户和反馈贡献者

---

## [0.9.0] - 2026-02-15 (内部版本)

### 新增 (Added)

- 增强版 TCP 连接管理
  - 连接池原型实现
  - 断线自动重连（3 次重试）
  - 连接状态持久化
- 后台日志监控系统
  - 多线程日志文件监控
  - 实时错误捕获
  - 日志轮转支持
- Bug 分类和严重程度评估
  - Critical（崩溃级）
  - Error（错误级）
  - Warning（警告级）
- 游戏状态跟踪
  - 玩家位置、状态、物品
  - NPC 交互记录
  - 房间环境信息

### 变更 (Changed)

- 重构配置加载器为单例模式
  - 避免重复加载配置
  - 全局配置访问点
- 优化消息解析性能
  - 减少字符串操作
  - 使用正则表达式缓存
- 改进错误处理
  - 更详细的错误信息
  - 异常堆栈追踪

### 修复 (Fixed)

- 修复 TCP 连接在高延迟下的超时问题
- 解决消息队列在并发访问时的竞争条件
- 修复配置文件路径在 Windows 下的兼容性问题

---

## [0.8.0] - 2026-01-20 (内部版本)

### 新增 (Added)

- 基础 MCP 服务器框架
  - stdio 传输层
  - JSON-RPC 消息处理
  - 工具注册和调用机制
- 工具定义和调用机制
  - 工具参数验证
  - 返回值格式化
  - 错误处理和报告
- JSON-RPC 通信协议
  - 请求/响应模型
  - 批量请求支持
  - 错误码标准化

### 修复 (Fixed)

- 解决 TCP 连接在 30 秒无响应时的超时问题
  - 增加心跳机制
  - 调整超时参数
- 修复消息队列在高并发时的竞争条件
  - 使用线程锁保护共享资源
  - 优化队列操作

---

## [0.7.0] - 2025-12-10 (内部版本)

### 新增 (Added)

- 项目初始化
  - 项目结构设计
  - 基础配置系统
- 基础 TCP 连接功能
  - Socket 连接封装
  - 简单的发送/接收
- 简单的命令发送和接收
  - 命令格式化
  - 响应解析

---

## 📊 版本统计

| 版本   | 发布日期   | 主要特性       | 代码行数 | 测试覆盖率 |
| ------ | ---------- | -------------- | -------- | ---------- |
| v1.0.0 | 2026-03-04 | 首次开源发布   | ~2000+   | 基础测试覆盖 |
| v0.9.0 | 2026-02-15 | 连接和日志增强 | ~1500    | 75%        |
| v0.8.0 | 2026-01-20 | MCP 框架       | ~1000    | 60%        |
| v0.7.0 | 2025-12-10 | 项目初始化     | ~500     | 40%        |

---

## 🔖 版本号说明

本项目使用**语义化版本** (Semantic Versioning 2.0.0)：

### 格式: `MAJOR.MINOR.PATCH`

- **MAJOR（主版本号）**: 不兼容的 API 变更
  - 例如: 从 v1.x 升级到 v2.0
- **MINOR（次版本号）**: 向下兼容的功能新增
  - 例如: v1.0 → v1.1（新增功能，但不破坏现有 API）
- **PATCH（修订号）**: 向下兼容的问题修复
  - 例如: v1.0.0 → v1.0.1（Bug 修复）

### 示例

- `v1.0.0` - 首个稳定版本
- `v1.1.0` - 新增 WebSocket 支持（向下兼容）
- `v1.1.1` - 修复连接 Bug（向下兼容）
- `v2.0.0` - 重构 API（不向下兼容）

---

## 📝 更新日志规范

### 变更类型

- **Added（新增）**: 新功能
- **Changed（变更）**: 现有功能的变更
- **Deprecated（废弃）**: 即将移除的功能
- **Removed（移除）**: 已移除的功能
- **Fixed（修复）**: Bug 修复
- **Security（安全）**: 安全相关的修复

### 如何维护

1. 每次提交代码时更新 `[未发布]` 部分
2. 发布新版本时，将 `[未发布]` 内容移到新版本号下
3. 遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范

---

## 🔗 相关链接

- [GitHub Releases](https://github.com/FengYunCalm/ai-player/releases) - 所有版本下载
- [GitHub Commits](https://github.com/FengYunCalm/ai-player/commits/main) - 详细提交历史
- [Milestone Tracker](https://github.com/FengYunCalm/ai-player/milestones) - 里程碑追踪

---

<div align="center">

**[🔝 回到顶部](#更新日志)**

</div>
