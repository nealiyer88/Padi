"""Pydantic models for batch data."""
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from .page_data import PageData


class BatchData(BaseModel):
    """Model for batch data (multiple pages)."""
    
    batch_id: str = Field(..., description="Unique batch identifier")
    start_page: int = Field(..., description="First page number in batch")
    end_page: int = Field(..., description="Last page number in batch")
    pages: List[PageData] = Field(..., description="List of pages in this batch")
    merged_text: str = Field(default="", description="Combined text from all pages")
    total_images: int = Field(default=0, description="Total number of images in batch")
    processing_time: float = Field(default=0.0, description="Total time to process batch")
    created_at: datetime = Field(default_factory=datetime.now, description="Timestamp of creation")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
