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
                        'Далее в открывшемся окне пишем следующее:\n`pip install pyTelegramBotAPI`. Если Вы сделали всё правильно, то все строки '+
                        'в консоли должны быть белыми. Если же появились красные строки (ошибка), то надо прописать в консоль следующее:\n'+
                        '`python -m pip install --upgrade pip`\nЭта команда обновит вашу пип-консоль. После этого установите библиотеку повторно ('+
                        '`pip install pyTelegramBotAPI`).\n\nПоздравляю! Если вы всё сделали правильно, то ваш python готов к написанию на нём кода)',
                        parse_mode='markdown')
    
@bot.message_handler(commands=['codeguide'])
def codeguide(m):
   if m.from_user.id==m.chat.id:
        bot.send_message(m.chat.id, 'Если вы нажали на эту команду, то вы, вероятно, уже прочитали пункт /basetools. Тогда '+
                         'приступим к написанию кода.\n\n*Как начать*\n\nГайд предназначен для тех, кто хотя бы немного знаком '+
                         'с понятием "язык программирования" и знаете хотя бы один из них. Если же нет, то вам будет немного тяжелее '+
                         'понять всё то, что я здесь опишу. Ладно, давайте к коду.\nПервые строки вашего кода должны содержать '+
                         'импортируемые библиотеки и переменные, в которых хранится информация о нашем боте (токен бота). Первая библиотека, которая '+
                         'нам обязательно понадобится, это `telebot`. Чтобы добавить её в наш код, первой строкой пишем:\nimport telebot\n'+
                         'Теперь про токен. Чтобы его получить, надо написать '+
                         'боту @BotFather и создать нового бота. В итоге он выдаст вам токен, который выглядит примерно так:\n'+
                         '12345:AbCdefGhigk43g\n(Не пытайтесь ввести этот токен, он невалидный).\nДалее нужно создать переменную, которая и будет '+
                         'давать нашей программе доступ к боту. Делается это так:\n'+
                         '`bot=telebot.TeleBot("ваш_токен")`.\nОбязательно нужно ставить токен, который вам выдал botfather, в кавычки.'+
                         'Вместо переменной *bot* вы можете придумать любое другое название.\n\nПоздравляю! Теперь вы готовы к написанию кода, '+
                         'отвечающего за реакцию бота на внешние раздражители (сообщения, стикеры и многое другое)! Для этого нажмите '+
                         '/code_part2.', parse_mode='markdown')
    

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
