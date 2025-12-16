import asyncio
from typing import List
import cohere
from config.settings import settings


class EmbeddingService:
    def __init__(self):
        self.client = cohere.Client(settings.cohere_api_key)
        self.model = settings.cohere_model

    async def create_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for a list of texts using Cohere
        """
        try:
            response = self.client.embed(
                texts=texts,
                model=self.model,
                input_type="search_query"  # Using search_query for user queries
            )
            return response.embeddings
        except Exception as e:
            raise Exception(f"Error creating embeddings: {str(e)}")

    async def create_document_embeddings(self, texts: List[str]) -> List[List[float]]:
        """
        Create embeddings for documents using Cohere (with appropriate input type)
        """
        try:
            response = self.client.embed(
                texts=texts,
                model=self.model,
                input_type="search_document"  # Using search_document for book content
            )
            return response.embeddings
        except Exception as e:
            raise Exception(f"Error creating document embeddings: {str(e)}")

    async def get_embedding_dimensions(self) -> int:
        """
        Get the dimensions of the embeddings for the current model
        """
        # Cohere's multilingual models typically return 1024-dimensional embeddings
        # This is a fixed value based on the model specification
        return 1024


# Singleton instance
embedding_service = EmbeddingService()