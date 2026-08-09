from memory.parser import DocumentParser
from memory.chunker import DocumentChunker

# Step 1: Parse the document
parser = DocumentParser()

text = parser.extract_text(
    "uploads/company_001/documents/TSLA-Q2-2026-Update.pdf"
)

# Step 2: Create chunks
chunker = DocumentChunker()

chunks = chunker.create_chunks(text)

print("=" * 60)
print("CHUNKING COMPLETED")
print("=" * 60)

print(f"\nTotal Characters : {len(text)}")
print(f"Total Chunks     : {len(chunks)}")

print("\n" + "=" * 60)
print("FIRST CHUNK")
print("=" * 60)

print(chunks[0])

print("\n" + "=" * 60)
print("SECOND CHUNK")
print("=" * 60)

print(chunks[1])