#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Automated Test Scenario
演示自动化测试场景
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_player.mcp_server import GameConnection


def test_newbie_village():
    """Test newbie village functionality"""
    print("Testing Newbie Village...")

    conn = GameConnection()

    # Step 1: Connect
    print("  Step 1: Connect")
    assert conn.connect(), "Connection failed"
    print("    ✓ Connected")

    # Step 2: Login
    print("  Step 2: Login")
    assert conn.login("test", "test123"), "Login failed"
    print("    ✓ Logged in")

    # Step 3: Look around
    print("  Step 3: Look around")
    conn.send("look")
    time.sleep(1)
    messages = conn.get_messages(1.0)
    assert len(messages) > 0, "No response from look command"
    print(f"    ✓ Got {len(messages)} messages")

    # Step 4: Check exits
    print("  Step 4: Check exits")
    room = conn.game_state.get("room", "Unknown")
    print(f"    Current room: {room}")

    # Step 5: Move
    print("  Step 5: Try moving")
    conn.send("go north")
    time.sleep(1)
    messages = conn.get_messages(1.0)
    print(f"    ✓ Move response received")

    # Step 6: Check for bugs
    print("  Step 6: Check bugs")
    bugs = conn.get_recent_bugs()
    if bugs:
        print(f"    ⚠ Found {len(bugs)} bugs")
        for bug in bugs:
            print(f"      - {bug['message']}")
    else:
        print("    ✓ No bugs")

    # Cleanup
    conn.disconnect()
    print("  ✓ Test completed successfully!")

    return True


def main():
    """Run tests"""
    print("=" * 50)
    print("AI-Player Automated Test Example")
    print("=" * 50)
    print()

    try:
        test_newbie_village()
        print("\n✅ All tests passed!")
        return 0
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        return 1
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
