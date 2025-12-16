# Research: RAG Chatbot for Physical AI & Humanoid Robotics Learning

## Decision: Chunk Size and Overlap for Book Content

**Rationale**: For the Physical AI & Humanoid Robotics Learning book, we need to balance context preservation with retrieval precision. Smaller chunks may break up related concepts, while larger chunks may dilute relevance.

**Choice**: 512-token chunks with 64-token overlap
- This preserves paragraphs and related concepts while allowing for precise retrieval
- 64-token overlap ensures concepts spanning chunk boundaries are preserved
- Standard size that works well with Cohere embeddings and Qdrant storage

**Alternatives considered**:
- 256-token chunks: Might break up important concepts and explanations
- 1024-token chunks: Might dilute relevance for specific queries
- Sentence-level chunks: Could break up important technical explanations

## Decision: Top-k Retrieval Value

**Rationale**: Need to balance retrieval accuracy with performance. Too few results might miss relevant content, too many might dilute the context or slow down generation.

**Choice**: Top-5 retrieval for full-book mode, Top-3 for selected-text mode
- For full-book: 5 results provides good coverage while maintaining performance
- For selected-text: 3 results keeps focus on the specific text user selected
- These values can be adjusted based on testing results

**Alternatives considered**:
- Top-3 for both: Might miss relevant content in full-book mode
- Top-10: Could slow down generation and introduce noise
- Dynamic k-value: Would add complexity without clear benefit initially

## Decision: Selected-Text Enforcement Logic

**Rationale**: The system must strictly answer only from user-selected text when in selected-text mode, which requires a specific enforcement mechanism.

**Choice**: Context filtering approach
- When in selected-text mode, filter retrieved results to only include chunks from the user-provided text
- Use content similarity matching to ensure retrieved chunks are from the selected text
- If no relevant content from selected text is found, return refusal response
- This ensures strict adherence to selected-text-only requirement

**Alternatives considered**:
- Separate vector index for selected text: Would require real-time index creation
- Post-retrieval validation: Could be less efficient than filtering approach
- Simple keyword matching: Would be less reliable than embedding-based approach

## Decision: Gemini Configuration

**Rationale**: Need to configure Gemini for optimal response quality while ensuring it respects the RAG constraints.

**Choice**: Gemini Pro (gemini-pro) model with specific safety settings
- Temperature: 0.3 (balances creativity with factual accuracy)
- Safety settings: Set to BLOCK_ONLY_HIGH to prevent inappropriate responses
- Max output tokens: 1024 (allows detailed explanations)
- System instruction: Include clear instructions to only use provided context and refuse when context is insufficient

**Alternatives considered**:
- Gemini Flash: Faster but potentially less accurate for technical content
- Higher temperature: Could lead to more hallucinations
- Different safety settings: Could be too restrictive or permissive

## Decision: Qdrant and Neon Schema Design

**Rationale**: Need efficient schemas for both vector storage (Qdrant) and relational data (Neon).

**Choice**:
For Qdrant:
- Collection: "book_content"
- Vectors: Cohere embeddings (1024 dimensions)
- Payload: {"content": text, "page_number": int, "section_title": string, "source_file": string, "chunk_id": string}
- HNSW index for fast similarity search

For Neon Postgres:
- Table: chat_sessions
- Columns: id, session_id, user_query, retrieved_context, generated_response, timestamp, mode (full_book/selected_text)
- Table: book_metadata
- Columns: id, title, author, page_count, total_chunks, indexed_at

**Alternatives considered**:
- Different vector dimensions: Would require different embedding models
- Alternative vector DBs: Qdrant was required by constitution
- Different payload structures: This provides necessary metadata for debugging and analytics

## Decision: Agent Architecture Pattern

**Rationale**: Need to decide how to implement the agent orchestration using OpenAI Agents SDK or ChatKit SDK.

**Choice**: Direct RAG implementation with FastAPI services rather than complex agent orchestration
- While the constitution requires OpenAI Agents SDK or ChatKit SDK, the core functionality can be implemented with services
- Use the SDK for conversation management and state tracking
- Keep the RAG pipeline as direct service calls for better control and monitoring
- This allows for the required refusal behavior and selected-text enforcement

**Alternatives considered**:
- Full agent orchestration: Could be overkill for this use case
- Simple function calling: Might not provide enough state management
- Rule-based system: Would be less flexible than service-based approach