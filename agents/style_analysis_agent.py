from typing import Dict, List, Optional
from utils.prompt_templates import PromptTemplates
from utils.ollama_client import OllamaClient
from tools.shop_tool import ShoppingLinkTool

from typing import Dict, List, Optional
from utils.prompt_templates import PromptTemplates
from utils.ollama_client import OllamaClient
from tools.shop_tool import ShoppingLinkTool


class StyleAnalysisAgent:
    def __init__(self):
        self.ollama_client = OllamaClient()
        self.shopping_tool = ShoppingLinkTool()
        self.templates = PromptTemplates()

    def analyze_style(self, user_query: str, user_preferences: Dict) -> Dict:
        """
        Analyzes the style/mood from user query and generates appropriate shopping parameters
        """
        system_prompt = """You are a fashion expert that analyzes queries to extract specific clothing details.
        For each query, identify:
        1. Specific clothing items that would be appropriate
        2. Style category (casual, formal, sporty, etc.)
        3. Occasion/setting
        4. Price range suggestion
        5. Season/weather appropriateness

        Format response as JSON with the following structure:
        {
            "style_category": "formal/casual/etc",
            "key_items": ["item1", "item2", "item3"],
            "occasion": "specific occasion",
            "price_range": "midrange/luxury/affordable",
            "mood": "romantic/professional/etc"
        }"""

        prompt = f"""Analyze this fashion query for a detailed shopping suggestion: "{user_query}"
        Consider user preferences: {user_preferences}
        Extract specific clothing items and style information."""

        try:
            analysis = self.ollama_client.generate_chat_completion(
                messages=[{"role": "user", "content": prompt}],
                system_prompt=system_prompt
            )

            # Convert string response to structured data
            import json
            style_data = json.loads(analysis)

            return {
                "style": style_data.get("style_category", "formal"),
                "price_range": style_data.get("price_range", "midrange"),
                "search_query": self._construct_search_query(style_data, user_preferences)
            }
        except Exception as e:
            print(f"Style analysis error: {str(e)}")
            return {
                "style": "formal",
                "price_range": "midrange",
                "search_query": self._construct_fallback_query(user_query, user_preferences)
            }

    def _construct_search_query(self, style_data: Dict, user_preferences: Dict) -> str:
        """Constructs optimized search query based on style analysis"""
        gender = user_preferences.get("gender", "")
        key_items = style_data.get("key_items", [])
        occasion = style_data.get("occasion", "")

        query_parts = []

        if gender and gender != "Unisex":
            query_parts.append(gender)

        if key_items:
            query_parts.extend(key_items[:2])

        if occasion:
            query_parts.append(occasion)

        if not key_items:
            if "date" in occasion.lower():
                if gender == "Male":
                    query_parts.extend(["dress shirt", "blazer"])
                elif gender == "Female":
                    query_parts.extend(["cocktail dress", "evening"])
                else:
                    query_parts.extend(["formal wear", "evening"])

        return " ".join(query_parts)

    def _construct_fallback_query(self, user_query: str, user_preferences: Dict) -> str:
        """Creates a smart fallback query when analysis fails"""
        gender = user_preferences.get("gender", "")

        if gender == "Male":
            return f"{gender} date night dress shirt blazer"
        elif gender == "Female":
            return f"{gender} date night cocktail dress"
        else:
            return "elegant date night outfit"

    def get_shopping_suggestions(self, user_query: str, user_preferences: Dict) -> List[Dict[str, str]]:
        """
        Analyzes style and returns shopping suggestions

        Args:
            user_query: The user's fashion question
            user_preferences: Dictionary of user preferences

        Returns:
            List of shopping link dictionaries
        """
        try:
            # Analyze style and get search parameters
            style_info = self.analyze_style(user_query, user_preferences)

            # Generate shopping links using the analyzed style
            return self.shopping_tool.generate_shopping_links(
                query=style_info["search_query"],
                style=style_info["style"],
                price_range=style_info["price_range"]
            )
        except Exception as e:
            print(f"Error generating shopping suggestions: {str(e)}")
            # Return an empty list rather than None to avoid further errors
            return []