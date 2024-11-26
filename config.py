import os
from dotenv import load_dotenv

load_dotenv()

# Set ChromaDB environment variable
os.environ['ALLOW_RESET'] = 'TRUE'

class Config:
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
    CHROMA_CONVERSATIONS_PATH = 'data/chroma_conversations'
    CHROMA_FASHION_PATH = 'data/chroma_fashion'
    OLLAMA_BASE_URL = 'http://localhost:11434'
    MODEL_NAME = 'llama3.2'
