import streamlit as st
from utils.pdf_reader import extract_text

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
    text = extract_text(uploaded_file)

    st.success("PDF uploaded successfully!")

    # Show text
    st.subheader("📄 Extracted PDF Content")

    st.text_area(
        "Content",
        text,
        height=500
    )