#!/usr/bin/python3


from typing import Counter
import praw 
import json

#open a file called config.json.
with open("config.json", "r") as file: 
    config = json.load(file)

id = config["client_id"]
secret = config["secret"]
reddit_username = config["reddit_username"]
reddit_password = config["reddit_password"]

#configure the bot
reddit = praw.Reddit(
    client_id= id ,
    client_secret = secret,
    password = reddit_password,
    user_agent = "kalogero by" + reddit_username,
    username = reddit_username,
)

#if the log in is correct will print the reddit username
print("\n")
print(reddit.user.me())
print("\n")

#subreddit = reddit.subreddit("wallstreetbets")

new_wallstreetbest = reddit.subreddit("wallstreetbets").hot(limit = 15)

counter = 0

for submission in new_wallstreetbest:
    if not submission.stickied:
        print(counter)
        print(") \n")
        print("Title:", submission.title)
        if (submission.selftext ):
            print("Text:", submission.selftext)
        print("Score:", submission.score)
        print("-----------------------\n")
        counter = counter + 1
        


pass