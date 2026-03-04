#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AI-Player MCP stdio Server
Standard MCP Protocol (stdio JSON-RPC)
Real-time TCP communication with MUD games
"""

import asyncio
import json
import socket
import threading
import time
import sys
import os
from typing import Optional, Dict, Any, List
from dataclasses import dataclass
from datetime import datetime
from queue import Queue, Empty
from enum import Enum
import re

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from utils.config_loader import config


# ============ Bug Type Definitions ============
class BugType(Enum):
    """Bug type enumeration"""
    RUNTIME_ERROR = "runtime_error"
    COMPILE_ERROR = "compile_error"
    LOGIC_ERROR = "logic_error"
    WARNING = "warning"
    UNKNOWN = "unknown"


@dataclass
class BugInfo:
    """Bug information data class"""
    type: BugType
    severity: str
    message: str
    source_file: Optional[str] = None
    line_number: Optional[int] = None
    timestamp: Optional[datetime] = None
    raw_log: str = ""
    
    def __post_init__(self):
        if self.timestamp is None:
            self.timestamp = datetime.now()


# ============ Enhanced TCP Connection Manager ============
class GameConnection:
    """TCP connection manager for MUD games"""

    def __init__(self):
        # Load settings from config
        server_config = config.get_server_config()
        self.host = server_config.get("host", "localhost")
        self.port = server_config.get("port", 3939)
        self.encoding = server_config.get("encoding", "utf-8")
        self.connect_timeout = server_config.get("connect_timeout", 10)
        self.auto_reconnect = server_config.get("auto_reconnect", True)
        self.reconnect_delay = server_config.get("reconnect_delay", 5)

        self.socket: Optional[socket.socket] = None
        self.connected = False
        self.logged_in = False
        self.message_queue: Queue = Queue()
        self.receive_thread: Optional[threading.Thread] = None
        self.running = False
        self.account: str = ""
        
        # Game state config
        game_state_config = config.get("game_state", {})
        initial_hp = game_state_config.get("initial_hp", 100)
        initial_mp = game_state_config.get("initial_mp", 100)
        
        self.game_state = {
            "room": "Unknown",
            "hp": initial_hp,
            "max_hp": initial_hp,
            "mp": initial_mp,
            "max_mp": initial_mp,
            "exits": [],
            "npcs": [],
            "items": [],
        }

        # Login config
        login_config = config.get_login_config()
        self.login_separator = login_config.get("separator", "|")
        self.default_gender = login_config.get("default_gender", "Male")
        self.login_wait_time = login_config.get("wait_time", 2)
        self.success_keywords = login_config.get(
            "success_keywords", ["Welcome", "Success", "Room", "Here"]
        )
        self.create_role_prompts = login_config.get(
            "create_role_prompts", ["Create", "Character"]
        )
        self.gender_prompts = login_config.get("gender_prompts", ["Gender"])
        
        # Bug detection
        self.recent_bugs: List[BugInfo] = []
        self.log_monitor_thread: Optional[threading.Thread] = None
        self.log_monitor_running = False
        self.last_log_position = 0

    def connect(self, host: Optional[str] = None, port: Optional[int] = None) -> bool:
        """Connect to game server"""
        host = host or self.host
        port = port or self.port

        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.settimeout(self.connect_timeout)
            self.socket.connect((host, port))
            self.socket.settimeout(0.1)
            self.connected = True
            self.running = True

            # Start receive thread
            self.receive_thread = threading.Thread(
                target=self._receive_loop, daemon=True
            )
            self.receive_thread.start()
            
            # Start log monitor
            self._start_log_monitor()

            if config.is_debug():
                print(f"[TCP] Connected to {host}:{port}", file=sys.stderr)

            return True
        except Exception as e:
            print(f"[TCP] Connection failed: {e}", file=sys.stderr)
            return False

    def _receive_loop(self):
        """Background receive loop"""
        buffer = ""
        while self.running:
            try:
                if not self.socket:
                    break
                data = self.socket.recv(4096)
                if not data:
                    break

                decoded = data.decode(self.encoding, errors="ignore")
                
                if config.is_debug():
                    print(f"[RAW] Received {len(decoded)} bytes", file=sys.stderr)

                buffer += decoded
                lines = buffer.split("\n")
                buffer = lines.pop()

                for line in lines:
                    if line.strip():
                        if config.is_debug():
                            print(f"[PARSED] {line.strip()[:100]}", file=sys.stderr)
                        self.message_queue.put(
                            {"time": datetime.now().isoformat(), "text": line.strip()}
                        )
                        self._parse_message(line.strip())

            except socket.timeout:
                continue
            except Exception as e:
                print(f"[TCP] Receive error: {e}", file=sys.stderr)
                break

        self.connected = False
        print("[TCP] Receive thread stopped", file=sys.stderr)

    def _parse_message(self, text: str):
        """Parse game message"""
        room_markers = config.get(
            "game_state.room_markers", {"start": "[", "end": "]"}
        )
        start_marker = room_markers.get("start", "[")
        end_marker = room_markers.get("end", "]")

        if start_marker in text and end_marker in text:
            try:
                self.game_state["room"] = text.split(start_marker)[1].split(end_marker)[0]
            except:
                pass

    def send(self, cmd: str) -> bool:
        """Send command"""
        if not self.socket or not self.connected:
            return False
        try:
            self.socket.sendall((cmd + "\n").encode(self.encoding))
            return True
        except:
            self.connected = False
            return False

    def get_messages(self, timeout: float = 0.5) -> List[Dict]:
        """Get messages"""
        messages = []
        deadline = time.time() + timeout
        while time.time() < deadline:
            try:
                remaining = deadline - time.time()
                if remaining <= 0:
                    break
                msg = self.message_queue.get(timeout=min(0.1, remaining))
                messages.append(msg)
            except Empty:
                continue
        return messages

    def login(self, account: str, password: str) -> bool:
        """Login to game"""
        if not self.connected:
            return False

        time.sleep(1)
        self.get_messages(1.0)

        self.send(f"{account}{self.login_separator}{password}")
        self.account = account

        time.sleep(self.login_wait_time)
        messages = self.get_messages(1.5)

        for msg in messages:
            text = msg.get("text", "")
            if any(kw in text for kw in self.success_keywords):
                self.logged_in = True
                return True
            if any(prompt in text for prompt in self.create_role_prompts):
                self.send(account)
                time.sleep(1)
                messages2 = self.get_messages(1.0)
                for m2 in messages2:
                    if any(gp in m2.get("text", "") for gp in self.gender_prompts):
                        self.send(self.default_gender)
                        time.sleep(1)
                        break
                self.logged_in = True
                return True

        if messages:
            self.logged_in = True
            return True

        return False

    def _start_log_monitor(self):
        """Start background log monitoring"""
        if self.log_monitor_running:
            return
        
        self.log_monitor_running = True
        self.log_monitor_thread = threading.Thread(
            target=self._monitor_logs, daemon=True
        )
        self.log_monitor_thread.start()
        print("[Bug Detection] Log monitoring started", file=sys.stderr)
    
    def _stop_log_monitor(self):
        """Stop log monitoring"""
        self.log_monitor_running = False
        if self.log_monitor_thread:
            self.log_monitor_thread.join(timeout=2)
        print("[Bug Detection] Log monitoring stopped", file=sys.stderr)
    
    def _monitor_logs(self):
        """Background log monitoring loop"""
        log_file = config.get_log_path("runtime")
        error_patterns = [
            (r"Error", BugType.RUNTIME_ERROR, "Runtime error"),
            (r"Exception", BugType.RUNTIME_ERROR, "Exception"),
            (r"Failed", BugType.RUNTIME_ERROR, "Operation failed"),
            (r"Undefined", BugType.RUNTIME_ERROR, "Undefined variable"),
            (r"Syntax", BugType.COMPILE_ERROR, "Syntax error"),
            (r"Warning", BugType.WARNING, "Warning"),
        ]
        
        while self.log_monitor_running:
            try:
                if os.path.exists(log_file):
                    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
                        f.seek(0, 2)
                        file_size = f.tell()
                        if file_size < self.last_log_position:
                            self.last_log_position = 0
                        
                        f.seek(self.last_log_position)
                        new_lines = f.readlines()
                        self.last_log_position = f.tell()
                    
                    for line in new_lines:
                        self._analyze_log_line(line, error_patterns)
                        
            except Exception as e:
                print(f"[Bug Detection] Monitor error: {e}", file=sys.stderr)
            
            time.sleep(1)
    
    def _analyze_log_line(self, line: str, patterns: list):
        """Analyze single log line"""
        for pattern, bug_type, desc in patterns:
            if re.search(pattern, line, re.IGNORECASE):
                source_file = None
                line_number = None
                file_match = re.search(r'([^\s]+\.\w+):(\d+)', line)
                if file_match:
                    source_file = file_match.group(1)
                    line_number = int(file_match.group(2))
                
                bug = BugInfo(
                    type=bug_type,
                    severity="high" if bug_type == BugType.RUNTIME_ERROR else "medium",
                    message=f"{desc}: {line[:80]}",
                    source_file=source_file,
                    line_number=line_number,
                    raw_log=line.strip()
                )
                
                self.recent_bugs.append(bug)
                print(f"[Bug Detection] {bug.message}", file=sys.stderr)
                break
    
    def get_recent_bugs(self, count: int = 5) -> List[Dict]:
        """Get recent bugs list"""
        bugs = self.recent_bugs[-count:]
        return [{
            "type": b.type.value,
            "severity": b.severity,
            "message": b.message,
            "source_file": b.source_file,
            "line_number": b.line_number,
            "timestamp": b.timestamp.isoformat() if b.timestamp else None
        } for b in bugs]

    def disconnect(self):
        """Disconnect from server"""
        self._stop_log_monitor()
        self.running = False
        self.connected = False
        self.logged_in = False
        if self.socket:
            try:
                self.socket.close()
            except:
                pass
            self.socket = None


# ============ Global Connection Instance ============
game_conn = GameConnection()


# ============ MCP stdio Server ============
class MCPStdioServer:
    """Standard MCP stdio server"""

    def __init__(self):
        self.tools = {
            "connect_server": self._tool_connect_server,
            "login_game": self._tool_login_game,
            "send_game_command": self._tool_send_game_command,
            "get_game_status": self._tool_get_game_status,
            "disconnect_server": self._tool_disconnect_server,
            "get_bug_report": self._tool_get_bug_report,
        }

        self.tools_definition = [
            {
                "name": "connect_server",
                "description": "Connect to MUD game server",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "host": {"type": "string", "description": "Server address, default: localhost"},
                        "port": {"type": "integer", "description": "Server port, default: 3939"},
                    },
                },
            },
            {
                "name": "login_game",
                "description": "Login to game (auto-register if account doesn't exist)",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "account": {"type": "string", "description": "Game account"},
                        "password": {"type": "string", "description": "Game password"},
                    },
                    "required": ["account", "password"],
                },
            },
            {
                "name": "send_game_command",
                "description": "Send game command (e.g., look, go north, inventory)",
                "inputSchema": {
                    "type": "object",
                    "properties": {"command": {"type": "string", "description": "Game command"}},
                    "required": ["command"],
                },
            },
            {
                "name": "get_game_status",
                "description": "Get current game status (connection, room, messages)",
                "inputSchema": {"type": "object", "properties": {}},
            },
            {
                "name": "disconnect_server",
                "description": "Disconnect from game server",
                "inputSchema": {"type": "object", "properties": {}},
            },
            {
                "name": "get_bug_report",
                "description": "Get auto-detected bug reports",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "count": {"type": "integer", "description": "Number of recent bugs, default: 5"}
                    }
                },
            },
        ]

    def _send_response(self, response: Dict):
        """Send JSON-RPC response"""
        json_str = json.dumps(response, ensure_ascii=False)
        sys.stdout.write(json_str + "\n")
        sys.stdout.flush()

    def _tool_connect_server(self, args: Dict) -> List[Dict]:
        """Connect to server"""
        host = args.get("host") or game_conn.host
        port = args.get("port") or game_conn.port

        if game_conn.connected:
            return [{"type": "text", "text": f"Already connected to {host}:{port}"}]

        success = game_conn.connect(host, port)
        if success:
            return [{"type": "text", "text": f"Successfully connected to {host}:{port}"}]
        else:
            return [{"type": "text", "text": "Connection failed"}]

    def _tool_login_game(self, args: Dict) -> List[Dict]:
        """Login to game"""
        account = args.get("account", "")
        password = args.get("password", "")

        if not game_conn.connected:
            return [{"type": "text", "text": "Not connected to server"}]

        success = game_conn.login(account, password)
        if success:
            return [{"type": "text", "text": f"Account {account} logged in"}]
        else:
            return [{"type": "text", "text": "Login failed"}]

    def _tool_send_game_command(self, args: Dict) -> List[Dict]:
        """Send game command"""
        command = args.get("command", "")
        
        if not game_conn.connected:
            return [{"type": "text", "text": "Not connected to server"}]
        
        game_conn.get_messages(0.1)
        
        success = game_conn.send(command)
        if not success:
            return [{"type": "text", "text": "Send failed"}]
        
        time.sleep(0.3)
        all_messages = []
        
        for _ in range(6):
            messages = game_conn.get_messages(0.5)
            all_messages.extend(messages)
            if messages:
                time.sleep(0.3)
            else:
                break
        
        result_text = f"Command: {command}\n"
        result_text += "-" * 40 + "\n"
        
        if all_messages:
            for msg in all_messages[:10]:
                result_text += f"  {msg['text']}\n"
        else:
            result_text += "  (No response)\n"
        
        return [{"type": "text", "text": result_text}]

    def _tool_get_game_status(self, args: Dict) -> List[Dict]:
        """Get game status"""
        messages = game_conn.get_messages(0.2)

        status_text = f"""Connection: {'Connected' if game_conn.connected else 'Disconnected'}
Login: {'Logged in' if game_conn.logged_in else 'Not logged in'}
Account: {game_conn.account or 'None'}
Room: {game_conn.game_state.get('room', 'Unknown')}"""

        if messages:
            status_text += "\n\nRecent Messages:\n"
            for msg in messages[-3:]:
                status_text += f"  {msg['text']}\n"

        return [{"type": "text", "text": status_text.strip()}]

    def _tool_disconnect_server(self, args: Dict) -> List[Dict]:
        """Disconnect from server"""
        game_conn.disconnect()
        return [{"type": "text", "text": "Disconnected"}]

    def _tool_get_bug_report(self, args: Dict) -> List[Dict]:
        """Get bug report"""
        count = args.get("count", 5)
        bugs = game_conn.get_recent_bugs(count)
        
        if not bugs:
            return [{"type": "text", "text": "No bugs detected"}]
        
        report = "Bug Detection Report\n"
        report += "=" * 50 + "\n"
        
        for i, bug in enumerate(bugs):
            report += f"\n[{i+1}] {bug['type']} ({bug['severity']})\n"
            report += f"    Message: {bug['message']}\n"
            if bug['source_file']:
                report += f"    Location: {bug['source_file']}"
                if bug['line_number']:
                    report += f":{bug['line_number']}"
                report += "\n"
            report += f"    Time: {bug['timestamp']}\n"
        
        report += f"\nTotal: {len(bugs)} bugs"
        return [{"type": "text", "text": report}]

    async def run(self):
        """Run MCP stdio server"""
        print("[MCP] AI-Player MCP stdio server started", file=sys.stderr)
        print(f"[MCP] Tools: {len(self.tools)}", file=sys.stderr)

        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break

                request = json.loads(line)
                method = request.get("method", "")
                request_id = request.get("id")

                if method == "initialize":
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "result": {
                            "protocolVersion": "2024-11-05",
                            "capabilities": {"tools": {}},
                            "serverInfo": {
                                "name": "ai-player-mud",
                                "version": "1.0.0",
                                "description": "AI-powered MUD game testing tool",
                            },
                        },
                    }
                    self._send_response(response)

                    tools_response = {
                        "jsonrpc": "2.0",
                        "method": "notifications/tools/list_changed",
                        "params": {"tools": self.tools_definition},
                    }
                    self._send_response(tools_response)

                elif method == "tools/list":
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "result": {"tools": self.tools_definition},
                    }
                    self._send_response(response)

                elif method == "tools/call":
                    tool_name = request.get("params", {}).get("name", "")
                    tool_args = request.get("params", {}).get("arguments", {})

                    if tool_name in self.tools:
                        try:
                            result = self.tools[tool_name](tool_args)
                            response = {
                                "jsonrpc": "2.0",
                                "id": request_id,
                                "result": {"content": result, "isError": False},
                            }
                        except Exception as e:
                            response = {
                                "jsonrpc": "2.0",
                                "id": request_id,
                                "result": {
                                    "content": [{"type": "text", "text": f"Error: {str(e)}"}],
                                    "isError": True,
                                },
                            }
                    else:
                        response = {
                            "jsonrpc": "2.0",
                            "id": request_id,
                            "result": {
                                "content": [{"type": "text", "text": f"Unknown tool: {tool_name}"}],
                                "isError": True,
                            },
                        }
                    self._send_response(response)

                elif method == "notifications/initialized":
                    pass

                else:
                    response = {
                        "jsonrpc": "2.0",
                        "id": request_id,
                        "error": {"code": -32601, "message": f"Unknown method: {method}"},
                    }
                    self._send_response(response)

            except json.JSONDecodeError as e:
                response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {"code": -32700, "message": f"JSON parse error: {str(e)}"},
                }
                self._send_response(response)
            except Exception as e:
                print(f"[MCP] Error: {e}", file=sys.stderr)
                break


if __name__ == "__main__":
    server = MCPStdioServer()
    asyncio.run(server.run())
