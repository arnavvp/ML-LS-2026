import faiss
import pickle

from src.embed import embed_text


index = faiss.read_index(
    "index/faiss.index"
)


with open(
    "index/chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)



def retrieve(query, k=5):

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