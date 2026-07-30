from fastapi import FastAPI
from app.database import Base, engine

import app.models
Base.metadata.create_all(bind=engine)
app = FastAPI(title="AI Resume Analyzer API")


@app.get("/")
def root():
    return {"message": "AI Resume Analyzer API is running!"}