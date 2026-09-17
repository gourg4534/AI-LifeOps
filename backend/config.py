from dotenv import load_dotenv
import os

load_dotenv()


APP_NAME = os.getenv("APP_NAME", "AI LifeOps")
APP_ENV = os.getenv("APP_ENV", "development")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
