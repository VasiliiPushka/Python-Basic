from .models import *


def get_or_create_user(user_id, username=None, first_name=None, last_name=None):
    user, created = User.get_or_create(
        user_id=user_id,
        defaults={
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
        },
    )
    return user


def add_search_history(user_id, search_type, query):
    user = get_or_create_user(user_id)
    search = SearchHistory.create(user=user, search_type=search_type, query=str(query))
    return search


def add_movie_to_history(search_id, movie_data):
    return MovieHistory.create(
        search_id=search_id,
        movie_id=movie_data.get("id"),
        title=movie_data.get("title"),
        description=movie_data.get("description"),
        rating=movie_data.get("rating"),
        year=movie_data.get("year"),
        genres=movie_data.get("genres"),
        age_rating=movie_data.get("age_rating"),
        poster_url=movie_data.get("poster_url"),
    )


def get_user_history(user_id, date_from=None, date_to=None):
    query = (
        MovieHistory.select()
        .join(SearchHistory)
        .join(User)
        .where(User.user_id == user_id)
    )

    if date_from:
        query = query.where(MovieHistory.created_at >= date_from)
    if date_to:
        query = query.where(MovieHistory.created_at <= date_to)

    return query.order_by(MovieHistory.created_at.desc())


def mark_movie_watched(movie_history_id, is_watched=True):
    (
        MovieHistory.update(is_watched=is_watched)
        .where(MovieHistory.movie_id == movie_history_id)
        .execute()
    )
