

#python 3.13.3
#pip install requests


from datetime import datetime, timedelta #connect datetime

file = open('Crypto tracker/History.txt', 'a')# file open

# console input
ques = input ("What coin you want to check? :  ").upper()#input with upper method 

#dictionary
price = {
"ETH": 2300,
"BTC": 75000,
"SOL": 85
}
#condition to check, have or not coin in the dictionary
if ques in price:
    price_value = price[ques]
    #continue the programm
else: 
    print("Coin not Found")
    exit()



#File outcome
selected_coin = (f"You selected : {ques}") 
price_value =(f"The Price is : {price[ques]}")
time_shown = (f"Time: {datetime.now().strftime('%Y %d %b %H:%M:%S')}")

#Output variables in file
whole = (f"\n{ques} \n {selected_coin} \n {price_value} \n {time_shown}")
print(whole)
file.write(whole + '\n')


file.close()# close file 