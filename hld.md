# High-Level Design (HLD)

## 1. System Overview

The objective of this project is to design a Retrieval-Augmented Generation (RAG) based customer support assistant that can answer user queries using a structured knowledge base.

Instead of relying solely on a language model, the system retrieves relevant information from a PDF document and uses it to generate accurate and context-aware responses. This reduces hallucination and improves reliability.

The system is designed to simulate a real-world customer support scenario where responses must be consistent, grounded, and explainable.

---

## 2. Architecture Overview

The system consists of the following major components:

- User Interface (CLI-based interaction)
- Document Processing Pipeline
- Embedding System
- Vector Database (ChromaDB)
- Retrieval Layer
- Language Model (LLM)
- Workflow Engine (LangGraph)
- Human-in-the-Loop (HITL) Module

---

## 3. Component Description

### 3.1 Document Loader
Loads the PDF knowledge base using PyPDFLoader.

### 3.2 Chunking Strategy
The document is divided into smaller chunks to improve retrieval accuracy and reduce noise.

### 3.3 Embedding Model
Sentence-transformer model is used to convert text into vector representations.

### 3.4 Vector Store
ChromaDB stores embeddings and allows efficient similarity search.

### 3.5 Retriever
Fetches top-k relevant chunks based on user query similarity.

### 3.6 Language Model
A lightweight HuggingFace model (FLAN-T5) is used to generate responses.

### 3.7 Workflow Engine
LangGraph is used to define execution flow:
- retrieval
- generation
- conditional routing

### 3.8 HITL Module
Handles escalation when:
- no relevant context is found
- query is outside knowledge base

---

## 4. Data Flow

User Query → Embedding Matching → Relevant Chunks → LLM → Final Response

If no relevant chunks are found:
→ system escalates to human

---

## 5. Technology Choices

- LangChain: orchestration
- ChromaDB: vector storage
- HuggingFace: embeddings + LLM
- LangGraph: workflow control

These were chosen to keep the system modular, interpretable, and cost-efficient.

---

## 6. Scalability Considerations

- Chunking allows handling large documents
- Vector search improves performance over full-text search
- Retrieval reduces unnecessary LLM computation

---

This makes it closer to production-level systems rather than simple chatbot implementations.