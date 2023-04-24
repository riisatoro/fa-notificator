import telebot
import requests

import consumer
import templates


API_TOKEN = '5996053155:AAFDHnVCZAz4pZGqTyIeGIkfsqj_4VdW3PI'

bot = telebot.TeleBot(API_TOKEN)
consumer = consumer.RabbitMQConsumer()


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, templates.START_MESSAGE)


@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.reply_to(message, templates.HELP_MESSAGE)


@bot.message_handler(commands=['cookies'])
def add_new_user(message):
    cookies = message.text.replace('/cookies ', '').split(' ')
    
    if len(cookies) != 2 or not all(cookies):
        bot.reply_to(message, templates.COOKIE_ERROR_MESSAGE)
        return

    consumer.send_new_user(message.chat.id, cookies[0], cookies[1])
    bot.reply_to(message, templates.COOKIE_SUCCESS_MESSAGE)


@bot.message_handler(commands=['setinterval'])
def change_interval(message):
    interval = message.text.replace('/setinterval ', '')
    if not interval.isnumeric():
        bot.reply_to(message, templates.INVALID_INTERVAL)

    consumer.set_new_interval(message.chat.id, interval)
    bot.reply_to(message, templates.INTERVAL_CHANGED)


@bot.message_handler(commands=['stop'])
def delete_user(message):
    consumer.delete_user(message.chat.id)
    bot.reply_to(message, templates.USER_DELETED_SUCCESSFULLY)


bot.infinity_polling()
