#!/usr/bin/env python3
"""
Script to create the Qdrant collection for the RAG chatbot
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.database import get_qdrant_client, ensure_collection_exists
from config.settings import settings

def main():
    print("Connecting to Qdrant...")
    client = get_qdrant_client()

    print(f"Ensuring collection '{settings.qdrant_collection_name}' exists...")
    ensure_collection_exists(client, settings.qdrant_collection_name)

    print("Collection is ready!")

    # Verify the collection exists
    try:
        collection_info = client.get_collection(settings.qdrant_collection_name)
        print(f"✓ Collection '{settings.qdrant_collection_name}' exists and is ready")
        print(f"  Points count: {collection_info.points_count}")
        print(f"  Config: {collection_info.config}")
    except Exception as e:
        print(f"✗ Error verifying collection: {e}")

if __name__ == "__main__":
    main()