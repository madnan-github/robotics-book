from fastapi import APIRouter, HTTPException
from typing import Optional
import uuid
from models.user_query import QueryMode
from services.rag_service import rag_service
from core.security import generate_session_id
from core.constants import SELECTED_TEXT_TOP_K
from pydantic import BaseModel


router = APIRouter()


class SelectedTextRequest(BaseModel):
    query: str
    selected_text: str
    session_id: Optional[str] = None


class SelectedTextResponse(BaseModel):
    response: str
    session_id: str
    retrieved_context: list
    confidence: float


@router.post("/chat/selected-text", response_model=SelectedTextResponse)
async def selected_text_endpoint(request: SelectedTextRequest):
    """
    Process a user query against only the user-selected text
    """
    # Generate a session ID if not provided
    session_id = request.session_id or generate_session_id()

    try:
        # Process the query using the RAG service in selected-text mode
        result = await rag_service.process_query(
            query_text=request.query,
            query_mode=QueryMode.SELECTED_TEXT,
            selected_text=request.selected_text
        )

        # Add the session ID to the result
        result["session_id"] = session_id

        # If it's a refusal response, format it appropriately
        if result.get("refusal_response", False):
            return SelectedTextResponse(
                response=result["response"],
                session_id=session_id,
                retrieved_context=[],
                confidence=0.0
            )

        return SelectedTextResponse(
            response=result["response"],
            session_id=session_id,
            retrieved_context=result["retrieved_context"],
            confidence=result["confidence"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing selected text request: {str(e)}")


@router.post("/chat/selected-text-with-context", response_model=SelectedTextResponse)
async def selected_text_with_context_endpoint(request: SelectedTextRequest, top_k: Optional[int] = SELECTED_TEXT_TOP_K):
    """
    Process a user query against selected text with specific top_k parameter
    """
    session_id = request.session_id or generate_session_id()

    try:
        result = await rag_service.process_query(
            query_text=request.query,
            query_mode=QueryMode.SELECTED_TEXT,
            selected_text=request.selected_text,
            top_k=top_k
        )

        result["session_id"] = session_id

        if result.get("refusal_response", False):
            return SelectedTextResponse(
                response=result["response"],
                session_id=session_id,
                retrieved_context=[],
                confidence=0.0
            )

        return SelectedTextResponse(
            response=result["response"],
            session_id=session_id,
            retrieved_context=result["retrieved_context"],
            confidence=result["confidence"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing selected text request: {str(e)}")