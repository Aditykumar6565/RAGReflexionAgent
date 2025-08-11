# 🧠 RAG Chatbot with LangChain, Streamlit & Groq

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-FF4B4B?logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-0.1%2B-brightgreen)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success)

This project is a **Retrieval-Augmented Generation (RAG) chatbot** that:
- Loads PDF documents
- Chunks and stores their embeddings
- Retrieves context-based answers from the document  
It is built using **LangChain**, **Streamlit**, **Groq API**, and **HuggingFace embeddings** for semantic search.

---

## 🚀 Features
- 📄 Upload and process PDF documents
- 🔍 Chunk and store document embeddings with `HuggingFaceBgeEmbeddings`
- 🤖 Query your document with context-aware answers
- 💬 Simple UI with chat history using Streamlit
- ⚡ Powered by Groq’s **LLaMA-3** for fast and precise inference

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Aditykumar6565/RAGReflexionAgent.git
cd RAGReflexionAgent
```

## Install Dependencies
```bash
pip install streamlit langchain_groq langchain_community pypdf sentence-transformers
```
## Add Your PDF
Place your PDF file in the project folder with the name.You can change this filename inside Rag.py in the get_vectorstore() function.
```bash
reflexion.pdf
```

## Add Your Groq API Key
```bash
groq_chat = ChatGroq(
    groq_api_key="YOUR_API_KEY_HERE",
    model_name=model
)
```
Tip: For better security, store your API key in a .env file.

## Run the Chatbot
```bash
streamlit run Rag.py
```
The app will open in your browser at:

http://localhost:8501

## License
Licensed under the MIT License
