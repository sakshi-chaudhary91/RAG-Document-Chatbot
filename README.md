# 📄 RAG Document Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload PDF documents and ask questions based on the document content.

This project is being developed step by step to understand every concept of the RAG pipeline, including text extraction, chunking, embeddings, vector databases, semantic search, and LLM integration.

---

## 🚀 Features Implemented

### ✅ Version 1
- PDF Upload
- PDF Text Extraction
- Text Preview

### ✅ Version 2
- Keyword Search
- Question Input
- Display Relevant Sentences

### ✅ Version 3
- Sentence Transformer Embeddings
- Embedding Generation
- Embedding Information Display

### ✅ Version 4.1
- Text Chunking
- Display Total Chunks
- Preview First Three Chunks

### ✅ Version 4.2
- Generate Embeddings for Every Chunk
- Store Embeddings in a List
- Display Total Embeddings
- Display Embedding Dimension

### ✅ Version 4.3
- Implemented FAISS Vector Database
- Created FAISS Index using IndexFlatL2
- Added all document embeddings to the index
- Displayed total vectors stored in the FAISS index

---

## 📂 Project Structure

```text
RAG_Document_Chatbot/
│
├── app.py
├── requirements.txt
├── README.md
│
├── uploads/
│
└── utils/
    ├── pdf_reader.py
    ├── embeddings.py
    ├── text_splitter.py
    ├── vector_store.py

```

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PDFPlumber
- Sentence Transformers
- FAISS 
- NumPy

---

## 🔄 RAG Pipeline

```text
PDF Upload
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embeddings
      ↓
FAISS Vector Database
      ↓
Semantic Search
      ↓
LLM
      ↓
Final Response
```

---

## 📌 Upcoming Features


- Semantic Search
- Retrieve Top-K Chunks
- Gemini API Integration
- AI-Powered Question Answering
- Chat History
- Multiple PDF Support

---

## 👩‍💻 Author

**Sakshi Chaudhary**

B.Tech (CSE - AI/ML)