from typing import Dict, List, Optional, Tuple
from utils.prompt_templates import PromptTemplates
from utils.ollama_client import OllamaClient
from tools.weather_tool import WeatherTool
from tools.image_search_tool import ImageSearchTool


class FashionAgent:
    def __init__(self):
        self.ollama_client = OllamaClient()
        self.weather_tool = WeatherTool()
        self.image_search_tool = ImageSearchTool()
        self.templates = PromptTemplates()

        # Validate Ollama connection
        if not self.ollama_client.validate_connection():
            raise ConnectionError("Could not connect to Ollama server. Please ensure it's running.")

    def _get_weather_context(self, location: str = "London") -> str:
        """Get weather information and format it into context"""
        try:
            weather_data = self.weather_tool.get_current_weather(location)
            weather_dict = eval(weather_data)  # Convert string to dict

            if 'Error' in weather_dict:
                return "Weather information unavailable"

            current = weather_dict.get('current', {})
            return self.templates.WEATHER_CONTEXT.format(
                location=location,
                temperature=current.get('temp_c', 'N/A'),
                conditions=current.get('condition', {}).get('text', 'N/A'),
                humidity=current.get('humidity', 'N/A')
            )
        except Exception as e:
            print(f"Error getting weather context: {str(e)}")
            return "Weather information unavailable"

    def get_response(
            self,
            user_query: str,
            chat_history: Optional[List[Dict[str, str]]] = None,
            location: str = "London",
            occasion: str = "casual",
            user_preferences: Optional[Dict] = None
    ) -> Tuple[str, List[str]]:
        """
        Generate a fashion recommendation response based on user query and context
        Returns a tuple of (text_response, image_urls)
        """
        try:
            # Initialize chat history if None
            if chat_history is None:
                chat_history = []

            # Get weather context
            weather_context = self._get_weather_context(location)

            # Format user preferences if available
            preferences_context = ""
            if user_preferences:
                preferences_context = self.templates.USER_PREFERENCES_CONTEXT.format(
                    favorite_colors=user_preferences.get('favorite_colors', 'Not specified'),
                    preferred_styles=user_preferences.get('preferred_styles', 'Not specified'),
                    restrictions=user_preferences.get('restrictions', 'None')
                )

            # Create the full query with context
            full_query = self.templates.FASHION_QUERY.format(
                weather_info=weather_context,
                occasion=occasion,
                preferences=preferences_context,
                user_query=user_query
            )

            # Prepare messages for the chat
            messages = chat_history + [{"role": "user", "content": full_query}]

            # Get response from Ollama
            response = self.ollama_client.generate_chat_completion(
                messages=messages,
                system_prompt=self.templates.SYSTEM_PROMPT
            )

            # Get images for the recommendation
            try:
                images = self.image_search_tool.search_fashion_images(user_query)
            except Exception as e:
                print(f"Error getting images: {str(e)}")
                images = []

            return response, images

        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error while processing your request. Please try again.", []