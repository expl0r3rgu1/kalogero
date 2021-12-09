#!/usr/bin/python3

from typing import Counter
import praw
import json
from datetime import datetime
from datetime import date
import time
import os
from praw.models import subreddits
from prawcore.exceptions import OAuthException


def sameDay(date1, date2):
    if date1.date() == date2.date():
        return True
    else:
        return False


def openFileConfig():
    dir = os.path.dirname(os.path.realpath(__file__))
    try:
        with open(dir + "/config.json", "r") as file:
            config = json.load(file)
            return config
    except FileNotFoundError:
        with open(dir + "/config.json", "w") as file:
            config = {
                "client_id": "",
                "secret": "",
                "reddit_username": "",
                "reddit_password": "", 
                "subreddits": ["", "", ""],
                "symbols" : ["", "", ""]
            }
            json.dump(config, file, indent=4)
            print("file config.json not found. It has been created in " + dir)
            print("please controll it and fill the blank fields")
            exit()
            
def checkConfigOk(config):
    if config["client_id"] == "" or config["secret"] == "" or config["reddit_username"] == "" or config["reddit_password"] == "" or config["subreddits"] == [""]:
        print("ERROR: controll the file config.json and instert the credential \n you can find the file in the path: ")
        print(dir)

        exit()

def checkLogin(reddit): 
    try: 
        reddit.user.me()
    except OAuthException:
        print("login failed, check credentials")
        exit()  

def printOccurences(symbols, symbolsOccurrence):
    print("occurrency of symbols:")
    for idx in enumerate(symbols, start = 0):
        print(idx[1],":", symbolsOccurrence[idx[0]])



#--------------------program starts here---------------------

#--------scarabocchi per trovare la data------------------ 
s = "01/12/2011"
print(time.mktime(datetime.strptime(s, "%d/%m/%Y").timetuple()))

#1322697600.0

firstDate = date(2001,5,4)
print(firstDate)
#----------------------------------------------------------



# open a file called config.json.
config = openFileConfig()

#controll if there are blank field in config.json 
checkConfigOk(config)

# configure the bot
reddit = praw.Reddit(
    client_id =     config["client_id"],
    client_secret=  config["secret"],
    password=       config["reddit_password"],
    username=       config["reddit_username"],
    user_agent=     "kalogero",
)

#if the login fail the program end
checkLogin(reddit)

#initialize variables taking the value from the file config.json
subreddits = config["subreddits"]
symbols = config["symbols"]

#initialize array for saving the result of the occurrency check.
symbolsOccurrence = [] 
for i in range(len(symbols)):
       symbolsOccurrence.append(0)

counter = 0
for subreddit in subreddits:
    print("\n \n \n analizing subreddit:" + subreddit)

    #for submission in reddit.subreddit(subreddit).new():
    #    if not submission.stickied:
    #        firstDate = datetime.utcfromtimestamp(submission.created_utc)
    #        break

    #insert here the code for find the first submission of the chosen day


    for submission in reddit.subreddit(subreddit).new():
        submissionDate = datetime.utcfromtimestamp(submission.created_utc)
        if sameDay(firstDate, submissionDate):
            if not submission.stickied:
                #textcheck contains the title and text of the post in lower case
                textocheck = (submission.title + submission.selftext).lower()
                #count occurrences
                for idx in enumerate(symbols, start = 0):
                    if idx[1] in textocheck:
                        symbolsOccurrence[idx[0]] += 1 
        else: 
            break
    
printOccurences(symbols, symbolsOccurrence)
        
    
