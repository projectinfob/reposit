# -*- coding: utf-8 -*-
import os
import telebot
import time
import chlenomerconfig
import telebot
import random
from telebot import types
from pymongo import MongoClient
import threading

client1=os.environ['database']
client=MongoClient(client1)
db=client.infobase
users=db.users

   
    
    
@bot.message_handler(commands=['start'])
def start(m):
    if m.from_user.id==m.chat.id:
        bot.send_message(m.chat.id, 'Здраствуйте, Вас приветствует бот-помощник, который научит Вас самостоятельно писать '+
                         'ботов для мессенджера Telegram. Если Вас интересует, как установить среду для разработки, нажмите /basetools.\n'+
                         'Если вы не знаете, как написать сам код для бота, нажмите /codeguide;\nЕсли '+
                         'Вас интересует то, где бесплатно организовать хостинг для бота (его постоянную работу), нажмите /hosting.\n'+
                         'Ответы на частозадаваемые вопросы вы можете найти по команде /answers.')
  
    
@bot.message_handler(commands=['basetools'])
def basetools(m):
    if m.from_user.id==m.chat.id:
        bot.send_message(m.chat.id, 'Чтобы скачать python с оффициального сайта, нажмите на ссылку ниже.\n'+
                         'https://www.python.org/downloads/release/python-361/'+'\nЗатем пролистайте сайт вниз, до надписи FILES.'+
                         'Там скачайте `Windows x86 executable installer` и установите .exe файл.')
    
    
    
    

if True:
 try:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
 except (requests.ReadTimeout):
        print('!!! READTIME OUT !!!')           
        bot.stop_polling()
        time.sleep(1)
        check = True
        while check==True:
          try:
            bot.polling(none_stop=True,timeout=1)
            print('checkkk')
            check = False
          except (requests.exceptions.ConnectionError):
            time.sleep(1)                    
