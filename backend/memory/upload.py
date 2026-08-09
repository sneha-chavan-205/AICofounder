from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pathlib import Path
import shutil
import os

router = APIRouter(
    prefix="/memory",
    tags=["Memory"]
)

# Allowed file types
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt"}

# Maximum file size (10 MB)
MAX_FILE_SIZE = 50 * 1024 * 1024


@router.post("/upload")
async def upload_document(
    company_id: str = Form(...),
    file: UploadFile = File(...)
):
    """
    Upload a document and store it inside:
    uploads/company_id/documents/
    """

    # ==========================
    # 1. Validate File Extension
    # ==========================
    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX and TXT files are allowed."
        )

    # ==========================
    # 2. Validate File Size
    # ==========================
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 50 MB."
        )

    # Reset file pointer after reading
    file.file.seek(0)

    # ==========================
    # 3. Create Company Folder
    # ==========================
    upload_path = Path(f"uploads/{company_id}/documents")
    upload_path.mkdir(parents=True, exist_ok=True)

    # ==========================
    # 4. Save Uploaded File
    # ==========================
    file_path = upload_path / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # ==========================
    # 5. Return Success Response
    # ==========================
    return {
        "success": True,
        "message": "Document uploaded successfully.",
        "company_id": company_id,
        "filename": file.filename,
        "file_type": extension,
        "file_size_kb": round(len(contents) / 1024, 2),
        "path": str(file_path)
    }