from memory.retriever import Retriever

retriever = Retriever("company_001")

query = "What is Tesla's revenue?"

results = retriever.retrieve(
    query=query,
    top_k=3
)

print("=" * 60)
print("TOP SEARCH RESULTS")
print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\nResult {i}")

    print(f"Distance : {result['distance']}")

    print(f"Document : {result['metadata']['document_name']}")

    print(f"Chunk ID : {result['metadata']['chunk_id']}")

print("\n")

print("=" * 60)
print("FORMATTED CONTEXT")
print("=" * 60)

context = retriever.format_context(results)

print(context)