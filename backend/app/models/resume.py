from sqlalchemy import Column, ForeignKey, Integer, String,Text
from sqlalchemy.orm import relationship

from app.database import Base


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    file_path = Column(String, nullable=False)

    extracted_text = Column(Text, nullable=True)

    text_length = Column(
    Integer,
    nullable=True,
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
    )

    owner = relationship("User")