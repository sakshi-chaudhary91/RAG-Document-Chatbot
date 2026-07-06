import streamlit as st
from utils.pdf_reader import extract_text, keyword_search
from utils.embeddings import generate_embedding
from utils.text_splitter import chunk_text

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
    embedding = generate_embedding(text[:500])

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
    st.subheader("📑 Chunk Information")
    st.write(f"Total Chunks: {len(chunks)}")
    st.write("First 3 Chunks:")
    for i, chunk in enumerate(chunks[:3]):
      st.write(f"### Chunk {i+1}")
      st.write(chunk)
      st.write("---")
    st.subheader("Embedding Information")
    st.write(f"Embedding Dimension: {len(embedding)}")
    st.write("First 10 Values:")
    st.write(embedding[:10])


    # 🔍 Question section
    st.subheader("Ask a Question")

    query = st.text_input("Enter your question")

    if query:

        results = keyword_search(text, query)

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

            st.write("---")
            st.write("#### 📄 Document Summary:")
            st.write(text[:800])