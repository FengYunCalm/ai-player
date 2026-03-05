# 贡献指南 | Contributing Guide

[English Version Below](#contributing-guide)

---

## 🇨🇳 中文贡献指南

感谢您对 AI-Player 项目的关注！我们欢迎所有形式的贡献。

### 🤝 如何贡献

#### 报告 Bug

如果您发现了 Bug，请通过 [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues) 报告，并包含以下信息：

- 问题描述
- 复现步骤
- 预期行为
- 实际行为
- 环境信息（Python 版本、操作系统等）
- 相关日志或截图

#### 提出新功能

1. 先检查是否已有相关的 Issue
2. 创建新 Issue，使用 "Feature Request" 标签
3. 清晰描述功能的用途和预期行为

#### 提交代码

1. **Fork** 本仓库
2. 创建您的特性分支：`git checkout -b feature/ amazing-feature`
3. 提交更改：`git commit -m '添加 amazing 功能'`
4. 推送到分支：`git push origin feature/amazing-feature`
5. 创建 **Pull Request**

### 📝 代码规范

#### Python 代码风格

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 规范
- 使用 4 个空格缩进
- 最大行长度 100 字符
- 使用有意义的变量名

#### 提交信息规范

使用 [Conventional Commits](https://www.conventionalcommits.org/) 格式：

```
类型(范围): 简短描述

详细描述（可选）

相关问题: #123
```

**类型**：

- `feat`: 新功能
- `fix`: Bug 修复
- `docs`: 文档更新
- `style`: 代码格式（不影响功能）
- `refactor`: 代码重构
- `test`: 测试相关
- `chore`: 构建/工具相关

**示例**：

```
feat(bug-fixer): 添加空指针自动修复功能

实现自动检测并修复 LPC 代码中的空指针问题。

Closes #42
```

### 🧪 测试

#### 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试
pytest tests/test_connection.py

# 生成覆盖率报告
pytest --cov=ai_player --cov-report=html
```

#### 测试规范

- 为新功能编写测试
- 保持测试简洁明了
- 使用有意义的测试名称
- 测试应独立于执行顺序

### 📚 文档

- 更新相关的 README 部分
- 为新功能添加使用示例
- 更新 API 文档
- **同时更新中英文文档**

### 🎯 开发路线图

查看 [ROADMAP.md](ROADMAP.md) 了解项目的未来计划。

### 💬 社区

- 加入讨论：[GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

### ❓ 常见问题

**Q: 我需要签署贡献者协议吗？**
A: 不需要，但提交 PR 即表示您同意将代码以 GPL v3 许可证授权。

**Q: 我是新手，可以贡献吗？**
A: 当然可以！我们有 "good first issue" 标签的问题适合新手。

**Q: 如何成为维护者？**
A: 持续贡献高质量的代码和审查，团队会主动邀请。

---

## 🇺🇸 Contributing Guide

Thank you for your interest in the AI-Player project! We welcome all forms of contributions.

### 🤝 How to Contribute

#### Reporting Bugs

If you find a bug, please report it via [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues) with the following information:

- Problem description
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment info (Python version, OS, etc.)
- Related logs or screenshots

#### Proposing New Features

1. Check if a related Issue already exists
2. Create a new Issue with the "Feature Request" label
3. Clearly describe the feature purpose and expected behavior

#### Submitting Code

1. **Fork** this repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Create a **Pull Request**

### 📝 Code Standards

#### Python Code Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use 4 spaces for indentation
- Maximum line length: 100 characters
- Use meaningful variable names

#### Commit Message Standards

Use [Conventional Commits](https://www.conventionalcommits.org/) format:

```
type(scope): short description

Detailed description (optional)

Related issues: #123
```

**Types**:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation update
- `style`: Code style (no functional change)
- `refactor`: Code refactoring
- `test`: Test related
- `chore`: Build/tooling related

**Example**:

```
feat(bug-fixer): add automatic null pointer fix

Implement automatic detection and fixing of null pointer issues in LPC code.

Closes #42
```

### 🧪 Testing

#### Running Tests

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_connection.py

# Generate coverage report
pytest --cov=ai_player --cov-report=html
```

#### Testing Standards

- Write tests for new features
- Keep tests concise and clear
- Use meaningful test names
- Tests should be independent of execution order

### 📚 Documentation

- Update relevant README sections
- Add usage examples for new features
- Update API documentation
- **Update both Chinese and English documentation**

### 🎯 Development Roadmap

See [ROADMAP.md](ROADMAP.md) for future project plans.

### 💬 Community

- Join discussions: [GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

### ❓ FAQ

**Q: Do I need to sign a contributor agreement?**
A: No, but submitting a PR means you agree to license your code under GPL v3.

**Q: I'm a beginner, can I contribute?**
A: Absolutely! We have "good first issue" labeled issues perfect for beginners.

**Q: How do I become a maintainer?**
A: Consistently contribute high-quality code and reviews, and the team will invite you.

---

## 📞 Contact

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/FengYunCalm/ai-player/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/FengYunCalm/ai-player/discussions)

---

**再次感谢您的贡献！| Thank you again for your contribution!** 🎉
