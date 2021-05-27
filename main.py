#!/usr/bin/python3
import os
from datetime import date
from Parser import download_json
from Parser import downloads_files
from Parser import links_writer
from Parser import parsing
from NComment_bot import bot


#Options
subreddits = ['memes', 'funny', 'aww', 'enexpected', 'earthporn', 'animalsbeingjerks', 'gifs', 'nextfuckinglevel',
              'pics', 'cats']

tg_channel = '@lol_what7'  #t.me/lol_what7
sec = 30                   #repost timeout 
today = date.today()


#where is check_links file? 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_check_links = BASE_DIR + '/check_links'


def main():
    for subreddit in subreddits:
        download_json(subreddit)
        parsing(subreddit, today, file_check_links)

    downloads_files()
    links_writer(file_check_links)
    bot(tg_channel,sec)


if __name__ == "__main__":
    main()
