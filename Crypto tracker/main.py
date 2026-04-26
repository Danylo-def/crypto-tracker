

#python 3.13.3
#pip install requests

import requests
from datetime import datetime, timedelta #connect datetime

file = open('Crypto tracker/History.txt', 'a')# file open

while True:

# console input
    ques = input ("What coin you want to check? :  ").upper()#input with upper method 

    if ques == "EXIT":
        break

#dictionary
    coin_map = {
"ETH": "ethereum",
"BTC": "bitcoin",
"SOL": "solana",
"ADA": "cardano"
}
#condition to check, if no coin in dic.
    if ques not in coin_map:
        print("Coin not Found")
        exit()

    coin_id = coin_map[ques]

    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"

    response = requests.get(url)
    data = response.json()

#File outcome
    selected_coin = (f"You selected : {ques}") 
    price_value = f"{ques} Price: {data[coin_id]['usd']} USD"
    time_shown = (f"Time: {datetime.now().strftime('%Y %d %b %H:%M:%S')}")

#Output variables in file
    whole = (f"\n{ques} \n {selected_coin} \n {price_value} \n {time_shown}")
    print(whole)
    file.write(whole + '\n')


    file.close()# close file 