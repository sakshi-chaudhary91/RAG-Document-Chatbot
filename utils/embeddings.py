from sentence_transformers import SentenceTransformer

# Load pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text):
    """
    Convert text into an embedding vector.
    """
    embedding = model.encode(text)
    return embedding

def generate_embeddings(chunks):
    """
    Generate embeddings for all chunks.
    """

    embeddings = []

    for chunk in chunks:
        embedding = generate_embedding(chunk)
        embeddings.append(embedding)

    return embeddings