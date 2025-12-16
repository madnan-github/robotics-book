from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


class ChatSession(BaseModel):
    session_id: str
    created_at: datetime
    updated_at: datetime
    active: bool = True
    user_id: Optional[str] = None


class HealthCheck(BaseModel):
    status: str
    timestamp: str
    dependencies: dict


class GeneratedResponse(BaseModel):
    response_id: str
    query_id: str
    generated_text: str
    confidence_score: float
    refusal_response: bool
    generation_timestamp: datetime
    response_metadata: dict