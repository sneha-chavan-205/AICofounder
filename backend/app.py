from fastapi import FastAPI
from memory.upload import router as memory_router

app = FastAPI(
    title="AI Co-Founder API",
    version="1.0.0"
)

app.include_router(memory_router)


@app.get("/")
def home():
    return {
        "message": "AI Co-Founder API is Running 🚀"
    }