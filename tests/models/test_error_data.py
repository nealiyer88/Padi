"""Tests for error data models."""
import pytest
from pathlib import Path
import sys
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

from padi.models.error_data import ErrorData


class TestErrorData:
    """Test cases for ErrorData model."""
    
    def test_error_data_creation(self):
        """Test that ErrorData can be created with required fields."""
        error_data = ErrorData(
            error_type="ValidationError",
            error_message="Invalid page number"
        )
        
        assert error_data.error_type == "ValidationError"
        assert error_data.error_message == "Invalid page number"
        assert error_data.error_code is None
        assert error_data.page_number is None
        assert error_data.batch_id is None
        assert error_data.stack_trace is None
        assert error_data.context is None
        assert isinstance(error_data.timestamp, datetime)
    
    def test_error_data_with_optional_fields(self):
        """Test that ErrorData can be created with optional fields."""
        error_data = ErrorData(
            error_type="ProcessingError",
            error_message="OCR failed",
            error_code="OCR_001",
            page_number=5,
            batch_id="batch_001",
            context={"ocr_confidence": 0.3}
        )
        
        assert error_data.error_code == "OCR_001"
        assert error_data.page_number == 5
        assert error_data.batch_id == "batch_001"
        assert error_data.context == {"ocr_confidence": 0.3}
