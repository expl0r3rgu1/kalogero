#!/usr/bin/python3
import snscrape.modules.twitter as sntwitter
import datetime

def get_symbol_occurrencies_in_day(symbol, date):
    #variable to return
    symbol_occurencies = 0
    
    #setting the next_day variable to define a time interval of one day
    next_day = date + datetime.timedelta(days=1)

    #for each tweet found add one to the occurrencies counter
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(symbol + " since:" + date.strftime("%Y") + "-" + date.strftime("%m") + "-" + date.strftime("%d") + " until:" + next_day.strftime("%Y") + "-" + next_day.strftime("%m") + "-" + next_day.strftime("%d")).get_items()):
        symbol_occurencies = symbol_occurencies + 1

    return symbol_occurencies


def get_crypto_occurrencies_in_day(symbol_list, date):
    occurencies = 0

    for symbol in symbol_list:
        occurencies = occurencies + get_symbol_occurrencies_in_day(symbol, date)

    return occurrencies
