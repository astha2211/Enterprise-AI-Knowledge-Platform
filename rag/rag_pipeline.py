import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load enterprise documents
df = pd.read_csv("data/silver/silver_data.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
documents = df["content"].tolist()
embeddings = model.encode(documents)

embeddings = np.array(embeddings).astype("float32")

# Build FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)


def retrieve_context(query, top_k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append({
            "title": df.iloc[idx]["title"],
            "content": df.iloc[idx]["content"],
            "department": df.iloc[idx]["department"]
        })

    return results


if __name__ == "__main__":

    query = input("Ask a question: ")

    results = retrieve_context(query)

    print("\nRelevant Documents:\n")

    for doc in results:
        print(f"Title: {doc['title']}")
        print(f"Department: {doc['department']}")
        print(f"Content: {doc['content']}")
        print("-" * 60)