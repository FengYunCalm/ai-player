from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 安全地读取 requirements.txt
requirements = []
try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [
            line.strip() for line in fh if line.strip() and not line.startswith("#")
        ]
except FileNotFoundError:
    # 如果在构建 wheel 时找不到 requirements.txt，使用默认依赖
    requirements = ["pyyaml>=6.0"]

setup(
    name="ai-player-mud",
    version="1.0.0",
    author="AI-Player Contributors",
    author_email="your.email@example.com",
    description="AI-powered MUD game automation and testing tool using MCP protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FengYunCalm/ai-player",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=22.0.0",
            "flake8>=5.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-player=ai_player.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "ai_player": ["config/*.yaml", "knowledge/*.json"],
    },
)
