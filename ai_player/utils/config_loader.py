#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置加载器
加载并管理 ai-player 的 YAML 配置
"""

import os
import yaml
from typing import Any, Dict, Optional

# 配置文件路径
DEFAULT_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "config", "config.yaml"
)

# 项目根目录（用于解析相对路径）
PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

# 默认配置（当配置文件不存在时使用）
DEFAULT_CONFIG = {
    "test_mode": True,
    "debug": True,
    "verbose": True,
    "server": {
        "host": "localhost",
        "port": 3939,
        "connect_timeout": 10,
        "encoding": "utf-8",
        "auto_reconnect": True,
        "reconnect_delay": 5,
        "max_reconnect_attempts": 3,
    },
    "login": {
        "separator": "║",
        "default_gender": "男",
        "wait_time": 2,
        "success_keywords": ["欢迎", "成功", "房间", "这里", "XKTITL"],
        "create_role_prompts": ["创建", "角色名"],
        "gender_prompts": ["性别", "gender"],
    },
    "game_state": {
        "room_markers": {"start": "【", "end": "】"},
        "initial_hp": 100,
        "initial_mp": 100,
    },
    "logging": {
        "runtime_log": "server/data/log/runtime.log",
        "compile_log": "server/data/log/compile.log",
        "driver_log": "server/data/log/driver.log",
        "level": "INFO",
    },
    "error_detection": {
        "keywords": ["错误", "Error", "failed", "FAIL", "执行时段错误", "Undefined"],
    },
}


class ConfigLoader:
    """配置加载器类"""

    _instance = None
    _config = None

    def __new__(cls):
        """单例模式"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        """加载配置文件"""
        config_path = os.environ.get("AI_PLAYER_CONFIG", DEFAULT_CONFIG_PATH)

        if os.path.exists(config_path):
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    self._config = yaml.safe_load(f)
            except Exception as e:
                print(f"[Config] 加载配置文件失败: {e}，使用默认配置")
                self._config = DEFAULT_CONFIG
        else:
            print(f"[Config] 配置文件不存在: {config_path}，使用默认配置")
            self._config = DEFAULT_CONFIG

    def get(self, key: str, default: Any = None) -> Any:
        """
        获取配置项
        支持点号分隔的路径，如 "server.host"
        """
        keys = key.split(".")
        value = self._config

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default

        return value

    def get_server_config(self) -> Dict[str, Any]:
        """获取服务器配置"""
        return self.get("server", DEFAULT_CONFIG["server"])

    def get_login_config(self) -> Dict[str, Any]:
        """获取登录配置"""
        return self.get("login", DEFAULT_CONFIG["login"])

    def get_log_path(self, log_type: str = "runtime") -> str:
        """
        获取日志文件完整路径

        Args:
            log_type: 日志类型 (runtime, compile, driver)

        Returns:
            日志文件的绝对路径
        """
        relative_path = self.get(
            f"logging.{log_type}_log", f"server/data/log/{log_type}.log"
        )

        # 如果是绝对路径，直接返回
        if os.path.isabs(relative_path):
            return os.path.normpath(relative_path)

        # 相对路径，基于项目根目录
        return os.path.normpath(os.path.join(PROJECT_ROOT, relative_path))

    def get_error_keywords(self) -> list:
        """获取错误检测关键词"""
        return self.get(
            "error_detection.keywords", DEFAULT_CONFIG["error_detection"]["keywords"]
        )

    def is_debug(self) -> bool:
        """是否调试模式"""
        return self.get("debug", DEFAULT_CONFIG["debug"])

    def get_all_config(self) -> Dict[str, Any]:
        """获取完整配置"""
        return self._config
    
    def get_project_root(self) -> str:
        """获取项目根目录"""
        return PROJECT_ROOT
    
    def get_server_path(self, subpath: str = "") -> str:
        """
        获取服务器目录路径
        
        Args:
            subpath: 子路径（如 "bin/start.bat"）
        
        Returns:
            完整路径
        """
        server_dir = self.get("paths.server_dir", "server")
        base_path = os.path.join(PROJECT_ROOT, server_dir)
        
        if subpath:
            return os.path.normpath(os.path.join(base_path, subpath))
        return os.path.normpath(base_path)
    
    def get_startup_script(self, platform: str = "windows") -> str:
        """
        获取启动脚本路径
        
        Args:
            platform: 平台 (windows, linux)
        
        Returns:
            启动脚本的完整路径
        """
        script_path = self.get(f"paths.startup_scripts.{platform}", f"server/bin/start.{platform[:3]}")
        
        if os.path.isabs(script_path):
            return os.path.normpath(script_path)
        return os.path.normpath(os.path.join(PROJECT_ROOT, script_path))
    
    def get_log_dir(self) -> str:
        """获取日志目录路径"""
        log_dir = self.get("paths.log_dir", "server/data/log")
        
        if os.path.isabs(log_dir):
            return os.path.normpath(log_dir)
        return os.path.normpath(os.path.join(PROJECT_ROOT, log_dir))


# 全局配置实例
config = ConfigLoader()

if __name__ == "__main__":
    # 测试配置加载
    print("=== 配置加载测试 ===")
    print(f"项目根目录: {config.get_project_root()}")
    print(f"服务器目录: {config.get_server_path()}")
    print(f"启动脚本: {config.get_startup_script('windows')}")
    print(f"日志目录: {config.get_log_dir()}")
    print(f"运行时日志: {config.get_log_path('runtime')}")
    print(f"编译日志: {config.get_log_path('compile')}")
    print(f"错误关键词: {config.get_error_keywords()}")
    print()
    print("✅ 所有配置项加载成功！")
