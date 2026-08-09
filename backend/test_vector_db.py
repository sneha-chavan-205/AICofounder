from memory.parser import DocumentParser
from memory.chunker import DocumentChunker
from memory.embeddings import generate_document_store
from memory.vector_db import VectorDatabase

# --------------------------------------------------
# Document Details
# --------------------------------------------------

file_path = "uploads/company_001/documents/TSLA-Q2-2026-Update.pdf"

company_id = "company_001"
document_name = "TSLA-Q2-2026-Update.pdf"
document_type = "financial_report"

# --------------------------------------------------
# Parse Document
# --------------------------------------------------

parser = DocumentParser()
text = parser.extract_text(file_path)

# --------------------------------------------------
# Create Chunks
# --------------------------------------------------

chunker = DocumentChunker()
chunks = chunker.create_chunks(text)

# --------------------------------------------------
# Generate Document Store
# --------------------------------------------------

document_store = generate_document_store(
    company_id=company_id,
    document_name=document_name,
    document_type=document_type,
    chunks=chunks
)

# --------------------------------------------------
# Create Vector Database
# --------------------------------------------------

db = VectorDatabase(company_id)

# --------------------------------------------------
# Add Documents
# --------------------------------------------------

db.add_documents(document_store)

# --------------------------------------------------
# Save Database
# --------------------------------------------------

db.save()

# --------------------------------------------------
# Load Database Again
# --------------------------------------------------

db.load()

# --------------------------------------------------
# Print Results
# --------------------------------------------------

print("=" * 60)
print("FAISS DATABASE CREATED")
print("=" * 60)

print("Company ID:", company_id)
print("Storage Path:", db.storage_path)
print("Metadata File:", db.metadata_path)
print("FAISS Index:", db.index_path)

print()

print("Embedding Dimension:", db.embedding_dimension)
print("Total Vectors:", db.index.ntotal)
print("Total Metadata:", len(db.metadata))