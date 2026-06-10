import ollama

response = ollama.chat(
    model="phi3",
    messages=[
        {
            "role": "user",
            "content": "What is Apache Spark?"
        }
    ]
)

print(response["message"]["content"])