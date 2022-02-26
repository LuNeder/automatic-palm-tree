# //just testing for now probably shouldnt mind reading this lol

import tweepy
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler


consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)

scheduler = BlockingScheduler()
scheduler.add_job(func=bot, trigger='interval', seconds=3600, id='lyricsbot')
scheduler.start()

def bot():
    client.create_tweet(text="Hello world")