from typing import Dict, List, Optional, Tuple
import asyncio
from utils.prompt_templates import PromptTemplates
from utils.ollama_client import OllamaClient
from tools.weather_tool import WeatherTool
from tools.image_search_tool import ImageSearchTool
from .style_analysis_agent import StyleAnalysisAgent


class FashionAgent:
    def __init__(self):
        self.ollama_client = OllamaClient()
        self.weather_tool = WeatherTool()
        self.image_search_tool = ImageSearchTool()
        self.style_agent = StyleAnalysisAgent()
        self.templates = PromptTemplates()

    async def get_response_with_suggestions(
            self,
            user_query: str,
            chat_history: Optional[List[Dict[str, str]]] = None,
            location: str = "London",
            user_preferences: Optional[Dict] = None
    ) -> Tuple[str, List[Dict[str, str]], List[Dict[str, str]]]:
        """
        Generates response and shopping suggestions in parallel
        """
        # Create tasks for parallel execution
        tasks = [
            self._generate_response(user_query, chat_history, location, user_preferences),
            self._get_shopping_suggestions(user_query, user_preferences)
        ]

        # Run tasks concurrently
        response, shopping_links = await asyncio.gather(*tasks)

        # Get images based on style analysis
        images = self.image_search_tool.search_fashion_images(
            query=user_query,
            max_results=5
        )

        return response, images, shopping_links

    async def _generate_response(
            self,
            user_query: str,
            chat_history: Optional[List[Dict[str, str]]],
            location: str,
            user_preferences: Optional[Dict]
    ) -> str:
        """Generates conversational response"""
        weather_context = self._get_weather_context(location)
        preferences_context = self._format_preferences(user_preferences)

        full_query = self.templates.FASHION_QUERY.format(
            weather_info=weather_context,
            occasion="any",  # Now handled by style agent
            preferences=preferences_context,
            user_query=user_query
        )

        messages = (chat_history or []) + [{"role": "user", "content": full_query}]
        return self.ollama_client.generate_chat_completion(
            messages=messages,
            system_prompt=self.templates.SYSTEM_PROMPT
        )

    async def _get_shopping_suggestions(
            self,
            user_query: str,
            user_preferences: Optional[Dict]
    ) -> List[Dict[str, str]]:
        """Gets shopping suggestions using style analysis"""
        return self.style_agent.get_shopping_suggestions(
            user_query=user_query,
            user_preferences=user_preferences
        )

    def _get_weather_context(self, location: str) -> str:
        """
        Gets formatted weather context for the given location

        Args:
            location: City name or location

        Returns:
            Formatted weather context string
        """
        try:
            weather_data = self.weather_tool.get_current_weather(location)
            weather_dict = eval(weather_data)

            if 'Error' in weather_dict:
                return "Weather information currently unavailable. Providing general recommendations."

            current = weather_dict.get('current', {})
            return self.templates.WEATHER_CONTEXT.format(
                location=location,
                temperature=current.get('temp_c', 'N/A'),
                conditions=current.get('condition', {}).get('text', 'N/A'),
                humidity=current.get('humidity', 'N/A')
            )
        except Exception as e:
            print(f"Error getting weather context: {str(e)}")
            return "Weather information currently unavailable. Providing general recommendations."

    def _format_preferences(self, preferences: Optional[Dict]) -> str:
        """
        Formats user preferences into a structured context string

        Args:
            preferences: Dictionary containing user preferences

        Returns:
            Formatted preferences context string
        """
        if not preferences:
            return "No specific style preferences provided."

        try:
            return self.templates.USER_PREFERENCES_CONTEXT.format(
                gender=preferences.get('gender', 'Unisex'),
                favorite_colors=', '.join(preferences.get('favorite_colors', [])) or 'Not specified',
                preferred_styles=', '.join(preferences.get('preferred_styles', [])) or 'Not specified',
                restrictions=', '.join(preferences.get('restrictions', [])) or 'None'
            )
        except Exception as e:
            print(f"Error formatting preferences: {str(e)}")
            return "Error processing style preferences. Using default recommendations."
