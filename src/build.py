from src.loader import load_documents
from src.chunk import chunk_documents
from src.vector_store import build_index

import os


os.makedirs(
    "index",
    exist_ok=True
)


print("Loading documents")

docs = load_documents(
    "data"
)


print("Chunking")

chunks = chunk_documents(
    docs
)


print(
    f"Chunks: {len(chunks)}"
)


print("Building FAISS")

build_index(
    chunks
)


print("Done")