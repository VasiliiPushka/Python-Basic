from datetime import datetime

from peewee import *
from dotenv import load_dotenv
import os

load_dotenv()

db = SqliteDatabase(os.getenv("DB_PATH"))

class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    telegram_id = IntegerField(unique=True)
    username = CharField(null=True)
    first_name = CharField()
    last_name = CharField()
    registration_date = DateTimeField(default=datetime.now())


class Movie(BaseModel):
    api_id = IntegerField(unique=True)
    title = CharField()
    description = TextField(null=True)
    rating = FloatField(null=True)
    year = IntegerField(null=True)
    age_rating = IntegerField(null=True)
    budget = IntegerField(null=True)
    poster_url = CharField(null=True)
    is_series = BooleanField(default=False)


class Genre(BaseModel):
    name = CharField(unique=True)


class MovieGenre(BaseModel):
    movie = ForeignKeyField(Movie, backref='genres')
    genre = ForeignKeyField(Genre, backref='movies')


class SearchHistory(BaseModel):
    user = ForeignKeyField(User, backref='searches')
    movie = ForeignKeyField(Movie, backref='searches')
    search_query = CharField()
    search_date = DateTimeField(default=datetime.now())
    created_at = DateTimeField(default=datetime.now())


db.create_tables(BaseModel.__subclasses__())