# 🤖 RAG-Based Customer Support Assistant

## 📌 Overview

This project implements a Retrieval-Augmented Generation (RAG) based Customer Support Assistant that answers user queries using a PDF knowledge base.

It also supports Human-in-the-Loop (HITL) escalation for complex queries using a workflow built with LangGraph.

---

## 🚀 Features

- PDF-based knowledge retrieval

- Semantic search using embeddings

- Context-aware answer generation

- Workflow orchestration using LangGraph

- Human-in-the-Loop (HITL) escalation

- Command-line interface (CLI)

---

## 🛠️ Tech Stack

- Python
  
- LangGraph

- ChromaDB (Vector Database)

- HuggingFace Embeddings

- Groq API (LLM)

- LangChain

---

## 🧠 System Architecture

User Query  
↓  
Retriever (ChromaDB)  
↓  
Relevant Chunks  
↓  
LLM (Groq)  
↓  
Decision Layer (LangGraph)  
|
├── Answer  
|
└── Escalation (HITL)   


---


## 🧪 Example Queries

### Normal Queries

What is the refund policy?  

How can I cancel my order?  

### Escalation (HITL)

I have a complex issue  

I want to talk to a human  

---

## ⚠️ Challenges

- API timeout issues

- Retrieval accuracy tuning

- Model hallucination

---

## 🚀 Future Improvements

- Web-based UI

- Multi-document support

- Chat history memory

- Cloud deployment

---

## 📌 Conclusion

This project demonstrates a scalable AI system using RAG, combining retrieval, generation, and decision-making with HITL support.
