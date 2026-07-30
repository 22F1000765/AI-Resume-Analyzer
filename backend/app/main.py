from fastapi import FastAPI
from app.database import Base, engine

from app.routers import auth,resume



import app.models
Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Resume Analyzer API")
app.include_router(auth.router)
app.include_router(resume.router)


@app.get("/")
def root():
    return {"message": "AI Resume Analyzer API is running!"}