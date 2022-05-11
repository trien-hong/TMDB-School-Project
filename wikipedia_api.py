# pylint: disable=C0303, C0114, C0116

import requests


def get_wiki_page(movie_title: str):
    base_url = "https://en.wikipedia.org/w/api.php"
    parameters = {
        "action": "opensearch",
        "namespace": "0",
        "search": movie_title,
        "limit": "1",
        "format": "json",
    }

    wikipedia_response = requests.get(url=base_url, params=parameters)

    wikipedia_response_json = wikipedia_response.json()

    return wikipedia_response_json[len(wikipedia_response_json) - 1]
