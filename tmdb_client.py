import requests
import random

api_token = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4NzE1NThiYzNlMDM2YTYzN2E1Zjg5MmZiMTBlNWZiOSIsInN1YiI6IjVmNWY0ODE5ZmQ3YWE0MDAzOWU4ODg2ZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.9GISWyFnjpvaIGkGuoSVDsitJkTkkFhwcBaxWvaTNcc'


def get_movies_list(list_type="popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()


images = {'base_url': 'https://image.tmdb.org/t/p/',
                      'poster_sizes': ["w92",
                                       "w154",
                                       "w185",
                                       "w342",
                                       "w500",
                                       "w780",
                                       "original"
                                       ]}


def get_poster_url(poster_api_path, size="w342"):
    poster_url = images['base_url'] + size
    return f"{poster_url}{poster_api_path}"


def get_random_eight(list_type=''):
    popular_movies = get_movies_list(list_type)["results"]
    random.shuffle(popular_movies)
    popular_info = popular_movies[:8]
    return popular_info


def get_movie_info():
    popular_info = get_random_eight()
    movie_info = {}
    for i in range(8):
        k = popular_info[i]['title']
        v = popular_info[i]['poster_path']
        movie_info[k] = v
    return movie_info


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_cast(movie_id, how_many):
    data = get_single_movie_cast(movie_id)
    return data[:how_many]


def get_backdrop_image(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["backdrops"]


def get_random_backdrop_image(movie_id):
    backdrop = get_backdrop_image(movie_id)
    random_backdrop = random.choice(backdrop)
    return random_backdrop['file_path']
