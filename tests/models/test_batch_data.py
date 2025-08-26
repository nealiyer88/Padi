"""Tests for batch data models."""
import pytest
from pathlib import Path
import sys
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from padi.models.batch_data import BatchData
from padi.models.page_data import PageData


class TestBatchData:
    """Test cases for BatchData model."""
    
    def test_batch_data_creation(self):
        """Test that BatchData can be created with required fields."""
        pages = [
            PageData(page_num=1, page_type="text", text="Page 1"),
            PageData(page_num=2, page_type="text", text="Page 2")
        ]
        
        batch_data = BatchData(
            batch_id="batch_001",
            start_page=1,
            end_page=2,
            pages=pages
        )
        
        assert batch_data.batch_id == "batch_001"
        assert batch_data.start_page == 1
        assert batch_data.end_page == 2
        assert len(batch_data.pages) == 2
        assert batch_data.merged_text == ""
        assert batch_data.total_images == 0
        assert batch_data.processing_time == 0.0
        assert isinstance(batch_data.created_at, datetime)
