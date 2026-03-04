#!/usr/bin/env python3
"""AI-Player CLI entry point."""

import argparse
import sys
from pathlib import Path

# 添加项目根目录到 Python 路径
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

try:
    from ai_player import __version__
except ImportError:
    __version__ = "1.0.0"


def main():
    """CLI main entry point."""
    parser = argparse.ArgumentParser(
        prog="ai-player",
        description="AI-powered MUD game automation and testing tool using MCP protocol",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  ai-player --version              Show version
  ai-player --mcp                  Start MCP server (stdio mode)
  ai-player --help                 Show this help message

For more information: https://github.com/FengYunCalm/ai-player
        """,
    )

    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    parser.add_argument(
        "--mcp",
        action="store_true",
        help="Start MCP server in stdio mode",
    )

    parser.add_argument(
        "--config",
        type=str,
        default=None,
        help="Path to configuration file (default: ai_player/config/config.yaml)",
    )

    # 解析参数
    args = parser.parse_args()

    # 如果没有提供任何参数,显示帮助
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # 启动 MCP 服务器
    if args.mcp:
        try:
            from ai_player.mcp_server import main as mcp_main

            print(f"Starting AI-Player MCP Server v{__version__}...", file=sys.stderr)
            mcp_main()
        except ImportError as e:
            print(f"Error: Failed to import MCP server: {e}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
