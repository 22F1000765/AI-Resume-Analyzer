from sqlalchemy.orm import Session

from app.models.resume import Resume



def create_resume(
    db: Session,
    filename: str,
    file_path: str,
    user_id: int,
):
    resume = Resume(
        filename=filename,
        file_path=file_path,
        user_id=user_id,
    )

    db.add(resume)
    db.commit()
    db.refresh(resume)

    return resume

def update_resume_text(
    db: Session,
    resume: Resume,
    extracted_text: str,
):
    resume.extracted_text = extracted_text
    resume.text_length = len(extracted_text)

    db.commit()

    db.refresh(resume)

    return resume