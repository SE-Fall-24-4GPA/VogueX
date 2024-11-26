from typing import List, Dict, Optional
import ollama
from config import Config


class OllamaClient:
    def __init__(self, model_name: str = Config.MODEL_NAME):
        self.model_name = model_name

    def generate_chat_completion(
            self,
            messages: List[Dict[str, str]],
            system_prompt: Optional[str] = None,
            temperature: float = 0.7,
            max_tokens: int = 500
    ) -> str:
        """
        Generate a chat completion using Ollama Python library.

        Args:
            messages: List of message dictionaries with 'role' and 'content'
            system_prompt: Optional system prompt to set context
            temperature: Controls randomness (0.0 to 1.0)
            max_tokens: Maximum number of tokens to generate

        Returns:
            Generated response text
        """
        try:
            # Prepare the chat messages
            formatted_messages = []

            # Add system prompt if provided
            if system_prompt:
                formatted_messages.append({
                    "role": "system",
                    "content": system_prompt
                })

            # Add the conversation messages
            formatted_messages.extend(messages)

            # Generate response using ollama
            response = ollama.chat(
                model=self.model_name,
                messages=formatted_messages,
                options={
                    "temperature": temperature,
                    "num_predict": max_tokens
                }
            )

            return response['message']['content']
        except Exception as e:
            return ""

    def validate_connection(self) -> bool:
        """
        Validate connection to Ollama server
        """
        try:
            # List available models to check connection
            ollama.list()
            return True
        except Exception as e:
            print(f"Failed to connect to Ollama: {str(e)}")
            return False