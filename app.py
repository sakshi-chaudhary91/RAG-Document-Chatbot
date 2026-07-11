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
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 RAG Document Chatbot")
st.caption("Upload PDF documents and chat with them using AI.")
st.divider()
if "chat_history" not in st.session_state:
   st.session_state.chat_history = []

# Upload PDF
uploaded_files = st.file_uploader(
    "📄 Upload PDF Documents",
    type="pdf",
    accept_multiple_files=True
)

if uploaded_files:

    # Extract text
    all_text = ""
    total_pages = 0
    total_word_count = 0
    for pdf in uploaded_files:
        text, pages, word_count = extract_text(pdf)
        all_text += text + "\n\n"
        total_pages += pages
        total_word_count += word_count
    chunks = chunk_text(all_text)
    embeddings = generate_embeddings(chunks)
    index = create_faiss_index(embeddings)

    st.success("PDF processed successfully!")

    # 📊 Stats
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pages", total_pages)

    with col2:
        st.metric("Words", total_word_count)

    # 📄 Preview
    st.subheader("Text Preview")
    st.text_area("Preview", all_text[:2000], height=300)

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
    query = st.chat_input(
        "Ask anything about your documents...",
        key="user_question"
        )

    if query: 
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
                st.caption("💡 Answer generated using Retrieval-Augmented Generation with Google Gemini 2.5 Flash.")
                with st.chat_message("user"):
                    st.write(query)
                with st.chat_message("assistant"):
                     placeholder = st.empty()
                     response = ""
                     import time
                     for word in ai_answer.split():
                        response += word + " "
                        placeholder.markdown(response)
                        time.sleep(0.03)
                     with st.expander("📌 View Retrieved Chunks"):
                         for i, (idx, chunk) in enumerate(results, 1):
                             st.markdown(f"### 📄 Source {i} (Chunk {idx + 1})")
                             st.info(chunk)
         else:
             st.warning("No relevant information found in the document.")
    else:
        st.warning("Please enter a question.")

       # 💬 Chat History
    if st.session_state.chat_history:
        st.subheader("💬 Chat History")
        if st.button("🗑️ Clear Chat"):
            st.session_state.chat_history.clear()
            st.rerun()
        for chat in st.session_state.chat_history:
            with st.chat_message("user"):
                st.write(chat["question"])
            with st.chat_message("assistant"):
                st.write(chat["answer"])
            