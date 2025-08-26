"""Configuration management for PADI."""
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from .platform_utils import get_platform_config


class ConfigManager:
    """Manages configuration loading and merging."""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config: Dict[str, Any] = {}
        self._load_config()
    
    def _load_config(self) -> None:
        """Load and merge configuration files."""
        # Load default config first
        default_config = self._load_yaml("config/default.yaml")
        if default_config:
            self.config.update(default_config)
        
        # Load platform-specific config and override defaults
        platform_config = self._load_yaml(get_platform_config())
        if platform_config:
            self.config.update(platform_config)
    
    def _load_yaml(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Load a YAML configuration file."""
        try:
            path = Path(file_path)
            if path.exists():
                with open(path, 'r', encoding='utf-8') as f:
                    return yaml.safe_load(f)
        except Exception as e:
            print(f"Warning: Could not load config file {file_path}: {e}")
        return None
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get a configuration value using dot notation."""
        keys = key.split('.')
        value = self.config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        
        return value
    
    def get_batch_size(self) -> int:
        """Get the configured batch size for PDF processing."""
        return self.get('pdf_processing.batch_size', 30)
    
    def get_merge_strategy(self) -> str:
        """Get the configured merge strategy."""
        return self.get('pdf_processing.merge_strategy', 'fixed')
    
    def get_output_directory(self) -> Path:
        """Get the base output directory."""
        base_dir = self.get('output.base_directory', 'digitized_output')
        return Path(base_dir)
    
    def get_ocr_confidence_threshold(self) -> float:
        """Get the OCR confidence threshold."""
        return self.get('ocr.confidence_threshold', 0.7)
