from models import Movie, User, db, BaseModel
from peewee import DoesNotExist


def create_db():
    """Создание БД"""
    tables = BaseModel.__subclasses__()
    db.create_tables(tables)


def create_or_get_user(user_id: str, username: str, first_name: str, last_name: str) -> tuple[User, bool]:
    """
    Получает или создает пользователя в БД.
    Возвращает кортеж (пользователь, created), где created - флаг создания нового пользователя.
    :param user_id:
    :param username:
    :param first_name:
    :param last_name:
    :return:
    """

    try:
        user = User.get(
            User.user_id == user_id,
            User.username == username,
            User.first_name == first_name,
            User.last_name == last_name
        )
        return user, False

    except DoesNotExist:
        user = User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name
        )
        return user, True


def create_or_get_movie(api_id: str, title: str, description: str, rating_kp: float, rating_imdb: float,
                    year: str, age_rating: str, budget: str, poster_url: str, is_series: bool) -> tuple[Movie, bool]:

    """
    Получает или создает фильм/сериал запрошенный пользователем и добавляет его в БД,
    возвращает кортеж (фильм/сериал, created), где created - флаг создания нового фильма/сериала.
    :param api_id:
    :param title:
    :param description:
    :param rating_kp:
    :param rating_imdb:
    :param year:
    :param age_rating:
    :param budget:
    :param poster_url:
    :param is_series:
    :return:
    """

    try:
        movie = Movie.get(
            Movie.api_id == api_id,
            Movie.title == title
        )
        return movie, False

    except DoesNotExist:
        movie = Movie.create(
            api_id=api_id,
            title=title,
            description=description,
            rating_kp=rating_kp,
            rating_imdb=rating_imdb,
            year=year,
            age_rating=age_rating,
            budget=budget,
            poster_url=poster_url,
            is_series=is_series
        )
        return movie, True


def get_all_users():
    all_user = User.select()
    return all_user



