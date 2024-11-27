import unittest
from unittest.mock import Mock, patch
from agents.fashion_agent import FashionAgent
from tools.database_tool import DatabaseManager
from tools.weather_tool import WeatherTool
from tools.image_search_tool import ImageSearchTool


class TestWeatherTool(unittest.TestCase):
    def setUp(self):
        self.weather_tool = WeatherTool()

    @patch('requests.get')
    def test_get_current_weather_success(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "current": {
                "temp_c": 20,
                "condition": {"text": "Sunny"},
                "humidity": 65
            }
        }
        mock_get.return_value = mock_response

        result = self.weather_tool.get_current_weather("London")
        self.assertIn("current", result)

    @patch('requests.get')
    def test_get_current_weather_failure(self, mock_get):
        mock_get.side_effect = Exception("API Error")
        result = self.weather_tool.get_current_weather("London")
        self.assertIn("Error", result)


class TestImageSearchTool(unittest.TestCase):
    def setUp(self):
        self.image_tool = ImageSearchTool()

    def test_get_retailer_urls(self):
        casual_query = "casual shirts"
        formal_query = "formal suits"

        casual_urls = self.image_tool._get_retailer_urls(casual_query)
        formal_urls = self.image_tool._get_retailer_urls(formal_query)

        self.assertEqual(casual_urls, self.image_tool.fashion_retailers['casual'])
        self.assertEqual(formal_urls, self.image_tool.fashion_retailers['formal'])

    @patch('duckduckgo_search.DDGS')
    def test_search_fashion_images(self, mock_ddgs):
        mock_ddgs.return_value.__enter__.return_value.images.return_value = [
            {'image': 'test.jpg', 'title': 'Test Image'}
        ]

        results = self.image_tool.search_fashion_images("casual shirts", max_results=1)
        self.assertEqual(len(results), 1)
        self.assertIn('image_url', results[0])
        self.assertIn('shopping_url', results[0])


class TestDatabaseManager(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseManager(reset_if_exists=True)

    def test_store_and_retrieve_conversation(self):
        user_id = "test_user"
        message = "What should I wear today?"
        response = "I recommend a casual outfit."

        self.db.store_conversation(user_id, message, response)
        history = self.db.get_conversation_history(user_id)

        self.assertGreater(len(history), 0)
        self.assertIn(message, history[0])
        self.assertIn(response, history[0])

    def test_clear_data(self):
        user_id = "test_user"
        self.db.store_conversation(user_id, "test", "test")
        self.db.clear_all_data()
        history = self.db.get_conversation_history(user_id)
        self.assertEqual(len(history), 0)


class TestFashionAgent(unittest.TestCase):
    def setUp(self):
        self.agent = FashionAgent()

    @patch('tools.weather_tool.WeatherTool.get_current_weather')
    @patch('tools.image_search_tool.ImageSearchTool.search_fashion_images')
    def test_get_response(self, mock_search, mock_weather):
        mock_weather.return_value = '{"current": {"temp_c": 20, "condition": {"text": "Sunny"}, "humidity": 65}}'
        mock_search.return_value = [{'image_url': 'test.jpg', 'shopping_url': 'test.com'}]

        user_preferences = {
            'gender': 'Male',
            'favorite_colors': ['Blue'],
            'preferred_styles': ['Casual'],
            'restrictions': []
        }

        response, images = self.agent.get_response(
            user_query="casual outfit for sunny day",
            location="London",
            user_preferences=user_preferences
        )

        self.assertIsInstance(response, str)
        self.assertIsInstance(images, list)
        self.assertGreater(len(images), 0)


if __name__ == '__main__':
    unittest.main()