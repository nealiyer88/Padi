"""Tests for page data models."""
import pytest
from pathlib import Path
import sys
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from padi.models.page_data import PageData


class TestPageData:
    """Test cases for PageData model."""
    
    def test_page_data_creation(self):
        """Test that PageData can be created with required fields."""
        page_data = PageData(
            page_num=1,
            page_type="text",
            text="Sample text content"
        )
        assert page_data.page_num == 1
        assert page_data.page_type == "text"
        assert page_data.text == "Sample text content"
    
    def test_page_data_defaults(self):
        """Test that PageData has correct default values."""
        page_data = PageData(
            page_num=1,
            page_type="text"
        )
        assert page_data.text == ""
        assert page_data.images == []
        assert page_data.ocr_confidence is None
        assert page_data.processing_time is None
        assert page_data.error_message is None
        assert isinstance(page_data.created_at, datetime)
