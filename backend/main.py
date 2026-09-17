from fastapi import FastAPI
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "AI LifeOps API"))


@app.get("/")
def home():
    return {
        "message": "AI LifeOps API is running",
        "status": "success",
        "environment": os.getenv("APP_ENV", "unknown")
    }