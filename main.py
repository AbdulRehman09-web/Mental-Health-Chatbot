import os
import re

from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

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
# CORS (Development Only)
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ================================
# Root Endpoint
# ================================
@app.get("/")
def read_root():
    return {
        "message": "✅ AI Mental Health Chatbot API is running."
    }


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

        # Emergency response
        response = "\n".join(SAFETY_MESSAGES)

    else:

        # ----------------------------
        # Always Use Formatted Engine
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
            # Fallback if model breaks format
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


    # Enforce 1–5 Numbered Points
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
