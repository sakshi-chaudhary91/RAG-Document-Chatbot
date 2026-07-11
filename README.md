# 📄 RAG Document Chatbot

A Retrieval-Augmented Generation (RAG) based chatbot that allows users to upload PDF documents and ask questions based on the document content.

This project is being developed step by step to understand every concept of the RAG pipeline, including text extraction, chunking, embeddings, vector databases, semantic search, and LLM integration.

---

# ✨ Features

```text
-📄 Upload Multiple PDF Documents
-📑 Automatic PDF Text Extraction
-✂️ Smart Text Chunking
-🧠 Sentence Embedding Generation
-🗂️ FAISS Vector Database
-🔍 Semantic Search
-🤖 AI Answer Generation using Gemini 2.5 Flash
-⚡ Streaming AI Response 
-💬 Chat History
-📌 View Retrieved Source Chunks
-📊 Document Statistics (Pages & Words)
-🎨 Modern Streamlit Interface
``` 

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

### ✅ Version 4.4
- Semantic Search using FAISS
- Retrieve Top Relevant Chunks
- Display Retrieved Chunks

### ✅ Version 5.1
- Google Gemini 2.5 Flash Integration
- Prompt Engineering for Context-Aware Responses
- AI-Generated Answers from Retrieved Context
- "Get AI Answer" Button
- Loading Spinner during Response Generation

### ✅ Version 5.2

- Added Exception Handling using "try-except"
- Display User-Friendly Error Messages
- Cached Sentence Transformer Model using "@st.cache_resource"
- Improved Application Performance

### ✅ Version 5.3

- Added Chat History using st.session_state
- Stored Previous Questions and AI Answers
- Displayed Conversation History
- Added Clear Question Button
- Added Clear Chat Button
- Improved Chatbot User Experience

### ✅ Version 5.4

- Added Expandable Retrieved Chunks using `st.expander`
- Improved AI Answer UI using `st.info`
- Enhanced Chunk Display Formatting
- Added RAG Information Caption
- Improved Overall User Interface

### ✅ Version 5.5

- Added Source Attribution
- Display Chunk Numbers with Retrieved Context
- Added "Sources Used" Section
- Improved Answer Transparency
- Enhanced Explainability of RAG Responses

### ✅ Version 5.6
- Upload multiple PDFs at once.
- Automatically merges text from all uploaded documents.
- Creates a single FAISS index from all documents.
- Ask questions across multiple PDFs simultaneously.

### ✅ Version 6
- Update streamlit UI.


---


# 📂 Project Structure

```text
RAG_Document_Chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── .env
├── uploads/
└── utils/
    ├── pdf_reader.py
    ├── text_splitter.py
    ├── embeddings.py
    ├── vector_store.py
    ├── search.py
    └── llm.py
```             
           


---

# 🏗️ RAG Pipeline

```text
PDF Upload
    │
    ▼
Extract Text from PDF
    │
    ▼
Split into Chunks
    │
    ▼
Generate Text Embeddings
    │
    ▼
Store in FAISS Index
    │
    ▼
User Asks Question
    │
    ▼
Generate Question Embedding
    │
    ▼
Semantic Search (FAISS)
    │
    ▼
Retrieve Top Relevant Chunks
    │
    ▼
Prompt Engineering
    │
    ▼
Gemini 2.5 Flash LLM
    │
    ▼
AI Generated Response
```

---

# 🛠️ Tech Stack

```text
- Python
- Streamlit
- Sentence Transformers
- FAISS
- Google Gemini 2.5 Flash
- NumPy
- PDFPlumber
- python-dotenv
``` 

---


# ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/sakshi-chaudhary91/RAG-Document-Chatbot.git

# Navigate to the project directory
cd RAG_Document_Chatbot

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

---

# 🚀 Future Improvements

```text
- 📚 Multiple PDF Support
- 📝 Source Citations
- ⚡ Embedding & FAISS Caching
- 📄 Download Answer as PDF
- 📋 Copy Answer Button
- 🎨 ChatGPT-style UI
- 🔄 Streaming AI Responses
``` 

---

# 👩‍💻 Author

```text
Sakshi Chaudhary

B.Tech (CSE - AI/ML)

Passionate about Artificial Intelligence, Machine Learning, Generative AI, and Large Language Models.
``` 