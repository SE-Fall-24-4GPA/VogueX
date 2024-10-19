import imp


import pytest
import website

from website.utils import QueryBuilder, WeatherAPI


def test_search_image_query_builder(app):
    query_key_words = [' gender female', ' in Clear weather to a "Wedding"']
    siObject = QueryBuilder()
    query = siObject.getQueryString(queries=query_key_words, culture="Indian")
    print("QUERY")
    print(query)
    assert query == 'Suggested Indian outfits for  gender female  in Clear weather to a "Wedding" '


def test_weather_api(app):
    city = "Mumbai"
    wObj = WeatherAPI()
    weather = wObj.getCurrentWeather(city=city)
    assert True
