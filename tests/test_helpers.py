# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import imp


import pytest
import website

from website.utils import QueryBuilder, WeatherAPI


def test_search_image_query_builder(app):
    query_key_words = [" gender female", ' in Clear weather to a "Wedding"']
    siObject = QueryBuilder()
    query = siObject.getQueryString(queries=query_key_words, culture="Indian")
    print("QUERY")
    print(query)
    assert (
        query
        == 'Suggested Indian outfits for  gender female  in Clear weather to a "Wedding" '
    )


def test_weather_api(app):
    city = "Mumbai"
    wObj = WeatherAPI()
    weather = wObj.getCurrentWeather(city=city)
    assert True
