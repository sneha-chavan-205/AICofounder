from memory.parser import DocumentParser
from memory.chunker import DocumentChunker
from memory.embeddings import generate_document_store

# =====================================================
# Test File Information
# =====================================================

file_path = "uploads/company_001/documents/TSLA-Q2-2026-Update.pdf"

company_id = "company_001"

document_name = "TSLA-Q2-2026-Update.pdf"

document_type = "financial_report"

# =====================================================
# Step 1 : Parse Document
# =====================================================

parser = DocumentParser()

text = parser.extract_text(file_path)

# =====================================================
# Step 2 : Create Chunks
# =====================================================

chunker = DocumentChunker()

chunks = chunker.create_chunks(text)

# =====================================================
# Step 3 : Generate Document Store
# =====================================================

document_store = generate_document_store(
    company_id=company_id,
    document_name=document_name,
    document_type=document_type,
    chunks=chunks
)

# =====================================================
# Output
# =====================================================

print("=" * 70)
print("DOCUMENT STORE CREATED SUCCESSFULLY")
print("=" * 70)

print(f"Company ID        : {company_id}")
print(f"Document Name     : {document_name}")
print(f"Document Type     : {document_type}")
print(f"Total Chunks      : {len(document_store)}")

print("\nMetadata Fields")

print(document_store[0].keys())

print("\n" + "=" * 70)
print("FIRST CHUNK DETAILS")
print("=" * 70)

print(f"Chunk ID          : {document_store[0]['chunk_id']}")
print(f"Company ID        : {document_store[0]['company_id']}")
print(f"Document Name     : {document_store[0]['document_name']}")
print(f"Document Type     : {document_store[0]['document_type']}")
print(f"Uploaded At       : {document_store[0]['uploaded_at']}")

print("\nChunk Preview:\n")

print(document_store[0]["chunk_text"][:400])

print("\nEmbedding Dimension :")

print(len(document_store[0]["embedding"]))

print("\nFirst 10 Embedding Values:\n")

print(document_store[0]["embedding"][:10])

print("\n" + "=" * 70)
print("DOCUMENT STORE READY FOR FAISS")
print("=" * 70)