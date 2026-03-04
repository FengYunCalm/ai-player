#!/bin/bash
# GitHub Upload Script for AI-Player
# Run this script to upload the project to GitHub

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  AI-Player GitHub Upload Script${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo -e "${RED}Error: git is not installed${NC}"
    echo "Please install git first: https://git-scm.com/downloads"
    exit 1
fi

# Navigate to project directory
cd "$(dirname "$0")"
PROJECT_DIR="$(pwd)"
echo -e "${YELLOW}Project directory: $PROJECT_DIR${NC}"

# Get GitHub username
echo ""
echo -n "Enter your GitHub username: "
read USERNAME

# Get repository name
echo -n "Enter repository name [ai-player]: "
read REPO_NAME
REPO_NAME=${REPO_NAME:-ai-player}

# Check if already initialized
if [ -d ".git" ]; then
    echo -e "${YELLOW}Git repository already initialized${NC}"
    echo -n "Do you want to reinitialize? (y/N): "
    read REINIT
    if [[ $REINIT =~ ^[Yy]$ ]]; then
        rm -rf .git
    else
        echo -e "${GREEN}Using existing git repository${NC}"
    fi
fi

# Initialize git
echo ""
echo -e "${YELLOW}Initializing git repository...${NC}"
git init

# Configure git (if not already configured)
if ! git config --global user.email &> /dev/null; then
    echo ""
    echo -n "Enter your email for git: "
    read EMAIL
    git config user.email "$EMAIL"
fi

if ! git config --global user.name &> /dev/null; then
    git config user.name "$USERNAME"
fi

# Add all files
echo -e "${YELLOW}Adding files to git...${NC}"
git add .

# Commit
echo -e "${YELLOW}Creating initial commit...${NC}"
git commit -m "Initial open source release v1.0.0

- MCP stdio server implementation
- TCP connection management
- Bug detection engine
- Configuration system
- Complete documentation
- CI/CD workflows"

# Rename branch to main
git branch -M main

# Add remote
echo ""
echo -e "${YELLOW}Setting up remote...${NC}"
git remote add origin "https://github.com/$USERNAME/$REPO_NAME.git" 2>/dev/null || git remote set-url origin "https://github.com/$USERNAME/$REPO_NAME.git"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Repository Ready!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo ""
echo "1. Create repository on GitHub:"
echo "   https://github.com/new"
echo ""
echo "   Repository name: $REPO_NAME"
echo "   Description: AI-powered MUD game automation tool"
echo "   Visibility: Public (or Private)"
echo "   ✓ Initialize with README (optional)"
echo ""
echo "2. Push to GitHub:"
echo -e "   ${GREEN}git push -u origin main${NC}"
echo ""
echo "   If prompted, enter your GitHub credentials"
echo "   (or use a personal access token)"
echo ""
echo "3. Create a release:"
echo "   - Go to https://github.com/$USERNAME/$REPO_NAME/releases"
echo "   - Click 'Create a new release'"
echo "   - Tag: v1.0.0"
echo "   - Upload: ai-player-open-source-v1.0.0.zip"
echo ""
echo -e "${GREEN}Done!${NC}"
