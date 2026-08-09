import fitz  # PyMuPDF
from docx import Document
from pathlib import Path


class DocumentParser:
    """
    Handles text extraction from PDF, DOCX and TXT files.
    """

    def extract_text(self, file_path: str) -> str:

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return self._extract_pdf(file_path)

        elif extension == ".docx":
            return self._extract_docx(file_path)

        elif extension == ".txt":
            return self._extract_txt(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")

    def _extract_pdf(self, file_path: str) -> str:

        document = fitz.open(file_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        return text

    def _extract_docx(self, file_path: str) -> str:

        document = Document(file_path)

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    def _extract_txt(self, file_path: str) -> str:

        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()