# 🚀 GitHub 上传指南

## 方式一：使用自动化脚本（推荐）

### Windows 用户

1. **双击运行脚本**

   ```
   upload-to-github.bat
   ```

2. **按提示输入**
   - GitHub 用户名
   - 仓库名称（默认：ai-player）

3. **完成提示后**
   - 访问 https://github.com/new 创建仓库
   - 运行 `git push -u origin main`

### Mac/Linux 用户

1. **打开终端，进入项目目录**

   ```bash
   cd ~/Desktop/ai-player-open-source
   ```

2. **运行脚本**

   ```bash
   bash upload-to-github.sh
   ```

3. **按提示操作**

---

## 方式二：手动上传

### 步骤 1: 准备环境

确保已安装：

- [Git](https://git-scm.com/downloads)
- GitHub 账号

### 步骤 2: 本地 Git 初始化

```bash
# 进入项目目录
cd C:\Users\MECHREVO\Desktop\ai-player-open-source

# 初始化 git
git init

# 配置 git（如果未配置过）
git config user.email "your.email@example.com"
git config user.name "Your Name"

# 添加所有文件
git add .

# 提交
git commit -m "Initial open source release v1.0.0"

# 重命名分支为 main
git branch -M main
```

### 步骤 3: 创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `ai-player`
   - **Description**: `AI-powered MUD game automation and testing tool using MCP protocol`
   - **Visibility**: Public (推荐) 或 Private
   - **☑️** Add a README file (可选)
   - **☑️** Add .gitignore → 选择 Python
   - **☑️** Choose a license → 选择 MIT

3. 点击 **Create repository**

### 步骤 4: 推送到 GitHub

```bash
# 添加远程仓库
git remote add origin https://github.com/你的用户名/ai-player.git

# 推送代码
git push -u origin main
```

如果提示输入密码，使用 GitHub Personal Access Token（见下文）。

### 步骤 5: 创建 Release

1. 访问 `https://github.com/你的用户名/ai-player/releases`
2. 点击 **Create a new release**
3. 填写：
   - **Tag version**: `v1.0.0`
   - **Release title**: `AI-Player v1.0.0 - Initial Release`
   - **Description**:

     ````markdown
     ## 🎉 Initial Release

     AI-powered MUD game automation and testing tool.

     ### Features

     - MCP stdio server implementation
     - TCP connection management
     - Automatic bug detection
     - Configuration system
     - Complete documentation

     ### Installation

     ```bash
     pip install ai-player-mud
     ```
     ````

     ```

     ```

   - **上传文件**: 拖拽 `ai-player-open-source-v1.0.0.zip`

4. 点击 **Publish release**

---

## 🔐 设置 GitHub Personal Access Token

如果你启用了两步验证，需要使用 Token 代替密码：

1. 访问 https://github.com/settings/tokens
2. 点击 **Generate new token (classic)**
3. 填写 **Note**: `AI-Player Upload`
4. 选择有效期（推荐 30 天）
5. 勾选权限：
   - ✅ `repo` (完整仓库访问)
6. 点击 **Generate token**
7. **复制 Token**（只显示一次！）
8. 推送时，用户名是你的 GitHub 用户名，密码是这个 Token

---

## ✅ 上传后检查清单

- [ ] 代码已推送到 GitHub
- [ ] README.md 显示正常
- [ ] LICENSE 文件存在
- [ ] .github/workflows/ 文件存在
- [ ] Release 已创建并包含 zip 文件
- [ ] Issues 和 Discussions 已启用
- [ ] GitHub Pages 可选启用

---

## 🎨 可选：美化仓库

### 添加徽章 (Badges)

编辑 `README.md`，在标题下方添加：

```markdown
![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Tests](https://github.com/你的用户名/ai-player/workflows/Tests/badge.svg)
```

### 启用 GitHub Pages

1. Settings → Pages
2. Source: Deploy from a branch
3. Branch: main / root
4. 保存后，访问 `https://你的用户名.github.io/ai-player/`

### 添加社交预览

1. Settings → Social preview
2. 上传图片 (1280×640px)
3. 保存

---

## 🆘 常见问题

### Q: 推送时提示 "Permission denied"

**A**: 检查仓库权限，或确认使用了 Personal Access Token

### Q: "error: failed to push some refs"

**A**: 运行 `git pull origin main` 然后重新推送

### Q: 如何更新已上传的代码？

**A**:

```bash
git add .
git commit -m "Update description"
git push origin main
```

### Q: 上传后如何删除？

**A**:

- 删除仓库: Settings → Danger Zone → Delete this repository
- 本地删除: 直接删除文件夹

---

## 📞 需要帮助？

- GitHub Docs: https://docs.github.com
- Git 文档: https://git-scm.com/doc
- 查看 `TROUBLESHOOTING.md` 解决常见问题

---

**祝你的开源项目成功！** 🎉
