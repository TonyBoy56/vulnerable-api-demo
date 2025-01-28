import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    HOST = os.getenv("FLASK_RUN_HOST")
    PORT = int(os.getenv("FLASK_RUN_PORT", ))
    DEBUG = os.getenv("DEBUG").lower() == "true"
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")