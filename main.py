import os
import telebot
from telebot import types
from dotenv import load_dotenv
from models.back_generator import image

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🌄 Случайный текст 🌠")
    item2 = types.KeyboardButton("Другое ➡️")

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
    bot.send_message(message.chat.id, message.text)
    image()
    bot.send_photo(message.chat.id, photo=open("./output/image_.png", "rb"))


bot.polling(non_stop=True)
