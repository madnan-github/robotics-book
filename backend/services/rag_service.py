import asyncio
from typing import Dict, List, Optional
from models.user_query import QueryMode
from services.embedding_service import embedding_service
from services.retrieval_service import retrieval_service
from services.generation_service import generation_service
from core.constants import DEFAULT_TOP_K, SELECTED_TEXT_TOP_K, NO_RELEVANT_CONTENT_FOUND, NO_RELEVANT_SELECTED_CONTENT_FOUND
from core.security import sanitize_input


class RAGService:
    def __init__(self):
        self.embedding_service = embedding_service
        self.retrieval_service = retrieval_service
        self.generation_service = generation_service

    async def process_query(self, query_text: str, query_mode: QueryMode, selected_text: str = None, top_k: int = None) -> Dict:
        """
        Process a user query through the RAG pipeline
        """
        # Sanitize the input
        sanitized_query = sanitize_input(query_text)

        if query_mode == QueryMode.FULL_BOOK:
            return await self._process_full_book_query(sanitized_query, top_k)
        elif query_mode == QueryMode.SELECTED_TEXT:
            if not selected_text:
                return {
                    "response": "Selected text is required for selected-text mode",
                    "confidence": 0.0,
                    "refusal_response": True,
                    "retrieved_context": []
                }
            return await self._process_selected_text_query(sanitized_query, selected_text, top_k)
        else:
            return {
                "response": "Invalid query mode",
                "confidence": 0.0,
                "refusal_response": True,
                "retrieved_context": []
            }

    async def _process_full_book_query(self, query: str, top_k: int = None) -> Dict:
        """
        Process a query against the full book content
        """
        if top_k is None:
            top_k = DEFAULT_TOP_K

        # Retrieve relevant context
        retrieved_chunks, similarity_scores = await self.retrieval_service.retrieve_full_book_context(query, top_k)

        if not retrieved_chunks:
            # No relevant content found, return refusal response
            return {
                "response": NO_RELEVANT_CONTENT_FOUND,
                "session_id": None,  # Will be added by the endpoint
                "retrieved_context": [],
                "confidence": 0.0,
                "refusal_response": True,
                "reason": "no relevant content found"
            }

        # Generate response based on context
        generation_result = await self.generation_service.generate_response(
            context=" ".join([chunk["content"] for chunk in retrieved_chunks]),
            query=query
        )

        return {
            "response": generation_result["generated_text"],
            "session_id": None,  # Will be added by the endpoint
            "retrieved_context": retrieved_chunks,
            "confidence": generation_result["confidence_score"],
            "refusal_response": generation_result["refusal_response"]
        }

    async def _process_selected_text_query(self, query: str, selected_text: str, top_k: int = None) -> Dict:
        """
        Process a query against only the selected text
        """
        if top_k is None:
            top_k = SELECTED_TEXT_TOP_K

        # Retrieve relevant context from selected text
        # In selected-text mode, we only use the provided selected text
        retrieved_chunks = [{"content": selected_text, "source": "selected_text"}]
        similarity_scores = [0.8]  # Placeholder similarity

        # Check if the query is relevant to the selected text
        # For now, we'll assume it is and proceed with generation
        # In a real implementation, you'd have more sophisticated relevance checking

        # Generate response based on the selected text
        generation_result = await self.generation_service.generate_selected_text_response(
            selected_text=selected_text,
            query=query
        )

        if generation_result["refusal_response"]:
            return {
                "response": NO_RELEVANT_SELECTED_CONTENT_FOUND,
                "session_id": None,  # Will be added by the endpoint
                "retrieved_context": [],
                "confidence": 0.0,
                "refusal_response": True,
                "reason": "no relevant content in selected text"
            }

        return {
            "response": generation_result["generated_text"],
            "session_id": None,  # Will be added by the endpoint
            "retrieved_context": retrieved_chunks,
            "confidence": generation_result["confidence_score"],
            "refusal_response": generation_result["refusal_response"]
        }

    async def update_rag_pipeline(self, new_content: str):
        """
        Update the RAG pipeline with new content
        """
        # This would typically involve re-indexing the content
        # For now, this is a placeholder
        pass


# Singleton instance
rag_service = RAGService()