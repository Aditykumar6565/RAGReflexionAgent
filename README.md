# 🧠 RAG Chatbot with LangChain, Streamlit & Groq

This project is a **Retrieval-Augmented Generation (RAG) chatbot** built with:
- **LangChain** for document retrieval and LLM orchestration
- **Streamlit** for the UI
- **Groq API** for LLM inference
- **HuggingFace embeddings** for semantic search

The chatbot loads a PDF, chunks the text, stores it in a vector database, and answers user queries with context-aware precision.

---

## 🚀 Features
- Upload and process PDF documents
- Chunk and store document embeddings using `HuggingFaceBgeEmbeddings`
- Query your document with **context-based answers**
- Simple UI with chat history using **Streamlit**
- Powered by **Groq's LLaMA-3** for fast inference

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Aditykumar6565/RAGReflexionAgent.git
cd RAGReflexionAgent
