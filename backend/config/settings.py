from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    # API Keys
    cohere_api_key: str
    gemini_api_key: str
    qdrant_api_key: Optional[str] = None
    qdrant_url: str
    database_url: str

    # Application Settings
    environment: str = "development"
    log_level: str = "info"

    # Qdrant Settings
    qdrant_collection_name: str = "book_content"

    # Model Settings
    gemini_model: str = "gemini-pro"
    cohere_model: str = "embed-multilingual-v3.0"

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()