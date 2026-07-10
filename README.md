# ML-LS-2026

IITB Insti Assist is a RAG based AI assistant that answers questions about IITB academics and institute procedures using verified documents.

The assistant retrieves relevant information from insti documents before generating responses, reducing hallucinations and also ensuring source grounded answers.

---

## Features

- Document Question Answering using RAG
- Transformer based MiniLM embeddings
- FAISS vector similarity search
- Chunking that is paragraph aware
- LLM response generation
- Source citation also with retrieved evidence
- Confidence score and grounding indicator
- Custom PDF upload is supported
- Streamlit web interface

---

## System Pipeline

```
User Query
     |
     v
Query Embedding (MiniLM)
     |
     v
FAISS Similarity Search
     |
     v
Retrieve Relevant Chunks
     |
     v
Put Retrieved Context into LLM
     |
     v
Generate Grounded Response
```

---

## Tech Stack

- Python
- Streamlit
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FAISS
- PyMuPDF
- LLM API
- NumPy

---

## Project Structure (Important files

```
Week 4/

├── app.py                 # Streamlit UI
│
├── src/
│   ├── builc.py          # Document loading
│   ├── chunk.py         # Text chunking
│   ├── embed.py        # Embedding generation
│   ├── loader.py         # Document loading
│   ├── rag.py             # RAG pipeline
│   └── pdf_rag.py         # Upload pdf
│   └── retreiver.py        # retreive relevant chunks
│   └── vector_store.py     # stores FAISS vectoring 
│
├── data/                  # Source documents
├── index/                 # Stored FAISS index
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/arnavvp/ML-LS-2026.git

cd ML-LS-2026/"Week 4"
```

---

### 2. Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Setup Environment Variables

Create a `.env` file:

```
API_KEY=your_api_key_here
```

---

## Running the Application

Start the Streamlit server:

```bash
streamlit run app.py
```

Open the displayed local URL:

```
http://localhost:8501
```

---

## Example Questions

```
What is Category VI?

What are the eligibility criteria for IDDDP?

When does the semester begin?

What happens in case of academic malpractice?
```

---

## Custom PDF Uploading

You can upload your own PDF through interface.

The system automatically:

1. Extracts document text
2. Creates chunks
3. Generates embeddings
4. Builds a FAISS index
5. Enables question answering over the uploaded document

---

## Future Improvements

- OCR support for scanned PDFs
- Hybrid keyword + vector retrieval
- Larger institute knowledge base
- Cloud deployment
