from typing import Optional
from pydantic import BaseModel
import requests
from config import Config


class WeatherTool(BaseModel):
    api_key: str = Config.OPENWEATHER_API_KEY
    base_url: str = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city: str) -> Optional[dict]:
        """
        Get current weather for a city using OpenWeather API.
        Returns temperature in Celsius, weather description, humidity, and wind speed.
        """
        try:
            params = {
                'q': city,
                'appid': self.api_key,
                'units': 'metric'  # Use metric units (Celsius)
            }

            response = requests.get(self.base_url, params=params)
            response.raise_for_status()

            data = response.json()

            return {
                "temperature": data['main']['temp'],
                "feels_like": data['main']['feels_like'],
                "description": data['weather'][0]['description'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "main_weather": data['weather'][0]['main']
            }

        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather: {e}")
            return None