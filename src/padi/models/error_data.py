"""Pydantic models for error data."""
from pydantic import BaseModel, Field
from typing import Optional, Any
from datetime import datetime


class ErrorData(BaseModel):
    """Model for error information."""
    
    error_type: str = Field(..., description="Type of error that occurred")
    error_message: str = Field(..., description="Human-readable error message")
    error_code: Optional[str] = Field(None, description="Error code if applicable")
    page_number: Optional[int] = Field(None, description="Page number where error occurred")
    batch_id: Optional[str] = Field(None, description="Batch ID where error occurred")
    stack_trace: Optional[str] = Field(None, description="Stack trace if available")
    context: Optional[dict] = Field(None, description="Additional error context")
    timestamp: datetime = Field(default_factory=datetime.now, description="When the error occurred")
    
    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
