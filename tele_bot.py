#!/usr/bin/env python3
import random

import telebot
from telebot.types import Message

TOKEN = ''

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo_gigits(message):
    if 'Hello' in message.text:
        bot.reply_to(message, 'Hi!')
    return
    bot.reply_to(message, str(random.random()))

bot.polling(timeout=60)
