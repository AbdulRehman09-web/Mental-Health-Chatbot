import os
import re

from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from models import ChatRequest
from crisis import check_for_crisis, SAFETY_MESSAGES
from logger import log_interaction
from doc_engine import get_response


# ================================
# Load Environment Variables
# ================================
load_dotenv()


# ================================
# Initialize App
# ================================
app = FastAPI(
    title="Mental Health Chatbot API",
    version="1.0"
)


# ================================
# CORS (Safe for Production)
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ================================
# Serve Frontend (UI)
# ================================
app.mount(
    "/static",
    StaticFiles(directory="chatbot-ui"),
    name="static"
)


@app.get("/")
def serve_ui():
    return FileResponse("chatbot-ui/index.html")


# ================================
# Health Check
# ================================
@app.get("/health")
def health_check():
    return {"status": "ok"}


# ================================
# Main Chat Endpoint
# ================================
@app.post("/chat")
def chat_with_ai(request: ChatRequest):

    session_id = request.session_id
    user_query = request.message


    # ----------------------------
    # Crisis Detection
    # ----------------------------
    is_crisis = check_for_crisis(user_query)

    if is_crisis:

        response = "\n".join(SAFETY_MESSAGES)

    else:

        # ----------------------------
        # Get LLM / Docs Response
        # ----------------------------
        response = get_response(user_query)


        # ----------------------------
        # Enforce 1–5 Numbered Points
        # ----------------------------
        MAX_POINTS = 5

        points = re.findall(r"\d+\.\s.*", response)

        if points:
            response = "\n".join(points[:MAX_POINTS])
        else:
            # Fallback format
            response = f"1. {response.strip()}"


    # ----------------------------
    # Logging
    # ----------------------------
    log_interaction(
        session_id,
        user_query,
        response,
        is_crisis
    )


    # ----------------------------
    # API Response
    # ----------------------------
    return {
        "reply": response,
        "crisis": is_crisis
    }


# ================================
# Document-Based Chat Endpoint
# ================================
@app.post("/doc-chat")
def chat_with_documents(request: ChatRequest):

    user_query = request.message

    response = get_response(user_query)


    # ----------------------------
    # Enforce 1–5 Numbered Points
    # ----------------------------
    MAX_POINTS = 5

    points = re.findall(r"\d+\.\s.*", response)

    if points:
        response = "\n".join(points[:MAX_POINTS])
    else:
        response = f"1. {response.strip()}"


    return {
        "reply": response,
        "crisis": False
    }
