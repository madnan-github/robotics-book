import asyncio
from typing import List, Dict
from qdrant_client.http import models
from ..core.database import get_qdrant_client, ensure_collection_exists
from ..config.settings import settings
from ..core.content_extraction import extract_book_content_from_directory
from ..core.security import hash_content
import cohere
from datetime import datetime


class IndexingService:
    def __init__(self):
        self.qdrant_client = get_qdrant_client()
        self.cohere_client = cohere.Client(settings.cohere_api_key)
        self.collection_name = settings.qdrant_collection_name

    async def index_book_content(self, source_path: str):
        """
        Index book content from source path into Qdrant using Cohere embeddings
        """
        # Ensure the collection exists
        ensure_collection_exists(self.qdrant_client, self.collection_name)

        # Extract content from the source
        chunks = extract_book_content_from_directory(source_path)

        # Process chunks in batches for embedding
        batch_size = 10  # Cohere's recommended batch size
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]

            # Extract text content for embedding
            texts = [chunk['content'] for chunk in batch]

            # Generate embeddings using Cohere
            response = self.cohere_client.embed(
                texts=texts,
                model=settings.cohere_model,
                input_type="search_document"
            )

            embeddings = response.embeddings

            # Prepare points for Qdrant
            points = []
            for idx, (chunk, embedding) in enumerate(zip(batch, embeddings)):
                point = models.PointStruct(
                    id=f"{chunk['chunk_id']}_{int(datetime.now().timestamp())}",
                    vector=embedding,
                    payload={
                        "content": chunk['content'],
                        "page_number": chunk.get('page_number', 1),
                        "section_title": chunk.get('section_title', 'Unknown'),
                        "source_file": chunk.get('source_file', 'unknown'),
                        "chunk_id": chunk['chunk_id'],
                        "created_at": datetime.now().isoformat(),
                        "content_hash": hash_content(chunk['content'])
                    }
                )
                points.append(point)

            # Upload batch to Qdrant
            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=points
            )

        print(f"Successfully indexed {len(chunks)} content chunks into Qdrant collection '{self.collection_name}'")

    async def update_book_content(self, source_path: str):
        """
        Update existing indexed content with new content from source path
        """
        # This would involve checking for changes and updating only what's needed
        # For now, we'll just call the index method which will overwrite
        await self.index_book_content(source_path)

    async def delete_book_content(self, content_hashes: List[str]):
        """
        Delete content from Qdrant based on content hashes
        """
        # Find points with matching content hashes and delete them
        points_to_delete = []

        # This is a simplified approach - in practice, you'd query for points with specific payloads
        # and then delete them by ID
        # For now, this is a placeholder for the deletion functionality
        print(f"Deletion of content with hashes {content_hashes} would happen here")


# Singleton instance
indexing_service = IndexingService()