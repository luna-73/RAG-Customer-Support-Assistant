RAG-Based Customer Support Assistant
A Retrieval-Augmented Generation (RAG) based customer support assistant built using LangChain, LangGraph, ChromaDB, and HuggingFace models.
The system retrieves relevant information from a PDF knowledge base and generates context-aware responses instead of relying purely on language model generation. It also includes a simple Human-in-the-Loop (HITL) fallback mechanism for queries where relevant context is unavailable.

Features
* PDF-based knowledge retrieval
* Semantic search using embeddings
* Vector storage with ChromaDB
* Context-aware response generation
* Workflow orchestration using LangGraph
* Human-in-the-Loop escalation
* Fully local setup (no paid APIs required)

Tech Stack
* Python
* LangChain
* LangGraph
* ChromaDB
* Sentence Transformers
* HuggingFace Transformers
* FLAN-T5
* PyPDF

