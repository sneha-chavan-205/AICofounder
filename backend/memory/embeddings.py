from google import genai
from datetime import datetime

from memory.config import (
    GEMINI_API_KEY,
    EMBEDDING_MODEL
)

# Create Gemini Client
client = genai.Client(api_key=GEMINI_API_KEY)


def generate_embedding(text: str):
    """
    Generate embedding for a single text chunk.
    """

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return response.embeddings[0].values


def generate_document_store(
    company_id: str,
    document_name: str,
    document_type: str,
    chunks: list[str]
):
    """
    Generate document store with metadata and embeddings.
    """

    document_store = []

    upload_time = datetime.now().isoformat()

    for idx, chunk in enumerate(chunks):

        embedding = generate_embedding(chunk)

        document_store.append({

            "chunk_id": idx,

            "company_id": company_id,

            "document_name": document_name,

            "document_type": document_type,

            "uploaded_at": upload_time,

            "chunk_text": chunk,

            "embedding": embedding

        })

    return document_store