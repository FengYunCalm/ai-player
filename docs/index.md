# AI-Player Documentation

Welcome to the AI-Player documentation!

## Table of Contents

1. [Getting Started](#getting-started)
2. [Configuration](#configuration)
3. [API Reference](#api-reference)
4. [Test Scenarios](#test-scenarios)
5. [Bug Fix Patterns](#bug-fix-patterns)
6. [Troubleshooting](#troubleshooting)

## Getting Started

### Installation

```bash
pip install ai-player-mud
```

### Quick Start

```python
from ai_player import GameConnection

conn = GameConnection()
conn.connect("localhost", 3939)
conn.login("test", "test123")
conn.send("look")
messages = conn.get_messages()
conn.disconnect()
```

## Configuration

See [Configuration Guide](configuration.md) for detailed configuration options.

## API Reference

See [API Reference](api.md) for complete API documentation.

## Test Scenarios

See [Test Scenarios](test-scenarios.md) for predefined test scenarios.

## Bug Fix Patterns

See [Bug Fix Patterns](bug-fix-patterns.md) for supported bug fixes.

## Troubleshooting

See [Troubleshooting](troubleshooting.md) for common issues and solutions.
