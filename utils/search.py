import numpy as np
from utils.embeddings import generate_embedding

def semantic_search(query, index, chunks, k=3):
    query_embedding = generate_embedding(query)

    query_embedding = np.array(query_embedding).astype("float32").reshape(1, -1)
    distances, indices = index.search(query_embedding, k)

    results = []
    for idx in indices[0]:
        results.append((idx, chunks[idx]))
    return results