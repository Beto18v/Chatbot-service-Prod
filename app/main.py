# Punto de entrada principal de la aplicación FastAPI para el microservicio Chatbot FAQ Service.
import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import chat

app = FastAPI(
    title="Chatbot FAQ Service",
    description="Microservicio para chatbot de preguntas frecuentes sobre adopción de mascotas",
    version="1.0.0"
)

# Configurar CORS
cors_origins_raw = os.getenv("CORS_ALLOW_ORIGINS", "*")
cors_origins = ["*"] if cors_origins_raw.strip() == "*" else [
    origin.strip() for origin in cors_origins_raw.split(",") if origin.strip()
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(chat.router)


@app.get("/")
async def root():
    return {"message": "Chatbot FAQ Service is running"}
