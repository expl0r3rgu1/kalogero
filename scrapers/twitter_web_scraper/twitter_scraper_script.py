#!/usr/bin/python3

from twitterscraper import query_tweets
import datetime
#test
print(get_symbol_occurencies_in_day("Shiba OR Shiba inu OR SHIB", datetime.date.today()))

def get_symbol_occurencies_in_day(symbol, date):
    occurencies = 0
    
    for tweet in query_tweets(str(symbol), limit=None, begindate=date, enddate=date, poolsize=20):
        occurencies = occurencies + 1

    return occurencies
