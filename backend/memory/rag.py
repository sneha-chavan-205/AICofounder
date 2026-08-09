from google import genai

from memory.config import (
    GEMINI_API_KEY,
    CHAT_MODEL
)

from memory.retriever import Retriever


class RAGEngine:
    """
    Retrieval Augmented Generation Engine.

    Retrieves relevant company information from the
    vector database and generates an answer using Gemini.
    """

    def __init__(self, company_id: str):
        """
        Initialize RAG Engine.
        """

        self.company_id = company_id

        # Gemini Client
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

        # Retriever
        self.retriever = Retriever(company_id)

    def build_prompt(self, query: str, context: str):
        """
        Build the prompt for Gemini.
        """

        prompt = f"""
You are an AI Co-Founder.

Your job is to answer the user's question ONLY using the provided company documents.

Rules:
1. Answer only from the provided company knowledge.
2. Do not make up information.
3. If the answer is not available in the context, reply exactly:
   "I couldn't find this information in the uploaded company documents."
4. Keep answers concise and professional.

==================================================
COMPANY KNOWLEDGE
==================================================

{context}

==================================================
USER QUESTION
==================================================

{query}

==================================================
ANSWER
==================================================
"""

        return prompt

    def ask(self, query: str):
        """
        Generate answer for a user query.
        """

        # Retrieve relevant chunks
        results = self.retriever.retrieve(
            query=query,
            top_k=5
        )

        # Convert chunks into context
        context = self.retriever.format_context(results)

        # Build Gemini prompt
        prompt = self.build_prompt(
            query=query,
            context=context
        )

        # Generate answer
        response = self.client.models.generate_content(
            model=CHAT_MODEL,
            contents=prompt
        )

        return response.text

    def ask_with_sources(self, query: str):
        """
        Generate answer along with retrieved chunks.
        Useful for debugging and evaluation.
        """

        results = self.retriever.retrieve(
            query=query,
            top_k=5
        )

        context = self.retriever.format_context(results)

        prompt = self.build_prompt(
            query=query,
            context=context
        )

        response = self.client.models.generate_content(
            model=CHAT_MODEL,
            contents=prompt
        )

        return {
            "question": query,
            "answer": response.text,
            "retrieved_chunks": results
        }