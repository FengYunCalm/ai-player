# Examples Directory

This directory contains example scripts demonstrating how to use AI-Player.

## Available Examples

### 1. basic_connection.py

Basic connection and command demonstration.

```bash
python examples/basic_connection.py
```

**Features:**

- Connect to MUD server
- Login
- Send commands
- Get bug reports

### 2. automated_test.py

Automated testing scenario example.

```bash
python examples/automated_test.py
```

**Features:**

- Structured test flow
- Assertions and validation
- Test reporting

### 3. bug_detection.py

Bug detection and reporting demonstration.

```bash
python examples/bug_detection.py
```

**Features:**

- Real-time bug monitoring
- Bug categorization
- Detailed reporting

## Running Examples

1. Make sure you have a MUD server running on localhost:3939
2. Configure `config/config.yaml` with your server settings
3. Run the example:

```bash
# From project root
python examples/basic_connection.py

# Or make it executable first
chmod +x examples/basic_connection.py
./examples/basic_connection.py
```

## Creating Your Own Examples

Use this template to create new examples:

```python
#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ai_player.mcp_server import GameConnection

def main():
    conn = GameConnection()

    # Your code here
    conn.connect()
    conn.login("account", "password")
    # ...

    conn.disconnect()
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

## Contributing Examples

We welcome example contributions! Please:

1. Follow the existing code style
2. Add comments explaining what the example does
3. Update this README with your example
4. Submit a pull request
