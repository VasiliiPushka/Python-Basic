import requests
from typing import List, Dict, Optional

from config import API_BASE_URL, API_KEY


def api_requests(endpoint: str, params: {}) -> requests.Response:
    headers = {"X-API-KEY": API_KEY}
    return requests.get(f"{API_BASE_URL}/{endpoint}", headers=headers, params=params)


def movie_search_id(movie_id: str) -> Optional[Dict]:
    """Функция для поиска фильмов и сериалов по id"""
    try:
        response = api_requests("movie", params={"id": movie_id})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к api: {e}")
        return None
