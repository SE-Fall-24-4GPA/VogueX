import chromadb
from config import Config


class DatabaseManager:
    def __init__(self):
        self.conversations_client = chromadb.PersistentClient(
            path=Config.CHROMA_CONVERSATIONS_PATH
        )
        self.fashion_client = chromadb.PersistentClient(
            path=Config.CHROMA_FASHION_PATH
        )

        self.conversations_collection = self.conversations_client.get_or_create_collection(
            name="conversations"
        )
        self.fashion_collection = self.fashion_client.get_or_create_collection(
            name="fashion_data"
        )

    def store_conversation(self, user_id: str, message: str, response: str):
        self.conversations_collection.add(
            documents=[message + "\n" + response],
            metadatas=[{"user_id": user_id, "type": "conversation"}],
            ids=[f"{user_id}_{len(self.conversations_collection.get())}"]
        )

    def get_conversation_history(self, user_id: str, limit: int = 5):
        results = self.conversations_collection.get(
            where={"user_id": user_id},
            limit=limit
        )
        return results['documents']