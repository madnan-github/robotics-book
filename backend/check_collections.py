#!/usr/bin/env python3
"""
Script to check Qdrant collections and their content
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.database import get_qdrant_client
from config.settings import settings

def check_qdrant_collections():
    print("Connecting to Qdrant...")
    client = get_qdrant_client()

    # List all collections
    collections = client.get_collections()
    print(f"Available collections: {[coll.name for coll in collections.collections]}")

    # Check each collection
    for collection_name in ['book_content', 'embedding']:
        try:
            collection_info = client.get_collection(collection_name)
            print(f"\nCollection '{collection_name}':")
            print(f"  Points count: {collection_info.points_count}")
            print(f"  Config: {collection_info.config}")

            # If collection has points, get a sample
            if collection_info.points_count > 0:
                sample_points = client.scroll(
                    collection_name=collection_name,
                    limit=2,
                    with_payload=True,
                    with_vectors=False
                )
                print(f"  Sample points: {len(sample_points[0])}")
                for i, point in enumerate(sample_points[0]):
                    print(f"    Point {i+1}: ID={point.id}, Payload keys={list(point.payload.keys()) if point.payload else 'None'}")
            else:
                print(f"  No points in collection")

        except Exception as e:
            print(f"  Error accessing collection '{collection_name}': {e}")

if __name__ == "__main__":
    check_qdrant_collections()