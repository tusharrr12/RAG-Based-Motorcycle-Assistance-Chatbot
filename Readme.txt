# RAG-Based Motorcycle Assistance Chatbot

An AI-powered motorcycle troubleshooting assistant built using **Retrieval-Augmented Generation (RAG)**.
The system helps riders diagnose motorcycle issues using official service manuals and generates context-aware answers using a Large Language Model.

---

# Features

* AI-powered motorcycle troubleshooting assistant
* Retrieval-Augmented Generation (RAG) architecture
* Semantic search using Sentence Transformers
* Vector database with ChromaDB
* Groq LLaMA model for fast inference
* FastAPI backend API
* Streamlit chatbot interface
* Multi-brand motorcycle manual support
* Context-aware responses using manual data

---

# Tech Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Backend API          | FastAPI               |
| Frontend UI          | Streamlit             |
| Vector Database      | ChromaDB              |
| Embeddings           | Sentence Transformers |
| LLM                  | Groq LLaMA            |
| Framework            | LangChain             |

---

# System Architecture

User Question
↓
Streamlit Chat Interface
↓
FastAPI Backend
↓
Retriever (ChromaDB Vector Search)
↓
Motorcycle Manual Context
↓
Groq LLaMA Model
↓
Generated Answer

---

# Project Structure

```
Bike-RAG-Chatbot
│
├── backend
│   └── main.py
│
├── frontend
│   └── app.py
│
├── data
│   ├── bajaj
│   ├── ktm
│   ├── royal_enfield
│   └── tvs
│
├── ingest.py
├── requirements.txt
└── README.md
```

---

# Installation

Clone the repository

```
git clone https://github.com/yourusername/bike-rag-chatbot.git
cd bike-rag-chatbot
```

Install dependencies

```
pip install -r requirements.txt
```

---

# Setup Environment Variables

Create a Groq API key from

https://console.groq.com/keys

Then set the environment variable

Windows:

```
setx GROQ_API_KEY "your_api_key_here"
```

Mac/Linux:

```
export GROQ_API_KEY="your_api_key_here"
```

---

# Run the Project

Step 1 — Create Vector Database

```
python ingest.py
```

Step 2 — Start Backend

```
uvicorn backend.main:app --reload
```

Step 3 — Run Chatbot UI

```
streamlit run frontend/app.py
```

---

# Example Questions

* Why is my bike engine overheating?
* Why does my motorcycle not start?
* Why is my clutch slipping?
* Why are my brakes making noise?

---

# Future Improvements

* Voice-based motorcycle assistant
* Image-based fault detection
* Mobile application interface
* Hybrid search (BM25 + Vector Search)

---

# Author

**Tushar Chaudhari**
Artificial Intelligence & Data Science Student
