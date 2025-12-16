# API Contract: RAG Chatbot for Physical AI & Humanoid Robotics Learning

## /chat endpoint

### POST /chat

**Description**: Process a user query against the full book content using semantic retrieval.

**Request**:
```json
{
  "query": "string, required - The user's question about the book content",
  "session_id": "string, optional - Session identifier for conversation history"
}
```

**Response (Success)**:
```json
{
  "response": "string - The AI-generated answer based on book content",
  "session_id": "string - The session identifier",
  "retrieved_context": [
    {
      "content": "string - The relevant book content used",
      "page_number": "integer - Page where content appears",
      "section_title": "string - Section title"
    }
  ],
  "confidence": "number - Confidence score between 0 and 1"
}
```

**Response (Refusal)**:
```json
{
  "response": "string - Explanation that answer cannot be provided from book content",
  "session_id": "string - The session identifier",
  "retrieved_context": [],
  "confidence": 0,
  "reason": "string - Reason for refusal (e.g., 'no relevant content found')"
}
```

**Response (Error)**:
```json
{
  "error": "string - Error message",
  "code": "string - Error code"
}
```

**Headers**:
- Content-Type: application/json
- Accept: application/json

## /chat/selected-text endpoint

### POST /chat/selected-text

**Description**: Process a user query against only the user-selected text.

**Request**:
```json
{
  "query": "string, required - The user's question about the selected text",
  "selected_text": "string, required - The text selected by the user",
  "session_id": "string, optional - Session identifier for conversation history"
}
```

**Response (Success)**:
```json
{
  "response": "string - The AI-generated answer based only on selected text",
  "session_id": "string - The session identifier",
  "retrieved_context": [
    {
      "content": "string - The relevant selected text used",
      "source": "string - Indicator that this is from selected text"
    }
  ],
  "confidence": "number - Confidence score between 0 and 1"
}
```

**Response (Refusal)**:
```json
{
  "response": "string - Explanation that answer cannot be provided from selected text",
  "session_id": "string - The session identifier",
  "retrieved_context": [],
  "confidence": 0,
  "reason": "string - Reason for refusal (e.g., 'no relevant content in selected text')"
}
```

**Response (Error)**:
```json
{
  "error": "string - Error message",
  "code": "string - Error code"
}
```

**Headers**:
- Content-Type: application/json
- Accept: application/json

## /health endpoint

### GET /health

**Description**: Check the health status of the RAG chatbot service.

**Request**: No request body required

**Response (Success)**:
```json
{
  "status": "string - 'healthy'",
  "timestamp": "string - ISO 8601 timestamp",
  "dependencies": {
    "qdrant": "string - Status of Qdrant connection (healthy/unhealthy)",
    "gemini": "string - Status of Gemini API connection (healthy/unhealthy)",
    "cohere": "string - Status of Cohere API connection (healthy/unhealthy)",
    "neon": "string - Status of Neon Postgres connection (healthy/unhealthy)"
  }
}
```

**Response (Error)**:
```json
{
  "status": "string - 'unhealthy'",
  "timestamp": "string - ISO 8601 timestamp",
  "error": "string - Error message",
  "dependencies": {
    "qdrant": "string - Status of Qdrant connection (healthy/unhealthy)",
    "gemini": "string - Status of Gemini API connection (healthy/unhealthy)",
    "cohere": "string - Status of Cohere API connection (healthy/unhealthy)",
    "neon": "string - Status of Neon Postgres connection (healthy/unhealthy)"
  }
}
```

**Headers**:
- Accept: application/json