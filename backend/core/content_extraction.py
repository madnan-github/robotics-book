import os
from typing import List, Dict, Optional
from pathlib import Path
import re


def extract_book_content_from_file(file_path: str) -> str:
    """
    Extract text content from a book file (supports .txt, .md, .pdf)
    """
    file_extension = Path(file_path).suffix.lower()

    if file_extension == '.txt':
        return extract_from_txt(file_path)
    elif file_extension == '.md':
        return extract_from_md(file_path)
    elif file_extension == '.pdf':
        return extract_from_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file format: {file_extension}")


def extract_from_txt(file_path: str) -> str:
    """
    Extract content from a text file
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content


def extract_from_md(file_path: str) -> str:
    """
    Extract content from a markdown file, removing markdown formatting
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Remove markdown formatting while preserving content
    # Remove headers
    content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
    # Remove bold/italic
    content = re.sub(r'\*{1,2}([^*]+)\*{1,2}', r'\1', content)
    content = re.sub(r'_{1,2}([^_]+)_{1,2}', r'\1', content)
    # Remove code blocks
    content = re.sub(r'`{3}[\s\S]*?`{3}', '', content)
    # Remove inline code
    content = re.sub(r'`([^`]+)`', r'\1', content)
    # Remove links but keep link text
    content = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', content)
    # Remove images
    content = re.sub(r'!\[([^\]]*)\]\([^)]+\)', r'\1', content)

    return content


def extract_from_pdf(file_path: str) -> str:
    """
    Extract content from a PDF file
    """
    try:
        import PyPDF2
    except ImportError:
        raise ImportError("PyPDF2 is required to extract content from PDF files. Install it with: pip install PyPDF2")

    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        content = []
        for page in reader.pages:
            content.append(page.extract_text())
    return "\n".join(content)


def chunk_content(content: str, chunk_size: int = 512, overlap: int = 64) -> List[Dict]:
    """
    Split content into overlapping chunks
    """
    # Split content into sentences or paragraphs
    paragraphs = content.split('\n\n')  # Split by double newlines first

    chunks = []
    chunk_id = 1

    for paragraph in paragraphs:
        if len(paragraph.strip()) == 0:
            continue

        # If paragraph is smaller than chunk size, use it as is
        if len(paragraph) <= chunk_size:
            chunks.append({
                "chunk_id": f"chunk_{chunk_id}",
                "content": paragraph.strip(),
                "page_number": 1,  # Placeholder - would need actual page info from source
                "section_title": "Unknown Section",  # Placeholder
                "source_file": "book_source.txt"  # Placeholder
            })
            chunk_id += 1
        else:
            # Split large paragraph into smaller chunks
            words = paragraph.split()
            start_idx = 0

            while start_idx < len(words):
                # Get a chunk of words
                end_idx = start_idx + chunk_size
                chunk_words = words[start_idx:end_idx]

                # Join the words back into text
                chunk_text = ' '.join(chunk_words)

                chunks.append({
                    "chunk_id": f"chunk_{chunk_id}",
                    "content": chunk_text.strip(),
                    "page_number": 1,  # Placeholder
                    "section_title": "Unknown Section",  # Placeholder
                    "source_file": "book_source.txt"  # Placeholder
                })

                chunk_id += 1

                # Move start index with overlap
                start_idx = end_idx - overlap if end_idx < len(words) else len(words)

    return chunks


def extract_book_content_from_directory(directory_path: str) -> List[Dict]:
    """
    Extract content from all supported files in a directory
    """
    all_chunks = []
    supported_extensions = ['.txt', '.md', '.pdf']

    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            file_extension = Path(file).suffix.lower()

            if file_extension in supported_extensions:
                try:
                    content = extract_book_content_from_file(file_path)
                    chunks = chunk_content(content)
                    all_chunks.extend(chunks)
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")

    return all_chunks