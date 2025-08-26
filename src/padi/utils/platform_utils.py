"""Platform utilities for cross-platform compatibility."""
import platform
import sys
from pathlib import Path
from typing import Dict, Any


def get_platform_info() -> Dict[str, Any]:
    """Get detailed platform information."""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
    }


def get_platform_config() -> str:
    """Get the appropriate configuration file for the current platform."""
    system = platform.system().lower()
    
    if system == "darwin":
        return "config/mac.yaml"
    elif system == "windows":
        return "config/windows.yaml"
    elif system == "linux":
        return "config/linux.yaml"
    else:
        return "config/default.yaml"


def get_platform_paths() -> Dict[str, Path]:
    """Get platform-specific path configurations."""
    system = platform.system().lower()
    
    if system == "windows":
        return {
            "temp_dir": Path("C:/temp"),
            "user_home": Path.home(),
            "separator": "\\"
        }
    else:
        return {
            "temp_dir": Path("/tmp"),
            "user_home": Path.home(),
            "separator": "/"
        }


def is_windows() -> bool:
    """Check if running on Windows."""
    return platform.system().lower() == "windows"


def is_mac() -> bool:
    """Check if running on macOS."""
    return platform.system().lower() == "darwin"


def is_linux() -> bool:
    """Check if running on Linux."""
    return platform.system().lower() == "linux"
