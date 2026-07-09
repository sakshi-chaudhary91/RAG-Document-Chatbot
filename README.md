📄 AI Document Chatbot using RAG

An AI-powered Document Chatbot built with Streamlit, Sentence Transformers, FAISS, and Google Gemini. Upload a PDF, ask questions in natural language, and receive context-aware AI-generated answers using a Retrieval-Augmented Generation (RAG) pipeline.

---

🚀 Features

- 📄 Upload PDF documents
- ✂️ Automatic text chunking
- 🧠 Sentence Transformer embeddings
- 🗂️ FAISS vector database
- 🔍 Semantic search
- 🤖 AI-generated answers using Gemini 2.5 Flash
- 📌 Displays retrieved document chunks
- ⚡ Interactive Streamlit interface

---

🏗️ RAG Pipeline

PDF Upload
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Generate Embeddings
      ↓
Store Embeddings in FAISS
      ↓
User Question
      ↓
Question Embedding
      ↓
Semantic Search
      ↓
Retrieve Top Relevant Chunks
      ↓
Gemini 2.5 Flash
      ↓
AI Generated Answer

---

🛠️ Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Google Gemini 2.5 Flash
- NumPy
- PDFPlumber

---

📂 Project Structure

RAG_Document_Chatbot/
│
├── app.py
├── README.md
├── requirements.txt
├── .env
├── .gitignore
│
├── uploads/
│
└── utils/
    ├── pdf_reader.py
    ├── text_splitter.py
    ├── embeddings.py
    ├── vector_store.py
    ├── search.py
    └── llm.py

---

⚙️ Installation

git clone <https://github.com/sakshi-chaudhary91/RAG-Document-Chatbot.git>
cd RAG_Document_Chatbot

pip install -r requirements.txt

streamlit run app.py

---

📸 Current Features

- ✅ PDF Upload
- ✅ Text Extraction
- ✅ Text Chunking
- ✅ Embedding Generation
- ✅ FAISS Vector Index
- ✅ Semantic Search
- ✅ Prompt Engineering
- ✅ Gemini LLM Integration
- ✅ AI Answer Generation

---

🔮 Future Improvements

- Chat History
- Multiple PDF Support
- Conversation Memory
- Source Citations
- Response Caching
- Download Answer as PDF
- Copy Answer Button
- Streaming AI Responses

---

👩‍💻 Author

Sakshi Chaudhary

AI/ML & Generative AI Enthusiast