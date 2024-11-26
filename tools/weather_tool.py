import json
import requests

from config import Config


class WeatherTool:
    api_key = Config.WEATHER_API_KEY

    @staticmethod
    def get_current_weather(location: str, date="today"):
        """
        :param location: city name
        :param date: today, tomorrow, or any specific date
        :return: Returns the weather at the specified location at the specified date
        """
        try:
            print(WeatherTool.api_key)
            url = f'https://api.weatherapi.com/v1/current.json?key={WeatherTool.api_key}&q={location}&dt={date}'
            response = requests.get(url)

            if response.status_code == 200:
                weather_info = response.json()

            else:
                weather_info = {"Error": "failed to get weather data"}

            return json.dumps(weather_info)

        except Exception as e:
            return json.dumps({"Error": str(e)})


# Test function

def test_weather():
    tool = WeatherTool()
    print(tool.get_current_weather("london", "today"))

if __name__ == '__main__':
    test_weather()
