import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.langchain import LangChainLLM
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

# ------------------------- 
# OpenRouter Configuration
# -------------------------
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
OPENROUTER_API_BASE = os.getenv("OPENROUTER_URL", "https://openrouter.ai/api/v1")
OPENROUTER_EMBEDDING_MODEL = "text-embedding-3-large"
OPENROUTER_LLM_MODEL = "gpt-5-nano"

if not OPENROUTER_API_KEY:
    raise ValueError("❌ OPENROUTER_API_KEY not found in .env file")

# -------------------------
# Create embeddings
# -------------------------
embeddings = OpenAIEmbeddings(
    model=OPENROUTER_EMBEDDING_MODEL,
    openai_api_key=OPENROUTER_API_KEY,
    openai_api_base=OPENROUTER_API_BASE
)

# -------------------------
# Lazy load documents and index
# -------------------------
index = None
query_engine = None

def load_index():
    global index, query_engine
    if index is None:
        # Load documents
        documents = SimpleDirectoryReader("data").load_data()
        # Build vector index
        index = VectorStoreIndex.from_documents(documents, embed_model=embeddings)
        # Wrap OpenRouter LLM
        chat_llm = ChatOpenAI(
            model_name=OPENROUTER_LLM_MODEL,
            openai_api_key=OPENROUTER_API_KEY,
            openai_api_base=OPENROUTER_API_BASE,
            temperature=0.7
        )
        llm = LangChainLLM(chat_llm)
        # Create query engine
        query_engine = index.as_query_engine(llm=llm)

    return query_engine

# -------------------------
# Function to get response
# -------------------------
def get_response(user_query: str) -> str:
    """
    Accepts a user query string and returns a formatted response.
    """

    engine = load_index()

    system_prompt = """
You are a supportive mental health assistant.

STRICT RULES:
- Reply ONLY in numbered points (1 to 5)
- Maximum 5 points
- Each point must be short
- No paragraphs
- No long explanations
- No extra text
- Be calm and encouraging

FORMAT:
1. ...
2. ...
3. ...
4. ...
5. ...
"""

    final_prompt = system_prompt + "\nUser: " + user_query

    response = engine.query(final_prompt)

    return str(response)

