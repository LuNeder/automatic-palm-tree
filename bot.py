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
import time # To wait between tweets
import os #for list files on lyrics dir
import random #to grab a random file on the lyrics dir


# login


client = tweepy.Client(
    consumer_key=consumer_key, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)


file = open("current.txt", "r")




# disc selector
def disc():
    date = str(datetime.datetime.now())
    print(date + " changing disc")
    #file.close()
    try:
        newdisc = random.choice(os.listdir("lyrics"))
    except:
        client.create_tweet(text="Error changing disc. There may be no new discs available or the next one is scratched.\nThe bot has abended. @1u4n4mh please check.")
        print(str(datetime.datetime.now()) + "ERROR changing disc, bot will abend.")
    src = "lyrics/" + newdisc
    dst = "current.txt"
    if "music" in newdisc:
        type = open("type.txt", "w")
        type.write("music")
        type.close()
        print("type: music")
    elif "poem" in newdisc:
        type = open("type.txt", "w")
        type.write("poem")
        type.close()
        print("type: poem")
    elif "ad" in newdisc:
        type = open("type.txt", "w")
        type.write("ad")
        type.close()
        print("type: ad")
    else:
        print("error detecting type")
    os.replace(src, dst)
    print("disc changed to " + newdisc)
    file = open("current.txt", "r")
    return file

# bot
while True:


    emus = ["🎶", "🎼", "🎵", "🎤", "🎧", "🎸", "🥁", "🎹", "🎺", "🎻", "🎷", "🪗", "🪘", "🪕"]
    epoe = ["📝", "🖊", "✍️"]
    ead = ["📑", "📰"]
    type = open("type.txt", "r")
    type = type.readline().replace("\n", "")
    if type == "music":
        one = random.choice(emus)
        two = random.choice(emus)
    elif type == "poem":
        one = random.choice(epoe)
        two = random.choice(epoe)
    elif type == "ad":
        one = random.choice(ead)
        two = random.choice(ead)
    else:
        print("no type?")
        one = "  ?  "
        two = "  ?  "

    tweet = one + file.readline().replace("\n", "") + two
    if tweet == "EOF":
        file.close()
        file = disc()
        eof = True
    else:
        if tweet == "EOF\n":
            file.close()
            file = disc()
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
        time.sleep(12)
