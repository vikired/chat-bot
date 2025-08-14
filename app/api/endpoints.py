# app/api/endpoints.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from core.config import settings # Import settings here 👈

router = APIRouter()

class ChatRequest(BaseModel):
    query: str

class ChatResponse(BaseModel):
    response: str
    intent: Optional[str] = None

@router.get("/health")
async def health_check():
    """
    Basic health check endpoint to ensure the server is running.
    """
    return {"status": "ok", "message": "Chatbot backend is healthy!"}

# Add this new endpoint temporarily
@router.get("/debug-status")
async def get_debug_status():
    """
    Returns the current DEBUG_MODE setting.
    """
    return {"debug_mode": settings.DEBUG_MODE}

@router.post("/chat", response_model=ChatResponse)
async def chat_with_bot(request: ChatRequest):
    """
    Main endpoint for user queries.
    This is a placeholder and will be expanded significantly.
    """
    dummy_intent = "unclassified"
    dummy_response = f"Received your query: '{request.query}'. Processing intent '{dummy_intent}'... (This is a dummy response)"

    return ChatResponse(response=dummy_response, intent=dummy_intent)