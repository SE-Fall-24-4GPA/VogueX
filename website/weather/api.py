# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

import requests


class Config:
    def __init__(self):
        self.API_KEY1 = "E2GXA3EGPJ7RHYM4MTCH4H7RQ"
        self.API_KEY2 = "424ca7dcc9a5422e811220113222311"


class WeatherAPI:
    def __init__(self) -> None:
        self.config = Config()

    def getCurrentWeather(self, latitude=None, longitude=None, city=None):
        url = "http://api.weatherapi.com/v1/current.json?key={API_KEY1}&q={city}&aqi=no".format(
            city=city, API_KEY1=self.config.API_KEY1
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

    def getFutureWeather(self, date=None, city=None, time=None):
        url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{City}/{Date}?key={API_KEY2}".format(
            city=city, Date=date, API_KEY2=self.config.API_KEY2
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
