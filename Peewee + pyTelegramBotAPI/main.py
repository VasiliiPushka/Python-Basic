import telebot
import json
from telebot.types import Message
from telebot import custom_filters
from telebot.storage import StateMemoryStorage

import api
from config import BOT_TOKEN, API_KEY, API_BASE_URL
from states import States

state_storage = StateMemoryStorage()
bot = telebot.TeleBot(BOT_TOKEN, state_storage=state_storage)


@bot.message_handler(commands=["start"])
def start(message: Message) -> None:
    bot.send_message(
        message.chat.id, f"Привет! Я телеграмм бот основанный на API кинопоиска"
    )
    bot.set_state(message.from_user.id, States.base, message.chat.id)


@bot.message_handler(commands=["movie_search_id"])
def movie_search_command(message: Message) -> None:
    bot.send_message(message.chat.id, f"Укажите id в диапазоне от 250 до 10000000!")
    bot.set_state(message.from_user.id, States.id, message.chat.id)


@bot.message_handler(state=States.id)
def movie_search(message: Message) -> None:
    # Проверяем, что введенное значение - число
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
            bot.send_message(
                message.chat.id, f"<pre>{json_raw}</pre>", parse_mode="HTML"
            )
        except Exception as e:
            bot.send_message(message.chat.id, f"Ошибка при обработке ответа: {e}")


if __name__ == "__main__":
    bot.add_custom_filter(custom_filters.StateFilter(bot))
    bot.set_my_commands(
        [telebot.types.BotCommand("movie_search_id", "Поиск фильма по id")]
    )
    bot.polling()
