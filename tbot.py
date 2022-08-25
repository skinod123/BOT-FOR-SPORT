import telebot
from telebot import types   
import bot_config 

bot = telebot.TeleBot(bot_config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'привет я бот-спорт консультант по спорту и ассистент, <b>{message.from_user.first_name}<u>{message.from_user.last_name}</u><</b>'
    
@bot.message_handler(commands=['sportsite'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("посетить веб сайт", url='https://bigser.kg/'))
    bot.send_message(message.chat.id, 'перейти на сайт', reply_markup=markup)


@bot.message_handler(commands=['more'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 2)
    website = types.KeyboardButton('/больше')
    start = types.KeyboardButton('/start')
    markup.add(website,start)
    bot.send_message(message.chat.id, 'Перейти на сайт', reply_markup=markup)

bot.polling(none_stop=True)
