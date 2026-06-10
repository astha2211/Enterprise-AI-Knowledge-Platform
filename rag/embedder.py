from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
    "Employees are entitled to 24 annual paid leaves.",
    "All enterprise accounts require MFA.",
    "Legacy workloads are migrated to AWS."
]

embeddings = model.encode(documents)

print("Embedding Shape:", embeddings.shape)