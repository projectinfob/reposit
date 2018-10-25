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
db=client.channelsbase
users=db.users
channels=db.channels

   
    
    
@bot.message_handler(commands=['start'])
def start(m):
    if m.from_user.id==m.chat.id:
        kb=types.ReplyKeyboardMarkup()
        kb.add(types.ReplyKeyboardButton('📮ПРОДАТЬ РЕКЛАМУ'))
        kb.add(types.ReplyKeyboardButton('МУЗЫКА'),types.ReplyKeyboardButton('БЛОГИ'))
        kb.add(types.ReplyKeyboardButton('КАНАЛЫ1'),types.ReplyKeyboardButton('КАНАЛЫ2'))
        kb.add(types.ReplyKeyboardButton('КАНАЛЫ3'),types.ReplyKeyboardButton('КАНАЛЫ4'))
        bot.send_message(m.chat.id, '🏡Главное меню',reply_markup=kb)
        
        

@bot.message_handler()
def channelselect(m):
    if m.text=='МУЗЫКА':
        x=channels.find_one({})
        y=x['music']
        channel=0
        text=''
        i=channel+3
        while channel<i:
            ch=y[channel]
            text+='Рекламодатель: '+ch['reklamodatel']+'\n'
            text+='Канал: '+ch['channel']+'\n'
            text+='Подписчиков: '+str(ch['subs'])+'\n'
            text+='Цена: '+str(ch['cost'])+'\n'
            text+='Скидка: '+str(ch['discount'])+'\n'
            text+='Итоговая цена: '+str(ch['finalcost'])+'\n'
            text+='Тематика: '+themetoname(ch['theme'])+'\n'
            text+='Взаимный пиар: '+yesno(ch['piar'])+'\n'
            text+='Условия: '+ch['conditions']+'\n'
            text+='Для заказа рекламы тебе стоит написать администратору канала.\n'
            text+='\n'
            channel+=1
        kb=types.ReplyKeyboardMarkup()
        kb.add(types.ReplyKeyboardButton(''),types.ReplyKeyboardButton(''))
            
            

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
