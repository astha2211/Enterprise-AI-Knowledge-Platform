<div align="center">

  <h1>🚀 Enterprise AI Knowledge Platform</h1>
  <p><b>An intelligent, scalable search and analytics solution powered by RAG, Apache Spark, and Local LLMs.</b></p>

  <a href="https://spark.apache.org/"><img src="https://img.shields.io/badge/Apache_Spark-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white" alt="Spark"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://github.com/facebookresearch/faiss"><img src="https://img.shields.io/badge/FAISS-Vector_Search-000000?style=for-the-badge&logo=facebook&logoColor=white" alt="FAISS"></a>
  <img src="https://img.shields.io/badge/Phi--3-Local_LLM-0078D4?style=for-the-badge" alt="Phi-3">

</div>

<br/>

## 📖 Overview

The **Enterprise AI Knowledge Platform** is a robust, end-to-end knowledge retrieval and analytics system. It bridges the gap between raw enterprise data and actionable intelligence by combining heavy-duty data engineering pipelines with cutting-edge Artificial Intelligence. 

By utilizing a **Bronze-Silver-Gold architecture** alongside a **Retrieval-Augmented Generation (RAG)** pipeline powered by a local Phi-3 model, this platform ensures fast, secure, and context-aware enterprise search capabilities.

---

## ✨ Key Features

* **🔍 Enterprise Knowledge Search:** Lightning-fast semantic search across vast document repositories.
* **🧠 Retrieval-Augmented Generation (RAG):** Contextually accurate AI answers grounded in your specific enterprise data.
* **⚙️ Apache Spark ETL Pipelines:** Scalable data ingestion and processing.
* **🏗️ Medallion Architecture:** Structured data flow from Bronze (raw) → Silver (cleaned) → Gold (analytics).
* **📐 Vector Search:** Powered by Sentence Transformer embeddings and FAISS vector databases.
* **🔒 Local LLM Inference:** Utilitzing Phi-3 via Ollama for secure, on-premise AI processing.
* **📊 Interactive Dashboard:** Rich, intuitive analytics and search interface.

---

## 🛠️ Technology Stack

### Data Engineering
![Apache Spark](https://img.shields.io/badge/Apache%20Spark-F16629.svg?style=flat&logo=Apache-Spark&logoColor=white) 
![Pandas](https://img.shields.io/badge/pandas-150458.svg?style=flat&logo=pandas&logoColor=white) 
![Python](https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white)

### Artificial Intelligence & Machine Learning
![HuggingFace](https://img.shields.io/badge/Sentence%20Transformers-FF9D00.svg?style=flat&logo=Hugging-Face&logoColor=white) 
![FAISS](https://img.shields.io/badge/FAISS-Vector_Store-black.svg?style=flat) 
![Phi3](https://img.shields.io/badge/Phi--3-Local_LLM-blue.svg?style=flat) 
![Ollama](https://img.shields.io/badge/Ollama-Local_Inference-lightgrey.svg?style=flat)

### Visualization & UI
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=flat&logo=Streamlit&logoColor=white) 
![Plotly](https://img.shields.io/badge/Plotly-3F4F75.svg?style=flat&logo=Plotly&logoColor=white)

---

### System Flow
```mermaid
graph TD
    A[Knowledge Base] -->|Apache Spark| B(Bronze Layer)
    B -->|Clean & Transform| C(Silver Layer)
    C -->|Analytics| D(Gold Layer)
    C -->|Embeddings| E[Sentence Transformers]
    E --> F[(FAISS Vector DB)]
    F -->|Context Retrieval| G{Phi-3 Local LLM}
    G --> H[Streamlit Dashboard]