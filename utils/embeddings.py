from sentence_transformers import SentenceTransformer

# Load pre-trained embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embedding(text):
    """
    Convert text into an embedding vector.
    """
    embedding = model.encode(text)
    return embedding