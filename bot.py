# //just testing for now probably shouldnt mind reading this lol

import tweepy
import datetime
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


# login


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

# disk selector
def music():
    date = str(datetime.datetime.now())
    print(date + " changing disk")


# bot
file = open("current.txt", "r")
def bot():
    tweet = file.readline()
    if tweet == "EOF":
        music()
        eof = True
    else:
        if tweet == "EOF\n":
            music()
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
