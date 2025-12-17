#!/usr/bin/env python3
"""
Script to migrate content from embeddings collection to book_content collection
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.database import get_qdrant_client, ensure_collection_exists
from config.settings import settings

def migrate_content():
    print("Connecting to Qdrant...")
    client = get_qdrant_client()

    # Ensure the target collection exists
    ensure_collection_exists(client, settings.qdrant_collection_name)
    print(f"Target collection '{settings.qdrant_collection_name}' is ready")

    # Get all points from the source collection
    source_collection = "embeddings"
    try:
        collection_info = client.get_collection(source_collection)
        print(f"Source collection '{source_collection}' has {collection_info.points_count} points")

        if collection_info.points_count == 0:
            print("Source collection is empty, nothing to migrate")
            return

        # Get all points from source collection
        all_points = []
        offset = None
        while True:
            records, next_offset = client.scroll(
                collection_name=source_collection,
                limit=100,
                with_payload=True,
                with_vectors=True,
                offset=offset
            )
            all_points.extend(records)

            if next_offset is None:
                break
            offset = next_offset

        print(f"Retrieved {len(all_points)} points from source collection")

        # Prepare points for the target collection with potentially modified payloads
        target_points = []
        for point in all_points:
            # Create a new point structure compatible with the RAG service expectations
            # The RAG service expects payloads with 'content', 'page_number', 'section_title', 'source_file'
            original_payload = point.payload or {}

            # Map the existing payload to the expected format
            new_payload = {
                'content': original_payload.get('content', ''),
                'page_number': original_payload.get('chunk_index', 1),
                'section_title': original_payload.get('title', 'Unknown Section'),
                'source_file': original_payload.get('url', 'unknown_source'),
                # Keep original fields as well
                **original_payload
            }

            target_point = {
                'id': point.id,
                'vector': point.vector,
                'payload': new_payload
            }
            target_points.append(target_point)

        # Upload to the target collection
        if target_points:
            client.upsert(
                collection_name=settings.qdrant_collection_name,
                points=target_points
            )
            print(f"Successfully migrated {len(target_points)} points to '{settings.qdrant_collection_name}'")

        # Verify the migration
        target_info = client.get_collection(settings.qdrant_collection_name)
        print(f"Target collection now has {target_info.points_count} points")

    except Exception as e:
        print(f"Error during migration: {e}")

if __name__ == "__main__":
    migrate_content()