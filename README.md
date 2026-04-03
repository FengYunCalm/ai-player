# AI-Player

English | [简体中文](README.zh-CN.md)

AI-Player is a Python codebase for MCP-driven MUD automation. In the current repository, the core focus is a stdio MCP server, TCP-based game interaction, login helpers, message capture, and log-backed bug reporting for FluffOS-style MUD projects.

## What this repository contains

- `ai_player/mcp_server.py` — MCP stdio server and TCP game connection workflow
- `ai_player/config/` — bundled configuration files (`config.example.yaml` and `config.yaml`)
- `ai_player/utils/config_loader.py` — configuration loading and project path helpers
- `examples/` — basic connection, automated test, and bug detection examples
- `tests/` — current pytest-based test suite
- `.github/workflows/tests.yml` — CI workflow for test execution

## Get the code

```bash
git clone https://github.com/FengYunCalm/ai-player.git
cd ai-player
```

This repository is documented as source code first. It does not claim any pip package release, hosted deployment, or one-command distribution flow.

## Current technical baseline

- default server target: `localhost:3939`
- configuration loader falls back to built-in defaults when the YAML file is missing
- login settings, log paths, and error keywords are all read from configuration
- pytest is configured for the current `tests/` directory with coverage output

## Repository layout

```text
ai-player/
├── ai_player/                 # Main package
│   ├── mcp_server.py          # MCP stdio server
│   ├── config/                # Bundled config files
│   ├── core/                  # Core package modules
│   ├── knowledge/             # Knowledge-related data
│   └── utils/                 # Utility helpers
├── examples/                  # Example scripts
├── tests/                     # Pytest suite
├── docs/                      # Supplemental documentation
├── .github/                   # GitHub workflows and community files
├── pyproject.toml             # Packaging metadata in repo
└── README.zh-CN.md            # Chinese README
```

## Contributing and security

- Contribution guide: `.github/CONTRIBUTING.md`
- Security policy: `.github/SECURITY.md`
- Code of conduct: `.github/CODE_OF_CONDUCT.md`

## License

GPL-3.0
