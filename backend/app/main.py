from fastapi import FastAPI

app = FastAPI(title="AI Resume Analyzer API")


@app.get("/")
def root():
    return {"message": "AI Resume Analyzer API is running!"}