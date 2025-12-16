from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class QueryMode(str, Enum):
    FULL_BOOK = "full_book"
    SELECTED_TEXT = "selected_text"


class UserQuery(BaseModel):
    query_id: str
    session_id: str
    query_text: str = Field(..., min_length=1, description="The actual question asked by the user")
    query_mode: QueryMode
    selected_text: Optional[str] = Field(default=None, description="Text selected by user (if in selected_text mode)")
    timestamp: datetime = Field(default_factory=datetime.now)

    class Config:
        use_enum_values = True

    def model_post_init(self, __context):
        if self.query_mode == QueryMode.SELECTED_TEXT and not self.selected_text:
            raise ValueError("selected_text is required when query_mode is 'selected_text'")


class SelectedText(UserQuery):
    """
    Extending UserQuery for selected-text-specific functionality
    """
    pass