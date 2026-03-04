# Configuration Guide

## Configuration File Location

AI-Player looks for configuration in the following order:

1. Environment variable: `AI_PLAYER_CONFIG`
2. Default location: `config/config.yaml`
3. Built-in defaults

## Configuration Options

### Server Connection

```yaml
server:
  host: "localhost" # Server hostname or IP
  port: 3939 # Server port
  encoding: "utf-8" # Character encoding
  connect_timeout: 10 # Connection timeout in seconds
```

### Login Settings

```yaml
login:
  separator: "|" # Account/password separator
  default_gender: "Male"
  wait_time: 2 # Seconds to wait after login
  success_keywords: # Keywords indicating successful login
    - "Welcome"
    - "Success"
```

### Game State Detection

```yaml
game_state:
  room_markers:
    start: "[" # Room name start marker
    end: "]" # Room name end marker
```

### Logging

```yaml
logging:
  level: "INFO" # DEBUG, INFO, WARNING, ERROR
  file: "logs/ai_player.log"
  console: true
```

## Environment Variables

- `AI_PLAYER_CONFIG`: Path to config file
- `AI_PLAYER_DEBUG`: Enable debug mode (set to "1" or "true")

## Example Configurations

### Development

```yaml
debug: true
verbose: true
server:
  host: "localhost"
  port: 3939
```

### Production

```yaml
debug: false
verbose: false
server:
  host: "mud.example.com"
  port: 4000
execution:
  rate_limit: 5
```
