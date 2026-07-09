import streamlit as st
from sentence_transformers import SentenceTransformer

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

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