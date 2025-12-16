from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import chat, health, selected_text
from config.settings import settings


def create_app():
    app = FastAPI(
        title="RAG Chatbot for Physical AI & Humanoid Robotics Learning",
        description="A Retrieval-Augmented Generation chatbot that answers questions from the book content",
        version="1.0.0"
    )

    # Add CORS middleware for Vercel frontend integration
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # In production, specify exact frontend URL
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include API routes
    app.include_router(chat.router, prefix="/api", tags=["chat"])
    app.include_router(selected_text.router, prefix="/api", tags=["selected-text"])
    app.include_router(health.router, prefix="/api", tags=["health"])

    return app


app = create_app()


@app.get("/")
def root():
    return {"message": "RAG Chatbot API for Physical AI & Humanoid Robotics Learning"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)