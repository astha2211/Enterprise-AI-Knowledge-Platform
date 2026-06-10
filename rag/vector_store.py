import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load enterprise knowledge base
df = pd.read_csv("data/silver/silver_data.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create embeddings
documents = df["content"].tolist()
embeddings = model.encode(documents)

# Convert to float32 for FAISS
embeddings = np.array(embeddings).astype("float32")

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)

# Add embeddings
index.add(embeddings)

print(f"Documents Indexed: {index.ntotal}")

# Example query
query = "How many annual leaves do employees get?"

query_embedding = model.encode([query])
query_embedding = np.array(query_embedding).astype("float32")

# Search
k = 3
distances, indices = index.search(query_embedding, k)

print("\nTop Matches:\n")

for idx in indices[0]:
    print(df.iloc[idx]["title"])
    print(df.iloc[idx]["content"])
    print("-" * 60)