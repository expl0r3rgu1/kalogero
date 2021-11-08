#!/usr/bin/python3
import praw 
import json

with open("scrapers/reddit_web_scraper/config.json", "r") as file: 
    config = json.load(file)

id = config["client_id"]
secret = config["secret"]
reddit_username = config["reddit_username"]
reddit_password = config["reddit_password"]

reddit = praw.Reddit(
    client_id= id ,
    client_secret = secret,
    password = reddit_password,
    user_agent = "kalogero by" + reddit_username,
    username = reddit_username,
)

print(reddit.user.me())

subreddit = reddit.subreddit("wallstreetbets")

for submission in reddit.subreddit("wallstreetbets").new(limit=5):
    print("Title:", submission.title)
    print("Text:", submission.selftext)
    print("Score:", submission.score)
    print("-----------------------\n")



pass