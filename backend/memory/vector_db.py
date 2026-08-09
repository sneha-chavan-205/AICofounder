import os
import json
import faiss
import numpy as np


class VectorDatabase:
    """
    Handles FAISS vector storage and metadata
    for each company.
    """

    def __init__(self, company_id: str, embedding_dimension: int = 3072):

        self.company_id = company_id
        self.embedding_dimension = embedding_dimension

        # Storage folder
        self.storage_path = self.get_company_storage()

        # Metadata file
        self.metadata_path = os.path.join(
            self.storage_path,
            "metadata.json"
        )

        # FAISS index file
        self.index_path = os.path.join(
            self.storage_path,
            "faiss.index"
        )

        # Metadata list
        self.metadata = []

        # FAISS Index
        self.index = self.create_index()

    def get_company_storage(self):
        """
        Returns company storage folder.
        Creates it if it doesn't exist.
        """

        path = os.path.join(
            "storage",
            self.company_id
        )

        os.makedirs(path, exist_ok=True)

        return path

    def create_index(self):
        """
        Creates an empty FAISS index.
        """

        index = faiss.IndexFlatL2(
            self.embedding_dimension
        )

        return index

    def add_documents(self, document_store):
        """
        Add document embeddings and metadata
        to the FAISS index.
        """

        embeddings = []

        for document in document_store:

            embeddings.append(document["embedding"])

            metadata = {
                "chunk_id": document["chunk_id"],
                "company_id": document["company_id"],
                "document_name": document["document_name"],
                "document_type": document["document_type"],
                "uploaded_at": document["uploaded_at"],
                "chunk_text": document["chunk_text"]
            }

            self.metadata.append(metadata)

        embeddings = np.array(
            embeddings,
            dtype=np.float32
        )

        self.index.add(embeddings)

        print(f"Added {len(embeddings)} vectors to FAISS.")

    def save(self):
        """
        Saves FAISS index and metadata.
        """

        # Save FAISS index
        faiss.write_index(
            self.index,
            self.index_path
        )

        # Save metadata
        with open(
            self.metadata_path,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                self.metadata,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Database saved successfully.")

    def load(self):
        """
        Loads FAISS index and metadata.
        """

        if os.path.exists(self.index_path):

            self.index = faiss.read_index(
                self.index_path
            )

        if os.path.exists(self.metadata_path):

            with open(
                self.metadata_path,
                "r",
                encoding="utf-8"
            ) as file:

                self.metadata = json.load(file)

        print("Database loaded successfully.")

    def search(self, query_embedding, top_k=5):
        """
        Searches the FAISS database
        and returns the most similar chunks.
        """

        query_embedding = np.array(
            [query_embedding],
            dtype=np.float32
        )

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for distance, index in zip(
            distances[0],
            indices[0]
        ):

            if index == -1:
                continue

            result = {
                "distance": float(distance),
                "metadata": self.metadata[index]
            }

            results.append(result)

        return results