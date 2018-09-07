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
                         'Там скачайте `Windows x86 executable installer` и установите .exe файл. Проделав этот шаг, вы утсановите '+
                        'python на свой компьютер, но для возможности написания кода для telegram вам потребуется специальная '+
                        'библиотека, которую Вы можете скачать через встроенную в python pip-консоль. Но чтобы иметь доступ '+
                        'к ней, вам потребуется добавить python в path. Ниже будет описано, как это сделать.\n\n'+
                        '*Добавление python в path*\nОткрываем мой компьютер --> Свойства системы --> Дополнительные параметры системы -->\n'+
                         'Переменные среды --> Находим снизу Системные переменные. Среди них есть переменная Path. '+
                         'Выделяем её и нажимаем Изменить. (в конце всего, что в этой переменной уже есть, пишем путь к папке Scripts питона. '+
                        'У Вас он может находиться в другом месте, но покажу, какую строку вставил я:\n'+
                        '*c:\Users\Имя_пользователя\AppData\Local\Programs\Python\Python36\Scripts\;c:\Users\Имя_пользователя\AppData\Local\Programs\Python\Python36-32\Scripts\*\n'+
                        'Если вы всё сделали правильно, то переходим к следующему шагу - установка библиотеки PyTelegramBotApi.\n\n'+
                        'Нажимаем кнопку "Пуск", и в строке "Найти программы и файлы" прописываем команду `cmd` и жмём Enter.'+
                        'Далее в открывшемся окне пишем следующее:\n`pip install pyTelegramBotAPI`.)
    
    c:\Users\Имя_пользователя\AppData\Local\Programs\Python\Python36\Scripts\;c:\Users\Имя_пользователя\AppData\Local\Programs\Python\Python36-32\Scripts\
    
    

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
