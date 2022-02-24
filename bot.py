# //just testing for now probably shouldnt mind reading this lol

import tweepy

client = tweepy.Client("BEARER TOKEN")
api = tweepy.API(client)


api.update_status("Hello world")