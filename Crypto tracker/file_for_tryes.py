


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

#check coin
def check_coin():
    if user_input not in coin_map:
        print("Coin not Found")
        return False
    return True

#API request
def api_get(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    return data

#extract price
def extract_price(coin_id,data):
    try:
        price = data[coin_id]["usd"]
    except KeyError:
        print("API error, try again...")
        return None

#clear terminal 
def clear_console():
    os.system('cls' if os.name == 'nt'else 'clear')

#build terminal components
def build_terminal(ques,price):
    name_project = ("\t CRYPTO TRACKER").upper()
    selected_coin = (f"Coin  : {ques}") 
    price_value = f"Price : {price} USD"
    time_shown = (f"Time  : {datetime.now().strftime('%Y %d %b %H:%M:%S')}")

    whole = (
        f"{"="*30}\n"
        f" {name_project} \n"
        f"{"="* 30} \n"
        f"{selected_coin} \n"
        f"{price_value} \n"
        f"{time_shown}"
        )
    
    whole_2 = (
        f"{"-"* 30}\n"
        f"{'Type CTRL+C to stop'} \n"
        f"{"="*30}"
    )

#save history
def save_history(whole,whole_2):
    with open('Crypto tracker/History.txt', 'a') as file:
        file.write(f"{whole}\n {whole_2} \n")

#