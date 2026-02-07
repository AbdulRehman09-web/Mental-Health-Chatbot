import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder
)

# ================================
# Load Environment Variables
# ================================
load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env file")


# ================================
# Configure OpenRouter LLM
# ================================
llm = ChatOpenAI(
    model="openai/gpt-5-nano",
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base="https://openrouter.ai/api/v1",
    temperature=0.4,  # Lower = more disciplined
)


# ================================
# Session Memory Storage
# ================================
session_memory_map = {}


# ================================
# Response Formatter (ENFORCER)
# ================================
def format_response(text: str) -> str:
    """
    Forces:
    - Max 5 points
    - Bullet style
    - No long paragraphs
    """

    lines = text.split("\n")

    cleaned = []

    for line in lines:
        line = line.strip()

        if not line:
            continue

        # Convert to bullet if needed
        if not line.startswith("-"):
            line = "- " + line

        cleaned.append(line)

    # Limit to 5 points
    cleaned = cleaned[:5]

    return "\n".join(cleaned)


# ================================
# Get Conversation Chain
# ================================
def get_conversation_chain(session_id: str, user_query: str) -> str:

    if session_id not in session_memory_map:

        # Memory
        memory = ConversationBufferMemory(
            memory_key="history",
            return_messages=True
        )

        # Strong System Prompt
        system_prompt = SystemMessagePromptTemplate.from_template(
            """
You are a mental health support assistant.

STRICT RULES (Must Follow):
1. Respond ONLY in bullet points.
2. Maximum 5 bullet points.
3. Each point must be short.
4. No paragraphs.
5. Be supportive and gentle.

If you break any rule, your answer is invalid.
"""
        )

        human_prompt = HumanMessagePromptTemplate.from_template("{input}")

        chat_prompt = ChatPromptTemplate.from_messages([
            system_prompt,
            MessagesPlaceholder(variable_name="history"),
            human_prompt
        ])

        conversation = ConversationChain(
            llm=llm,
            memory=memory,
            prompt=chat_prompt,
            input_key="input",
            verbose=False
        )

        session_memory_map[session_id] = conversation

    conversation = session_memory_map[session_id]

    # Get raw output
    raw_response = conversation.predict(input=user_query)

    # Enforce formatting
    final_response = format_response(raw_response)

    return final_response
