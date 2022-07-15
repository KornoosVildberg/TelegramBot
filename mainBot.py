import telebot

bot = telebot.TeleBot('5360883455:AAHk4kyImiqL5VS7Vd4Xwz9AmCVubGwfut4')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '<b>Привет</b>', parse_mode='html')


    bot.polling(non_stop=True)