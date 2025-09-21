# /backend/app/config.py
import os
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file for local development

class Config:
    """Application configuration class."""
    DB_TYPE = os.environ.get('DB_TYPE', 'mysql') # 'mysql' or 'mssql'
    DB_USER = os.environ.get('DB_USER')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'your-secret-key')
    

    if DB_TYPE == 'mysql':
        # MySQL connection string
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
    elif DB_TYPE == 'mssql':
        # MSSQL connection string
        SQLALCHEMY_DATABASE_URI = (
            f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
            "?driver=ODBC+Driver+17+for+SQL+Server"
        )
    else:
        raise ValueError("Unsupported DB_TYPE. Choose 'mysql' or 'mssql'.")

    SQLALCHEMY_TRACK_MODIFICATIONS = False