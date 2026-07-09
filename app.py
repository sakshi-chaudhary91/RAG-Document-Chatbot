import streamlit as st
from utils.pdf_reader import extract_text, keyword_search
from utils.embeddings import generate_embedding, generate_embeddings
from utils.text_splitter import chunk_text
from utils.vector_store import create_faiss_index
from utils.search import semantic_search

# Page config
st.set_page_config(
    page_title="RAG Document Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG Document Chatbot")

# Upload PDF
uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:

    # Extract text
    text, pages, word_count = extract_text(uploaded_file)
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)
    index = create_faiss_index(embeddings)

    st.success("PDF processed successfully!")

    # 📊 Stats
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pages", pages)

    with col2:
        st.metric("Words", word_count)

    # 📄 Preview
    st.subheader("Text Preview")
    st.text_area("Preview", text[:2000], height=300)

#--------Chunk Information----------------

    st.subheader("📑 Chunk Information")
    st.write(f"Total Chunks: {len(chunks)}")
    st.write("First 3 Chunks:")
    for i, chunk in enumerate(chunks[:3]):
      st.write(f"### Chunk {i+1}")
      st.write(chunk)
      st.write("---")

# -------------Embeddings Information--------

    st.subheader("📊 Embedding Information")
    st.write(f"Total Embeddings: {len(embeddings)}")
    st.write(f"Embedding Dimension: {len(embeddings[0])}")
    st.write("First Embedding (First 10 Values):")
    st.write(embeddings[0][:10])

##-------- FAISS Information ----------

    st.subheader("FAISS Index Information")
    st.write(f"Total Vectors in Index: {index.ntotal}")

    # 🔍 Question section
    st.subheader("Ask a Question")

    query = st.text_input("Enter your question")

    if query:

        results = semantic_search(query, index, chunks)

        st.write("### 🔎 Answer")

        if results:
            st.write("#### 📌 Relevant Sentences:")
            for i, res in enumerate(results):
                st.write(f"{i+1}. {res}")

            st.write("---")
            st.write("#### 💡 Final Answer:")
            st.write("\n\n".join(results))

        else:
            st.warning("No relevant information found in document")