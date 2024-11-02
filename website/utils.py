# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from google_images_search import GoogleImagesSearch
import requests


class WeatherConfig:
    def __init__(self):
        self.API_KEY = "424ca7dcc9a5422e811220113222311"


# class WeatherAPI:
#     def __init__(self) -> None:
#         self.config = WeatherConfig()

#     def getCurrentWeather(self, latitude=None, longitude=None, city=None):
#         url = "http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no".format(
#             city=city, API_KEY=self.config.API_KEY
#         )
#         response = requests.request("GET", url, headers={}, data={})
#         if response.status_code != 200:
#             raise Exception(
#                 "Weather API failed : response code : {code}".format(
#                     code=response.status_code
#                 )
#             )
#         jsonResponse = response.json()
#         if (
#             "current" in jsonResponse
#             and "condition" in jsonResponse["current"]
#             and "text" in jsonResponse["current"]["condition"]
#         ):
#             return jsonResponse["current"]["condition"]["text"]
#         return ""


class WeatherAPI:
    def __init__(self) -> None:
        self.config = WeatherConfig()

    """
    Function to fetch current weather forecast using city from external weather API
    """

    def getCurrentWeather(self, latitude=None, longitude=None, city=None):
        url = "http://api.weatherapi.com/v1/current.json?key={API_KEY1}&q={city}&aqi=no".format(
            city=city, API_KEY1=self.config.API_KEY
        )
        response = requests.request("GET", url, headers={}, data={})
        if response.status_code != 200:
            raise Exception(
                "Weather API failed : response code : {code}".format(
                    code=response.status_code
                )
            )
        jsonResponse = response.json()
        if "condition" in jsonResponse:
            return jsonResponse["condition"]["text"]
        return ""

    """
    Function to fetch weather forecast for future from external weather API
    """

    def getFutureWeather(self, date=None, city=None, time=None):
        url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{Date}?key={API_KEY2}".format(
            city=city, Date=date, API_KEY2=self.config.API_KEY
        )
        response = requests.request("GET", url, headers={}, data={})
        if response.status_code != 200:
            raise Exception(
                "Weather API failed : response code : {code}".format(
                    code=response.status_code
                )
            )
        jsonResponse = response.json()
        hours = jsonResponse["days"]["hours"]
        x = (time.split[":"])[0]
        index = 0

        # hours=24
        for t in hours:
            if x == ((hours[0].split[":"])[0]):
                index = t
        return hours[index]["conditions"]


class ImageConfig:
    def __init__(self) -> None:
        self.API_KEY = "AIzaSyBnKm9SLLT0j_Hmw5CXV5h54GNOm_NhvLI"
        self.PROJ_CX = "951651316f70a470c"


class QueryBuilder:
    def __init__(self) -> None:
        pass

    def getQueryString(self, queries, culture=""):
        return_query_string = ""
        for q in queries:
            return_query_string += q + " "

        return "Suggested " + culture + " outfits for " + return_query_string


class SearchImages:
    def __init__(self) -> None:
        self.config = ImageConfig()
        self.gis = GoogleImagesSearch(self.config.API_KEY, self.config.PROJ_CX)
        self.default_num_of_records = 10
        self.query_builder = QueryBuilder()

    # gives the list of urls for a search
    def image_search(self, query_keywords, culture, num_of_records=None):
        if not num_of_records:
            num_of_records = self.default_num_of_records

        query = self.query_builder.getQueryString(query_keywords, culture=culture)
        print("Searchingy ", query)
        _search_params = {"q": query, "num": num_of_records}
        self.gis.search(search_params=_search_params)

        image_urls = []
        for image in self.gis.results():
            image_urls.append(image.url)
        return image_urls
