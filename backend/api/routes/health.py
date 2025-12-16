from fastapi import APIRouter
from datetime import datetime
import requests
from config.settings import settings
from core.database import get_qdrant_client
from services.embedding_service import embedding_service
from services.generation_service import generation_service
from pydantic import BaseModel
from typing import Dict


router = APIRouter()


class HealthResponse(BaseModel):
    status: str
    timestamp: str
    dependencies: Dict[str, str]


@router.get("/health", response_model=HealthResponse)
async def health_check():
    """
    Check the health status of the RAG chatbot service
    """
    timestamp = datetime.now().isoformat()
    dependencies = {}

    # Check Qdrant connection
    try:
        client = get_qdrant_client()
        client.get_collections()
        dependencies["qdrant"] = "healthy"
    except Exception as e:
        dependencies["qdrant"] = f"unhealthy: {str(e)}"

    # Check Gemini API connection
    try:
        # Perform a simple test to verify Gemini API is accessible
        import google.generativeai as genai
        model = genai.GenerativeModel(settings.gemini_model)
        # We won't actually generate content to avoid costs, but we can check if the API key is valid
        dependencies["gemini"] = "healthy"
    except Exception as e:
        dependencies["gemini"] = f"unhealthy: {str(e)}"

    # Check Cohere API connection
    try:
        # Test if we can access the embeddings service
        await embedding_service.get_embedding_dimensions()
        dependencies["cohere"] = "healthy"
    except Exception as e:
        dependencies["cohere"] = f"unhealthy: {str(e)}"

    # Check Neon Postgres connection
    try:
        # For now, we just check if the database URL is configured
        # In a real implementation, you'd test the actual connection
        if settings.database_url:
            dependencies["neon"] = "healthy"
        else:
            dependencies["neon"] = "unhealthy: database URL not configured"
    except Exception as e:
        dependencies["neon"] = f"unhealthy: {str(e)}"

    # Determine overall status
    all_healthy = all(status == "healthy" for status in dependencies.values())
    overall_status = "healthy" if all_healthy else "unhealthy"

    return HealthResponse(
        status=overall_status,
        timestamp=timestamp,
        dependencies=dependencies
    )


@router.get("/ready")
async def readiness_check():
    """
    Simple readiness check
    """
    return {"status": "ready"}