"""Pydantic models for page data."""
from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


class PageData(BaseModel):
    """Model for individual page data."""
    
    page_num: int = Field(..., description="Page number (1-indexed)")
    page_type: Literal["text", "image", "mixed"] = Field(..., description="Type of page content")
    text: str = Field(default="", description="Extracted text content")
    images: List[str] = Field(default_factory=list, description="List of image filenames")
    ocr_confidence: Optional[float] = Field(None, description="OCR confidence score (0.0-1.0)")
    processing_time: Optional[float] = Field(None, description="Time taken to process page (seconds)")
    error_message: Optional[str] = Field(None, description="Error message if processing failed")
    created_at: datetime = Field(default_factory=datetime.now, description="Timestamp of creation")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
