# Data Model: RAG Chatbot for Physical AI & Humanoid Robotics Learning

## Book Content Entity

**Fields**:
- `chunk_id`: Unique identifier for each text chunk
- `content`: The actual text content from the book
- `page_number`: Page number where the content appears in the book
- `section_title`: Title of the section containing this content
- `source_file`: Original source file name
- `embedding`: Vector representation of the content (stored in Qdrant)
- `created_at`: Timestamp when the chunk was created
- `updated_at`: Timestamp when the chunk was last updated

**Validation Rules**:
- `content` must not be empty
- `chunk_id` must be unique
- `page_number` must be positive integer

## User Query Entity

**Fields**:
- `query_id`: Unique identifier for the query
- `session_id`: Identifier for the chat session
- `query_text`: The actual question asked by the user
- `query_mode`: Either "full_book" or "selected_text"
- `selected_text`: Text selected by user (if in selected_text mode)
- `timestamp`: When the query was submitted

**Validation Rules**:
- `query_text` must not be empty
- `query_mode` must be one of the allowed values
- If `query_mode` is "selected_text", `selected_text` must not be empty

## Retrieved Context Entity

**Fields**:
- `retrieval_id`: Unique identifier for the retrieval
- `query_id`: Reference to the associated query
- `retrieved_chunks`: List of relevant book content chunks
- `similarity_scores`: List of similarity scores for each chunk
- `retrieval_timestamp`: When the retrieval was performed

**Validation Rules**:
- `retrieved_chunks` must not be empty
- Each chunk in `retrieved_chunks` must exist in the Book Content entity

## Generated Response Entity

**Fields**:
- `response_id`: Unique identifier for the response
- `query_id`: Reference to the associated query
- `generated_text`: The AI-generated response
- `confidence_score`: Confidence level of the response (0.0-1.0)
- `refusal_response`: Boolean indicating if this is a refusal response
- `generation_timestamp`: When the response was generated
- `response_metadata`: Additional metadata about the generation process

**Validation Rules**:
- `generated_text` must not be empty if `refusal_response` is false
- `confidence_score` must be between 0.0 and 1.0
- If no relevant context was found, `refusal_response` must be true

## Chat Session Entity

**Fields**:
- `session_id`: Unique identifier for the chat session
- `created_at`: When the session was created
- `updated_at`: When the session was last updated
- `active`: Boolean indicating if the session is active
- `user_id`: Optional identifier for the user (for future enhancement)

**Validation Rules**:
- `session_id` must be unique
- `created_at` must be before `updated_at`

## Book Metadata Entity

**Fields**:
- `metadata_id`: Unique identifier for the metadata record
- `book_title`: Title of the book
- `author`: Author of the book
- `page_count`: Total number of pages in the book
- `total_chunks`: Total number of content chunks in the system
- `indexed_at`: When the book content was last indexed
- `source_path`: Path to the original book content

**Validation Rules**:
- `book_title` must not be empty
- `page_count` must be positive integer
- `total_chunks` must be positive integer