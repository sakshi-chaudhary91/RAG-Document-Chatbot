import streamlit as st
from utils.pdf_reader import extract_text

st.set_page_config(
    page_title="RAG Document Chatbot",
    page_icon="📄",
    layout="wide"
)

st.title("📄 RAG Document Chatbot")

uploaded_file = st.file_uploader("Upload your PDF", type=["pdf"])

if uploaded_file is not None:

    text, pages, word_count = extract_text(uploaded_file)

    st.success("PDF processed successfully!")

    # 📊 Stats
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Pages", pages)

    with col2:
        st.metric("Words", word_count)

    # 📄 Preview
    st.subheader("Text Preview")

    st.text_area(
        "Preview",
        text[:2000],   
        height=400
    )