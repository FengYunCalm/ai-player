#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example: Bug Detection and Reporting
演示 Bug 检测和报告功能
"""

import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_player.mcp_server import GameConnection


def main():
    """Bug detection example"""
    print("=" * 50)
    print("AI-Player Bug Detection Example")
    print("=" * 50)

    conn = GameConnection()

    # Connect and login
    print("\nConnecting and logging in...")
    if not conn.connect():
        print("Failed to connect!")
        return 1

    if not conn.login("test", "test123"):
        print("Failed to login!")
        conn.disconnect()
        return 1

    print("Connected and logged in!")

    # Execute some commands that might trigger bugs
    print("\nExecuting commands...")

    test_commands = [
        "look",
        "inventory",
        "go north",
        "go south",
        "get item",
        "drop item",
    ]

    for cmd in test_commands:
        print(f"\n  Testing: {cmd}")
        conn.send(cmd)
        time.sleep(1)

        # Check for new bugs after each command
        bugs = conn.get_recent_bugs(count=3)
        if bugs:
            print(f"    ⚠ Detected {len(bugs)} bugs:")
            for bug in bugs:
                print(f"      Type: {bug['type']}")
                print(f"      Severity: {bug['severity']}")
                print(f"      Message: {bug['message']}")
                if bug["source_file"]:
                    print(f"      Source: {bug['source_file']}:{bug['line_number']}")
                print()
        else:
            print("    ✓ No bugs detected")

    # Final report
    print("\n" + "=" * 50)
    print("Final Bug Report")
    print("=" * 50)

    all_bugs = conn.get_recent_bugs(count=10)
    if all_bugs:
        print(f"\nTotal bugs detected: {len(all_bugs)}")
        print("\nBreakdown by type:")

        by_type = {}
        by_severity = {}

        for bug in all_bugs:
            bug_type = bug["type"]
            severity = bug["severity"]
            by_type[bug_type] = by_type.get(bug_type, 0) + 1
            by_severity[severity] = by_severity.get(severity, 0) + 1

        for bug_type, count in by_type.items():
            print(f"  {bug_type}: {count}")

        print("\nBreakdown by severity:")
        for severity, count in by_severity.items():
            print(f"  {severity}: {count}")
    else:
        print("\n✅ No bugs detected during testing!")

    conn.disconnect()
    print("\nDone!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
