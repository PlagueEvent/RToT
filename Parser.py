#!/usr/bin/python3

import json
import os
import re
from datetime import date

links = []
check_links = []

today = date.today()


def rename_video(link):
    dir = '{}/'.format(today)
    fullname = link.split('/')
    temp_name = str(fullname[3] + fullname[4])
    temp_name = temp_name.split('?')
    name = dir + temp_name[0]
    return name


def rename_gifv(link):
    pass


# Download and save
def download_json(name):
    cr_dir = "mkdir {0}".format(today)
    my_command = r"wget -O {1}/{0}.json https://reddit.com/r/{0}.json".format(name, today)

    os.system(cr_dir)
    os.system(my_command)


def parsing(name, today,file_check_links):
    rating = []

    file_name = '{1}/{0}.json'.format(name, today)
    with open(file_name, 'r') as f:
        json_text = f.read()
    json_data = json.loads(json_text)

    # get rating 
    for rows in (json_data['data']['children']):
        rating.append(rows['data']['score'])
        rating.sort(reverse=True)
    rating = rating[:5]  # top 5 posts
    print(rating)

    
    with open(file_check_links, 'r') as f:
        check_links = f.read().strip().split(' ')


    # get links 
    for rows in (json_data['data']['children']):
        for rate in rating:
            if rate == rows['data']['score']:
                if rows['data']['is_video'] == True:
                    link = (rows['data']['media']['reddit_video']['fallback_url'])
                    if link not in check_links:
                        links.append(link)
                else:
                    link = (rows['data']['url'])
                    if link not in check_links:
                        links.append(link)



def downloads_files():
    for link in links:
        if re.findall("fallback", link):
            name = rename_video(link)
            command = 'wget -O {2} -P {0} {1}'.format(today, link, name)
            os.system(command)
        else:
            command = 'wget -P {0} {1}'.format(today, link)
            os.system(command)



def links_writer(file_check_links):
    with open(file_check_links, 'a') as f:
        print(*links, file=f)
    file_name = '{0}/today_links'.format(today)
    with open(file_name, 'w') as f:
        print(*links, file=f)
