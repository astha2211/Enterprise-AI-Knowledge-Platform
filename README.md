\# Enterprise AI Knowledge Platform



\## Overview



Enterprise AI Knowledge Platform is an AI-powered enterprise search and analytics solution built using Apache Spark, Retrieval-Augmented Generation (RAG), FAISS vector search, and a local Large Language Model (Phi-3 via Ollama).



The platform enables intelligent enterprise knowledge retrieval by combining data engineering pipelines, semantic search, vector databases, and AI-powered question answering.



\---



\## Key Features



\* Enterprise Knowledge Search

\* Retrieval-Augmented Generation (RAG)

\* Apache Spark ETL Pipelines

\* Bronze → Silver → Gold Architecture

\* Semantic Search using FAISS

\* Sentence Transformer Embeddings

\* Local LLM Inference using Phi-3

\* Interactive Analytics Dashboard

\* Enterprise Architecture Visualization



\---



\## Architecture



```text

Knowledge Base

&#x20;      ↓

Apache Spark

&#x20;      ↓

Bronze Layer

&#x20;      ↓

Silver Layer

&#x20;      ↓

Gold Layer

&#x20;      ↓

Sentence Transformers

&#x20;      ↓

FAISS Vector Database

&#x20;      ↓

Phi-3 Local LLM

&#x20;      ↓

Streamlit Dashboard

```



\---



\## Technology Stack



\### Data Engineering



\* Apache Spark

\* Pandas

\* Python



\### Artificial Intelligence



\* Retrieval-Augmented Generation (RAG)

\* Sentence Transformers

\* FAISS

\* Phi-3

\* Ollama



\### Visualization



\* Streamlit

\* Plotly



\---



\## Project Structure



```text

EnterpriseAI/



├── dashboard/

│   └── app.py



├── data/

│   ├── bronze/

│   ├── silver/

│   └── gold/



├── rag/

│   ├── enterprise\_rag.py

│   ├── embedder.py

│   └── vector\_store.py



├── spark\_jobs/

│   ├── bronze\_ingestion.py

│   ├── silver\_transform.py

│   └── gold\_analytics.py



├── images/



├── requirements.txt

├── README.md

└── .gitignore

```



\---



\## Data Pipeline



\### Bronze Layer



Raw enterprise knowledge base ingestion using Apache Spark.



\### Silver Layer



Data cleansing, deduplication, normalization, and transformation.



\### Gold Layer



Department-level analytics and business insights generation.



\---



\## AI Pipeline



1\. Enterprise documents are converted into embeddings using Sentence Transformers.

2\. Embeddings are indexed using FAISS Vector Database.

3\. User queries are embedded and matched against enterprise knowledge.

4\. Relevant documents are retrieved.

5\. Phi-3 generates context-aware responses using RAG.



\---



\## Dashboard Features



\### AI Assistant



\* Natural language querying

\* Context-aware enterprise search

\* Local AI-powered responses



\### Analytics Dashboard



\* Department-wise document distribution

\* Knowledge base analytics

\* Interactive visualizations



\### Platform Overview



\* Architecture diagram

\* Technology stack

\* System components



\---



\## Installation



```bash

git clone <repository-url>



cd EnterpriseAI



python -m venv venv



venv\\Scripts\\activate



pip install -r requirements.txt

```



\---



\## Run Application



```bash

streamlit run dashboard/app.py

```



\---



\## Future Enhancements



\* PDF document ingestion

\* Conversational memory

\* Multi-user authentication

\* MLflow experiment tracking

\* Cloud deployment (AWS/Azure)

\* Real-time knowledge synchronization



\---



\## Author



Astha Mehra



Artificial Intelligence \& Data Science



