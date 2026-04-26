

#python 3.13.3
#pip install requests

import requests 
from datetime import datetime, timedelta #connect datetime


while True: #loop to not rerun code

# console input
    ques = input ("What coin you want to check? :  ").upper()#input with upper method 

    if ques == "EXIT":#condition if 'exit' --> stop code
        break

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
    

#condition to check, if no coin in dic.
    if ques not in coin_map:
        print("Coin not Found")
        continue

    coin_id = coin_map[ques]

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"#url to choose directly what coin I chose. 

    response = requests.get(url)#import requests from coingecko
    data = response.json()# form it to python 

#condition if API not give the programm will not crash
    try:
        price = data[coin_id]["usd"]
    except KeyError:
        print("API error, try again...")
        continue


#File outcome
    selected_coin = (f"You selected : {ques}") 
    price_value = f"{ques} Price: {price} USD"
    time_shown = (f"Time: {datetime.now().strftime('%Y %d %b %H:%M:%S')}")

#Output variables in file
    whole = (f"\n{ques} \n {selected_coin} \n {price_value} \n {time_shown}")
    print(whole)

    with open('Crypto tracker/History.txt', 'a') as file:
        file.write(whole + '\n')