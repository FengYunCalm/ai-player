#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Basic Connection and Commands
演示基本的连接和游戏命令发送
"""

import sys
import os
import time

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_player.mcp_server import GameConnection


def main():
    """Main example"""
    print("=" * 50)
    print("AI-Player Basic Example")
    print("=" * 50)

    # Create connection
    conn = GameConnection()

    # Connect to server
    print("\n1. Connecting to server...")
    if not conn.connect(host="localhost", port=3939):
        print("Failed to connect!")
        return 1
    print("Connected!")

    # Login
    print("\n2. Logging in...")
    if not conn.login(account="test", password="test123"):
        print("Login failed!")
        conn.disconnect()
        return 1
    print("Logged in!")

    # Send some commands
    print("\n3. Sending commands...")

    commands = ["look", "inventory", "hp"]

    for cmd in commands:
        print(f"\n  Command: {cmd}")
        conn.send(cmd)
        time.sleep(1)

        messages = conn.get_messages(timeout=1.0)
        for msg in messages:
            print(f"    -> {msg['text'][:60]}...")

    # Get bug report
    print("\n4. Checking for bugs...")
    bugs = conn.get_recent_bugs(count=5)
    if bugs:
        print(f"  Found {len(bugs)} bugs:")
        for bug in bugs:
            print(f"    - {bug['message']}")
    else:
        print("  No bugs detected!")

    # Disconnect
    print("\n5. Disconnecting...")
    conn.disconnect()
    print("Disconnected!")

    print("\n" + "=" * 50)
    print("Example completed!")
    print("=" * 50)

    return 0


if __name__ == "__main__":
    sys.exit(main())
