


#python 3.13.3
#pip install requests
#Will upgrade = w\i

import requests 
from datetime import datetime, timedelta #connect datetime
import time 
import os 

###progress :
# dictionary
## user input
# check coin
# api request
# extract price (if coin typed incorrect)
# clear terminal
# build terminal ui
# save history
# live tracking
# main


#dictionary

coin_map = {
"ETH": "ethereum",
"BTC": "bitcoin",
"SOL": "solana",
"ADA": "cardano",
"XRP": "ripple",
"BNB": "binancecoin",
"TRX": "tron",
"DOGE": "dogecoin",
"BCH": "bitcoin-cash",
"LINK": "chainlink",
"XLM": "stellar",
"LTC": "litecoin",
"AVAX": "avalanche",
"HBAR": "hedera",
"SUI": "sui",
"UNI": "uniswap",
"ARB": "arbitrum",
"APT": "aptos",
}

#user input
def user_input():
    return  input("What coin you want to check? :  ").upper()
user_input()