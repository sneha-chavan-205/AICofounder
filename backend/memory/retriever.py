from memory.embeddings import generate_embedding
from memory.vector_db import VectorDatabase


class Retriever:
    """
    Retrieves the most relevant chunks
    from the company's vector database.
    """

    def __init__(self, company_id: str):
        """
        Initialize retriever for a company.
        """

        self.company_id = company_id

        # Load Vector Database
        self.vector_db = VectorDatabase(company_id)

        self.vector_db.load()

    def embed_query(self, query: str):
        """
        Convert the user query into an embedding.
        """

        return generate_embedding(query)

    def retrieve(self, query: str, top_k: int = 5):
        """
        Retrieve the top-k most relevant chunks.
        """

        query_embedding = self.embed_query(query)

        results = self.vector_db.search(
            query_embedding=query_embedding,
            top_k=top_k
        )

        return results

    def format_context(self, results):
        """
        Convert retrieved chunks into a context
        that will be sent to Gemini.
        """

        context = ""

        for i, result in enumerate(results, start=1):

            metadata = result["metadata"]

            context += f"""
===============================
Document {i}
===============================

Document Name:
{metadata['document_name']}

Document Type:
{metadata['document_type']}

Chunk ID:
{metadata['chunk_id']}

Content:
{metadata['chunk_text']}


"""

        return context