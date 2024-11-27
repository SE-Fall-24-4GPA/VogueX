from typing import Dict, List, Optional, Tuple
from utils.prompt_templates import PromptTemplates
from utils.ollama_client import OllamaClient
from tools.weather_tool import WeatherTool
from tools.image_search_tool import ImageSearchTool
from tools.shop_tool import ShoppingLinkTool


class FashionAgent:
    def __init__(self):
        self.ollama_client = OllamaClient()
        self.weather_tool = WeatherTool()
        self.image_search_tool = ImageSearchTool()
        self.shopping_tool = ShoppingLinkTool()
        self.templates = PromptTemplates()

        if not self.ollama_client.validate_connection():
            raise ConnectionError("Could not connect to Ollama server")

    def _get_weather_context(self, location: str = "London") -> str:
        try:
            weather_data = self.weather_tool.get_current_weather(location)
            weather_dict = eval(weather_data)

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
        try:
            chat_history = chat_history or []
            gender = user_preferences.get('gender', 'Unisex')

            weather_context = self._get_weather_context(location)
            preferences_context = ""

            if user_preferences:
                preferences_context = self.templates.USER_PREFERENCES_CONTEXT.format(
                    gender=gender,
                    favorite_colors=user_preferences.get('favorite_colors', 'Not specified'),
                    preferred_styles=user_preferences.get('preferred_styles', 'Not specified'),
                    restrictions=user_preferences.get('restrictions', 'None')
                )

            full_query = self.templates.FASHION_QUERY.format(
                weather_info=weather_context,
                occasion=occasion,
                preferences=preferences_context,
                user_query=user_query
            )

            messages = chat_history + [{"role": "user", "content": full_query}]
            response = self.ollama_client.generate_chat_completion(
                messages=messages,
                system_prompt=self.templates.SYSTEM_PROMPT
            )

            # Get images and shopping links
            search_query = f"{gender} {user_query}" if gender else user_query
            images = self.image_search_tool.search_fashion_images(query=search_query, max_results=5)

            shopping_links = self.shopping_tool.generate_shopping_links(
                query=search_query,
                style=occasion,
                price_range='midrange'
            )

            # Add shopping links to image data
            for idx, image in enumerate(images):
                if idx < len(shopping_links):
                    image['shopping_url'] = shopping_links[idx]['url']

            return response, images

        except Exception as e:
            print(f"Error generating response: {str(e)}")
            return "I apologize, but I encountered an error while processing your request.", []