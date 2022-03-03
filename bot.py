  # bot.py
  # Copyright 2022 Luana Neder
  #
  # This work may be distributed and/or modified under the
  # conditions of the LaTeX Project Public License, either version 1.3
  # of this license or (at your option) any later version.
  # The latest version of this license is in
  #   http://www.latex-project.org/lppl.txt
  # and version 1.3 or later is part of all distributions of LaTeX
  # version 2005/12/01 or later.
  #
  # This work has the LPPL maintenance status `maintained'.
  #
  # The Current Maintainer of this work is Luana Neder
  #
  # This work consists of the file bot.py



# Work In Progress

import tweepy # twitter client
import datetime # To print the time in the logs
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler # To auto run periodically
import os #for list files on lyrics dir 
import random #to grab a random file on the lyrics dir


# login


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# disk selector
file = open("current.txt", "r")
def disk():
    date = str(datetime.datetime.now())
    print(date + " changing disk")
    file.close()
    newdisk = random.choice(os.listdir("/lyrics"))
    src = "/lrcbot/lyrics" + newdisk
    dst = "/lrcbot/current.txt"
    os.replace(src, dst)
    print("disk changed to " + newdisk)
    file = open("current.txt", "r")

# bot
def bot():
    tweet = file.readline()
    if tweet == "EOF":
        disk()
        eof = True
    else:
        if tweet == "EOF\n":
            disk()
            eof = True
        else:
            eof = False

    if eof == False:
        try:
            client.create_tweet(text=tweet)
            date = str(datetime.datetime.now())
            print(date + "=" + tweet)
        except:
            try:
                print("error, trying to avoid duplicate")
                tweet = tweet + "⠀"
                client.create_tweet(text=tweet)
                date = str(datetime.datetime.now())
                print(date + "=" + tweet)
            except:
                print("error again, trying to avoid duplicate one last time")
                try:
                    tweet = tweet + "⠀"
                    client.create_tweet(text=tweet)
                    date = str(datetime.datetime.now())
                    print(date + "=" + tweet)

                except:
                    date = str(datetime.datetime.now())
                    print(date + "ERROR when tweeting = " + tweet)
                else:
                    pass


# cron
scheduler = BlockingScheduler()
scheduler.add_job(func=bot, trigger='interval', seconds=12, id='lyricsbot')
scheduler.start()
