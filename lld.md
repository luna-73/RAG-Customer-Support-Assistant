# Low-Level Design (LLD)

## 1. Module-Level Design

### 1.1 Document Processing Module
Responsible for:
- loading PDF
- splitting into chunks
- preparing text for embedding

### 1.2 Chunking Module
Uses recursive splitting with overlap to maintain context continuity.

### 1.3 Embedding Module
Transforms text chunks into dense vectors using a sentence-transformer model.

### 1.4 Vector Storage Module
Stores embeddings in ChromaDB for efficient similarity search.

### 1.5 Retrieval Module
- Takes user query
- converts it into embedding
- retrieves top-k similar chunks

### 1.6 Query Processing Module
Combines retrieved context with query to form final prompt.

### 1.7 Graph Execution Module
Implemented using LangGraph:
- retrieve node
- generate node
- conditional routing

### 1.8 HITL Module
Triggered when:
- no context is retrieved
- answer confidence is low

---

## 2. Data Structures

### Document Chunk
- text content
- metadata (page number, source)

### Embedding
- vector representation of text

### State Object (LangGraph)
- query
- docs
- answer
- escalation flag

---

## 3. Workflow Design

1. User inputs query  
2. Retriever fetches relevant chunks  
3. LLM generates answer using context  
4. System checks for escalation  
5. Either:
   - returns answer  
   - or routes to human  

---

## 4. Conditional Routing Logic

Escalation is triggered when:
- no documents are retrieved
- generated response lacks relevance
- query is out-of-domain

---

## 5. API / Interaction Design

Input:
- user query (string)

Output:
- generated response (string)

Interaction is synchronous via CLI.

---

## 6. Error Handling

Handled cases include:
- empty retrieval results
- malformed input
- model generation issues

Fallback:
- return default message
- escalate to human

---

## 7. Design Decisions

- Smaller chunk size for better precision
- Top-k retrieval to reduce noise
- Prompt constraints to avoid repetition

---

## 8. System Behavior

The system is deterministic in retrieval but generative in response, ensuring a balance between accuracy and flexibility.