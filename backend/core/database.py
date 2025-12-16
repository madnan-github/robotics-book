from qdrant_client import QdrantClient
from qdrant_client.http import models
from config.settings import settings


def get_qdrant_client():
    """
    Create and return a Qdrant client instance
    """
    client = QdrantClient(
        url=settings.qdrant_url,
        api_key=settings.qdrant_api_key,
        prefer_grpc=False  # Using HTTP for simplicity
    )
    return client


def ensure_collection_exists(client: QdrantClient, collection_name: str = None):
    """
    Ensure the specified collection exists in Qdrant with proper configuration
    """
    if collection_name is None:
        collection_name = settings.qdrant_collection_name

    try:
        # Check if collection exists
        client.get_collection(collection_name)
    except:
        # Create collection if it doesn't exist
        client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=1024,  # Cohere's multilingual embedding size
                distance=models.Distance.COSINE
            )
        )