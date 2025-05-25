import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "info")
    TEMP_DIR = os.getenv("TEMP_DIR", "/tmp")

settings = Settings()
