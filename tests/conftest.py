"""Test configuration and fixtures"""

import pytest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def mock_config():
    """Mock configuration for tests"""
    return {
        "server": {"host": "localhost", "port": 3939, "encoding": "utf-8"},
        "login": {"separator": "|", "default_gender": "Male"},
    }
