#!/usr/bin/env python3
"""
Script to index the actual book content from docs directory into Qdrant
"""

import sys
import os
import asyncio
import uuid
import re
from typing import List, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from core.database import get_qdrant_client, ensure_collection_exists
from config.settings import settings
from services.embedding_service import embedding_service

def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 100) -> List[str]:
    """Split text into overlapping chunks"""
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

        # Make sure we don't get stuck
        if start >= end:
            break

    return chunks

def read_docs_content():
    """Read content from all documentation files"""
    docs_path = "/home/ruser/q4/robotics-book/docs"
    content_chunks = []

    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if file.endswith(('.md', '.mdx')):
                file_path = os.path.join(root, file)

                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()

                        # Extract title from the content (first heading or filename)
                        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
                        title = title_match.group(1) if title_match else file.replace('.mdx', '').replace('.md', '')

                        # Remove markdown headers and other metadata from content
                        # This regex removes frontmatter if present
                        content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)

                        # Split content into chunks
                        chunks = chunk_text(content, chunk_size=1000, overlap=100)

                        for i, chunk in enumerate(chunks):
                            content_chunks.append({
                                "content": chunk.strip(),
                                "page_number": i + 1,
                                "section_title": f"{title} - Chunk {i + 1}",
                                "source_file": file_path.replace('/home/ruser/q4/robotics-book/', '')
                            })

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")
                    continue

    return content_chunks

async def index_book_content():
    print("Connecting to Qdrant...")
    client = get_qdrant_client()

    # Ensure collection exists
    ensure_collection_exists(client, settings.qdrant_collection_name)
    print(f"Collection '{settings.qdrant_collection_name}' is ready")

    # Read documentation content
    print("Reading documentation content...")
    content_chunks = read_docs_content()
    print(f"Found {len(content_chunks)} content chunks to index")

    if not content_chunks:
        print("No content found to index")
        return

    # Prepare points for Qdrant
    points = []
    for i, chunk in enumerate(content_chunks):
        if not chunk["content"].strip():
            continue

        try:
            # Create embeddings for the content
            embeddings = await embedding_service.create_document_embeddings([chunk["content"]])
            vector = embeddings[0]

            point = {
                "id": str(uuid.uuid4()),
                "vector": vector,
                "payload": {
                    "content": chunk["content"],
                    "page_number": chunk["page_number"],
                    "section_title": chunk["section_title"],
                    "source_file": chunk["source_file"]
                }
            }
            points.append(point)

            if (i + 1) % 10 == 0:
                print(f"Processed {i + 1}/{len(content_chunks)} chunks...")

        except Exception as e:
            print(f"Error processing chunk {i}: {e}")
            continue

    # Upload to Qdrant
    if points:
        print(f"Uploading {len(points)} points to Qdrant...")
        client.upsert(
            collection_name=settings.qdrant_collection_name,
            points=points
        )

        print(f"Successfully indexed {len(points)} content chunks into Qdrant collection")

        # Verify the collection now has content
        collection_info = client.get_collection(settings.qdrant_collection_name)
        print(f"Collection now contains {collection_info.points_count} vectors")
    else:
        print("No points were created due to processing errors")

if __name__ == "__main__":
    print("Starting to index book content from documentation files...")
    asyncio.run(index_book_content())
    print("Book content indexing completed!")