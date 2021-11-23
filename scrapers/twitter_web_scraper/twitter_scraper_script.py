#!/usr/bin/python3
import os

def get_symbol_occurrencies_in_day(symbol, date):
    next_day = date.datetime.now() + date.timedelta(days=1)
    os.system("snscrape --json --since " + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d") + " twitter-search \""+ symbol + "until:" + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + next_day.strftime("%d") + "\" > text-query-tweets.json")

#test
print(get_symbol_occurrencies_in_day("SHIB", datetime.date.today()))
