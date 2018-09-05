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
