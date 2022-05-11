# pylint: disable=C0303, C0114, C0103, C0116, W0611

import os
import random
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())


def generate_movie_info(TMDB_KEY: str):
    top_movies = [
        "198375",
        "568160",
        "38142",
        "372058",
        "22843",
        "579741",
        "28874",
        "283566",
        "225745",
        "378064",
        "390635",
        "482150",
    ]
    movie_id = random.choice(top_movies)

    tmdb_movie_request = (
        "https://api.themoviedb.org/3/movie/" + movie_id + "?api_key=" + TMDB_KEY
    )

    movie_response = requests.get(tmdb_movie_request)

    m_response_json = movie_response.json()

    genres = ""
    title = m_response_json["title"]
    tagline = m_response_json["tagline"]
    poster_file = m_response_json["poster_path"]
    for genre in m_response_json["genres"]:
        genres = genres + genre["name"] + " "

    if tagline == "":
        return title, "tagline N/A for this movie", genres, poster_file
    return title, tagline, genres, poster_file


def generate_movie_poster(TMDB_KEY: str, file_name: str):
    poster_response = requests.get(
        "https://api.themoviedb.org/3/configuration?api_key=" + TMDB_KEY
    )

    p_response_json = poster_response.json()
    p_response_json = p_response_json["images"]

    base_url = p_response_json["secure_base_url"]
    poster_size = p_response_json["poster_sizes"][5]

    return base_url + poster_size + file_name
