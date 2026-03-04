@echo off
chcp 65001 >nul
echo ========================================
echo   AI-Player GitHub Upload Script
echo ========================================
echo.

REM Check if git is installed
where git >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: git is not installed
    echo Please install git first: https://git-scm.com/downloads
    pause
    exit /b 1
)

REM Navigate to project directory
cd /d "%~dp0"
echo Project directory: %cd%
echo.

REM Get GitHub username
set /p USERNAME="Enter your GitHub username: "

REM Get repository name
set /p REPO_NAME="Enter repository name [ai-player]: "
if "%REPO_NAME%"=="" set REPO_NAME=ai-player

REM Check if already initialized
if exist ".git" (
    echo Git repository already initialized
    set /p REINIT="Do you want to reinitialize? (y/N): "
    if /i "%REINIT%"=="y" (
        rmdir /s /q .git
    ) else (
        echo Using existing git repository
    )
)

echo.
echo Initializing git repository...
git init

REM Configure git (if not already configured)
git config user.email >nul 2>&1
if %errorlevel% neq 0 (
    set /p EMAIL="Enter your email for git: "
    git config user.email "%EMAIL%"
)

git config user.name >nul 2>&1
if %errorlevel% neq 0 (
    git config user.name "%USERNAME%"
)

REM Add all files
echo Adding files to git...
git add .

REM Commit
echo Creating initial commit...
git commit -m "Initial open source release v1.0.0"

REM Rename branch to main
git branch -M main

REM Add remote
echo Setting up remote...
git remote add origin "https://github.com/%USERNAME%/%REPO_NAME%.git" 2>nul || git remote set-url origin "https://github.com/%USERNAME%/%REPO_NAME%.git"

echo.
echo ========================================
echo   Repository Ready!
echo ========================================
echo.
echo Next steps:
echo.
echo 1. Create repository on GitHub:
echo    https://github.com/new
echo.
echo    Repository name: %REPO_NAME%
echo    Description: AI-powered MUD game automation tool
echo    Visibility: Public (or Private)
echo    [x] Initialize with README (optional)
echo.
echo 2. Push to GitHub:
echo    git push -u origin main
echo.
echo    If prompted, enter your GitHub credentials
echo    (or use a personal access token)
echo.
echo 3. Create a release:
echo    - Go to https://github.com/%USERNAME%/%REPO_NAME%/releases
echo    - Click "Create a new release"
echo    - Tag: v1.0.0
echo    - Upload: ai-player-open-source-v1.0.0.zip
echo.
pause
