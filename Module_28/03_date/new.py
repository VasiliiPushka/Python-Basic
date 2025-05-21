import datetime
from abc import ABC, abstractmethod

class Date:

    def __init__(self, day: int = 0, month: int = 0, year: int = 0):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"День: {self.day}\tМесяц: {self.month}\tГод: {self.year}"

    @classmethod
    def from_string(cls, date:str) -> "Date":
        # day, month, year = map(int, date.split('-'))
        dmy_list = date.split('-')
        day, month, year = int(dmy_list[0]), int(dmy_list[1]), int(dmy_list[2])
        date = Date(day, month, year)
        return date

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        day, month, year = map(int, date.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

