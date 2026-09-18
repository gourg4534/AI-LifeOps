from fastapi import FastAPI

from backend.config import APP_NAME, APP_ENV
from backend.routes import router

app = FastAPI(title=f"{APP_NAME} API")

app.include_router(router)


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