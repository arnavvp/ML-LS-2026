import faiss

from src.chunk import chunk_documents
from src.embed import embed_text


def create_pdf_index(text, filename):

    docs = [
        {
            "source": filename,
            "text": text
        }
    ]

    chunks = chunk_documents(docs)


    embeddings = embed_text(
        [
            chunk["text"]
            for chunk in chunks
        ]
    )


    index = faiss.IndexFlatIP(
        embeddings.shape[1]
    )

    index.add(
        embeddings
    )


    return index, chunks



def search_pdf(query, index, chunks, k=5):

    query_embedding = embed_text(
        [query]
    )


    scores, ids = index.search(
        query_embedding,
        k
    )


    results = []


    for score, idx in zip(scores[0], ids[0]):

        results.append(
            {
                "score": float(score),
                "source": chunks[idx]["source"],
                "text": chunks[idx]["text"]
            }
        )


    return results