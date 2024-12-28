import telebot
from Include.NailsBot.Admin import callback
from lxml.html.diff import token
from numpy.ma.core import resize
from openpyxl.reader.excel import load_workbook

from pymupdf import message
from telebot import types
import random
from telebot.types import InputMediaPhoto, InlineKeyboardMarkup, ReplyKeyboardRemove
import csv
import telebot_calendar
from telebot_calendar import Calendar, CallbackData, RUSSIAN_LANGUAGE
import datetime
import openpyxl as xl
from openpyxl import load_workbook
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.utils import quote_sheetname, absolute_coordinate
from contextlib import redirect_stdout
import os
import sqlite3
import zipfile


name = None

TO_CHAT_ID = 7486722014  # Не забудьте подставить нужный id!













users = {}


bot = telebot.TeleBot('7587151505:AAEyx-l1wtEsxTDxHp6fSPhuhdp6VMR9r3g')
PRISE = '''
Сдесь Вы перечисляете перечень Ваших услуг или товаров и цену, сюда же можно добавить оплату
'''
CONTACT = '''
Город, телефон, адрес, электронная почта
'''



@bot.message_handler(commands=['start'])
def welcom(message):
    photo = open('Фото.jpg', 'rb')
    bot.send_photo(message.chat.id,photo, caption='🤩Здравствуй, я тестовый бот, протестируй пожалуйста меня, напиши свое имя и появятся кнопки💬' )
    bot.register_next_step_handler(message, answ)
def answ(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Прайс')
    btn2 = types.KeyboardButton('Контакты')
    btn3 = types.KeyboardButton('Локация')
    btn4 = types.KeyboardButton('Мои достижения')
    btn5 = types.KeyboardButton('Записаться')
    btn6 = types.KeyboardButton('Новости')





    markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id, f'Очень приятно {message.from_user.first_name}!!!🖐\nВыберите с помощью кнопок нужное Вам действие ',allow_sending_without_reply=True,reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Прайс')
def prise(message):
    bot.send_message(message.chat.id, PRISE)
@bot.message_handler(func=lambda message: message.text == 'Контакты')
def contact(message):
    bot.send_message(message.chat.id, CONTACT)
@bot.message_handler(func=lambda message: message.text == 'Мои достижения')
def My_achievemen(message):
    bot.send_message(message.chat.id, 'Сейчас загрузиться')
    bot.send_photo(message.chat.id, (open('Диплом.jpg', 'rb')))

@bot.message_handler(func=lambda message: message.text == 'Локация')
def location(message):
    bot.send_location(message.chat.id, 56, 82)
    bot.send_message(message.chat.id,'Сдесь может быть Ваше местоположения оказание услуг и указатель как добираться')



@bot.message_handler(func=lambda message: message.text == 'Записаться')
def record(message):
    conn = sqlite3.connect('bd1.sql')
    cur = conn.cursor()

    cur.execute(''' CREATE TABLE IF NOT EXISTS users (
            id int auto_increment primary key,
            name varchar(50),
            surname varchar,
            number varchar,
            data varchar,
            time varchar 
        ) ''')

    conn.commit()
    cur.close()
    conn.close()


    chat_id = message.chat.id
    bot.send_message(chat_id,'Введите своё имя: ')
    users[chat_id] = {}
    bot.register_next_step_handler(message, save_username)


def save_username(message):
    global name
    chat_id = message.chat.id

    name = message.text
    users[chat_id]['name'] = name
    bot.send_message(chat_id, f'Отлично, {name}. Введите Вашу фамилию: ')
    bot.register_next_step_handler(message, save_surname)


def save_surname(message):
    global surname
    chat_id = message.chat.id
    surname = message.text
    users[chat_id]['surname'] = surname
    name = users[chat_id]['name']
    surname = users[chat_id]['surname']
    bot.send_message(chat_id, f' {name} {surname} Введите Ваш номер телефона: ')
    bot.register_next_step_handler(message, number)

def number(message):
    global number
    chat_id = message.chat.id
    number = message.text
    users[chat_id]['number'] = number


#Day 1


    time_delt1 = timedelta(days=1)
    time_now = datetime.now()
    future_date1 = time_now + time_delt1

#Day 2
    time_delt2 = timedelta(days=2)
    time_now = datetime.now()
    future_date2 = time_now + time_delt2

#Day 3
    time_delt3 = timedelta(days=3)
    time_now = datetime.now()
    future_date3 = time_now + time_delt3

#Day 4
    time_delt4 = timedelta(days=4)
    time_now = datetime.now()
    future_date4 = time_now + time_delt4

#Day 5
    time_delt5 = timedelta(days=5)
    time_now = datetime.now()
    future_date5 = time_now + time_delt5

#Day 6
    time_delt6 = timedelta(days=6)
    time_now = datetime.now()
    future_date6 = time_now + time_delt6

#Day 7
    time_delt7 = timedelta(days=7)
    time_now = datetime.now()
    future_date7 = time_now + time_delt7



    markup = types.InlineKeyboardMarkup(row_width=4)
    global btn
    global btn1
    global btn2
    global btn3
    global btn4
    global btn5
    global btn6
    btn = types.InlineKeyboardButton(f'{future_date1.strftime("%d.%m.%Y")}', callback_data='date1')
    btn1 = types.InlineKeyboardButton(f'{future_date2.strftime("%d.%m.%Y")}', callback_data='date2')
    btn2 = types.InlineKeyboardButton(f'{future_date3.strftime("%d.%m.%Y")}', callback_data='date3')
    btn3 = types.InlineKeyboardButton(f'{future_date4.strftime("%d.%m.%Y")}', callback_data='date4')
    btn4 = types.InlineKeyboardButton(f'{future_date5.strftime("%d.%m.%Y")}', callback_data='date5')
    btn5 = types.InlineKeyboardButton(f'{future_date6.strftime("%d.%m.%Y")}', callback_data='date6')
    btn6 = types.InlineKeyboardButton(f'{future_date7.strftime("%d.%m.%Y")}', callback_data='date7')
    markup.add(btn,btn1,btn2,btn3,btn4,btn5, btn6)
    bot.send_message(message.chat.id, f'Выберете пожалуйста дату:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    reg = call.data.split('_')
    if reg[0] == 'date1':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date1':
        markup = types.InlineKeyboardMarkup()
        global bt1
        global bt2
        global bt3
        global bt4
        global bt5
        global bt6
        bt1 = types.InlineKeyboardButton(f'11:00', callback_data='hour1')
        bt2 = types.InlineKeyboardButton(f'12:00', callback_data='hour2')
        bt3 = types.InlineKeyboardButton(f'13:00', callback_data='hour3')
        bt4 = types.InlineKeyboardButton(f'14:00', callback_data='hour4')
        bt5 = types.InlineKeyboardButton(f'15:00', callback_data='hour5')
        bt6 = types.InlineKeyboardButton(f'16:00', callback_data='hour6')
        markup.add(bt1,bt2,bt3,bt4,bt5,bt6)
        bot.send_message(call.message.chat.id,'Выберите время :', reply_markup=markup )
        reg = call.data.split('_')
    if reg[0] == 'date2':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date2':
        global b1
        global b2
        global b3
        global b4
        global b5
        global b6
        markup = types.InlineKeyboardMarkup()
        b1 = types.InlineKeyboardButton(f'11:00', callback_data='hou1')
        b2 = types.InlineKeyboardButton(f'12:00', callback_data='hou2')
        b3 = types.InlineKeyboardButton(f'13:00', callback_data='hou3')
        b4 = types.InlineKeyboardButton(f'14:00', callback_data='hou4')
        b5 = types.InlineKeyboardButton(f'15:00', callback_data='hou5')
        b6 = types.InlineKeyboardButton(f'16:00', callback_data='hou6')
        markup.add(b1, b2, b3, b4, b5, b6)
        bot.send_message(call.message.chat.id, 'Выберите время :', reply_markup=markup)
    if reg[0] == 'date3':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date3':
        global button1
        global button2
        global button3
        global button4
        global button5
        global button6
        markup = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(f'11:00', callback_data='ho1')
        button2 = types.InlineKeyboardButton(f'12:00', callback_data='ho2')
        button3 = types.InlineKeyboardButton(f'13:00', callback_data='ho3')
        button4 = types.InlineKeyboardButton(f'14:00', callback_data='ho4')
        button5 = types.InlineKeyboardButton(f'15:00', callback_data='ho5')
        button6 = types.InlineKeyboardButton(f'16:00', callback_data='ho6')
        markup.add(button1,button2,button3,button4,button5,button6)
        bot.send_message(call.message.chat.id, 'Выберите время :', reply_markup=markup)
    if reg[0] == 'date4':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date4':
        global butto1
        global butto2
        global butto3
        global butto4
        global butto5
        global butto6
        markup = types.InlineKeyboardMarkup()
        butto1 = types.InlineKeyboardButton(f'11:00', callback_data='h1')
        butto2 = types.InlineKeyboardButton(f'12:00', callback_data='h2')
        butto3 = types.InlineKeyboardButton(f'13:00', callback_data='h3')
        butto4 = types.InlineKeyboardButton(f'14:00', callback_data='h4')
        butto5 = types.InlineKeyboardButton(f'15:00', callback_data='h5')
        butto6 = types.InlineKeyboardButton(f'16:00', callback_data='h6')
        markup.add(butto1,butto2,butto3,butto4,butto5,butto6)
        bot.send_message(call.message.chat.id, 'Выберите время :', reply_markup=markup)
    if reg[0] == 'date5':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date5':
        global butt1
        global butt2
        global butt3
        global butt4
        global butt5
        global butt6
        global butt7
        markup = types.InlineKeyboardMarkup()
        butt1 = types.InlineKeyboardButton(f'11:00', callback_data='1')
        butt2 = types.InlineKeyboardButton(f'12:00', callback_data='2')
        butt3 = types.InlineKeyboardButton(f'13:00', callback_data='3')
        butt4 = types.InlineKeyboardButton(f'14:00', callback_data='4')
        butt5 = types.InlineKeyboardButton(f'15:00', callback_data='5')
        butt6 = types.InlineKeyboardButton(f'16:00', callback_data='6')
        markup.add(butt1,butt2,butt3,butt4,butt5,butt6)
        bot.send_message(call.message.chat.id, 'Выберите время :', reply_markup=markup)
    if reg[0] == 'date6':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date6':
        global but1
        global but2
        global but3
        global but4
        global but5
        global but6
        markup = types.InlineKeyboardMarkup()
        but1 = types.InlineKeyboardButton(f'11:00', callback_data='1h')
        but2 = types.InlineKeyboardButton(f'12:00', callback_data='2h')
        but3 = types.InlineKeyboardButton(f'13:00', callback_data='3h')
        but4 = types.InlineKeyboardButton(f'14:00', callback_data='4h')
        but5 = types.InlineKeyboardButton(f'15:00', callback_data='5h')
        but6 = types.InlineKeyboardButton(f'16:00', callback_data='6h')
        markup.add(but1,but2,but3,but4,but5,but6)
        bot.send_message(call.message.chat.id, 'Выберите время :', reply_markup=markup)
    if reg[0] == 'date7':
        bot.delete_message(call.message.chat.id, call.message.message_id)
    if call.data == 'date7':
        global bu1
        global bu2
        global bu3
        global bu4
        global bu5
        global bu6
        markup = types.InlineKeyboardMarkup()
        bu1 = types.InlineKeyboardButton(f'11:00', callback_data='1ho')
        bu2 = types.InlineKeyboardButton(f'12:00', callback_data='2ho')
        bu3 = types.InlineKeyboardButton(f'13:00', callback_data='3ho')
        bu4 = types.InlineKeyboardButton(f'14:00', callback_data='4ho')
        bu5 = types.InlineKeyboardButton(f'15:00', callback_data='5ho')
        bu6 = types.InlineKeyboardButton(f'16:00', callback_data='6ho')
        markup.add(bu1,bu2,bu3,bu4,bu5,bu6)
        bot.send_message(call.message.chat.id, 'Выберите время :', reply_markup=markup)


#btn = date 1



    elif call.data == 'hour1':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn.text}  в {bt1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn.text}\nВремя: {bt1.text} ")  # отправляем в группу
    if reg[0] == 'hour1':
        bot.delete_message(call.message.chat.id, call.message.message_id)


    elif call.data == 'hour2':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn.text}  в {bt2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn.text}\nВремя: {bt2.text} ")  # отправляем в группу
        r = call.data.split('_')
    if reg[0] == 'hour2':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hour3':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn.text}  в {bt3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn.text}\nВремя: {bt3.text} ")  # отправляем в группу
    if reg[0] == 'hour3':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hour4':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn.text}  в {bt4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn.text}\nВремя: {bt4.text} ")  # отправляем в группу
    if reg[0] == 'hour4':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hour5':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn.text}  в {bt5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn.text}\nВремя: {bt5.text} ")  # отправляем в группу
    if reg[0] == 'hour5':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hour6':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn.text}  в {bt6.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn.text}\nВремя: {bt6.text} ")  # отправляем в группу
    if reg[0] == 'hour6':
        bot.delete_message(call.message.chat.id, call.message.message_id)





#btn1 = date 2
    elif call.data == 'hou1':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn1.text}  в {b1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn1.text}\nВремя: {b1.text} ")  # отправляем в группу
    if reg[0] == 'hou1':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hou2':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn1.text}  в {b2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn1.text}\nВремя: {b2.text} ")  # отправляем в группу
    if reg[0] == 'hou2':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hou3':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn1.text}  в {b3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn1.text}\nВремя: {b3.text} ")  # отправляем в группу
    if reg[0] == 'hou3':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hou4':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn1.text}  в {b4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn1.text}\nВремя: {b4.text} ")  # отправляем в группу
    if reg[0] == 'hou4':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hou5':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn1.text}  в {b5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn1.text}\nВремя: {b5.text} ")  # отправляем в группу
    if reg[0] == 'hou5':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'hou6':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn1.text}  в {b6.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn1.text}\nВремя: {b6.text} ")  # отправляем в группу
        if reg[0] == 'hou6':
            bot.delete_message(call.message.chat.id, call.message.message_id)








    #btn2 = date 3
    elif call.data == 'ho1':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn2.text}  в {button1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn2.text}\nВремя: {button1.text} ")  # отправляем в группу
    if reg[0] == 'ho1':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ho2':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn2.text}  в {button2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn2.text}\nВремя: {button2.text} ")  # отправляем в группу
    if reg[0] == 'ho2':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ho3':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn2.text}  в {button3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn2.text}\nВремя: {button3.text} ")  # отправляем в группу
    if reg[0] == 'ho3':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ho4':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn2.text}  в {button4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn2.text}\nВремя: {button4.text} ")  # отправляем в группу
    if reg[0] == 'ho4':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ho5':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn2.text}  в {button5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn2.text}\nВремя: {button5.text} ")  # отправляем в группу
    if reg[0] == 'ho5':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'ho6':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn2.text}  в {button6.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn2.text}\nВремя: {button6.text} ")  # отправляем в группу
    if reg[0] == 'ho6':
        bot.delete_message(call.message.chat.id, call.message.message_id)





    #btn3 = date 4
    elif call.data == 'h1':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn3.text}  в {butto1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn3.text}\nВремя: {butto1.text} ")  # отправляем в группу
    if reg[0] == 'h1':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'h2':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn3.text}  в {butto2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn3.text}\nВремя: {butto2.text} ")  # отправляем в группу
    if reg[0] == 'h2':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'h3':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn3.text}  в {butto3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn3.text}\nВремя: {butto3.text} ")  # отправляем в группу
    if reg[0] == 'h3':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'h4':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn3.text}  в {butto4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn3.text}\nВремя: {butto4.text} ")  # отправляем в группу
    if reg[0] == 'h4':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'h5':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn3.text}  в {butto5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn3.text}\nВремя: {butto5.text} ")  # отправляем в группу
    if reg[0] == 'h5':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == 'h6':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn3.text}  в {butto6.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn3.text}\nВремя: {butto6.text} ")  # отправляем в группу
    if reg[0] == 'h6':
        bot.delete_message(call.message.chat.id, call.message.message_id)



    ##btn4 = date 5
    elif call.data == '1':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn4.text}  в {butt1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn4.text}\nВремя: {butt1.text} ")  # отправляем в группу
    if reg[0] == '1':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '2':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn4.text}  в {butt2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn4.text}\nВремя: {butt2.text} ")  # отправляем в группу
    if reg[0] == '2':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '3':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn4.text}  в {butt3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn4.text}\nВремя: {butt3.text} ")  # отправляем в группу
    if reg[0] == '3':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '4':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn4.text}  в {butt4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn4.text}\nВремя: {butt4.text} ")  # отправляем в группу
    if reg[0] == '4':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '5':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn4.text}  в {butt5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn4.text}\nВремя: {butt5.text} ")  # отправляем в группу
    if reg[0] == '5':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '6':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn4.text}  в {butt6.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn4.text}\nВремя: {butt6.text} ")  # отправляем в группу
    if reg[0] == '6':
        bot.delete_message(call.message.chat.id, call.message.message_id)







    #btn5 = date 6
    elif call.data == '1h':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn5.text}  в {but1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn6.text}\nВремя: {but1.text} ")  # отправляем в группу
    if reg[0] == '1h':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '2h':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn5.text}  в {but2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn5.text}\nВремя: {but2.text} ")  # отправляем в группу
    if reg[0] == '2h':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '3h':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn5.text}  в {but3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn5.text}\nВремя: {but3.text} ")  # отправляем в группу
    if reg[0] == '3h':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '4h':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn5.text}  в {but4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn5.text}\nВремя: {but4.text} ")  # отправляем в группу
    if reg[0] == '4h':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '5h':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn5.text}  в {but5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn5.text}\nВремя: {but5.text} ")  # отправляем в группу
    if reg[0] == '5h':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '6h':
        bot.send_message(call.message.chat.id, f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn5.text}  в {but6.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn5.text}\nВремя: {but6.text} ")  # отправляем в группу
    if reg[0] == '6h':
        bot.delete_message(call.message.chat.id, call.message.message_id)






    #btn6 = date 7
    elif call.data == '1ho':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn6.text}  в {bu1.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id, f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn6.text}\nВремя: {bu1.text} ")  # отправляем в группу
    if reg[0] == '1ho':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '2ho':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn6.text}  в {bu2.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn6.text}\nВремя: {bu2.text} ")  # отправляем в группу
    if reg[0] == '2ho':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '3ho':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn6.text}  в {bu3.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn6.text}\nВремя: {bu3.text} ")  # отправляем в группу
    if reg[0] == '3ho':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '4ho':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn6.text}  в {bu4.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn6.text}\nВремя: {bu4.text} ")  # отправляем в группу
    if reg[0] == '4ho':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '5ho':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn6.text}  в {bu5.text}')
        group_chat_id = -4762887704  # chat id группы, в которую пересылаем сообщение
        bot.send_message(group_chat_id,f"У Вас запись:\n{name} {surname}\nТелефон: {number}\nДата: {btn6.text}\nВремя: {bu5.text} ")  # отправляем в группу
    if reg[0] == '5ho':
        bot.delete_message(call.message.chat.id, call.message.message_id)

    elif call.data == '6ho':
        bot.send_message(call.message.chat.id,f'{surname} {name}\nТелефон: {number}\nЖдем Вас {btn6.text}  в {bu6.text}')
        
        group_chat_id =  -4762887704  # chat id группы, в которую пересылаем сообщение
    if reg[0] == '6ho':
        bot.delete_message(call.message.chat.id, call.message.message_id)






        if __name__ == '__main__':
            print()




    #bot.clear_state(user_id=message.from_user.id, chat_id=message.chat.id)














#@bot.message_handler(content_types=['text'])






















#@bot.message_handler(func=lambda message: message.chat.type == 'private', content_types=['text'])
#def forward(message):
    #bot.forward_message(7486722014, message.chat.id,message.message_id)
























bot.polling(non_stop=True, interval=0)













