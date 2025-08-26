"""Tests for configuration utilities."""
import pytest
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from padi.utils.config import ConfigManager


class TestConfigManager:
    """Test cases for ConfigManager."""
    
    def test_config_manager_creation(self):
        """Test that ConfigManager can be instantiated."""
        config = ConfigManager()
        assert config.config_dir == Path("config")
    
    def test_get_batch_size(self):
        """Test that batch size can be retrieved."""
        config = ConfigManager()
        batch_size = config.get_batch_size()
        assert isinstance(batch_size, int)
        assert batch_size > 0
    
    def test_get_merge_strategy(self):
        """Test that merge strategy can be retrieved."""
        config = ConfigManager()
        strategy = config.get_merge_strategy()
        assert strategy in ["fixed", "chapter"]
