# app/core/config.py
import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional # Add this import 👈

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    APP_NAME: str = "Chatbot Backend"
    APP_VERSION: str = "0.1.0"
    DEBUG_MODE: bool = True

    LLM_PROVIDER: str = "openai"
    # Change 'str | None' to 'Optional[str]' here 👇
    OPENAI_API_KEY: Optional[str] = None
    # And also here 👇
    LLAMA_API_URL: Optional[str] = None # For local Llama models (e.g., Ollama)

    DATABASE_URL: Optional[str] = None # This line was already changed

settings = Settings()