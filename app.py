import streamlit as st
from utils.pdf_reader import extract_text, keyword_search
from utils.embeddings import generate_embedding, generate_embeddings
from utils.text_splitter import chunk_text
from utils.vector_store import create_faiss_index
from utils.search import semantic_search
from utils.llm import generate_answer

# Page config
st.set_page_config(
    page_title="RAG Document Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG Document Chatbot")
if "chat_history" not in st.session_state:
   st.session_state.chat_history = []

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
    
    # 🔍 Question Section
    
    st.subheader("Ask a Question")
    def clear_question():
        st.session_state.user_question = ""
    query = st.text_input(
        "Enter your question",
        key="user_question"
        )

    col1, col2 = st.columns(2)
    with col1:
        ask = st.button("🤖 Get AI Answer")
    with col2:
        st.button("🗑️ Clear Question", on_click=clear_question)

    if ask:
        if query.strip():
            results = semantic_search(query, index, chunks)
            if results:
                context = "\n\n".join([chunk for _, chunk in results])
                with st.spinner("Generating AI Answer..."):
                    ai_answer = generate_answer(context, query)
                    
                    st.session_state.chat_history.append({
                         "question": query,
                         "answer": ai_answer
                         })
                    st.success("Answer Generated Successfully!")
                    st.caption("💡 Answer generated using Retrieval-Augmented Generation (RAG) with Google Gemini 2.5 Flash.")
                    with st.expander("📌 View Retrieved Chunks"):
                        for i, (idx, chunk) in enumerate(results, 1):
                            st.markdown(f"### 📄 Source {i} (Chunk {idx + 1})")
                            st.info(chunk)
                        
                    st.subheader("🤖 AI Answer")
                    st.info(ai_answer)
                    st.subheader("📚 Sources Used")
                    for idx, _ in results:
                        st.markdown(f"- 📄 Chunk {idx + 1}")
            else:
                st.warning("No relevant information found in the document.")
        else:
            st.warning("Please enter a question.")

       # 💬 Chat History
    if st.session_state.chat_history:
        st.write("## 💬 Chat History")
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history.clear()
            st.rerun()
        for chat in reversed(st.session_state.chat_history):
            st.markdown(f"**👤 You:** {chat['question']}")
            st.markdown(f"**🤖 AI:** {chat['answer']}")
            st.write("---")