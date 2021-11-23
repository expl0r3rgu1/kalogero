#!/usr/bin/python3
import os
import datetime
import pandas as pd

def get_symbol_occurrencies_in_day(symbol, date):
    next_day = date + datetime.timedelta(days=1)
    os.system("snscrape --jsonl --progress --since " + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d") + " twitter-search \'" + symbol + " " + "until:" + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + next_day.strftime("%d") + "\' > text-query-tweets.json")

    tweets_df = pd.read_json('text-query-tweets.json', lines=True)

#test
get_symbol_occurrencies_in_day("SHIB", datetime.date.today())
