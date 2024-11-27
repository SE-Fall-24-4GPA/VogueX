import os
import shutil
import chromadb
from chromadb.config import Settings


class DatabaseManager:
    def __init__(self, reset_if_exists=False):
        self.conversations_path = 'data/chroma_conversations'
        self.fashion_path = 'data/chroma_fashion'

        if reset_if_exists:
            self._reset_databases()

        os.makedirs(self.conversations_path, exist_ok=True)
        os.makedirs(self.fashion_path, exist_ok=True)

        settings = Settings(
            anonymized_telemetry=False,
            is_persistent=True,
            allow_reset=True
        )

        try:
            # Force reset existing client instances
            try:
                chromadb.reset_persistent()
            except:
                pass

            self.conversations_client = chromadb.PersistentClient(
                path=self.conversations_path,
                settings=settings
            )

            self.fashion_client = chromadb.PersistentClient(
                path=self.fashion_path,
                settings=settings
            )

            # Initialize collections
            self.conversations_collection = self.conversations_client.get_or_create_collection('conversations')
            self.fashion_collection = self.fashion_client.get_or_create_collection('fashion')

        except Exception as e:
            self._reset_databases()
            raise RuntimeError(f"Failed to initialize DatabaseManager: {str(e)}")

    def _reset_databases(self):
        """Reset databases by removing directories"""
        paths = [self.conversations_path, self.fashion_path]
        for path in paths:
            if os.path.exists(path):
                try:
                    shutil.rmtree(path)
                except Exception as e:
                    print(f"Error removing {path}: {str(e)}")

    def store_conversation(self, user_id: str, message: str, response: str, gender: str = None):
        try:
            existing = self.conversations_collection.get(where={"user_id": user_id})
            conversation_count = len(existing['documents']) if existing else 0

            metadata = {
                "user_id": user_id,
                "type": "conversation",
                "gender": gender if gender else "Unisex"
            }

            self.conversations_collection.add(
                documents=[f"{message}\n{response}"],
                metadatas=[metadata],
                ids=[f"{user_id}_{conversation_count}"]
            )
        except Exception as e:
            print(f"Error storing conversation: {str(e)}")
            raise

    def get_conversation_history(self, user_id: str, limit: int = 5):
        try:
            results = self.conversations_collection.get(
                where={"user_id": user_id},
                limit=limit
            )
            return results['documents']
        except Exception as e:
            print(f"Error retrieving conversation history: {str(e)}")
            return []

    def clear_all_data(self):
        """Clear all data from collections"""
        try:
            self.conversations_client.reset()
            self.fashion_client.reset()

            self.conversations_collection = self.conversations_client.get_or_create_collection('conversations')
            self.fashion_collection = self.fashion_client.get_or_create_collection('fashion')
        except Exception as e:
            print(f"Error clearing data: {str(e)}")
            raise