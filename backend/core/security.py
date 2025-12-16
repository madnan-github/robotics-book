import hashlib
import secrets
from typing import Optional
from datetime import datetime, timedelta
from fastapi import HTTPException, status


def generate_session_id() -> str:
    """
    Generate a unique session ID for chat sessions
    """
    return f"session_{secrets.token_urlsafe(16)}"


def validate_api_key(api_key: str) -> bool:
    """
    Validate an API key format (basic validation)
    """
    if not api_key or len(api_key) < 10:
        return False
    return True


def hash_content(content: str) -> str:
    """
    Create a hash of content for identifying unique chunks
    """
    return hashlib.sha256(content.encode()).hexdigest()


def sanitize_input(user_input: str) -> str:
    """
    Basic sanitization of user input
    """
    if not user_input:
        return ""

    # Strip whitespace and limit length
    sanitized = user_input.strip()

    # Additional sanitization could be added here
    return sanitized


def check_content_relevance(content: str, query: str) -> bool:
    """
    Basic check for content relevance (placeholder - implement more sophisticated logic as needed)
    """
    if not content or not query:
        return False

    # Simple keyword overlap check as a basic relevance indicator
    content_lower = content.lower()
    query_lower = query.lower()

    query_words = query_lower.split()
    matching_words = [word for word in query_words if word in content_lower]

    # If at least 30% of query words appear in content, consider it relevant
    if len(query_words) == 0:
        return False

    relevance_ratio = len(matching_words) / len(query_words)
    return relevance_ratio >= 0.3