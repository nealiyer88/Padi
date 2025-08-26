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


class BatchData(BaseModel):
    """Model for batch data (multiple pages)."""
    
    batch_id: str = Field(..., description="Unique batch identifier")
    start_page: int = Field(..., description="First page number in batch")
    end_page: int = Field(..., description="Last page number in batch")
    pages: List[PageData] = Field(..., description="List of pages in this batch")
    merged_text: str = Field(default="", description="Combined text from all pages")
    total_images: int = Field(default=0, description="Total number of images in batch")
    processing_time: Optional[float] = Field(None, description="Total time to process batch")
    created_at: datetime = Field(default_factory=datetime.now, description="Timestamp of creation")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
