#!/usr/bin/python3
#import os
import snscrape.modules.twitter as sntwitter
import datetime
#import pandas as pd

occurencies = 0

def get_symbol_occurrencies_in_day(symbol, date):
    symbol_occurencies = 0

    next_day = date + datetime.timedelta(days=1)
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(symbol + " since:" + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d") + " until:" + next_day.strftime("%Y") + "-" + next_day.strftime("%m") + "-" + next_day.strftime("%d")).get_items()):
        symbol_occurencies = symbol_occurencies + 1

    return symbol_occurencies
    #os.system("snscrape --jsonl --progress --since " + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d") + " twitter-search \'" + symbol + " " + "until:" + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + next_day.strftime("%d") + "\' > text-query-tweets.json")

    #tweets_df = pd.read_json('text-query-tweets.json', lines=True)

#test
occurencies = occurencies + get_symbol_occurrencies_in_day("SHIB", datetime.date.today())

print(symbol + " occured " + occurencies + " times")
