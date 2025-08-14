# app/main.py
from fastapi import FastAPI
from app.api.endpoints import router as api_router
from core.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        debug=settings.DEBUG_MODE,
        docs_url="/docs" if settings.DEBUG_MODE else None,
        redoc_url="/redoc" if settings.DEBUG_MODE else None,
    )
    app.include_router(api_router, prefix="/api/v1")

    @app.on_event("startup")
    async def startup_event():
        print(f"{settings.APP_NAME} v{settings.APP_VERSION} starting up...")
        # Future: Initialize DB connections, LLM clients, etc.

    @app.on_event("shutdown")
    async def shutdown_event():
        print(f"{settings.APP_NAME} shutting down...")
        # Future: Close DB connections, clean up resources

    return app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    # Make sure to run from the project root: uvicorn app.main:app --reload
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=settings.DEBUG_MODE)