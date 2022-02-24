# //just testing for now probably shouldnt mind reading this lol

import tweepy

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)



client.create_tweet(text="Hello world")