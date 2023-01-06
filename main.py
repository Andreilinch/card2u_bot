import os
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):
    """Initial messages and design

    Args:
        message (_type_): _description_
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(text="🌄 Случайный текст 🌠")
    item2 = types.KeyboardButton(text="Другое ➡️")

    markup.add(item1, item2)

    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Отправь сообщение с текстом и бот сгенерирует тебе \
        открытку с твоим пожеланием 🥰🥰🥰! Еще бот может сгенерировать открытку \
        со случайным текстом 🪄".format(
            message.from_user
        ),
        reply_markup=markup,
    )


@bot.message_handler()
def interaction(message):
    """Reply function

    Args:
        message (_type_): _description_
    """
    bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)
