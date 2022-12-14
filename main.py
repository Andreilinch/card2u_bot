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
    item1 = types.KeyboardButton("🌄 Волшебное утро")
    item2 = types.KeyboardButton("🍗 Прекрасный обеденный перерыв")
    item3 = types.KeyboardButton("🌠 Умиротворяющий вечер")

    markup.add(item1, item2, item3)

    bot.send_message(
        message.chat.id,
        "Привет дорогой, {0.first_name}! Выбери пожелание для твоего времени дня 🥰".format(message.from_user),
        reply_markup=markup,
    )

# @bot.message_handler(content_types=["text"])
# def process_message(message):
#     if message.text == '🌄 Волшебное утро':
#         # bot.send_photo
#         pass
#     elif message.text == '🌄 Прекрасный обеденный перерыв':
#         pass
#     elif message.text == '🌠 Умиротворяющий вечер':
#         pass
#     else:
#         pass






bot.polling(non_stop=True)
