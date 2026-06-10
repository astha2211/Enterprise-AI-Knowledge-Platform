import pandas as pd
import faiss
import numpy as np
import ollama
from sentence_transformers import SentenceTransformer

print("Loading enterprise knowledge base...")

# Load data
df = pd.read_csv("data/silver/silver_data.csv")

# Embedding model
embed_model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
documents = df["content"].tolist()
embeddings = embed_model.encode(documents)

embeddings = np.array(embeddings).astype("float32")

# Build vector index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print(f"Indexed {index.ntotal} enterprise documents")


def retrieve_context(query, top_k=3):
    query_embedding = embed_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    context = ""

    for idx in indices[0]:
        context += (
            f"Title: {df.iloc[idx]['title']}\n"
            f"Department: {df.iloc[idx]['department']}\n"
            f"Content: {df.iloc[idx]['content']}\n\n"
        )

    return context


while True:

    query = input("\nAsk a question (type exit to quit): ")

    if query.lower() == "exit":
        break

    context = retrieve_context(query)

    prompt = f"""
You are an enterprise knowledge assistant.

Answer ONLY from the provided context.

Context:
{context}

Question:
{query}

Answer:
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

    print("\nAnswer:\n")
    print(response["message"]["content"])