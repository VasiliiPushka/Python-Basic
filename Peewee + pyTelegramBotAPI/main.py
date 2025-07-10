import telebot
import json

from telebot.types import Message
from telebot import custom_filters
from telebot.storage import StateMemoryStorage

from api.api import print_info, movie_search, movie_search_id, filter_list
from Telegramm_bot.database.crud import get_or_create_user
from config.config import BOT_TOKEN
from states.states import States, MovieStates
from db.crud import *


state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)

@bot.message_handler(commands=["start"])
def start(message: Message) -> None:

    user_id = message.from_user.id or ''
    username = message.from_user.username or ''
    first_name = message.from_user.first_name or ''
    last_name = message.from_user.last_name or ''

    user, created = get_or_create_user(user_id, username, first_name, last_name)

    if created:
        bot.send_message(message.from_user.id, f"Добро пожаловать в бот по поиску фильмов, {username}!")
    else:
        bot.send_message(message.from_user.id, f"Рад снова тебя видеть, {username}!")


@bot.message_handler(commands=["movie_search_id"])
def movie_search_id_command(message: Message) -> None:
    bot.send_message(message.chat.id, f"Укажите id в диапазоне от 250 до 10000000!")
    bot.set_state(message.from_user.id, States.id, message.chat.id)


@bot.message_handler(state=States.id)
def movie_search_id(message: Message) -> None:

    if not message.text.isdigit():
        bot.send_message(message.chat.id, "Пожалуйста, введите числовой ID")
        return

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        result = movie_search_id(message.text)

        if result is None:
            bot.send_message(message.chat.id, f"Произошла ошибка при запросе к API")

        if not result:
            bot.send_message(message.chat.id, f"Фильм с таким id не найден")

        try:
            movie_id_info = result.get('docs')
            print(json.dumps(movie_id_info, ensure_ascii=False, indent=4))

            for info in movie_id_info:
                name = info.get('name')
                description = info.get('description')
                rating = info.get('rating')
                year = info.get('year')
                genres = info.get('genres')
                age_rating = info.get('ageRating')
                poster = info.get('poster')

                response_text = (
                    f"<b>{name}</b>\n"
                    f"<b>Год выпуска: {year}</b>\n"
                    f"<b>Рейтинг</b>\n"
                    f"  • КиноПоиск: {rating.get('kp', 'N/A')}\n"
                    f"  • IMDB: {rating.get('imdb', 'N/A')}\n"
                    f"<b>Возрастной рейтинг:</b> {age_rating}+\n"
                    f"<b>Жанр:</b> {genres}\n"
                    f"<b>Описание:</b> {description}"
                    )

                if poster and poster.get('url'):
                    bot.send_photo(
                        message.chat.id,
                        poster['url'],
                        caption=response_text,
                        parse_mode='HTML'
                    )
                else:
                    bot.send_message(
                        message.chat.id,
                        response_text,
                        parse_mode='HTML'
                    )

        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при обработке ответа: {e}")


@bot.message_handler(commands=["movie_search"])
@bot.message_handler(state=States.name)
def ask_movie_query(message: Message) -> None:
    bot.send_message(message.chat.id, f"Пожалуйста, введите название фильма для поиска 🎬")
    bot.set_state(message.from_user.id, MovieStates.query, message.chat.id)


@bot.message_handler(state=MovieStates.query)
def ask_movie_page(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['query'] = message.text

    bot.send_message(message.chat.id, f"Укажите страницу выборки фильма")
    bot.set_state(message.from_user.id, MovieStates.page, message.chat.id)


@bot.message_handler(state=MovieStates.page)
def ask_movie_limit(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['page'] = message.text

    bot.send_message(message.chat.id, f"Укажите какое количество фильмов с введенным ранее "
                                      f"названием необходимо вывести на экран")
    bot.set_state(message.from_user.id, MovieStates.limit, message.chat.id)


@bot.message_handler(state=MovieStates.limit)
def ask_movie_search(message: Message) -> None:
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        try:
            query = data['query']
            page = data['page']
            limit = message.text

            print_info(query=query, page=page, limit=limit)

            result = movie_search(page=int(page), limit=int(limit), query=query)
            movies = result.get('docs', [])

            for movie_data in movies:
                # Извлекаем данные
                api_id = str(movie_data.get('id'))
                title = movie_data.get('name', 'Неизвестно')
                description = movie_data.get('description', 'Описание отсутствует')
                rating = movie_data.get('rating', {})
                rating_kp = float(rating.get('kp', 0))
                rating_imdb = float(rating.get('imdb', 0))
                year = str(movie_data.get('year', 'Неизвестно'))
                age_rating = str(movie_data.get('ageRating', 0))
                budget = str(movie_data.get('budget', {}).get('value', 'Неизвестно'))
                poster_url = movie_data.get('poster', {}).get('url')
                is_series = bool(movie_data.get('isSeries', False))

                movie, created = create_or_get_movie(
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

                filter_genres = [genre.get('name') for genre in movie_data.get('genres', [])]

                movie_text = (
                    f"🎬 <b>{title}</b>\n"
                    f"   <b>Год выпуска: {year}</b>\n"
                    f"⭐ <b>Рейтинг</b>\n"
                    f"  • КиноПоиск: {rating.get('kp', 'N/A')}\n"
                    f"  • IMDB: {rating.get('imdb', 'N/A')}\n"
                    f"<b>Возрастной рейтинг:</b> {age_rating}+\n"
                    f"<b>Жанр:</b> {filter_list(filter_genres)}\n"
                    f"📖 <b>Описание:</b> {description}"
                    )

                if poster_url:
                    bot.send_photo(message.chat.id, poster_url, caption=movie_text,
                        parse_mode='HTML')
                else:
                    bot.send_message(
                        message.chat.id,
                        movie_text,
                        parse_mode='HTML'
                        )

                bot.delete_state(message.from_user.id, message.chat.id)

        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при обработке ответа: {e}")
            bot.delete_state(message.from_user.id, message.chat.id)


if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands(
        [
            telebot.types.BotCommand("movie_search_id", "Поиск фильма по id"),
            telebot.types.BotCommand("movie_search", "Поиск фильма по названию"),
            telebot.types.BotCommand("start", "Нажми для начала работы")
        ]
    )
    bot.polling()