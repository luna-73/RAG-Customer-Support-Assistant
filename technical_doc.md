# Technical Documentation

## 1. Introduction

RAG combines retrieval with generation to improve answer accuracy.

## 2. System Design

- PDF → Chunking → Embedding → Storage
- Query → Retrieval → LLM → Answer

## 3. Design Decisions

- Chunk size optimized for context quality
- Top-k retrieval to reduce noise
- Prompt designed to avoid repetition

## 4. Workflow

LangGraph handles:
- retrieval
- generation
- routing

## 5. Conditional Logic

- If no docs → escalate
- If weak answer → escalate

## 6. HITL

Allows manual intervention for:
- complex queries
- missing context

## 7. Challenges

- repetitive outputs
- chunk overlap
- prompt tuning

## 8. Future Improvements

- better models
- reranking
- UI integration