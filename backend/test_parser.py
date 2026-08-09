from memory.parser import DocumentParser

# Create parser object
parser = DocumentParser()

# Path to the uploaded document
file_path = "uploads/company_001/documents/TSLA-Q2-2026-Update.pdf"

# Extract text
text = parser.extract_text(file_path)

print("=" * 60)
print("DOCUMENT PARSED SUCCESSFULLY")
print("=" * 60)

print(f"\nTotal Characters: {len(text)}")

print("\nFirst 1000 Characters:\n")
print(text[:1000])