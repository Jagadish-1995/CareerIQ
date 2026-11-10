from fastapi import FastAPI

app = FastAPI(
    title="CareerIQ API",
    description="AI Career Intelligence and Interview Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to CareerIQ API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }