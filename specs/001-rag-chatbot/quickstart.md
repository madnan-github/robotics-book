# Quickstart: RAG Chatbot for Physical AI & Humanoid Robotics Learning

## Local Development Setup

### Prerequisites
- Python 3.11+
- pip package manager
- Git
- Access to API keys for:
  - Cohere (for embeddings)
  - Google Gemini (for generation)
  - Qdrant Cloud (vector database)
  - Neon Postgres (relational database)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the `backend/` directory with the following:
   ```env
   COHERE_API_KEY=your_cohere_api_key
   GEMINI_API_KEY=your_gemini_api_key
   QDRANT_URL=your_qdrant_cluster_url
   QDRANT_API_KEY=your_qdrant_api_key
   DATABASE_URL=your_neon_postgres_connection_string
   ```

5. **Index the book content**:
   ```bash
   python -m scripts.index_book_content
   ```

6. **Start the development server**:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### API Endpoints

- Health check: `GET http://localhost:8000/health`
- Full-book chat: `POST http://localhost:8000/chat`
- Selected-text chat: `POST http://localhost:8000/chat/selected-text`

### Example API Usage

**Full-book query**:
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain the concept of inverse kinematics in robotics",
    "session_id": "session-123"
  }'
```

**Selected-text query**:
```bash
curl -X POST http://localhost:8000/chat/selected-text \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What does this text say about sensor fusion?",
    "selected_text": "Sensor fusion is the process of combining data from multiple sensors to achieve better accuracy and reliability than could be achieved by using a single sensor alone. In robotics, this typically involves combining data from cameras, lidars, IMUs, and other sensors.",
    "session_id": "session-123"
  }'
```

## Testing

Run the test suite:
```bash
pytest tests/
```

Run specific test types:
```bash
# Unit tests
pytest tests/unit/

# Integration tests
pytest tests/integration/
```

## Deployment to Hugging Face

1. Create a Hugging Face Space or use the Inference API
2. Add the required environment variables in the Space settings
3. Push the code to the Hugging Face repository
4. The Space will automatically build and deploy the application

## Troubleshooting

- If the server doesn't start, check that all environment variables are properly set
- If queries return no results, verify that the book content was properly indexed
- For API errors, check the logs and ensure API keys are valid and have sufficient quota