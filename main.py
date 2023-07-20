import telebot
import os
from os.path import join, dirname
from dotenv import load_dotenv
from telebot import types
def get_from_env(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)
token = get_from_env('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'back'])
def start(message):
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
            url = types.KeyboardButton('/url')
            text = types.KeyboardButton('/text')
            vcard = types.KeyboardButton('/vcard')
            sms = types.KeyboardButton('/sms')
            call = types.KeyboardButton('/call')
            geo = types.KeyboardButton('/geo')
            event = types.KeyboardButton('/event')
            email = types.KeyboardButton('/email')
            wifi = types.KeyboardButton('/wifi')
            make_a_tip = types.KeyboardButton('/make_a_tip')
            markup.add(url, text, vcard, sms, call, geo, event, email, wifi, make_a_tip)
            bot.send_message(message.chat.id, 'Chose option to generate QR code', reply_markup=markup)

@bot.message_handler(commands=['url'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter your url in format = https://example.com', reply_markup=markup)
    bot.register_next_step_handler(msg, urlrecord)
def urlrecord(message):
    user_info = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id, f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={user_info}')
        start(message)

@bot.message_handler(commands=['text'])
def text(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter your text in free format', reply_markup=markup)
    bot.register_next_step_handler(msg, textrecord)
def textrecord(message):
    user_info = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={user_info}')
        start(message)
@bot.message_handler(commands=['vcard'])
def vcard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter name of your contact', reply_markup=markup)
    bot.register_next_step_handler(msg, vcardnamerecord)
def vcardnamerecord(message):
    user_info = {}
    user_info['name'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter organization of your contact')
        bot.register_next_step_handler(msg, vcardorgrecord, user_info)
def vcardorgrecord(message, user_info):
    user_info['org'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter phone of your contact')
        bot.register_next_step_handler(msg, vcardphonerecord, user_info)
def vcardphonerecord(message, user_info):
    user_info['phone'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter note of your contact')
        bot.register_next_step_handler(msg, vcardnoterecord, user_info)
def vcardnoterecord(message, user_info):
    user_info['note'] = message.text
    name = user_info['name']
    phone = user_info['phone']
    org = user_info['org']
    note = user_info['note']
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=BEGIN%3AVCARD%0AVERSION%3A2.1%0AFN%3A{name}%0AN%3A%3B{name}%0ATEL%3BWORK%3BVOICE%3A{phone}%0ANOTE%3A{note}%0AORG%3A{org}%0AEND%3AVCARD%0A')
        start(message)
@bot.message_handler(commands=['sms'])
def sms(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter phone for your sms', reply_markup=markup)
    bot.register_next_step_handler(msg, smsphonerecord)
def smsphonerecord(message):
    user_info = {}
    user_info['phone'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter text for your sms')
        bot.register_next_step_handler(msg, smstextrecord, user_info)
def smstextrecord(message, user_info):
    user_info['text'] = message.text
    phone = user_info['phone']
    text = user_info['text']
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=SMSTO:{phone}:{text}')
        start(message)
@bot.message_handler(commands=['call'])
def call(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter phone. Number only format', reply_markup=markup)
    bot.register_next_step_handler(msg, callrecord)
def callrecord(message):
    user_info = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=tel:+{user_info}')
        start(message)
@bot.message_handler(commands=['geo'])
def geo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Share your location to bot or write latitude and longitude. \nExample: 38.8951,-77.0364', reply_markup=markup)
    bot.register_next_step_handler(msg, georecord)
def georecord(message):
    user_info = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=geo:{user_info}')
        start(message)
@bot.message_handler(commands=['event'])
def event(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter description of your event', reply_markup=markup)
    bot.register_next_step_handler(msg, eventnamerecord)
def eventnamerecord(message):
    user_info = {}
    user_info['name'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter start date of your event in yearmonthday format \nExample: 20220611')
        bot.register_next_step_handler(msg, eventdaterecord, user_info)
def eventdaterecord(message, user_info):
    user_info['sdate'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter start time of your event. \nExample: 1030 where 10 = hours, 30 = minutes GMT+6')
        bot.register_next_step_handler(msg, eventtimerecord, user_info)
def eventtimerecord(message, user_info):
    user_info['stime'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter end date of your event in yearmonthday format \nExample: 20220611')
        bot.register_next_step_handler(msg, eventdateendrecord, user_info)
def eventdateendrecord(message, user_info):
    user_info['edate'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter end time of your event. \nExample: 1030 where 10 = hours, 30 = minutes GMT+6')
        bot.register_next_step_handler(msg, eventtimeendrecord, user_info)
def eventtimeendrecord(message, user_info):
    user_info['etime'] = message.text
    name = user_info['name']
    sdate = user_info['sdate']
    stime = user_info['stime']
    edate = user_info['edate']
    etime = user_info['etime']
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=BEGIN%3AVEVENT%0ASUMMARY%3A{name}%0ADTSTART%3A{sdate}T{stime}00Z%0ADTEND%3A{edate}T{etime}00Z%0AEND%3AVEVENT')
        start(message)
@bot.message_handler(commands=['email'])
def email(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter adress for your email', reply_markup=markup)
    bot.register_next_step_handler(msg, emailadrrecord)
def emailadrrecord(message):
    user_info = {}
    user_info['adr'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter subject for your email')
        bot.register_next_step_handler(msg, emailsubjrecord, user_info)
def emailsubjrecord(message, user_info):
    user_info['subj'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter body for your email')
        bot.register_next_step_handler(msg, emailbodyrecord, user_info)
def emailbodyrecord(message, user_info):
    user_info['body'] = message.text
    adr = user_info['adr']
    subj = user_info['subj']
    body = user_info['body']
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=MATMSG:TO:{adr};SUB:{subj};BODY:{body};;')
        start(message)
@bot.message_handler(commands=['wifi'])
def wifi(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'Enter adress of your wifi network', reply_markup=markup)
    bot.register_next_step_handler(msg, wifiadrrecord)
def wifiadrrecord(message):
    user_info = {}
    user_info['adr'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter type of your wifi encryption (WPA,WEP,nopass)')
        bot.register_next_step_handler(msg, wifiencrecord, user_info)
def wifiencrecord(message, user_info):
    user_info['enc'] = message.text
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        msg = bot.send_message(message.chat.id, 'Enter password of your wifi network')
        bot.register_next_step_handler(msg, wifipassrecord, user_info)
def wifipassrecord(message, user_info):
    user_info['passwd'] = message.text
    adr = user_info['adr']
    enc = user_info['enc']
    passwd = user_info['passwd']
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id,f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=WIFI:T:{enc};S:{adr};P:{passwd};;')
        start(message)
@bot.message_handler(commands=['make_a_tip'])
def tip(message):
    bot.send_message(message.chat.id, 'If you wanna tip me - https://www.buymeacoffee.com//wolfhoundt6')
@bot.message_handler(content_types=['location'])
def get_user_location(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    back = types.KeyboardButton('/back')
    markup.add(back)
    latitude = message.location.latitude
    longitude = message.location.longitude
    try:
        if message.entities[0].type == 'bot_command':
            start(message)
    except:
        bot.send_photo(message.chat.id, f'https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=geo:{latitude},{longitude}', reply_markup=markup)
        start(message)
bot.polling(none_stop=True)