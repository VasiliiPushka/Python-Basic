from peewee import *
from datetime import datetime

db = SqliteDatabase("movies.db")


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    user_id = BigIntegerField(unique=True)
    username = CharField(unique=True)
    first_name = CharField(null=True)
    last_name = CharField(null=True)
    created_at = DateTimeField(default=datetime.now)


class SearchHistory(BaseModel):
    user = ForeignKeyField(User, backref="searches")
    search_type = CharField()
    query = TextField()
    created_at = DateTimeField(default=datetime.now)


class MovieHistory(BaseModel):
    search = ForeignKeyField(SearchHistory, backref="movies")
    movie_id = IntegerField()
    title = CharField()
    description = TextField(null=True)
    rating = FloatField(null=True)
    year = IntegerField(null=True)
    genres = CharField(null=True)
    age_rating = CharField(null=True)
    poster_url = CharField(null=True)
    is_watched = BooleanField(default=False)
    created_at = DateTimeField(default=datetime.now)


def create_tables():
    with db:
        db.create_tables([User, SearchHistory, MovieHistory])
