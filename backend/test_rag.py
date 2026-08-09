from memory.rag import RAGEngine

# Initialize RAG Engine
rag = RAGEngine("company_001")

# Ask a question
question = "What was Tesla's revenue?"

print("=" * 60)
print("QUESTION")
print("=" * 60)
print(question)

print()

# Generate answer
answer = rag.ask(question)

print("=" * 60)
print("ANSWER")
print("=" * 60)
print(answer)