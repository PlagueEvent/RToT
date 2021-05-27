#!/usr/bin/python3
import os
import re
import time
import telebot
from datetime import date
from Parser import rename_video

today = date.today()
names = []


def getFileName():
    today_list = '{0}/today_links'.format(today)
    names = []
    with open(today_list, 'r') as f:
        links = f.read().strip().split(' ')

    for link in links:
        print(link, type(link))
        if re.findall("fallback", link):
            names.append(str(rename_video(link)))
        else:
            fullname = link.split('/')
            dir = '{}/'.format(today)
            name = dir + fullname[3]
            names.append(name)
    return names


def bot(tg_channel, sec):
    names = getFileName()
    TOKEN = os.environ.get('TG_TOKEN')
    tb = telebot.TeleBot(TOKEN)

    for name in names:
        print(name)
        file = open(name, 'rb')
        try:
            if re.findall("jpg", name):
                tb.send_photo(tg_channel, file)
            if re.findall("png", name):
                tb.send_photo(tg_channel, file)
            if (re.findall("gifv", name):
                continue
            if re.findall("gif", name):
                tb.send_animation(tg_channel, file)
            if re.findall("DASH", name):
                tb.send_video(tg_channel, file)
            else:
                pass
        except:
            print(name, "Ncomment_bot,  Здесь упало с ошибкой!")
            continue
        time.sleep(sec)
