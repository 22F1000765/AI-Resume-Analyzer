import os
import shutil

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.resume import ResumeAnalysisPreview
from app.services.resume_service import create_resume, update_resume_text,get_resume_by_id
from app.utils.pdf_parser import extract_text_from_pdf,detect_sections
from app.models.resume import Resume

router = APIRouter(
    prefix="/resume",
    tags=["Resume"],
)


@router.post(
    "/upload",
    response_model=ResumeAnalysisPreview,
    status_code=status.HTTP_201_CREATED,
)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed.",
        )

    upload_dir = "uploads"

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(
        upload_dir,
        file.filename,
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer,
        )

    resume = create_resume(
        db=db,
        filename=file.filename,
        file_path=file_path,
        user_id=1,
    )

    text = extract_text_from_pdf(file_path)
    

    sections = detect_sections(text)

    resume = update_resume_text(
        db,
        resume,
        text,
)

    return {
    "filename": resume.filename,
    "characters": len(resume.extracted_text),
    "preview": resume.extracted_text[:500],
    }

@router.get("/{resume_id}")

def get_resume(
    resume_id: int,
    db: Session = Depends(get_db),
):
    resume = get_resume_by_id(db,
                              resume_id
    )

    if not resume:
        raise HTTPException(
            status_code=404,
            detail="Resume not found",
        )

    return {
        "id": resume.id,
        "filename": resume.filename,
        "text_length": resume.text_length,
        "preview": resume.extracted_text[:500],
    }