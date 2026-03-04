# 更新日志

所有项目的显著变更都将记录在此文件中。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 新增

- 计划中: 连接池管理
- 计划中: 测试场景 DSL
- 计划中: LLM 集成

## [1.0.0] - 2026-03-04

### 新增

- 初始开源版本
- MCP stdio 服务器实现
- TCP 连接管理器
- 实时消息接收系统
- Bug 自动检测引擎
- 6个 MCP 工具:
  - connect_server
  - login_game
  - send_game_command
  - get_game_status
  - disconnect_server
  - get_bug_report
- YAML 配置管理系统
- 日志文件监控
- 完整的文档和示例

### 技术特性

- 基于 Python 3.8+
- 遵循 MCP 协议标准
- 支持多平台 (Windows/Linux/macOS)
- MIT 开源许可证

## [0.9.0] - 2026-02 (内部版本)

### 新增

- 增强版 TCP 连接管理
- 后台日志监控系统
- Bug 分类和严重程度评估
- 游戏状态跟踪

### 变更

- 重构配置加载器为单例模式
- 优化消息解析性能

## [0.8.0] - 2026-01 (内部版本)

### 新增

- 基础 MCP 服务器框架
- 工具定义和调用机制
- JSON-RPC 通信协议

### 修复

- 解决 TCP 连接超时问题
- 修复消息队列竞争条件

## [0.7.0] - 2025-12 (内部版本)

### 新增

- 项目初始化
- 基础 TCP 连接功能
- 简单的命令发送和接收

---

## 版本号说明

本项目使用**语义化版本** (Semantic Versioning)：

- **主版本号 (MAJOR)**: 不兼容的 API 变更
- **次版本号 (MINOR)**: 向下兼容的功能新增
- **修订号 (PATCH)**: 向下兼容的问题修复

示例: `v1.2.3` 表示主版本1，次版本2，修订3
