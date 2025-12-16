# Application Constants

# RAG Pipeline Constants
DEFAULT_TOP_K = 5  # Default number of results to retrieve for full-book mode
SELECTED_TEXT_TOP_K = 3  # Default number of results for selected-text mode
CHUNK_SIZE = 512  # Token size for content chunks
CHUNK_OVERLAP = 64  # Overlap between chunks to preserve context

# API Response Constants
DEFAULT_CONFIDENCE_THRESHOLD = 0.7
MIN_CONFIDENCE_FOR_ANSWER = 0.3

# Model Configuration
GEMINI_TEMPERATURE = 0.3
GEMINI_MAX_OUTPUT_TOKENS = 1024

# Error Messages
NO_RELEVANT_CONTENT_FOUND = "No relevant content found in the book to answer this question."
NO_RELEVANT_SELECTED_CONTENT_FOUND = "No relevant content found in the selected text to answer this question."

# Collection names
QDRANT_COLLECTION_NAME = "book_content"