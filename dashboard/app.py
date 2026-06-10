import streamlit as st
import pandas as pd
import faiss
import numpy as np
import plotly.express as px
import ollama
from sentence_transformers import SentenceTransformer

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="Enterprise AI Knowledge Platform",
    page_icon="🤖",
    layout="wide"
)
st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    background: linear-gradient(
        135deg,
        #1f2937,
        #111827
    );

    padding: 2rem;

    border-radius: 15px;

    margin-bottom: 2rem;

    border: 1px solid #374151;
}

.hero h1 {
    color: white;
}

.hero p {
    color: #D1D5DB;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">

<h1>
🏢 Enterprise AI Knowledge Platform
</h1>

<p>
AI-Powered Enterprise Search,
Analytics & Knowledge Retrieval
</p>

</div>
""", unsafe_allow_html=True)

# ---------------------------
# TABS
# ---------------------------

tab1, tab2, tab3 = st.tabs([
    "🤖 AI Assistant",
    "📊 Analytics",
    "🏢 Platform Overview"
])

# ---------------------------
# LOAD MODELS & DATA
# ---------------------------

@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


@st.cache_data
def load_data():
    return pd.read_csv("data/silver/silver_data.csv")


df = load_data()
embed_model = load_model()

# ---------------------------
# BUILD FAISS INDEX
# ---------------------------

@st.cache_resource
def build_index():

    documents = df["content"].tolist()

    embeddings = embed_model.encode(documents)
    embeddings = np.array(embeddings).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index


index = build_index()

# ---------------------------
# RETRIEVAL FUNCTION
# ---------------------------

def retrieve_context(query, top_k=3):

    query_embedding = embed_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    _, indices = index.search(query_embedding, top_k)

    context = ""

    for idx in indices[0]:
        context += (
            f"Title: {df.iloc[idx]['title']}\n"
            f"Department: {df.iloc[idx]['department']}\n"
            f"Content: {df.iloc[idx]['content']}\n\n"
        )

    return context

# ============================================================
# TAB 1 : AI ASSISTANT
# ============================================================

with tab1:

    st.subheader("Enterprise Knowledge Assistant")

    question = st.text_area(
        "Ask an Enterprise Question",
        height=120
    )

    if st.button("Get Answer") and question:

        context = retrieve_context(question)

        st.info("Retrieved 3 relevant documents")

        prompt = f"""
You are an Enterprise AI Knowledge Assistant.

Instructions:
- Answer using complete sentences.
- Use ONLY the information provided in the context.
- Do not return only numbers or fragments.

Context:
{context}

Question:
{question}

Provide a professional answer:
"""

        response = ollama.chat(
            model="phi3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.divider()

        col1, col2 = st.columns([2, 1])

        with col1:

            st.subheader("🤖 AI Response")

            st.success(
                response["message"]["content"]
            )

        with col2:

            st.subheader("📄 Retrieved Sources")

            st.code(context)
# ============================================================
# TAB 2 : ANALYTICS
# ============================================================

with tab2:

    st.header("📊 Department Analytics Dashboard")

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Knowledge Docs", len(df))

    with col2:
        st.metric("Departments", df["department"].nunique())

    with col3:
        st.metric("Vector Index Size", index.ntotal)

    with col4:
        st.metric("AI Model", "Phi-3")

    analytics_df = pd.read_csv(
        "data/gold/department_analytics.csv"
    )

    st.subheader("Department Summary")

    st.dataframe(
        analytics_df,
        width="stretch"
    )

    # PIE CHART
    fig = px.pie(
        analytics_df,
        names="department",
        values="count",
        title="Department Distribution"
    )

    st.plotly_chart(
        fig,
        width="stretch"
    )

    # BAR CHART
    st.subheader("Department-wise Document Count")

    st.bar_chart(
        analytics_df.set_index("department")
    )

# ============================================================
# TAB 3 : PLATFORM OVERVIEW
# ============================================================

with tab3:

    st.header("🏢 Enterprise AI Architecture")

    st.image(
    "images/architecture.png",
     width="stretch"
)

    st.subheader("Platform Components")

    st.markdown("""
✅ Apache Spark ETL Pipelines

✅ Bronze → Silver → Gold Architecture

✅ Sentence Transformer Embeddings

✅ FAISS Vector Search

✅ Retrieval-Augmented Generation (RAG)

✅ Phi-3 Local LLM

✅ Streamlit Analytics Dashboard

✅ Enterprise Knowledge Retrieval
""")

    st.subheader("Technology Stack")

    st.markdown("""
- Apache Spark
- Python
- FAISS
- Sentence Transformers
- Phi-3
- Ollama
- Streamlit
- Pandas
- Plotly
""")