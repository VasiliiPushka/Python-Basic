import telebot
import json

from peewee import IntegrityError
from telebot.types import Message
from telebot import custom_filters
from telebot.storage import StateMemoryStorage
from telebot.util import split_string

import api
from config import BOT_TOKEN, API_KEY, API_BASE_URL
from states import States
from models import User

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)


@bot.message_handler(commands=["start"])
def start(message: Message) -> None:

    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    try:
        User.create(
            user_id = user_id,
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        bot.send_message(
            message.chat.id, f"Привет {first_name}! "
                             f"Я телеграмм бот основанный на API Кинопоиска")
        bot.set_state(message.from_user.id, States.id, message.chat.id)

    except IntegrityError:
        bot.reply_to(message, f"Рад снова Вас видеть {first_name}")


@bot.message_handler(commands=["movie_search_id"])
def movie_search_id_command(message: Message) -> None:
    bot.send_message(message.chat.id, f"Укажите id в диапазоне от 250 до 10000000!")
    bot.set_state(message.from_user.id, States.id, message.chat.id)


@bot.message_handler(commands=["movie_search"])
def movie_search_command(message: Message) -> None:
    bot.send_message(message.chat.id, f"Введите название фильма ")
    bot.set_state(message.from_user.id, States.name, message.chat.id)


@bot.message_handler(state=States.id)
def movie_search(message: Message) -> None:

    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, введите числовой ID")
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = api.movie_search_id(movie_id=message.text)

        if result is None:
            bot.send_message(message.chat.id, "Произошла ошибка при запросе к API")

        if not result:
            bot.send_message(message.chat.id, "Фильм с таким ID не найден")

        try:
            json_raw = json.dumps(result, ensure_ascii=False, indent=2)
            message_parts = split_string(json_raw, 3000)  # Разбиваем на части по 3000 символов

            for part in message_parts:
                bot.send_message(
                    message.chat.id,
                    f"<pre>{part}</pre>",
                    parse_mode="HTML"
                )
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при обработке ответа: {e}")

        # try:
        #     movie_id = result.get('docs', [])
        #     response_text = "Результаты поиска: \n\n"
        #
        #     for movie in movie_id:
        #         name = movie.get('name', 'Нет названия')
        #         year = movie.get('year', 'Нет данных')
        #         year =  movie.get('year', 'Нет данных')
        #         rating = movie.get('rating', {}).get('kp', 'Нет рейтинга')
        #         description = movie.get('description', 'Нет описания')[:500]  # Обрезаем описан
        #         backdrop = movie.get('backdrop', 'Нет ссылки на постер')
        #
        #         response_text += (
        #             f"🎬 <b>{name}</b> ({year})\n"
        #             f" <b>{backdrop}</b\n"
        #             f"⭐ Рейтинг: <b>{rating}</b>\n"
        #             f"📖 Описание: <i>{description}...</i>\n\n"
        #         )
        #
        #
        #     bot.send_message(
        #         message.chat.id,
        #         response_text,
        #         parse_mode="HTML"
        #     )

        # try:
        #     json_raw = json.dumps(result, ensure_ascii=False, indent=2)
        #     bot.send_message(message.chat.id, f"<pre>{json_raw}</pre>", parse_mode="HTML")
        # except Exception as e:
        #     bot.send_message(message.chat.id, f"Ошибка при обработке ответа: {e}")



@bot.message_handler(state=States.name)
def movie_search(message: Message) -> None:

    # проверяем, что введенное значение строка
    if not message.text.strip():  # если пустая строка или пробелы
        bot.send_message(message.chat.id, "Пожалуйста, введите название фильма")
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = api.movie_search(query=message.text, page=1, limit=10)

        if result is None:
            bot.send_message(message.chat.id, "Произошла ошибка при запросе к API")

        if not result:
            bot.send_message(message.chat.id, "Фильм с таким названием не найден")

        try:
            movies = result.get('docs', [])
            response_text = "Результаты поиска: \n\n"

            for movie in movies:
                name = movie.get('name', 'Нет названия')
                year = movie.get('year', 'Нет данных')
                rating = movie.get('rating', {}).get('kp', 'Нет рейтинга')
                description = movie.get('description', 'Нет описания')[:300]  # Обрезаем описание

                response_text += (
                    f"🎬 <b>{name}</b> ({year})\n"
                    f"⭐ Рейтинг: <b>{rating}</b>\n"
                    f"📖 Описание: <i>{description}...</i>\n\n"
                )

            bot.send_message(
                message.chat.id,
                response_text,
                parse_mode="HTML"
            )

        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при обработке ответа: {e}")


if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands(
        [
            telebot.types.BotCommand("movie_search_id", "Поиск фильма по id"),
            telebot.types.BotCommand("movie_search", "Поиск фильма по названию")
        ]
    )
    bot.polling()