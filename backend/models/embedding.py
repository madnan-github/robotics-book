from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime


class RetrievedContext(BaseModel):
    retrieval_id: str
    query_id: str
    retrieved_chunks: List[Dict] = Field(..., description="List of relevant book content chunks")
    similarity_scores: List[float] = Field(..., description="List of similarity scores for each chunk")
    retrieval_timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        json_schema_extra = {
            "example": {
                "retrieval_id": "retrieval_123",
                "query_id": "query_456",
                "retrieved_chunks": [
                    {
                        "content": "The content of the retrieved chunk...",
                        "page_number": 42,
                        "section_title": "Introduction to Robotics"
                    }
                ],
                "similarity_scores": [0.85, 0.72, 0.68]
            }
        }

    def model_post_init(self, __context):
        if len(self.retrieved_chunks) != len(self.similarity_scores):
            raise ValueError("Number of retrieved chunks must match number of similarity scores")


class BookMetadata(BaseModel):
    metadata_id: str
    book_title: str = Field(..., min_length=1, description="Title of the book")
    author: str = Field(..., min_length=1, description="Author of the book")
    page_count: int = Field(..., gt=0, description="Total number of pages in the book")
    total_chunks: int = Field(..., gt=0, description="Total number of content chunks in the system")
    indexed_at: datetime
    source_path: str = Field(..., min_length=1, description="Path to the original book content")

    class Config:
        json_schema_extra = {
            "example": {
                "metadata_id": "meta_789",
                "book_title": "Physical AI & Humanoid Robotics Learning",
                "author": "Author Name",
                "page_count": 350,
                "total_chunks": 120,
                "indexed_at": "2025-12-16T10:00:00Z",
                "source_path": "/path/to/book/source"
            }
        }