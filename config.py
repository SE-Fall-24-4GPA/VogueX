import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENWEATHER_API_KEY = os.environ.get('OPENWEATHER_API_KEY')
    CHROMA_CONVERSATIONS_PATH = "data/chroma_conversations"
    CHROMA_FASHION_PATH = "data/chroma_fashion"
    OLLAMA_BASE_URL = "http://localhost:11434"
    MODEL_NAME = "llama3.2"