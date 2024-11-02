# VogueX
# Copyright (c) 2024 Group 84: Gokul Prakash Ramesh, Haricharan Bharathi, Raghunandan Ganesh Mante
# This project is licensed under the MIT License.
# #
# Governance Model:
# This project follows an open governance model, which includes a leadership team,
# contribution guidelines, a code of conduct, and a clear decision-making process.
# Contributions are welcome, and please see CONTRIBUTING.md for details.

from google_images_search import GoogleImagesSearch


class Config:
    def __init__(self) -> None:
        self.API_KEY = "AIzaSyBnKm9SLLT0j_Hmw5CXV5h54GNOm_NhvLI"
        self.PROJ_CX = "951651316f70a470c"


class QueryBuilder:
    def __init__(self) -> None:
        pass

    def getQueryString(self, queries):
        return_query_string = ""
        for q in queries:
            return_query_string += q + " "

        return return_query_string


class SearchImages:
    def __init__(self) -> None:
        self.config = Config()
        self.gis = GoogleImagesSearch(self.config.API_KEY, self.config.PROJ_CX)
        self.default_num_of_records = 10
        self.query_builder = QueryBuilder()

    # gives the list of urls for a search
    def image_search(self, query_keywords, num_of_records=None):
        if not num_of_records:
            num_of_records = self.default_num_of_records

        query = self.query_builder.getQueryString(query_keywords)
        print("Searchingx ", query)
        _search_params = {"q": query, "num": num_of_records}
        self.gis.search(search_params=_search_params)

        image_urls = []
        for image in self.gis.results():
            image_urls.append(image.url)
        return image_urls
