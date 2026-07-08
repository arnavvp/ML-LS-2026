import faiss
import pickle

from src.embed import embed_text


def build_index(chunks):

    texts = [
        chunk["text"]
        for chunk in chunks
    ]


    embeddings = embed_text(texts)


    dimension = embeddings.shape[1]


    index = faiss.IndexFlatIP(
        dimension
    )


    index.add(
        embeddings
    )


    faiss.write_index(
        index,
        "index/faiss.index"
    )


    with open(
        "index/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(
            chunks,
            f
        )


    print(
        f"Saved {len(chunks)} chunks"
    )