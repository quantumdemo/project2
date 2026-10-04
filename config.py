import os
from pathlib import Path
from dotenv import load_dotenv

basedir = Path(__file__).resolve().parent
load_dotenv(basedir / '.env')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'primecore-industrial-dev-secret-key-2026'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{basedir / 'primecore.db'}"
    # For Vercel / serverless environment handling if sqlite is read-only in root
    if SQLALCHEMY_DATABASE_URI.startswith("sqlite:///") and os.environ.get("VERCEL"):
        SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/primecore.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
