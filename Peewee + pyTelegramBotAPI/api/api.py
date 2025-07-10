from typing import Any

import requests
from typing import List, Dict, Optional

from ..config.config import API_BASE_URL, API_KEY


def filter_list(list_list):
    return "; ".join(list_list)


def api_requests(endpoint: str, params: {}) -> requests.Response:
    headers = {"X-API-KEY": API_KEY}
    return requests.get(f"{API_BASE_URL}/{endpoint}", headers=headers, params=params)


def movie_search_id(movie_id: str) -> Optional[Dict]:

    """ Функция для поиска фильмов и сериалов по id:
    :param
    :movie_id int - номер фильма
    """

    try:
        response = api_requests("movie", params={"id": movie_id})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к api: {e}")
        return None


def movie_search(page:int, limit: int, query: str) -> Optional[Dict]:

    """  Функция для поиска фильма по названию:
    :param
        page: int - Страница выборки
        limit: int - количество элементов на странице (какое кол-во фильмов с данным названием должно быть показано)
        query: str - поисковый запрос (наименование фильма/сериала)
    """

    if not query.strip():
        print("Ошибка. Название фильма не может быть пустым")
        return None

    if page < 1 or limit < 1:
        print("Ошибка. Значение limit и page должны быть положительными числами")
        return None

    try:
        response = api_requests(
            "movie/search",
            params={"page": page, "limit": limit, "query": query}
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None


def print_info(query: Any, page: Any, limit: Any) -> str:
    return (f"Название: {query}\n"
            f"Страница выборки: {page}\n"
            f"Количество элементов на странице: {limit}")




