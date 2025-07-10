from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    base = State()
    id = State()
    name = State()

class MovieStates(StatesGroup):
    query = State()
    page = State()
    limit = State()

