# HR Policy Chatbot

## Project Overview
This project is an **HR Policy Chatbot** designed to help employees quickly get answers to their HR-related questions by interacting with company policy documents.

The chatbot uses natural language processing and retrieval techniques to understand queries and provide accurate responses based on HR policy documents.

---

## Features
- Upload and process HR policy documents (PDFs, DOCX)
- Text preprocessing and chunking for better understanding
- Vector embeddings for semantic search
- Fast and relevant response generation using LLM
- Interactive chat interface
- Dockerized for easy deployment

---

## Technologies Used
- Python 3.11
- Streamlit (frontend UI)
- Qdrant (vector search database)
- Ollama or other LLM backend
- Docker and Docker Compose

---

## Project Structure

```
HR-Policy-Chatbot/
│
├── utils/
│   ├── preprocessing.py
│   ├── embedding.py
│   ├── loader.py
│   ├── chunking.py
│   └── vectorstore.py
│
├── ingestion.py
├── query.py
├── app.py
├── config.yaml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/YourUsername/HR-Policy-Chatbot.git
cd HR-Policy-Chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Chatbot

### Using Docker Compose

```bash
docker-compose up --build
```

This starts:
- The Streamlit web app
- The vector database (Qdrant)
- The LLM backend server

---

## Accessing the Chatbot

Open your browser and navigate to:

```
http://localhost:8501
```

---

## Usage Workflow

1. Upload or load HR policy documents
2. Documents are preprocessed and split into chunks
3. Embeddings are generated and stored in the vector database
4. User submits a query via chat interface
5. Query embeddings are matched against stored vectors
6. LLM generates context-aware answers

---

## Future Enhancements
- Support for more document formats
- Add multi-user authentication and role-based access
- Cloud deployment with scalability
- Enhanced UI with chat history and analytics

---

## Author

[MANOHARA A R]

---
