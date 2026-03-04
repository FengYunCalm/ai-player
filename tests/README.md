# Tests

This directory contains the test suite for AI-Player.

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=ai_player --cov-report=html

# Run specific test file
pytest tests/test_connection.py

# Run with verbose output
pytest -v
```

## Test Structure

```
tests/
├── test_connection.py    # Connection tests
├── test_config.py        # Configuration tests
├── test_bug_detection.py # Bug detection tests
└── conftest.py          # Shared fixtures
```

## Writing Tests

Use pytest for all tests:

```python
def test_connection():
    conn = GameConnection()
    assert conn.connect() == True
```
