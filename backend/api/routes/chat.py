from fastapi import APIRouter, HTTPException, Depends
from typing import Optional
import uuid
from models.user_query import UserQuery, QueryMode
from models.chat import GeneratedResponse
from services.rag_service import rag_service
from core.security import generate_session_id
from core.constants import DEFAULT_TOP_K
from pydantic import BaseModel


router = APIRouter()


class ChatRequest(BaseModel):
    query: str
    session_id: Optional[str] = None


class ChatResponse(BaseModel):
    response: str
    session_id: str
    retrieved_context: list
    confidence: float


@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Process a user query against the full book content using semantic retrieval
    """
    # Generate a session ID if not provided
    session_id = request.session_id or generate_session_id()

    try:
        # Process the query using the RAG service
        result = await rag_service.process_query(
            query_text=request.query,
            query_mode=QueryMode.FULL_BOOK
        )

        # Add the session ID to the result
        result["session_id"] = session_id

        # If it's a refusal response, format it appropriately
        if result.get("refusal_response", False):
            return ChatResponse(
                response=result["response"],
                session_id=session_id,
                retrieved_context=[],
                confidence=0.0
            )

        return ChatResponse(
            response=result["response"],
            session_id=session_id,
            retrieved_context=result["retrieved_context"],
            confidence=result["confidence"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")


@router.post("/chat-with-context", response_model=ChatResponse)
async def chat_with_context_endpoint(request: ChatRequest, top_k: Optional[int] = DEFAULT_TOP_K):
    """
    Process a user query with specific top_k parameter for retrieval
    """
    session_id = request.session_id or generate_session_id()

    try:
        result = await rag_service.process_query(
            query_text=request.query,
            query_mode=QueryMode.FULL_BOOK,
            top_k=top_k
        )

        result["session_id"] = session_id

        if result.get("refusal_response", False):
            return ChatResponse(
                response=result["response"],
                session_id=session_id,
                retrieved_context=[],
                confidence=0.0
            )

        return ChatResponse(
            response=result["response"],
            session_id=session_id,
            retrieved_context=result["retrieved_context"],
            confidence=result["confidence"]
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing chat request: {str(e)}")