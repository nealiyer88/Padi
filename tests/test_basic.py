"""Basic tests to verify project structure."""
import pytest
from pathlib import Path
import sys

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from padi.utils.platform_utils import get_platform_info, is_windows, is_mac, is_linux
from padi.utils.config_manager import ConfigManager


def test_platform_utils():
    """Test platform utilities work correctly."""
    platform_info = get_platform_info()
    
    assert "system" in platform_info
    assert "release" in platform_info
    assert "python_version" in platform_info
    
    # Test platform detection functions
    assert isinstance(is_windows(), bool)
    assert isinstance(is_mac(), bool)
    assert isinstance(is_linux(), bool)


def test_config_manager():
    """Test configuration manager loads correctly."""
    config = ConfigManager()
    
    # Test basic config access
    batch_size = config.get_batch_size()
    assert isinstance(batch_size, int)
    assert batch_size > 0
    
    merge_strategy = config.get_merge_strategy()
    assert merge_strategy in ["fixed", "chapter"]


def test_project_structure():
    """Test that all required directories and files exist."""
    project_root = Path(__file__).parent.parent
    
    # Check main directories
    assert (project_root / "src" / "padi").exists()
    assert (project_root / "config").exists()
    assert (project_root / "tests").exists()
    
    # Check main files
    assert (project_root / "src" / "padi" / "__init__.py").exists()
    assert (project_root / "config" / "default.yaml").exists()
    assert (project_root / "pyproject.toml").exists()


if __name__ == "__main__":
    pytest.main([__file__])
