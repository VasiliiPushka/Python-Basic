from telebot.types import Message
from ..db.crud import create_or_get_user


def register_start_handlers(bot):

    @bot.message_handler(commands=["start"])
    def start(message:Message) -> None:

        user_id = message.from_user.id or ''
        username = message.from_user.username or ''
        first_name = message.from_user.first_name or ''
        last_name = message.from_user.last_name or ''

        user, created = create_or_get_user(user_id, username, first_name, last_name)

        if created:
            bot.send_message(message.from_user.id, f"Добро пожаловать в бот по поиску фильмов, {username}!")
        else:
            bot.send_message(message.from_user.id, f"Рад снова тебя видеть, {username}!")

