import telebot
from telebot import types


def read_token(token_file: str) -> str:
    with open(token_file, "r") as f:
        TOKEN = "".join(f.readlines())
    return TOKEN


bot = telebot.TeleBot(read_token("token"))


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🌄 Случайный текст 🌠")

    markup.add(item1)

    bot.send_message(
        message.chat.id,
        "Привет, {0.first_name}! Отправь сообщение с текстом и бот сгенерирует тебе открытку с твоим пожеланием 🥰🥰🥰!".format(
            message.from_user
        ),
        reply_markup=markup,
    )


@bot.message_handler()
def interaction(message):
    bot.send_message(message.chat.id, message.text)


bot.polling(non_stop=True)
