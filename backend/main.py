from fastapi import FastAPI
from .config import APP_NAME, APP_ENV

app = FastAPI(title=f"{APP_NAME} API")


@app.get("/")
def home():
    return {
        "message": f"{APP_NAME} API is running",
        "status": "success",
        "environment": APP_ENV
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": f"{APP_NAME} API"
    }