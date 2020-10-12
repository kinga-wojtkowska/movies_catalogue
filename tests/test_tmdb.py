import tmdb_client
from main import app
from unittest.mock import Mock


def test_get_poster_url_uses_default_size():
    # Przygotowanie danych
    poster_api_path = "some-poster-path"
    expected_default_size = 'w342'
    # Wywołanie kodu, który testujemy
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
    # Porównanie wyników
    assert expected_default_size in poster_url


def test_get_movies_list_type_popular():
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list is not None


def test_get_movies_list(monkeypatch):
    # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
    mock_movies_list = ['Movie 1', 'Movie 2']
    requests_mock = Mock()
    # Wynik wywołania zapytania do API
    response = requests_mock.return_value
    # Przysłaniamy wynik wywołania metody .json()
    response.json.return_value = mock_movies_list
    monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
    movies_list = tmdb_client.get_movies_list(list_type="popular")
    assert movies_list == mock_movies_list


def test_get_single_movie(monkeypatch):
    mock_single_movie = ['Single_movie']
    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_single_movie
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)
    single_movie = tmdb_client.get_single_movie(movie_id=1)
    assert single_movie == mock_single_movie


def test_get_backdrop_image(monkeypatch):
    mock_backdrop_image = {'Id': 1, 'backdrops': [1, 2]}
    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_backdrop_image
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)
    backdrop_image = tmdb_client.get_backdrop_image(movie_id=1)
    return backdrop_image == mock_backdrop_image


def test_get_single_movie_cast(monkeypatch):
    mock_movie_cast = {'Id': 1, 'cast': [1, 2]}
    call_tmdb_api_mock = Mock()
    call_tmdb_api_mock.return_value = mock_movie_cast
    monkeypatch.setattr("tmdb_client.call_tmdb_api", call_tmdb_api_mock)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id=1)
    return movie_cast == mock_movie_cast
