import os
from dotenv import load_dotenv

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

# ==========================================
# Gemini API Key
# ==========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ==========================================
# Gemini Embedding Model
# ==========================================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "models/gemini-embedding-001"
)

# ==========================================
# Gemini Chat Model
# ==========================================

CHAT_MODEL = os.getenv(
    "CHAT_MODEL",
    "models/gemini-3.5-flash"
)

# ==========================================
# Vector Database Configuration
# ==========================================

EMBEDDING_DIMENSION = 3072

TOP_K_RESULTS = 5

# ==========================================
# Storage Configuration
# ==========================================

STORAGE_FOLDER = "storage"

UPLOAD_FOLDER = "uploads"