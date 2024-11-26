import os
import shutil
import chromadb
from chromadb.config import Settings
from config import Config


class DatabaseManager:
    def __init__(self, reset_if_exists=False):
        try:
            # Define paths
            self.conversations_path = Config.CHROMA_CONVERSATIONS_PATH
            self.fashion_path = Config.CHROMA_FASHION_PATH

            # Reset databases if requested or if there are permission issues
            if reset_if_exists:
                self._reset_databases()

            # Ensure directories exist
            os.makedirs(self.conversations_path, exist_ok=True)
            os.makedirs(self.fashion_path, exist_ok=True)

            # Initialize settings with allow_reset=True
            settings = Settings(
                anonymized_telemetry=False,
                is_persistent=True,
                allow_reset=True  # Enable reset functionality
            )

            # Initialize clients
            try:
                self.conversations_client = chromadb.PersistentClient(
                    path=self.conversations_path,
                    settings=settings
                )
                self.fashion_client = chromadb.PersistentClient(
                    path=self.fashion_path,
                    settings=settings
                )
            except ValueError as ve:
                # If we get a settings mismatch, reset and try again
                print(f"Settings mismatch detected: {ve}")
                self._reset_databases()
                # Try initialization again after reset
                self.conversations_client = chromadb.PersistentClient(
                    path=self.conversations_path,
                    settings=settings
                )
                self.fashion_client = chromadb.PersistentClient(
                    path=self.fashion_path,
                    settings=settings
                )

            # Initialize collections
            self.conversations_collection = self.conversations_client.get_or_create_collection(
                name='conversations'
            )
            self.fashion_collection = self.fashion_client.get_or_create_collection(
                name='fashion'
            )

        except Exception as e:
            raise RuntimeError(f"Failed to initialize DatabaseManager: {str(e)}")

    def _reset_databases(self):
        """Reset the database by removing the directories"""
        try:
            if os.path.exists(self.conversations_path):
                shutil.rmtree(self.conversations_path)
            if os.path.exists(self.fashion_path):
                shutil.rmtree(self.fashion_path)
        except Exception as e:
            print(f"Error resetting databases: {str(e)}")
            raise

    def store_conversation(self, user_id: str, message: str, response: str):
        try:
            # Get current count for ID generation
            existing = self.conversations_collection.get(
                where={"user_id": user_id}
            )
            conversation_count = len(existing['documents']) if existing else 0

            # Add new conversation
            self.conversations_collection.add(
                documents=[f"{message}\n{response}"],
                metadatas=[{"user_id": user_id, "type": "conversation"}],
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
        """Clear all data from the collections"""
        try:
            # Reset both clients
            self.conversations_client.reset()
            self.fashion_client.reset()

            # Reinitialize collections after reset
            self.conversations_collection = self.conversations_client.get_or_create_collection(
                name='conversations'
            )
            self.fashion_collection = self.fashion_client.get_or_create_collection(
                name='fashion'
            )
        except Exception as e:
            print(f"Error clearing data: {str(e)}")
            raise


# Test database tool
def test_database():
    try:
        # Initialize with reset flag
        db = DatabaseManager(reset_if_exists=True)
        db.store_conversation('test', 'test message', 'test response')
        print(db.get_conversation_history('test'))
    except Exception as e:
        print(f"Test failed: {str(e)}")


if __name__ == '__main__':
    test_database()