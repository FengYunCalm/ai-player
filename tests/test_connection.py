#!/usr/bin/env python3
"""Test connection module"""

import pytest
from unittest.mock import Mock, patch, MagicMock
import socket


def test_game_connection_init():
    """Test GameConnection initialization"""
    from ai_player.mcp_server import GameConnection

    conn = GameConnection()
    assert conn.host == "localhost"
    assert conn.port == 3939
    assert conn.connected == False
    assert conn.logged_in == False


def test_connection_config():
    """Test connection uses config values"""
    from ai_player.mcp_server import GameConnection

    conn = GameConnection()
    # Should use default config values
    assert conn.encoding == "utf-8"


# Add more tests as needed
